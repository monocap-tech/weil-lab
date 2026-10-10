#!/usr/bin/env python3
"""Pay a complete 56-column response gate using the CC116 high family."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import json,gzip,base64,argparse,time
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
import certify_cc104_joint_response_rebase as response
K=F(647,1000)
def freeze(N,W):
 with localcontext() as ctx:
  ctx.prec=160;dec=lambda x:D(x.numerator)/D(x.denominator);n=len(N)
  a=[[dec(sum(v)/2) for v in row]+[dec(sum(W[j][i])/2) for j in range(56)] for i,row in enumerate(N)]
  for i in range(n):
   v=a[i][i];assert v!=0;a[i]=[x/v for x in a[i]]
   for j in range(n):
    if j!=i:
     v=a[j][i];a[j]=[x-v*y for x,y in zip(a[j],a[i])]
  return [[F(int(x*10**100),10**100) for x in row[n:]] for row in a]
def run(output,replay=None):
 start=time.perf_counter();saved,sh,_=data.read(replay) if replay else (None,None,None)
 tr,th,_=data.read('notes/data/RPB108_CC116_COMPLETE_RESPONSE_TRANSPORT_20261010.json.gz.b64');tv,tvh,_=data.read('notes/data/RPB108_CC116_COMPLETE_RESPONSE_VALIDATION_20261010.json')
 assert tv['status']=='PASS' and tv['certificate_decoded_sha256']==th
 sv,svh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_COMPLETE_SOURCE_VALIDATION_20261010.json');assert sv['status']=='PASS'
 packet,ph,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64')
 floor,fh,_=data.read('notes/data/RPB108_CC113_FRESH_HIGH_FLOOR_AUDIT_20261010.json');assert floor['status']=='PASS' and F(floor['original_infinite_F112_floor'])>=K
 rows=[]
 for idx,p in enumerate(['even','odd']):
  z=tr['parity_checks'][idx];src,gh,_=data.read(f'notes/cc117-source/notes/data/RPB108_DNE50_{p.upper()}_COMPLETE_SOURCE_20261010.json.gz.b64')
  assert gh==sv['rows'][idx]['primary_sha256'] and src['native_block']==packet['rows'][idx]['native_matrix'] and src['parity']==p
  mapping=src['native_to_source'];assert mapping==z['source_native_map']==packet['rows'][idx]['native_to_source'] and len(mapping)==56
  Q=c.matrix(src['native_block']);allG=c.matrix(src['original_projected_source_Gram']);G=[[allG[i][j] for j in mapping] for i in mapping]
  high,hh,_=data.read(f'notes/cc104-source/notes/data/RPB108_NF52_{p.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');assert hh==z['NF52_high_decoded_sha256']
  N=r.sub(r.scale(c.matrix(high['enlarged_high_complete_source_Gram']),1/K),c.matrix(high['enlarged_high_native_Gram']));W=c.matrix(z['complete_signed_response_rows']);n=len(N)
  assert z['signed_response_floor']==str(K) and len(W)==56 and all(len(row)==n for row in W)
  _,np=proof.proof(N,z['response_denominator_positive_proof']['frozen_rational_congruence'])
  old=saved['parity_checks'][idx] if saved else None;H=[[F(x) for x in row] for row in old['frozen_H']] if old else freeze(N,W);HI=[[c.iv(x) for x in row] for row in H]
  if replay:
   credit=[[r.compact(c.mul(c.sub(c.sumiv([c.mul(W[i][a],c.iv(H[a][j])) for a in range(n)]+[c.mul(c.iv(H[a][i]),W[j][a]) for a in range(n)]),c.sumiv(c.mul(c.iv(H[a][i]*H[b][j]),N[a][b]) for a in range(n) for b in range(n))),c.iv(1/K**2))) for j in range(56)] for i in range(56)]
  else:
   WH=r.mm(W,HI);penalty=r.mm(c.transpose(HI),r.mm(N,HI));credit=[[r.compact(c.mul(c.sub(c.add(WH[i][j],WH[j][i]),penalty[i][j]),c.iv(1/K**2))) for j in range(56)] for i in range(56)]
  plain=r.sub(Q,r.scale(G,1/K));S=[[r.compact(c.add(plain[i][j],credit[i][j])) for j in range(56)] for i in range(56)];S=[[(min(S[i][j][0],S[j][i][0]),max(S[i][j][1],S[j][i][1])) for j in range(56)] for i in range(56)]
  if old and old['full_response_sign']['status']=='POSITIVE':
   d,pc=proof.proof(S,old['full_response_sign']['proof']['frozen_rational_congruence']);sign=dict(status='POSITIVE',floor=str(d),proof=pc)
  elif old:
   v=list(map(F,old['full_response_sign']['witness']));value=c.quad(S,v);sign=dict(status='REJECTED' if value[1]<0 else 'UNRESOLVED',witness=old['full_response_sign']['witness'],value=c.pair(value))
  else:sign=response.sign(S)
  mass=sum(F(src['exact_masses'][i]) for i in mapping);trace=sum(G[i][i][1] for i in range(56));gap=min(F(sign['floor'])/(4*(mass+trace/K**2)),K/2) if sign['status']=='POSITIVE' else None
  row=dict(parity=p,source_decoded_sha256=gh,high_decoded_sha256=hh,native_to_source=mapping,frozen_H=[list(map(str,row)) for row in H],denominator_positive_proof=np,paid_plain_comparison=[[c.pair(x) for x in row] for row in plain],paid_response_credit=[[c.pair(x) for x in row] for row in credit],paid_response_comparison=[[c.pair(x) for x in row] for row in S],full_response_sign=sign,physical_packet_mass=str(mass),projected_source_trace_upper=str(trace),physical_gap_lower=str(gap) if gap else None,matrix_dimension=56,trial_dimension=n)
  if old:
   assert row['frozen_H']==old['frozen_H'] and row['source_decoded_sha256']==old['source_decoded_sha256'];assert sign['status']==old['full_response_sign']['status']
   if gap:assert gap>=F(old['physical_gap_lower'])
  rows.append(row);print(p,sign['status'],'gap',float(gap) if gap else None,flush=True)
 whole=all(z['full_response_sign']['status']=='POSITIVE' for z in rows)
 out=dict(milestone='CC117',status='PASS',CC116_decoded_sha256=th,CC116_validation_sha256=tvh,DNE50_source_validation_sha256=svh,DNE49_packet_decoded_sha256=ph,current_high_floor_audit_sha256=fh,original_high_floor=str(K),parity_checks=rows,full_packet_retained_rank=112,whole_aperture_positive=whole,original_analytic_source_domain_high_floor_theorems_inherited=True,source_integrals_recomputed=False,certified_inverse_evaluations=0,computational_cost_dominance_proved=False,RH=False,F4=False,Lean=False,elapsed_seconds=time.perf_counter()-start)
 if replay:out.update(producer_decoded_sha256=sh,independent_entrywise_reassembly=True)
 b=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);a.add_argument('--replay');x=a.parse_args();run(x.output,x.replay)
