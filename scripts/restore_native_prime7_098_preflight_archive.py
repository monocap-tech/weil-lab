"""Restore the hash-bound prime majorant transport."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    m=json.loads((root/'RPB108_PRIME7_098_PREFLIGHT_CUSTODY_20261007.json').read_text())
    name=m['archive_file'];raw=base64.b64decode((root/(name+'.base64')).read_text().strip(),validate=True)
    assert hashlib.sha256(raw).hexdigest()==m['archive_gzip_sha256']
    assert hashlib.sha256(gzip.decompress(raw)).hexdigest()==m['archive_decoded_sha256']
    target=root/name
    if target.exists():assert target.read_bytes()==raw
    else:target.write_bytes(raw)
    print(name,'verified')

if __name__=='__main__':restore()
