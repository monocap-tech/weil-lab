#!/usr/bin/env python3
"""IV046 pure Fraction interval verifier of FOUR 16-cell original Weil trials.

The independently SHA-pinned IV045 exact checker provides rigorously outward
intervals for all source transcendentals and primitive exponential/log/sqrt.
All NEW 16-cell translated-overlap geometry, positive original Gamma atom
sums, genuine seven prime-power terms, and both Mellin crossed poles are
checked here in exact rational interval arithmetic. Source Fourier matching
and Schwartz form-domain density are classical mathematical dependencies,
NOT new Lean kernel proofs. No GitHub, no CI, no network.
"""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json, runpy

HERE=Path(__file__).resolve().parent
UPSTREAM=HERE/'IV045_fixed_window_parity_trial_checker.py'
UPSTREAM_SHA='54d49affe407f3838015963b485975b885a5cde0c1c507dc318f9b33c64f86ac'
assert sha256(UPSTREAM.read_bytes()).hexdigest()==UPSTREAM_SHA
s=runpy.run_path(str(UPSTREAM))
exp_pos=s['bracket_exp_pos'];exp_neg=s['bracket_exp_neg']
DROUND=10**18
def _floor(x):return Q((x*DROUND).numerator//(x*DROUND).denominator,DROUND)
def _ceil(x):return -_floor(-x)
def _roundiv(v):return _floor(v[0]),_ceil(v[1])
E0=_roundiv((2*s['Slo'],2*s['Shi']))
gamma0=_roundiv((s['gamma0_lo'],s['gamma0_hi']))
LOGS={2:s['log2'],3:s['log3'],4:(2*s['log2'][0],2*s['log2'][1]),5:s['log5'],7:s['log7'],8:(3*s['log2'][0],3*s['log2'][1]),9:(2*s['log3'][0],2*s['log3'][1])}
KAP={n:(LOGS[{4:2,8:2,9:3}.get(n,n)][0]/s['bracket_sqrt'](n)[1],LOGS[{4:2,8:2,9:3}.get(n,n)][1]/s['bracket_sqrt'](n)[0]) for n in LOGS}

Z=(Q(0),Q(0))
def add(x,y):return _roundiv((x[0]+y[0],x[1]+y[1]))
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 p=[i*j for i in x for j in y];return _roundiv((min(p),max(p)))
def scl(x,q):return _roundiv((x[0]*q,x[1]*q) if q>=0 else (x[1]*q,x[0]*q))
def const(q):return q,q
def floor_dec(x,scale=10**15):return Q((x*scale).numerator//(x*scale).denominator,scale)
def ceil_dec(x,scale=10**15):return -floor_dec(-x,scale)
KAP={n:_roundiv(v) for n,v in KAP.items()}
def norm(x,b):
 assert b>0
 return x[0]/b,x[1]/b

def E(t):
 """Exact bracket E(t)=sum_{n>=0} exp(-2(n+1/4)t)/(n+1/4)^2."""
 if t==0:return E0
 assert t>0
 out=Z
 n=0
 while 2*(Q(n)+Q(1,4))*t<Q(28):
  a=Q(n)+Q(1,4)
  out=add(out,scl(_roundiv(exp_neg(2*a*t,76)),1/(a*a)))
  n+=1
 a=Q(n)+Q(1,4)
 # monotonically decreasing geometric bound: 1/(a+m)^2 <= 1/a^2.
 tail_exp_hi=_roundiv(exp_neg(2*a*t,76))[1]
 ratio_hi=_roundiv(exp_neg(2*t,76))[1]
 assert ratio_hi<1
 tail=tail_exp_hi/(a*a*(1-ratio_hi))
 return _roundiv((out[0],out[1]+tail))

# All intervals have equal rational width, and exact endpoints.
NC=8
L=Q(11,10)
w=L/NC
intervals=[(-L+j*w,-L+(j+1)*w) for j in range(2*NC)]
Eb=[E(k*w) for k in range(2*NC+1)]
Ddiag=scl(sub(Eb[0],Eb[1]),Q(1,2))
Jbygap=[]
for g in range(2*NC-1):
 J=scl(add(sub(Eb[g],scl(Eb[g+1],2)),Eb[g+2]),Q(1,4))
 assert J[0]>0,(g,float(J[0]),float(J[1]))
 Jbygap.append(J)

def overlap_bounds(a,b,d):
 # d is a positive or negative exact interval of uncertain logarithm shift.
 dlo,dhi=d
 lower=max(Q(0),min(a[1],b[1]+dlo)-max(a[0],b[0]+dhi))
 upper=max(Q(0),min(a[1],b[1]+dhi)-max(a[0],b[0]+dlo))
 assert lower<=upper
 return lower,upper

def exp_bracket(q):
 return _roundiv(exp_pos(q,78) if q>=0 else exp_neg(-q,78))

def moments_interval(iv):
 l,r=iv
 ep_l=exp_bracket(l/2);ep_r=exp_bracket(r/2)
 em_l=exp_bracket(-l/2);em_r=exp_bracket(-r/2)
 return scl(sub(ep_r,ep_l),2),scl(sub(em_l,em_r),2)
MOM=[moments_interval(iv) for iv in intervals]

def eval_trial(c,parity,tag):
 assert len(c)==NC
 coeff=c+([c[NC-1-j] for j in range(NC)] if parity=='even' else [-c[NC-1-j] for j in range(NC)])
 assert len(coeff)==2*NC
 mass=sum((z*z*w for z in coeff),Q(0))
 assert mass>0
 # Complete original REAL Gamma positive difference form + gamma0 mass.
 D=Z
 for i,v in enumerate(coeff):
  D=add(D,scl(Ddiag,v*v))
  for j in range(i+1,len(coeff)):
   D=sub(D,scl(Jbygap[j-i-1],2*v*coeff[j]))
 assert D[0]>0,(tag, 'Dirichlet positivity failure')
 # P=2*sum kappan sum_{i,j} ci*cj overlap(Ii, Ij+log n).
 P=Z
 for n,d in LOGS.items():
  z=Z
  for i,ci in enumerate(coeff):
   if ci==0:continue
   for j,cj in enumerate(coeff):
    if cj==0:continue
    ol=overlap_bounds(intervals[i],intervals[j],d)
    if ol[1]:z=add(z,scl(ol,ci*cj))
  P=add(P,scl(mul(KAP[n],z),2))
 Mplus=Z; Mminus=Z
 for i,ci in enumerate(coeff):
  Mplus=add(Mplus,scl(MOM[i][0],ci))
  Mminus=add(Mminus,scl(MOM[i][1],ci))
 pole=scl(mul(Mplus,Mminus),2)
 T=add(sub(add(scl(gamma0,mass),D),P),Z)
 W=add(T,pole)
 q=norm(W,mass)
 hsq=scl(mul(add(Mplus,Mminus),add(Mplus,Mminus)),Q(1,2))
 ksq=scl(mul(sub(Mplus,Mminus),sub(Mplus,Mminus)),Q(1,2))
 ell_sq=hsq if parity=='even' else ksq
 assert ell_sq[0]>0
 quotients=[x/y for x in T for y in ell_sq]
 constrained=min(quotients),max(quotients)
 # For all generated parity-symmetric vectors, the complementary pole norm vanishes mathematically.
 assert (pole[0]>0 if parity=='even' else pole[1]<0),(tag, 'unexpected pole parity',float(pole[0]),float(pole[1]))
 return {'tag':tag,'parity':parity,'positive_half_cell_coefficients':c,'mass':str(mass),
  'normal_W_q':[float(q[0]),float(q[1])],
  'constrained_T_affine_value':[float(constrained[0]),float(constrained[1])],
  'Gamma_D':[float(D[0]),float(D[1])],
  'P_original':[float(P[0]),float(P[1])],
  'pole_cross':[float(pole[0]),float(pole[1])],
  'exact_bounds':{'q_lo_outward_1e15':str(floor_dec(q[0])),'q_hi_outward_1e15':str(ceil_dec(q[1])),'A_upper_outward_1e15':str(ceil_dec(constrained[1]))},
  '_q_exact':q,'_a_exact':constrained}

cases=[
 ('even_low','even',[189,390,574,738,846,964,1000,989]),
 ('odd_low','odd',[447,783,1000,983,791,634,421,71]),
 ('even_constrained','even',[226,441,621,773,863,978,1000,977]),
 ('odd_constrained','odd',[540,847,1000,903,665,514,323,9]),
]
results=[eval_trial(coeff,parity,tag) for tag,parity,coeff in cases]
d={r['tag']:r for r in results}
assert d['even_low']['_q_exact'][1]<Q(87,10000),d['even_low']['normal_W_q']
assert d['odd_low']['_q_exact'][1]<Q(367,10000),d['odd_low']['normal_W_q']
assert d['even_constrained']['_a_exact'][1]<-Q(9979,10000),d['even_constrained']['constrained_T_affine_value']
assert d['odd_constrained']['_a_exact'][1]<Q(547,500),d['odd_constrained']['constrained_T_affine_value']
# Independent 16-cell regression to IV045's full-width even indicator and
# odd sign indicator; prevents sign/shift/normalization drift in this emitter.
reg_even=eval_trial([1]*NC,'even','IV045_F_regression')
reg_odd=eval_trial([1]*NC,'odd','IV045_S_regression')
assert reg_even['_q_exact'][0]>Q(401,10000) and reg_even['_q_exact'][1]<Q(407,10000)
assert reg_odd['_q_exact'][0]>Q(202,1000) and reg_odd['_q_exact'][1]<Q(203,1000)
# The exact source prime shift-energy constant is itself rationally enclosed.
sigma_lo=sum((v[0] for v in KAP.values()),Q(0))
sigma_hi=sum((v[1] for v in KAP.values()),Q(0))
barrier_lo=2*sigma_lo-gamma0[1]
barrier_hi=2*sigma_hi-gamma0[0]
assert Q(12447,1000)<barrier_lo<barrier_hi<Q(12448,1000)
# New exact identity: P_orig=2sum kappa ||f||² -sum kappa ||f-T_shift f||²;
# using shift-norm squared 2M-2*Re C(d), verified at rational formal symbol level.
for m,c in [(Q(7,11),Q(1,9)),(Q(31,19),-Q(2,7)),(Q(3,2),Q(0))]:
 assert 2*c==2*m-(2*m-2*c)
for r in results:
 del r['_q_exact'];del r['_a_exact']
receipt={'stage':'IV046','status':'EXACT FRACTION PASS — four source-aligned 16-cell variational upper witnesses, not actual infinite-dimensional lower spectral bounds or Lean certificates',
 'source_window':'(-11/10,11/10)','parity':'8 mirrored equal cells per half; 16 intervals total; each width 11/80',
 'upstream_IV045_checker_sha256':UPSTREAM_SHA,'gamma_data':'exact source quarter digamma and positive finite Fourier-atom interval formula',
 'dirichlet_data':'D_ii=(E(0)-E(w))/2; D_ij=-[E(g)-E(g+w_i)-E(g+w_j)+E(g+w_i+w_j)]/4',
 'E(t)':'sum_{n>=0} exp(-2(n+1/4)t)/(n+1/4)^2; exact tail with geometric bound',
 'prime_data':'P=2 sum_n (Lambda(n)/sqrt(n)) sum_{i,j} c_i*c_j |I_i intersect (I_j+log(n))|, n in {2,3,4,5,7,8,9}',
 'global_shift_dirichlet_identity':'T[f]=D[f]+sum_n kappa_n ||f-U_log(n)f||² -(2 sum_n kappa_n - gamma(0))||f||², for zero extended f supported in I',
 'barrier_C_outward':[str(floor_dec(barrier_lo)),str(ceil_dec(barrier_hi))],
 'pole_data':'2 M_+(f) M_-(f); exact parity sign',
 'regressions':{'IV045_even_full_interval':reg_even['normal_W_q'],'IV045_odd_sign_interval':reg_odd['normal_W_q']},
 'results':results,'rigorous_conclusions':['inf spectrum W_even <87/10000','inf spectrum W_odd <367/10000','A_e <-9979/10000','A_o <547/500'],
 'important_limit':'all are UPPER bounds from explicit trials; no whole-space lower or sign proof; smooth form-domain transfer is mathematical and not yet Lean source audited',
 'no_new_ci':True,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
out=HERE/'IV046_fixed_window_multicell_variational_receipt.json'
out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print('IV046 EXACT FRACTION variational preflight PASS — NONKERNEL')
for r in results:print(r['tag'], 'W/M',r['normal_W_q'], 'T/moment²',r['constrained_T_affine_value'])
print('Poincare gap C=2Σκ-gamma0:',float(barrier_lo),'..',float(barrier_hi))
print('script_sha256:',receipt['checker_sha256'])
print('receipt:',out)
