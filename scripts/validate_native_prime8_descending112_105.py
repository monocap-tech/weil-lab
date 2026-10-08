"""Independent raw normalization and widened descending-parity shifted sign audit."""
import gzip,hashlib,json
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
from certify_native_legendre_small_window import I,positive_pivots
root=Path('notes/data')
p=root/'RPB108_PRIME8_MATRIX112_105_DESCENDING_CERTIFICATE_20261008.json';r=p.read_bytes();c=json.loads(r)
rp=root/'RPB108_PRIME8_MATRIX112_105_DESCENDING_REPEAT_20261008.json';assert r==rp.read_bytes()
raw=(root/'RPB108_PRIME8_RAW112_105_ORDERS420_CHECKPOINT_20261008.json.gz').read_bytes();s=json.loads(gzip.decompress(raw))
assert c['complete_raw_checkpoint_sha256']==hashlib.sha256(raw).hexdigest()
assert s['completed_rows']==112 and s['bindings']['aperture']=='21/20' and s['bindings']['bernoulli_pairs']==420
assert c['pivot_order']=='descending even degrees, then descending odd degrees; exact parity decomposition'
for name,h in s['bindings']['scripts'].items():assert hashlib.sha256((Path('scripts')/name).read_bytes()).hexdigest()==h
G=10**400
q=lambda lo,hi:(F((lo*G).__floor__(),G),F((hi*G).__ceil__(),G))
def mul(a,b):
 v=[x*y for x in a for y in b];return q(min(v),max(v))
inverse=q(F(10,21),F(10,21));index=checks=0
for i in range(112):
 for j in range(i+1):
  vals=[F(int(x),G) for x in s['lower_triangle'][index]];index+=1
  n=isqrt((2*i+1)*(2*j+1)*G*G)
  result=mul(mul((F(n,G),F(n+1,G)),vals),inverse)
  assert result==tuple(map(F,c['matrix_intervals'][i][j]));checks+=1 if i==j else 2
old=I.grid;I.grid=10**80
try:
 tau=F(c['raw_physical_coercivity_lower_bound']);assert tau>0
 Q=[[I(*map(F,x)) for x in row]for row in c['matrix_intervals']]
 compact=json.loads((root/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json').read_bytes());idx=0
 for i in range(112):
  for j in range(i+1):
   lo,hi=[F(int(x),10**80)for x in compact['lower_triangle_row_major'][idx]];idx+=1
   assert (lo,hi)==(Q[i][j].lo,Q[i][j].hi)
 pivots=[]
 for parity in [0,1]:
  degrees=list(range(parity,112,2))[::-1]
  pivots+=positive_pivots([[Q[i][j]-(I(tau)if i==j else I(0))for j in degrees]for i in degrees])
 broken=[[I(-1),I(0)],[I(0),I(1)]]
 try:positive_pivots(broken)
 except ArithmeticError:pass
 else:raise AssertionError('Negative control accepted')
 out={'aperture':'21/20','native_sha256':hashlib.sha256(r).hexdigest(),'native_finalization_repeated_byte_for_byte':True,
 'independent_raw_to_physical_entries_checked':checks,'independent_compact_outward_entries_checked':checks,
 'widened_grid_digits':80,'shifted_pivots_checked':len(pivots),'finite_native_physical_margin':str(tau),
 'descending_parity_ordering_verified':True,'negative_diagonal_control_rejected':True,'finite_sign_certified':True,
 'whole_domain_positivity':False,'f4_entry_closed':False,'lean_formalized':False}
 print(json.dumps(out,indent=2))
finally:I.grid=old
