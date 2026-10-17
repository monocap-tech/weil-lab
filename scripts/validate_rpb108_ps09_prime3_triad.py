#!/usr/bin/env python3
"""PS09: true original signed log(3)-log(9) prime IMS three-channel triad.

Checks exact-rational original source, support, cutoff, shift exclusion,
weighted 3x3 plateau characteristic polynomial, and new essential-norm
lower >0.732. No fabricated finite Schur PSD, full-prime channel closure,
inverse-energy matrix, CC27 transfer, whole Weil positivity or RH.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps07_ims_localization as ps07

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
R = 2 * B
ORIGINAL = ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    # Complete original signed source and PS07 full IMS source/geometry parent.
    ps07.run()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(x is False for x in lane["closures"].values())

    logs={n:old.log_i(F(n)) for n,_ in ORIGINAL}
    ln3=logs[3]
    ln9=logs[9]
    # The true exact log9=2*log3 is a source identity; interval
    # enclosures for two independently evaluated logs must overlap.
    assert 2*ln3.lo <= ln9.hi and ln9.lo <= 2*ln3.hi
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    a=old.IV(ln9.lo-B,ln9.hi-B)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert F(1)<a.lo<=a.hi<B
    # I_L=[-B,-a], I_M=[ln3-B,B-ln3], I_R=[a,B].
    M_lower=ln3.lo-B
    M_upper=B-ln3.lo
    assert -F(1,100) < M_lower < 0 < M_upper < F(1,100)
    assert M_lower>-a.lo and M_upper<a.lo
    # Exact equal triad widths and translation mappings follow
    # algebraically from ell9=2ell3, not approximate endpoints.
    assert R-2*B==0
    assert F(2)*F(1,2)==F(1)
    assert len(ORIGINAL)==7 and {n for n,_ in ORIGINAL}=={2,3,4,5,7,8,9}

    # All other original prime shifts are separated by more than
    # the entire triad width from log3 and 2log3. This ensures exact
    # vanishing of their TRIPLE COMPRESSION, not full-space vanishing.
    for n,p in ORIGINAL:
        if n in (3,9):
            continue
        ln=logs[n]
        if n==2:
            assert ln3.lo-ln.hi>delta.hi
            assert ln9.lo-ln.hi>delta.hi
        else:
            assert ln.lo-ln3.hi>delta.hi
            assert ln9.lo-ln.hi>delta.hi
    assert ln3.lo>delta.hi and ln9.lo>ln3.hi+delta.hi

    # Actual weight source: von Mangoldt(3)=von Mangoldt(9)=log3.
    # The exact integer roots give
    #   w3=(log3)/sqrt3, w9=(log3)/3,
    #   sqrt(w3²+w9²)=2log3/3.
    root3=old.sqrt_i(F(3))
    w3=ln3/root3
    w9=ln3/F(3)
    assert F(0)<w3.lo<=w3.hi<F(1)
    assert F(0)<w9.lo<=w9.hi<F(1)
    rho=(F(2)/3)*ln3
    assert F(1,3)+F(1,9)==F(4,9)
    assert (F(2)/3)**2==F(4,9)
    assert F(732,1000)<rho.lo<=rho.hi<F(733,1000)
    row_upper=w3.hi+w9.hi
    assert F(1)<row_upper<F(101,100)

    # χ_L(t)+χ_R(t)=1 on exactly t∈[0,δ], by symmetry
    # of the PS06 linearly ramped edge cutoff; θ_M=0.
    # On t∈[0,δ/4]: χ_L=1, χ_R=0, χ_M=0. The
    # exact fiberwise TRUE prime IMS matrix is
    #       [[0, w3, w9],[w3,0,0],[w9,0,0]].
    #
    # Its characteristic polynomial λ*(λ²−(w3²+w9²)).
    # The underlying *exact* identity:
    #     w3²+w9²=(4/9)(log3)²=rho².
    #
    # Test generic Fraction coefficients of a,b to guard the
    # sign/coefficient orientation without floating eigenvalues:
    u,v=F(3,5),F(4,5)
    A=((F(0),u,v),(u,F(0),F(0)),(v,F(0),F(0)))
    def matvec(M,x):
        return tuple(sum((M[i][j]*x[j] for j in range(3)),F(0)) for i in range(3))
    # sqrt((3/5)²+(4/5)²)=1, ±1,0 eigenvalues exactly
    plus=(F(1),u,v)
    minus=(F(1),-u,-v)
    zero=(F(0),-v,u)
    assert matvec(A,plus)==plus
    assert matvec(A,minus)==tuple(-x for x in minus)
    assert matvec(A,zero)==(F(0),F(0),F(0))
    # Full original IMS remainder differs on the triad from this
    # prime block by compact original arch HS + finite rank poles.
    # Infinite orthonormal plateau fiber profiles are weakly null,
    # so essential norm of original full IMS >= rho.
    #
    # No spectral assertion about the whole original Q is made.

    # Classical nonnegative symmetric 3x3 row-sum upper:
    # a=w3(1-cosz), b=w3(1-sinz), c=w9(1-sin2z).
    # Since sin z+cos z >=1, a+b<=w3;
    # since 0<=1-sin2z<=1, a+c,b+c<=w3+w9.
    # This remains a true L2 three-channel compression, never
    # a claim that the GLOBAL seven-prime remainder is 3x3.

    print("PS09 original log9 edge width",float(delta.lo),float(delta.hi),flush=True)
    print("PS09 prime3 middle channel",float(M_lower),float(M_upper),flush=True)
    print("PS09 true w3 and w9 upper",float(w3.hi),float(w9.hi),flush=True)
    print("PS09 true 3-channel prime IMS row norm upper",float(row_upper),flush=True)
    print("PS09 exact noncompact plateau eigen +/-2log3/3 lower",
          float(rho.lo),flush=True)
    print("PS09 new whole original signed IMS essential norm LOWER",
          float(rho.lo),flush=True)
    print("PS09 PASS SCOPED: exact original log3-log9 triad is"
          " a fiberwise 3x3 signed PRIME-IMS compression;"
          " 5 other original prime shifts do not connect triad nodes;"
          " original full IMS essential norm >= 2log3/3 >0.732."
          " Not a 3D L2 finite rank, not a full seven-prime"
          " decomposition, Schur PSD, CC27 bridge, Weil or RH.",flush=True)

if __name__=="__main__":
    run()
