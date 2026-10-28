"""Independent rational replay: separate pole budget, sine-only squared-poly tail,
physical lowband no-go. No reuse of producer functions."""
from fractions import Fraction as R
from collections import defaultdict
import json,zipfile,hashlib
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
rep=json.loads(Path(str(CUSTODY_ROOT / 'nf364_split_tail_exact_report.json')).read_text())
zipb=Path(str(CUSTODY_ROOT / 'nf361-pr348-fourmode.zip')).read_bytes()
assert hashlib.sha256(zipb).hexdigest()==rep['artifact_sha256']
with zipfile.ZipFile(str(CUSTODY_ROOT / 'nf361-pr348-fourmode.zip')) as z: raw=z.read('original_four_mode_critical_block.json')
assert hashlib.sha256(raw).hexdigest()==rep['json_sha256']
o=json.loads(raw); cs=[R(5*i,11) for i in range(1,33)]
bs=[R(p['sinh_coefficient']) for p in o['exact_candidates']['probes']]
assert sum(x*x for x in bs)==R(rep['full_4direction_pole_coeff_squared_exact'])
assert R(rep['shared_pole_unprojected_global_strong_square_upper_exact'])==100+650*R(7,30)**2==R(2437,18)<136
assert R(rep['pole_forcing_four_direction_square_upper_exact'])==136*sum(x*x for x in bs)
for entry in rep['tail']:
 L=entry['cutoff'];k=L.bit_length()-1;V=R(17)+R(347,500)*k
 poly=defaultdict(R)
 for v in o['exact_candidates']['probes']:
  a=[R(q) for q in v['sine_coefficients']]
  m1=sum(((-1)**i)*a[i-1]*cs[i-1] for i in range(1,33))
  m3=sum(((-1)**i)*a[i-1]*cs[i-1]**3 for i in range(1,33))
  r5=sum(abs(a[i])*cs[i]**5 for i in range(32))
  terms=[(2,abs(m1)/3),(4,abs(m3)/3),(6,R(4,9)*r5)]
  for p,u in terms:
   for q,w in terms:poly[p+q]+=u*w
 ans=R(0)
 for power,coeff in poly.items():
  m=power-1
  ans += 2*coeff*R(1,m*L**m)*(V*V+2*V/m+R(2,m*m))
 assert ans==R(entry['order2_sine_only_tail_exact'])
 assert ans>=0
 print('SINE-ONLY exact polynomial',L,'=',float(ans))
assert R(rep['unprojected_low32_strong_action_norm_lower_exact'])==R(989,10**6)
assert R(rep['unprojected_low32_strong_action_square_lower_exact'])==R(989,10**6)**2
print('INDEPENDENT RATIONAL REPLAY PASS')
