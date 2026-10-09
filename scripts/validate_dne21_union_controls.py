#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,sys
a,b=(json.loads(Path(p).read_text()) for p in sys.argv[1:3]);checks=0
assert a['input_sha256']==b['input_sha256'];checks+=1
for x,y in zip(a['rows'],b['rows']):
 assert x['original_low_lift_pairings']==y['original_low_lift_pairings'];checks+=1
 assert F(y['scaled_positive_margin'])>=F(x['scaled_positive_margin'])>0;checks+=1
 assert F(y['whole_high_physical_gap_strict_lower'])>=F(x['whole_high_physical_gap_strict_lower'])>F(a['common_physical_gap_guard']);checks+=1
 for l,h in zip(x['coarse_three_direction_matrix_intervals'],y['coarse_three_direction_matrix_intervals']):
  for u,v in zip(l,h):
   assert F(u[0])<=F(v[0])<=F(v[1])<=F(u[1]);checks+=1
controls=[];k=F(11,25);r=[F(1,10),F(-1,20),F(1,30)];H=[F(1,10),F(1,20),F(-1,30)]
# Three retained directions: every two-coordinate restriction stays
# positive as the full three-direction matrix crosses a genuine null.
for c in (F(-49,100),F(-1,2),F(-51,100)):
 level=1+2*c
 assert 1-c*c>0 and (level>0)==(c>F(-1,2));checks+=2
 controls.append({'kind':'three_direction_union_crossing','mixed':str(c),'exact_ground_level':str(level),'all_two_coordinate_restrictions_positive':True})
 if level<=0:continue
 g=1-2*abs(c)
 # Nonorthogonal physical retained columns; coordinate norms differ.
 L=[[F(1),F(1,10),F(1,20)],[F(0),F(1,2),F(0)],[F(0),F(0),F(1,3)]]
 masses=[sum(abs(L[j][i]) for j in range(3)) for i in range(3)]
 corrected=[masses[i]+abs(H[i])+abs(r[i])/k for i in range(3)]
 gap=1/(sum(v*v/g for v in corrected)+1/k)
 for values in product((F(-2),F(-1,3),F(0),F(5,4)),repeat=4):
  z=list(values[:3]);f=values[3];rz=sum(r[i]*z[i] for i in range(3));hz=sum(H[i]*z[i] for i in range(3))
  schur=sum(z[i]*z[i] for i in range(3))+2*c*sum(z[i]*z[j] for i in range(3) for j in range(i+1,3))
  original=schur+rz*rz/k+2*f*rz+k*f*f;u=f+rz/k
  mass=sum(sum(L[j][i]*z[i] for i in range(3))**2 for j in range(3))+(hz+f)**2
  assert original==schur+k*u*u;checks+=1
  assert schur>=g*sum(v*v for v in z);checks+=1
  assert original>=gap*mass;checks+=1
 controls.append({'kind':'nonorthogonal_six_union_model_with_full_high_completion','vectors':256,'gap':str(gap)})
# Whole-mass shifts of the PSD three-direction null model: all-ones
# remains an exact physical eigenvector at each positive ground level.
for mu in (F(1,10**40),F(1,100),F(1,20)):
 assert 1+mu+2*F(-1,2)==mu;checks+=1
 assert F(3,2)+mu>mu;checks+=1
 controls.append({'kind':'positive_whole_mass_ground_level','mu':str(mu)})
out={'stage':'DNE21','status':'PASS','exact_rational_assertions':checks,
 'primary_consumer_assertions':a['exact_rational_assertions'],
 'replay_consumer_assertions':b['exact_rational_assertions'],
 'six_direction_joint_union_verified':True,'controls':controls,
 'whole_aperture_positive':False,'RH':False}
Path(sys.argv[3]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('status','exact_rational_assertions')}))
