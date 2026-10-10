#!/usr/bin/env python3
"""Use the improved original floor while preserving every DNE44 positive column."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,gzip,base64,numpy as np
from certify_dne39_signed_comparison import read,matrix,positive
from certify_dne32_native_remainder import I
from certify_dne44_positive_subspace import midpoint,compress
from materialize_dne44_joint_sources import run as materialize
from validate_dne34_source_block import mm as rational_mm
PARENT='a9eda40b874163be980da517d3dda87942f83533'
def run(parity,output):
 up=parity.upper();paths=[f'notes/data/RPB108_DNE44_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64',f'notes/data/RPB108_DNE44_{up}_POSITIVE_SUBSPACE_20261010.json.gz.b64','notes/data/RPB108_DNE46_HIGH_FLOOR_VALIDATION_20261010.json','notes/data/RPB108_DNE44_POSITIVE_SUBSPACE_VALIDATION_20261010.json'];inp=[read(p) for p in paths];s,prior,high,audit=[x for x,_ in inp];assert high['status']==audit['status']=='PASS';ar=next(r for r in audit['rows'] if r['parity']==parity);assert ar['certificate_sha256']==inp[1][1] and ar['input_sha256'][0]==inp[0][1]
 k=F(high['original_infinite_F112_floor']);assert k==F(647,1000);Q=matrix(s['native_block']);G=matrix(s['original_projected_source_Gram']);H=[[I(k)*q-g for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)];PB=[list(map(F,row)) for row in prior['positive_embedding_B']];PD=[list(map(F,row)) for row in prior['negative_comparison_embedding_D']];C=[a+b for a,b in zip(PB,PD)];n=prior['positive_retained_rank'];rest=44-n;HC=compress(H,C);hm=midpoint(HC);j=np.linalg.solve(hm[:n,:n],hm[:n,n:]);schur=hm[n:,n:]-hm[n:,:n]@j;vals,vec=np.linalg.eigh((schur+schur.T)/2)
 J=[[F(round(float(x)*10**40),10**40) for x in row] for row in j];W=[[F(round(float(x)*10**20),10**20) for x in row] for row in vec];R=[[-x for x in row] for row in J]+[[F(i==z) for z in range(rest)] for i in range(rest)];pos=[i for i,x in enumerate(vals) if x>0];neg=[i for i,x in enumerate(vals) if x<0];assert len(pos)==1 and len(neg)==int(parity=='even')
 def ext(ids):return [[sum(row[t]*W[t][i] for t in range(rest)) for i in ids] for row in R]
 E=ext(pos);DC=ext(neg);BC=[[F(i==z) for z in range(n)]+e for i,e in enumerate(E)]
 def transform(B):return [[sum(C[i][t]*B[t][z] for t in range(44)) for z in range(len(B[0]))] for i in range(44)]
 B=transform(BC);D=transform(DC);pc=positive(compress(H,B));nc=positive([[-x for x in row] for row in compress(H,D)]) if neg else None;assert pc and (nc or not neg);rank=len(B[0]);assert all(row[:n]==old for row,old in zip(B,PB))
 pp=output+'.packet';materialize(s['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();assert ph==s['normalized_packet_sha256'];raw=[dict(zip(x['indices'],map(F,x['coefficients']))) for x in packet['columns']];ids=sorted({i for row in raw for i in row});physical=[[sum(raw[t].get(i,F(0))*B[t][z] for t in range(44)) for i in ids] for z in range(rank)];masses=[sum(x*x for x in col) for col in physical]
 GI=[[(x.l,x.h) for x in row] for row in G];BI=[[(x,x) for x in row] for row in B];BG=rational_mm([list(x) for x in zip(*BI)],rational_mm(GI,BI));trace=sum(BG[i][i][1] for i in range(rank));sf=F(pc['coefficient_floor_lower'])/k;gap=min(sf/(4*(sum(masses)+trace/k**2)),k/2);assert gap>0
 out=dict(stage='DNE46',parent=PARENT,parity=parity,input_paths=paths,input_sha256=[h for _,h in inp],original_high_floor=str(k),joint_native_positive_control=prior['joint_native_positive_control'],prior_positive_prefix_dimension=n,positive_embedding_B=[list(map(str,row)) for row in B],negative_comparison_embedding_D=[list(map(str,row)) for row in D],positive_comparison_certificate=pc,negative_comparison_certificate=nc,positive_retained_rank=rank,negative_comparison_rank=len(D[0]),uniform_comparison_inertia=[rank,len(D[0]),0],prior_positive_span_contained=True,physical_indices=ids,exact_physical_columns=[list(map(str,row)) for row in physical],exact_physical_masses_squared=list(map(str,masses)),projected_source_trace_upper=str(trace),Schur_coefficient_floor=str(sf),all_high_physical_gap_lower=str(gap),new_source_integrals_computed=False,prior_source_Gram_entries_reintegrated=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 payload=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(payload,mtime=0))+b'\n');print(parity,'positive rank',rank,'negative rank',len(D[0]),'gap',float(gap),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('parity',choices=['even','odd']);ap.add_argument('--output',required=True);a=ap.parse_args();run(a.parity,a.output)
