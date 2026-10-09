#!/usr/bin/env python3
"""NF24 read-only replay, CC63 native projections, and nonzero measured-source response controls."""
import argparse,base64,gzip,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from certify_native_fixed_trials_cc63 import plus,times,outward
from validate_correlated_high_floor_cc59 import mul,tr,inv,add,sc,eye,psd,KAPPA

def squared(a):
 l,h=a
 return (F(0) if l<=0<=h else min(l*l,h*h),max(l*l,h*h))

def native(replay_dir,cc63):
 d=Path(replay_dir)
 targets=json.loads((d/'RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json').read_text())
 replay=json.loads((d/'target_replay.json').read_text())
 assert replay==targets
 upstream=json.loads((d/'RPB108_NF24_COMPENSATED_SOURCE_CERTIFICATE_20261009.json').read_text())
 proj=json.loads((d/'projection_replay.json').read_text())
 for k,v in proj.items():assert upstream[k]==v
 raw=gzip.decompress(base64.b64decode((d/'RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64').read_bytes()))
 assert hashlib.sha256(raw).hexdigest()==upstream['native_projection_source_sha256']
 source=json.loads(raw);records=source['complete_original_signed_source']
 assert source['aperture']=='53/50' and len(records)==116
 checks=0
 for r in records.values():
  assert set(r)=={'arch','prime','pole','full'}
  for lo,hi in r.values():assert F(lo)<=F(hi);checks+=1
  l,h=map(F,r['full'])
  assert l<=sum(F(r[k][1]) for k in ('arch','prime','pole'))
  assert h>=sum(F(r[k][0]) for k in ('arch','prime','pole'))
 assert checks==464
 original=json.loads(Path(cc63).read_text());rows=[]
 eta=F(targets['all_polynomial_arch_operator_error_upper'])
 assert eta==2*F(53,50)*4*F(106,125)**320/(1-F(106,125)) and eta<F(7,10**22)
 for w in original['fixed_rational_trials']:
  even=w['parity']=='even';j=118 if even else 117
  ids=w['indices'];coeff=[F(v)/F(w['coefficient_denominator']) for v in w['numerators']]
  nf=next(v for v in targets['authenticated_compensated_targets'] if v['parity']==w['parity'])
  coeff_nf=list(map(F,nf['retained_coefficients']+nf['exact_rational_high_compensation']))
  assert ids==nf['retained_indices']+nf['high_indices']
  assert coeff[:56]==coeff_nf[:56]
  delta=sum((v-z)**2 for v,z in zip(coeff,coeff_nf))
  assert delta<F(2,10**150)
  q=(F(0),F(0))
  for i,v in zip(ids,coeff):q=plus(q,times(tuple(map(F,records[f'{i},{j}']['full'])),v))
  square=squared(q);energy=tuple(map(F,w['fixed_trial_energy']))
  ratio=(square[0]/energy[1],square[1]/energy[0])
  bounds=(F(284,10000),F(285,10000)) if even else (F(298,10000),F(300,10000))
  assert bounds[0]<ratio[0]<=ratio[1]<bounds[1]<KAPPA
  mass=F(w['physical_mass']);assert mass<F(1001,1000)
  # ||p||<1001/1000; both construction and retained projection errors paid.
  error=eta*F(1001,1000)+F(8,10**60)
  lower=F(w['strict_energy_lower']);target=KAPPA*lower
  # Rational sqrt lower: precision180, no floating arithmetic.
  from math import isqrt
  scale=10**180;root=F(isqrt((target*scale*scale).__floor__()),scale)
  assert root*root<=target and root>error
  budget=(root-error)**2
  assert budget>F(999,1000)*target
  rows.append(dict(parity=w['parity'],new_high_degree=j,original_source_pairing=outward(q,100),
    residual_square_lower=str(square[0]),measured_square_over_Q=outward(ratio,60),
    strict_measured_ratio_bounds=list(map(str,bounds)),residual_nonzero=True,
    CC63_NF24_vector_difference_squared=str(delta),
    arch_and_retained_projection_error_upper=str(error),
    sufficient_reconstructed_residual_square_budget=str(budget),
    budget_fraction_of_coarse_lower_threshold_strict_lower='999/1000',
    complete_residual_square_evaluated=False,coarse_gate_failure_certified=False))
 hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in d.iterdir() if p.is_file() and p.suffix=='.py'}
 return dict(NF24_target_replay_exact=True,NF24_projection_replay_exact=True,
  source_raw_SHA256=hashlib.sha256(raw).hexdigest(),new_signed_component_checks=checks,
  upstream_script_SHA256=hashes,CC63_native_trials=rows)

def correlation(c,k,d,u,v):
 assert c>KAPPA
 s=v-k*u/c
 measured=u*u/c
 credit=(k*s)**2/(c*(c-KAPPA)+k*k)
 upper=measured+(s*s-credit)/KAPPA
 V=c*(c-KAPPA)+k*k
 zbar=(c-KAPPA)*u+k*v
 assert upper==(u*u+v*v-zbar*zbar/V)/KAPPA
 y=zbar/V
 assert upper==((u-c*y)**2+(v-k*y)**2)/KAPPA+2*u*y-c*y*y
 high=[[c,k],[k,d]]
 assert psd(add(high,sc(eye(2),-KAPPA)))
 exact=mul(mul([[u,v]],inv(high)),[[u],[v]])[0][0]
 assert exact<=upper
 return exact,upper,s,credit

def controls():
 c=F(3);k=F(3);d=KAPPA+k*k/(c-KAPPA)
 lam=F(1,7);u=F(1,1000);v=F(1)
 b=u-c*lam;t=v-k*lam
 exact,upper,s,credit=correlation(c,k,d,u,v);assert exact==upper
 crossings=[];Qzero=None
 for delta in [F(-1,100),F(0),F(1,100)]:
  qp=exact+delta;a=qp-2*lam*b-lam*lam*c
  Q=[[a,b,t],[b,c,k],[t,k,d]]
  response=mul(mul([[b,t]],inv([[c,k],[k,d]])),[[b],[t]])[0][0]
  assert a-response==delta
  z=mul(inv([[c,k],[k,d]]),[[b],[t]])
  h=[[F(1)],[-z[0][0]],[-z[1][0]]]
  assert mul(mul(tr(h),Q),h)[0][0]==delta
  if delta==0:assert mul(Q,h)==[[F(0)]]*3;Qzero=Q;null=h
  assert qp-upper==delta
  assert qp-(u*u+v*v)/KAPPA<0
  crossings.append(dict(full_Schur=str(delta),corrected_gate_margin=str(delta),
    measured_source_nonzero=True,coarse_gate_fails=True,actual_null=delta==0))
 assert psd(Qzero)
 levels=[]
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  Q=add(Qzero,sc(eye(3),mu))
  assert mul(Q,null)==sc(null,mu) and psd(add(Q,sc(eye(3),-mu)))
  # An original positive ground level becomes a null only after WHOLE mass shift.
  retained_shift=[r[:] for r in Q];retained_shift[0][0]-=mu
  assert mul(retained_shift,null)!=[[F(0)]]*3
  levels.append(dict(original_ground_level=str(mu),whole_shift_has_null=True,
    retained_only_shift_has_no_this_null=True,positive_level_is_original_null=False))
 # Sharp majorant is attained with nonzero measured coordinate, remains
 # valid after unknown high increments. Same norm without alignment gains nothing.
 increments=[]
 for tau in [F(0),F(1,100),F(1),F(100)]:
  ex,up,_,_=correlation(c,k,d+tau,u,v)
  increments.append(dict(high_increment=str(tau),actual_response=str(ex),upper=str(up),attained=ex==up))
 orth_high=[[c,k,F(0)],[k,d,F(0)],[F(0),F(0),KAPPA]]
 orth_response=mul(mul([[F(0),F(0),F(1)]],inv(orth_high)),[[F(0)],[F(0)],[F(1)]])[0][0]
 assert orth_response==1/KAPPA
 return dict(nonzero_measured_residual=str(u),exact_shifted_source=str(s),
  sharp_upper=str(upper),correlation_credit=str(credit),crossings=crossings,
  genuine_positive_ground_levels=levels,unknown_high_increments=increments,
  orthogonal_unit_source_has_zero_credit=True,orthogonal_response=str(orth_response),
  original_Weil_countermodel=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay-dir',required=True);p.add_argument('--cc63',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 result=dict(milestone='CC64',status='PASS',native=native(a.replay_dir,a.cc63),controls=controls(),
  full_native_correlation_evaluated=False,whole_aperture_positive=False,all_cap_frame=False,RH=False,Lean=False)
 Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print('CC64 native transfer and nonzero-residual correlation controls PASS')
