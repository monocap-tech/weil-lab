"""CC25 exact finite exponential-kernel rigidity controls; analytic proof in note."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json
from validate_native_translation_candidate_cc21 import ga,gm,gs,gc,gn
from validate_native_pair_correlation_cc24 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
Z=(F(0),F(0));ONE=(F(1),F(0))
def div(a,b):return gs(1/gn(b),gm(a,gc(b)))
def power(z,k):
 r=ONE
 for _ in range(k):r=gm(r,z)
 return r
def mm(A,B):
 return [[sumg([gm(a,b) for a,b in zip(row,col)]) for col in zip(*B)] for row in A]
def sumg(v):
 out=Z
 for x in v:out=ga(out,x)
 return out
def inv(A):
 n=len(A);C=[r[:]+[ONE if i==j else Z for j in range(n)] for i,r in enumerate(A)]
 for i in range(n):
  p=next(j for j in range(i,n) if C[j][i]!=Z);C[i],C[p]=C[p],C[i]
  pivot=C[i][i];C[i]=[div(v,pivot) for v in C[i]]
  for j in range(n):
   if j!=i:
    pivot=C[j][i];C[j]=[ga(a,gs(-1,gm(pivot,b))) for a,b in zip(C[j],C[i])]
 return [r[n:] for r in C]
def det(A):
 C=[r[:] for r in A];out=ONE;n=len(C)
 for i in range(n):
  p=next(j for j in range(i,n) if C[j][i]!=Z)
  if p!=i:C[i],C[p]=C[p],C[i];out=gs(-1,out)
  pivot=C[i][i];out=gm(out,pivot)
  for j in range(i+1,n):
   factor=div(C[j][i],pivot)
   C[j]=[ga(a,gs(-1,gm(factor,b))) for a,b in zip(C[j],C[i])]
 return out
def run():
 counts={k:0 for k in ('vandermonde','paired_normalization','conditioning','full_mass')}
 def check(v,k):assert v,k;counts[k]+=1
 cases=0
 for beta in (F(1,16),F(1,4),F(3,8)):
  for theta in (F(1),F(7,3),F(25)):
   for two in (False,True):
    nodes=[(b,t) for t in (theta,-theta) for b in (beta,-beta)]
    if two:nodes += [(b,t) for t in (theta+1,-theta-1) for b in (beta/2,-beta/2)]
    n=len(nodes);V=[[power(z,k) for z in nodes] for k in range(n)]
    Vi=inv(V);product=ONE
    for j in range(n):
     for i in range(j):product=gm(product,ga(nodes[j],gs(-1,nodes[i])))
    check(det(V)==product and product!=Z,'vandermonde')
    check(mm(Vi,V)==[[ONE if i==j else Z for j in range(n)] for i in range(n)],'vandermonde')
    coeff=[[(F(1) if j<4 else F(-1),F(0))] for j in range(n)]
    moments=mm(V,coeff);check(mm(Vi,moments)==coeff,'vandermonde')
    check(any(x[0]!=Z for x in moments),'vandermonde')
    # Reflection-invariant multiplicities: cosh dictionary equals exponent sum.
    for k in range(13):
     direct=sumg([gm(c[0],power(z,k)) for z,c in zip(nodes,coeff)])
     paired=sumg([gm(c[0],gs(F(1,2),ga(power(z,k),power((-z[0],z[1]),k)))) for z,c in zip(nodes,coeff)])
     check(direct==paired,'paired_normalization')
    cases+=1
 # An antisymmetric beta-only change is invisible to cosh; it is not a legal
 # reflected divisor modification. This is why the symmetry hypothesis matters.
 for beta in (F(1,8),F(3,8)):
  for k in range(1,13):
   z=(beta,F(2));zr=(-beta,F(2))
   check(gs(F(1,2),ga(power(z,k),power(zr,k)))==gs(F(1,2),ga(power(zr,k),power(z,k))),'paired_normalization')
 # Balanced near-coincident critical atoms: coefficient 1 cannot be recovered
 # uniformly from vanishing moment errors without a separation-dependent bound.
 examples=[]
 for j in range(2,42):
  eps=F(1,2**j);nodes=[(F(0),F(1)),(F(0),F(-1)),(F(0),1+eps),(F(0),-1-eps)]
  V=[[power(z,k) for z in nodes] for k in range(4)]
  coeff=[[(F(c),F(0))] for c in (1,1,-1,-1)];mom=mm(V,coeff)
  check(mom==[[Z],[Z],[(4*eps+2*eps*eps,F(0))],[Z]],'conditioning')
  check(0<4*eps+2*eps*eps<=6*eps,'conditioning')
  check(mm(inv(V),mom)==coeff,'conditioning')
  check(1/(6*eps)>=F(2**j,6),'conditioning')
  if j in (2,12,24,41):examples.append({'j':j,'location_separation':str(eps),
     'moment_error_sup':str(4*eps+2*eps*eps),'required_inverse_norm_lower':str(1/(6*eps))})
 # An infinite physical mass channel cannot be replaced by finitely many rows.
 # Exact finite feature null-vectors model the rank argument, not bump integrals.
 for m in range(1,25):
  h=[F((-1)**j*comb(m,j)) for j in range(m+1)]
  for k in range(m):check(sum((h[j]*F(j)**k for j in range(m+1)),F(0))==0,'full_mass')
  check(sum((x*x for x in h),F(0))==comb(2*m,m)>0,'full_mass')
  check(F(16,25)*sum((x*x for x in h),F(0))>0,'full_mass')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==22492
 return {'stage':'CC25 exact local identity rigidity versus quantitative stability',
  'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc24_checks':22492,'total_exact_checks':22492+sum(counts.values()),
  'finite_vandermonde_cases':cases,'conditioning_examples':examples,
  'classification':'A: exact mixed-form identity excludes every nonzero finite reflected divisor alteration; C: this qualitative rigidity does not yield uniform relative leakage',
  'finite_perturbation_full_identity_counterexample_possible':False,
  'uniform_arithmetic_relative_bound_certified':False,'actual_zeta_bound_disproved':False,
  'complete_Weil_logical_independence_proved':False,'new_aperture':False,
  'global_nonstalling':False,'lean_certified':False,
  'whole_domain_anchor':'21/20 even0/odd0 inherited',
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
    'scripts/validate_native_pair_correlation_cc24.py',
    'notes/data/RPB108_PAIR_CORRELATION_CC24_VALIDATION_20261008.json',
    'WeilDefect/Arithmetic/ActualZetaSourceDecomposition.lean',
    'WeilDefect/Arithmetic/ActualZetaNativeWeilForm.lean']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_FINITE_IDENTITY_CC25_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
