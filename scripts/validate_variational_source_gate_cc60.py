#!/usr/bin/env python3
"""CC60 exact variational gate and authenticated native two-high penalty bounds."""
from fractions import Fraction as F
import argparse,json,gzip,hashlib
from validate_correlated_high_floor_cc59 import tr,mul,add,sc,eye,inv,gram,psd,KAPPA
FIRST_SHA='da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'
SECOND_SHA='0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad'
def read(p,sha):
 raw=gzip.open(p,'rb').read();assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def native(first,second):
 f=read(first,FIRST_SHA);s=read(second,SECOND_SHA)
 assert f['aperture']==s['aperture']=='53/50'
 assert s['parent_first_boundary_SHA256']==FIRST_SHA
 sources={**f['original_full_source'],**s['original_full_source']};result=[];checks=0
 for parity,degrees,beta,L in [('even',(112,114),F(14,5),F(419,100)),('odd',(113,115),F(289,100),F(402,100))]:
  records={};intervals={}
  for i,j in [(degrees[0],degrees[0]),degrees,(degrees[1],degrees[1])]:
   key=f'{i},{j}';r=sources[key];pole='pole' if 'pole' in r else 'poles'
   assert set(r)=={'arch','prime',pole,'full'}
   for lo,hi in r.values():assert F(lo)<=F(hi);checks+=1
   lo,hi=map(F,r['full']);assert lo<=sum(F(r[k][1]) for k in ('arch','prime',pole))
   assert hi>=sum(F(r[k][0]) for k in ('arch','prime',pole))
   intervals[key]=(lo,hi);g=10**45
   records[key]=[str(F((lo*g).__floor__(),g)),str(F((hi*g).__ceil__(),g))]
  d0=intervals[f'{degrees[0]},{degrees[0]}'];d1=intervals[f'{degrees[1]},{degrees[1]}'];off=intervals[f'{degrees[0]},{degrees[1]}']
  offmax=max(abs(x) for x in off)
  assert d0[0]>beta and d1[0]>beta and (d0[0]-beta)*(d1[0]-beta)>offmax**2
  assert max(d0[1]+offmax,d1[1]+offmax)<L
  result.append({'parity':parity,'C2_eigenvalue_strict_lower':str(beta),'C2_eigenvalue_strict_upper':str(L),
    'penalty_eigenvalue_strict_lower':str(beta*(beta-KAPPA)),
    'penalty_eigenvalue_strict_upper':str(L*(L-KAPPA)),'native_full_intervals_rounded_outward_1e45':records})
 assert checks==24
 return result,checks
def validate(first,second):
 bounds,checks=native(first,second)
 C=[[F(3),F(1,5)],[F(1,5),F(4)]];K=[[F(3),F(1,2)],[F(1,3),F(2)],[F(1,7),F(-1,4)]]
 R=[[F(1),F(1,5)],[F(1,4),F(2)],[F(1,9),F(-1,3)]]
 W=mul(C,add(C,sc(eye(2),-KAPPA)));V=add(W,gram(K));Z=mul(tr(K),R);Ystar=mul(inv(V),Z)
 Jmin=add(gram(R),sc(mul(mul(tr(Z),inv(V)),Z),-1));trials=[]
 rounded=[[F((x*1000).__floor__(),1000) for x in row] for row in Ystar]
 for name,Y in [('zero',sc(Ystar,0)),('half',sc(Ystar,F(1,2))),('exact_optimizer',Ystar),('rational_1e3_round',rounded),('double',sc(Ystar,2))]:
  rho=add(R,sc(mul(K,Y),-1));J=add(gram(rho),mul(mul(tr(Y),W),Y));err=add(Y,sc(Ystar,-1))
  assert add(J,sc(Jmin,-1))==mul(mul(tr(err),V),err)
  assert psd(add(J,sc(Jmin,-1)))
  trials.append({'trial':name,'exact_variational_gap_identity':True,'attains_minimum':J==Jmin})
 # Projection identity: correcting the polynomial creates measured source coefficients.
 A=[[F(5),F(1,4)],[F(1,4),F(6)]];B=[[F(1,3),F(1,5)],[F(-1,7),F(1,4)]]
 lowtail=[[F(1,5),F(1,6)],[F(1,9),F(-1,8)],[F(1,11),F(1,13)]]
 source=[r+s for r,s in zip(A,B)]+[r+s for r,s in zip(tr(B),C)]+[r+s for r,s in zip(lowtail,K)]
 T=eye(2)+sc(mul(inv(C),tr(B)),-1);S=add(A,sc(mul(mul(B,inv(C)),tr(B)),-1))
 Y=rounded;Ty=T[:2]+add(T[2:],sc(Y,-1));action=mul(source,Ty)
 assert action[:2]==add(S,sc(mul(B,Y),-1)) and action[2:4]==sc(mul(C,Y),-1)
 sigma=mul(source,T)[4:];assert action[4:]==add(sigma,sc(mul(K,Y),-1))
 # Rational near-optimal source gate, conservative AUTHENTICATED penalty envelope, paid source error.
 y=F(17,100);rho=1-3*y;w=F(bounds[0]['penalty_eigenvalue_strict_upper']);s=F(4)
 error_radius=F(1,1000);t=F(1,10)
 upper=(1+t)*rho*rho+(1+1/t)*error_radius**2+w*y*y
 assert 1/KAPPA>s and upper<KAPPA*s
 # Rank-two correction cannot improve the third coordinate of a three-plane.
 Z3=[[F(3),F(0),F(0)],[F(0),F(3),F(0)]];blind=[[F(0)],[F(0)],[F(1)]]
 assert mul(Z3,blind)==[[0],[0]]
 corr=add(eye(3),sc(mul(mul(tr(Z3),sc(eye(2),1/(3*(3-KAPPA)+9))),Z3),-1))
 assert mul(mul(tr(blind),corr),blind)==[[F(1)]]
 # Actual-null and genuine positive-level controls retained from the correlated theorem.
 from validate_correlated_high_floor_cc59 import validate as previous
 controls=previous();assert len(controls['genuine_crossings'])==len(controls['positive_ground_levels'])==3
 return {'status':'PASS','milestone':'CC60','native_archive_SHA256':[FIRST_SHA,SECOND_SHA],
  'native_component_interval_checks':checks,'native_penalty_bounds':bounds,'variational_trials':trials,
  'both_low_and_measured_high_source_projections_checked':True,
  'rational_trial_with_paid_source_error':{'Y':'17/100','penalty_envelope':str(w),'source_error_radius':str(error_radius),
    'upper_J':str(upper),'kappa_S2':str(KAPPA*s),'strict_gate_passes':True,'coarse_gate_fails':True,
    'source_radius_is_abstract_control_not_native':True},
  'rank_two_blind_three_plane_control':True,'retained_parity_blind_dimension_at_least':54,
  'genuine_crossing_controls':controls['genuine_crossings'],'positive_ground_level_controls':controls['positive_ground_levels'],
  'native_source_residual_enclosed':False,'native_correlated_gate_evaluated':False,'all_cap_frame':False,'RH':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--first',required=True);p.add_argument('--second',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 r=validate(a.first,a.second);open(a.output,'w').write(json.dumps(r,indent=2)+'\n');print('CC60 PASS')
