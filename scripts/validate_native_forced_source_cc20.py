"""CC20: exact forced-source covariance and arithmetic cancellation controls.

Finite source controls are not zeta evaluations. The differential and
logarithmic operator arguments are analytic, not proved by these samples.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_shell_leakage_cc19 import run as cc19_run

ROOT=Path(__file__).resolve().parents[1]
def tr(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum((a*b for a,b in zip(row,col)),F(0))
                      for col in zip(*B)] for row in A]
def sub(A,B):return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def inv(A):
 n=len(A);C=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  p=C[i][i];assert p;C[i]=[v/p for v in C[i]]
  for j in range(n):
   if i!=j:
    p=C[j][i];C[j]=[a-p*b for a,b in zip(C[j],C[i])]
 return [row[n:] for row in C]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def run():
 counts={k:0 for k in ('source_covariance','quotient_projection',
     'hyperbolic_dictionary','partner_normalization','positive_level',
     'genuine_crossing_scaling')}
 def check(v,k):assert v,k;counts[k]+=1
 cases=0;positive=0;negative=0
 for a in (F(1,2),F(3,4),1-F(1,2**8),1-F(1,2**24)):
  for b in (F(1,3),F(4,5)):
   for r in (F(0),F(1,3)):
    for x in (F(-1,4),F(2,3)):
     for y in (F(-1,2),F(1,5)):
      for m in (F(1,3),F(2)):
       P=[[F(1),r,x],[F(0),F(1),y],[F(0),F(0),m]]
       M=mm(tr(P),P);Mi=inv(M)
       oldM=[row[:2] for row in M[:2]];oi=inv(oldM)
       emb=[[oi[0][0],oi[0][1],F(0)],
            [oi[1][0],oi[1][1],F(0)],[F(0)]*3]
       R=mm(emb,M)
       Z=sub(eye(3),R)
       W=sub(Mi,emb)
       check(mm(mm(Z,Mi),tr(Z))==W,'quotient_projection')
       check(mm(R,R)==R,'quotient_projection')
       check(mm(mm(tr(R),M),Z)==[[F(0)]*3 for _ in range(3)],
             'quotient_projection')
       h=[[F(1),F(0),F(0)],[-r,F(1),F(0)]]
       d=[1-a*a,1-b*b];lam=[a*a,b*b]
       for k1,k2 in ((F(1,8),F(1,6)),(F(1,2),F(2,3)),
                     (d[0]/4,d[1]/5)):
        T=[[a,F(0),k1],[F(0),b,k2]];N=mm(T,P)
        Q=sub(M,mm(tr(N),N));HM=mm(h,M);HQ=mm(h,Q)
        J=[[HQ[i][j]-d[i]*HM[i][j] for j in range(3)] for i in range(2)]
        check(all(J[i][j]==0 for i in range(2) for j in range(2)),
              'source_covariance')
        check(J==[[F(0),F(0),-a*k1*m],[F(0),F(0),-b*k2*m]],
              'source_covariance')
        C=mm(mm(J,Mi),tr(J))
        check(C==mm(mm(J,W),tr(J)),'source_covariance')
        # Independent direct whole source-shell lift, unit POSITIVE norm.
        z=[[(r*y-x)/m],[-y/m],[1/m]]
        check(mm(P,z)==[[F(0)],[F(0)],[F(1)]],'source_covariance')
        K=mm(N,z);check(K==[[k1],[k2]],'source_covariance')
        covariance=mm(K,tr(K))
        check([[C[i][j]/([a,b][i]*[a,b][j]) for j in range(2)]
              for i in range(2)]==covariance,'source_covariance')
        check(mm(J,R)==[[F(0)]*3 for _ in range(2)],'source_covariance')
        # Whole mixed covariance bound: qG-KK* is PSD with determinant0.
        cost=k1*k1/d[0]+k2*k2/d[1]
        D=[[cost*d[i]*F(i==j)-covariance[i][j] for j in range(2)]
           for i in range(2)]
        check(D[0][0]>=0 and D[1][1]>=0 and
              D[0][0]*D[1][1]-D[0][1]*D[1][0]==0,'source_covariance')
        # This is the exact ORIGINAL completion, not a diagonal-only test.
        fullsource=sub(eye(3),mm(tr(T),T))
        schur=fullsource[2][2]-sum((fullsource[i][2]**2/d[i]
                                  for i in range(2)),F(0))
        check(schur==1-cost,'source_covariance')
        positive+=cost<1;negative+=cost>1;cases+=1
 # Exact pair kernels. No pointwise infinite divisor sum is asserted.
 for r in (F(1,2),F(2),F(3)):
  for s in (F(1,3),F(1),F(4)):
   ch=(r+1/r)/2;sh=(r-1/r)/2
   cf=(s+1/s)/2;sf=(s-1/s)/2
   diff=(r/s+s/r)/2;total=(r*s+1/(r*s))/2
   for delta in (F(0),F(1,4),F(1,2**20)):
    check(ch*cf==(diff+total)/2,'hyperbolic_dictionary')
    check(sh*sf==(total-diff)/2,'hyperbolic_dictionary')
    check((1-delta)*ch*cf-sh*sf==
          (1-delta/2)*diff-delta*total/2,'hyperbolic_dictionary')
    check((-sh)*(-sf)==sh*sf,'hyperbolic_dictionary')
    if delta==0:check(ch*cf-sh*sf==diff>0,'hyperbolic_dictionary')
 # Full-copy pair normalization: P=(A+B)/2, N=(A-B)/2.
 for A in (F(-2),F(0),F(3)):
  for B in (F(-1),F(2)):
   for C in (F(-3),F(1)):
    for D in (F(0),F(4)):
     p,n=(A+B)/2,(A-B)/2;pf,nf=(C+D)/2,(C-D)/2
     check(p*pf-n*nf==(A*D+B*C)/2,'partner_normalization')
     check(p*pf-(-n)*(-nf)==p*pf-n*nf,'partner_normalization')
     check(2*(p*pf-n*nf)==A*D+B*C,'partner_normalization')
 # Genuine positive physical level, full mass channel, all shifted budgets.
 a,k,mu=F(9,25),F(12,25),F(16,25)
 original=k*k/(1-a*a)
 lam=a*a+mu;defect=1-lam
 shifted=k*k+mu+a*a*k*k/defect
 critical=a*a*k*k/(lam*defect)
 low=k*k+mu-a*a*k*k/lam
 check(a*a+k*k+mu==1,'positive_level')
 check(original==F(9,34)<1,'positive_level')
 check(shifted==1,'positive_level')
 check(critical+low==1,'positive_level')
 check(lam>0 and defect>0 and low>0,'positive_level')
 # Shifted null vector is genuinely ORIGINAL-positive with physical mass.
 N=[[a,k]];Q=sub(eye(2),mm(tr(N),N));h0=[[a],[k]]
 check(mm(Q,h0)==[[mu*a],[mu*k]],'positive_level')
 check(mm(mm(tr(h0),Q),h0)[0][0]==mu*(a*a+k*k)>0,'positive_level')
 # CC19 exact differential leakage translated to J C_t^-1 J*.
 for j in range(1,81):
  u=1-F(1,2**j);lam=u*u;delta=1-lam
  leakage=2*u*(1-u);residualcov=lam*leakage
  check(residualcov/(lam*delta)==2*u/(1+u),
        'genuine_crossing_scaling')
  check(residualcov/(lam*delta)>F(1,2),'genuine_crossing_scaling')
  check(residualcov*residualcov/(lam*lam*delta**3)>F(2)**(j-3),
        'genuine_crossing_scaling')
 inherited=cc19_run();assert inherited['all_passed']
 assert inherited['total_exact_checks']==7032 and positive and negative
 return {'stage':'CC20 forced arithmetic residual / positive-source inverse',
   'classification':'A: exact analytic interface; C: automatic defect-factor candidate rejected',
   'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
   'inherited_cc19_checks':7032,'total_exact_checks':sum(counts.values())+7032,
   'complete_source_cases':cases,'positive_cases':positive,'negative_cases':negative,
   'exact_covariance':'L L*=Lambda^-1/2 J M_t^-1 J* Lambda^-1/2',
   'independent_arithmetic_target':'J M_t^-1 J* <= q Lambda G, low+q<1',
   'automatic_small_factor_from_source_orthogonality':False,
   'actual_zeta_covariance_evaluated':False,'arithmetic_estimate_certified':False,
   'arithmetic_estimate_disproved_for_zeta':False,'new_aperture':False,
   'whole_domain_anchor':'21/20 inherited CC18, even0/odd0',
   'global_nonstalling':False,'lean_certified':False,
   'scope':'Actual arithmetic identities are analytic. Finite matrices and pair values are controls, not actual divisor data.',
   'input_sha256':{'cc19_validator':hashlib.sha256(
       (ROOT/'scripts/validate_native_shell_leakage_cc19.py').read_bytes()).hexdigest(),
       'cc19_validation':hashlib.sha256((ROOT/'notes/data/RPB108_SHELL_LEAKAGE_CC19_VALIDATION_20261008.json').read_bytes()).hexdigest()},
   'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_FORCED_SOURCE_CC20_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks','complete_source_cases')},indent=2))
