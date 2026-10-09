#!/usr/bin/env python3
"""Expand the fixed native-normalized remainder for the next source Gram."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,base64,gzip,hashlib,json
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def multiply(A,B):return [[sum(x*y for x,y in zip(row,col) if x and y) for col in zip(*B)] for row in A]
def run(cert_path,output):
    cert,ch=read(cert_path);native,nh=read(cert['input_paths'][1]);frame,fh=read(cert['input_paths'][2]);selected,sh=read(native['input_paths'][2])
    assert nh==cert['input_sha256'][1] and fh==cert['input_sha256'][2] and sh==native['input_sha256'][2]
    U=[list(map(F,row)) for row in cert['exact_rational_congruence_U']];W=[list(col) for col in zip(*[list(map(F,row)) for row in native['exact_W_columns']])];K=[list(map(F,row)) for row in frame['frozen_original_projection_K']]
    WU=multiply(W,U);KU=multiply(K,U);ids=native['retained_indices'];T=[{ids[0]:F(1)}]+[dict(zip(c['indices'],map(F,c['coefficients']))) for c in selected['columns']]
    columns=[];scale=10**160
    for j in range(52):
        poly={n:WU[i][j] for i,n in enumerate(ids)}
        for i,t in enumerate(T):
            for n,v in t.items():poly[n]=poly.get(n,F(0))-v*KU[i][j]
        indices=sorted(poly);coeff=[poly[n] for n in indices];mass=sum(v*v for v in coeff);norm=F(isqrt(mass.numerator*scale*scale//mass.denominator)+1,scale);assert norm*norm>mass
        columns.append(dict(indices=indices,coefficients=list(map(str,coeff)),exact_mass_squared=str(mass),norm_upper=str(norm)))
    out=dict(stage='DNE32',parity=cert['parity'],frame='X=hatY*U; original native Q(X)=certified congruence matrix C',input_sha256=[ch,nh,fh,sh],columns=columns,
        next_source_matrix='Gamma_X=U*Gamma_hatY*U; require Gamma_X<=(c/2)*C',complete_remaining_source_Gram_certified=False,whole_aperture_positive=False)
    Path(output).write_text(json.dumps(out,indent=2)+'\n');print(cert['parity'],'52 exact native-normalized source columns materialized')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('output');a=p.parse_args();run(a.certificate,a.output)
