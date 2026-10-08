"""Publish complete CC18 matrices in individually recoverable gzip parts."""
import json,gzip,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'notes/data'
MATRICES=['whole_odd_native_chart','full_original_native_projection_rows','full_source_proxy_gram','full_actual_source_gram_enclosure','full_actual_F112_residual_gram','whole_trial_native_matrix','whole_trial_retained_native_cross','whole_defect_matrix','whole_defect_source_cross','whole_odd_schur_lower','whole_odd_deterministic_lower']

def pack(d):
 d=dict(d);archives={}
 for name in MATRICES:
  matrix=d.pop(name);parts=[]
  # Split projection rows; all other matrices already fit individually.
  size=36 if name=='full_original_native_projection_rows' else len(matrix)
  for i in range(0,len(matrix),size):
   rows=matrix[i:i+size];raw=(json.dumps(rows,indent=2)+'\n').encode();compressed=gzip.compress(raw,mtime=0)
   path=f'RPB108_ODD_FRAME_CC18_{name.upper()}_{i//size}_20261008.json.gz';(BASE/path).write_bytes(compressed)
   assert len(compressed)<1_000_000,('archive must be recoverable',path,len(compressed))
   parts.append({'path':path,'row_start':i,'row_count':len(rows),'gzip_bytes':len(compressed),'gzip_sha256':hashlib.sha256(compressed).hexdigest(),'decoded_sha256':hashlib.sha256(raw).hexdigest()})
  archives[name]={'parts':parts,'row_count':len(matrix),'column_count':len(matrix[0]),'concatenate_rows':True}
 d['matrix_archives']=archives;d['complete_matrix_data_split_without_omission']=True
 raw=(json.dumps(d,indent=2)+'\n').encode();assert len(raw)<1_000_000
 (BASE/'RPB108_ODD_FRAME_CC18_CERTIFICATE_20261008.json').write_bytes(raw)
 return d

if __name__=='__main__':
 p=BASE/'RPB108_ODD_FRAME_CC18_CERTIFICATE_20261008.json';d=json.loads(p.read_bytes())
 if 'matrix_archives' in d:
  for name,record in d['matrix_archives'].items():
   d[name]=[]
   for part in record['parts']:
    data=(BASE/part['path']).read_bytes();assert hashlib.sha256(data).hexdigest()==part['gzip_sha256'];d[name]+=json.loads(gzip.decompress(data))
  del d['matrix_archives']
 packed=pack(d);print(json.dumps({'matrix_parts':sum(len(x['parts']) for x in packed['matrix_archives'].values()),'main_bytes':p.stat().st_size,'maximum_archive_bytes':max(p['gzip_bytes'] for x in packed['matrix_archives'].values() for p in x['parts'])}))
