"""Outward physical native intervals only; explicitly no native sign certificate."""
import gzip,hashlib,json
from pathlib import Path
from math import isqrt
from certify_native_legendre_small_window import F,I
from certify_native_matrix112_checkpoint import load
p=Path('notes/data/RPB108_PRIME8_RAW112_105_ORDERS420_CHECKPOINT_20261008.json.gz');b=p.read_bytes();s=json.loads(gzip.decompress(b))
assert s['completed_rows']==112 and s['bindings']['aperture']=='21/20'
I.grid=10**400;done,m=load(p,s['bindings']);assert done==112
q=[]
for i in range(112):
 row=[]
 for j in range(112):
  n=isqrt((2*i+1)*(2*j+1)*I.grid**2);row.append(I(F(n,I.grid),F(n+1,I.grid))*m[i][j]/F(21,10))
 q.append(row)
width=max(x.hi-x.lo for row in q for x in row)
I.grid=10**80;tri=[];checked=0
for i in range(112):
 for j in range(i+1):
  x=I(q[i][j].lo,q[i][j].hi);assert x.lo<=q[i][j].lo<=q[i][j].hi<=x.hi
  tri.append([str(int(x.lo*I.grid)),str(int(x.hi*I.grid))]);checked+=1 if i==j else 2
out={'aperture':'21/20','physical_degrees':list(range(112)),'prime_terms':[2,3,4,5,7,8],
 'matrix_encoding':'row-major lower triangle integer endpoints on grid 10^-80','lower_triangle_row_major':tri,
 'native_sign_certified':False,'raw_physical_coercivity_lower_bound':'0','whole_domain_positivity':False,
 'raw_checkpoint_sha256':hashlib.sha256(b).hexdigest(),'raw_constructor_bindings':s['bindings'],
 'maximum_entry_width_before_compact':str(width),'compact_outward_inclusions_checked':checked,
 'exponential_order':420,'bernoulli_pairs':420,'interval_grid_digits':80,'f4_entry_closed':False,'lean_formalized':False}
Path('notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'outward_entries':checked,'native_sign_certified':False,'width_display':float(width)}))
