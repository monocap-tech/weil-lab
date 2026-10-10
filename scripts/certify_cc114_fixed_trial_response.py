#!/usr/bin/env python3
"""Pay a fixed rational residual trial without evaluating a certified inverse."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse,time
from decimal import Decimal as D,localcontext
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
  packet,ph,_=data.read(f'notes/cc110-source/notes/data/RPB108_DNE44_{p.upper()}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');assert ph==src['original_DNE44_source_sha256']
  Q,G=c.matrix(packet['native_block']),c.matrix(packet['original_projected_source_Gram']);N=r.sub(r.scale(c.matrix(high['enlarged_high_complete_source_Gram']),1/K),c.matrix(high['enlarged_high_native_Gram']));W=c.matrix(src['complete_signed_response_rows']);n=len(N)
  # Denominator positivity is replayed; no certified inverse is formed.
  _,np=proof.proof(N,src['high_denominator_proof']['frozen_rational_congruence'])
  if frozen:
   H=[[F(x) for x in row] for row in frozen['parity_checks'][idx]['frozen_H']]
  else:
   with localcontext() as ctx:
    ctx.prec=160;dec=lambda x:D(x.numerator)/D(x.denominator)
    aug=[[dec(sum(x)/2) for x in row]+[dec(sum(W[j][i])/2) for j in range(44)] for i,row in enumerate(N)]
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
   for i in range(44):
    row=[]
    for j in range(44):
     v=c.sumiv([c.mul(W[i][a],c.iv(H[a][j])) for a in range(n)]+[c.mul(c.iv(H[a][i]),W[j][a]) for a in range(n)])
     penalty=c.sumiv(c.mul(c.iv(H[a][i]*H[b][j]),N[a][b]) for a in range(n) for b in range(n))
     row.append(r.compact(c.mul(c.sub(v,penalty),c.iv(1/K**2))))
    credit.append(row)
  else:
   WH=r.mm(W,HI);penalty=r.mm(c.transpose(HI),r.mm(N,HI));credit=[[r.compact(c.mul(c.sub(c.add(WH[i][j],WH[j][i]),penalty[i][j]),c.iv(1/K**2))) for j in range(44)] for i in range(44)]
  plain=r.sub(Q,r.scale(G,1/K));lower=[[r.compact(c.add(plain[i][j],credit[i][j])) for j in range(44)] for i in range(44)]
  lower=[[(min(lower[i][j][0],lower[j][i][0]),max(lower[i][j][1],lower[j][i][1])) for j in range(44)] for i in range(44)]
  fp=frozen['parity_checks'][idx]['positive_proof']['frozen_rational_congruence'] if frozen else src['full_response_sign']['proof']['frozen_rational_congruence'];d,positive=proof.proof(lower,fp)
  mass=sum(map(F,packet['exact_masses']));trace=sum(G[i][i][1] for i in range(44));gap=min(d/(4*(mass+trace/K**2)),K/2);assert gap>F(1,10**37)
  # Exact scalar controls for completion of square: covers optimal, imperfect,
  # zero, negative fixed credit, and off-diagonal signed matrices.
  controls=[]
  for a,w,h in [(2,3,F(3,2)),(2,3,1),(2,3,0),(2,3,4)]:
   opt=F(w*w,a);trial=2*w*h-a*h*h;loss=a*(h-F(w,a))**2;assert opt-trial==loss and loss>=0;controls.append([str(opt),str(trial),str(loss)])
  row=dict(parity=p,high_decoded_sha256=hh,packet_decoded_sha256=ph,frozen_H=[list(map(str,x)) for x in H],denominator_positive_proof=np,positive_proof=positive,coefficient_floor=str(d),physical_gap_lower=str(gap),matrix_dimension=44,trial_dimension=n,certified_inverse_evaluations=0,fixed_trial_response_positive=True,completion_square_controls=controls)
  rows.append(row);print(p,'fixed trial PASS gap',float(gap),flush=True)
 return dict(milestone='CC114',status='PASS',CC113_decoded_sha256=oh,original_high_floor=str(K),parity_checks=rows,retained_rank=88,uncovered_retained_dimension=24,physical_guard=str(F(1,10**37)),source_integrations_recomputed=False,certified_inverse_evaluations=0,whole_aperture_positive=False,computational_cost_dominance_proved=False,elapsed_seconds=time.perf_counter()-start)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);a.add_argument('--replay');args=a.parse_args();frozen=json.loads(Path(args.replay).read_text()) if args.replay else None;result=run(frozen)
 if frozen:
  assert result['CC113_decoded_sha256']==frozen['CC113_decoded_sha256']
  for got,old in zip(result['parity_checks'],frozen['parity_checks']):
   for key in ['parity','high_decoded_sha256','packet_decoded_sha256','frozen_H','denominator_positive_proof','matrix_dimension','trial_dimension','completion_square_controls']:assert got[key]==old[key]
   assert got['positive_proof']['frozen_rational_congruence']==old['positive_proof']['frozen_rational_congruence']
   assert F(got['coefficient_floor'])>=F(old['coefficient_floor']) and F(got['physical_gap_lower'])>=F(old['physical_gap_lower'])
  result['certificate_sha256']=hashlib.sha256(Path(args.replay).read_bytes()).hexdigest()
  result['entrywise_reassembly_with_frozen_trial_and_congruence']=True
  result['producer_proof_floors_reproduced_or_improved']=True
 Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
