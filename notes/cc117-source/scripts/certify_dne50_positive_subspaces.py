#!/usr/bin/env python3
"""Maximal positive parts of the paid budgets, preserving all prior 88 directions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,gzip,base64,numpy as np
from certify_dne39_signed_comparison import read,matrix,positive
from certify_dne44_positive_subspace import midpoint,compress
from certify_dne32_native_remainder import I

def run(output):
 rp='notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64';r,rh=read(rp);vp='notes/data/RPB108_DNE50_FULL_RESPONSE_VALIDATION_20261010.json';v,vh=read(vp);assert v['status']=='PASS' and v['certificate_sha256']==rh;rows=[];k=F(r['original_high_floor'])
 for z in r['rows']:
  H=matrix(z['paid_response_budget']);hm=midpoint(H);j=np.linalg.solve(hm[:44,:44],hm[:44,44:]);S=hm[44:,44:]-hm[44:,:44]@j;vals,vec=np.linalg.eigh((S+S.T)/2);assert all(abs(x)>1e-12 for x in vals);pos=[i for i,x in enumerate(vals) if x>0];neg=[i for i,x in enumerate(vals) if x<0];J=[[F(round(float(x)*10**40),10**40) for x in row] for row in j];W=[[F(round(float(x)*10**20),10**20) for x in row] for row in vec];R=[[-x for x in row] for row in J]+[[F(i==j) for j in range(12)] for i in range(12)]
  def ext(ids):return [[sum(row[t]*W[t][i] for t in range(12)) for i in ids] for row in R]
  E=ext(pos);D=ext(neg);B=[[F(i==j) for j in range(44)]+e for i,e in enumerate(E)];pc=positive(compress(H,B));nc=positive([[-x for x in row] for row in compress(H,D)]) if neg else None;assert pc and (nc or not neg);order=pos+neg;WC=[[row[i] for i in order] for row in W];Gram=[[sum(WC[t][i]*WC[t][j] for t in range(12)) for j in range(12)] for i in range(12)];wc=positive([[I(x) for x in row] for row in Gram]);assert wc
  source,sh=read(z['source_path']);assert sh==z['source_sha256'];mapn=z['native_to_source'];mass=sum(F(source['exact_masses'][i]) for i in mapn);G=matrix(z['projected_native_source_Gram']);trace=sum(G[i][i].h for i in range(56));bf=sum(x*x for row in B for x in row);massup=mass*bf;traceup=trace*bf;sf=F(pc['coefficient_floor_lower'])/k;gap=min(sf/(4*(massup+traceup/k**2)),k/2);assert gap>0;rank=len(B[0]);rows.append(dict(parity=z['parity'],positive_embedding_B=[list(map(str,row)) for row in B],negative_comparison_embedding_D=[list(map(str,row)) for row in D],bottom_full_chart=[list(map(str,row)) for row in WC],bottom_chart_Gram_positive_certificate=wc,positive_comparison_certificate=pc,negative_comparison_certificate=nc,comparison_inertia=[rank,len(neg),0],positive_retained_rank=rank,prior_44_direction_span_contained=True,embedding_Frobenius_squared=str(bf),original_packet_physical_mass=str(mass),original_projected_source_trace_upper=str(trace),physical_packet_mass_upper=str(massup),projected_source_trace_upper=str(traceup),Schur_coefficient_floor=str(sf),all_high_physical_gap_lower=str(gap)));print(z['parity'],'positive rank',rank,'comparison negative rank',len(neg),'gap',float(gap),flush=True)
 rank=sum(z['positive_retained_rank'] for z in rows);out=dict(stage='DNE50',parent='bb68642b1384d50d6b9fea517db9691e924fe5a5',input_paths=[rp,vp],input_sha256=[rh,vh],rows=rows,actual_certified_all_high_retained_dimension=rank,uncovered_retained_dimension=112-rank,prior_88_direction_span_contained=True,original_high_floor=str(k),whole_aperture_positive=rank==112,true_high_inverse_evaluated=False,RH=False,Lean=False);b=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);run(p.parse_args().output)
