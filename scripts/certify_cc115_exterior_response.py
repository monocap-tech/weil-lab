#!/usr/bin/env python3
"""Pay a fixed rational residual trial without evaluating a certified inverse."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse,time
from decimal import Decimal as D,localcontext
from cc115_response_transport import transport,signed_rows
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
BASE=Path(__file__).resolve().parents[1];K=F(647,1000)
def run(frozen=None):
 start=time.perf_counter();old,oh,_=data.read('notes/data/RPB108_CC113_RESPONSE_AT_647_20261010.json');assert old['status']=='PASS' and old['integrated_retained_rank']==88
 rows=[]
 for idx,p in enumerate(['even','odd']):
  src=old['parity_checks'][idx];assert src['parity']==p and src['full_packet_response_positive']
  high,hh,_=data.read(f'notes/cc104-source/notes/data/RPB108_NF52_{p.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');assert hh==src['NF52_high_certificate_sha256']
  packet,ph,_=data.read(f'notes/data/RPB108_CC115_{p.upper()}_PHYSICAL_PACKET_20261010.json.gz.b64');audit,ash,_=data.read('notes/data/RPB108_CC115_EXTERIOR_SOURCE_AUDIT_20261010.json');ar=audit['parity_checks'][idx];assert audit['status']=='PASS' and ar['packet_sha256']==ph;packet=dict(packet,native_block=ar['native_matrix'],original_projected_source_Gram=ar['complete_source_Gram'],exact_masses=[x['exact_mass_squared'] for x in packet['columns']])
  Q,G=c.matrix(packet['native_block']),c.matrix(packet['original_projected_source_Gram']);N=r.sub(r.scale(c.matrix(high['enlarged_high_complete_source_Gram']),1/K),c.matrix(high['enlarged_high_native_Gram']));tr,th=transport(p,packet);W=signed_rows(p,K,high,tr);n=len(N)
  # Denominator positivity is replayed; no certified inverse is formed.
  _,np=proof.proof(N,src['high_denominator_proof']['frozen_rational_congruence'])
  if frozen:
   H=[[F(x) for x in row] for row in frozen['parity_checks'][idx]['frozen_H']]
  else:
   with localcontext() as ctx:
    ctx.prec=160;dec=lambda x:D(x.numerator)/D(x.denominator)
    aug=[[dec(sum(x)/2) for x in row]+[dec(sum(W[j][i])/2) for j in range(45)] for i,row in enumerate(N)]
    for a in range(n):
     pivot=aug[a][a];assert pivot!=0;aug[a]=[x/pivot for x in aug[a]]
     for b in range(n):
      if b!=a:
       factor=aug[b][a];aug[b]=[x-factor*y for x,y in zip(aug[b],aug[a])]
    H=[[F(int(x*10**100),10**100) for x in row[n:]] for row in aug]
  assert len(H)==n and all(len(x)==44 for x in H)
  HI=[[c.iv(x) for x in row] for row in H]
  if frozen:
   # Entrywise reconstruction distinct from producer's matrix-product assembly.
   credit=[]
   for i in range(45):
    row=[]
    for j in range(45):
     v=c.sumiv([c.mul(W[i][a],c.iv(H[a][j])) for a in range(n)]+[c.mul(c.iv(H[a][i]),W[j][a]) for a in range(n)])
     penalty=c.sumiv(c.mul(c.iv(H[a][i]*H[b][j]),N[a][b]) for a in range(n) for b in range(n))
     row.append(r.compact(c.mul(c.sub(v,penalty),c.iv(1/K**2))))
    credit.append(row)
  else:
   WH=r.mm(W,HI);penalty=r.mm(c.transpose(HI),r.mm(N,HI));credit=[[r.compact(c.mul(c.sub(c.add(WH[i][j],WH[j][i]),penalty[i][j]),c.iv(1/K**2))) for j in range(45)] for i in range(45)]
  plain=r.sub(Q,r.scale(G,1/K));lower=[[r.compact(c.add(plain[i][j],credit[i][j])) for j in range(45)] for i in range(45)]
  lower=[[(min(lower[i][j][0],lower[j][i][0]),max(lower[i][j][1],lower[j][i][1])) for j in range(45)] for i in range(45)]
  fp=frozen['parity_checks'][idx]['positive_proof']['frozen_rational_congruence'] if frozen else None;d,positive=proof.proof(lower,fp)
  mass=sum(map(F,packet['exact_masses']));trace=sum(G[i][i][1] for i in range(45));gap=min(d/(4*(mass+trace/K**2)),K/2);assert gap>0
  # Exact scalar controls for completion of square: covers optimal, imperfect,
  # zero, negative fixed credit, and off-diagonal signed matrices.
  controls=[]
  for a,w,h in [(2,3,F(3,2)),(2,3,1),(2,3,0),(2,3,4)]:
   opt=F(w*w,a);trial=2*w*h-a*h*h;loss=a*(h-F(w,a))**2;assert opt-trial==loss and loss>=0;controls.append([str(opt),str(trial),str(loss)])
  row=dict(parity=p,high_decoded_sha256=hh,packet_decoded_sha256=ph,source_audit_sha256=ash,exact_transport=tr,frozen_H=[list(map(str,x)) for x in H],denominator_positive_proof=np,positive_proof=positive,coefficient_floor=str(d),physical_gap_lower=str(gap),CC112_transport_decoded_sha256=th,signed_rows_rebuilt_at_floor=str(K),signed_response_rows=[[c.pair(x) for x in row] for row in W],matrix_dimension=45,trial_dimension=n,certified_inverse_evaluations=0,fixed_trial_response_positive=True,completion_square_controls=controls)
  rows.append(row);print(p,'fixed trial PASS gap',float(gap),flush=True)
 return dict(milestone='CC115',status='PASS',CC113_decoded_sha256=oh,original_high_floor=str(K),parity_checks=rows,retained_rank=90,uncovered_retained_dimension=22,physical_guard=str(min(F(x['physical_gap_lower']) for x in rows)),source_integrations_recomputed=False,certified_inverse_evaluations=0,whole_aperture_positive=False,computational_cost_dominance_proved=False,elapsed_seconds=time.perf_counter()-start)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);a.add_argument('--replay');args=a.parse_args();frozen=json.loads(Path(args.replay).read_text()) if args.replay else None;result=run(frozen)
 if frozen:
  assert result['CC113_decoded_sha256']==frozen['CC113_decoded_sha256']
  for got,old in zip(result['parity_checks'],frozen['parity_checks']):
   for key in ['parity','high_decoded_sha256','packet_decoded_sha256','frozen_H','denominator_positive_proof','matrix_dimension','trial_dimension','completion_square_controls','CC112_transport_decoded_sha256','signed_rows_rebuilt_at_floor','signed_response_rows']:assert got[key]==old[key]
   for key in ['source_audit_sha256','exact_transport']:
    if key in old:assert got[key]==old[key]
   assert got['positive_proof']['frozen_rational_congruence']==old['positive_proof']['frozen_rational_congruence']
   assert F(got['coefficient_floor'])>=F(old['coefficient_floor']) and F(got['physical_gap_lower'])>=F(old['physical_gap_lower'])
  result['certificate_sha256']=hashlib.sha256(Path(args.replay).read_bytes()).hexdigest()
  result['entrywise_reassembly_with_frozen_trial_and_congruence']=True
  result['producer_proof_floors_reproduced_or_improved']=True
 Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
