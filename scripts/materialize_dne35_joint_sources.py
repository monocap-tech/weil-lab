#!/usr/bin/env python3
"""Exact scaled tested columns plus eight frozen native-normalized remainders."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
from materialize_dne32_normalized_sources import run as remainder
from certify_dne32_native_remainder import I,mm
from certify_dne34_source_block import root

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def run(cert_path,output):
 temp=output+'.remainder';remainder(cert_path,temp);packet,ph=read(temp);Path(temp).unlink();cert,ch=read(cert_path);native,nh=read(cert['input_paths'][1]);frame,fh=read(cert['input_paths'][2]);selected,sh=read(native['input_paths'][2]);assert [nh,fh]==cert['input_sha256'][1:3] and sh==native['input_sha256'][2]
 ids=native['retained_indices'];T=[dict(indices=[ids[0]],coefficients=['1'])]+selected['columns'];scales=list(map(F,frame['column_scales']));columns=[]
 for i,(t,s) in enumerate(zip(T,scales)):
  cc=[F(v)*s for v in t['coefficients']];mass=sum(v*v for v in cc);columns.append(dict(indices=t['indices'],coefficients=list(map(str,cc)),exact_mass_squared=str(mass),norm_upper=str(root(mass))))
 columns+=packet['columns'][:8]
 A=[[I(*v) for v in row] for row in cert['tightened_scaled_T4_native_matrix']];P=[[I(*v) for v in row] for row in cert['tightened_scaled_T4_W52_border']];J=[list(map(F,row)) for row in frame['frozen_scaled_projection_J']];E=[[p-v for p,v in zip(row,correction)] for row,correction in zip(P,mm(A,J))];U=[list(map(F,row[:8])) for row in cert['exact_rational_congruence_U']];cross=mm(E,U);C=[[I(*cert['congruence_matrix'][i][j]) for j in range(8)] for i in range(8)]
 Q=[[I(0) for _ in range(12)] for _ in range(12)]
 for i in range(4):
  for j in range(4):Q[i][j]=A[i][j]
  for j in range(8):Q[i][4+j]=Q[4+j][i]=cross[i][j]
 for i in range(8):
  for j in range(8):Q[4+i][4+j]=C[i][j]
 out=dict(stage='DNE35',parity=cert['parity'],frame='T4*S union X[0:8]; X=hatY*U unchanged',columns=columns,column_labels=[f'TS{i}' for i in range(4)]+[f'X{i}' for i in range(8)],input_sha256=[ch,nh,fh,sh,ph],native_matrix=[[v.box() for v in row] for row in Q],native_mixed_formula='(P_s-A_s*J)*U[0:8]',whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(cert['parity'],'12 exact joint columns materialized')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('output');a=p.parse_args();run(a.certificate,a.output)
