#!/usr/bin/env python3
"""NF18: reproducibly generate exact rational near-critical E112 witnesses.
mpmath selects a candidate direction, but ALL proof comparisons are
subsequently carried out using its exact rational coefficients and
complete original signed interval matrices, not eigenvalue floats.
"""
import gzip,json,hashlib,argparse
from fractions import Fraction as F
from decimal import Decimal,localcontext,ROUND_HALF_EVEN
import mpmath as mp

SOURCE_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'

def main(src,out):
    with gzip.open(src,'rb') as h: raw=h.read()
    assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA
    intervals=json.loads(raw)['complete_form']
    D=10**55
    res=dict(aperture='53/50',basis='physical normalized Legendre',
             coefficient_denominator=str(D),parent_source=SOURCE_SHA,
             witnesses={})
    mp.mp.dps=115
    for parity in ('even','odd'):
        ids=list(range(0 if parity=='even' else 1,112,2))
        n=len(ids);M=mp.matrix(n)
        for i,x in enumerate(ids):
            for j,y in enumerate(ids):
                lo,hi=intervals[f'{min(x,y)},{max(x,y)}']['full']
                a,b=F(lo),F(hi)
                M[i,j]=(mp.mpf(a.numerator)/a.denominator+
                        mp.mpf(b.numerator)/b.denominator)/2
        vals,vecs=mp.eigsy(M)
        with localcontext() as ctx:
            ctx.prec=110
            coeff=[str(int((Decimal(mp.nstr(vecs[j,0],75))*D).to_integral_value(
                    rounding=ROUND_HALF_EVEN))) for j in range(n)]
        res['witnesses'][parity]={'indices':ids,'numerators':coeff}
    with open(out,'w') as f:f.write(json.dumps(res,sort_keys=True,indent=2)+'\n')
    print('NF18 rational witness SHA256:',hashlib.sha256(
           open(out,'rb').read()).hexdigest())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('old_e112')
    p.add_argument('--output',required=True)
    a=p.parse_args();main(a.old_e112,a.output)
