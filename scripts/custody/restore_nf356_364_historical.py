#!/usr/bin/env python3
"""Restore NF356--364 *historical* 49-file custody package without overwrite.

The archived output has provisional provenance only. This script checks
SHA-pinned parent Action ZIPs, exact historical per-file SHA, and an xz-packed
46-file transfer payload. It does NOT accept a mathematical theorem.
"""
import argparse
import base64
import hashlib
import io
import json
import lzma
import pathlib
import tarfile
import zipfile

PAYLOAD = 'notes/data/provisional/transfer/NF356-364_NONPARENT_PAYLOAD.tar.xz.b64'
PAYLOAD_SHA = '0a62aae0307b37c5ef1d13ce13a608dbf5699e3b4ee2d00569a2be303a3e507f'
MANIFEST_SHA = 'ba22fbea27c06c6725807d906e5af1ddfd96026bae3d6e679238b02ed52f05ed'
FULL_HISTORICAL_ZIP_SHA = '18a70ff301da621a9aaaaa420922a544f17e46a5f905947d6433932c962fa1fc'
PARENTS = [
    ('nf361-pr348-fourmode.zip', 12738593751,
     '735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968',
     'original_four_mode_critical_block.json',
     'notes/data/provisional/parents/pr348_original_four_mode_critical_block.json'),
    ('pr350-certificate.zip', 12770022548,
     '3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09',
     'original_BS_pruned_rank_bound.json',
     'notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json'),
    ('pr355-exterior.zip', 12776684037,
     'f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0',
     'original_exterior_scalar_floor_stop.json',
     'notes/data/provisional/parents/pr355_original_exterior_scalar_floor_stop.json'),
]


def digest(b):
    return hashlib.sha256(b).hexdigest()


def safe_path(path):
    p = pathlib.PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or '.' in p.parts or str(p) != path:
        raise ValueError(f'Unsafe archive path: {path!r}')
    if not (path.startswith('notes/') or path.startswith('scripts/local_replay/') or
            path == '.github/workflows/provisional-nf356-364-custody.yml'):
        raise ValueError(f'Unrecognized custody path: {path!r}')
    return path


def historical_bytes(source_dir, artifacts_dir):
    encoded = (source_dir / PAYLOAD).read_bytes()
    payload = base64.b64decode(encoded, validate=True)
    assert digest(payload) == PAYLOAD_SHA, 'Nonparent payload checksum mismatch'
    assert lzma.is_check_supported(lzma.CHECK_CRC64)
    untarred = lzma.decompress(payload)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(untarred), mode='r:') as z:
        names = z.getmembers()
        assert len(names) == 46
        for info in names:
            assert info.isfile(), info.name
            path = safe_path(info.name)
            assert path not in files, path
            files[path] = z.extractfile(info).read()
    assert len(files) == 46
    parent_metadata = []
    for archive_name, artifact_id, zip_hash, src_name, target in PARENTS:
        raw = (artifacts_dir / archive_name).read_bytes()
        assert digest(raw) == zip_hash, f'Parent artifact SHA mismatch: {archive_name}'
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            child = z.read(src_name)
        files[target] = child
        parent_metadata.append({
            'name': archive_name, 'artifact_id': artifact_id,
            'zip_sha256': zip_hash, 'snapshot_path': target,
            'snapshot_sha256': digest(child),
        })
    assert len(files) == 49
    manifest_bytes = files['notes/data/provisional/NF356-364_SHA256_MANIFEST.json']
    assert digest(manifest_bytes) == MANIFEST_SHA, 'Historical manifest changed'
    m = json.loads(manifest_bytes)
    assert m['active_obligation'] == 'W-ODD-NEG' and m['status'] == 'OPEN'
    assert len(m['records']) == 48
    listed = set()
    for row in m['records']:
        name = safe_path(row['path'])
        assert name in files and name not in listed, name
        listed.add(name)
        assert len(files[name]) == row['size'], f'Historical size conflict: {name}'
        assert digest(files[name]) == row['sha256'], f'Historical SHA conflict: {name}'
    assert set(files) == listed | {'notes/data/provisional/NF356-364_SHA256_MANIFEST.json'}
    return files, parent_metadata


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source', type=pathlib.Path, default=pathlib.Path('.'))
    p.add_argument('--destination', type=pathlib.Path, default=pathlib.Path('.'))
    p.add_argument('--artifacts-dir', required=True, type=pathlib.Path)
    p.add_argument('--verify-only', action='store_true')
    args = p.parse_args()
    source = args.source.resolve()
    dest = args.destination.resolve()
    files, parent_metadata = historical_bytes(source, args.artifacts_dir.resolve())
    new, same = [], []
    for name, content in sorted(files.items()):
        target = dest / name
        if target.exists():
            if not target.is_file() or target.read_bytes() != content:
                raise RuntimeError(f'REFUSING TO OVERWRITE DIFFERENT FILE: {name}')
            same.append(name)
        else:
            new.append(name)
    if not args.verify_only:
        for name in new:
            target = dest / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(files[name])
    receipt = {
        'status': 'HISTORICAL_BYTE_CUSTODY_RESTORED__NOT_MATHEMATICAL_ACCEPTANCE',
        'original_49_file_zip_sha256_locally_verified': FULL_HISTORICAL_ZIP_SHA,
        'transfer_payload_xz_sha256': PAYLOAD_SHA,
        'manifest_sha256': MANIFEST_SHA,
        'historical_file_count': 49, 'manifest_record_count': 48,
        'parent_artifacts': parent_metadata,
        'new_paths': new, 'identical_paths': same,
        'current_pr_newer_results_overwritten': False,
        'native_arb_recomputed': False,
        'W_ODD_NEG': 'OPEN', 'RH': 'OPEN',
    }
    if not args.verify_only:
        out = dest / 'notes/data/provisional/NF356-364_RECONCILIATION_RECEIPT.json'
        if out.exists():
            previous = json.loads(out.read_text())
            # A second invocation may be fully identical, with no new paths.
            assert previous['manifest_sha256'] == MANIFEST_SHA
            assert previous['transfer_payload_xz_sha256'] == PAYLOAD_SHA
        else:
            out.write_text(json.dumps(receipt, indent=2) + '\n')
    print(f"PASS exact historical custody: 49 files; new {len(new)}; already identical {len(same)}")
    print('Parent SHA256: ', [v['zip_sha256'] for v in parent_metadata])
    print('Historical mathematical standing: PROVISIONAL; W-ODD-NEG OPEN')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()