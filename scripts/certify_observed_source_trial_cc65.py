#!/usr/bin/env python3
"""Freeze native observed-source optimizers and certify exact unseen-tail budgets."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,gzip,base64,hashlib
from certify_native_fixed_trials_cc63 import read,OLD,FIRST,SECOND,plus,times,outward,midpoint
from validate_correlated_high_floor_cc59 import inv,mul,KAPPA,add,sc,eye,psd

def square(a):
 l,h=a
 return (F(0) if l<=0<=h else min(l*l,h*h),max(l*l,h*h))

def run(oldp,firstp,secondp,nf24p,cc63p):
 old=read(oldp,OLD);first=read(firstp,FIRST);second=read(secondp,SECOND)
 source={**old['complete_form'],**first['original_full_source'],**second['original_full_source']}
 raw=gzip.decompress(base64.b64decode(Path(nf24p).read_bytes()))
 assert hashlib.sha256(raw).hexdigest()=='4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346'
 fresh=json.loads(raw);assert fresh['aperture']=='53/50' and fresh['projection_degrees']==[117,118]
 source.update(fresh['complete_original_signed_source'])
 assert len(source)==3538
 checks=0
 for r in source.values():
  pole='poles' if 'poles' in r else 'pole'
  assert set(r)=={'arch','prime',pole,'full'}
  for l,h in r.values():assert F(l)<=F(h);checks+=1
  lo,hi=map(F,r['full'])
  assert lo<=sum(F(r[k][1]) for k in ('arch','prime',pole))
  assert hi>=sum(F(r[k][0]) for k in ('arch','prime',pole))
 assert checks==14152
 def q(i,j):return tuple(map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
 def pairing(x,j):
  out=(F(0),F(0))
  for i,v in x.items():out=plus(out,times(q(i,j),v))
  return out
 def energy(x):
  out=(F(0),F(0))
  for i,v in x.items():out=plus(out,times(pairing(x,i),v))
  return out
 original=json.loads(Path(cc63p).read_text());cases=[];den=10**90
 for w in original['fixed_rational_trials']:
  start=0 if w['parity']=='even' else 1
  high=[112+start,114+start];j=118 if start==0 else 117;J=high+[j]
  p={i:F(v)/F(w['coefficient_denominator']) for i,v in zip(w['indices'],w['numerators'])}
  C=[[midpoint(q(a,b)) for b in high] for a in high]
  G=[[midpoint(q(a,b)) for b in high] for a in J]
  r=[midpoint(pairing(p,a)) for a in J]
  V=[[sum(G[k][a]*G[k][b] for k in range(3))-KAPPA*C[a][b] for b in range(2)] for a in range(2)]
  assert V[0][0]>0 and V[0][0]*V[1][1]-V[0][1]**2>0
  z=[[sum(G[k][a]*r[k] for k in range(3))-KAPPA*r[a]] for a in range(2)]
  optimum=mul(inv(V),z)
  Y=[F((v[0]*den).__floor__(),den) for v in optimum]
  shifted=dict(p)
  for a,y in zip(high,Y):shifted[a]-=y
  e0=energy(p);e=energy(shifted)
  assert e[0]>0
  old_known=(F(0),F(0));known=(F(0),F(0))
  residuals={}
  for a in J:
   old_known=plus(old_known,square(pairing(p,a)))
   coordinate=pairing(shifted,a);known=plus(known,square(coordinate));residuals[str(a)]=outward(coordinate,100)
  budget=plus(times(e,KAPPA),times(known,-1))
  old_budget=plus(times(e0,KAPPA),times(old_known,-1))
  improvement=plus(budget,times(old_budget,-1))
  assert budget[0]>0 and improvement[0]>0
  # Exact midpoint objective completion and rounding penalty.
  ym=[v[0] for v in optimum];delta=[[y-v] for y,v in zip(Y,ym)]
  penalty=mul(mul(list(map(list,zip(*delta))),V),delta)[0][0]
  credit=mul(mul(list(map(list,zip(*z))),inv(V)),z)[0][0]
  assert penalty>=0 and credit>penalty and penalty<F(1,10**178)
  mass=sum(v*v for v in shifted.values());assert F(4,5)<mass<F(1001,1000)
  # This pays ONLY arch and retained projection. Other errors stay explicit.
  eta=2*F(53,50)*4*F(106,125)**320/(1-F(106,125))*F(1001,1000)+F(8,10**60)+F(2,10**80)
  from math import isqrt
  root=F(isqrt((budget[0]*den**4).__floor__()),den**2)
  assert root>eta
  approx_budget=(root-eta)**2
  assert approx_budget>F(999,1000)*budget[0]
  projections={str(a):outward(pairing(shifted,a)) for a in range(start,112,2)}
  assert all(F(h)-F(l)<=F(2,10**60) for l,h in projections.values())
  assert all(F(h)-F(l)<=F(2,10**80) for l,h in residuals.values())
  assert all((v*den).denominator==1 for v in shifted.values())
  cases.append(dict(parity=w['parity'],high_indices=high,new_observed_index=j,
   original_CC63_indices=w['indices'],coefficient_denominator=str(den),
   combined_polynomial_numerators=[str((shifted[i]*den).numerator) for i in w['indices']],
   rational_correlation_Y=list(map(str,Y)),midpoint_optimum_Y=list(map(str,ym)),
   finite_objective_rounding_penalty=str(penalty),midpoint_observed_credit=str(credit),
   original_energy=outward(e0),combined_energy=outward(e),physical_mass=str(mass),
   observed_high_coordinate_intervals=residuals,observed_source_square=outward(known),
   previous_unseen_source_square_budget=outward(old_budget),
   unseen_source_square_strict_budget_lower=str(budget[0]),
   strict_budget_improvement_lower=str(improvement[0]),
   budget_improvement_over_original_energy=outward((improvement[0]/e0[1],improvement[1]/e0[0])),
   unseen_source_budget_over_combined_energy=outward((budget[0]/e[1],budget[1]/e[0])),
   retained_source_projection_intervals=projections,
   arch_and_retained_projection_error_upper=str(eta),
   sufficient_reconstructed_unseen_source_square_upper=str(approx_budget),
   complete_unseen_source_square_evaluated=False,whole_seed_high_sign_certified=False))
 # An observed-only positive budget persists across a genuine unseen crossing.
 b=F(1,2);c=F(3);crossings=[]
 for delta in [F(-1,100),F(0),F(1,100)]:
  a=b*b/KAPPA+delta;Q=[[a,F(0),b],[F(0),c,F(0)],[b,F(0),KAPPA]]
  null=[[F(1)],[F(0)],[-b/KAPPA]]
  assert mul(mul(list(map(list,zip(*null))),Q),null)[0][0]==delta
  observed_budget=KAPPA*a;unseen=b*b
  assert observed_budget>0 and observed_budget-unseen==KAPPA*delta
  if delta==0:Qzero=Q;assert mul(Q,null)==[[F(0)]]*3
  crossings.append(dict(full_Schur=str(delta),observed_budget_positive=True,
    exact_unseen_test_margin=str(observed_budget-unseen),actual_null=delta==0))
 assert psd(Qzero);levels=[]
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  Q=add(Qzero,sc(eye(3),mu));assert mul(Q,null)==sc(null,mu)
  assert psd(add(Q,sc(eye(3),-mu)))
  levels.append(dict(genuine_positive_ground_level=str(mu),original_null=False,whole_shift_null=True))
 return dict(milestone='CC65',status='PASS',aperture='53/50',signed_component_checks=checks,
  native_archive_SHA256=[OLD,FIRST,SECOND,hashlib.sha256(raw).hexdigest()],
  observed_optimization_is_not_complete_correlation=True,combined_source_trials=cases,
  partial_observation_crossings=crossings,positive_ground_level_controls=levels,
  abstract_controls_are_not_Weil_countermodels=True,
  whole_aperture_positive=False,all_cap_frame=False,RH=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser()
 for n in ('old','first','second','nf24','cc63','output'):p.add_argument('--'+n,required=True)
 a=p.parse_args();r=run(a.old,a.first,a.second,a.nf24,a.cc63)
 Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print('CC65 original combined trials and strict unseen budgets PASS')
