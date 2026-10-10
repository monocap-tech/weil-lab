#!/usr/bin/env python3
"""Independent rational custody, projection, payment, and two-order audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,ast
from validate_dne51_response_extension import read,add,sub,mul,total

def run(paths,output):
 checks=0
 def ck(v):
  nonlocal checks
  assert v;checks+=1
 def box(v):
  a=tuple(map(F,v));ck(a[0]<=a[1]);return a
 def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
 def fn(path,name):return ast.dump(next(x for x in ast.parse(Path(path).read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name),include_attributes=False)
 ck(fn('scripts/certify_dne53_even_source_extension.py','packed_conv')==fn('scripts/certify_dne50_complete_source_Gram.py','packed_conv'))
 ck(fn('scripts/certify_dne53_even_source_extension.py','root')==fn('scripts/certify_dne50_complete_source_Gram.py','root'))
 a,ah=read(paths[0]);b,bh=read(paths[1]);sv,svh=read('notes/data/RPB108_DNE50_COMPLETE_SOURCE_VALIDATION_20261010.json');row=sv['rows'][0];ck(sv['status']=='PASS' and row['parity']=='even')
 fresh=set()
 for data,N,P in ((a,360,600),(b,400,620)):
  ck(data['stage']=='DNE53' and data['parent']=='7d0d03400f78a3bf0d91d01c52a1b6d6a33e4bd4');ck((data['regular_order'],data['precision'])==(N,P));inp=[read(p) for p in data['input_paths']];ck([h for x,h in inp]==data['input_sha256']);g,e,bridge,bv,old=[x for x,h in inp];ck(bv['status']=='PASS' and bv['certificate_sha256']==inp[2][1]);ck(inp[4][1]==row['primary_sha256' if N==360 else 'replay_sha256']);ck(data['helper_sha256']==hashlib.sha256(Path('scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest())
  z=g['rows'][0];cols=z['columns'][:44]+z['high_trial_columns']+z['columns'][44:]+[{**c,'norm_upper':str(F(1)+F(1,10**100))} for c in e['proposed_source_extensions'][0]['new_trial_columns']];ck(data['columns']==cols and len(cols)==62);ck(data['column_labels']==old['column_labels']+['e112','e114','e116']);ck(data['native_to_source']==z['native_to_source'] and data['native_block']==z['native_matrix']);ck(data['trial_source_indices']==[44,45,46,59,60,61]);ck(data['retained_projection_indices']==list(range(0,112,2)));ck(data['new_action_coordinate_indices']==list(range(0,181,2)))
  ck(old['joint_packet_input_sha256'][0]==inp[0][1]);packet=dict(columns=cols,column_labels=data['column_labels'],native_matrix=z['native_matrix'],native_to_source=z['native_to_source'],trial_source_indices=[44,45,46,59,60,61]);ck(data['packet_definition_sha256']==hashlib.sha256((json.dumps(packet,sort_keys=True)+'\n').encode()).hexdigest())
  expected={(i,j) for j in (59,60) for i in (44,45,46)}|{(i,61) for i in range(62)};controls={(59,59),(59,60),(60,60)};fresh=expected|controls;ck(set(map(tuple,data['new_source_upper_triangle']))==expected==set(map(tuple,bridge['new_even_source_upper_triangle'])));ck(set(map(tuple,data['source_control_upper_triangle']))==controls and len(expected)==68)
  for key in ('retained_rounded_source_coordinates','panel_regular_polynomial_sup_error_upper','logarithmic_polynomial_sup_error_upper','source_L2_error_upper','exact_masses','physical_norm_upper','projected_source_norm_upper'):
   ck(data[key][:59]==old[key])
  for key in ('complete_rounded_source_Gram','projected_rounded_source_Gram','original_projected_source_Gram','source_Gram_error_payments'):ck([r[:59] for r in data[key][:59]]==old[key])
  eta=F(data['uniform_original_source_operator_error_upper']);sq=F(data['physical_interval_sqrt_upper']);ln=F(data['complete_log_norm_upper']);ck(eta>=2*F(53,50)*F(550,19)*F(106,125)**N+F(3,10**99));ck(sq*sq>=2*F(53,50) and ln*ln>=F(data['complete_log_squared_norm'][1]));errors=list(map(F,data['source_L2_error_upper']));roots=list(map(F,data['projected_source_norm_upper']));coords=[[box(x) for x in r] for r in data['retained_rounded_source_coordinates']];ck(len(coords)==62 and all(len(r)==56 for r in coords));newcoords=[[box(x) for x in r] for r in data['new_rounded_action_coordinates']];ck(len(newcoords)==3 and all(len(r)==91 for r in newcoords));ck([r[:56] for r in newcoords]==coords[59:])
  for i,c in enumerate(cols):
   norm=F(c['norm_upper']);mass=sum(F(v)**2 for v in c['coefficients']);ck(mass==F(data['exact_masses'][i])==F(c['exact_mass_squared']) and norm==F(data['physical_norm_upper'][i]) and norm*norm>mass);pe=list(map(F,data['panel_regular_polynomial_sup_error_upper'][i]));ck(len(pe)==7);rounding=F(data['polynomial_rounding_source_L2_error_upper'][i]);ck(rounding>=sq*max(pe)+F(data['logarithmic_polynomial_sup_error_upper'][i])*ln/2);ck(errors[i]>=eta*norm+rounding);ck(roots[i]>0 and roots[i]**2>F(data['projected_rounded_source_Gram'][i][i][1]))
  for i in range(62):
   for j in range(62):
    ck(data['original_projected_source_Gram'][i][j]==data['original_projected_source_Gram'][j][i]);box(data['original_projected_source_Gram'][i][j]);x=data['complete_rounded_source_Gram'][i][j];ck(x==data['complete_rounded_source_Gram'][j][i]);ck((x is not None)==(i<59 and j<59 or tuple(sorted((i,j))) in fresh))
  for i,j in fresh:
   whole=box(data['complete_rounded_source_Gram'][i][j]);projected=sub(whole,total(mul(x,y) for x,y in zip(coords[i],coords[j])));ck(projected==box(data['projected_rounded_source_Gram'][i][j]));pay=F(data['source_Gram_error_payments'][i][j]);ck(pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);paid=(projected[0]-pay,projected[1]+pay);ck(paid==box(data['fresh_original_projected_source_pairings'][f'{i},{j}']));
   if (i,j) in expected:ck(paid==box(data['original_projected_source_Gram'][i][j]))
   else:overlap(paid,box(data['original_projected_source_Gram'][i][j]))
  for ii,i in enumerate(data['native_to_source']):
   for u,j in enumerate((59,60)):ck(data['original_projected_source_Gram'][i][j]==bridge['reused_projected_source_pairings_Z_to_e112_e114'][ii][u])
  for u,i in enumerate((59,60)):
   for v,j in enumerate((59,60)):ck(data['original_projected_source_Gram'][i][j]==bridge['reused_projected_source_self_Gram'][u][v])
  for key in ('complete_original_source_action','exact_endpoint_logs','all_six_primes_both_orientations','complete_remaining_source_Gram_certified'):ck(data[key] is True)
  ck(data['half_translation_panels']==7 and data['polynomial_rounding_grid_digits']==250)
  for key in ('sampled_quadrature','whole_aperture_positive','RH','Lean'):ck(data[key] is False)
 for i,j in fresh:
  x=box(a['fresh_original_projected_source_pairings'][f'{i},{j}']);y=box(b['fresh_original_projected_source_pairings'][f'{i},{j}']);ck(x[0]<=y[0]<=y[1]<=x[1])
 for u in range(3):
  ea=F(a['source_L2_error_upper'][59+u]);eb=F(b['source_L2_error_upper'][59+u])
  for x,y in zip(a['new_rounded_action_coordinates'][u],b['new_rounded_action_coordinates'][u]):overlap((F(x[0])-ea,F(x[1])+ea),(F(y[0])-eb,F(y[1])+eb))
 out=dict(stage='DNE53',status='PASS',exact_rational_checks=checks,primary_path=paths[0],replay_path=paths[1],primary_sha256=ah,replay_sha256=bh,prior_source_validation_sha256=svh,source_dimension=62,reused_source_dimension=59,new_required_correlations=68,new_control_correlations=3,reused_CC_correlations=115,complete_remaining_source_Gram_certified=True,source_integrals_recomputed=True,sampled_quadrature=False,response_upper_established=False,whole_aperture_positive=False,RH=False,Lean=False);Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'DNE53 source checks',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=2);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
