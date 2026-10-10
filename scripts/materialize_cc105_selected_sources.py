#!/usr/bin/env python3
"""Recover exact physical trial and NF52 high columns without original archives."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib,base64,gzip,argparse
BASE=Path(__file__).resolve().parents[1]
def read(root,name):
 b=(root/name).read_bytes();h=hashlib.sha256(b).hexdigest()
 if name.endswith('.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),h
def root(x):
 g=10**100;r=F(isqrt(x.numerator*g*g//x.denominator)+1,g);assert r*r>x;return r
def run(parity,out):
 idx=['even','odd'].index(parity);r=BASE/'notes/cc104-source';s=BASE/'notes/cc105-source'
 original,oh=read(r,'notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json');row=original['parity_frames'][idx]
 P=[dict(zip(col['indices'],map(F,col['coefficients']))) for col in row['unchanged_joined_columns']]
 ids=row['retained_indices'];x,w,u=[[col.get(i,F(0)) for i in ids] for col in P]
 p,q=row['old_two_constraint_pivots'];free=row['old_free_coordinates'];det=x[p]*w[q]-x[q]*w[p];assert det
 T=[[F(0)]*54 for _ in ids]
 for col,j in enumerate(free):
  T[j][col]=1;T[p][col]=(-x[j]*w[q]+x[q]*w[j])/det;T[q][col]=(-x[p]*w[j]+x[j]*w[p])/det
 ell=[sum(a*b for a,b in zip(u,col)) for col in zip(*T)];assert list(map(str,ell))==row['third_constraint_coordinates']
 k=row['third_constraint_pivot_in_old_free_coordinates'];rem=[j for j in range(54) if j!=k]
 T53=[[r[j]-ell[j]/ell[k]*r[k] for j in rem] for r in T]
 assert all(sum(a*b for a,b in zip(v,col))==0 for v in [x,w,u] for col in zip(*T53))
 assert [[T53[free[j]][l] for l in range(53)] for j in rem]==[[F(int(j==l)) for l in range(53)] for j in range(53)]
 retained=P+[dict(zip(ids,col)) for col in zip(*T53)]
 cert,sh=read(BASE,'notes/data/RPB108_CC104_JOINT_RESPONSE_REBASE_20261010.json');z=list(map(F,cert['parity_checks'][idx]['sign']['witness']))
 trial={i:sum(a*col.get(i,F(0)) for a,col in zip(z,retained)) for i in sorted(set().union(*retained))}
 mass=sum(a*a for a in trial.values());norm=root(mass);trial={i:a/norm for i,a in trial.items()}
 name='RPB108_NF46_EVEN_FIXED_NEXT_SHELL_20261009.json' if idx==0 else 'RPB108_NF45_ODD_FIXED_INVERSE_WITNESS_20261009.json'
 d,dh=read(s,'notes/data/'+name);H=[dict(zip(c['indices'],map(F,c['coefficients']))) for c in d['seven_high_columns' if idx==0 else 'six_high_columns']]
 H.append(dict(zip(d['selection_indices'],map(F,d['fixed_rational_eighth_high_coefficients' if idx==0 else 'fixed_rational_seventh_high_coefficients']))))
 hashes=[oh,sh,dh]
 for nf in [50,51,52]:
  d,h=read(s if nf<52 else r,f'notes/data/RPB108_NF{nf}_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');hashes.append(h)
  selection=d['fixed_high_selection'];H.append(dict(zip(selection['selection_indices'],map(F,selection['fixed_rational_high_coefficients']))))
 M=d['enlarged_high_physical_Gram'];assert len(H)==11-idx
 for i,a in enumerate(H):
  assert min(a)>=112
  for j,b in enumerate(H):
   val=sum(c*b.get(k,F(0)) for k,c in a.items());lo,hi=map(F,M[i][j]);assert lo<=val<=hi
 cols=[]
 for col in [trial]+H:
  ids2=sorted(col);m=sum(a*a for a in col.values());cols.append(dict(indices=ids2,coefficients=[str(col[i]) for i in ids2],exact_mass_squared=str(m),norm_upper=str(root(m))))
 packet=dict(milestone='CC105',parity=parity,columns=cols,column_labels=['normalized_CC104_trial']+[f'NF52_H{i}' for i in range(len(H))],
  input_sha256=hashes,source_trial_coefficients=list(map(str,z)),source_trial_physical_mass_squared=str(mass),source_trial_normalizing_upper=str(norm),
  exact_retained_constraint_frame_verified=True,exact_high_physical_Gram_verified=True,native_matrix=[[None]*len(cols) for _ in cols])
 Path(out).write_text(json.dumps(packet,indent=2)+'\n');print(parity,'physical packet',len(cols),'max degree',max(max(c['indices']) for c in cols))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('parity');a.add_argument('--output',required=True);v=a.parse_args();run(v.parity,v.output)
