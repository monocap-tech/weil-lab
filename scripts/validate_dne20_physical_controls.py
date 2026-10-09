#!/usr/bin/env python3
"""Physical mass and all-high completion controls, exact rational arithmetic."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,sys
new,old=(json.loads(Path(p).read_text()) for p in sys.argv[1:3]);checks=0
assert new['high_floor']=='11/25' and old['high_floor']=='207/1000';checks+=1
for a,b in zip(new['rows'],old['rows']):
 assert a['parity']==b['parity'] and a['family']==b['family'];checks+=1
 if b['positive_definite']:
  assert F(a['whole_high_physical_gap_strict_lower'])>F(b['whole_high_physical_gap_strict_lower']);checks+=1
 else:
  assert a['positive_definite'] and b['parity']=='even';checks+=1
assert F(new['common_physical_gap_strict_lower'])>F(4,10**35);checks+=1
assert not new['mixed_six_direction_union_certified'];checks+=1
controls=[];k=F(11,25);m=(F(1),F(1,10**12));r=(F(1,10**18),F(-1,10**24));H=(F(1,10),F(-1,10**7))
for b in (F(99,100),F(1),F(101,100)):
 s=(F(1,10**34),b/F(10**28),F(1,10**22));det=s[0]*s[2]-s[1]**2
 assert (det>0)==(b<1) and (det==0)==(b==1);checks+=2
 controls.append({'kind':'near_critical_matrix_crossing','b':str(b),'determinant':str(det)})
 if b>=1:continue
 mu=det/(s[2]*m[0]+s[0]*m[1])
 eta2=(r[0]**2/m[0]+r[1]**2/m[1])/k**2
 xi2=H[0]**2/m[0]+H[1]**2/m[1]
 factor=1+4*eta2+4*xi2;gap=min(mu/factor,k/2)
 for z0,z1,f in product((F(-2),F(-1,3),F(0),F(5,4)),repeat=3):
  retained=m[0]*z0*z0+m[1]*z1*z1
  rz=r[0]*z0+r[1]*z1;hz=H[0]*z0+H[1]*z1
  u=f+rz/k
  schur=s[0]*z0*z0+2*s[1]*z0*z1+s[2]*z1*z1
  Q00=s[0]+r[0]**2/k;Q01=s[1]+r[0]*r[1]/k;Q11=s[2]+r[1]**2/k
  original=Q00*z0*z0+2*Q01*z0*z1+Q11*z1*z1+2*f*rz+k*f*f
  mass=retained+(hz+f)**2
  assert original==schur+k*u*u;checks+=1
  assert schur>=mu*retained;checks+=1
  assert mass<=factor*retained+2*u*u;checks+=1
  assert original>=gap*mass;checks+=1
 # The inverse response f=-rz/k must be covered too.
 for z0,z1 in product((F(-1),F(0),F(1)),repeat=2):
  rz=r[0]*z0+r[1]*z1;hz=H[0]*z0+H[1]*z1
  mass=m[0]*z0*z0+m[1]*z1*z1+(hz-rz/k)**2
  schur=s[0]*z0*z0+2*s[1]*z0*z1+s[2]*z1*z1
  assert schur>=gap*mass;checks+=1
 controls.append({'kind':'all_high_square_completion_and_physical_gap','tested_vectors':64,'response_minimizers':9,'gap':str(gap)})
# Whole-physical-mass shifts of the rank-one null form have exact ground mu.
c=F(1,3)
for mu in (F(1,10**40),F(1,100),F(1,20)):
 a=c*c+mu;cc=1+mu;v=(F(1),-c)
 assert a*v[0]+c*v[1]==mu*v[0] and c*v[0]+cc*v[1]==mu*v[1];checks+=2
 assert a*cc-c*c>0;checks+=1
 controls.append({'kind':'positive_whole_physical_mass_ground_level','mu':str(mu)})
# Separate positive restrictions cannot certify their union.
assert 1-F(11,10)**2<0;checks+=1
controls.append({'kind':'union_countercontrol','matrix':[['1','11/10'],['11/10','1']],
 'each_coordinate_positive':True,'union_indefinite':True})
out={'stage':'DNE20','status':'PASS','exact_rational_assertions':checks,'controls':controls,
 'both_lift_families_same_retained_plane':True,'new_floor_repairs_NF29_even':True,
 'common_gap_guard':'4/'+str(10**35),'mixed_six_direction_union_certified':False,
 'whole_aperture_positive':False,'RH':False}
Path(sys.argv[3]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('status','exact_rational_assertions','common_gap_guard')}))
