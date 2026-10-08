"""CC28 exact stationary/moment algebra and genuine crossing controls.
The native nonanalyticity and local-extension theorems are analytic,
not certified by these finite checks; no actual critical Gram is evaluated.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb,factorial
import hashlib,json
from validate_native_flux_cc27 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def derivative_pair(A,B,k):
 # (A0+A1*r)cos(k*r)+(B0+B1*r)sin(k*r)
 return ([A[1]+k*B[0],k*B[1]], [B[1]-k*A[0],-k*A[1]])
def run():
 counts={k:0 for k in ('finite_difference','correlation_derivative','outward_crossing','full_shift')}
 def check(v,k):assert v,k;counts[k]+=1
 for n in range(1,9):
  for p in range(2*n):
   check(sum((-1)**j*comb(2*n,j)*(n-j)**p for j in range(2*n+1))==0,'finite_difference')
  check(sum((-1)**j*comb(2*n,j)*(n-j)**(2*n) for j in range(2*n+1))==factorial(2*n),'finite_difference')
 # Independently differentiate exact overlap correlation coefficients.
 for s,k in [(F(3,2),F(4,3)),(F(5,4),F(7,5)),(F(11,10),F(13,11))]:
  A=[s,F(-1,2)];B=[1/(2*k),F(0)]
  A1,B1=derivative_pair(A,B,k);A2,B2=derivative_pair(A1,B1,k)
  qA=[-x-y for x,y in zip(A2,A)];qB=[-x-y for x,y in zip(B2,B)]
  check(qA==[(k*k-1)*s,-(k*k-1)/2],'correlation_derivative')
  check(qB==[-(k*k+1)/(2*k),F(0)],'correlation_derivative')
  check(A1==[F(0),F(0)] and B1==[-k*s,k/2],'correlation_derivative')
 z=F(1,16);sin_lower=z-z**3/6;rows=[]
 for j in (8,12,16,24,32,48,64):
  u=1-F(1,2**j);delta=1-u*u;r=u*z
  upper=delta-(1+u*u)*F(7,22)*sin_lower
  check(0<delta<F(1,128),'outward_crossing')
  check(upper<F(-1,100),'outward_crossing')
  check(-upper>delta,'outward_crossing')
  check(delta*delta-upper*upper<0,'outward_crossing')
  check(F(1,32)<r<F(1,16),'outward_crossing')
  # s+r < pi/2+1/16 <2 using pi<22/7.
  check(F(11,7)+F(1,16)<2,'outward_crossing')
  check(delta< F(1,2**(j-1)),'outward_crossing')
  rows.append({'u':str(u),'old_defect':str(delta),'shift':str(r),
   'mixed_entry_upper':str(upper),'scope':'genuine differential ground translation; not zeta'})
 mu=F(9,16);kappa=1+mu;lam=1/kappa
 check(lam==F(16,25),'full_shift')
 check(1-lam==F(9,25)>0,'full_shift')
 check(1-kappa*lam==0,'full_shift')
 check(mu*lam==1-lam,'full_shift')
 # Full shifted source rows with a nontrivial physical vector: retain
 # original N plus sqrt(mu)*h, not a lone constant at the diagonal.
 mass=F(7,9);cross=F(-2,7)
 check(mass+F(9,16)*mass==F(25,16)*mass,'full_shift')
 check(cross+F(9,16)*cross==F(25,16)*cross,'full_shift')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==24604
 return {'stage':'CC28 stationary translation / analytic extension',
  'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc27_checks':24604,'total_exact_checks':24604+sum(counts.values()),
  'analytic_theorem':'nonzero compact canonical-domain vector has native stationary correlation nonanalytic at0',
  'analytic_theorem_lean_certified':False,
  'positive_extension_identified_with_native':False,
  'genuine_crossing_translation_examples':rows,
  'actual_critical_covariance_evaluated':False,'defect_relative_bound_proved':False,
  'actual_zeta_bound_disproved':False,'full_identity_independence_proved':False,
  'RH_proved':False,'new_aperture':False,
  'negative_source_height_moment_theorem_claimed':False,
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
   'scripts/validate_native_flux_cc27.py',
   'notes/data/RPB108_NATIVE_FLUX_CC27_VALIDATION_20261008.json',
   'WeilDefect/Morphology/NeutralWeilMultiplier.lean',
   'notes/REFLECTED_PACKET_BRIDGE_108_LOG_SOURCE_ANALYSIS_20261003.md']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_STATIONARY_EXTENSION_CC28_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
