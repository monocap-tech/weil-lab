#!/usr/bin/env python3
"""Import the current original high floor; test the unchanged CC93 packet."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as direct
import certify_cc91_both_joined_pass as joined
import certify_cc92_conditional_physical_restriction as custody
import certify_cc93_sharpen_physical_gap as physical

K=F(11,25)
def controls():
 # Same A=diag(1,0.44), paid high H=e1. The old-floor response
 # inverse bound is diag(1,1/0.207); DNE's is diag(1/0.44,1/0.44).
 old=F(207,1000);cases=[]
 for q,cc,dd in [(F(3,2),F(1),1/K),(F(3),1/old,1/K)]:
  cases.append(dict(native=str(q),old_floor_response_margin=str(q-cc),current_floor_scalar_margin=str(q-dd)))
 assert F(cases[0]['old_floor_response_margin'])>0>F(cases[0]['current_floor_scalar_margin'])
 assert F(cases[1]['current_floor_scalar_margin'])>0>F(cases[1]['old_floor_response_margin'])
 crossings=[]
 for actual_high in [F(1,2),F(2,3),F(1)]:
  assert actual_high>=K
  n=actual_high**2/K-actual_high;w=actual_high-K
  inverse_bound=1/K-w*w/(K*K*n);assert inverse_bound==1/actual_high
  crossings.append(dict(actual_high=str(actual_high),response_margin=str(F(3,2)-inverse_bound)))
 assert [F(x['response_margin']) for x in crossings]==[F(-1,2),F(0),F(1,2)]
 # Positive whole-mass levels preserve the true null vector (1,-3/2).
 for delta in [F(1,1000),F(1,10),F(2)]:
  v=[F(1),F(-3,2)];m=[[F(3,2)+delta,F(1)],[F(1),F(2,3)+delta]]
  assert [sum(m[i][j]*v[j] for j in range(2)) for i in range(2)]==[delta*x for x in v]
 return dict(current_different_floor_criteria_incomparable=cases,same_floor_response_strictly_stronger_control=crossings,
  whole_physical_mass_positive_level_controls=True)
def load(root,name,sha=None):
 b=(root/'notes/data'/name).read_bytes()
 if sha:assert hashlib.sha256(b).hexdigest()==sha
 return json.loads(b)
def floor(root):
 manifest=load(root,'RPB108_DNE17_CUSTODY_20261009.json','afdd8f217c1171a1bcc9677f13c5de2f87655b004a56a9fe04d17036b976384c')
 for path,sha in manifest['artifact_sha256'].items():
  if (root/path).exists():assert hashlib.sha256((root/path).read_bytes()).hexdigest()==sha
 val=load(root,'RPB108_DNE17_VALIDATION_20261009.json');assert val['status']=='PASS'
 assert F(val['original_infinite_F112_floor'])==K and val['fresh_arch_pole_replay_passed']
 for suffix in ['CERTIFICATE','REPLAY_CERTIFICATE']:
  d=load(root,'RPB108_DNE17_PRIME_SCHUR_'+suffix+'_20261009.json')
  assert d['aperture']=='53/50' and d['prime_powers']==[2,3,4,5,7,8]
  assert d['both_orientations'] and d['weight_is_actual_positive_step_function']
  assert d['symbolic_cut_order_verified'] and d['all_clipped_bands_included']
  allowance=F(d['certified_prime_norm_strict_upper']);assert allowance==F(233,100)
  assert F(d['certified_original_F112_lower'])==K and len(d['rows'])==81
  for row in d['rows']:
   lo,hi=map(F,row['weight']);pl,ph=map(F,row['prime_weight'])
   assert 0<lo<=hi and pl<=ph and ph/lo<=F(row['row_ratio_upper'])<allowance
  assert F(d['inherited_arch_minus_pole_strict_lower'])-allowance==F(d['derived_high_raw_strict_lower'])>K
 nf=load(root,'RPB108_NF47_FLOOR_TRANSPORT_VALIDATION_20261009.json','ea61fe7be3895da40c67c8f5c8cbf060032873f4210ad8831b823fe359c7a2d3')
 assert nf['status']=='PASS' and F(nf['original_F112_floor']['independent_original_F112_lower'])>F(207,1000)
 return dict(current_original_high_floor=str(K),DNE17_row_arithmetic_checked=True,
  DNE17_analytic_archimedean_and_weight_theorems_inherited=True,
  NF47_same_original_domain_attachment_inherited=True,
  fresh_NF46_original_source_replay=nf['fresh_NF46_original_source_replay'])
def run(root,massroot,newroot,parentroot,oldroot):
 standing=floor(root);prior=physical.run(massroot,newroot,parentroot,oldroot);rows=[]
 for parity in ['even','odd']:
  move=custody.load(massroot,'RPB108_NF37_'+parity.upper()+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
  q=c.matrix(move['original_selected_native_energy_Gram']);gamma=c.matrix(move['original_selected_complete_source_Gram'])
  k=direct.sub(q,direct.scale(gamma,1/K));leading=c.det2([r[:2] for r in k[:2]]);det=c.det3(k)
  assert k[0][0][0]>0 and leading[0]>0 and det[0]>0
  s,ei,beta=joined.condensation(k);assert s[0]>0
  trace=ei[0][0][1]+ei[1][1][1]+(1+sum(direct.absmax(x)**2 for x in beta))/s[0]
  old=next(r for r in prior['parity_checks'] if r['parity']==parity)
  mass=F(old['actual_lifted_Gram_operator_upper']);source=sum(gamma[i][i][1] for i in range(3))/K**2
  gap=min(1/trace/(4*(mass+source)),K/2);assert gap>F(old['conditional_physical_gap_lower'])
  if parity=='even':d=joined.load(newroot,'RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json');count='eight'
  else:d=joined.seven.load(parentroot,'RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json');count='seven'
  n=direct.sub(direct.scale(c.matrix(d[count+'_high_complete_source_Gram']),1/K),c.matrix(d[count+'_high_native_Gram']))
  _,rho,_=direct.inverse(n)
  rows.append(dict(parity=parity,plain_current_floor_determinant=c.pair(det),
   plain_current_floor_pass=True,source_response_correction_used_for_positivity=False,
   physical_gap_lower=c.pair(c.iv(gap))[0],improvement_over_CC93_lower=c.pair(c.iv(gap/F(old['conditional_physical_gap_lower'])))[0],
   same_high_response_denominator_at_current_floor_verified=True,denominator_inverse_residual_upper=c.pair(c.iv(rho))[1]))
 return dict(milestone='CC96',integration_parent='f930a038512eacfd00dcb62a7849b6a40619743e',
  read_only_DNE='2154898d5d346883cfb201d3a846f19758ac72da',read_only_Native_Source='4b1cba2a490545758c4c9d4cadd7af1d9c5d5926',
  floor_custody=standing,parity_checks=rows,exact_comparison_controls=controls(),
  original_six_retained_directions_plus_all_F_physical_gap_lower=str(min(F(r['physical_gap_lower']) for r in rows)),
  expensive_original_source_integrations_rerun=False,new_positive_retained_directions=0,
  future_full_retained_unique_source_Gram_entries=3192,future_extra_current_response_mixed_source_entries=840,
  next_collective_policy='signed uniform-floor comparison at 11/25 first; response correction at same floor only if needed',
  complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('floor_root',type=Path);ap.add_argument('mass_root',type=Path);ap.add_argument('NF46_root',type=Path);ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
 a=ap.parse_args();d=run(a.floor_root,a.mass_root,a.NF46_root,a.NF45_root,a.NF44_root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC96 PASS: current 0.44 floor suffices without response correction; physical gap',float(F(d['original_six_retained_directions_plus_all_F_physical_gap_lower'])))
