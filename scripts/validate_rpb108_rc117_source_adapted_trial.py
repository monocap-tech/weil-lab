"""RC117 source-adapted canonical trial: retain the complete physical source shape.
Inputs RC116 RC115 RC112 RC67 RC56. No original Weil/augmented action.
"""
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal as D,Context,ROUND_FLOOR,ROUND_CEILING
from math import comb
from validate_rpb108_rc29_atom_reduction import legendre
import argparse,json,hashlib
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root
from validate_rpb108_rc116_canonical_adjoint_trials import sqrt_lower
from validate_rpb108_rc44_reduced_native_head import exp_bounds

lc=Context(prec=700,rounding=ROUND_FLOOR);hc=Context(prec=700,rounding=ROUND_CEILING)
def mrat(a,q):
 if q<0:return mrat((a[1].copy_negate(),a[0].copy_negate()),-q)
 return lc.divide(lc.multiply(a[0],D(q.numerator)),D(q.denominator)),hc.divide(hc.multiply(a[1],D(q.numerator)),D(q.denominator))
def plus(a,b):return lc.add(a[0],b[0]),hc.add(a[1],b[1])
def minus(a,b):return lc.subtract(a[0],b[1]),hc.subtract(a[1],b[0])
def legendre_source(data,replay=False):
 degree=max(r['native_degree'] for r in data);cs={r['native_degree']:F(r['physical_Chebyshev_coefficient_center']) for r in data};a=[(D(0),D(0)) for _ in range(degree+1)]
 prev=[];cur=[(D(1),D(1))]
 for n in range(degree+1):
  if n in cs:
   for j,t in enumerate(cur):a[j]=plus(a[j],mrat(t,cs[n]))
  if n==degree:break
  nxt=[(D(0),D(0)) for _ in range(n+2)]
  jobs=list(enumerate(cur))
  if replay:jobs.reverse()
  for j,t in jobs:
   nxt[j+1]=plus(nxt[j+1],mrat(t,F(2*(j+1),2*j+1)))
   if j:nxt[j-1]=plus(nxt[j-1],mrat(t,F(2*j,2*j+1)))
  for j,t in enumerate(prev):nxt[j]=minus(nxt[j],t)
  # T1=t rather than 2t*T0.
  if n==0:nxt=[(D(0),D(0)),(D(1),D(1))]
  prev,cur=cur,nxt
 return [(down(F(l),10**80),up(F(h),10**80)) for l,h in a]
def cheb_log_moments(N):
 I=lambda j:F(2,1-j*j) if j%2==0 else F(0)
 d=[F(0),F(2)]
 for j in range(2,N+2):d.append(2*I(j-1)-2*d[-1]-d[-2])
 return [F(2),F(-1)]+[(d[j+1]/(j+1)-d[j-1]/(j-1))/2 for j in range(2,N+1)]
def endpoint(data,B,replay=False):
 den=2*10**70;cs=[(x['native_degree'],int(F(x['physical_Chebyshev_coefficient_center'])*den)) for x in data];N=2*max(j for j,_ in cs);prod=[0]*(N+1)
 for i,(j,a) in enumerate(cs):
  for k,b in cs[i:]:
   v=a*b*(1 if j==k else 2);prod[j+k]+=v;prod[abs(j-k)]+=v
 L=cheb_log_moments(N);terms=[F(v)*L[j] for j,v in enumerate(prod) if v]
 q=B*sum(reversed(terms) if replay else terms,F(0))/(2*den*den);assert q>0
 return down(q,10**20),up(q,10**20)
def log_upper(q):
 k=0
 while q>=2:q/=2;k+=1
 y=(q-1)/(q+1);n=40;s=2*sum((y**(2*j+1)/F(2*j+1) for j in range(n)),F(0));tail=2*y**(2*n+1)/F((2*n+1)*(1-y*y))
 return up(F(694*k,1000)+s+tail,10**20)
def controls():
 # Endpoint log moments independently checked by exact shifted power integration.
 L=cheb_log_moments(24);a,b=[F(1)],[F(0),F(1)]
 for n in range(25):
  p=a if n==0 else b
  shifted=[sum((p[j]*comb(j,k)*2**k*(-1)**(j-k) for j in range(k,len(p))),F(0)) for k in range(len(p))]
  assert 2*sum((x/F(k+1)**2 for k,x in enumerate(shifted)),F(0))==L[n]
  if n>=1:
   new=[F(0)]*(len(b)+1)
   for j,x in enumerate(b):new[j+1]+=2*x
   for j,x in enumerate(a):new[j]-=x
   a,b=b,new
 for n in range(25):
  p=legendre(n);out=[F(0)]*len(p)
  for k,a in enumerate(p):
   H=sum((F(1,j) for j in range(1,k+1)),F(0));out[k]+=2*H*a
   for r in range(1,k,2):out[k-1-r]-=2*a/F(r+1)
  H=sum((F(1,j) for j in range(1,n+1)),F(0))
  assert out==[2*H*a for a in p]
 return 50

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];old,src,cov,metric,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [old,src,cov,metric,prec]]==['RC116','RC115','RC112','RC67','RC56']
 assert [old['input_sha256'][i] for i in [0,2,4]]==hs[1:4] and src['input_sha256'][1]==hs[2] and metric['input_sha256'][3]==hs[4]
 assert exp_bounds(F(1))[1]<F(11,4) and exp_bounds(F(694,1000))[0]>2
 checks=controls();B=F(11,10);cL,cH=map(F,prec['actual_constant_enclosure']);assert cL<cH<0
 T0=F(6);gap=64*F(693,1000)-F(3,4)*2*F(22,7)*B*T0;assert gap>0
 eps=up(4/exp_bounds(gap)[0],10**40);eupper=F(11,4)
 weightint=up(T0*log_upper(1+eupper/T0)+eupper*log_upper(1+T0/eupper),10**12)
 rows=[]
 for idx,r in enumerate(src['parity_rational_Fourier_adjoint_sources']):
  oldr=old['parity_canonical_adjoint_trial_certificates'][idx];data=r['physical_source_coefficient_intervals'];lohi=legendre_source(data,replay);degree=len(lohi)-1
  # Independent physical moments from RC116 verify the connection transform at all 64 old coordinates.
  for j in range(64):
   m=2*B/F(2*j+1)
   assert F(oldr['physical_Legendre_source_pairing_lower'][j])/m<=lohi[j][0]<=lohi[j][1]<=F(oldr['physical_Legendre_source_pairing_upper'][j])/m
  H=F(0);slo=F(0);shi=F(0);normlo=F(0);normhi=F(0)
  for j,(a,b) in enumerate(lohi):
   if j:H+=F(1,j)
   m=2*B/F(2*j+1);l=0 if a<=0<=b else min(a*a,b*b);h=max(a*a,b*b)
   slo+=H*m*l;shi+=H*m*h;normlo+=m*l;normhi+=m*h
  sLo,sHi=down(slo,10**12),up(shi,10**12);epLo,epHi=endpoint(data,B,replay)
  Qlo=F(oldr['physical_source_norm_squared_lower']);Qhi=F(oldr['physical_source_norm_squared_upper']);assert Qlo<=normlo<=normhi<=Qhi
  principalLo=sLo+cL*Qhi+epLo;principalHi=sHi+cH*Qlo+epHi
  tailHi=F(oldr['physical_source_projection_onto_degree_63_squared_tail_upper']);physicalCapHi=up(Qhi-F(oldr['physical_source_projection_onto_degree_63_squared_tail_lower']),10**12)
  low=up(4*B*(root(physicalCapHi,10**80)+eps*root(tailHi,10**80))**2*weightint,10**12)
  high=up(eupper*Qhi/T0,10**12);Ehi=up(principalHi+low+high,10**12);Elo=max(Qlo,down(principalLo,10**12));assert Ehi>=Elo>0
  alpha=down(Qlo/Ehi,10**30);benefit=2*alpha*Qlo-alpha*alpha*Ehi;U=F(oldr['canonical_Riesz_source_norm_squared_upper']);es=F(r['canonical_adjoint_source_error_squared_upper']);err=up(U-benefit,10**12);assert err>0
  exacterr=up((root(err,10**80)+root(es,10**80))**2,10**12)
  line_capture=max(F(0),sqrt_lower(Qlo*Qlo/Ehi,10**80)-root(es,10**80))**2;targetU=up((root(U,10**80)+root(es,10**80))**2,10**12);fraction=down(line_capture/targetU,10**12)
  old_projected_hi=(root(physicalCapHi,10**80)+root(es,10**80))**2
  stronger_old_lower=max(F(0),line_capture-old_projected_hi)
  stronger_old_fraction=max(F(0),1-old_projected_hi/line_capture)
  old_lower=F(oldr['canonical_distance_squared_to_entire_degree_63_trial_space_lower']);beats=exacterr<old_lower
  if r['parity']=='odd':assert beats and fraction>F(4,5)
  rows.append(dict(parity=r['parity'],source_global_phase=r['physical_source_global_phase'],source_physical_polynomial_degree=degree,source_shape_trial_scalar=str(alpha),trial_space_dimension=1,canonical_source_shape_energy_lower=str(Elo),canonical_source_shape_energy_upper=str(Ehi),principal_log_frequency_energy_lower=str(down(principalLo,10**12)),principal_log_frequency_energy_upper=str(up(principalHi,10**12)),Legendre_harmonic_energy_lower=str(sLo),Legendre_harmonic_energy_upper=str(sHi),endpoint_log_energy_lower=str(epLo),endpoint_log_energy_upper=str(epHi),positive_regular_multiplier_energy_upper=str(low+high),regular_low_frequency_energy_upper=str(low),regular_high_frequency_energy_upper=str(high),canonical_trial_error_squared_upper_for_center_source=str(err),canonical_trial_error_squared_upper_for_exact_adjoint=str(exacterr),canonical_energy_capture_fraction_lower_on_source_shape_line=str(fraction),strictly_beats_every_degree_63_trial_by_certified_bounds=beats,strengthened_old_degree_63_canonical_distance_squared_lower=str(down(stronger_old_lower,10**12)),strengthened_old_degree_63_outside_energy_fraction_lower=str(down(stronger_old_fraction,10**12)),exact_adjoint_canonical_norm_squared_lower=str(down(line_capture,10**12)),source_connection_interval_sha256=hashlib.sha256(json.dumps([[str(a),str(b)] for a,b in lohi],separators=(',',':')).encode()).hexdigest(),all_64_independent_physical_pairing_checks_passed=True,full_degree_physical_norm_connection_check_passed=True,original_Weil_form_on_trial_evaluated=False))
 return dict(milestone='RC117',status='PASS: source-adapted one-dimensional canonical trial beats odd V64 obstruction; high-accuracy response remains open',input_sha256=hs,arithmetic='700-digit directed Chebyshev-Legendre connection with exact rational energy/error acceptance',aperture='11/10',principal_constant_enclosure=list(map(str,[cL,cH])),regular_frequency_split=str(T0),old_64_moment_kernel_uniform_error_upper=str(eps),regular_weight_integral_upper=str(weightint),exact_endpoint_and_singular_Legendre_controls=checks,parity_source_adapted_trial_certificates=rows,odd_source_shape_line_certifiably_beats_all_degree_63_trials=True,new_dense_canonical_metric_constructed=False,high_accuracy_canonical_source_realization_completed=False,original_Weil_or_augmented_actions_performed=False,augmented_inverse_responses_computed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
 print('RC117 PASS: source-shape canonical trial beats full odd V64 space; accurate responses remain open')
