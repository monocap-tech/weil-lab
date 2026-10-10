#!/usr/bin/env python3
"""Audit DNE44's paid original packet and integrate its 85 positive directions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
from certify_cc108_dne41_integration import rank,compress
BASE=Path(__file__).resolve().parents[1];ROOT='notes/cc110-source/';K=F(603,1000)
def read(p):return data.read(ROOT+p)
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 custody=json.loads((BASE/ROOT/'input_custody.json').read_bytes())
 for pin in custody['files']:check(hashlib.sha256((BASE/ROOT/pin['path']).read_bytes()).hexdigest()==pin['stored_sha256'])
 standing,sh,_=data.read('notes/data/RPB108_CC109_FULL_PACKET_INTEGRATION_20261010.json')
 check(standing['original_high_floor']==str(K) and standing['integrated_retained_rank']==72)
 fresh,fh,_=data.read('notes/data/RPB108_CC109_FRESH_HIGH_FLOOR_AUDIT_20261010.json');check(fh==standing['fresh_high_floor_validation_sha256'] and fresh['status']=='PASS' and fresh['original_infinite_F112_floor']==str(K))
 high,hh,_=data.read('notes/cc109-source/notes/data/RPB108_DNE43_HIGH_FLOOR_VALIDATION_20261010.json');check(hh==standing['published_high_floor_validation_sha256']);check(fresh=={k:v for k,v in high.items() if k!='certificate_hash_encoding'})
 prior,ph,_=data.read('notes/cc109-source/notes/data/RPB108_DNE43_FULL_PACKET_VALIDATION_20261010.json');check(ph==standing['DNE43_full_packet_validation_sha256'])
 audit,ah,_=read('notes/data/RPB108_DNE44_POSITIVE_SUBSPACE_VALIDATION_20261010.json');sourceaudit,sah,_=read('notes/data/RPB108_DNE44_JOINT_SOURCE_VALIDATION_20261010.json')
 oldaudit,oah,_=data.read('notes/cc108-source/notes/data/RPB108_DNE40_SIGNED_SOURCE_VALIDATION_20261010.json')
 check(audit['status']==sourceaudit['status']==oldaudit['status']=='PASS');check(sourceaudit['high_floor_validation_sha256']==hh and sourceaudit['prior_source_validation_sha256']==oah)
 for idx,p in enumerate(['even','odd']):
  up=p.upper();cert,ch,_=read(f'notes/data/RPB108_DNE44_{up}_POSITIVE_SUBSPACE_20261010.json.gz.b64');ar=next(x for x in audit['rows'] if x['parity']==p);sr=next(x for x in sourceaudit['rows'] if x['parity']==p)
  check(ch==ar['certificate_sha256']);a,ash,_=read(f'notes/data/RPB108_DNE44_{up}_JOINT_SOURCE_20261010.json.gz.b64');s,ssh,_=read(f'notes/data/RPB108_DNE44_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64')
  check(cert['input_sha256']==ar['input_sha256']==[ssh,ph,sah]);check([ash,ssh]==[sr['primary_sha256'],sr['replay_sha256']]);check(s['normalized_packet_sha256']==sr['packet_sha256'])
  old,osh,_=data.read(f'notes/cc108-source/notes/data/RPB108_DNE40_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');check(osh==standing['parity_checks'][idx]['source_replay_sha256']==s['reused_source_sha256']);check(s['reused_joint_dimension']==36 and s['fresh_joint_dimension']==8 and s['reused_rounded_source_definition_unchanged'])
  check(s['certificate_sha256']==old['certificate_sha256'] and s['exact_masses'][:36]==old['exact_masses'] and s['column_labels'][:36]==old['column_labels'])
  for key in ['native_block','original_projected_source_Gram','complete_rounded_source_Gram','projected_rounded_source_Gram','source_Gram_error_payments']:
   check([row[:36] for row in s[key][:36]]==old[key])
  check((a['regular_order'],s['regular_order'],a['precision'],s['precision'])==(360,400,600,620))
  for source in [a,s]:
   check(source['columns']==list(range(44)) and source['parity']==p and source['column_labels']==[f'TS{i}' for i in range(4)]+[f'X{i}' for i in range(40)])
   check(source['helper_sha256']=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8');check(source['complete_original_source_action'] and source['exact_endpoint_logs'] and source['all_six_primes_both_orientations'] and source['complete_joint_source_Gram_certified'] and not source['sampled_quadrature'])
   check(source['retained_projection_indices']==list(range(int(p=='odd'),112,2)))
   eta=F(source['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**source['regular_order']+F(3,10**99))
   sq=F(source['physical_interval_sqrt_upper']);ln=F(source['complete_log_norm_upper']);check(sq*sq>=2*F(53,50) and ln*ln>=F(source['complete_log_squared_norm'][1]))
   G=c.matrix(source['original_projected_source_Gram']);full=c.matrix(source['complete_rounded_source_Gram']);coords=c.matrix(source['retained_rounded_source_coordinates']);proj=c.matrix(source['projected_rounded_source_Gram']);errors=list(map(F,source['source_L2_error_upper']));norms=list(map(F,source['projected_source_norm_upper']))
   check(len(G)==len(full)==len(coords)==len(proj)==44)
   for i in range(44):
    norm=F(source['physical_norm_upper'][i]);check(norm**2>F(source['exact_masses'][i]) and norms[i]**2>proj[i][i][1] and len(coords[i])==56)
    pe=list(map(F,source['panel_regular_polynomial_sup_error_upper'][i]));check(len(pe)==7);rounding=F(source['polynomial_rounding_source_L2_error_upper'][i]);check(rounding>=sq*max(pe)+F(source['logarithmic_polynomial_sup_error_upper'][i])*ln/2);check(errors[i]>=eta*norm+rounding)
    for j in range(44):
     check(G[i][j]==G[j][i] and full[i][j]==full[j][i]);raw=c.sub(full[i][j],c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])));check(raw==proj[i][j]);pay=F(source['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*norms[j]+errors[j]*norms[i]+errors[i]*errors[j]);check(G[i][j]==c.add(raw,(-pay,pay)))
  GA=c.matrix(a['original_projected_source_Gram']);G=c.matrix(s['original_projected_source_Gram']);Q=c.matrix(s['native_block'])
  for i in range(44):
   for j in range(44):enclose(GA[i][j],G[i][j])
  B=[list(map(F,row)) for row in cert['positive_embedding_B']];D=[list(map(F,row)) for row in cert['negative_comparison_embedding_D']];dim=cert['positive_retained_rank'];neg=cert['negative_comparison_rank'];check((dim,neg)==[(42,2),(43,1)][idx]);check(len(B)==len(D)==44 and all(len(x)==dim for x in B) and all(len(x)==neg for x in D));check(rank([x+y for x,y in zip(B,D)])==44)
  for i in range(44):
   for j in range(36):check(B[i][j]==F(i==j))
  phys=[list(map(F,col)) for col in cert['exact_physical_columns']];ids=cert['physical_indices'];check(len(phys)==dim and all(len(x)==len(ids) for x in phys));check(rank([[x[j] for j,i in enumerate(ids) if i<112] for x in phys])==dim)
  masses=[sum(x*x for x in col) for col in phys];check(masses==list(map(F,cert['exact_physical_masses_squared'])) and all(x>0 for x in masses))
  nf,np=proof.proof(Q,cert['joint_native_positive_control']['exact_congruence_U']);check(nf>0)
  H=r.sub(r.scale(Q,K),G);HB=compress(H,B);d,pc=proof.proof(HB,cert['positive_comparison_certificate']['exact_congruence_U']);check(d>0)
  HD=r.scale(compress(H,D),F(-1));nd,npc=proof.proof(HD,cert['negative_comparison_certificate']['exact_congruence_U']);check(nd>0);check(cert['uniform_comparison_inertia']==[dim,neg,0])
  BG=compress(G,B);trace=sum(BG[i][i][1] for i in range(dim));check(trace>0);gap=min((d/K)/(4*(sum(masses)+trace/K**2)),K/2);check(gap>F(1,10**38))
  rows.append(dict(parity=p,positive_retained_rank=dim,negative_comparison_rank=neg,comparison_inertia=[dim,neg,0],prior_36_direction_span_contained=True,source_primary_sha256=ash,source_replay_sha256=ssh,positive_subspace_certificate_sha256=ch,fresh_native_positive_proof=np,fresh_positive_comparison_proof=pc,fresh_negative_comparison_proof=npc,fresh_exact_positive_physical_retained_rank=dim,physical_mass_sum=str(sum(masses)),compressed_source_trace_upper=str(trace),all_high_physical_gap_lower=str(gap),full_44_packet_uniform_criterion_rejected=True))
  print(p,'rank',dim,'inertia',[dim,neg,0],'physical gap',float(gap),flush=True)
 check(sum(x['positive_retained_rank'] for x in rows)==85)
 return dict(milestone='CC110',status='PASS',parent='eaa176a0fe27b3cf71cc6537ab7f05f3ef7d8555',read_only_DNE='bb7220c07aa66c2fea00bbc36452a59130ee3fb1',original_high_floor=str(K),exact_rational_checks=checks,CC109_standing_sha256=sh,fresh_high_floor_validation_sha256=fh,DNE44_source_validation_sha256=sah,DNE44_positive_validation_sha256=ah,parity_checks=rows,integrated_retained_rank=85,uncovered_retained_dimension=27,outside_44_packets_retained_dimension=24,inside_packets_negative_comparison_dimension=3,all_high_physical_gap_guard=str(F(1,10**38)),complete_source_entries_rechecked=7744,primary_replay_containment_checked=True,prior_72_direction_span_contained=True,source_integrals_recomputed=False,analytic_source_integrations_and_raw_packet_materialization_inherited=True,physical_domain_attachment_inherited=True,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
