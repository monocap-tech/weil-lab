"""Same completed intervals, reordered positive-pivot tests; no enlarged data."""
import gzip,json
from pathlib import Path
from math import isqrt
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_matrix112_checkpoint import load
p=Path('notes/data/RPB108_PRIME8_RAW112_105_ORDERS420_CHECKPOINT_20261008.json.gz');s=json.loads(gzip.decompress(p.read_bytes()))
I.grid=10**400;done,m=load(p,s['bindings']);assert done==112
q=[]
for i in range(112):
 row=[]
 for j in range(112):
  n=isqrt((2*i+1)*(2*j+1)*I.grid**2);row.append(I(F(n,I.grid),F(n+1,I.grid))*m[i][j]/F(21,10))
 q.append(row)
I.grid=10**160
Q=[[I(x.lo,x.hi) for x in row]for row in q]
out=[]
for name in ['descending','diagonal-descending']:
 allpass=True
 for parity in [0,1]:
  d=list(range(parity,112,2))
  if name=='descending':d.reverse()
  else:d.sort(key=lambda i:Q[i][i].lo,reverse=True)
  try:r=positive_pivots([[Q[i][j] for j in d]for i in d]);passed=True
  except ArithmeticError:passed=False;allpass=False
  out.append({'ordering':name,'parity':parity,'passed':passed,'degrees':d})
 print(json.dumps({'ordering':name,'all_native_pivots_pass':allpass}),flush=True)
Path('notes/data/RPB108_PRIME8_PIVOT_ORDER_105_PROBE_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
