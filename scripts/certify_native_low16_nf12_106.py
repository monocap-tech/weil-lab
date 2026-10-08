#!/usr/bin/env python3
"""NF12 native 16-mode exact-rational sign, with all original source terms.
Depends on independent low4 full-form generator; increases its retained degree
to 15. No claim about full112 corrected Schur or whole-domain positivity.
"""
import json,hashlib
from fractions import Fraction as F
import certify_native_low4_nf12_106 as native
native.DEG=15

def certificate():
    D,width,secs=native.construct()
    N=16;GRID=10**32;M=[[F(0)]*N for _ in range(N)];err=F(0)
    assert len(D)==72
    for key,v in D.items():
        i,j=map(int,key.split(','))
        lo,hi=map(F,v['full']);mid=(lo+hi)/2
        c=F(int(mid*GRID),GRID)
        err=max(err,abs(c-lo),abs(c-hi))
        M[i][j]=M[j][i]=c
    # Exact parity: the source constructor skips all odd i+j entries.
    assert all(M[i][j]==M[j][i] for i in range(N) for j in range(N))
    assert all(M[i][j]==0 for i in range(N) for j in range(N) if (i+j)%2)
    assert N*err<F(1,10**17)
    shift=F(6,10**13)
    B=[[M[i][j]-(shift if i==j else 0) for j in range(N)]
       for i in range(N)]
    pivots=[]
    for k in range(N):
        p=B[k][k]
        assert p>0, (k,str(p))
        pivots.append(p)
        for i in range(k+1,N):
            for j in range(i,N):
                B[i][j]=B[j][i]=B[i][j]-B[i][k]*B[k][j]/p
    assert len(pivots)==16
    assert shift-N*err>F(5,10**13)
    raw=json.dumps(D,sort_keys=True,separators=(',',':'))
    return dict(stage="NF12 complete native finite low16 signed interval certificate",
      aperture="53/50",retained_dimension=N,even_modes=8,odd_modes=8,
      native_interval_entries=len(D),all_prime_powers=[2,3,4,5,7,8],
      complete_archimedean=True,both_original_prime_orientations=True,
      signed_hermitian_poles=True,
      exact_native_interval_max_width=str(width),
      midpoint_rounding_denominator=str(GRID),
      entrywise_max_midpoint_error=str(err),
      complete_symmetric_operator_error_upper=str(N*err),
      shifted_midpoint_test_amount=str(shift),
      exact_shifted_LDL_positive_pivots=len(pivots),
      rigorous_full16_native_lower="1/2000000000000",
      native_interval_json_sha256=hashlib.sha256(raw.encode()).hexdigest(),
      compute_seconds_display=secs,
      full_112=False,corrected_source_gram=False,
      infinite_complement_schur=False,whole_original_positive=False,
      RH=False,lean_certified=False)
if __name__=="__main__":
    print(json.dumps(certificate(),indent=2))
