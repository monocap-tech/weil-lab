"""CC21 exact translation/phase candidate audit, not zeta covariance data."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_forced_source_cc20 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def ga(a,b=(F(0),F(0))):return (a[0]+b[0],a[1]+b[1])
def gs(c,a):return (c*a[0],c*a[1])
def gm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gc(a):return (a[0],-a[1])
def gn(a):return a[0]*a[0]+a[1]*a[1]
def tr(A):return [list(x) for x in zip(*A)]
def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def inv2(A):
 d=A[0][0]*A[1][1]-A[0][1]*A[1][0];assert d
 return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def sub(A,B):return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def run():
 counts={k:0 for k in ('exact_pair_translation','phase_countercontrol',
                      'whole_frame','positive_level')}
 def check(v,k):assert v,k;counts[k]+=1
 vals=[(F(1),F(0)),(F(0),F(1)),(F(1,2),F(-1,3))]
 phases=[(F(1),F(0)),(F(-1),F(0)),(F(3,5),F(4,5)),(F(-4,5),F(3,5))]
 for R in (F(1),F(9,8),F(5,4),F(3,2)):
  c=(R+1/R)/2;s=(R-1/R)/2
  for phase in phases:
   for p in vals:
    for n in vals:
     pt=gm(phase,ga(gs(c,p),gs(s,n)))
     nt=gm(phase,ga(gs(s,p),gs(c,n)))
     check(c*c-s*s==1,'exact_pair_translation')
     check(gn(pt)-gn(nt)==gn(p)-gn(n),'exact_pair_translation')
     check(gn(pt)+gn(nt)<=R*R*(gn(p)+gn(n)),'exact_pair_translation')
     error=gn(ga(pt,gs(-1,gm(phase,p))))+gn(ga(nt,gs(-1,gm(phase,n))))
     check(error<=(R-1)**2*(gn(p)+gn(n)),'exact_pair_translation')
     # Complete partner sign: beta -> -beta, n -> -n.
     pp=gm(phase,ga(gs(c,p),gs(-s,gs(-1,n))))
     np=gm(phase,ga(gs(-s,p),gs(c,gs(-1,n))))
     check(pp==pt and np==gs(-1,nt),'exact_pair_translation')
     for q in vals:
      for m in vals:
       qt=gm(phase,ga(gs(c,q),gs(s,m)))
       mt=gm(phase,ga(gs(s,q),gs(c,m)))
       check(ga(gm(gc(pt),qt),gs(-1,gm(gc(nt),mt)))==
             ga(gm(gc(p),q),gs(-1,gm(gc(n),m))),'exact_pair_translation')
 # A finite complete-pair source control; not actual zeta coordinates.
 # p_old=(1,1), n_old=(a,0), U=diag(1,-1), hyperbolic c,s.
 # Pell a=p/q approaches sqrt(2) from below, with exact old defect.
 p,q=1,1;examples=[]
 for j in range(1,41):
  a=F(p,q);lam=a*a/2;delta=1-lam
  R=1+F(1,2**j);c=(R+1/R)/2;s=(R-1/R)/2
  A=c+s*a/2;fcrit=c*a+s*delta
  P=[[F(1),c+s*a],[F(1),-c]]
  N=[[a,s+c*a],[F(0),-s]]
  M=mm(tr(P),P);Q=sub(M,mm(tr(N),N))
  check(p*p-2*q*q==-1 and delta==F(1,2*q*q),'phase_countercontrol')
  check(M[0][0]==2 and M[0][1]==s*a,'phase_countercontrol')
  check(Q[0][0]==Q[1][1]==2*delta,'phase_countercontrol')
  check(Q[0][1]==-c*a*a,'phase_countercontrol')
  # Positive source inverse stays protected independent of old signed gap.
  check(M[1][1]-1-M[0][1]**2>0,'phase_countercontrol')
  check(M[0][0]+M[1][1]<7,'phase_countercontrol')
  projection=s*a/2
  z=[[-projection],[F(1)]]
  check(mm(P,z)==[[A],[-A]],'phase_countercontrol')
  check(mm(N,z)==[[fcrit],[-s]],'phase_countercontrol')
  leakage=fcrit*fcrit/(2*A*A)
  criticalcost=leakage/delta;low=s*s/(2*A*A);cost=criticalcost+low
  schur=Q[1][1]-Q[0][1]**2/Q[0][0]
  check(schur/(2*A*A)==1-cost,'phase_countercontrol')
  check(cost>1 and schur<0,'phase_countercontrol')
  check(criticalcost>lam/(4*delta),'phase_countercontrol')
  # Pure phase commutator on old unit positive vector has squared norm lam.
  T=[[a/2,a/2],[F(0),F(0)]];U=[[F(1),F(0)],[F(0),F(-1)]]
  comm=sub(mm(U,T),mm(T,U));onold=mm(comm,[[F(1)],[F(1)]])
  check(onold==[[a],[F(0)]],'phase_countercontrol')
  check(sum((row[0]**2 for row in onold),F(0))/2==lam,'phase_countercontrol')
  check(((fcrit-a)**2+s*s)/2<=4*(R-1)**2,'phase_countercontrol')
  # Independent CC20 forced covariance, including h_old positive norm2.
  J=[[Q[0][k]-delta*M[0][k] for k in range(2)]]
  cov=mm(mm(J,inv2(M)),tr(J))[0][0]/2
  check(J[0][0]==0 and J[0][1]==-a*fcrit,'phase_countercontrol')
  check(cov==lam*leakage,'phase_countercontrol')
  if j in (1,4,16,40):examples.append({'j':j,'old_defect':str(delta),
     'boost_exponential':str(R),'critical_leakage':str(leakage),
     'weighted_critical_cost':str(criticalcost),'low_cost':str(low),
     'positive_gram_lower':'1','positive_gram_upper':'7',
     'scope':'finite pair-law/phase control; not actual zeta or full physical translation model'})
  p,q=3*p+4*q,2*p+3*q
 # Whole incoming right inverse, all columns and all mixed products.
 # Algebra controls for the analytic physical partition construction.
 for b in (F(-1),F(0),F(1,2)):
  A=[[F(1),F(0),F(1),b],[F(0),F(1),F(0),F(1)]]
  W=mm(A,tr(A));Wi=inv2(W);R=mm(tr(A),Wi)
  check(mm(A,R)==[[F(1),F(0)],[F(0),F(1)]],'whole_frame')
  check(mm(tr(R),R)==Wi,'whole_frame')
  D=sub([[F(1),F(0)],[F(0),F(1)]],Wi)
  check(D[0][0]>=0 and D[1][1]>=0 and
        D[0][0]*D[1][1]-D[0][1]*D[1][0]>=0,'whole_frame')
  for k in (F(1,8),F(1,2),F(2)):
   K=[[k,F(1,5)],[F(1,7),-k]];Frow=mm(K,A)
   check(mm(Frow,R)==K,'whole_frame')
   check(mm(mm(mm(Frow,R),tr(R)),tr(Frow))==mm(K,tr(K)),
         'whole_frame')
 # Genuine positive physical level; full added mass channel, not a pair row.
 a,k,mu=F(9,25),F(12,25),F(16,25)
 original=k*k/(1-a*a)
 lam=a*a+mu;delta=1-lam
 crit=a*a*k*k/(lam*delta);low=k*k+mu-a*a*k*k/lam
 check(original==F(9,34)<1,'positive_level')
 check(crit+low==1,'positive_level')
 shiftedN=[[a,k],[F(4,5),F(0)],[F(0),F(4,5)]]
 Q=sub([[F(1),F(0)],[F(0),F(1)]],mm(tr(shiftedN),shiftedN))
 check(Q[1][1]-Q[0][1]**2/Q[0][0]==0,'positive_level')
 check(a*a+k*k==1-mu,'positive_level')
 check(lam>a*a and delta<1-a*a,'positive_level')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==11308
 return {'stage':'CC21 exact translation candidate and phase commutator gate',
   'classification':'A: actual boost bound and whole-shell generation; C: boost-only continuation inference rejected',
   'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
   'inherited_cc20_checks':11308,'total_exact_checks':sum(counts.values())+11308,
   'finite_phase_controls':examples,
   'actual_gap_independent_boost_bound':'||Gamma(tau_r h)-U_r Gamma(h)|| <= (exp(3|r|/8)-1)||Gamma(h)||',
   'whole_shell_generation':'two opposite translated old windows with a fixed bounded smooth partition',
   'remaining_arithmetic_target':'whole critical defect-weighted covariance of F_-h,F_+h, including the phase/gain commutator and low output',
   'phase_cancellation_on_old_range_proved':False,
   'actual_arithmetic_relative_bound_certified':False,
   'actual_zeta_bound_disproved':False,'actual_zeta_critical_matrix_evaluated':False,
   'new_aperture':False,'global_nonstalling':False,'lean_certified':False,
   'whole_domain_anchor':'21/20 inherited CC18, even0/odd0',
   'scope':'Actual analytic divisor/partition lemmas; finite source controls are not actual zeta or complete physical models.',
   'input_sha256':{'cc20_validator':hashlib.sha256((ROOT/'scripts/validate_native_forced_source_cc20.py').read_bytes()).hexdigest(),
      'cc20_validation':hashlib.sha256((ROOT/'notes/data/RPB108_FORCED_SOURCE_CC20_VALIDATION_20261008.json').read_bytes()).hexdigest()},
   'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_TRANSLATION_CANDIDATE_CC21_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
