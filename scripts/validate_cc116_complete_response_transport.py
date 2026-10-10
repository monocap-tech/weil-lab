#!/usr/bin/env python3
"""Directly reassemble all signed rows and verify saved full physical transport."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc101_next_source_packet as proof
from certify_cc108_dne41_integration import rank
from certify_cc112_physical_response_transport import solve,sparse
K=F(647,1000)
def run(path):
 saved,sh,_=data.read(path);checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 check(saved['status']=='PASS' and saved['complete_current_family_response_rows_paid'] and not saved['complete_original_G56_certified']);dne,dh,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64');audit,ah,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_VALIDATION_20261010.json');check(audit['status']=='PASS' and dh==audit['certificate_sha256'] and ah==saved['DNE49_validation_sha256']);old,oh,_=data.read('notes/data/RPB108_CC115_CORRECTED_647_RESPONSE_20261010.json');check(oh==saved['CC115_corrected_certificate_sha256']);fr,fh,_=data.read('notes/cc104-source/notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
 for idx,p in enumerate(['even','odd']):
  row=saved['parity_checks'][idx];tr=row['exact_transport'];check(row['parity']==p and row['signed_response_floor']==str(K) and row['DNE49_decoded_sha256']==dh and tr['NF47_frame_sha256']==fh)
  frame=fr['parity_frames'][idx];joined=[sparse(x) for x in frame['unchanged_joined_columns']];low=frame['retained_indices'];pv=frame['old_two_constraint_pivots']+[frame['old_free_coordinates'][frame['third_constraint_pivot_in_old_free_coordinates']]];free=[i for i in frame['old_free_coordinates'] if i!=pv[2]];A=[[x.get(low[i],F(0)) for i in pv] for x in joined];R=[[-x.get(low[i],F(0)) for i in free] for x in joined];sol=solve(A,R);native=joined+[{low[i]:F(1),**{low[q]:sol[k][j] for k,q in enumerate(pv)}} for j,i in enumerate(free)]
  hp,hph,_=data.read(f'notes/data/RPB108_CC105_{p.upper()}_PHYSICAL_PACKET_20261010.json');check(hph==tr['CC105_high_packet_sha256']);Y=[sparse(x) for x in hp['columns'][1:]];v=dict(zip(tr['high_residual_indices'],map(F,tr['exact_missing_high_coefficients'])));C=[list(map(F,x)) for x in tr['Native_trial_transport_C']];D=[list(map(F,x)) for x in tr['paid_high_transport_D']];t=list(map(F,tr['missing_high_transport_row_t']));check(rank(C)==56)
  cols=dne['rows'][idx]['columns'];ids=sorted(set().union(*(set(x) for x in native+Y+[v]+[sparse(x) for x in cols])))
  for j,col in enumerate(cols):
   raw=sparse(col)
   for degree in ids:check(sum(C[a][j]*x.get(degree,F(0)) for a,x in enumerate(native))+sum(D[a][j]*x.get(degree,F(0)) for a,x in enumerate(Y))+t[j]*v.get(degree,F(0))==raw.get(degree,F(0)))
  high,hh,_=data.read(f'notes/cc104-source/notes/data/RPB108_NF52_{p.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');check(hh==row['NF52_high_decoded_sha256']);BN,SN,QY,GY=[c.matrix(high[k]) for k in ['enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses','enlarged_high_native_Gram','enlarged_high_complete_source_Gram']];star,_,_=data.read(f'notes/data/RPB108_CC113_{p.upper()}_SOURCE_REPLAY_20261010.json');gv=list(map(c.iv,star['original_projected_source_Gram'][0][1:]));qv=list(map(c.iv,tr['recovered_native_residual_high_row']));W=c.matrix(row['complete_signed_response_rows'])
  for i in range(56):
   for j in range(11-idx):
    actual=c.sumiv([c.mul(c.iv(C[a][i]),c.sub(SN[a][j],c.mul(c.iv(K),BN[a][j]))) for a in range(56)]+[c.mul(c.iv(D[a][i]),c.sub(GY[a][j],c.mul(c.iv(K),QY[a][j]))) for a in range(11-idx)]+[c.mul(c.iv(t[i]),c.sub(gv[j],c.mul(c.iv(K),qv[j])))])
    check(W[i][j][0]<=actual[0]<=actual[1]<=W[i][j][1])
  check(row['complete_signed_response_rows'][:44]==old['parity_checks'][idx]['signed_response_rows']);Q=c.matrix(dne['rows'][idx]['native_matrix']);d,qp=proof.proof(Q,row['finite_native_positive_proof']['frozen_rational_congruence']);check(d>=F(row['finite_native_positive_proof']['coefficient_floor_lower']))
  N=[[c.sub(c.mul(c.iv(1/K),GY[i][j]),QY[i][j]) for j in range(11-idx)] for i in range(11-idx)];_,np=proof.proof(N,row['response_denominator_positive_proof']['frozen_rational_congruence']);mapping=list(range(44))+list(range(47,59)) if idx==0 else list(range(56));check(mapping==row['source_native_map']);rows.append(dict(parity=p,exact_retained_rank=56,all_physical_column_identities_checked=True,complete_signed_rows_checked=56*(11-idx),finite_native_coefficient_floor=str(d),source_native_map=mapping))
 return dict(milestone='CC116',status='PASS',certificate_decoded_sha256=sh,exact_rational_checks=checks,parity_checks=rows,complete_signed_rows_checked=1176,full_retained_chart_rank=112,positive_all_high_retained_rank=88,uncovered_retained_dimension=24,complete_original_G56_certified=False,whole_response_gate_evaluated=False,whole_aperture_positive=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(a.certificate),indent=2)+'\n')
