#!/usr/bin/env python3
"""Verify the three original Library archives before literal NF46 replay.

Never regenerates or substitutes a native input. Reads only the supplied
original gzip bytes; hashes are over their decompressed JSON payloads.
The historical certifier and validator are executed without monkey-patching.
"""
import argparse
import gzip
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = {
    'native112_N720_K620.json.gz': 'f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81',
    'native_boundary_columns_112_113.json.gz': 'da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee',
    'native_boundary_114_115.json.gz': '0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad',
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, default=ROOT/'nf24-inputs/Weil')
    parser.add_argument('--output-directory', type=Path, default=ROOT/'work/nf46-original-replay')
    parser.add_argument('--replay-selection', action='store_true', help='Also reconstruct the NF46 choose output against the frozen trial')
    args = parser.parse_args()
    missing = [str(args.inputs/name) for name in ARCHIVES if not (args.inputs/name).is_file()]
    if missing:
        print(json.dumps(dict(status='BLOCKED_MISSING_ORIGINAL_NATIVE_ARCHIVES', missing=missing), indent=2))
        return 2
    verified = []
    for name, expected in ARCHIVES.items():
        path = args.inputs/name
        compressed = path.read_bytes()
        raw = gzip.decompress(compressed)
        actual = digest(raw)
        if actual != expected:
            raise ValueError(f'Original archive custody mismatch: {name}; got {actual}, expected {expected}')
        payload = json.loads(raw)
        if payload.get('aperture') != '53/50':
            raise ValueError(f'Wrong original aperture in {name}')
        verified.append(dict(name=name, uncompressed_sha256=actual, compressed_sha256=digest(compressed)))
    # Only after ALL originals are verified may any historical computation
    # start. Install their unchanged bytes if the supplied source is elsewhere.
    destination = ROOT/'nf24-inputs/Weil'
    destination.mkdir(parents=True, exist_ok=True)
    for name in ARCHIVES:
        target = destination/name
        source = args.inputs/name
        if target.resolve() != source.resolve():
            if target.exists():
                if target.read_bytes() != source.read_bytes():
                    raise ValueError(f'Refusing to overwrite different frozen archive: {target}')
            else:
                shutil.copyfile(source, target)
    out = args.output_directory
    out.mkdir(parents=True, exist_ok=True)
    trial = ROOT/'notes/data/RPB108_NF46_EVEN_FIXED_NEXT_SHELL_20261009.json'
    results = []
    def execute(name, command, expected, generated):
        print(f'Running unchanged historical NF46 {name}', flush=True)
        with (out/(name+'.log')).open('w') as log:
            subprocess.run([sys.executable]+command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
        actual = generated.read_bytes()
        original = expected.read_bytes()
        if actual != original:
            raise ValueError(f'Fresh historical {name} output differs from frozen bytes; inspect {generated}')
        results.append(dict(stage=name, status='PASS_BYTE_IDENTICAL', output_sha256=digest(actual)))
    if args.replay_selection:
        selected = out/'NF46_fixed_next_shell.json'
        execute('selection', ['scripts/certify_native_next_shell_nf46_106.py', 'choose', '--parity', 'even', '--output', str(selected)], trial, selected)
    certificate = out/'NF46_next_shell_certificate.json'
    execute('certification', ['scripts/certify_native_next_shell_nf46_106.py', 'certify', '--trial', str(trial), '--output', str(certificate)], ROOT/'notes/data/RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json', certificate)
    validation = out/'NF46_next_shell_validation.json'
    execute('independent_validation', ['scripts/validate_native_next_shell_nf46_106.py', '--output', str(validation)], ROOT/'notes/data/RPB108_NF46_NEXT_SHELL_VALIDATION_20261009.json', validation)
    report = dict(milestone='NF47', status='PASS', original_archive_hashes=verified, fresh_NF46_replay=results,
                  original_archives_regenerated_or_substituted=False, whole_aperture_positive=False)
    (out/'replay_manifest.json').write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps(report, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
