#!/usr/bin/env python3
"""Complete joint 14-trial fixed residual response on the original even Z56."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
import certify_cc104_joint_response_rebase as response
from certify_cc117_complete_response_gate import freeze
K=F(647,1000)
def run(output,replay=None):
 interface,ih,_=data.read('notes/data/RPB108_CC118_JOINT_RESPONSE_INTERFACE_20261010.json');iv,ivh,_=data.read('notes/data/RPB108_CC118_JOINT_RESPONSE_VALIDATION_20261010.json');assert iv['status']=='PASS' and iv['certificate_sha256']==ih
 sv,svh,_=data.read('notes/data/RPB108_CC119_MIXED_SOURCE_VALIDATION_20261010.json');assert sv['status']=='PASS' and sv['CC118_certificate_sha256']==ih
 src,sh,_=data.read('notes/data/RPB108_CC119_EVEN_SOURCE_REPLAY_20261010.json');assert sh==sv['rows'][1]['source_decoded_sha256'];U=[[c.iv(src['original_projected_source_Gram'][i][11+j]) for j in range(3)] for i in range(11)];T=c.matrix(interface['paid_mixed_native_matrix']);X=r.sub(r.scale(U,1/K),T);N=response.block(c.matrix(interface['CC_denominator_block']),X,c.matrix(interface['DNE_denominator_block']));W=[[r.compact(x) for x in a+b] for a,b in zip(c.matrix(interface['CC_complete_signed_response_rows']),c.matrix(interface['DNE_complete_signed_response_rows']))]
 frozen,fh,_=data.read(replay) if replay else (None,None,None);d,np=proof.proof(N,frozen['denominator_positive_proof']['frozen_rational_congruence'] if frozen else None)
 H=[[F(x) for x in row] for row in frozen['frozen_H']] if frozen else freeze(N,W);assert len(H)==14 and all(len(row)==56 for row in H);HI=[[c.iv(x) for x in row] for row in H]
 if replay:
  credit=[[r.compact(c.mul(c.sub(c.sumiv([c.mul(W[i][a],c.iv(H[a][j])) for a in range(14)]+[c.mul(c.iv(H[a][i]),W[j][a]) for a in range(14)]),c.sumiv(c.mul(c.iv(H[a][i]*H[b][j]),N[a][b]) for a in range(14) for b in range(14))),c.iv(1/K**2))) for j in range(56)] for i in range(56)]
 else:
  WH=r.mm(W,HI);PN=r.mm(c.transpose(HI),r.mm(N,HI));credit=[[r.compact(c.mul(c.sub(c.add(WH[i][j],WH[j][i]),PN[i][j]),c.iv(1/K**2))) for j in range(56)] for i in range(56)]
 cc,ch,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_GATE_20261010.json.gz.b64');assert ch==interface['CC117_gate_decoded_sha256'];plain=c.matrix(cc['parity_checks'][0]['paid_plain_comparison']);M=[[r.compact(c.add(plain[i][j],credit[i][j])) for j in range(56)] for i in range(56)];M=[[(min(M[i][j][0],M[j][i][0]),max(M[i][j][1],M[j][i][1])) for j in range(56)] for i in range(56)]
 if frozen and frozen['sign']['status']=='POSITIVE':
  sf,sp=proof.proof(M,frozen['sign']['proof']['frozen_rational_congruence']);sign=dict(status='POSITIVE',floor=str(sf),proof=sp)
 elif frozen:
  z=list(map(F,frozen['sign']['witness']));val=c.quad(M,z);sign=dict(status='REJECTED' if val[1]<0 else 'UNRESOLVED',witness=frozen['sign']['witness'],value=c.pair(val))
 else:sign=response.sign(M)
 mass=F(cc['parity_checks'][0]['physical_packet_mass']);trace=F(cc['parity_checks'][0]['projected_source_trace_upper']);gap=min(F(sign['floor'])/(4*(mass+trace/K**2)),K/2) if sign['status']=='POSITIVE' else None
 out=dict(milestone='CC119',status='PASS',CC118_certificate_sha256=ih,CC118_validation_sha256=ivh,mixed_source_validation_sha256=svh,mixed_source_replay_sha256=sh,CC117_gate_decoded_sha256=ch,original_high_floor=str(K),mixed_native_source_denominator_block=[[c.pair(x) for x in row] for row in X],joint_denominator=[[c.pair(x) for x in row] for row in N],denominator_positive_proof=np,complete_signed_response_rows=[[c.pair(x) for x in row] for row in W],frozen_H=[list(map(str,row)) for row in H],paid_response_credit=[[c.pair(x) for x in row] for row in credit],paid_full_comparison=[[c.pair(x) for x in row] for row in M],sign=sign,physical_packet_mass=str(mass),projected_source_trace_upper=str(trace),physical_gap_lower=str(gap) if gap else None,even_retained_rank=56 if gap else 55,integrated_positive_retained_rank=112 if gap else 111,uncovered_retained_dimension=0 if gap else 1,joint_trial_dimension=14,matrix_dimension=56,certified_inverse_evaluations=0,true_infinite_inverse_evaluated=False,whole_aperture_positive=bool(gap),RH=False,F4=False,Lean=False)
 if frozen:
  assert frozen['frozen_H']==out['frozen_H'] and frozen['sign']['status']==out['sign']['status'];assert sh==frozen['mixed_source_replay_sha256']
  if gap:assert gap>=F(frozen['physical_gap_lower'])
  out.update(producer_certificate_sha256=fh,independent_entrywise_response_replay=True)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('CC119 joint even',sign['status'],'physicalgap',float(gap) if gap else None,flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);a.add_argument('--replay');x=a.parse_args();run(x.output,x.replay)
