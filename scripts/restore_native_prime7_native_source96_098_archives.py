"""Restore compressed and decoded hash-bound native/source transports."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    manifest=json.loads((root/'RPB108_PRIME7_NATIVE_SOURCE96_098_CUSTODY_20261007.json').read_text())
    for name,entry in manifest['archives'].items():
        transport=''.join((root/p).read_text().strip() for p in entry['transport_files'])
        raw=base64.b64decode(transport,validate=True)
        assert hashlib.sha256(raw).hexdigest()==entry['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(raw)).hexdigest()==entry['decoded_sha256']
        target=root/name
        if target.exists():assert target.read_bytes()==raw
        else:target.write_bytes(raw)
        print(name,'verified')

if __name__=='__main__':restore()
