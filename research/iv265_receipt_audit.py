#!/usr/bin/env python3
"""Receipt-only exact IV256 audit; does NOT regenerate factor or check residual bytes."""
import json, pathlib
from fractions import Fraction as F
root=pathlib.Path(__file__).resolve().parent
for parity in (0,1):
    r=json.loads((root/f'iv256_parity_{parity}.json').read_text())
    assert r['certified'] and r['parity']==parity and r['dimension']==14080
    S=int(r['scale']); n=r['dimension']; R=int(r['max_residual_row_scaled'])
    s=F(1,100)-F(R,S)-n*F(r['entry_error'])
    assert s==F(r['schur_surplus_lower'])
    a=s+F(1,1000)
    assert a>F(1,125)
    assert int(r['mean_upper_scaled'])<4*(1<<80)
    assert int(r['oscillation_upper_scaled'])<600*(1<<80)
    end=0
    for i,b in enumerate(r['residual_blocks']):
        assert b['block']==i and b['first']==end
        assert b['last_exclusive']>end
        assert b['factor_sha256']==r['factor_sha256']
        assert b['target_sha256']==r['target_sha256']
        end=b['last_exclusive']
    assert end==n and len(r['residual_blocks'])==7
    if parity==1:
        assert a>F(41,5000) and 1/a<F(5000,41)<122
    print(json.dumps(dict(parity=parity,surplus=str(s),surplus_plus_eta=str(a),
        inverse_upper=str(1/a),blocks=7,mean_lt4=True,oscillation_lt600=True,
        odd_refinement=parity==1,classification='receipt arithmetic and metadata only')))
