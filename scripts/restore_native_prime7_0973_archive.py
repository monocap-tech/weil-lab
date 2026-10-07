"""Decode and verify the UTF-8 transport of the prime-7 weighted certificate."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    name='RPB108_PRIME7_WEIGHTED_POINTWISE_0973_CERTIFICATE_20261007.json.gz'
    encoded=root/(name+'.base64')
    raw=base64.b64decode(encoded.read_text().strip(),validate=True)
    manifest=json.loads((root/'RPB108_PRIME7_0973_PREFLIGHT_CUSTODY_20261007.json').read_text())
    assert hashlib.sha256(raw).hexdigest()==manifest['weighted_gzip_sha256']
    assert hashlib.sha256(gzip.decompress(raw)).hexdigest()==manifest['weighted_decoded_sha256']
    target=root/name
    if target.exists():assert target.read_bytes()==raw
    else:target.write_bytes(raw)
    print(name,'verified')

if __name__=='__main__':restore()
