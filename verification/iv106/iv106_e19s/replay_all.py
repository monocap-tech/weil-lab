#!/usr/bin/env python3
"""Authenticate all frozen inputs, replay accepted arithmetic in a temporary
copy, verify exact output hashes. Install numpy==2.3.5 and scipy==1.17.0.
This does not establish the conditional analytic or Lean dependencies."""
import hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
p=Path(__file__).resolve().parent
m=json.loads((p/'custody_manifest.json').read_text())
root=p.parent
def check(base,items):
    for row in items:
        f=base/row['path']
        data=f.read_bytes()
        assert hashlib.sha256(data).hexdigest()==row['sha256'],f
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['git_blob'],f
check(root,m['files'])
print('AUTHENTICATED',len(m['files']),flush=True)
with tempfile.TemporaryDirectory(prefix='iv106-e19s-') as d:
    d=Path(d)
    for row in m['files']:
        out=d/row['path']
        out.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(root/row['path'],out)
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1')
    for args in [['iv106_e19o/certify_row.py','iv106_e19n/row_pilot.json'],['iv106_e19p/certify_bank.py'],['iv106_e19q/joint.py'],['iv106_e19r/remaining_reserves.py']]:
        subprocess.run([sys.executable,*args],cwd=d,env=env,check=True)
    check(d,[row for row in m['files'] if row['path'] in m['replayed_outputs']])
    print('BYTE-IDENTICAL OUTPUTS',len(m['replayed_outputs']),flush=True)
