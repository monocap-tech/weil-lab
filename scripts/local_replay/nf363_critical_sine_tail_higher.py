from fractions import Fraction as F
import hashlib,json,zipfile
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
p=Path(str(CUSTODY_ROOT / 'nf361-pr348-fourmode.zip'))
raw=zipfile.ZipFile(p).read('original_four_mode_critical_block.json')
assert hashlib.sha256(p.read_bytes()).hexdigest()=='735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968'
assert hashlib.sha256(raw).hexdigest()=='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
o=json.loads(raw)
probes=o['exact_candidates']['probes'];cs=[F(x) for x in o['exact_candidates']['sine_frequencies']]
assert cs==[F(5*n,11) for n in range(1,33)]
assert all(2*F(11,10)*c==n for n,c in enumerate(cs,1))
Cs=F(440,837)

def integrate_log_square(p,L,X):
 q=p-1
 return F(1,L**q*q)*(X*X + 2*X/q + F(2,q*q))

def terms(probe,order):
 a=[F(v) for v in probe['sine_coefficients']]
 b=F(probe['sinh_coefficient'])
 # bound nonzero (1/xi) pole and truncated signed moment 1/xi^(2k+2); + abs remainder in 1/xi^(2order+2)
 t=[(1,abs(b)*Cs)]
 for k in range(order):
  S=sum((-1)**n*ak*c**(2*k+1) for n,(ak,c) in enumerate(zip(a,cs),1))
  t.append((2*k+2, abs(S)/3))
 r=sum(abs(ak)*c**(2*order+1) for ak,c in zip(a,cs))
 t.append((2*order+2,F(4,9)*r))
 return t

def loewner2(L,order):
 k=L.bit_length()-1;X=F(17)+k*F(347,500)
 val=F(0)
 for v in probes:
  t=terms(v,order)
  for j,(p,cp) in enumerate(t):
   for h,(q,cq) in enumerate(t):
    val+=2*cp*cq*integrate_log_square(p+q,L,X)
 return val
report={'standing':'EXACT_RATIONAL_ORIGINAL_FOUR_CRITICAL_SINE_SQUARED_POSITIVE_MULTIPLIER_TAIL_UPPER','input_archive_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'input_json_sha256':hashlib.sha256(raw).hexdigest(),'normalization':'fourier hat f = int_{-11/10}^{11/10} f exp(-2pi i xi x) dx','multiplier_bound':'a_o(xi)<=17+log|xi| for |xi|>=1 (SM41)','pole_ibp_constant':'440/837','pi_lower':3,'log2_upper':'347/500','sine_high_frequency_cutoff_minimum':'320/11','source_count':4,'sine_terms':32,'boundary_frequency_identity_certified':True}
for i,v in enumerate(probes):
 a=[F(x) for x in v['sine_coefficients']]
 moments=[sum((-1)**n*x*c**(2*j+1) for n,(x,c) in enumerate(zip(a,cs),1)) for j in range(5)]
 report.setdefault('moments',[]).append({'direction':i,'signed_moments_exact':[str(x) for x in moments],'signed_moments_approx':[float(x) for x in moments],'pole_exact':v['sinh_coefficient']})
for k in [5,6,7,8,9,10,11,12,14]:
 L=1<<k
 row={'cutoff':L}
 for order in [0,1,2,3,4]:
  val=loewner2(L,order)
  row[f'order{order}_upper_exact']=str(val)
  row[f'order{order}_upper_float']=float(val)
  row[f'order{order}_relative_to_kappa_*0.99']=float(val/F(33621,10**9)/F(99,100))
 report.setdefault('tail',[]).append(row)
Path(str(CUSTODY_ROOT / 'nf363_critical_sine_tail_higher_report.json')).write_text(json.dumps(report,indent=2))
for r in report['tail']:
 print('Λ',r['cutoff'],*[f'{j}:{r[f"order{j}_upper_float"]:.4g}' for j in range(5)],'ratio 4/η',r['order4_relative_to_kappa_*0.99']/3e-12)
