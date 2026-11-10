"""Prepare a local PDF ZIP and SHA-256 manifests. Does not upload anything."""
import argparse
import hashlib
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def sha256(file):
    with file.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def entry(name):
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extra-pdf', type=Path, action='append', default=[], help='Existing release PDF, already downloaded and verified')
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    pdfs = sorted([*ROOT.glob('*.pdf'), *args.extra_pdf], key=lambda p: p.name)
    if not pdfs or any(not p.is_file() or p.suffix.lower() != '.pdf' for p in pdfs):
        raise SystemExit('All inputs must be existing PDFs.')
    names = [p.name for p in pdfs]
    if len(names) != len(set(names)):
        raise SystemExit('PDF filenames must be unique.')
    for file in pdfs:
        with file.open('rb') as stream:
            if stream.read(5) != b'%PDF-':
                raise SystemExit(f'Input does not have a PDF header: {file.name}')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive = args.output_dir / 'cpsa-study-materials.zip'
    manifest = ''.join(f'{sha256(p)}  {p.name}\n' for p in pdfs)
    (args.output_dir / 'PDF-SHA256SUMS.txt').write_text(manifest, encoding='utf-8', newline='\n')
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for file in pdfs:
            with file.open('rb') as src, bundle.open(entry(file.name), 'w', force_zip64=True) as dst:
                shutil.copyfileobj(src, dst, length=1024 * 1024)
        bundle.writestr(entry('PDF-SHA256SUMS.txt'), manifest.encode('utf-8'))
    # Read every member back: check archive CRCs and SHA-256 against source bytes.
    expected = {p.name: sha256(p) for p in pdfs}
    with zipfile.ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise SystemExit('ZIP CRC validation failed.')
        if set(bundle.namelist()) != {*names, 'PDF-SHA256SUMS.txt'}:
            raise SystemExit('Unexpected ZIP member inventory.')
        for name, digest in expected.items():
            with bundle.open(name) as member:
                if hashlib.file_digest(member, 'sha256').hexdigest() != digest:
                    raise SystemExit(f'Archived PDF differs from its source: {name}')
        if bundle.read('PDF-SHA256SUMS.txt') != manifest.encode('utf-8'):
            raise SystemExit('Internal manifest differs from the expected manifest.')
    zip_hash = sha256(archive)
    all_hashes = manifest + f'{zip_hash}  {archive.name}\n'
    (args.output_dir / 'SHA256SUMS.txt').write_text(all_hashes, encoding='utf-8', newline='\n')
    (args.output_dir / 'cpsa-study-materials.zip.sha256').write_text(f'{zip_hash}  {archive.name}\n', encoding='utf-8', newline='\n')
    print(f'PASS: {len(pdfs)} PDFs, ZIP CRCs, per-PDF SHA-256 readback, and internal manifest.')
    print(f'ZIP: {archive.stat().st_size:,} bytes')
    print(f'SHA-256: {zip_hash}')
    print(f'Prepared locally in {args.output_dir.resolve()}; nothing uploaded.')


if __name__ == '__main__':
    main()
