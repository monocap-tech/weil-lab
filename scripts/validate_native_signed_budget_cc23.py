"""CC23 exact signed Schur/circularity controls; not actual zeta data."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_forced_source_cc20 import mm,tr,inv,eye,sub
from validate_native_density_phase_cc22 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def psd(A):return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]>=A[0][1]*A[1][0]
def spd(A):return A[0][0]>0 and A[0][0]*A[1][1]>A[0][1]*A[1][0]
def quadratic(A,x):return mm(mm(tr(x),A),x)[0][0]
def run():
 counts={k:0 for k in ('whole_schur','completion_square','same_diagonal','crossing_budget','positive_level')}
 def check(v,k):assert v,k;counts[k]+=1
 I=eye(2);R=[[F(3,5),F(-4,5)],[F(4,5),F(3,5)]]
 vectors=[[[F(1)],[F(0)]],[[F(0)],[F(1)]],[[F(1)],[F(1)]],[[F(2)],[-F(3)]]]
 cases=0;positive=negative=0
 for a in (F(1,2),F(3,4),F(255,256)):
  for b in (F(1,3),F(4,5),F(31,32)):
   for U in (I,R):
    T=mm(mm(U,[[a,F(0)],[F(0),b]]),tr(R))
    H=sub(I,mm(tr(T),T));D=sub(I,mm(T,tr(T)))
    check(add(I,mm(mm(T,inv(H)),tr(T)))==inv(D),'whole_schur')
    for scale in (F(1,100),F(1,5),F(3,4)):
     K=[[scale,scale/3],[-scale/2,scale]]
     C=mm(tr(T),K);incoming=sub(I,mm(tr(K),K))
     S=sub(incoming,mm(mm(tr(C),inv(H)),C))
     budget=mm(mm(tr(K),inv(D)),K)
     check(S==sub(I,budget),'whole_schur')
     check(psd(S)==psd(sub(D,mm(K,tr(K)))),'whole_schur')
     check(spd(S)==spd(sub(D,mm(K,tr(K)))),'whole_schur')
     Q=[H[0]+[-C[0][0],-C[0][1]],H[1]+[-C[1][0],-C[1][1]],
       [-C[0][0],-C[1][0]]+incoming[0],[-C[0][1],-C[1][1]]+incoming[1]]
     for p in vectors:
      for w in vectors:
       shifted=sub(p,mm(mm(inv(H),C),w))
       check(quadratic(Q,p+w)==quadratic(H,shifted)+quadratic(S,w),'completion_square')
     for w in vectors:
      minimizer=mm(mm(inv(H),C),w)
      check(quadratic(Q,minimizer+w)==quadratic(S,w),'completion_square')
     cases+=1;positive+=int(spd(S));negative+=int(not psd(S))
 examples=[]
 for j in range(4,65):
  a=1-F(1,2**j);delta=1-a*a;c=F(1,2)
  safeN=[[a,F(0)],[F(0),c]];unsafeN=[[a,c],[F(0),F(0)]]
  safeQ=sub(I,mm(tr(safeN),safeN));unsafeQ=sub(I,mm(tr(unsafeN),unsafeN))
  check([safeQ[i][i] for i in range(2)]==[unsafeQ[i][i] for i in range(2)],'same_diagonal')
  check(safeQ[0][0]==delta and safeQ[1][1]==F(3,4),'same_diagonal')
  check(spd(safeQ) and not psd(unsafeQ),'same_diagonal')
  check(c*c==F(1,4) and c*c/delta>1,'same_diagonal')
  check(unsafeQ[0][1]**2>unsafeQ[0][0]*unsafeQ[1][1],'same_diagonal')
  check(unsafeQ[1][1]-unsafeQ[0][1]**2/delta==1-c*c/delta,'same_diagonal')
  check(unsafeQ[0][0]+unsafeQ[1][1]==safeQ[0][0]+safeQ[1][1],'same_diagonal')
  if j in (4,16,32,64):examples.append({'j':j,'old_defect':str(delta),
     'incoming_negative_norm_squared':'1/4','safe_budget':'1/4',
     'unsafe_budget':str(c*c/delta),'scope':'same diagonal/full positive Gram control, not actual zeta'})
  # Genuine differential model, exact restriction imposed by q<1.
  u=a;gap=1-u*u
  for q in (F(1,4),F(1,2),F(3,4),F(1)):
   step=q*gap/(2*u);v=u+step
   check(2*u*(v-u)/gap==q,'crossing_budget')
   check(step/(1-u)==q*(1+u)/(2*u),'crossing_budget')
   if q<1:check(v<1,'crossing_budget')
  check(2*u*(1-u)/gap==2*u/(1+u)<1,'crossing_budget')
  check(1-2*u/(1+u)==(1-u)/(1+u),'crossing_budget')
 # Full positive mass shift from the inherited source model.
 a,k,mu=F(9,25),F(12,25),F(16,25)
 original=sub(I,mm(tr([[a,k]]),[[a,k]]))
 shifted=sub(original,[[mu,F(0)],[F(0),mu]])
 check(spd(original) and psd(shifted) and not spd(shifted),'positive_level')
 check(shifted[1][1]-shifted[0][1]**2/shifted[0][0]==0,'positive_level')
 check(original[1][1]-original[0][1]**2/original[0][0]==1-F(9,34)>0,'positive_level')
 check(a*a+k*k+mu==1,'positive_level')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==18352
 return {'stage':'CC23 signed covariance and circularity audit','all_passed':True,
  'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc22_checks':18352,'total_exact_checks':18352+sum(counts.values()),
  'whole_source_cases':cases,'strict_positive_cases':positive,'indefinite_cases':negative,
  'same_diagonal_controls':examples,
  'exact_equivalence':'Q_t >= 0 iff K*D_s^-1 K <= I iff K K* <= D_s',
  'classification':'A: exact signed completion; C: enlarged signed Cauchy-Schwarz would assume target positivity',
  'actual_arithmetic_strict_budget_certified':False,'actual_zeta_bound_disproved':False,
  'complete_Weil_logical_independence_proved':False,'new_aperture':False,
  'global_nonstalling':False,'lean_certified':False,
  'whole_domain_anchor':'21/20 even0/odd0 inherited',
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
    'scripts/validate_native_density_phase_cc22.py',
    'notes/data/RPB108_DENSITY_PHASE_CC22_VALIDATION_20261008.json',
    'WeilDefect/Arithmetic/ActualZetaNativeWeilForm.lean']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_SIGNED_BUDGET_CC23_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks','whole_source_cases','strict_positive_cases','indefinite_cases')},indent=2))
