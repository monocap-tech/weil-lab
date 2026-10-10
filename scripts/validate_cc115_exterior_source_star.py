#!/usr/bin/env python3
"""Audit new original source star, preserving the complete old44 block."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse,hashlib,ast
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
BASE=Path(__file__).resolve().parents[1]
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def contains(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def fn(p,n):return ast.dump(next(x for x in ast.parse((BASE/p).read_text()).body if isinstance(x,ast.FunctionDef) and x.name==n),include_attributes=False)
 check(fn('scripts/certify_cc115_exterior_source_star.py','packed_conv')==fn('scripts/certify_cc113_missing_source_star.py','packed_conv'))
 for idx,p in enumerate(['even','odd']):
  up=p.upper();packet,ph,_=data.read(f'notes/data/RPB108_CC115_{up}_PHYSICAL_PACKET_20261010.json.gz.b64');a,ah,_=data.read(f'notes/data/RPB108_CC115_{up}_SOURCE_PRIMARY_20261010.json');b,bh,_=data.read(f'notes/data/RPB108_CC115_{up}_SOURCE_REPLAY_20261010.json');old,oh,_=data.read(f'notes/cc110-source/notes/data/RPB108_DNE44_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');check(packet['column_labels']==[f'TS{i}' for i in range(4)]+[f'X{i}' for i in range(41)]);check(len(packet['columns'])==45);check([x[:44] for x in packet['native_matrix'][:44]]==old['native_block']);check(packet['input_sha256'][:4]==old['joint_packet_input_sha256'][:4]);check(a['regular_order']==360 and a['precision']==760 and b['regular_order']==400 and b['precision']==800)
  for src in [a,b]:
   check(src['normalized_packet_sha256']==ph==src['certificate_sha256']);check(src['native_block']==packet['native_matrix'] and src['joint_packet_input_sha256']==packet['input_sha256']);check(src['helper_sha256']==hashlib.sha256((BASE/'notes/cc101-source/scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest());check(src['complete_original_source_action'] and src['exact_endpoint_logs'] and src['all_six_primes_both_orientations'] and src['half_translation_panels']==7 and not src['sampled_quadrature']);check(src['retained_projection_indices']==list(range(idx,112,2)));eta=F(src['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**src['regular_order']+F(3,10**99));sq=F(src['physical_interval_sqrt_upper']);ln=F(src['complete_log_norm_upper']);check(sq**2>=2*F(53,50) and ln**2>=F(src['complete_log_squared_norm'][1]));coords=c.matrix(src['retained_rounded_source_coordinates']);e=list(map(F,src['source_L2_error_upper']));norm=list(map(F,src['projected_source_norm_upper']))
   for i,col in enumerate(packet['columns']):
    mass=sum(F(x)**2 for x in col['coefficients']);pn=F(col['norm_upper']);check(mass==F(col['exact_mass_squared'])==F(src['exact_masses'][i]) and pn==F(src['physical_norm_upper'][i]) and pn**2>mass);check(len(coords[i])==56 and len(src['panel_regular_polynomial_sup_error_upper'][i])==7);rounding=F(src['polynomial_rounding_source_L2_error_upper'][i]);check(rounding>=sq*max(map(F,src['panel_regular_polynomial_sup_error_upper'][i]))+F(src['logarithmic_polynomial_sup_error_upper'][i])*ln/2);check(e[i]>=eta*pn+rounding);check(norm[i]**2>F(src['projected_rounded_source_Gram'][i][i][1]))
    for j in range(45):
     if i!=44 and j!=44 and i!=j:check(src['original_projected_source_Gram'][i][j] is None);continue
     raw=c.sub(c.iv(src['complete_rounded_source_Gram'][i][j]),c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])));check(raw==c.iv(src['projected_rounded_source_Gram'][i][j]));pay=F(src['source_Gram_error_payments'][i][j]);check(pay>=e[i]*norm[j]+e[j]*norm[i]+e[i]*e[j]);check(c.add(raw,(-pay,pay))==c.iv(src['original_projected_source_Gram'][i][j]))
  for i in range(45):
   for j in range(45):
    if i==44 or j==44 or i==j:contains(c.iv(a['original_projected_source_Gram'][i][j]),c.iv(b['original_projected_source_Gram'][i][j]))
   if i<44:check(c.overlap(c.iv(b['original_projected_source_Gram'][i][i]),c.iv(old['original_projected_source_Gram'][i][i])))
  G=[[old['original_projected_source_Gram'][i][j] if i<44 and j<44 else b['original_projected_source_Gram'][i][j] for j in range(45)] for i in range(45)];check([x[:44] for x in G[:44]]==old['original_projected_source_Gram']);rows.append(dict(parity=p,packet_sha256=ph,primary_sha256=ah,replay_sha256=bh,inherited_DNE44_decoded_sha256=oh,native_matrix=packet['native_matrix'],complete_source_Gram=G,exact_mass_sum=str(sum(F(x['exact_mass_squared']) for x in packet['columns'])),literal_old44_source_block_preserved=True,new_source_mixed_pairings=44,fresh_diagonal_controls=45))
 return dict(milestone='CC115',status='PASS',exact_rational_checks=checks,parity_checks=rows,new_source_mixed_pairings=88,new_exterior_source_diagonals=2,old_diagonal_compatibility_controls=88,analytic_source_theorems_inherited=True,source_integrations_fresh=True,coverage_upgraded=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
