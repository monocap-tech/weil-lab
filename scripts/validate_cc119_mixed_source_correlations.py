#!/usr/bin/env python3
"""Independent coherent source projection/payment and primary/replay audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,ast
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
K=F(647,1000)
def run(output):
 checks=0
 def check(x):
  nonlocal checks
  assert x;checks+=1
 def contain(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 packet,ph,_=data.read('notes/data/RPB108_CC119_EVEN_PHYSICAL_PACKET_20261010.json');old,oh,_=data.read('notes/data/RPB108_CC118_JOINT_RESPONSE_INTERFACE_20261010.json');ov,ovh,_=data.read('notes/data/RPB108_CC118_JOINT_RESPONSE_VALIDATION_20261010.json');check(ov['status']=='PASS' and ov['certificate_sha256']==oh and packet['input_sha256'][0]==oh);check(packet['columns']==old['joint_high_columns'] and len(packet['columns'])==14);pairs=[[i,j] for i in range(14) for j in range(i,14) if i==j or i<11<=j];check(packet['source_upper_pairs']==pairs and len(pairs)==47)
 def function(path,name):return ast.dump(next(x for x in ast.parse(Path(path).read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name),include_attributes=False)
 check(function('scripts/certify_cc119_mixed_source_correlations.py','packed_conv')==function('scripts/certify_cc113_missing_source_star.py','packed_conv'))
 helper=hashlib.sha256(Path('notes/cc101-source/scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest();check(helper=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8');rows=[];sources=[]
 for label,n,p in [('PRIMARY',360,760),('REPLAY',400,800)]:
  src,sh,_=data.read(f'notes/data/RPB108_CC119_EVEN_SOURCE_{label}_20261010.json');sources.append(src);check(src['stage']=='CC119' and src['parity']=='even' and src['normalized_packet_sha256']==ph);check(src['regular_order']==n and src['precision']==p and src['helper_sha256']==helper);check(src['native_block']==packet['native_matrix'] and src['joint_packet_input_sha256']==packet['input_sha256']);check(src['columns']==list(range(14)) and src['column_labels']==packet['column_labels']);check(src['retained_projection_indices']==list(range(0,112,2)));check(src['complete_original_source_action'] and src['exact_endpoint_logs'] and src['all_six_primes_both_orientations'] and src['half_translation_panels']==7 and not src['sampled_quadrature']);check(src['complete_missing_mixed_source_correlations_certified'] and src['missing_cross_count']==33 and not src['complete_joint_source_Gram_certified'])
  archive,arh,_=data.read(f'notes/data/RPB108_CC119_EVEN_{label}_PROFILES_20261010.json.gz.b64');identity=archive['identity'];check(identity['packet_sha256']==ph and identity['helper_sha256']==helper and identity['order']==n and identity['precision']==p);check(identity['producer_sha256']==hashlib.sha256(Path('scripts/certify_cc119_mixed_source_correlations.py').read_bytes()).hexdigest());check(len(archive['profiles'])==14)
  for i,profile in enumerate(archive['profiles']):check(profile['identity']==identity and profile['column_sha256']==hashlib.sha256(json.dumps(packet['columns'][i],sort_keys=True).encode()).hexdigest());check(hashlib.sha256(json.dumps(profile).encode()).hexdigest()==archive['profile_stored_sha256'][i])
  whole=src['complete_rounded_source_Gram'];proj=src['projected_rounded_source_Gram'];G=src['original_projected_source_Gram'];coords=c.matrix(src['retained_rounded_source_coordinates']);check(len(coords)==14 and all(len(row)==56 for row in coords));errors=list(map(F,src['source_L2_error_upper']));roots=list(map(F,src['projected_source_norm_upper']));eta=F(src['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**n+F(3,10**99));sq=F(src['physical_interval_sqrt_upper']);ln=F(src['complete_log_norm_upper']);check(sq*sq>=F(53,25) and ln*ln>=F(src['complete_log_squared_norm'][1]));check(src['polynomial_rounding_grid_digits']==250)
  for i,col in enumerate(packet['columns']):
   mass=sum(F(x)**2 for x in col['coefficients']);norm=F(col['norm_upper']);check(mass==F(col['exact_mass_squared'])==F(src['exact_masses'][i]) and norm==F(src['physical_norm_upper'][i]) and norm*norm>mass);pe=list(map(F,src['panel_regular_polynomial_sup_error_upper'][i]));check(len(pe)==7);rounding=F(src['polynomial_rounding_source_L2_error_upper'][i]);check(rounding>=sq*max(pe)+F(src['logarithmic_polynomial_sup_error_upper'][i])*ln/2);check(errors[i]>=eta*norm+rounding);check(roots[i]>0 and roots[i]**2>F(proj[i][i][1]))
   for j in range(14):
    selected=i==j or min(i,j)<11<=max(i,j)
    if not selected:check(whole[i][j] is None and proj[i][j] is None and G[i][j] is None and src['source_Gram_error_payments'][i][j] is None);continue
    check(whole[i][j]==whole[j][i] and proj[i][j]==proj[j][i] and G[i][j]==G[j][i]);raw=c.sub(c.iv(whole[i][j]),c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])));check(raw==c.iv(proj[i][j]));pay=F(src['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);check(c.iv(G[i][j])==c.add(raw,(-pay,pay)))
  rows.append(dict(run=label,source_decoded_sha256=sh,profiles_decoded_sha256=arh,regular_order=n,precision=p,coherent_selected_upper_correlations=47))
 # All paid entries, including the diagonal controls, nest after original
 # source-error payment. Raw approximants need not nest across Taylor orders.
 for i,j in pairs:contain(c.iv(sources[0]['original_projected_source_Gram'][i][j]),c.iv(sources[1]['original_projected_source_Gram'][i][j]))
 for i in range(14):
  ea=F(sources[0]['source_L2_error_upper'][i]);eb=F(sources[1]['source_L2_error_upper'][i])
  for x,y in zip(sources[0]['retained_rounded_source_coordinates'][i],sources[1]['retained_rounded_source_coordinates'][i]):check(max(F(x[0])-ea,F(y[0])-eb)<=min(F(x[1])+ea,F(y[1])+eb))
 high,hh,_=data.read('notes/cc104-source/notes/data/RPB108_NF52_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');dn,dh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_EVEN_COMPLETE_SOURCE_20261010.json.gz.b64');check(hh==packet['input_sha256'][1]);oldGY=high['enlarged_high_complete_source_Gram'];mapping=dn['trial_source_indices'];DG=dn['original_projected_source_Gram']
 oldresponse,orh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64');oldsv,osvh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_COMPLETE_SOURCE_VALIDATION_20261010.json');check(oldsv['status']=='PASS' and oldsv['rows'][0]['primary_sha256']==dh);check(orh==packet['input_sha256'][2]==old['DNE50_response_decoded_sha256'])
 for i in range(14):
  known=c.iv(oldGY[i][i] if i<11 else DG[mapping[i-11]][mapping[i-11]])
  for src in sources:check(c.overlap(known,c.iv(src['original_projected_source_Gram'][i][i])))
 out=dict(milestone='CC119',status='PASS',exact_rational_checks=checks,physical_packet_sha256=ph,CC118_certificate_sha256=oh,CC118_validation_sha256=ovh,rows=rows,new_mixed_source_correlations_certified=33,fresh_diagonal_controls=14,original_analytic_source_domain_theorems_inherited=True,fresh_analytic_source_integrals=True,complete_joint_source_Gram_assembled=False,joint_response_gate_evaluated=False,integrated_positive_retained_rank=111,uncovered_retained_dimension=1,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('CC119 mixed source PASS',checks,'checks',flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);run(a.parse_args().output)
