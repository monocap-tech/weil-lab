#!/usr/bin/env python3
"""Activate CC105's directional comparison using CC106's original floor."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
import validate_cc105_selected_response as prior
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc104_joint_response_rebase as response
BASE=Path(__file__).resolve().parents[1]
def run():
 floor_path=BASE/'notes/data/RPB108_CC106_HIGH_FLOOR_VALIDATION_20261010.json'
 floor=json.loads(floor_path.read_bytes());assert floor['status']=='PASS' and floor['original_infinite_F112_floor']=='73/125'
 for row in floor['rows']:
  assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256']
 old,oldhash,_=prior.read('notes/data/RPB108_CC105_SELECTED_RESPONSE_VALIDATION_20261010.json')
 assert prior.run()==old
 rows=[]
 for idx,p in enumerate(['even','odd']):
  selected=old['parity_checks'][idx]
  high,hh,_=prior.read(f'notes/cc104-source/notes/data/RPB108_NF52_{p.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')
  source,sh,_=prior.read(f'notes/data/RPB108_CC105_{p.upper()}_SOURCE_REPLAY_20261010.json')
  assert hh==selected['original_NF52_certificate_decoded_sha256'] and sh==selected['replay_decoded_sha256']
  M,QH,GH=[c.matrix(high[k]) for k in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram']]
  q=c.iv(selected['native_trial_energy']);g=c.iv(selected['projected_trial_source_square']);native=list(map(c.iv,selected['native_trial_high_row']))
  for kappa in [F(29,50),F(73,125)]:
   C=r.sub(QH,r.scale(M,kappa));N=r.sub(r.scale(GH,1/kappa),QH)
   _,cp=response.proof.proof(C);_,np=response.proof.proof(N);NI,rho=response.inverse(N)
   w=[[c.sub(c.iv(source['original_projected_source_Gram'][0][i+1]),c.mul(c.iv(kappa),v)) for i,v in enumerate(native)]]
   plain=c.sub(q,c.mul(g,c.iv(1/kappa)));credit=c.mul(c.mm(c.mm(w,NI),c.transpose(w))[0][0],c.iv(1/kappa**2));value=c.add(plain,credit)
   assert credit[0]>0 and value[0]>0
   if kappa==F(29,50):
    assert plain[1]<0 and c.overlap(value,c.iv(selected['conditional_target_refined_value']))
   rows.append(dict(parity=p,kappa=str(kappa),plain_value=c.pair(plain),response_credit=c.pair(credit),response_value=c.pair(value),surplus_proof=cp,denominator_proof=np,inverse_residual_upper=str(rho),plain_sign='POSITIVE' if plain[0]>0 else 'REJECTED' if plain[1]<0 else 'UNRESOLVED',response_sign='POSITIVE'))
   print(p,str(kappa),'plain',[float(x) for x in plain],'response',[float(x) for x in value],flush=True)
 return dict(milestone='CC106',parent='6d5109fcd50d9d280701d03d4ff16d6c9763ac02',original_high_floor='73/125',high_floor_validation_sha256=hashlib.sha256(floor_path.read_bytes()).hexdigest(),CC105_validation_sha256=oldhash,CC105_exact_rational_audit_reproduced=True,original_sources_recomputed=False,activated_actual_directional_separation_at_floor='29/50',rows=rows,full_collective_matrix_positive=False,integrated_retained_rank=56,uncovered_retained_dimension=56,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
