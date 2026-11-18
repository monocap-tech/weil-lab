#!/usr/bin/env python3
"""Exact uniform-radius payments for original physical H,V enclosure receipts.
External arithmetic only: no assertion of Lean analytic receipt custody.
"""
import argparse
import gzip
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
Q = 10**2600
N = 242
FROZEN_SHA = '0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
TNUM = [-2271087, -1621433, 1115405, 1048576]


def dyad(p):
    a,e = map(int,p)
    return F(a)*F(2)**e


def common_dyads(xs):
    """Return exact integer coordinates on a shared positive binary scale."""
    d=max(x.denominator for x in xs)
    assert d & (d-1) == 0
    assert all(d % x.denominator == 0 for x in xs)
    return [int(x*d) for x in xs],d


def transpose(a):
    return list(map(list,zip(*a)))


def products(D,H,V,w,y,mm):
    """Integer products only, no rounding in any center."""
    dt=transpose(D)
    A=mm(mm(dt,H),D)
    b=mm(mm(dt,V),[[x] for x in w])
    Ay=mm(A,[[x] for x in y])
    Dy=mm(D,[[x] for x in y])
    return A,[r[0] for r in b],[r[0] for r in Ay],[r[0] for r in Dy]


def cached_products(D,H,V,w,y,mm):
    """NF626 association: retain independently checkable integer dot proposals."""
    dt=transpose(D)
    HD=mm(H,D)
    A=mm(dt,HD)
    Vw=mm(V,[[x] for x in w])
    b=mm(dt,Vw)
    Ay=mm(A,[[x] for x in y])
    Dy=mm(D,[[x] for x in y])
    return dict(HD=HD,A=A,Vw=[r[0] for r in Vw],b=[r[0] for r in b],
                Ay=[r[0] for r in Ay],Dy=[r[0] for r in Dy])


def exact_gates(D,S,H,V,w,T,y,U,eH,eV,mid,rad,mm,scale=Q,cache=None):
    n=len(D)
    if cache is None:
        A,b,Ay,Dy=products(D,H,V,w,y,mm)
    else:
        A,b,Ay,Dy=(cache[k] for k in ('A','b','Ay','Dy'))
    aden=scale*S*S; bden=scale*S*T
    col=[sum(map(abs,row)) for row in transpose(D)]
    row=[sum(map(abs,r)) for r in D]
    C=sum(col); W=sum(map(abs,w)); Y=sum(abs(v)*c for v,c in zip(y,col))
    defect=[]; residual=[]
    for i in range(n):
        d=F(sum(abs(int(i==j)*aden-A[i][j]) for j in range(n)),aden)
        defect.append(d+eH*F(col[i]*C,S*S))
        rc=abs(F(b[i],bden)-F(Ay[i],aden*U))
        residual.append(rc+eV*F(col[i]*W,S*T)+eH*F(col[i]*Y,S*S*U))
    r=max(residual)
    pay=[abs(F(Dy[i],S*U)-mid[i])+2*r*F(row[i],S) for i in range(n)]
    return defect,residual,r,pay


def read_jsonl(path):
    with gzip.open(path,'rt') as f:
        return [json.loads(line) for line in f]


def to_fixed(mr):
    m,r=map(dyad,mr)
    assert r>=0
    z=m*Q; a=z.numerator//z.denominator
    v=r*Q+abs(z-a)
    return a,-(-v.numerator//v.denominator)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--historical',type=Path,required=True,help='NF613 entry receipt with exact historical D and untrusted y0')
    p.add_argument('--entries',type=Path,help='NF622 moment-derived entry receipt; omit for Arb baseline')
    p.add_argument('--center-cache',type=Path,help='emit NF626 untrusted common-scale integer product proposals')
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    from flint import fmpz_mat
    from verify_nf380_original_archived_signed_dual import FRAME_SHA
    def mm(x,y):
        z=fmpz_mat(x)*fmpz_mat(y)
        return [[int(z[i,j]) for j in range(z.ncols())] for i in range(z.nrows())]
    frozen_bytes=(a.root/'notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json').read_bytes()
    assert hashlib.sha256(frozen_bytes).hexdigest()==FROZEN_SHA
    frozen=json.loads(frozen_bytes)
    historic=read_jsonl(a.historical); head,*rows=historic
    assert head['schema']=='NF613-original-physical-entry-balls-v1'
    assert head['frame_sha256']==FRAME_SHA and head['frozen_sha256']==FROZEN_SHA
    assert len(rows)==N and [r['row'] for r in rows]==list(range(N))
    dig=hashlib.sha256()
    for r in rows:
        assert len(r['D'])==N
        for d in r['D']:
            dig.update((json.dumps(d,separators=(',',':'))+'\n').encode())
    assert dig.hexdigest()==FRAME_SHA
    Dflat,S=common_dyads([dyad(d) for r in rows for d in r['D']])
    D=[Dflat[i*N:(i+1)*N] for i in range(N)]
    y,U=common_dyads([dyad(v) for v in head['y0']]); assert len(y)==N
    crit=frozen['original_exact_native_original_four_critical_coefficients_mid_radius']
    assert len(crit)==4 and all(dyad(r)==0 for _,r in crit)
    w,T=common_dyads([F(t,2**20)-dyad(m) for t,(m,_) in zip(TNUM,crit)])
    frozen_sel=frozen['original_exact_native_raw_selected_coefficients_mid_radius']
    mid,rad=zip(*[tuple(map(dyad,r)) for r in frozen_sel]); assert len(mid)==N and all(x>=0 for x in rad)
    if a.entries:
        eh,*er=read_jsonl(a.entries)
        assert eh['schema']=='NF622-original-physical-entry-balls-v1' and eh['scale']=='10^2600'
        convert=lambda a:tuple(map(int,a))
        evidence='NF622 moment-derived external entry enclosures'
    else:
        er=rows; convert=to_fixed
        evidence='NF613 Arb entry enclosures converted outward to fixed-point'
    assert len(er)==N and [r['row'] for r in er]==list(range(N))
    H=[[0]*N for _ in range(N)]; V=[]; EH=EV=0
    for i,r in enumerate(er):
        assert len(r['H_lower'])==i+1 and len(r['V'])==4
        for j,pair in enumerate(r['H_lower']):
            m,e=convert(pair); assert e>=0
            H[i][j]=H[j][i]=m; EH=max(EH,e)
        v=[convert(p) for p in r['V']]; assert all(e>=0 for _,e in v)
        V.append([m for m,_ in v]); EV=max(EV,max(e for _,e in v))
    cache=cached_products(D,H,V,w,y,mm) if a.center_cache else None
    defect,residual,r,pay=exact_gates(D,S,H,V,w,T,y,U,F(EH,Q),F(EV,Q),mid,rad,mm,cache=cache)
    row_ok=all(d<=F(1,100) for d in defect)
    payments=[p<=v for p,v in zip(pay,rad)]
    # Ratios for diagnostics only. Preserve exact numerators/denominators.
    def rat(z): return [str(z.numerator),str(z.denominator)]
    receipt={'schema':'NF623-uniform-physical-payments-v1','evidence':evidence,
      'frame_sha256':FRAME_SHA,'frozen_sha256':FROZEN_SHA,
      'entry_sha256':hashlib.sha256((a.entries or a.historical).read_bytes()).hexdigest(),
      'uniform_H_radius':rat(F(EH,Q)),'uniform_V_radius':rat(F(EV,Q)),
      'r':rat(r),'row_defect_max':rat(max(defect)), 'row_defect_pass':row_ok,
      'rows':[{'i':i,'defect_upper':rat(defect[i]),'residual_upper':rat(residual[i]),
               'selected_payment':rat(pay[i]),'selected_radius':rat(rad[i]),'pass':payments[i]} for i in range(N)],
      'selected_payments_pass':sum(payments),'all_pass':row_ok and all(payments),
      'scope':'exact finite arithmetic conditional on input analytic enclosure validity; NOT Lean custody'}
    a.output.write_text(json.dumps(receipt,separators=(',',':'))+'\n')
    print('row defect PASS:',row_ok,'selected payments:',sum(payments),'/',N,flush=True)
    assert row_ok and all(payments), 'uniform error route did not pay every historical gate'
    if cache is not None:
        with gzip.open(a.center_cache,'wt',compresslevel=3) as f:
            def emit(obj): f.write(json.dumps(obj,separators=(',',':'))+'\n')
            emit({'schema':'NF626-integer-center-cache-v1','scales':{k:str(v) for k,v in [('S',S),('Q',Q),('T',T),('U',U)]},
                  'entry_sha256':receipt['entry_sha256'],'historical_sha256':hashlib.sha256(a.historical.read_bytes()).hexdigest(),
                  'frame_sha256':FRAME_SHA,'frozen_sha256':FROZEN_SHA,'eH':rat(F(EH,Q)),'eV':rat(F(EV,Q)), 'r':rat(r),
                  'w':list(map(str,w)),'y':list(map(str,y)), 'scope':'untrusted exact integer dot proposals; verify separately'})
            for i in range(N):
                emit({'i':i,'HD':list(map(str,cache['HD'][i])),'A':list(map(str,cache['A'][i])),
                      **{k:str(cache[k][i]) for k in ('Vw','b','Ay','Dy')}})
        print('NF626 integer center cache emitted (untrusted proposals)',flush=True)


if __name__=='__main__': main()
