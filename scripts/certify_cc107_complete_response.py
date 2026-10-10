#!/usr/bin/env python3
"""Authenticate NF53 and rebase the complete original response at 0.584."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import certify_cc104_joint_response_rebase as previous
import validate_cc105_selected_response as selected
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
BASE=Path(__file__).resolve().parents[1];K=F(73,125)
def read(name):return selected.read(name)
def sha(name):return hashlib.sha256((BASE/name).read_bytes()).hexdigest()
def audit(parity,idx):
 previous.check_custody(parity,idx)
 prefix='notes/cc107-source/notes/data/';stem=f'RPB108_NF53_{parity.upper()}_JOINT_REFINEMENT_'
 h,_,stored=read(prefix+stem+'CERTIFICATE_20261010.json.gz.b64');v,_,_=read(prefix+stem+'VALIDATION_20261010.json')
 assert v['status']=='PASS' and v['certificate_sha256']==stored and v['inherited_NF52_certificate_and_validation_authenticated']
 assert v['validator_sha256']==sha('notes/cc107-source/scripts/validate_native_joint_refinement_nf53_106.py')
 oldpath=f'notes/cc104-source/notes/data/RPB108_NF52_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
 old,_,_=read(oldpath);assert h['inherited_NF52_certificate_sha256']==sha(oldpath)
 assert h['inherited_NF52_validation_sha256']==sha(oldpath.replace('CERTIFICATE','VALIDATION').replace('.gz.b64',''))
 assert h['original_archive_uncompressed_sha256']==old['original_archive_uncompressed_sha256']==v['original_archive_uncompressed_sha256']
 assert h['original_joined_and_T53_columns_unchanged'] and h['old_high_columns_unchanged'] and not h['original_inputs_regenerated']
 assert h['all_new_complete_source_pairings_certified'] and h['all_new_native_pairings_certified'] and h['source_analytic_infinite_remainders_paid']
 for key in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram']:
  a=c.matrix(h[key]);b=c.matrix(old[key]);assert [row[:-1] for row in a[:-1]]==b
 for key in ['enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']:
  assert [row[:-1] for row in c.matrix(h[key])]==c.matrix(old[key])
 packet,_,_=read(f'notes/data/RPB108_CC105_{parity.upper()}_PHYSICAL_PACKET_20261010.json')
 cols=[dict(zip(x['indices'],map(F,x['coefficients']))) for x in packet['columns'][1:]]
 s=h['fixed_high_selection'];y=dict(zip(s['selection_indices'],map(F,s['fixed_rational_high_coefficients'])));assert min(y)>=112 and max(y)==308-idx
 assert sum(x*x for x in y.values())==F(s['exact_new_physical_mass_squared'])
 assert all(sum(x*y.get(k,F(0)) for k,x in col.items())==0 for col in cols)
 cols.append(y);M=c.matrix(h['enlarged_high_physical_Gram']);assert len(M)==len(cols)==12-idx
 for i,col in enumerate(cols):
  for j,other in enumerate(cols):
   mass=sum(x*other.get(k,F(0)) for k,x in col.items());assert M[i][j][0]<=mass<=M[i][j][1]
 o,_,_=read(f'notes/cc104-source/notes/data/RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64')
 errors=list(map(F,o['joined_source_physical_errors']+o['remaining_source_physical_errors']+o['high_source_physical_errors']))
 norms=list(map(F,o['joined_source_approximant_norm_upper']+o['remaining_source_approximant_norm_upper']+o['high_source_approximant_norm_upper']))
 for nf in [50,51,52]:
  root='notes/cc105-source' if nf<52 else 'notes/cc104-source'
  z,_,_=read(f'{root}/notes/data/RPB108_NF{nf}_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')
  errors.append(F(z['new_projected_source_error_upper']));norms.append(F(z['new_source_approximant_norm_upper']))
 ey=F(h['new_projected_source_error_upper']);ny=F(h['new_source_approximant_norm_upper']);errors.append(ey);norms.append(ny)
 raw=list(map(c.iv,h['reconstructed_new_complete_source_pairings']));paid=list(map(c.iv,h['original_new_complete_source_pairings']));assert len(raw)==len(errors)==68-idx
 for a,b,e,n in zip(raw,paid,errors,norms):
  payment=e*ny+ey*n+e*ey;value=c.add(a,(-payment,payment));assert b[0]<=value[0]<=value[1]<=b[1]
 QH,GH,B,S=[c.matrix(h[k]) for k in ['enlarged_high_native_Gram','enlarged_high_complete_source_Gram','enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']]
 assert [row[-1] for row in S]+[row[-1] for row in GH]==paid
 assert [row[-1] for row in B]+[row[-1] for row in QH]==list(map(c.iv,h['new_native_pairings']))
 return h,stored

def run(parity,idx):
 h,stored=audit(parity,idx);print(parity,'NF53 custody/physical/source payments passed',flush=True)
 o,_,_=read(f'notes/cc104-source/notes/data/RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64')
 joined,_,_=read(f'notes/cc104-source/notes/data/RPB108_NF37_{parity.upper()}_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
 native,_,_=read('notes/cc104-source/notes/data/RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64');native=native['parity_certificates'][idx]
 Q=previous.block(c.matrix(joined['original_selected_native_energy_Gram']),c.matrix(native['original_remaining_native_couplings']),c.matrix(native['original_remaining_native_Gram']))
 G=previous.block(c.matrix(joined['original_selected_complete_source_Gram']),c.transpose(c.matrix(o['original_remaining_joined_source_crosses'])),previous.unpack(o['original_remaining_complete_source_Gram_upper'],53))
 M,QH,GH,B,S=[c.matrix(h[k]) for k in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram','enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']]
 C=r.sub(QH,r.scale(M,K));N=r.sub(r.scale(GH,1/K),QH);W=r.sub(S,r.scale(B,K))
 _,cp=previous.proof.proof(C);_,np=previous.proof.proof(N);NI,rho=previous.inverse(N)
 print(parity,'surplus/denominator/inverse paid',float(rho),flush=True)
 gain=r.scale(r.mm(r.mm(W,NI),c.transpose(W)),1/K**2);plain=r.sub(Q,r.scale(G,1/K))
 lower=[[r.compact(c.add(x,y)) for x,y in zip(a,b)] for a,b in zip(plain,gain)]
 lower=[[(min(lower[i][j][0],lower[j][i][0]),max(lower[i][j][1],lower[j][i][1])) for j in range(56)] for i in range(56)]
 plain_sign=previous.sign(plain);response_sign=previous.sign(lower)
 prefixes=[]
 for n in ([54,48,40,32,24,16,12] if idx==0 else [53,48,40,32,24,20]):
  try: coefficient_floor,certificate=previous.proof.proof([row[:n] for row in lower[:n]])
  except AssertionError: continue
  prefixes.append(dict(dimension=n,coefficient_floor=str(coefficient_floor),positive_proof=certificate));print(parity,'certified response prefix',n,flush=True);break
 assert prefixes
 trials=[]
 candidates=[('NF53_historical',h['joint_lower_bound_sign']['fixed_rational_lower_bound_witness'])]
 if 'witness' in response_sign:candidates.append(('new_collective_midpoint',response_sign['witness']))
 for label,raw in candidates:
  z=list(map(F,raw));wz=c.mm([list(map(c.iv,z))],W)
  q=c.quad(Q,z);g=c.quad(G,z);credit=c.mul(c.mm(c.mm(wz,NI),c.transpose(wz))[0][0],c.iv(1/K**2));pv=c.sub(q,c.mul(g,c.iv(1/K)));rv=c.add(pv,credit)
  trials.append(dict(label=label,witness=list(map(str,z)),plain_value=c.pair(pv),response_credit=c.pair(credit),response_value=c.pair(rv),response_sign='POSITIVE' if rv[0]>0 else 'REJECTED' if rv[1]<0 else 'UNRESOLVED'))
  print(parity,label,trials[-1]['response_sign'],[float(x) for x in rv],flush=True)
  if label=='new_collective_midpoint':
   response_sign['correlated_value']=c.pair(rv);response_sign['status']=trials[-1]['response_sign']
   midpoint=[[c.iv(sum(x)/2) for x in row] for row in lower];box_value=c.quad(midpoint,z);assert box_value[1]<0
   response_sign['interval_box_midpoint_negative_exact_value']=c.pair(box_value)
   response_sign['actual_original_negative_form_claimed']=False
 return dict(parity=parity,NF53_stored_sha256=stored,kappa=str(K),joint_dimension=56,high_dimension=len(M),surplus_proof=cp,denominator_proof=np,inverse_residual_upper=str(rho),plain_sign=plain_sign,response_sign=response_sign,trials=trials,certified_response_prefixes=prefixes,whole_collective_positive=response_sign['status']=='POSITIVE')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 custody=json.loads((BASE/'notes/cc107-source/input_custody.json').read_bytes())
 for pin in custody['files']:assert sha('notes/cc107-source/'+pin['path'])==pin['sha256']
 floor,fh,_=read('notes/data/RPB108_CC106_HIGH_FLOOR_VALIDATION_20261010.json');assert floor['status']=='PASS' and floor['original_infinite_F112_floor']==str(K)
 for row in floor['rows']:assert sha(row['path'])==row['sha256']
 rows=[run(p,i) for i,p in enumerate(['even','odd'])]
 out=dict(milestone='CC107',parent='1742db941887e45ebff52046d8d10a8db707fdfc',original_high_floor=str(K),high_floor_validation_decoded_sha256=fh,source_integrations_recomputed=False,NF53_independent_analytic_validations_inherited=True,complete_collective_matrix_arithmetic_fresh=True,parity_checks=rows,full_collective_positive=all(x['whole_collective_positive'] for x in rows),integrated_retained_rank=56,uncovered_retained_dimension=56,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
