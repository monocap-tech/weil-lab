#!/usr/bin/env python3
"""Ingest the 111 packet and reuse original e112/e114 source pairings."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse,numpy as np
from certify_dne39_signed_comparison import read,matrix,quadratic,positive
from certify_dne32_native_remainder import I,mm,tr
ROOT='notes/dne52-cc117/'
PATHS=[ROOT+'notes/data/RPB108_CC117_COMPLETE_RESPONSE_GATE_20261010.json.gz.b64',ROOT+'notes/data/RPB108_CC117_COMPLETE_RESPONSE_VALIDATION_20261010.json',ROOT+'notes/data/RPB108_CC117_POSITIVE_PACKET_20261010.json',ROOT+'notes/data/RPB108_CC116_COMPLETE_RESPONSE_TRANSPORT_20261010.json.gz.b64',ROOT+'notes/data/RPB108_CC116_COMPLETE_RESPONSE_VALIDATION_20261010.json',ROOT+'notes/cc104-source/notes/data/RPB108_NF52_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64',ROOT+'notes/data/RPB108_CC105_EVEN_PHYSICAL_PACKET_20261010.json.gz.b64','notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64','notes/data/RPB108_DNE50_POSITIVE_SUBSPACES_20261010.json.gz.b64','notes/data/RPB108_DNE51_RESPONSE_EXTENSION_20261010.json.gz.b64','notes/data/RPB108_DNE51_RESPONSE_EXTENSION_VALIDATION_20261010.json']
K=F(647,1000)
def bb(M):return [[x.box() for x in row] for row in M]
def mid(M):return np.array([[float((x.l+x.h)/2) for x in row] for row in M])
def run(output):
 inp=[read(p) for p in PATHS];g,gv,p,t,tv,nf,physical,dne,sub,previous,pv=[x for x,h in inp]
 assert gv['status']==tv['status']==pv['status']=='PASS' and gv['gate_decoded_sha256']==inp[0][1] and gv['positive_packet_sha256']==inp[2][1] and tv['certificate_decoded_sha256']==inp[3][1] and pv['certificate_sha256']==inp[9][1]
 assert p['DNE50_positive_subspaces_decoded_sha256']==inp[8][1] and p['DNE50_full_response_decoded_sha256']==inp[7][1]
 assert p['integrated_positive_retained_rank']==111 and p['uncovered_retained_dimension']==1
 z=t['parity_checks'][0];transport=z['exact_transport'];assert z['NF52_high_decoded_sha256']==inp[5][1] and transport['CC105_high_packet_sha256']==inp[6][1]
 for j,degree in [(2,112),(3,114)]:
  c=physical['columns'][1+j];assert c['indices']==[degree] and c['coefficients']==['1'] and c['exact_mass_squared']=='1'
 C=[[I(F(x)) for x in row] for row in transport['Native_trial_transport_C']];D=[[I(F(x)) for x in row] for row in transport['paid_high_transport_D']];a=list(map(F,transport['missing_high_transport_row_t']));BN=matrix(nf['enlarged_joint_high_native_crosses']);QY=matrix(nf['enlarged_high_native_Gram']);GY=matrix(nf['enlarged_high_complete_source_Gram']);qv=[I(*x) for x in transport['recovered_native_residual_high_row']];W=matrix(z['complete_signed_response_rows'])
 CQ=mm(tr(C),BN);DQ=mm(tr(D),QY);Q=[[CQ[i][j]+DQ[i][j]+I(a[i])*qv[j] for j in (2,3)] for i in range(56)];G=[[W[i][j]+I(K)*Q[i][u] for u,j in enumerate((2,3))] for i in range(56)];selfG=[[GY[i][j] for j in (2,3)] for i in (2,3)];selfQ=[[QY[i][j] for j in (2,3)] for i in (2,3)]
 # One common witness rejects every convex average of the saved DNE budget
 # and any coefficient choice in the current CC eleven-trial even family.
 DD=[[x*I(1/K) for x in row] for row in matrix(dne['rows'][0]['paid_response_budget'])];CC=matrix(g['parity_checks'][0]['paid_response_comparison']);best=None
 for blend in np.linspace(.90,.93,301):
  vals,vec=np.linalg.eigh(float(blend)*mid(DD)+(1-float(blend))*mid(CC))
  if best is None or vals[0]>best[0]:best=(vals[0],vec[:,0])
 v=[F(round(float(x)*10**20),10**20) for x in best[1]];dq=quadratic(DD,v);assert dq.h<0
 N=[[I(1/K)*gg-qq for gg,qq in zip(gr,qr)] for gr,qr in zip(GY,QY)];pc=positive(N);assert pc;mu=F(pc['coefficient_floor_lower']);e=[sum((I(v[i])*W[i][j] for i in range(56)),I(0)) for j in range(11)];candidate=np.linalg.solve(mid(N),np.array([float((x.l+x.h)/2) for x in e]));y=[F(round(float(x)*10**60),10**60) for x in candidate];res=[ee-sum((nn*I(x) for nn,x in zip(row,y)),I(0)) for ee,row in zip(e,N)];r2=sum(max(abs(x.l),abs(x.h))**2 for x in res);credit=2*sum((I(x)*ee for x,ee in zip(y,e)),I(0))-quadratic(N,y)+I(r2/mu);plain=matrix(g['parity_checks'][0]['paid_plain_comparison']);cq=quadratic(plain,v)+credit*I(1/K**2);assert cq.h<0
 missing=[[i,j] for j in (59,60) for i in (44,45,46)]+[[i,61] for i in range(62)];assert len(missing)==68
 out=dict(stage='DNE52',parent='3e022ead0c400a5098946dc57da789592183bd5e',CC117_head='8d3b66127af94d0dba06389b14579f5b79e9a6d6',input_paths=PATHS,input_sha256=[h for x,h in inp],actual_high_floor=str(K),original_aperture='53/50',integrated_positive_retained_rank=111,uncovered_retained_dimension=1,physical_guard=str(F(1,10**39)),odd_complete_response_inherited=True,DNE50_109_span_preserved=True,even_old_response_certificate_preserved=True,reused_high_family_indices=[2,3],reused_source_native_map=z['source_native_map'],reused_native_pairings_Z_to_e112_e114=bb(Q),reused_projected_source_pairings_Z_to_e112_e114=bb(G),reused_projected_source_self_Gram=bb(selfG),reused_native_self_Gram=bb(selfQ),reused_source_correlation_count=115,new_even_source_upper_triangle=missing,new_even_source_correlation_count=68,odd_new_source_correlations_required=0,common_even_failure=dict(exact_trial=list(map(str,v)),DNE_trial_budget=dq.box(),CC_denominator_positive_certificate=pc,CC_inverse_trial=list(map(str,y)),CC_residual_squared_upper=str(r2),CC_optimal_budget_upper=cq.box(),every_convex_average_with_any_CC_coefficients_fails=True),new_source_integrations=0,new_even_positivity_established=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('DNE52 rank111; reused115 even source pairs; remaining68; common even failure',float(dq.h),float(cq.h),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);run(p.parse_args().output)
