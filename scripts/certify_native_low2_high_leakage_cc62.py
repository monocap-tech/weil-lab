#!/usr/bin/env python3
"""Original NF23 source squares minus COMPLETE E112 projections; exact high leakage gate."""
import argparse,gzip,hashlib,json
from fractions import Fraction as F
OLD_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
NF23_SHA='134deb5db09b2bd720284c7f4e2a2fca5918982a307eb67267ecf3586e6810de'
KAPPA=F(207,1000)
def outward(lo,hi,digits=45):
 g=10**digits
 return F((lo*g).__floor__(),g),F((hi*g).__ceil__(),g)
def interval_square(lo,hi):
 return (F(0) if lo<=0<=hi else min(lo*lo,hi*hi)),max(lo*lo,hi*hi)
def certify(old_path,nf23_path):
 raw=gzip.open(old_path,'rb').read();assert hashlib.sha256(raw).hexdigest()==OLD_SHA
 old=json.loads(raw);raw23=open(nf23_path,'rb').read();assert hashlib.sha256(raw23).hexdigest()==NF23_SHA
 new=json.loads(raw23);assert old['aperture']==new['aperture']=='53/50' and old['dim']==112
 assert new['complete_low2_source_square_certified'] is True
 assert new['complete_source_square_gram_offdiagonal']==['0','0']
 source=old['complete_form'];assert len(source)==3192
 cases=[];component_checks=0;records=0
 for parity,j,ratio,margin in [('even',0,F(543,1000),F(457,1000)),('odd',1,F(417,1000),F(583,1000))]:
  lower=upper=F(0)
  for i in range(j,112,2):
   r=source[f'{j},{i}'];assert set(r)=={'arch','prime','poles','full'}
   for lo,hi in r.values():assert F(lo)<=F(hi);component_checks+=1
   lo,hi=map(F,r['full']);assert lo<=sum(F(r[k][1]) for k in ('arch','prime','poles'))
   assert hi>=sum(F(r[k][0]) for k in ('arch','prime','poles'))
   sl,sh=interval_square(lo,hi);lower+=sl;upper+=sh;records+=1
  dl,dh=map(F,new['complete_source_square_gram_diagonal'][j]);assert dl<=dh
  pl,ph=outward(dl-upper,dh-lower);al,ah=outward(*map(F,source[f'{j},{j}']['full']))
  assert pl>0 and al>F(1,25) and ph<ratio*KAPPA*al
  assert 1-ratio==margin
  assert ph<F(9,16)*KAPPA*al and ratio<F(9,16)
  cases.append({'parity':parity,'retained_source_projection_coefficients':56,
   'native_Q_diagonal':[str(al),str(ah)],'full_source_square':list(map(str,outward(dl,dh))),
   'complete_retained_source_square':list(map(str,outward(lower,upper))),
   'full_F112_source_square':[str(pl),str(ph)],
   'P_over_kappa_A_strict_upper':str(ratio),'complete_high_corrected_margin_relative_A':str(margin),
   'coarse_uncompensated_full_high_gate_passes':True})
 assert records==112 and component_checks==448
 # Exact rational Young domination for COMPLEX low/high vectors.
 assert F(543,1000)<F(3,4)**2
 assert (1-F(3,4))*F(1,25)==F(1,100) and KAPPA>F(1,25)
 # Separate controls do NOT satisfy the newly certified native leakage hypothesis.
 crossings=[]
 for eps in [F(1,100),F(0),F(-1,100)]:
  b=F(1,4);a=b*b+eps
  assert a-b*b==eps and b*b>KAPPA*a
  crossings.append({'full_Schur':str(eps),'complete_high_floor_above_kappa':True,'native_leakage_hypothesis_satisfied':False})
 levels=[]
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  c=F(1);b=F(1,4);a=mu+b*b/(c-mu);h=[F(1),-b/(c-mu)]
  assert a*h[0]+b*h[1]==mu*h[0] and b*h[0]+c*h[1]==mu*h[1]
  assert a-mu-b*b/c>0
  assert b*b>KAPPA*a
  levels.append({'positive_ground_level':str(mu),'whole_shift_null':True,'retained_only_shift_misses_null':True,'native_leakage_hypothesis_satisfied':False})
 return {'status':'PASS','milestone':'CC62','original_E112_raw_SHA256':OLD_SHA,'NF23_manifest_SHA256':NF23_SHA,
  'native_component_interval_checks':component_checks,'complete_retained_projection_records':records,
  'native_parity_gates':cases,'restricted_physical_gap':'1/100',
  'certified_original_subspace':'span(e0,e1)+F112 canonical form domain at53/50',
  'excluded_retained_dimension':110,'genuine_crossing_controls':crossings,'positive_level_controls':levels,
  'whole_aperture_positive':False,'compensated_P2_evaluated':False,'all_cap_frame':False,'RH':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--old',required=True);p.add_argument('--nf23',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 r=certify(a.old,a.nf23);open(a.output,'w').write(json.dumps(r,indent=2)+'\n');print('CC62 native low-two/full-high restriction PASS')
