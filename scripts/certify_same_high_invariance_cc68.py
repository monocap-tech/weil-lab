#!/usr/bin/env python3
"""Transport certified NF25 Gram to CC63/65 and certify all-H2 estimator rejection."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,hashlib
from validate_correlated_high_floor_cc59 import tr,mul,inv,add,sc,eye,block,psd,KAPPA

def controls():
 C2=[[F(3),F(0)],[F(0),F(4)]];K=[[F(3),F(1,2)]]
 D=add([[KAPPA]],mul(mul(K,inv(add(C2,sc(eye(2),-KAPPA)))),tr(K)))
 C=block(C2,tr(K),K,D);r=[[F(1,1000)],[F(-1,500)],[F(1)]]
 T=mul(mul(tr(r),inv(C)),r)[0][0]
 shifts=[[[F(0)],[F(0)]],[[F(1,7)],[F(-2,9)]],[[F(10**10)],[F(-10**10)]],[[F(1,10**90)],[F(-1,10**90)]]]
 tests=[]
 for delta in [F(-1,100),F(0),F(1,100)]:
  q=T+delta;u=r[:2];G=[row[:2] for row in C]
  V=add(mul(tr(G),G),sc(C2,-KAPPA));z=add(mul(tr(G),r),sc(u,-KAPPA))
  P=mul(tr(r),r)[0][0];credit=mul(mul(tr(z),inv(V)),z)[0][0]
  assert (P-credit)/KAPPA==T
  for beta in shifts:
   qb=q+2*mul(tr(u),beta)[0][0]+mul(mul(tr(beta),C2),beta)[0][0]
   rb=add(r,mul(G,beta));ub=add(u,mul(C2,beta))
   zb=add(mul(tr(G),rb),sc(ub,-KAPPA));Pb=mul(tr(rb),rb)[0][0]
   assert zb==add(z,mul(V,beta))
   Ub=(Pb-mul(mul(tr(zb),inv(V)),zb)[0][0])/KAPPA
   assert qb-Ub==delta
   assert qb-Pb/KAPPA<=delta
  Q=block([[q]],tr(r),r,C);h=[[F(1)]]+sc(mul(inv(C),r),-1)
  assert mul(mul(tr(h),Q),h)[0][0]==delta
  if delta==0:assert mul(Q,h)==[[F(0)]]*4;Qzero=Q;null=h
  tests.append(dict(full_Schur=str(delta),all_four_corrections_preserve_margin=True,genuine_null=delta==0))
 assert psd(Qzero);levels=[]
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  Q=add(Qzero,sc(eye(4),mu));assert mul(Q,null)==sc(null,mu)
  assert psd(add(Q,sc(eye(4),-mu)))
  levels.append(dict(original_ground_level=str(mu),original_null=False,whole_shift_null=True))
 return dict(crossings=tests,positive_ground_levels=levels,actual_Weil_countermodel=False)

def run(root,replay):
 root=Path(root);replay=Path(replay);sys.path.insert(0,str(replay.resolve()))
 import certify_native_correlated_sources_nf25_106 as n
 def iv(pair):return n.I(*map(F,pair))
 def lo(v):return F(v.l,n.SCALE)
 def hi(v):return F(v.h,n.SCALE)
 original=json.loads((replay/'RPB108_NF25_DIRECTIONAL_SOURCE_CORRELATION_CERTIFICATE_20261009.json').read_text())
 reproduced=json.loads((replay/'certificate_replay.json').read_text())
 for k,v in reproduced.items():
  if k=='parity_certificates':
   for a,b in zip(original[k],v):
    for field,value in b.items():assert a[field]==value
    for field,(l,h) in a['strict_outward_decimal_display_brackets'].items():
     assert F(l)<F(a[field][0])<=F(a[field][1])<F(h)
  else:assert original[k]==v
 assert original['independent_native_pairings_checked']==12
 assert original['producer_sha256']==hashlib.sha256((replay/'certify_native_correlated_sources_nf25_106.py').read_bytes()).hexdigest()
 assert original['validator_sha256']==hashlib.sha256((replay/'validate_native_correlated_response_nf25_106.py').read_bytes()).hexdigest()
 targets=json.loads((replay/'RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json').read_text())
 cc63=json.loads((root/'notes/data/RPB108_FIXED_TRIALS_CC63_CERTIFICATE_20261009.json').read_text())
 cc65=json.loads((root/'notes/data/RPB108_OBSERVED_SOURCE_TRIAL_CC65_CERTIFICATE_20261009.json').read_text())
 rows=[]
 for cert,w in zip(original['parity_certificates'],targets['authenticated_compensated_targets']):
  assert cert['parity']==w['parity'];parity=w['parity']
  gram=[[iv(v) for v in row] for row in cert['original_complete_three_source_Gram']]
  C=[[iv(v) for v in row] for row in cert['original_C2']]
  u=list(map(iv,cert['original_measured_residual_u']));q=iv(w['compensated_energy'])
  V=[[iv(v) for v in row] for row in cert['positive_correlation_matrix_V']]
  det=V[0][0]*V[1][1]-n.sq(V[0][1]);assert det.l>0
  z=list(map(iv,cert['shifted_source_correlation_zbar']))
  credit=iv(cert['correlation_credit']);U=(gram[0][0]-credit)/KAPPA
  margin=q-U
  factor=F(68,100) if parity=='even' else F(35,100)
  assert hi(margin)<-factor*lo(q)
  cases=[]
  for label,collection in [('CC63',cc63['fixed_rational_trials']),('CC65',cc65['combined_source_trials'])]:
   v=next(x for x in collection if x['parity']==parity)
   ns=v['numerators'] if label=='CC63' else v['combined_polynomial_numerators']
   coeff=[F(x)/F(v['coefficient_denominator']) for x in ns]
   assert coeff[:56]==list(map(F,w['retained_coefficients']))
   beta=[coeff[56+i]-F(w['exact_rational_high_compensation'][i]) for i in range(2)]
   qnew=q+2*sum((u[i]*beta[i] for i in range(2)),n.I(0))+sum((beta[i]*beta[j]*C[i][j] for i in range(2) for j in range(2)),n.I(0))
   P=gram[0][0]+2*sum((beta[i]*gram[0][i+1] for i in range(2)),n.I(0))+sum((beta[i]*beta[j]*gram[i+1][j+1] for i in range(2) for j in range(2)),n.I(0))
   zn=[z[i]+sum((V[i][j]*beta[j] for j in range(2)),n.I(0)) for i in range(2)]
   cn=(V[1][1]*n.sq(zn[0])-2*V[0][1]*zn[0]*zn[1]+V[0][0]*n.sq(zn[1]))/det
   Un=(P-cn)/KAPPA
   own=iv(v['fixed_trial_energy'] if label=='CC63' else v['combined_energy'])
   assert lo(qnew)<=hi(own) and hi(qnew)>=lo(own)
   assert lo(P)>KAPPA*hi(own) and lo(Un)>hi(own)
   source_ratio=P/own;response_ratio=Un/own
   data=dict(trial=label,beta_from_NF24=list(map(str,beta)),complete_high_source_square=P.ends(),
    complete_high_source_square_over_own_energy=source_ratio.ends(),
    transported_correlated_response_majorant_over_own_energy=response_ratio.ends(),
    native_coarse_gate_rejected=True,native_correlated_gate_rejected=True)
   if label=='CC65':
    known=iv(v['observed_source_square']);omitted=P-known;budget=KAPPA*own-known
    assert lo(budget)>0 and lo(omitted)>hi(budget)
    ratio=omitted/budget
    assert lo(ratio)>(F(179,100) if parity=='even' else F(141,100))
    data.update(complete_omitted_source_square=omitted.ends(),native_omitted_source_over_budget=ratio.ends(),CC65_tail_gate_rejected=True)
   cases.append(data)
  rows.append(dict(parity=parity,original_NF24_gap_Q_minus_majorant=margin.ends(),
   invariant_gap_strict_upper=str(-factor*lo(q)),all_H2_corrections_fail_coarse_and_correlated_gates=True,
   transported_trials=cases,actual_inverse_response_evaluated=False,actual_negative_vector=False))
 return dict(milestone='CC68',status='PASS',NF25_all_response_replay_fields_exact=True,NF25_added_display_brackets_checked=True,
  native_parities=rows,exact_invariance_controls=controls(),
  complete_Weil_nonimplication_claimed=False,whole_aperture_positive=False,all_cap_frame=False,RH=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--replay',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 Path(a.output).write_text(json.dumps(run(a.root,a.replay),indent=2)+'\n');print('CC68 native Gram transport and all-H2 estimator rejection PASS')
