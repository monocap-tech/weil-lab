"""Restore exact native certificate/checkpoint gzip and optional decoded JSON."""
import base64,gzip,hashlib,json
from pathlib import Path

def restore():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    manifest=json.loads((root/'RPB108_PRIME7_NATIVE96_0973_CUSTODY_20261007.json').read_text())
    for name,meta in manifest['archives'].items():
        raw=base64.b64decode((root/meta['transport_file']).read_text().strip(),validate=True)
        assert hashlib.sha256(raw).hexdigest()==meta['gzip_sha256']
        decoded=gzip.decompress(raw)
        assert hashlib.sha256(decoded).hexdigest()==meta['decoded_sha256']
        outputs={name:raw}
        if meta.get('write_decoded_file'):outputs[meta['write_decoded_file']]=decoded
        for path,value in outputs.items():
            target=root/path
            if target.exists():assert target.read_bytes()==value
            else:target.write_bytes(value)
        print(name,'verified')

if __name__=='__main__':restore()
