#!/usr/bin/env python3
"""Reassemble literal H and V from original source terms and moment receipts.
Exact integer/rational arithmetic. External evidence, not a Lean certificate.
"""
import argparse, gzip, json, re
from fractions import Fraction as F
from pathlib import Path
from verify_nf620_physical_key_tables import Q, N, M, exact, add, neg, canonical, inventory, table, ceildiv

ZERO=(0,0)
def scale(a,c):
    c=F(c)
    m,r=divmod(a[0]*c.numerator,c.denominator)
    return m,ceildiv(a[1]*abs(c.numerator),c.denominator)+int(r!=0)

def zadd(a,b): return add(a[0],b[0]),add(a[1],b[1])
def zscale(a,c,d):
    return add(scale(a[0],c),neg(scale(a[1],d))),add(scale(a[0],d),scale(a[1],c))

def osc(f,n,w=F(1)):
    return [(F(0),s*f,n,w/2 if n%2 else F(0),F(0) if n%2 else -s*w/2) for s in (1,-1)]
def pole(w=F(1)):
    return [(F(s,2),F(0),0,s*w/2,F(0)) for s in (1,-1)]

def selected(root):
    src=root/'WeilDefect/Arithmetic'
    sig=(src/'ActualZetaOriginalJ242ExponentialSignature.lean').read_text()
    groups=[(F(f),int(m)) for f,m in re.findall(r'\(\((\d+(?:/\d+)?)\s*:\s*ℚ\),\s*(\d+)\)',sig)]
    assert len(groups)==67 and sum(m for _,m in groups)==241
    return [osc(f,n) for f,m in groups for n in range(m)]+[pole()]

def critical(root):
    src=(root/'WeilDefect/Arithmetic/ActualZetaOriginalNF407FrozenData.lean').read_text()
    def nums(s): return [F(v) for v in re.findall(r'\((-?\d+(?:/\d+)?)\)',s)]
    freq=nums(src.split('def neutralNF587CriticalFrequencies',1)[1].split(']',1)[0])
    sine=src.split('def neutralNF587CriticalSines',1)[1].split('def neutralNF587CriticalPoles',1)[0]
    weights=[nums(s) for s in re.findall(r'#\[([^\[\]]+)\]',sine)]
    poles=nums(src.split('def neutralNF587CriticalPoles',1)[1].split(']',1)[0])
    assert len(freq)==32 and len(weights)==len(poles)==4 and all(len(w)==32 for w in weights)
    return [sum((osc(f,0,w) for f,w in zip(freq,ws)),[])+pole(p) for ws,p in zip(weights,poles)]

def read_shards(root,paths):
    schedule=inventory(root)
    expected={k:n+1 for k,n in schedule.items() if k!=(0,0)}
    data={}
    for path in sorted(paths.rglob('nf621-shard*.json.gz')):
        with gzip.open(path,'rt') as fh: d=json.load(fh)
        assert d['scale']=='10^2600' and d['exp_terms']==N and d['atan_terms']==M
        for t in d['tables']:
            k=F(t['h']),F(t['f'])
            assert k in expected and k not in data and len(t['rows'])==expected[k]
            data[k]=[tuple(map(int,r)) for r in t['rows']]
            assert all(len(r)==3 and r[2]>=0 for r in data[k])
    assert {k:len(r) for k,r in data.items()}==expected
    return data

def moment(data,h,f,n,pilot=False):
    if h==f==0:
        return exact((F(11,10)**(n+1)-F(-11,10)**(n+1))/(n+1)),ZERO
    k=canonical(h,f)
    if pilot and (k not in data or len(data[k])<=n):
        data[k]=table(*k,n)
    x,y,r=data[k][n]
    s=(-1)**n if k!=(h,f) else 1
    return (s*x,r),(s*y,r)

def entry(data,a,b,pilot=False):
    out=ZERO,ZERO
    for h,f,n,c,d in a:
        for j,g,m,e,v in b:
            z=moment(data,h+j,f+g,n+m,pilot)
            out=zadd(out,zscale(z,c*e-d*v,c*v+d*e))
    assert abs(out[1][0])<=out[1][1], 'imaginary enclosure missed zero'
    return out[0]

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--shards',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--pilot',action='store_true')
    a=p.parse_args()
    S=selected(a.root)
    if a.pilot:
        data={}
        for i,j in ((0,0),(1,0),(241,0),(241,241)):
            m,r=entry(data,S[i],S[j],True)
            print(f'H[{i},{j}] prefix={F(m,Q).__float__():.16g} (display only); radius < 10^{len(str(r))-2600}')
            if (i,j)==(241,241):
                c=F(2356474701241767793847805235787,10**31); R=F(1,10**30)
                assert abs(F(m,Q)-c)+F(r,Q)<=R
            if (i,j)==(0,0):
                c=F(96365058853459560322855497082803181,10**35)
                assert abs(F(m,Q)-c)+F(r,Q)<=F(5,10**34)
            if (i,j)==(241,0):
                c=F(14043467082935807939230485585476647,10**35)
                assert abs(F(m,Q)-c)+F(r,Q)<=F(1,10**33)
        print('NF622 four complete H entry pilots PASS')
        return
    assert a.shards and a.output
    data=read_shards(a.root,a.shards)
    C=critical(a.root)
    maxH=maxV=0
    with gzip.open(a.output,'wt') as fh:
        def emit(x): fh.write(json.dumps(x,separators=(',',':'))+'\n')
        emit({'schema':'NF622-original-physical-entry-balls-v1','scale':'10^2600','evidence':'external moment reassembly; not formal custody'})
        for i in range(242):
            H=[entry(data,S[i],S[j]) for j in range(i+1)]
            V=[entry(data,S[i],c) for c in C]
            maxH=max(maxH,max(r for _,r in H)); maxV=max(maxV,max(r for _,r in V))
            emit({'row':i,'H_lower':[[str(m),str(r)] for m,r in H],'V':[[str(m),str(r)] for m,r in V]})
            if i%20==0: print('assembled row',i,flush=True)
    print('assembled 29403 lower triangular H entries and 968 V entries')
    print('max radius H < 10^',len(str(maxH))-2600,'V < 10^',len(str(maxV))-2600,sep='')
if __name__=='__main__': main()
