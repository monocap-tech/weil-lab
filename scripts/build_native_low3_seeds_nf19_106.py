#!/usr/bin/env python3
"""NF19 candidate 3D low-energy rational Legendre seeds at aperture 53/50.
mpmath selects 56x3 vectors; this script is NOT the proof.
The independent Fraction interval certifier proves all final inequalities.
"""
import argparse,gzip,hashlib,json
from fractions import Fraction as F
from decimal import Decimal,localcontext,ROUND_HALF_EVEN
from pathlib import Path
import mpmath as mp
PARENT='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
DEN=10**60

def create(source,path):
    with gzip.open(source,'rb') as f:raw=f.read()
    assert hashlib.sha256(raw).hexdigest()==PARENT
    Q=json.loads(raw)['complete_form'];mp.mp.dps=110
    data={'E112_source_sha256':PARENT,'denominator':str(DEN),'parities':{}}
    for parity in (0,1):
        indices=list(range(parity,112,2))
        M=mp.matrix(56)
        for i,a in enumerate(indices):
            for j,b in enumerate(indices):
                lo,hi=map(F,Q[f'{min(a,b)},{max(a,b)}']['full'])
                M[i,j]=(mp.mpf(lo.numerator)/lo.denominator+
                        mp.mpf(hi.numerator)/hi.denominator)/2
        eig,vec=mp.eigsy(M)
        with localcontext() as ctx:
            ctx.prec=115
            vectors=[[str(int((Decimal(mp.nstr(vec[i,k],100))*DEN).
                         to_integral_value(rounding=ROUND_HALF_EVEN)))
                      for i in range(56)] for k in range(3)]
        data['parities']['even' if parity==0 else 'odd']=dict(
            indices=indices,vectors=vectors,
            eigenvalue_candidate_display=[mp.nstr(eig[k],15) for k in range(3)])
    Path(path).write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(json.dumps(dict(status='candidate rational vectors only',
          sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),
          exact_certification_required=True),indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('original_e112');p.add_argument('--output',required=True)
    a=p.parse_args();create(a.original_e112,a.output)
