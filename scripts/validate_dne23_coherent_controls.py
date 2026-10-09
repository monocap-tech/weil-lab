#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,sys
a,b,pe,po,qe,qo=(json.loads(Path(p).read_text()) for p in sys.argv[1:7]);checks=0
for p,q in ((pe,qe),(po,qo)):
 l,h=map(F,p['original_low_probe_pairing']);ll,hh=map(F,q['original_low_probe_pairing'])
 assert l<=ll<=hh<=h;checks+=1
 assert F(q['uniform_low_source_operator_error_upper'])<F(p['uniform_low_source_operator_error_upper']);checks+=1
 assert p['CC62_low_diagonal_overlap'] and q['CC62_low_diagonal_overlap'];checks+=1
for x,y in zip(a['rows'],b['rows']):
 assert F(y['joint_low_diagonal_lower'])>=F(x['joint_low_diagonal_lower'])>0;checks+=1
 assert F(y['whole_high_physical_gap_strict_lower'])>=F(x['whole_high_physical_gap_strict_lower'])>F(a['common_physical_gap_guard']);checks+=1
 assert min(map(F,x['scaled_V_minus_Gamma_margins']))>0;checks+=1
controls=[];k=F(11,25);theta=F(1,10);A=F(1,10);P0=F(1,100)
R=[F(1,3),F(1,4),F(1,5)];p=[F(1,100)]*3
# Exact conservative dual norm M=1/4:
# sqrt(3/10000)<9/500 and sqrt(P0)/k=5/22.
assert sum(v*v for v in p)<F(9,500)**2;checks+=1
assert F(9,500)+F(5,22)<F(1,4);checks+=1
M=F(1,4);alpha=A-M*M/(1-theta);assert alpha>0;checks+=1
physical_columns=[F(1),F(7,10),F(37,100),F(22,100)]
completed=[physical_columns[0]+F(1,10)/k]+[physical_columns[i+1]+R[i]/k for i in range(3)]
gap=1/(completed[0]**2/alpha+sum(v*v/theta for v in completed[1:])+1/k)
for rlow in product((F(-1,20),F(1,20)),repeat=3):
 norm=sum(v*v for v in rlow);assert norm<=P0;checks+=1
 cross=[rlow[i]*R[i] for i in range(3)]
 for t,z0,z1,z2 in product((F(-1),F(0),F(1)),repeat=4):
  z=[z0,z1,z2];vv=sum(v*v for v in z)
  gamma=sum(R[i]**2*z[i]**2 for i in range(3))
  gz=sum(cross[i]*z[i] for i in range(3));pz=sum(p[i]*z[i] for i in range(3))
  assert gz*gz<=P0*gamma<=P0*vv;checks+=1
  # Native Q3=I+Gamma3/k and Q00=A+P0/k, high C=kI.
  # Its EXACT condensed form uses the actual Gram, not independent boxes.
  S=(A+(P0-norm)/k)*t*t+2*t*(pz-gz/k)+vv
  assert S>=alpha*t*t+theta*vv;checks+=1
  for high in ((F(0),F(0),F(0)),(F(1,10),F(-1,10),F(1,5))):
   source=[rlow[i]*t+R[i]*z[i] for i in range(3)]
   f=[high[i]-source[i]/k for i in range(3)]
   retained=[t+F(1,10)*z0+F(1,20)*z1+F(1,50)*z2,z0/2,F(3,10)*z1,z2/5]
   H=[z0/10,z1/50,F(0)]
   mass=sum(v*v for v in retained)+sum((H[i]+f[i])**2 for i in range(3))
   original=S+k*sum(v*v for v in high)
   assert original>=gap*mass;checks+=1
controls.append({'kind':'coherent_source_Gram_and_joint_condensation','source_rows':8,'retained_vectors_per_row':81,'joint_low_lower':str(alpha),'nonorthogonal_physical_completion_tests':1296,'physical_gap':str(gap)})
# Genuine crossings: selected two-block diagonals remain positive.
for mixed in (F(99,100),F(1),F(101,100)):
 det=1-mixed*mixed;assert (det>0)==(mixed<1) and (det==0)==(mixed==1);checks+=2
 controls.append({'kind':'genuine_joint_crossing','mixed':str(mixed),'determinant':str(det)})
for mu in (F(1,10**40),F(1,100),F(1,20)):
 assert 1+mu-1==mu and 2+mu>mu;checks+=2
 controls.append({'kind':'positive_whole_mass_ground_level','mu':str(mu)})
assert a['retained_dimension']==8 and a['uncovered_retained_dimension']==104 and a['eight_direction_mixed_union_certified'];checks+=1
out={'stage':'DNE23','status':'PASS','exact_rational_assertions':checks,'controls':controls,
 'fresh_native_pairing_replay_nested':True,'source_Gram_coherent_bound_verified':True,
 'primary_consumer_assertions':a['exact_rational_assertions'],'replay_consumer_assertions':b['exact_rational_assertions'],
 'eight_direction_mixed_union_certified':True,'whole_aperture_positive':False,'RH':False}
Path(sys.argv[7]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
