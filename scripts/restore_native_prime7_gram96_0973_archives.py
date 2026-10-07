"""Restore and verify the complete eleven-panel Gram and contraction archives."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    manifest=json.loads((root/'RPB108_PRIME7_GRAM96_0973_CUSTODY_20261007.json').read_text())
    for item in manifest['archives']:
        raw=b''.join(base64.b64decode((root/name).read_text().strip(),validate=True) for name in item['transport_parts'])
        assert hashlib.sha256(raw).hexdigest()==item['gzip_sha256']
        decoded=gzip.decompress(raw)
        assert hashlib.sha256(decoded).hexdigest()==item['decoded_sha256']
        target=root/item['archive_file']
        if target.exists():assert target.read_bytes()==raw
        else:target.write_bytes(raw)
        print(item['archive_file'],'verified')

if __name__=='__main__':restore()
