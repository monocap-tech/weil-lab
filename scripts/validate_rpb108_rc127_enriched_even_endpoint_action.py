"""RC127: full three-vector even endpoint action with paid infinite output.
Standalone directed-arithmetic validator; no original Weil response claim.
"""
from fractions import Fraction as F
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
from math import isqrt
import argparse, hashlib, json

lc=Context(prec=70,rounding=ROUND_FLOOR)
hc=Context(prec=70,rounding=ROUND_CEILING)
Z=(D(0),D(0)); B=F(11,10); GRID=10**40
def down(x,g=GRID):return F(x.numerator*g//x.denominator,g)
def up(x,g=GRID):return -down(-x,g)
def sqrtup(x):
 assert x>=0
 t=(x.numerator*GRID*GRID+x.denominator-1)//x.denominator
 n=isqrt(t)
 return F(n+(n*n<t),GRID)
def rat(x):
 x=F(x);return lc.divide(D(x.numerator),D(x.denominator)),hc.divide(D(x.numerator),D(x.denominator))
def plus(a,b):return lc.add(a[0],b[0]),hc.add(a[1],b[1])
def minus(a,b):return lc.subtract(a[0],b[1]),hc.subtract(a[1],b[0])
def mul(a,b):
 assert a[0]>=0 and b[0]>=0
 return lc.multiply(a[0],b[0]),hc.multiply(a[1],b[1])
def div(a,b):
 assert a[0]>=0 and b[0]>0
 return lc.divide(a[0],b[1]),hc.divide(a[1],b[0])
def bounds(a):return down(F(a[0])),up(F(a[1]))
def ser(A):return [[str(x) for x in row] for row in A]
def psd(A):
 A=[r[:] for r in A];n=len(A)
 assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
 for k in range(n):
  d=A[k][k]
  if d<0:return False
  if d==0:
   if any(A[k][j] for j in range(k+1,n)):return False
  else:
   for i in range(k+1,n):
    for j in range(k+1,n):A[i][j]-=A[i][k]*A[k][j]/d
 return True
def loewner(L,U,weights):
 n=len(L);mid=[[(L[i][j]+U[i][j])/2 for j in range(n)] for i in range(n)]
 rad=[[(U[i][j]-L[i][j])/2 for j in range(n)] for i in range(n)]
 e=[sum(rad[i][j]*weights[i]/weights[j] for j in range(n)) for i in range(n)]
 return [[mid[i][j]-(e[i] if i==j else 0) for j in range(n)] for i in range(n)],[[mid[i][j]+(e[i] if i==j else 0) for j in range(n)] for i in range(n)],e

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,joint=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC126' and joint['milestone']=='RC124' and prior['input_sha256'][1]==hs[1]
 pr=prior['parity_finite_response_variance_certificates'][0]
 jr=joint['parity_actual_joint_endpoint_moment_certificates'][0]
 assert pr['parity']==jr['parity']=='even' and pr['tail_cutoff']==jr['tail_cutoff']==989
 M=989;R=2047;L=4095
 g0l=F(jr['Gamma_0_Loewner_lower'][0][0]);g0u=F(jr['Gamma_0_Loewner_upper'][0][0])
 sl=g0l/(2*B);sh=g0u/(2*B);s=(rat(sl)[0],rat(sh)[1])
 h00l=F(jr['endpoint_pairing_entry_lower'][0][0]);h00u=F(jr['endpoint_pairing_entry_upper'][0][0])
 log=(rat(1-h00u/(2*B))[0],rat(1-h00l/(2*B))[1])
 H=[Z]
 for n in range(1,2*L+1):H.append(plus(H[-1],rat(F(1,n))))
 dn={n:plus(H[n],s) for n in range(0,L+1,2)}
 diag={n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),log) for n in range(0,L+1,2)}
 assert all(v[0]>0 for v in diag.values())
 coeff={};rounded={}
 for x in pr['finite_response_Legendre_coefficient_intervals']:
  n=x['degree'];v=div(rat(F(2*n+1,n*(n+1))),dn[n]);coeff[n]=v
  center=F(x['center']);radius=F(x['radius']);rounded[n]=center
  assert center-radius<=F(v[0]) and F(v[1])<=center+radius
 assert len(coeff)==494
 psi={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(M+1,R+1,2)}
 def gram_tail(cut):
  # Monotone preceding width-two cells, H_n >= H_cut and D_n >= s+H_cut.
  dlow=F(plus(H[cut],s)[0])
  return up(B/(dlow*(cut-1)*cut))
 tailR=gram_tail(R-1);tailL=gram_tail(L-1)
 gs=[(g0l,g0u),(F(jr['analytic_tail_D_norm_squared_lower']),F(jr['analytic_tail_D_norm_squared_upper'])),(F(pr['finite_response_D_energy_squared_lower']),F(pr['finite_response_D_energy_squared_upper']))]
 GL=[[gs[i][0] if i==j else F(0) for j in range(3)] for i in range(3)]
 GU=[[gs[i][1] if i==j else F(0) for j in range(3)] for i in range(3)]
 def kernel(n,m):
  if n==m:return mul(rat(2*B/F(2*n+1)),diag[n])
  return rat(2*B/F(abs(n-m)*(n+m+1)))
 # Complete f/f pairing. Positive same-parity kernel permits directed sums.
 ff=Z;ns=list(coeff);order=ns[::-1] if replay else ns
 for n in order:
  ff=plus(ff,mul(kernel(n,n),mul(coeff[n],coeff[n])))
  for m in order:
   if m>n:ff=plus(ff,mul(rat(2),mul(kernel(n,m),mul(coeff[n],coeff[m]))))
 ffl,ffu=bounds(ff)
 fp=Z
 for m in order:
  for n in (list(psi)[::-1] if replay else psi):fp=plus(fp,mul(kernel(n,m),mul(coeff[m],psi[n])))
 fpl,fpu=bounds(fp)
 asum=Z
 for m in order:asum=plus(asum,coeff[m])
 asumU=up(F(asum[1]));firstR=R+1
 missingMixed=up(tailR*asumU/(1-F((M-1)*M,firstR*(firstR+1))))
 HL=[[h00l,gs[1][0],gs[2][0]],[gs[1][0],F(jr['actual_analytic_tail_endpoint_energy_lower']),fpl],[gs[2][0],fpl,ffl]]
 HU=[[h00u,gs[1][1],gs[2][1]],[gs[1][1],F(jr['actual_analytic_tail_endpoint_energy_upper']),fpu+missingMixed],[gs[2][1],fpu+missingMixed,ffu]]
 weights=[sqrtup(v[1]) for v in gs]
 Hlo,Hhi,Herr=loewner(HL,HU,weights)
 assert psd(Hlo) and psd([[GL[i][j]-Hhi[i][j] for j in range(3)] for i in range(3)])
 # Explicit signed operator action. All tested coefficients and kernel entries are positive.
 # q is a rational finite action trial, never an assumed invariant compression.
 sources=[{0:rat(1)},psi,coeff];q=[{}, {}, {}];radEnergy=[F(0)]*3
 for j,u in enumerate(sources):
  jobs=list(u);jobs=jobs[::-1] if replay else jobs
  for n in range(0,L+1,2):
   val=Z
   for m in jobs:
    # h coefficient = d_n on diagonal; (2n+1)/|z_n-z_m| off diagonal.
    entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
    val=plus(val,mul(entry,u[m]))
   val=div(val,dn[n]);cl,cu=bounds(val);center=down((cl+cu)/2);radius=max(center-cl,cu-center)
   q[j][n]=center
   radEnergy[j]+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius)
  print('RC127 action column',j,'complete',flush=True)
 # For finite input u: |(Cu)_n| <= psi_n * sum|u_m|/(1-z_max/z_first).
 tailErrors=[];actionErrors=[]
 for j,u in enumerate(sources):
  total=Z
  for m in (list(u)[::-1] if replay else u):total=plus(total,u[m])
  last=max(u);first=L+1;factor=up(F(total[1])/(1-F(last*(last+1),first*(first+1))))
  tout=up(tailL*factor*factor);tailErrors.append(tout)
  actionErrors.append(up(sqrtup(radEnergy[j])+sqrtup(tout)+(sqrtup(tailR) if j==1 else 0)))
 # Finite trial Gram, followed by a full action-Gram enclosure with norm error paid.
 QL=[[F(0)]*3 for _ in range(3)];QU=[[F(0)]*3 for _ in range(3)]
 degrees=list(range(0,L+1,2));degrees=degrees[::-1] if replay else degrees
 for i in range(3):
  for j in range(i,3):
   val=Z
   for n in degrees:val=plus(val,mul(mul(rat(2*B/F(2*n+1)),dn[n]),rat(q[i][n]*q[j][n])))
   QL[i][j],QU[i][j]=bounds(val);QL[j][i]=QL[i][j];QU[j][i]=QU[i][j]
 norms=[sqrtup(QU[i][i]) for i in range(3)]
 H2L=[[F(0)]*3 for _ in range(3)];H2U=[[F(0)]*3 for _ in range(3)]
 for i in range(3):
  for j in range(3):
   e=up(actionErrors[i]*norms[j]+actionErrors[j]*norms[i]+actionErrors[i]*actionErrors[j])
   H2L[i][j]=max(F(0),QL[i][j]-e);H2U[i][j]=QU[i][j]+e
 # The exact CP0=a P0+psi0+f0 identity tightens the whole first row.
 al=h00l/g0u;au=h00u/g0l
 for j in range(3):
  lower=al*HL[0][j]+HL[1][j]+HL[2][j];upper=au*HU[0][j]+HU[1][j]+HU[2][j]
  H2L[0][j]=H2L[j][0]=max(H2L[0][j],down(lower))
  H2U[0][j]=H2U[j][0]=min(H2U[0][j],up(upper))
  assert H2L[0][j]<=H2U[0][j]
 # R=H2-HG^-1H; exact symbolic P0 residual vanishes.
 RL=[[F(0)]*3 for _ in range(3)];RU=[[F(0)]*3 for _ in range(3)]
 for i in range(1,3):
  for j in range(1,3):
   pl=sum(HL[i][k]*HL[k][j]/gs[k][1] for k in range(3))
   pu=sum(HU[i][k]*HU[k][j]/gs[k][0] for k in range(3))
   RL[i][j]=down(H2L[i][j]-pu);RU[i][j]=up(H2U[i][j]-pl)
   if i==j:RL[i][j]=max(F(0),RL[i][j]);RU[i][j]=min(RU[i][j],gs[i][1])
   assert RL[i][j]<=RU[i][j]
 Rlo,Rhi,Rerr=loewner(RL,RU,weights)
 assert psd(Rhi)
 frel=down(RL[2][2]/gs[2][1],10**12)
 assert frel>F(18,1000)
 # A positive diagonal upper also follows directly from residual Cauchy-Schwarz.
 rdiag=[F(0),2*RU[1][1],2*RU[2][2]]
 assert all(x>=0 for x in rdiag)
 SigmaL=[[F(3,4)*GL[i][j]-Hhi[i][j]/4 for j in range(3)] for i in range(3)]
 SigmaU=[[GU[i][j]-Hlo[i][j]/2 for j in range(3)] for i in range(3)]
 assert psd(SigmaL) and psd([[SigmaU[i][j]-SigmaL[i][j] for j in range(3)] for i in range(3)])
 payload=[dict(degree=n,coefficients=[str(q[j][n]) for j in range(3)]) for n in range(0,L+1,2)]
 return dict(milestone='RC127',status='PASS: enriched even joint endpoint action, first moment and paid second-moment/covariance enclosures',input_sha256=hs,starting_commit='c72b672465a8172f9f04cb98ceaf3669e495fc0b',aperture='11/10',joint_family=['P_0','actual infinite psi_0','exact symbolic collective f_0'],finite_response_cutoff=M,analytic_input_prefix_cutoff=R,finite_action_output_cutoff=L,arithmetic='70-digit directed positive coefficient sums; exact rational interval-to-Loewner and norm-tail acceptance',D_Gram_Loewner_lower=ser(GL),D_Gram_Loewner_upper=ser(GU),endpoint_pairing_entry_lower=ser(HL),endpoint_pairing_entry_upper=ser(HU),endpoint_pairing_Loewner_lower=ser(Hlo),endpoint_pairing_Loewner_upper=ser(Hhi),endpoint_weighted_interval_error_diagonal=list(map(str,Herr)),finite_tail_mixed_omitted_pairing_upper=str(missingMixed),analytic_input_omitted_D_energy_upper=str(tailR),finite_output_leading_tail_D_energy_upper=str(tailL),finite_action_trial_coefficient_sha256=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest(),finite_action_trial_coefficient_count_per_column=len(payload),finite_action_trial_generator='run: equation (10), directed bounds, 1e-40 rational centers, degrees 0..4094 even',finite_action_trial_rounding_D_energy_upper=list(map(str,radEnergy)),finite_source_action_output_tail_D_energy_upper=list(map(str,tailErrors)),full_action_D_norm_error_upper=list(map(str,actionErrors)),action_trial_Gram_entry_lower=ser(QL),action_trial_Gram_entry_upper=ser(QU),endpoint_second_moment_entry_lower=ser(H2L),endpoint_second_moment_entry_upper=ser(H2U),projected_covariance_entry_lower=ser(RL),projected_covariance_entry_upper=ser(RU),projected_covariance_Loewner_lower=ser(Rlo),projected_covariance_Loewner_upper=ser(Rhi),projected_covariance_positive_diagonal_Loewner_upper=list(map(str,rdiag)),projected_covariance_is_PSD_by_residual_Gram=True,exact_P0_covariance_row_and_column_zero=True,rounded_f0_exact_invariance_claimed=False,rounded_f0_P0_residual_D_energy_upper=pr['finite_response_center_D_error_squared_upper'],joint_reference_response_Loewner_lower=ser(SigmaL),joint_reference_response_Loewner_upper=ser(SigmaU),full_joint_endpoint_first_moment_certified=True,all_three_action_outputs_have_paid_infinite_error=True,full_second_moment_and_covariance_enclosed=True,analytic_tail_covariance_small_certified=False,finite_response_covariance_over_own_D_Gram_lower=str(frel),whole_enriched_small_variance_target_below_this_lower_impossible=True,high_accuracy_reference_response_completed=False,regular_multiplier_action_evaluated=False,original_Weil_or_augmented_actions_performed=False,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,new_positive_native_directions_certified=0,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=2);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC127 PASS: full enriched even endpoint action enclosed; accurate inverse and original Weil response remain open')
