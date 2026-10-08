#!/usr/bin/env python3
"""NF12: validate full original native low4 interval manifest, no whole sign.
Usage: python scripts/validate_native_low4_nf12_106.py
"""
from pathlib import Path
from fractions import Fraction as F
import json
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"notes/data/RPB108_NF12_FULL_NATIVE_LOW4_106_CERTIFICATE_20261008.json").read_text())
D=data["intervals"];G=F(data["interval_grid_denominator"])
def p(key,kind="full"):
    lo,hi=map(F,D[key][kind]);assert lo<=hi
    return lo/G,hi/G
def det(a,b):
    x,y,z=p(f"{a},{a}"),p(f"{b},{b}"),p(f"{a},{b}")
    assert x[0]>0 and y[0]>0
    lower=x[0]*y[0]-max(z[0]**2,z[1]**2)
    assert lower>0
    return lower,lower/(x[1]+y[1])
checks=0
for key in ("0,0","0,2","1,1","1,3","2,2","3,3"):
    whole=p(key)
    parts=[p(key,kind) for kind in ("arch","poles","prime")]
    assert whole[0]<=sum(q[1] for q in parts);checks+=1
    assert whole[1]>=sum(q[0] for q in parts);checks+=1
    assert whole[0]<=whole[1];checks+=1
# Independently reconstruct every analytic part from the published Fraction producer.
from certify_native_low4_nf12_106 import construct
rebuilt,_,_=construct()
for key in D:
    for part in ("arch","poles","prime","full"):
        lo,hi=map(F,rebuilt[key][part]);publo,pubhi=p(key,part)
        assert publo<=lo<=hi<=pubhi
        checks+=1
even=det(0,2);odd=det(1,3);checks+=4
assert even[1]>F(1,2000) and odd[1]>F(1,1000);checks+=2
assert data["full_native_112"] is False and data["whole_aperture_sign"] is False;checks+=1
assert len(D)==6 and data["parity_even"]==[0,2] and data["parity_odd"]==[1,3];checks+=1
print(json.dumps(dict(passed=True,exact_checks=checks,aperture=data["aperture"],
    finite_four_mode_lower="1/2000",
    even_det_lower=str(even[0]),odd_det_lower=str(odd[0]),
    complete_native_112=False,whole_original_positive=False),indent=2))
