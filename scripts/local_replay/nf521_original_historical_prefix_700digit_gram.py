#!/usr/bin/env python3
"""NF521: SHA-pinned original full-carrier 700-decimal raw J prefix Gram.

Reuses NF520's source-original analytic Gram product formulas, but upgrades
pi, sin/cos, exp and integer interval scale to 700 digits. Candidate rank
23, 100, or 140, always the first actual NF505 historical selected nodes.
No untrusted numerical candidate enters this original source Gram oracle.
"""
import argparse,hashlib,json,math,pickle,sys
from pathlib import Path
from fractions import Fraction as F
import nf520_original_raw_gram_exact as m
SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
S=10**700

def configure():
    m.S=S
    m.ONE=(S,S)
    def atan(q,n):
        v=sum(((-1)**i*q**(2*i+1)/F(2*i+1) for i in range(n)),F(0))
        e=q**(2*n+1)/F(2*n+1)
        return (v,v+e) if n%2==0 else (v-e,v)
    a=atan(F(1,5),510);b=atan(F(1,239),510)
    pl=16*a[0]-4*b[1];ph=16*a[1]-4*b[0]
    assert ph-pl<F(1,10**710)
    m.PI=(m.const(pl)[0],m.const(ph)[1])
    def sincos(q):
        y=m.mul(m.const(m.reduce(q)),m.PI)
        assert y[1]-y[0]<=5
        mid=(y[0]+y[1])//2
        x2=mid*mid//S
        sn=st=mid;cs=ct=S
        for k in range(1,241):
            st=-(st*x2//(S*(2*k)*(2*k+1)));sn+=st
            ct=-(ct*x2//(S*(2*k-1)*(2*k)));cs+=ct
        # Exact analytic sine/cosine next remainders:
        assert F(4)**483/math.factorial(483)<F(1,10**790)
        assert F(4)**482/math.factorial(482)<F(1,10**790)
        # Each fixed-point arithmetic truncation <1 unit, recurrent
        # accumulation bounded by <241*100*exp(4)+phase error.
        E=10**10
        return (sn-E,sn+E),(cs-E,cs+E)
    def expint(q):
        q=F(q);assert abs(q)<=F(6,5)
        z=m.const(q);assert z[1]-z[0]<=1
        x=(z[0]+z[1])//2
        t=u=S
        for k in range(1,401):
            t=t*x//(S*k);u+=t
        assert F(3)*F(6,5)**401/math.factorial(401)<F(1,10**830)
        return u-10**10,u+10**10
    m.sincos=sincos
    m.expint=expint

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True)
    p.add_argument('--rank',type=int,choices=(23,100,140,242),required=True)
    p.add_argument('--workdir',required=True)
    a=p.parse_args()
    raw=Path(a.nf505).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA
    j=json.loads(raw)
    assert j['pass']=='NF504-native' and j['original_selected_J_dimension']==242
    assert j['original_original_D_frame_SHA256']==FRAME
    assert j['original_source_basis_nodes'][:23]==[['37/64',k] for k in range(14)]+[['211/128',k] for k in range(9)]
    configure()
    g=m.gram_at(F(11,10),j['original_source_basis_nodes'][:a.rank])
    assert len(g)==a.rank and all(len(row)==i+1 for i,row in enumerate(g))
    maxwidth=max(hi-lo for row in g for lo,hi in row)
    assert F(maxwidth,S)<F(1,10**680)
    root=Path(a.workdir);root.mkdir(parents=True,exist_ok=True)
    target=root/f'G_original_full_I_prefix{a.rank}_700.pkl'
    blob=pickle.dumps(g,protocol=4);target.write_bytes(blob)
    custody={'pass':'NF521-original-source-full-I-prefix-700digit-Gram',
      'original_nf505_source_SHA256':SHA,
      'historical_D_source_SHA256':FRAME,
      'full_original_selected_dimension':242,
      'source_historical_prefix_rank':a.rank,
      'full_carrier_halfwidth':'11/10',
      'source_fixed_interval_denominator':str(S),
      'original_raw_Gram_blob_SHA256':hashlib.sha256(blob).hexdigest(),
      'original_full_I_raw_Gram_max_interval_width':str(F(maxwidth,S)),
      'untrusted_pickle_requires_local_generation':True,
      'remaining_selected_D_columns':242-a.rank,
      'original_complete_physical_beta':'OPEN',
      'original_complete_local_eH':'OPEN',
      'original_NF404_named_support':'OPEN','RH':'OPEN'}
    (root/f'NF521_original_prefix{a.rank}_gram_custody.json').write_text(json.dumps(custody,indent=2)+'\n')
    print('NF521 ORIGINAL SOURCE raw historical prefix Gram',a.rank,'RIGOROUS EXACT PASS')
if __name__=='__main__':main()
