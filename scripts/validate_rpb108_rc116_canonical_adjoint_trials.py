"""RC116 canonical trials for RC115 adjoint sources; no Weil action evaluated.
Inputs RC115 RC114 RC112 RC107 RC67. Exact physical moments and canonical metric.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
from decimal import Decimal as D,localcontext,ROUND_HALF_EVEN
from validate_rpb108_rc47_correlated_native_transport import matrix,root
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc29_atom_reduction import legendre
from math import isqrt

def legendre_cheb(n):
 p=[[F(1)],[F(0),F(1)]]
 for k in range(1,n-1):
  v=[F(0)]*(k+2)
  for j,a in enumerate(p[k]):
   if j==0:v[1]+=a
   else:v[j-1]+=a/2;v[j+1]+=a/2
  v=[F(2*k+1,k+1)*x for x in v]
  for j,a in enumerate(p[k-1]):v[j]-=F(k,k+1)*a
  p.append(v)
 return p[:n]

def source_moments(data,B,replay=False):
 den=2*10**70;coeff=[(r['native_degree'],int(F(r['physical_Chebyshev_coefficient_center'])*den)) for r in data]
 assert all(F(v,den)==F(r['physical_Chebyshev_coefficient_center']) for (_,v),r in zip(coeff,data))
 products=[0]*(2*max(j for j,_ in coeff)+1)
 for a,(j,x) in enumerate(coeff):
  for k,y in coeff[a:]:
   w=x*y*(1 if j==k else 2);products[j+k]+=w;products[abs(j-k)]+=w
 terms=[F(v,1-m*m) for m,v in enumerate(products) if v]
 norm2=B*sum(reversed(terms) if replay else terms,F(0))/den**2;assert norm2>0
 moments=[]
 for l in range(64):
  if (l-coeff[0][0])%2:moments.append(F(0));continue
  terms=[F(x,1-(j+l)**2)+F(x,1-(j-l)**2) for j,x in coeff]
  moments.append(B*sum(reversed(terms) if replay else terms,F(0))/den)
 P=legendre_cheb(64);f=[]
 for k in range(64):
  ts=[a*moments[l] for l,a in enumerate(P[k])]
  f.append(sum(reversed(ts) if replay else ts,F(0)))
 return norm2,f

def log_lower(q):
 assert q>1;k=0
 while q>=2:q/=2;k+=1
 y=(q-1)/(q+1);r=F(693*k,1000)+2*sum((y**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
 return down(r,10**12)
def ambient_dual(T,odd,replay=False):
 terms=[]
 for j in range(128):
  a=T*j/128;b=T*(j+1)/128;w=max(F(1),log_lower(F(8,3)+a))
  mass=(b**3-a**3)/(3*T*T) if odd else b-a
  terms.append(2*mass/w)
 return up(sum(reversed(terms) if replay else terms,F(0)),10**12)
def quad(v,G,replay=False):
 terms=[v[i]*G[i][j]*v[j] for i in range(64) for j in range(64)]
 return sum(reversed(terms) if replay else terms,F(0))

def sqrt_lower(q,d):
 assert q>=0
 return F(isqrt(q.numerator*d*d//q.denominator),d)
def polynomial_canonical_factor(degree,B):
 S=F((degree+1)**2*(degree+3)**2,2*B);K=1
 while F(8,3)**K<=S+3:K+=1
 return F(19*K+1,18),S,K

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];src,aug,cov,census,metric=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [src,aug,cov,census,metric]]==['RC115','RC114','RC112','RC107','RC67']
 assert src['input_sha256'][:2]==hs[1:3] and aug['input_sha256'][1]==hs[2] and cov['input_sha256'][1]==hs[3] and census['input_sha256'][2]==hs[4]
 G=matrix(metric['recentered_nominal_metric_center']);mass=list(map(F,metric['physical_mass']));dg=F(metric['actual_recentered_metric_mass_error_upper']);B=F(11,10);rho=F(252,257)
 assert len(G)==64 and all(mass[j]==2*B/F(2*j+1) for j in range(64)) and pd(G)
 # Exact Legendre derivative-norm controls, supporting the universal energy lemma.
 for j in range(1,25):
  poly=legendre(j);der=[F(k)*poly[k] for k in range(1,len(poly))]
  assert sum((a*b*F(2,i+k+1) for i,a in enumerate(der) for k,b in enumerate(der) if (i+k)%2==0),F(0))==j*(j+1)
 rows=[]
 for idx,r in enumerate(src['parity_rational_Fourier_adjoint_sources']):
  parity=r['parity'];odd=parity=='odd';qr,f=source_moments(r['physical_source_coefficient_intervals'],B,replay)
  qlo,qhi=down(qr,10**20),up(qr,10**20);fl=[down(x,10**40) for x in f];fh=[up(x,10**40) for x in f];fc=[(a+b)/2 for a,b in zip(fl,fh)]
  inds=list(range(1 if odd else 0,64,2));v=[F(0)]*64
  if replay:v=list(map(F,saved['parity_canonical_adjoint_trial_certificates'][idx]['physical_Legendre_trial_coefficients']))
  else:
   with localcontext() as ctx:
    ctx.prec=100
    A=[[D(G[i][j].numerator)/D(G[i][j].denominator) for j in inds] for i in inds];rhs=[D(fc[i].numerator)/D(fc[i].denominator) for i in inds]
    for k in range(32):
     for j in range(k+1,32):
      factor=A[j][k]/A[k][k]
      for l in range(k,32):A[j][l]-=factor*A[k][l]
      rhs[j]-=factor*rhs[k]
    proposal=[D(0)]*32
    for k in range(31,-1,-1):proposal[k]=(rhs[k]-sum((A[k][j]*proposal[j] for j in range(k+1,32)),D(0)))/A[k][k]
    for i,x in zip(inds,proposal):v[i]=F(int((x*10**35).to_integral_value(rounding=ROUND_HALF_EVEN)),10**35)
  assert all(v[j]==0 for j in range(64) if (j-(1 if odd else 0))%2)
  vp=sum((mass[i]*v[i]**2 for i in range(64)),F(0));en=quad(v,G,replay);elo,ehi=en-dg*vp,en+dg*vp;assert elo>0
  pairinglo=sum(((fl[i] if v[i]>=0 else fh[i])*v[i] for i in range(64)),F(0));pairinghi=sum(((fh[i] if v[i]>=0 else fl[i])*v[i] for i in range(64)),F(0));capturedlo=2*pairinglo-ehi;assert capturedlo>0
  physical_captured_lo=F(0);physical_captured_hi=F(0)
  for j in inds:
   low=0 if fl[j]<=0<=fh[j] else min(fl[j]**2,fh[j]**2);high=max(fl[j]**2,fh[j]**2)
   physical_captured_lo+=low/mass[j];physical_captured_hi+=high/mass[j]
  tail_lo=qlo-physical_captured_hi;tail_hi=qhi-physical_captured_lo;assert tail_lo>0
  T=F(r['rational_frequency_half_bandwidth']);da=next(x for x in cov['parity_coverage_certificates'] if x['parity']==parity);d2=F(da['Fourier_restriction_squared_tail_upper']);yn=F(r['auxiliary_vector_physical_norm_squared']);es=F(r['canonical_adjoint_source_error_squared_upper'])
  amb=ambient_dual(T,odd,replay);U=up((root(amb,10**80)+root(d2*yn,10**80)+root(es,10**80))**2,10**12);U=min(U,up(rho*qhi,10**12))
  degree=max(z['native_degree'] for z in r['physical_source_coefficient_intervals']);Cpoly,S,K=polynomial_canonical_factor(degree,B)
  source_norm_lo=max(capturedlo,qlo/Cpoly);distlo=max(F(0),qlo/Cpoly-physical_captured_hi)
  dist_target=max(F(0),sqrt_lower(distlo,10**80)-root(es,10**80))**2
  target_norm_lo=max(F(0),sqrt_lower(source_norm_lo,10**80)-root(es,10**80))**2
  projected_target_hi=(root(physical_captured_hi,10**80)+root(es,10**80))**2
  outside_fraction=max(F(0),1-projected_target_hi/target_norm_lo)
  if odd:assert dist_target>2 and outside_fraction>F(97,100)
  else:assert dist_target==0
  assert U>=source_norm_lo
  ehat=up(U-capturedlo,10**12);etarget=up((root(ehat,10**80)+root(es,10**80))**2,10**12)
  rows.append(dict(parity=parity,global_source_phase=r['physical_source_global_phase'],physical_source_norm_squared_lower=str(qlo),physical_source_norm_squared_upper=str(qhi),physical_Legendre_source_pairing_lower=list(map(str,fl)),physical_Legendre_source_pairing_upper=list(map(str,fh)),physical_Legendre_trial_coefficients=list(map(str,v)),trial_physical_norm_squared=str(vp),trial_actual_canonical_norm_squared_lower=str(down(elo,10**20)),trial_actual_canonical_norm_squared_upper=str(up(ehi,10**20)),canonical_Riesz_source_norm_squared_lower=str(down(source_norm_lo,10**12)),canonical_Riesz_source_norm_squared_upper=str(U),ambient_weighted_dual_norm_squared_upper=str(amb),canonical_trial_error_squared_upper_for_rational_center_source=str(ehat),canonical_trial_error_squared_upper_for_exact_rational_band_adjoint=str(etarget),polynomial_degree=degree,universal_polynomial_canonical_over_physical_squared_factor=str(Cpoly),Fourier_tail_split=str(S),integer_log_weight_upper=K,canonical_distance_squared_to_entire_degree_63_trial_space_lower=str(down(dist_target,10**12)),canonical_exact_adjoint_energy_fraction_outside_degree_63_lower=str(down(outside_fraction,10**12)),canonical_trial_error_has_positive_lower_certified=dist_target>0,physical_source_projection_onto_degree_63_squared_tail_lower=str(down(tail_lo,10**12)),physical_source_projection_onto_degree_63_squared_tail_upper=str(up(tail_hi,10**12)),physical_source_projection_tail_fraction_lower=str(down(tail_lo/qhi,10**12)),source_metric_and_tail_errors_paid=True,trial_selected_numerically_but_acceptance_exact=True,original_Weil_form_on_trial_evaluated=False))
 return dict(milestone='RC116',status='PASS: canonical source trial pair and rigorous physical truncation obstruction; operator actions open',input_sha256=hs,arithmetic='exact physical moments and canonical metric enclosures; numerical trial proposals are not proof decisions',aperture='11/10',trial_dimension=64,actual_canonical_metric_error_upper=str(dg),parity_canonical_adjoint_trial_certificates=rows,canonical_trial_pair_with_error_bounds_certified=True,physical_degree_63_source_truncation_has_positive_error_lower_certified=True,all_639_adjoint_source_coefficients_used=True,odd_canonical_degree_63_trial_space_has_positive_error_lower_certified=True,even_canonical_degree_63_trial_error_lower_certified=False,original_Weil_or_augmented_actions_performed=False,augmented_inverse_responses_computed=False,auxiliary_response_norm_below_one_certified=False,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,new_positive_native_directions_certified=0,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5);a=p.parse_args();saved=json.loads(Path(a.output).read_text()) if a.replay else None;c=run(a.inputs,a.replay,saved)
 if a.replay:assert c==saved
 else:Path(a.output).write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
 print('RC116 PASS: canonical trial/error pair and physical truncation obstruction; original actions open')
