"""Restore hash-pinned complete native/source inputs and saved columns at 1."""
import base64,gzip,hashlib,io,json,tarfile
from pathlib import Path

def restore(rebuild_columns=False):
    root=Path(__file__).resolve().parents[1]
    manifest=json.loads((root/'notes/data/RPB108_PRIME7_NATIVE_SOURCE112_100_CUSTODY_20261007.json').read_bytes())
    results={}
    for key,record in manifest['archives'].items():
        parts=[]
        for path in record['parts']:
            raw=(root/path).read_bytes()
            assert hashlib.sha256(raw).hexdigest()==manifest['files'][path]['sha256']
            parts.append(raw.strip())
        compressed=base64.b64decode(b''.join(parts),validate=True)
        assert hashlib.sha256(compressed).hexdigest()==record['transport_sha256']
        raw=gzip.decompress(compressed) if record['transport']=='gzip' else compressed
        assert hashlib.sha256(raw).hexdigest()==record['decoded_sha256']
        target=root/record['decoded_path'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
        results[key]=record['decoded_sha256']
    if rebuild_columns:
        import certify_native_prime7_source112_100 as source
        saved=manifest['saved_columns'];folder=root/saved['folder']
        rebuilt=source.certificate(str(folder))
        primary=json.loads((root/manifest['archives']['source']['decoded_path']).read_bytes())
        assert rebuilt==primary
        for name,digest in saved['column_sha256'].items():
            assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest
        results['saved_columns_reconstructed']=True
    return results

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--rebuild-columns',action='store_true')
    args=parser.parse_args();print(json.dumps(restore(args.rebuild_columns),indent=2))
