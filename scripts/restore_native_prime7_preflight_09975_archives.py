"""Restore the pinned exact prime-majorant input at aperture 399/400."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    manifest=json.loads((root/'RPB108_PRIME7_PREFLIGHT_09975_CUSTODY_20261007.json').read_bytes())
    archive=manifest['archive']
    parts=[]
    for name in archive['parts']:
        raw=(root/name).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==manifest['files']['notes/data/'+name]['sha256']
        parts.append(raw.strip())
    compressed=base64.b64decode(b''.join(parts),validate=True)
    assert hashlib.sha256(compressed).hexdigest()==archive['compressed_sha256']
    decoded=gzip.decompress(compressed)
    assert hashlib.sha256(decoded).hexdigest()==archive['decoded_sha256']
    (root/archive['compressed_name']).write_bytes(compressed)
    (root/archive['decoded_name']).write_bytes(decoded)
    (root/archive['fresh_repeat_alias']).write_bytes(decoded)
    return archive['decoded_sha256']

if __name__=='__main__':print(restore())
