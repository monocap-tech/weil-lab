"""Test whether reordering alone repairs the ORIGINAL completed 400-order matrix."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from certify_native_legendre_small_window import I,positive_pivots
p=Path('notes/data/RPB108_PRIME8_MATRIX112_105_UNDECIDED_20261008.json');b=p.read_bytes();c=json.loads(b)
assert c['aperture']=='21/20' and c['prime_terms']==[2,3,4,5,7,8]
I.grid=10**80;Q=[[I(*map(F,x)) for x in row]for row in c['matrix_intervals']]
tau=F(1,2621440000000000000000000000000000);count=0
failures=[]
for parity in [0,1]:
 d=list(range(parity,112,2))[::-1]
 try:
  pivots=positive_pivots([[Q[i][j]-(I(tau)if i==j else I(0))for j in d]for i in d]);count+=len(pivots)
 except ArithmeticError:failures.append(parity)
out={'aperture':'21/20','orders':[400,400],'original_undecided_matrix_sha256':hashlib.sha256(b).hexdigest(),
 'widened_grid_digits':80,'descending_parity_shifted_pivots_checked':count,'finite_physical_margin':str(tau),
 'same_original_intervals_reordering_alone_certifies_selected_margin':not failures,'failed_parity_blocks':failures,'native_sign_certified':not failures,
 'whole_domain_positivity':False,'f4_entry_closed':False,'lean_formalized':False}
print(json.dumps(out,indent=2))
