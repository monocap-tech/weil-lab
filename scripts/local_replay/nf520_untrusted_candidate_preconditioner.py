#!/usr/bin/env python3
"""NF520 UNTRUSTED numerical trial preconditioner for exact source Gram gaps.

mpmath is used ONLY to choose a rational 242x242 triangular matrix T.
No numerical eigenvalue, Cholesky, or rounding is a proof. A separate
integer verifier accepts/rejects any submitted T using exact source boxes.
"""
import argparse,hashlib,json,pickle,time
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
from nf520_original_raw_gram_exact import S
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--workdir',required=True)
    p.add_argument('--case',choices=('H4094','H4095','union'),required=True)
    a=p.parse_args();root=Path(a.workdir)
    custody=json.loads((root/'nf520_original_gram_custody.json').read_text())
    assert custody['pass']=='NF520-original-source-exact-physical-gram-oracle'
    G=[]
    for i in range(3):
        raw=(root/f'G{i}_oracle.pkl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==custody['Gram'][str(i)]['original_source_interval_file_sha256']
        G.append(pickle.loads(raw))
    t=time.time();mp.mp.dps=300;n=242
    cases={
        'union':[(F(1),2),(-F(1,20000),0)],
        'H4095':[(F(1),1),(-F(1,1000),0)],
        'H4094':[(F(3,5),0),(-F(1),1),(F(1),2)]
    }
    A=mp.matrix(n)
    for i in range(n):
        for j in range(i+1):
            z=mp.mpf(0)
            for c,k in cases[a.case]:
                lo,hi=G[k][i][j]
                z+=(mp.mpf(c.numerator)/c.denominator)*mp.mpf(lo+hi)/(2*S)
            A[i,j]=A[j,i]=z
    L=mp.cholesky(A) # untrusted: used only to select a preconditioner
    T=mp.matrix(n)
    for k in reversed(range(n)):
        for i in reversed(range(k+1)):
            T[i,k]=(mp.mpf(int(i==k))-
                sum((L[j,i]*T[j,k] for j in range(i+1,n)),mp.mpf(0)))/L[i,i]
    Q=10**200
    entries=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if j<i:row.append(0);continue
            sign,mant,exp,bits=T[i,j]._mpf_
            z=mant*Q
            z=(z<<exp) if exp>=0 else (z>>(-exp))
            row.append(-z if sign else z)
        entries.append(row)
    (root/f'T_{a.case}_candidate.pkl').write_bytes(pickle.dumps(entries,protocol=4))
    print('NF520 untrusted numerical candidate ONLY',a.case,
          round(time.time()-t,1),'seconds; exact source verification REQUIRED')
if __name__=='__main__':main()
