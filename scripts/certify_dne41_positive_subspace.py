#!/usr/bin/env python3
"""Retain the prior positive prefix and certify additional comparison directions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,numpy as np
from certify_dne39_signed_comparison import read,matrix,positive
from certify_dne32_native_remainder import I,mm,tr
from materialize_dne40_joint_sources import run as materialize
from validate_dne34_source_block import mm as rational_mm
PARENT='4cc32239ede79980bceac75226add04e167c659e'
def midpoint(M):return np.array([[float((x.l+x.h)/2) for x in row] for row in M])
def compress(M,B):return mm(tr([[I(x) for x in row] for row in B]),mm(M,[[I(x) for x in row] for row in B]))
def run(parity,output):
 up=parity.upper();sp=f'notes/data/RPB108_DNE40_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64';cp=f'notes/data/RPB108_DNE40_{up}_SIGNED_COMPARISON_20261010.json';vp='notes/data/RPB108_DNE40_SIGNED_SOURCE_VALIDATION_20261010.json';s,sh=read(sp);prior,ph=read(cp);validation,vh=read(vp);assert validation['status']=='PASS';audit=next(r for r in validation['rows'] if r['parity']==parity);assert audit['replay_sha256']==sh and audit['comparison_sha256']==ph
 n=prior['certified_joint_prefix_dimension'];Q=matrix(s['native_block']);G=matrix(s['original_projected_source_Gram']);k=F(289,500);H=[[I(k)*q-g for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)];hm=midpoint(H);j=np.linalg.solve(hm[:n,:n],hm[:n,n:]);schur=hm[n:,n:]-hm[n:,:n]@j;vals,vec=np.linalg.eigh((schur+schur.T)/2);assert all(abs(x)>1e-8 for x in vals)
 J=[[F(round(float(x)*10**40),10**40) for x in row] for row in j];W=[[F(round(float(x)*10**20),10**20) for x in row] for row in vec];R=[[-x for x in row] for row in J]+[[F(i==z) for z in range(36-n)] for i in range(36-n)];pos=[i for i,x in enumerate(vals) if x>0];neg=[i for i,x in enumerate(vals) if x<0]
 def extension(ids):return [[sum(row[t]*W[t][i] for t in range(36-n)) for i in ids] for row in R]
 E=extension(pos);D=extension(neg);B=[[F(i==z) for z in range(n)]+e for i,e in enumerate(E)];BH=compress(H,B);DH=compress(H,D);pc=positive(BH);nc=positive([[-x for x in row] for row in DH]);assert pc and nc;rank=len(B[0]);assert rank+len(D[0])==36
 packet_path=output+'.packet';materialize(s['certificate_path'],packet_path);packet,pkh=read(packet_path);Path(packet_path).unlink();assert pkh==s['normalized_packet_sha256'];cols=packet['columns'];ids=sorted({a for c in cols for a in c['indices']});raw=[dict(zip(c['indices'],map(F,c['coefficients']))) for c in cols];physical=[[sum(raw[t].get(a,F(0))*B[t][i] for t in range(36)) for a in ids] for i in range(rank)];masses=[sum(x*x for x in col) for col in physical];GI=[[(x.l,x.h) for x in row] for row in G];BI=[[(x,x) for x in row] for row in B];BG=rational_mm([list(x) for x in zip(*BI)],rational_mm(GI,BI));trace=sum(BG[i][i][1] for i in range(rank));d=F(pc['coefficient_floor_lower']);schur_floor=d/k;gap=min(schur_floor/(4*(sum(masses)+trace/k**2)),k/2);assert gap>0
 out=dict(stage='DNE41',parent=PARENT,parity=parity,input_paths=[sp,cp,vp],input_sha256=[sh,ph,vh],original_high_floor=str(k),prior_positive_prefix_dimension=n,positive_embedding_B=[list(map(str,row)) for row in B],negative_comparison_embedding_D=[list(map(str,row)) for row in D],positive_comparison_certificate=pc,negative_comparison_certificate=nc,positive_retained_rank=rank,negative_comparison_rank=len(D[0]),uniform_comparison_inertia=[rank,len(D[0]),0],prior_positive_span_contained=True,physical_indices=ids,exact_physical_columns=[list(map(str,row)) for row in physical],exact_physical_masses_squared=list(map(str,masses)),projected_source_trace_upper=str(trace),Schur_coefficient_floor=str(schur_floor),all_high_physical_gap_lower=str(gap),source_integrals_recomputed=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(parity,'positive rank',rank,'negative comparison rank',len(D[0]),'physical gap',float(gap))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('parity',choices=['even','odd']);p.add_argument('--output',required=True);a=p.parse_args();run(a.parity,a.output)
