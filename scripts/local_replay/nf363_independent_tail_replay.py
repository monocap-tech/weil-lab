"""Independent coefficient-polynomial replay of NF363 2-moment high-tail certificate.
No imports or code reuse from primary producer. All arithmetic is Fraction.
"""
from fractions import Fraction as R
from collections import defaultdict
import json,zipfile,hashlib
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
j=json.loads(Path(str(CUSTODY_ROOT / 'nf363_critical_sine_tail_higher_report.json')).read_text())
with zipfile.ZipFile(str(CUSTODY_ROOT / 'nf361-pr348-fourmode.zip')) as z:raw=z.read('original_four_mode_critical_block.json')
assert hashlib.sha256(raw).hexdigest()==j['input_json_sha256']
obj=json.loads(raw)
cutoffs=[512,1024,2048,4096,16384]
for L in cutoffs:
  assert L&(L-1)==0
  exponent=L.bit_length()-1
  y=R(17)+R(347,500)*exponent
  # Aggregate the square of each majorant as polynomial in t^-1;
  # this is algebraically separate from the pairwise integral in primary.
  square=defaultdict(R)
  for candidate in obj['exact_candidates']['probes']:
    aa=[R(q) for q in candidate['sine_coefficients']]
    c=[R(5*i,11) for i in range(1,33)]
    moments=[sum(((-1)**(i+1))*aa[i]*c[i]**(2*m+1) for i in range(32)) for m in (0,1)]
    # |hat f| <= pole*t^-1+ |S1|/(3t^2)+ |S3|/(3t^4) + (4/9)*sum|a|c^5 *t^-6.
    poles=abs(R(candidate['sinh_coefficient']))*R(440,837)
    powers={1:poles,2:abs(moments[0])/3,4:abs(moments[1])/3,6:R(4,9)*sum(abs(aa[i])*c[i]**5 for i in range(32))}
    for p,cp in powers.items():
      for q,cq in powers.items():
        square[p+q]+=cp*cq
  integral=R(0)
  for pow_,coeff in square.items():
    b=pow_-1
    # integrate q:  2*integral_L^infty (17+log x)^2*x^-pow dx
    integral+=2*coeff*R(1,b*L**b)*(y*y+2*y/b+R(2,b*b))
  ref=next(R(x['order2_upper_exact']) for x in j['tail'] if x['cutoff']==L)
  assert integral==ref,(L,float(integral),float(ref))
  print('PASS independent polynomial rational tail',L,'=',float(integral))
print('NF363 INDEPENDENT REPLAY PASSED')
