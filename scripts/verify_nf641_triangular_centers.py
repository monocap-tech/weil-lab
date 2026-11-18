#!/usr/bin/env python3
"""Deterministic triangular center-product replay, from immutable widened data.

The retained cache is untrusted. Recompute HD exactly, then verify the
lower triangle of D^T HD and exact symmetry. No probabilistic test.
External replay is not Lean kernel custody.
"""
import argparse
import gzip
import json
from pathlib import Path
from emit_nf630_original_literal_payments import historical, payment_receipt, sha, rat
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA,read_jsonl

def main():
    p=argparse.ArgumentParser()
    for k in ('root','historical','entries','payments','cache','output'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    from flint import fmpz_mat
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    eh,dh=sha(a.entries),sha(a.historical)
    pay=payment_receipt(a.payments,eh,frame)
    H=[[0]*N for _ in range(N)]; V=[]
    hh,*er=read_jsonl(a.entries)
    assert hh['schema']=='NF622-original-physical-entry-balls-v1' and hh['scale']=='10^2600'
    assert len(er)==N
    EH=EV=0
    for i,row in enumerate(er):
        assert row['row']==i and len(row['H_lower'])==i+1 and len(row['V'])==4
        for j,(x,e) in enumerate(row['H_lower']):
            assert int(e)>=0
            H[i][j]=H[j][i]=int(x); EH=max(EH,int(e))
        V.append([int(x) for x,e in row['V']])
        for x,e in row['V']:
            assert int(e)>=0
            EV=max(EV,int(e))
    from fractions import Fraction as F
    assert rat(pay['uniform_H_radius'])==F(EH,Q) and rat(pay['uniform_V_radius'])==F(EV,Q)
    ch,*cr=read_jsonl(a.cache)
    assert ch['schema']=='NF626-integer-center-cache-v1'
    assert ch['entry_sha256']==eh and ch['historical_sha256']==dh
    assert ch['frame_sha256']==frame and ch['frozen_sha256']==FROZEN_SHA
    assert {k:int(v) for k,v in ch['scales'].items()}==dict(S=S,Q=Q,U=U,T=T)
    assert list(map(int,ch['y']))==y and list(map(int,ch['w']))==w
    assert [rat(ch[k]) for k in ('eH','eV','r')]==[rat(pay[k]) for k in ('uniform_H_radius','uniform_V_radius','r')]
    assert len(cr)==N and [r['i'] for r in cr]==list(range(N))
    HD=[list(map(int,row['HD'])) for row in cr]
    A=[list(map(int,row['A'])) for row in cr]
    assert all(len(row)==N for row in HD+A)
    Hm,Dm,HDm=fmpz_mat(H),fmpz_mat(D),fmpz_mat(HD)
    assert Hm*Dm==HDm
    print('NF641 all 58564 HD coordinates exactly verified',flush=True)
    # Verify lower triangular A using exact rectangular row-block products.
    # Off-diagonal upper values follow only from exact H symmetry and
    # the verified HD product. An explicit symmetry check binds A.
    dt=Dm.transpose()
    block=16
    checked=0; symmetry=0; evaluated=0
    for start in range(0,N,block):
        end=min(start+block,N)
        left=fmpz_mat([[int(dt[i,k]) for k in range(N)] for i in range(start,end)])
        right=fmpz_mat([[HD[k][j] for j in range(end)] for k in range(N)])
        prod=left*right
        evaluated+=(end-start)*end
        for i in range(start,end):
            for j in range(i+1):
                assert int(prod[i-start,j])==A[i][j]
                checked+=1
            for j in range(i+1,N):
                assert A[i][j]==A[j][i]
                symmetry+=1
    assert checked==N*(N+1)//2 and symmetry==N*(N-1)//2
    dot=lambda x,y:sum(a*b for a,b in zip(x,y))
    vw=[int(row['Vw']) for row in cr]
    for i,row in enumerate(cr):
        assert vw[i]==dot(V[i],w)
        assert int(row['b'])==dot([v[i] for v in D],vw)
        assert int(row['Ay'])==dot(A[i],y)
        assert int(row['Dy'])==dot(D[i],y)
    m={'schema':'NF641-triangular-center-replay-v1','historical_sha256':dh,'entry_sha256':eh,
       'payment_sha256':sha(a.payments),'cache_sha256':sha(a.cache),'frame_sha256':frame,
       'HD_exact':N*N,'A_lower_exact':checked,'A_upper_symmetry':symmetry,
       'vector_exact':4*N,'A_block_coordinates_evaluated':evaluated,
       'scope':'external exact arithmetic; not literal Lean matrix truth'}
    a.output.write_text(json.dumps(m,indent=2)+'\n')
    print('NF641 deterministic replay PASS:',m,flush=True)
if __name__=='__main__': main()
