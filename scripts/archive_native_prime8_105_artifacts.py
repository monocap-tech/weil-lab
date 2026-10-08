"""Deterministic gzip custody for large target artifacts; exact repeat aliases only."""
import gzip,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def archive(paths,aliases=None):
 records=[];stored=[]
 for name in paths:
  p=ROOT/name;raw=p.read_bytes();assert raw
  if len(raw)<=55000 and not raw.startswith(b'\x1f\x8b'):
   stored.append(name);continue
  gz=raw.startswith(b'\x1f\x8b');archive_name=name if gz else name+'.gz'
  compressed=raw if gz else gzip.compress(raw,mtime=0)
  (ROOT/archive_name).write_bytes(compressed);stored.append(archive_name)
  records.append({'local_path':name,'archive_path':archive_name,'transport':'existing-gzip' if gz else 'gzip',
    'restored_size':len(raw),'restored_sha256':hashlib.sha256(raw).hexdigest(),'compressed_sha256':hashlib.sha256(compressed).hexdigest()})
 aliases=aliases or {}
 for a,b in aliases.items():assert (ROOT/a).read_bytes()==(ROOT/b).read_bytes()
 out={'version':2,'aperture':'21/20','records':records,'repeat_aliases':aliases}
 (ROOT/'notes/data/RPB108_PRIME8_105_TRANSPORT_MANIFEST_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 return stored
if __name__=='__main__':
 import sys
 print(json.dumps(archive(sys.argv[1:]),indent=2))
