"""Outward rational recheck of the saved actual corrected Schur matrix."""
from pathlib import Path
import json,hashlib,sys,base64,gzip
from certify_native_legendre_small_window import F,I
class PivotFailure(Exception):
 def __init__(self,k,p):self.k,self.p=k,p
def positive_pivots(matrix):
 m=[row[:]for row in matrix];pivots=[]
 for k in range(len(m)):
  pivot=m[k][k]
  if pivot.lo<=0:raise PivotFailure(k,pivot)
  pivots.append(pivot)
  for i in range(k+1,len(m)):
   for j in range(i,len(m)):
    m[i][j]=m[i][j]-m[i][k]*m[k][j]/pivot
    m[j][i]=m[i][j]
 return pivots
I.grid=10**100
r=Path(__file__).resolve().parents[1]/'notes/data';c=json.loads((r/'RPB108_PRIME7_SCHUR112_100_CERTIFICATE_20261007.json').read_text())
names={'native':'RPB108_PRIME7_MATRIX112_100_COMPACT80_20261007.json',
       'gram':'RPB108_PRIME7_GRAM112_100_CERTIFICATE_20261007.json'}
d={}
for key,name in names.items():
 target=r/name
 if not target.exists():
  stem=name+('.transport.b64' if key=='native' else '.gz.b64')
  parts=sorted(r.glob(stem+'.part*'))
  if not parts:raise FileNotFoundError('Missing saved archive: '+stem)
  transport=base64.b64decode(b''.join(p.read_bytes().strip() for p in parts),validate=True)
  raw=gzip.decompress(transport)
  assert hashlib.sha256(raw).hexdigest()==c['input_sha256'][key]
  target.write_bytes(raw)
for key,name in names.items():
 raw=(r/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==c['input_sha256'][key]
 d[key]=json.loads(raw)
Q=[[None]*112 for _ in range(112)];k=0
for i in range(112):
 for j in range(i+1):
  Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in d['native']['lower_triangle_row_major'][k]));k+=1
beta=F(c['complement_inverse_factor']);delta=F(c['actual_gram_operator_error_upper'])
R=[[I(F(lo),F(hi))for lo,hi in row]for row in d['gram']['residual_gram_surrogate']]
assert all((R[i][j].lo,R[i][j].hi)==(R[j][i].lo,R[j][i].hi) for i in range(112) for j in range(112))
odd=max(sum((max(abs((Q[i][j]-beta*R[i][j]).lo),abs((Q[i][j]-beta*R[i][j]).hi))for j in range(112)if (i+j)%2),F(0))for i in range(112))
tau=F(sys.argv[1]);result={'tau':str(tau),'grid_digits':100,'input_hashes_verified':True,'odd_parity_operator_budget':str(odd),'blocks':[]}
for p in [0,1]:
 ids=list(range(p,112,2))
 G=[[Q[i][j]-beta*R[i][j]-(beta*delta+tau+odd if i==j else 0)for j in ids]for i in ids]
 try:
  pivots=positive_pivots(G)
  result['blocks'].append({'parity':p,'passed':True,'pivot_lowers':list(str(x.lo)for x in pivots)})
 except PivotFailure as fail:
  result['blocks'].append({'parity':p,'passed':False,'failed_pivot_index':fail.k,
                          'failed_pivot_lower':str(fail.p.lo),'failed_pivot_upper':str(fail.p.hi),
                          'negative_upper':fail.p.hi<0})
  break
 print(json.dumps({'parity':p,'passed':result['blocks'][-1]['passed']}),flush=True)
result['passed']=len(result['blocks'])==2 and all(x['passed']for x in result['blocks'])
(Path(sys.argv[2]) if len(sys.argv)>2 else r/('RPB108_PRECONTACT_SCHUR_MARGIN_'+str(tau.denominator)+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='blocks'}),flush=True)
