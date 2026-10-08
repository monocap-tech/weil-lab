"""CC27 rational native-kernel/sign and full covariance checks.
No actual generalized critical vector is evaluated. Bump-limit arguments
and digamma distribution calculations are analytic, not these checks.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from validate_native_forced_source_cc20 import mm,tr
from validate_native_uniform_exit_cc26 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def coff(r):return r+1/r-r**3/(r**4-1)
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(c,A):return [[c*x for x in row] for row in A]
def exp_bounds(q,N=32):
 term=F(1);s=term
 for j in range(1,N+1):term*=q/j;s+=term
 nxt=term*q/(N+1)
 assert 0<q<N+2
 return s,s+nxt/(1-q/(N+2))
def run():
 counts={k:0 for k in ('native_kernel','parity_sign','prime_support','mixed_covariance','crossing','full_mass')}
 def check(v,k):assert v,k;counts[k]+=1
 for r in (F(11,10),F(3,2),F(13,11),F(143,100),F(22,21),F(231,200)):
  y=r*r
  check(coff(r)==(y**3-y-1)/(r*(y*y-1)),'native_kernel')
  check(y>1 and r**4-1>0,'native_kernel')
 check(coff(F(11,10))<0<coff(F(3,2)),'native_kernel')
 pos=[coff(F(13,11)),coff(F(143,100))]
 neg=[coff(F(22,21)),coff(F(231,200))]
 check(all(x>0 for x in pos),'parity_sign')
 check(sum(neg)<0,'parity_sign')
 check(pos[0]-pos[1]<0 and neg[0]-neg[1]<0,'parity_sign')
 # Every separation in these pairs avoids every integer prime-power atom.
 for r in (F(13,11),F(143,100),F(22,21),F(231,200)):
  check((r*r).denominator>1,'parity_sign')
 # Native negative translation atoms reflect to positive odd image atoms.
 # Matrix entries connect +x to -y and -x to +y only, x+y=log2.
 atom=[[F(0),F(-1)],[F(-1),F(0)]]
 even=[[F(1),F(1)]];odd=[[F(1),F(-1)]]
 check(mm(mm(even,atom),tr(even))==[[F(-2)]],'parity_sign')
 check(mm(mm(odd,atom),tr(odd))==[[F(2)]],'parity_sign')
 check(F(5,4)*F(8,5)==2,'prime_support')
 check((F(8,5)/F(5,4)).denominator>1,'prime_support')
 for q in (F(21,10),F(53,25)):
  lo,hi=exp_bounds(q)
  check(8<lo<=hi<9,'prime_support')
 check([n for n in range(2,9) if any(n==p**k for p in (2,3,5,7) for k in range(1,4))]==[2,3,4,5,7,8],'prime_support')
 lo,hi=exp_bounds(F(69,100));lo2,hi2=exp_bounds(F(7,10))
 check(hi<2<lo2,'prime_support')
 s,t,eps,width=F(21,20),F(53,50),F(1,200),F(1,1000)
 # log2 in(.69,.70) certifies old bump and exterior translated bump supports.
 check(-s<s+eps-F(7,10)-width,'prime_support')
 check(s+eps-F(69,100)+width<s,'prime_support')
 check(s<s+eps-width<s+eps+width<t,'prime_support')
 # Keep all 16 native covariance blocks, including off-diagonal row entries.
 A=[[F(2),F(1),F(0)],[F(1),F(0),F(3)]]
 Pi=[[F(1),F(0),F(2)],[F(2),F(1),F(0)]]
 C=[[F(0),F(2),F(1)],[F(1),F(3),F(1)]]
 M=[[F(1),F(2),F(3)],[F(2),F(1),F(1)]]
 W=[[F(2),F(1,2),F(0)],[F(1,2),F(1),F(0)],[F(0),F(0),F(3)]]
 check(W[0][0]*W[1][1]-W[0][1]*W[1][0]>0 and W[2][2]>0,'mixed_covariance')
 for delta in (F(1,4),F(1,16),F(1,1024)):
  X=[A,scale(-1,Pi),C,scale(-delta,M)]
  J=[[F(0)]*3 for _ in range(2)]
  for x in X:J=add(J,x)
  full=mm(mm(J,W),tr(J));blocks=[[F(0)]*2 for _ in range(2)];diag=[[F(0)]*2 for _ in range(2)]
  for i in range(4):
   for j in range(4):
    block=mm(mm(X[i],W),tr(X[j]));blocks=add(blocks,block)
    if i==j:diag=add(diag,block)
  check(full==blocks,'mixed_covariance')
  check(full!=diag,'mixed_covariance')
  check(full[0][1]!=0 and full==tr(full),'mixed_covariance')
 for j in (8,16,32):
  u=1-F(1,2**j);lam=u*u;delta=1-lam
  check(lam*2*u*(1-u)/(lam*delta)==2*u/(1+u),'crossing')
  check(2*u*F(1,16)/delta>1,'crossing')
 a,k,mu=F(9,25),F(12,25),F(16,25)
 lam=a*a+mu;gap=1-lam
 critical=a*a*k*k/(lam*gap);low=k*k+mu-a*a*k*k/lam
 check(k*k/(1-a*a)==F(9,34)<1,'full_mass')
 check(critical+low==1 and low>0,'full_mass')
 check(lam==F(481,625) and gap==F(144,625),'full_mass')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==24554
 return {'stage':'CC27 native exterior forcing / sign mechanism',
  'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc26_checks':24554,'total_exact_checks':24554+sum(counts.values()),
  'actual_coefficient_sign_mechanism_rejected':True,
  'only_new_prime_powers_force_exterior_rejected':True,
  'new_prime_support_control':{'s':'21/20','t':'53/50','same_support':[2,3,4,5,7,8]},
  'actual_critical_covariance_evaluated':False,'defect_relative_bound_proved':False,
  'actual_zeta_bound_disproved':False,'full_identity_independence_proved':False,
  'RH_proved':False,'new_aperture':False,'lean_certified':False,
  'scope':'native coefficient controls and analytic separated-support tests; no actual critical eigenvector evaluation',
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
   'scripts/validate_native_uniform_exit_cc26.py',
   'notes/data/RPB108_UNIFORM_EXIT_CC26_VALIDATION_20261008.json',
   'WeilDefect/Morphology/NeutralWeilMultiplier.lean',
   'WeilDefect/Arithmetic/ActualZetaNativeWeilForm.lean']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_NATIVE_FLUX_CC27_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
