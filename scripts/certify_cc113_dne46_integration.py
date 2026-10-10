#!/usr/bin/env python3
"""Freshly integrate DNE46's current original floor and nested 87-direction span."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse,hashlib
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
from certify_cc108_dne41_integration import rank,compress
BASE=Path(__file__).resolve().parents[1];K=F(647,1000)
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 for x in json.loads((BASE/'notes/cc113-source/input_custody.json').read_text())['files']:check(hashlib.sha256((BASE/'notes/cc113-source'/x['path']).read_bytes()).hexdigest()==x['stored_sha256'])
 fresh,fh,_=data.read('notes/data/RPB108_CC113_FRESH_HIGH_FLOOR_AUDIT_20261010.json');high,hh,_=data.read('notes/cc113-source/notes/data/RPB108_DNE46_HIGH_FLOOR_VALIDATION_20261010.json');check({k:v for k,v in fresh.items() if k!='certificate_path'}=={k:v for k,v in high.items() if k!='certificate_path'});check(high['status']=='PASS' and high['original_infinite_F112_floor']==str(K))
 audit,ah,_=data.read('notes/cc113-source/notes/data/RPB108_DNE46_POSITIVE_SUBSPACE_VALIDATION_20261010.json');check(audit['status']=='PASS' and audit['all_high_positive_retained_dimension']==87)
 for idx,p in enumerate(['even','odd']):
  up=p.upper();cert,ch,_=data.read(f'notes/cc113-source/notes/data/RPB108_DNE46_{up}_POSITIVE_SUBSPACE_20261010.json.gz.b64');ar=next(x for x in audit['rows'] if x['parity']==p);check(ch==ar['certificate_sha256'])
  inputs=[data.read(('notes/cc113-source/' if 'DNE46' in q else 'notes/cc110-source/')+q) for q in cert['input_paths']];check([x[1] for x in inputs]==cert['input_sha256']==ar['input_sha256']);s,old,h,a=[x[0] for x in inputs]
  Q=c.matrix(s['native_block']);G=c.matrix(s['original_projected_source_Gram']);H=r.sub(r.scale(Q,K),G);B=[list(map(F,row)) for row in cert['positive_embedding_B']];D=[list(map(F,row)) for row in cert['negative_comparison_embedding_D']];prior=[list(map(F,row)) for row in old['positive_embedding_B']];dim=len(B[0]);z=len(D[0]);check((dim,z)==[(43,1),(44,0)][idx]);check(rank([b+d for b,d in zip(B,D)])==44);check(all(b[:len(prior[0])]==a for a,b in zip(prior,B)))
  phys=[list(map(F,x)) for x in cert['exact_physical_columns']];ids=cert['physical_indices'];check(rank([[col[j] for j,i in enumerate(ids) if i<112] for col in phys])==dim);masses=[sum(x*x for x in col) for col in phys];check(masses==list(map(F,cert['exact_physical_masses_squared'])))
  _,np=proof.proof(Q,cert['joint_native_positive_control']['exact_congruence_U']);d,pc=proof.proof(compress(H,B),cert['positive_comparison_certificate']['exact_congruence_U'])
  nc=None
  if z:_,nc=proof.proof(r.scale(compress(H,D),F(-1)),cert['negative_comparison_certificate']['exact_congruence_U'])
  BG=compress(G,B);trace=sum(BG[i][i][1] for i in range(dim));gap=min((d/K)/(4*(sum(masses)+trace/K**2)),K/2);check(gap>F(1,10**37))
  rows.append(dict(parity=p,source_replay_sha256=inputs[0][1],DNE46_subspace_certificate_sha256=ch,positive_retained_rank=dim,negative_comparison_rank=z,comparison_inertia=[dim,z,0],prior_CC110_span_contained=True,fresh_native_positive_proof=np,fresh_positive_comparison_proof=pc,fresh_negative_comparison_proof=nc,physical_mass_sum=str(sum(masses)),complete_compressed_source_trace_upper=str(trace),all_high_physical_gap_lower=str(gap)))
  print(p,'DNE46 integrated',dim,'guard gap',float(gap),flush=True)
 return dict(milestone='CC113',status='PASS',original_high_floor=str(K),fresh_high_floor_audit_sha256=fh,DNE46_positive_audit_sha256=ah,exact_integration_checks=checks,parity_checks=rows,integrated_retained_rank=87,uncovered_retained_dimension=25,outside_computed_packet_dimension=24,inside_even_comparison_dimension=1,prior_85_direction_span_contained=True,all_high_physical_gap_guard=str(F(1,10**37)),source_integrals_recomputed=False,physical_domain_attachment_inherited=True,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
