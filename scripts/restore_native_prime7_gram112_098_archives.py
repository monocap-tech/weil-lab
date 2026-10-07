"""Restore complete compressed and decoded hash-bound Gram archives."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    m=json.loads((root/'RPB108_PRIME7_GRAM112_098_CUSTODY_20261007.json').read_text())
    for name,entry in m['archives'].items():
        text=''.join((root/p).read_text().strip() for p in entry['transport_files'])
        raw=base64.b64decode(text,validate=True)
        assert hashlib.sha256(raw).hexdigest()==entry['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(raw)).hexdigest()==entry['decoded_sha256']
        p=root/name
        if p.exists():assert p.read_bytes()==raw
        else:p.write_bytes(raw)
        print(name,'verified')

if __name__=='__main__':restore()
