#!/usr/bin/env python3
"""Audit byte custody of the provisional stage. No proof-status inference."""
from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parents[2]
M=ROOT/'notes/data/provisional/NF356-364_SHA256_MANIFEST.json'
obj=json.loads(M.read_text())
assert obj['active_obligation']=='W-ODD-NEG' and obj['status']=='OPEN'
for row in obj['records']:
    p=ROOT/row['path']
    assert p.is_file(),p
    data=p.read_bytes()
    assert len(data)==row['size'],p
    assert hashlib.sha256(data).hexdigest()==row['sha256'],p
print('PASS',len(obj['records']),'provisional SHA256 files; NO theorem acceptance')
