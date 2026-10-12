"""RC120: full endpoint residual of harmonic-diagonal reference inverse trials.
No regular multiplier, canonical inverse iteration, or original Weil action.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D
import argparse,json,hashlib
from validate_rpb108_rc117_source_adapted_trial import legendre_source,cheb_log_moments,endpoint,mrat,plus,minus,lc,hc
from validate_rpb108_rc119_reference_preconditioned_source_solver import log2_bounds
from validate_rpb108_rc115_rational_fourier_adjoint import machin
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root
from validate_rpb108_rc116_canonical_adjoint_trials import sqrt_lower

def moment_vectors(N):
 # K_n= integral T_n h^2; basis [1,log2,log2^2,pi^2].
 I=lambda j:F(2,1-j*j) if j%2==0 else F(0)
 L=cheb_log_moments(N);K0=[F(4),F(-4),F(2),F(-1,6)];K=[K0]+[[F(0)]*4 for _ in range(N)]
 A=C=F(0)
 for n in range(2,N+1,2):
  j=n-1;A+=j*(L[j+1]+L[j-1]);C-=j*(I(j+1)+I(j-1));den=F(n*n-1)
  K[n]=[-K0[0]/den+2*A/den,-K0[1]/den+2*C/den,-K0[2]/den,-K0[3]/den]
 return K

def controls():
 # Independent beta-derivative monomial moments, exact four-symbol arithmetic.
 K=moment_vectors(24);p0=[F(1)];p1=[F(0),F(1)]
 for n in range(25):
  p=p0 if n==0 else p1;v=[F(0)]*4
  for j,x in enumerate(p):
   if j%2:continue
   k=j//2;O=sum((F(1,2*r-1) for r in range(1,k+2)),F(0));O2=sum((F(1,(2*r-1)**2) for r in range(1,k+2)),F(0));z=[4*(O*O+O2)/F(4*k+2),-8*O/F(4*k+2),F(4,4*k+2),-F(1,3*(4*k+2))]
   for t in range(4):v[t]+=x*z[t]
  assert v==K[n]
  if n>=1:
   new=[F(0)]*(len(p1)+1)
   for j,x in enumerate(p1):new[j+1]+=2*x
   for j,x in enumerate(p0):new[j]-=x
   p0,p1=p1,new
 return 25

def connect_legendre_to_cheb(v,replay=False):
 N=len(v)-1;prev=[];cur=[(D(1),D(1))];out=[(D(0),D(0)) for _ in range(N+1)]
 for n in range(N+1):
  for j,x in enumerate(cur):out[j]=plus(out[j],mrat(x,v[n]))
  if n==N:break
  xp=[(D(0),D(0)) for _ in range(n+2)];jobs=list(enumerate(cur))
  if replay:jobs.reverse()
  for j,x in jobs:
   if j==0:xp[1]=plus(xp[1],x)
   else:
    xp[j-1]=plus(xp[j-1],mrat(x,F(1,2)));xp[j+1]=plus(xp[j+1],mrat(x,F(1,2)))
  nxt=[mrat(x,F(2*n+1,n+1)) for x in xp]
  for j,x in enumerate(prev):nxt[j]=minus(nxt[j],mrat(x,F(n,n+1)))
  prev,cur=cur,nxt
 data=[]
 for j,(lo,hi) in enumerate(out):
  if lo==hi==0:continue
  mid=down((F(lo)+F(hi))/2,10**70);rad=up(max(abs(mid-F(lo)),abs(mid-F(hi))),10**80)
  data.append(dict(native_degree=j,physical_Chebyshev_coefficient_center=str(mid),physical_Chebyshev_coefficient_radius=str(rad)))
 return data

def product_coeff(a,b):
 den=2*10**70;aa=[(x['native_degree'],int(F(x['physical_Chebyshev_coefficient_center'])*den)) for x in a];bb=[(x['native_degree'],int(F(x['physical_Chebyshev_coefficient_center'])*den)) for x in b];out=[0]*(max(j for j,_ in aa)+max(j for j,_ in bb)+1)
 for j,x in aa:
  for k,y in bb:out[j+k]+=x*y;out[abs(j-k)]+=x*y
 return out,2*den*den

def physical_pair(a,b,B,replay=False):
 v,den=product_coeff(a,b);terms=[F(x)*F(2,1-j*j) for j,x in enumerate(v) if x and j%2==0]
 return B*sum(reversed(terms) if replay else terms,F(0))/den

def endpoint_squared(data,B,l2,pi,replay=False):
 prod,den=product_coeff(data,data);K=moment_vectors(len(prod)-1);v=[F(0)]*4;jobs=list(enumerate(prod))
 if replay:jobs.reverse()
 for j,x in jobs:
  if x:
   for t in range(4):v[t]+=F(x)*K[j][t]
 v=[B*x/den for x in v];lo=hi=F(0);bs=[(F(1),F(1)),l2,(l2[0]**2,l2[1]**2),(pi[0]**2,pi[1]**2)]
 for c,(a,b) in zip(v,bs):lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 assert lo>0
 return down(lo,10**30),up(hi,10**30)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,src,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [prior,src,prec]]==['RC119','RC115','RC56'] and prior['input_sha256'][1:]==hs[1:]
 checks=controls();B=F(11,10);r=F(prior['positive_principal_reference_shift']);slo=F(prior['reference_form_floor_lower']);cl,ch=map(F,prec['actual_constant_enclosure']);ll,lh=log2_bounds(replay);smid=r+(cl+ch+ll+lh)/2;delta=(ch-cl+lh-ll)/2
 pl,ph=machin();p0=F(src['rational_pi']);epi=F(src['rational_pi_error_upper']);assert p0-epi<=pl<ph<=p0+epi
 rows=[]
 for source in src['parity_rational_Fourier_adjoint_sources']:
  data=source['physical_source_coefficient_intervals'];ab=legendre_source(data,replay);N=len(ab)-1;H=F(0);v=[];poly2=J=Jl=F(0)
  for j,(a,b) in enumerate(ab):
   if j:H+=F(1,j)
   mid=(a+b)/2;w=down(mid/(H+smid),10**70);v.append(w);e=max(abs(a-(H+smid)*w),abs(b-(H+smid)*w));mass=2*B/F(2*j+1);poly2+=up(mass*e*e,10**160);J+=up(mass*H*w*w,10**70);Jl+=down(mass*H*w*w,10**70)
  wdata=connect_legendre_to_cheb(v,replay);rad=sum((F(z['physical_Chebyshev_coefficient_radius']) for z in wdata),F(0));pe=root(2*B,10**90)*rad
  Q=physical_pair(wdata,wdata,B,replay);pair=physical_pair(data,wdata,B,replay);assert Q>0 and pair>0
  polyerr=root(poly2,10**90)+(H+smid)*pe+delta*root(Q,10**90)
  h2lo,h2hi=endpoint_squared(wdata,B,(ll,lh),(pl,ph),replay)
  residual2=up((root(h2hi,10**90)+polyerr)**2,10**30);errorP=up(residual2/slo,10**30)
  Jhi=up((root(J,10**90)+root(H,10**90)*pe)**2,10**30);Jlo=max(F(0),down((max(F(0),sqrt_lower(Jl,10**90)-root(H,10**90)*pe))**2,10**30))
  eplo,ephi=endpoint(wdata,B,replay);Plo=down(Jlo+(cl+r)*Q+eplo,10**30);Phi=up(Jhi+(ch+r)*Q+ephi,10**30);assert Plo>0
  Clo=down(2*pair-Phi,10**30);Chi=up(2*pair-Plo,10**30);assert Clo>0
  refupper=Chi+errorP;capture=down(Clo/refupper,10**12);rel=up(errorP/Clo,10**12)
  source_rad=sum((F(z['physical_Chebyshev_coefficient_radius']) for z in data),F(0));source_err=root(2*B,10**90)*source_rad;pair_err=source_err*root(Q,10**90);targetClo=down(Clo-2*pair_err,10**30);targetChi=up(Chi+2*pair_err,10**30);targetErr=up((root(residual2,10**90)+source_err)**2/slo,10**30);assert targetClo>0
  targetUpper=targetChi+targetErr;targetRel=up(targetErr/targetClo,10**12);targetCapture=down(targetClo/targetUpper,10**12)
  rows.append(dict(parity=source['parity'],source_global_phase=source['physical_source_global_phase'],polynomial_degree=N,trial_Chebyshev_coefficients=wdata,trial_Legendre_proposal_sha256=hashlib.sha256(json.dumps(list(map(str,v)),separators=(',',':')).encode()).hexdigest(),trial_physical_norm_squared=str(Q),physical_source_trial_pairing=str(pair),endpoint_log_squared_energy_lower=str(h2lo),endpoint_log_squared_energy_upper=str(h2hi),polynomial_reference_residual_norm_error_upper=str(up(polyerr,10**60)),full_physical_reference_residual_squared_upper=str(residual2),reference_inverse_trial_P_error_squared_upper=str(errorP),reference_trial_P_energy_lower=str(Plo),reference_trial_P_energy_upper=str(Phi),signed_reference_response_lower=str(Clo),signed_reference_response_upper=str(Chi),exact_reference_response_upper=str(refupper),relative_reference_inverse_P_error_squared_upper=str(rel),reference_inverse_trial_energy_capture_fraction_lower=str(capture),exact_rational_model_source_physical_error_norm_upper=str(up(source_err,10**60)),exact_rational_model_reference_inverse_trial_P_error_squared_upper=str(targetErr),exact_rational_model_reference_response_lower=str(targetClo),exact_rational_model_reference_response_upper=str(targetUpper),exact_rational_model_relative_reference_inverse_P_error_squared_upper=str(targetRel),exact_rational_model_reference_energy_capture_fraction_lower=str(targetCapture),physical_source_coefficient_errors_paid=True,residual_annihilation_outside_finite_trial_space_assumed=False,full_endpoint_residual_in_L2_certified=True,canonical_Riesz_source_trial_claimed=False))
 return dict(milestone='RC120',status='PASS: two implemented principal-reference inverse trials with full physical endpoint residuals',input_sha256=hs,aperture='11/10',arithmetic='700-digit directed connections; exact logarithm-squared moment vectors and signed residual acceptance',reference_form_floor_lower=str(slo),exact_endpoint_squared_moment_controls=checks,parity_reference_inverse_action_certificates=rows,two_source_reference_error_Gram_is_diagonal_by_parity=True,two_source_reference_response_lower_and_upper_Gram_certified=True,reference_inverse_approximate_trials_implemented=True,reference_inverse_high_accuracy_contract_completed=False,full_auxiliary_range_reference_actions_certified=False,positive_regular_multiplier_action_evaluated=False,canonical_Riesz_iteration_performed=False,original_Weil_or_augmented_actions_performed=False,augmented_inverse_responses_computed=False,auxiliary_response_norm_below_one_certified=False,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,new_positive_native_directions_certified=0,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC120 PASS: reference source-pair trials and full endpoint residuals; full-range actions open')
