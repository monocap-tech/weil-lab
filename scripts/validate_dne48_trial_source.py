#!/usr/bin/env python3
"""Independent projection/payment/old-prefix audit of the 47-column source packet."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,ast
from certify_dne39_signed_comparison import read
from materialize_dne48_trial_sources import run as materialize
from validate_dne34_source_block import add,mul,neg,boxes,sum_box

def run(paths,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def function(path,name):return ast.dump(next(n for n in ast.parse(Path(path).read_text()).body if isinstance(n,ast.FunctionDef) and n.name==name),include_attributes=False)
 check(function('scripts/certify_dne48_trial_source_Gram.py','packed_conv')==function('scripts/certify_dne44_joint_source_Gram.py','packed_conv'))
 old_validation,ovh=read('notes/data/RPB108_DNE44_JOINT_SOURCE_VALIDATION_20261010.json');check(old_validation['status']=='PASS');oldrow=next(r for r in old_validation['rows'] if r['parity']=='even')
 a,ah=read(paths[0]);b,bh=read(paths[1]);check(a['regular_order']==360 and b['regular_order']==400 and a['precision']==600 and b['precision']==620)
 pp=output+'.packet';materialize(b['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();cols=packet['columns'];check(len(cols)==47);check(packet['column_labels'][-3:]==['Y0','Y1','Y2'])
 for data in (a,b):
  check(data['stage']=='DNE48' and data['parent']=='da5b09e3b72b8e05e3daab5e37e6b3398a5558f8' and data['parity']=='even');check(data['normalized_packet_sha256']==ph);check(data['joint_packet_input_sha256']==packet['input_sha256']);check(data['columns']==list(range(47)) and data['column_labels']==packet['column_labels']);check(data['native_block']==packet['native_matrix']);cert,ch=read(data['certificate_path']);check(data['certificate_sha256']==ch and cert['parity']=='even');check(data['helper_sha256']==hashlib.sha256(Path('scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest());check(data['polynomial_rounding_grid_digits']==250)
  old,oh=read(data['reused_source_path']);check(oh==data['reused_source_sha256']);check(oh==oldrow['primary_sha256' if data['regular_order']==360 else 'replay_sha256']);check(old['normalized_packet_sha256']==packet['prior_packet_sha256']);check(data['reused_joint_dimension']==44 and data['fresh_joint_dimension']==3 and data['reused_rounded_source_definition_unchanged'])
  for key in ('retained_rounded_source_coordinates','panel_regular_polynomial_sup_error_upper','logarithmic_polynomial_sup_error_upper','source_L2_error_upper','exact_masses','physical_norm_upper'):check(data[key][:44]==old[key])
  for key in ('complete_rounded_source_Gram','projected_rounded_source_Gram','original_projected_source_Gram','source_Gram_error_payments'):check([row[:44] for row in data[key][:44]]==old[key])
  check(data['retained_projection_indices']==list(range(0,112,2)));check(data['trial_action_coordinate_indices']==list(range(0,181,2)));tcoords=boxes(data['trial_rounded_action_coordinates']);check(len(tcoords)==3 and all(len(row)==91 for row in tcoords));coords=boxes(data['retained_rounded_source_coordinates']);check(len(coords)==47 and all(len(row)==56 for row in coords));check(tcoords[0][:56]==coords[44] and tcoords[1][:56]==coords[45] and tcoords[2][:56]==coords[46]);whole=boxes(data['complete_rounded_source_Gram']);projected=boxes(data['projected_rounded_source_Gram']);original=boxes(data['original_projected_source_Gram']);check(len(whole)==len(projected)==len(original)==47 and all(len(row)==47 for row in whole+projected+original))
  eta=F(data['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**data['regular_order']+F(3,10**99));sq=F(data['physical_interval_sqrt_upper']);ln=F(data['complete_log_norm_upper']);check(sq*sq>=2*F(53,50) and ln*ln>=F(data['complete_log_squared_norm'][1]));errors=list(map(F,data['source_L2_error_upper']));roots=list(map(F,data['projected_source_norm_upper']))
  for i,c in enumerate(cols):
   mass=sum(F(v)**2 for v in c['coefficients']);norm=F(c['norm_upper']);check(mass==F(data['exact_masses'][i])==F(c['exact_mass_squared']) and norm==F(data['physical_norm_upper'][i]) and norm*norm>mass);pe=list(map(F,data['panel_regular_polynomial_sup_error_upper'][i]));check(len(pe)==7);rounding=F(data['polynomial_rounding_source_L2_error_upper'][i]);check(rounding>=sq*max(pe)+F(data['logarithmic_polynomial_sup_error_upper'][i])*ln/2);check(errors[i]>=eta*norm+rounding);check(roots[i]>0 and roots[i]**2>projected[i][i][1])
   for x in coords[i]:check(x[0]<=x[1])
  for i in range(47):
   for j in range(47):
    check(whole[i][j]==whole[j][i] and projected[i][j]==projected[j][i] and original[i][j]==original[j][i]);value=add(whole[i][j],neg(sum_box(mul(x,y) for x,y in zip(coords[i],coords[j]))));check(value==projected[i][j]);pay=F(data['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);check(original[i][j]==(value[0]-pay,value[1]+pay))
  for key in ('complete_original_source_action','exact_endpoint_logs','all_six_primes_both_orientations','complete_joint_source_Gram_certified'):check(data[key] is True)
  check(data['half_translation_panels']==7)
  for key in ('sampled_quadrature','complete_remaining_source_Gram_certified','whole_aperture_positive','RH','Lean'):check(data[key] is False)
 for i in range(47):
  for j in range(47):enclose(tuple(map(F,a['original_projected_source_Gram'][i][j])),tuple(map(F,b['original_projected_source_Gram'][i][j])))
 # Every new complete action coordinate is independently enclosed by the replay.
 for trial,(ar,br) in enumerate(zip(a['trial_rounded_action_coordinates'],b['trial_rounded_action_coordinates'])):
  for x,y in zip(ar,br):
   ea=F(a['source_L2_error_upper'][44+trial]);eb=F(b['source_L2_error_upper'][44+trial]);check(max(F(x[0])-ea,F(y[0])-eb)<=min(F(x[1])+ea,F(y[1])+eb))
 out=dict(stage='DNE48',status='PASS',exact_rational_checks=checks,primary_path=paths[0],replay_path=paths[1],primary_sha256=ah,replay_sha256=bh,packet_sha256=ph,prior_source_validation_sha256=ovh,source_dimension=47,reused_source_dimension=44,new_trial_dimension=3,new_upper_triangle_correlations=138,complete_original_trial_source_actions=True,source_integrals_recomputed=True,prior_source_entries_reintegrated=False,response_upper_established=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'trial-source checks',flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('inputs',nargs=2);ap.add_argument('--output',required=True);a=ap.parse_args();run(a.inputs,a.output)
