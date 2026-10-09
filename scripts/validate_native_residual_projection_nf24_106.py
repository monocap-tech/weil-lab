#!/usr/bin/env python3
"""NF24: exact Bessel lower bounds for authenticated compensated sources.
New finite native projections are not a complete residual square/inverse.
"""
import argparse,json,hashlib,gzip,base64
from fractions import Fraction as F
import certify_native_compensated_witness_nf24_106 as c

def validate(targets,source):
    assert source['aperture']==targets['aperture']=='53/50'
    assert source['projection_degrees']==[117,118]
    entries=source['complete_original_signed_source']
    assert len(entries)==116
    rows=[]
    for w in targets['authenticated_compensated_targets']:
        parity=w['parity'];j=118 if parity=='even' else 117
        ids=w['retained_indices']+w['high_indices']
        coeff=w['retained_coefficients']+w['exact_rational_high_compensation']
        q=c.I(0)
        for i,v in zip(ids,coeff):
            record=entries[f'{i},{j}']
            assert set(record)=={'arch','prime','pole','full'}
            lo,hi=map(F,record['full'])
            assert lo<=sum(F(record[k][1]) for k in ['arch','prime','pole'])
            assert hi>=sum(F(record[k][0]) for k in ['arch','prime','pole'])
            q+=F(v)*c.I(lo,hi)
        sq=c.square(q)
        energy=c.I(*map(F,w['compensated_energy']))
        ratio=sq/energy
        lo,hi=(F(284,10000),F(285,10000)) if parity=='even' else (F(298,10000),F(300,10000))
        assert lo<ratio.l<ratio.h<hi
        assert sq.l>0 and ratio.h<F(207,1000)
        rows.append(dict(parity=parity,projection_degree=j,
            original_native_source_pairing=q.asstr(),
            rigorous_residual_source_square_lower=str(sq.l),
            measured_projection_square_over_compensated_energy=ratio.asstr(),
            strict_display_ratio_bounds=[str(lo),str(hi)],
            source_residual_nonzero_certified=True,
            coarse_residual_gate_failure_certified=False))
    return dict(milestone='NF24',status='PASS',aperture='53/50',
        original_native_projection_certificates=rows,
        full_source_residual_square=False,whole_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('targets');p.add_argument('source');p.add_argument('--output');a=p.parse_args()
    raw=open(a.source,'rb').read()
    if a.source.endswith('.b64'):raw=gzip.decompress(base64.b64decode(raw))
    source=json.loads(raw);out=validate(json.load(open(a.targets)),source)
    out['native_projection_source_sha256']=hashlib.sha256(raw).hexdigest()
    s=json.dumps(out,indent=2)+'\n'
    if a.output:open(a.output,'w').write(s)
    else:print(s,end='')
