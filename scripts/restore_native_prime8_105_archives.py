"""Restore target data from exact gzip Git blobs and byte-identical repeat aliases."""
import gzip,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'notes/data/RPB108_PRIME8_105_TRANSPORT_MANIFEST_20261008.json').read_bytes())
assert m['version']==2 and m['aperture']=='21/20'
for row in m['records']:
 b=(ROOT/row['archive_path']).read_bytes();assert hashlib.sha256(b).hexdigest()==row['compressed_sha256']
 raw=b if row['transport']=='existing-gzip' else gzip.decompress(b)
 assert len(raw)==row['restored_size'] and hashlib.sha256(raw).hexdigest()==row['restored_sha256']
 p=ROOT/row['local_path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
for alias,original in m['repeat_aliases'].items():
 (ROOT/alias).write_bytes((ROOT/original).read_bytes())
print(json.dumps({'restored_records':len(m['records']),'repeat_aliases':len(m['repeat_aliases']),'aperture':'21/20'}))
