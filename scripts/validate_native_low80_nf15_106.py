#!/usr/bin/env python3
"""NF15: exact original E80 native finite positivity; not full Weil aperture.
Inputs: new 80-mode source JSON and optionally older 64-mode source JSON
(both signed original, same aperture) to audit all 4224 nested overlaps.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def validate(source,old64=None):
    raw=Path(source).read_bytes();d=json.loads(raw);n=80
    assert d["aperture"]=="53/50" and d["dim"]==n
    assert d["N"]==490 and d["K"]==430
    D=d["complete_form"];assert len(D)==1640
    matrix=[[F(0)]*n for _ in range(n)]
    error=F(0);width=F(0);component_checks=0
    midpoint_grid=10**85
    for key,parts in D.items():
        i,j=map(int,key.split(","))
        assert 0<=i<=j<n and (i+j)%2==0
        for kind in ("arch","prime","poles","full"):
            lo,hi=map(F,parts[kind]);assert lo<=hi
            component_checks+=1
        lo,hi=map(F,parts["full"])
        assert lo<=sum(F(parts[k][1]) for k in ("arch","prime","poles"))
        assert hi>=sum(F(parts[k][0]) for k in ("arch","prime","poles"))
        middle=(lo+hi)/2;center=F((middle*midpoint_grid).__floor__(),midpoint_grid)
        matrix[i][j]=matrix[j][i]=center
        error=max(error,abs(center-lo),abs(center-hi))
        width=max(width,hi-lo)
    assert component_checks==6560
    assert all(matrix[i][j]==0 for i in range(n) for j in range(n) if (i+j)%2)
    op_error=n*error
    assert op_error<F(1,10**65)
    shift=F(1,10**33)
    counts={}
    for parity in (0,1):
        ids=list(range(parity,n,2));a=[
            [matrix[i][j]-(shift if i==j else 0) for j in ids] for i in ids
        ]
        for k in range(len(ids)):
            pivot=a[k][k]
            assert pivot>0,("Nonpositive shifted pivot; INCONCLUSIVE",parity,k,str(pivot))
            for i in range(k+1,len(ids)):
                for j in range(i,len(ids)):
                    a[i][j]=a[j][i]=a[i][j]-a[i][k]*a[k][j]/pivot
        counts["even" if parity==0 else "odd"]=len(ids)
    lower=shift-op_error
    assert lower>F(9,10**34)
    overlaps=None
    if old64 is not None:
        old=json.loads(Path(old64).read_bytes())
        assert old["dim"]==64 and old["aperture"]=="53/50"
        overlaps=0
        for key,v in old["complete_form"].items():
            for kind in ("arch","prime","poles","full"):
                lo,hi=map(F,v[kind]);a,b=map(F,D[key][kind])
                assert max(lo,a)<=min(hi,b),(key,kind)
                overlaps+=1
        assert overlaps==4224
    return dict(status="PASS",aperture="53/50",source_sha256=hashlib.sha256(raw).hexdigest(),
        dim=80,entry_count=len(D),component_interval_checks=component_checks,
        E64_component_interval_intersections=overlaps,
        max_entry_interval_width=str(width),
        complete_operator_error_upper=str(op_error),midpoint_shift=str(shift),
        all_exact_shifted_parity_pivots=counts,
        strict_finite_physical_lower=str(lower),
        conservative_physical_lower="9/10000000000000000000000000000000000",
        full_native112=False,source_action_Gram=False,
        corrected_whole_domain_Schur=False,whole_aperture_positive=False,
        RH=False,Lean=False)

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("native80");p.add_argument("--old64")
    a=p.parse_args();print(json.dumps(validate(a.native80,a.old64),indent=2))
