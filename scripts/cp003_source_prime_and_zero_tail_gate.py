#!/usr/bin/env python3
"""CP003 exact Fraction audit: arithmetic overlap, bump mass and zero tail.
Never claim Lean, complete zero enumeration, or original spectral-source acceptance.
The IV011 byte check is optional because the CP branch intentionally excludes IV###.
"""
import argparse
import hashlib
from fractions import Fraction as F
from pathlib import Path

H = F(1, 2000)
D = F(1099, 500)
RADII = (F(1, 1000), F(1, 500))
IV011_BLOB = "14d8f01ce34f764900eccc68399d7323b4f4a25c"

def log_enclosure(n, terms=64):
    """Rational atanh series + positive geometric tail, n>=2."""
    assert n >= 2
    x = F(n-1, n+1)
    lower = sum((2*x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    upper = lower+2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
    return lower, upper

def bump_mass_lower(steps=64, power=32):
    """Proves a2>24/25 using exp(-x)>=(1-x/power)^power."""
    width = F(7,8)/steps
    total = F(0)
    for j in range(1, steps+1):
        u = j*width
        x = 2*u*u/(1-u*u)
        assert 0 <= x < power
        total += 2*width*(1-x/power)**power
    return total

def source_audit(source):
    if source is None:
        print("Original IV011 source-bounded attachment: OPEN (no --iv011-file)")
        return
    raw = Path(source).read_bytes()
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()
    assert blob == IV011_BLOB, "Original IV011 source changed: fail closed"
    content = raw.decode("utf-8")
    for marker in (
        "theorem neutralIV011MixedCorrelation_eq_schwartzIntegral",
        "∫ x : ℝ, t x * conj (s (x - τ))",
        "def neutralIV011OriginalMixedPrime",
        "ArithmeticFunction.vonMangoldt n / Real.sqrt n",
        "def neutralIV011OriginalMixedPole",
        "def neutralIV011OriginalMixedArch",
        "theorem neutralIV011OriginalMixed_arithmeticSplit",
    ):
        assert marker in content, f"Original IV011 marker missing: {marker}"
    print("Original IV011 blob and literal conventions match (text audit only)")

def prime_gate():
    lo, hi = log_enclosure(9)
    assert F(219722,100000) < lo < hi < F(219723,100000)
    assert 0 < D-hi and D-lo < 2*H
    overlap_width_upper = F(219723,100000)-(D-2*H)
    assert overlap_width_upper == F(23,100000)
    # At least one of the two bump coordinates exceeds 3/4 in magnitude.
    # Then phi(u)<1/2, since exp(9/7)>1+9/7>2.
    assert (D-hi)/H > F(3,2)
    assert F(9,7)>1
    i9_upper = overlap_width_upper/2
    assert i9_upper == F(23,200000)
    shape_mass_lower = bump_mass_lower()
    assert shape_mass_lower > F(24,25)
    m0_lower = H*F(24,25)
    assert m0_lower == F(3,6250)
    ratio_upper = i9_upper/m0_lower
    assert ratio_upper == F(23,96)
    assert log_enclosure(3)[1] < F(6,5)
    prime_burden_upper = F(2,5)*ratio_upper
    assert prime_burden_upper == F(23,240) < F(1,10)
    for r in RADII:
        # eta<2 from strict Cauchy-Schwarz; exact kappa=eta*(2H+r).
        capacity_upper = 2*(2*H+r)
        margin = F(11,10)-75*capacity_upper-prime_burden_upper
        target = F(7,10) if r==F(1,1000) else F(11,20)
        assert margin>target
        print(f"r={r}: conditional original signed margin > {target}; prime burden < {prime_burden_upper}")
    print("PRIME: a2>24/25, I9<23/200000 and pi(V_r)<23/240 (exact-rational deductions PASS)")

def zero_tail_gate():
    # Hasanalizade--Shen--Wong 2022 counts positive nontrivial zeros.
    # Conservatively allow 7/8 beyond the arXiv abstract's error formula:
    # N+(U) <= (U/6+2)*log U+11 <= (U/2)log U for U>=100.
    assert F(1038,10000)+F(2573,10000)<2
    assert F(7,8)+F(93675,10000)<11
    assert F(100,3)-2>11
    # So two-sided Nabs(U)<=U*log U, U>=100, with conjugate symmetry.
    # Bump calculus: ||phi||1<=2, ||phi'||1=2, ||phi''||1<16,
    # exp(11/20)<2; thus C2(b_h)<32/h+4+h and L2mass>=4h/9.
    exponent=20
    T=2**exponent
    assert T>=100
    # k=2, A=B=1, log2<1 => rational upper K2(T).
    K = F(2, T**3)*(F(8,7)*(exponent+1)+F(8,49))
    for r in RADII:
        C_old=32/H+4+H
        C_new=32/r+4+r
        mass_normalized_sum=F(9,4)*(2*C_old*C_old/H+C_new*C_new/r)
        tail=K*mass_normalized_sum
        assert tail<F(1,500)
        print(f"r={r}, T=2^{exponent}: conditional operator tail < 1/500 (exact-rational PASS)")
    print("ZERO: zero-count theorem provenance and completeness remain external proof inputs")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--iv011-file", default=None)
    opts=parser.parse_args()
    source_audit(opts.iv011_file)
    prime_gate()
    zero_tail_gate()
    print("CP003 FRACTION PREFLIGHT PASS; NO LEAN PASS, RH OR GLOBAL POSITIVITY")

if __name__=="__main__":
    main()
