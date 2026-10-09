#!/usr/bin/env python3
"""Flat interval energy, physical completion, replay and floor controls."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,argparse,hashlib
import certify_dne26_floor_transfer as c
def validate(certpath,replaypath,ep,op):
 a=json.loads(Path(certpath).read_bytes());b=json.loads(Path(replaypath).read_bytes());inputs=[c.read(ep),c.read(op)];sources=[v[0] for v in inputs];checks=0
 assert [v[1] for v in inputs]==c.SHA[:2];checks+=1
 assert a['input_sha256']==b['input_sha256']==c.SHA;checks+=1
 for r,replay,s in zip(a['rows'],b['rows'],sources):
  assert r['parity']==replay['parity']==s['parity'];checks+=1
  assert F(replay['whole_high_physical_gap_strict_lower'])>=F(r['whole_high_physical_gap_strict_lower']);checks+=1
  Q=s['original_selected_native_energy_Gram'];G=s['original_selected_complete_source_Gram'];U=c.coarse(Q,G,F(11,25));sc=([F(10**17),F(10**18),F(10**11)] if r['parity']=='even' else [F(10**15),F(2*10**16),F(10**9)])
  g=F(r['scaled_margin']);scaled=[[tuple(z*sc[i]*sc[j] for z in U[i][j]) for j in range(3)] for i in range(3)]
  for z in product(range(-2,3),repeat=3):
   if not any(z):continue
   lo=sum(min(v*z[i]*z[j] for v in scaled[i][j]) for i in range(3) for j in range(3))
   assert lo>=g*sum(v*v for v in z)>0;checks+=1
  masses=list(map(F,r['high_completed_column_mass_upper']));gap=F(r['whole_high_physical_gap_strict_lower']);k=F(11,25)
  for z in product(range(-1,2),repeat=4):
   norm=sum(abs(z[i])*sc[i]*masses[i] for i in range(3))+abs(z[3]);energy=g*sum(v*v for v in z[:3])+k*z[3]*z[3]
   assert energy>=gap*norm*norm;checks+=1
  assert F(r['old_universal_witness_value_on_same_selected_frame'][1])<0<F(r['new_value_on_same_selected_frame'][0]);checks+=1
 # Same original positive matrix: failure at .207 and passage at .44.
 source_square=F(1,4);assert 1-source_square/F(207,1000)<0<1-source_square/F(11,25);checks+=1
 assert 1-source_square>0;checks+=1
 # Positive/null/negative original Schur crossings; source and native fixed.
 crossings=[]
 for high in [F(1,5),F(1,4),F(1,2)]:
  margin=1-source_square/high;det=high-source_square;assert det==high*margin;checks+=1
  crossings.append(dict(original_high_diagonal=str(high),retained_Schur_eigenvalue=str(margin),actual_null=(margin==0)))
 # Whole-mass shift of the null [[1,1/2],[1/2,1/4]].
 for lam in [F(1,10),F(1),F(2)]:
  v=[F(-1,2),F(1)];Q=[[F(1)+lam,F(1,2)],[F(1,2),F(1,4)+lam]]
  for i in range(2):assert sum(Q[i][j]*v[j] for j in range(2))==lam*v[i];checks+=1
  assert (Q[0][0]-lam)*Q[1][1]-Q[0][1]**2==lam;checks+=1
 return dict(stage='DNE26',status='PASS',independent_rational_checks=checks,
  certificate_sha256=hashlib.sha256(Path(certpath).read_bytes()).hexdigest(),higher_precision_gap_replay_not_weaker=True,
  flat_complete_mixed_energy_tests_passed=True,nonorthogonal_physical_high_completion_tests_passed=True,
  same_positive_original_matrix_old_floor_rejected_new_floor_passed=True,genuine_original_crossings=crossings,
  whole_mass_positive_level_controls_passed=True,controls_are_abstract_not_Weil_countermodels=True,
  complete_source_producers_replayed=False,whole_aperture_positive=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for k in ['certificate','replay','even','odd','output']:p.add_argument(k)
 a=p.parse_args();r=validate(a.certificate,a.replay,a.even,a.odd);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'checks':r['independent_rational_checks'],'status':r['status']}))
