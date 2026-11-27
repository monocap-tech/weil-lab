from pathlib import Path
import hashlib,json,numpy as np
p=Path(__file__).resolve().parent
m=json.loads((p/'freeze_manifest.json').read_text())
old=json.loads((p/'pilot_result.json').read_text())
assert len(m['files'])==7
assert {row['raw_sha256'] for row in m['files']}=={row['coefficient_sha256'] for row in old['rows']}
for row in m['files']:
    b=(p/row['path']).read_bytes()
    assert len(b)==row['bytes']
    assert hashlib.sha256(b).hexdigest()==row['sha256']
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob']
    a=np.load(p/row['path'],allow_pickle=False)
    assert a.dtype.str=='<i8' and a.ndim==1
    assert hashlib.sha256(a.tobytes()).hexdigest()==row['raw_sha256']
print('PASS: 7/7 exact original coefficient arrays')
