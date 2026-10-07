"""Restore exact hash-bound complete 112-vector native and source archives."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    m=json.loads((root/'RPB108_PRIME7_NATIVE_SOURCE112_099_CUSTODY_20261007.json').read_bytes())
    for name,e in m['archives'].items():
        raw=base64.b64decode(''.join((root/p).read_text().strip() for p in e['transport_files']),validate=True)
        assert hashlib.sha256(raw).hexdigest()==e['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(raw)).hexdigest()==e['decoded_sha256']
        p=root/name
        if p.exists():assert p.read_bytes()==raw
        else:p.write_bytes(raw)
        print(name,'verified')

if __name__=='__main__':restore()
