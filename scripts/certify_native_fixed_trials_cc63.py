#!/usr/bin/env python3
"""Original rational near-critical trials with paid measured residuals, not exact Galerkin annihilation."""
import argparse,gzip,json,hashlib
from fractions import Fraction as F
OLD='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
FIRST='da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'
SECOND='0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad'
def read(p,sha):
 raw=gzip.open(p,'rb').read();assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,t):return (min(t*a[0],t*a[1]),max(t*a[0],t*a[1]))
def outward(a,digits=60):
 g=10**digits
 return [str(F((a[0]*g).__floor__(),g)),str(F((a[1]*g).__ceil__(),g))]
def midpoint(a):return sum(a)/2
def certify(oldp,firstp,secondp,seedp):
 old=read(oldp,OLD);first=read(firstp,FIRST);second=read(secondp,SECOND)
 assert old['aperture']==first['aperture']==second['aperture']=='53/50'
 assert first['parent_sha256']==OLD and second['parent_E112_SHA256']==OLD and second['parent_first_boundary_SHA256']==FIRST
 source={**old['complete_form'],**first['original_full_source'],**second['original_full_source']}
 assert len(source)==3422;checks=0
 for r in source.values():
  pole='poles' if 'poles' in r else 'pole';assert set(r)=={'arch','prime',pole,'full'}
  for lo,hi in r.values():assert F(lo)<=F(hi);checks+=1
  lo,hi=map(F,r['full']);assert lo<=sum(F(r[k][1]) for k in ('arch','prime',pole))
  assert hi>=sum(F(r[k][0]) for k in ('arch','prime',pole))
 assert checks==13688
 seedraw=open(seedp,'rb').read();seeds=json.loads(seedraw)
 assert seeds['aperture']=='53/50' and seeds['parent_source']==OLD
 def q(i,j):return tuple(map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
 def pairing(x,i):
  ans=(F(0),F(0))
  for j,v in x.items():ans=plus(ans,times(q(i,j),v))
  return ans
 def energy(x):
  ans=(F(0),F(0))
  for i,v in x.items():ans=plus(ans,times(pairing(x,i),v))
  return ans
 cases=[];den=10**75
 for parity,high,lower,upper in [('even',[112,114],F(8,10**35),F(1,10**34)),('odd',[113,115],F(3,10**31),F(4,10**31))]:
  w=seeds['witnesses'][parity];x={int(i):F(n)/F(seeds['coefficient_denominator']) for i,n in zip(w['indices'],w['numerators'])}
  assert len(x)==56
  b=[pairing(x,j) for j in high];c0=midpoint(q(high[0],high[0]));c1=midpoint(q(high[0],high[1]));c2=midpoint(q(high[1],high[1]));det=c0*c2-c1*c1;assert det>0
  bm=list(map(midpoint,b));ym=[(c2*bm[0]-c1*bm[1])/det,(c0*bm[1]-c1*bm[0])/det]
  y=[F((z*den).__floor__(),den) for z in ym]
  trial=dict(x);trial.update({j:-v for j,v in zip(high,y)})
  oldq=energy(x);newq=energy(trial);mass=sum(v*v for v in trial.values());oldmass=sum(v*v for v in x.values())
  assert lower<newq[0]<=newq[1]<upper and newq[1]<oldq[0]
  assert mass>=oldmass>F(4,5)
  residual=[pairing(trial,j) for j in high]
  assert all(max(abs(z) for z in pair)<F(1,10**60) for pair in residual)
  projections={str(i):outward(pairing(trial,i)) for i in w['indices']}
  assert len(projections)==56
  # Source projection center error <=sqrt(56)*1e-60<8e-60.
  for lo,hi in projections.values():assert F(hi)-F(lo)<=F(2,10**60)
  measured_square=sum(max(abs(l),abs(h))**2 for l,h in residual)
  assert measured_square<F(2,10**120)
  initial_min=sum(F(0) if l<=0<=h else min(l*l,h*h) for l,h in b)
  numerators=[str((trial[i]*den).numerator) for i in sorted(trial)]
  assert all((v*den).denominator==1 for v in trial.values())
  cases.append({'parity':parity,'indices':sorted(trial),'coefficient_denominator':str(den),'numerators':numerators,
    'original_seed_energy':outward(oldq),'fixed_trial_energy':outward(newq),'physical_mass':str(mass),
    'strict_energy_lower':str(lower),'strict_energy_upper':str(upper),
    'fixed_trial_Rayleigh_strict_upper':str(upper/F(4,5)),
    'retained_source_projection_intervals':projections,'retained_projection_center_L2_error_upper':'8/10^60',
    'measured_high_residual_squared_strict_upper':'2/10^120',
    'initial_measured_source_lower_over_kappa_seed_Q':outward((initial_min/(F(207,1000)*oldq[1]),initial_min/(F(207,1000)*oldq[0]))),
    'exact_Galerkin_source_annihilation_claimed':False,'full_high_source_residual_evaluated':False})
 return {'status':'PASS','milestone':'CC63','aperture':'53/50','source_archive_SHA256':[OLD,FIRST,SECOND],
  'original_seed_SHA256':hashlib.sha256(seedraw).hexdigest(),'signed_component_interval_checks':checks,
  'fixed_rational_trials':cases,'near_critical_full_source_gate_evaluated':False,'whole_aperture_positive':False,'all_cap_frame':False,'RH':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for n in ['old','first','second','seeds','output']:p.add_argument('--'+n,required=True)
 a=p.parse_args();r=certify(a.old,a.first,a.second,a.seeds);open(a.output,'w').write(json.dumps(r,indent=2)+'\n');print('CC63 native rational trials PASS')
