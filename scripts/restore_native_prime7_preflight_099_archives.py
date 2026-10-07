"""Restore compressed and decoded hash-bound prime majorant archive at 99/100."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    m=json.loads((root/'RPB108_PRIME7_PREFLIGHT_099_CUSTODY_20261007.json').read_text())
    for name,e in m['archives'].items():
        b=base64.b64decode(''.join((root/p).read_text().strip() for p in e['transport_files']),validate=True)
        assert hashlib.sha256(b).hexdigest()==e['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(b)).hexdigest()==e['decoded_sha256']
        p=root/name
        if p.exists():assert p.read_bytes()==b
        else:p.write_bytes(b)
        print(name,'verified')

if __name__=='__main__':restore()
