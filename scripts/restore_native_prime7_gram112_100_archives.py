"""Restore exact complete 1 Gram/checkpoint archives with pinned identities."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]
    manifest=json.loads((root/'notes/data/RPB108_PRIME7_GRAM112_100_CUSTODY_20261007.json').read_bytes())
    restored={}
    for key,record in manifest['archives'].items():
        pieces=[]
        for path in record['parts']:
            raw=(root/path).read_bytes()
            assert hashlib.sha256(raw).hexdigest()==manifest['files'][path]['sha256']
            pieces.append(raw.strip())
        compressed=base64.b64decode(b''.join(pieces),validate=True)
        assert hashlib.sha256(compressed).hexdigest()==record['compressed_sha256']
        raw=gzip.decompress(compressed)
        assert hashlib.sha256(raw).hexdigest()==record['decoded_sha256']
        for path in [record['decoded_path']]+record['identical_alias_paths']:
            target=root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
        restored[key]=record['decoded_sha256']
    return restored

if __name__=='__main__':print(json.dumps(restore(),indent=2))
