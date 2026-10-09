#!/usr/bin/env python3
"""Exact retained complement; finite inherited energy is not a high Schur bound."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc92_conditional_physical_restriction as custody

HASH={
 'RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json':'6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00',
 'RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json':'2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42',
 'RPB108_NF33_FIXED_SHARED_REMAINING_LIFT_20261009.json':'89683af32013c4bfc3ed3bd66d90ff889131a4ccdd03dd769523a7dfbbcd9cff',
 'RPB108_NF33_SHARED_REMAINING_FRAME_CERTIFICATE_20261009.json':'1f2887cbdb0c3c237ff279d7715ee4a29ac7cec89d4caecf6c56f7474b1b6d37',
 'RPB108_NF33_SHARED_REMAINING_LIFT_VALIDATION_20261009.json':'e4b687464c42c4d498c78c8b9d640b5b8767cd607cf2de05e1af6d8e86278fdd'}
def load(root,name):
 b=(root/'notes/data'/name).read_bytes();assert hashlib.sha256(b).hexdigest()==HASH[name]
 return json.loads(b)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def run(root,massroot):
 targets=load(root,'RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json')
 response=load(root,'RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json')
 trial=load(root,'RPB108_NF33_FIXED_SHARED_REMAINING_LIFT_20261009.json')
 frame=load(root,'RPB108_NF33_SHARED_REMAINING_FRAME_CERTIFICATE_20261009.json')
 validation=load(root,'RPB108_NF33_SHARED_REMAINING_LIFT_VALIDATION_20261009.json')
 assert validation['status']=='PASS' and validation['frame_certificate_sha256']==HASH['RPB108_NF33_SHARED_REMAINING_FRAME_CERTIFICATE_20261009.json']
 rows=[]
 for idx,parity in enumerate(['even','odd']):
  x=list(map(F,targets['authenticated_compensated_targets'][idx]['retained_coefficients']))
  w=list(map(F,response['parity_certificates'][idx]['exact_rational_retained_response']))
  assert len(x)==len(w)==56 and dot(x,w)==0 and dot(x,x)>0 and dot(w,w)>0
  p,q=max(((i,j) for i in range(56) for j in range(i+1,56)),key=lambda ij:abs(x[ij[0]]*w[ij[1]]-x[ij[1]]*w[ij[0]]))
  det=x[p]*w[q]-x[q]*w[p];assert det!=0
  free=[j for j in range(56) if j not in (p,q)]
  T=[[F(0)]*54 for _ in range(56)]
  for k,j in enumerate(free):
   T[j][k]=F(1);T[p][k]=(-x[j]*w[q]+x[q]*w[j])/det;T[q][k]=(-x[p]*w[j]+x[j]*w[p])/det
  tr=trial['parities'][idx];a=list(map(F,tr['inherited_constraint_coordinates']))
  u=[dot(row,a) for row in T];assert u==list(map(F,tr['fixed_probe_coefficients'][:56]))
  joined=custody.load(massroot,'RPB108_NF35_'+parity.upper()+'_JOINED_WITNESSES_CERTIFICATE_20261009.json')
  assert dot(u,u)==F(joined['inherited_retained_masses'][2])>0
  assert dot(x,u)==dot(w,u)==0
  r=[dot(u,col) for col in zip(*T)];pivot=max(range(54),key=lambda i:abs(r[i]));assert r[pivot]!=0
  keep=[i for i in range(54) if i!=pivot];ratios=[-r[i]/r[pivot] for i in keep]
  for i,z in zip(keep,ratios):
   col=[row[i]+z*row[pivot] for row in T]
   assert dot(x,col)==dot(w,col)==dot(u,col)==0
   assert all(col[free[j]]==int(i==j) for j in keep)
  # The 53 identity rows prove independence; three nonzero orthogonal
  # retained vectors plus these columns span the entire 56-dimensional E.
  cert=frame['parity_certificates'][idx];gap=F(cert['physical_lifted_frame_gap_lower'])
  assert cert['original_lifted_finite_energy_positive'] and gap>0
  assert F(cert['inverse_physical_trace_upper'])*gap==1
  shell=F(cert['selected_shell_physical_operator_norm_upper']);assert shell==11*F(cert['selected_shell_max_entry_upper'])
  rows.append(dict(parity=parity,retained_constraint_pivots=[p,q],T_free_retained_coordinates=free,
   additional_constraint_coordinate_pivot=pivot,remaining_coordinate_indices=keep,
   pivot_row_coefficients=list(map(str,ratios)),exact_retained_complement_dimension=53,
   exact_three_way_orthogonality=True,exact_identity_minor_rank=53,
   retained_full_span_dimension=56,inherited_finite_lifted_physical_gap_lower=str(gap),
   inherited_selected_two_shell_operator_norm_upper=str(shell),
   finite_gap_numerical_display=float(gap),shell_norm_numerical_display=float(shell),
   original_complete_remaining_source_Gram_available=False))
 return dict(milestone='CC94',integration_parent='e9209e00da05f805aec9508b4a201d6c50769738',
  read_only_source='6658ff2837838ab00b9b9c605fdd200d473c3293',authenticated_input_sha256=HASH,
  parity_checks=rows,exact_remaining_retained_dimension=106,
  finite_106_direction_lifted_gap_lower=str(min(F(r['inherited_finite_lifted_physical_gap_lower']) for r in rows)),
  inherited_native_finite_frame_sign=True,new_native_source=False,
  remaining_plus_all_F_positive_certified=False,six_plus_remaining_collective_sign_certified=False,
  background_floor_newly_proved=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('mass_root',type=Path);ap.add_argument('--output',type=Path,required=True)
 a=ap.parse_args();d=run(a.source_root,a.mass_root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC94 PASS: exact 53+53 complement; inherited finite gap',float(F(d['finite_106_direction_lifted_gap_lower'])))
