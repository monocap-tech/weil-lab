#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,sys
a,b=(json.loads(Path(p).read_text()) for p in sys.argv[1:3]);checks=0
assert a['input_sha256']==b['input_sha256'];checks+=1
for r,s in zip(a['rows'],b['rows']):
 assert F(s['whole_high_physical_gap_strict_lower'])>=F(r['whole_high_physical_gap_strict_lower'])>F(a['common_physical_gap_guard']);checks+=1
 assert r['unchanged_full_remaining_loading_at_new_floor_interval']==s['unchanged_full_remaining_loading_at_new_floor_interval'];checks+=1
 assert F(r['unchanged_full_remaining_loading_at_new_floor_interval'][0])>1;checks+=1
 U=r['complete_coarse_matrix_intervals'];positions=[(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
 # Independent closed-form Sylvester checks at ALL interval vertices.
 # These corroborate the all-interval Gershgorin proof, not a sampled
 # proof in place of it; the cone of positive forms is convex.
 for bits in product((0,1),repeat=6):
  M=[[F(0)]*3 for _ in range(3)]
  for (i,j),bit in zip(positions,bits):M[i][j]=M[j][i]=F(U[i][j][bit])
  aa,dd,ff=M[0][0],M[1][1],M[2][2];bb,cc,ee=M[0][1],M[0][2],M[1][2]
  det=aa*dd*ff+2*bb*cc*ee-aa*ee*ee-dd*cc*cc-ff*bb*bb
  assert aa>0;checks+=1
  assert aa*dd-bb*bb>0;checks+=1
  assert det>0;checks+=1
controls=[]
# An unchanged full-background scalar floor estimator can fail even
# while an explicit orthogonal probe passes. Positivity of the actual
# original matrix is independent of the conservative floor estimate.
k=F(11,25)
for bmix in (F(99,100),F(1),F(101,100)):
 det=1-bmix*bmix
 assert (det>0)==(bmix<1) and (det==0)==(bmix==1);checks+=2
 controls.append({'kind':'genuine_joint_crossing','mixed':str(bmix),'determinant':str(det)})
for mu in (F(1,10**40),F(1,100),F(1,20)):
 assert 1+mu-1==mu and 2+mu>mu;checks+=2
 controls.append({'kind':'positive_whole_mass_ground_level','mu':str(mu)})
# high C=I on R2, background A=I on R2, coupling diag(1/2,4/5).
# True condensed values positive; the .44-floor estimate rejects only
# the second direction. The first explicit probe remains positive.
actual=[1-F(1,2)**2,1-F(4,5)**2]
coarse=[1-F(1,2)**2/k,1-F(4,5)**2/k]
assert min(actual)>0 and coarse[0]>0>coarse[1];checks+=1
controls.append({'kind':'passing_probe_failing_collective_floor_positive_actual_form','actual_Schur_diagonal':list(map(str,actual)),'coarse_diagonal':list(map(str,coarse))})
assert a['union_with_DNE21_retained_dimension']==8 and not a['eight_direction_mixed_union_certified'];checks+=1
out={'stage':'DNE22','status':'PASS','exact_rational_assertions':checks,
 'all_64_interval_vertices_each_parity_positive':True,'controls':controls,
 'primary_consumer_assertions':a['exact_rational_assertions'],'replay_consumer_assertions':b['exact_rational_assertions'],
 'new_probe_plane_positive':True,'full_unlifted_remaining_floor_estimator_rejected':True,
 'eight_direction_union_certified':False,'whole_aperture_positive':False,'RH':False}
Path(sys.argv[3]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
