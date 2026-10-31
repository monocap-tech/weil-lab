#!/usr/bin/env python3
"""NF429: true original cell-6 Chebyshev-square integration router.

Acceptance levels:
  (1) Original NF406 true log7/log8 knots + pure exact Chebyshev product
      algebra and native 0..2998 raw dx moment enclosures.
  (2) Optional actual signed pz and z^2 ONLY if ALL 1500 original-source
      Chebyshev coefficient interval balls and NF428 signed p moments exist.
Without complete inputs, no signed integral is asserted. No RH claim.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb, ctx

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

B, C, H = F(11, 10), F(91, 100), F(7, 100)
DEGREE, MOMENTS = 1499, 2999
EPS = F(2, 10**45)
ZERO = (F(0), F(0))


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def A(x):
    return arb(str(x))


def outward(z, digits=75):
    m, r, e = z.mid_rad_10exp(digits)
    q = F(10) ** int(e)
    return F((int(m)-int(r))) * q, F((int(m)+int(r))) * q


def read_ball(pair):
    lo, hi = F(pair[0]), F(pair[1])
    assert lo <= hi
    return lo, hi


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    products = (x[0]*y[0], x[0]*y[1], x[1]*y[0], x[1]*y[1])
    return min(products), max(products)


def scale(q, x):
    return (q*x[0], q*x[1]) if q >= 0 else (q*x[1], q*x[0])


def abs_upper(x):
    return max(abs(x[0]), abs(x[1]))


def pol_add(a, b):
    o = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a): o[i] += v
    for i, v in enumerate(b): o[i] += v
    return o


def pol_mul(a, b):
    o = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            o[i+j] += u*v
    return o


def pol_integral(a, l, r):
    return sum((q * (r**(k+1)-l**(k+1)) / (k+1)
                for k, q in enumerate(a)), F(0))


def cheb_square_coefficients(a):
    """Valid for interval coefficients, product-to-sum with paired i<j."""
    n = len(a)
    out = [ZERO for _ in range(2*n-1)]
    for i in range(n):
        for j in range(i, n):
            prod = mul(a[i], a[j])
            if i == j:
                half = scale(F(1, 2), prod)
                out[0] = add(out[0], half)
                out[2*i] = add(out[2*i], half)
            else:
                out[j-i] = add(out[j-i], prod)
                out[j+i] = add(out[j+i], prod)
    return out


def exact_identity_tests():
    """Independent Fraction polynomial/rational endpoint integration."""
    t = [[F(1)], [F(0), F(1)]]
    for n in range(2, 10):
        t.append(pol_add([2*q for q in pol_mul([F(0), F(1)], t[-1])],
                         [-q for q in t[-2]]))
    l, r = F(-3, 5), F(4, 5)
    j = [pol_integral(p, l, r) for p in t]
    for i in range(5):
        for k in range(5):
            direct = pol_integral(pol_mul(t[i], t[k]), l, r)
            assert direct == (j[i+k] + j[abs(i-k)])/2
    # Independent nontrivial square check, including constant T0,
    # high/low product cross terms and signed input coefficients.
    c = [F(2, 3), F(-3, 7), F(5, 11), F(-2, 13)]
    polynomial = [F(0)]
    for ci, ti in zip(c, t):
        polynomial = pol_add(polynomial, [ci*q for q in ti])
    direct = pol_integral(pol_mul(polynomial, polynomial), l, r)
    b = cheb_square_coefficients([(ci, ci) for ci in c])
    contracted = sum((x[0]*j[k] for k, x in enumerate(b)), F(0))
    assert contracted == direct
    return True


def original_raw_moments(seams, bits):
    assert seams["W_ODD_NEG"] == seams["RH"] == "OPEN"
    knots = seams["certified_ordered_knots"]
    assert knots[13]["label"] == "-B+log(7)"
    assert knots[14]["label"] == "-B+log(8)"
    assert F(knots[13]["low"]) > F(21, 25)
    assert F(knots[14]["high"]) < F(49, 50)
    assert F(knots[13]["high"]) < F(knots[14]["low"])
    ctx.prec = bits
    left, right = A(7).log()-A(B), A(8).log()-A(B)
    assert A(F(21, 25)) < left < right < A(F(49, 50))
    tl, tr = (left-A(C))/A(H), (right-A(C))/A(H)
    assert -1 < tl < tr < 1
    length = right - left
    tleft, tright = tl.acos(), tr.acos()
    vals = [outward(length), outward(A(H)*(tr*tr-tl*tl)/2)]
    # For n>=2, Chebyshev primitive:
    # H*[ T_{n+1}/(2(n+1)) - T_{n-1}/(2(n-1)) ]_{tl}^{tr}.
    for n in range(2, MOMENTS):
        dm = (arb(n+1)*tright).cos() - (arb(n+1)*tleft).cos()
        dp = (arb(n-1)*tright).cos() - (arb(n-1)*tleft).cos()
        vals.append(outward(A(H)*(dm/(2*(n+1))-dp/(2*(n-1)))))
    assert len(vals) == MOMENTS
    lval = outward(length)
    assert vals[0][0] <= lval[1] and lval[0] <= vals[0][1]
    # On the true cell |T_n|<=1. With 2048-bit intervals the
    # extra 1e-40 safety envelope below is larger than native widths.
    for n, v in enumerate(vals):
        assert 0 <= v[1]-v[0] < F(1, 10**40), n
        assert v[0] > -lval[1] - F(1, 10**40), n
        assert v[1] <  lval[1] + F(1, 10**40), n
    return vals


def assemble_full_z(paths, source_sha, seams_sha):
    received = {}
    digests = []
    for path in paths:
        data, digest = load(path)
        assert data["source_sha256"] == source_sha
        assert data["seams_sha256"] == seams_sha
        assert data["original_true_cell6"] == "(log(7)-11/10,log(8)-11/10)"
        assert data["original_all_five_post_seam_primes_retained"] == [2,3,4,5,7]
        assert data["original_two_neither_branches"] == [8,9]
        assert data["W_ODD_NEG"] == data["RH"] == "OPEN"
        digests.append(digest)
        for e in data["coefficients"]:
            n = e["n"]
            assert 0 <= n <= DEGREE and n not in received
            v = read_ball(e["true_original_cell6_fixed_branch_coefficient_outward_interval"])
            assert v[1]-v[0] < F(1, 10**25)
            received[n] = v
    missing = sorted(set(range(DEGREE+1)) - set(received))
    return received, missing, digests


def finish_if_complete(a, moments, p, p_sha):
    assert len(a) == DEGREE+1 and len(moments) == MOMENTS
    assert p["all_1500_source_signed_chebyshev_moments_certified"]
    assert p["original_signed_primes_on_cell6"] == [2,3,4,5,7]
    assert p["original_inactive_prime_branches"] == [8,9]
    assert p["original_x_domain"] == "(log(7)-11/10,log(8)-11/10)"
    assert p["degree"] == DEGREE
    assert p["W_ODD_NEG"] == p["RH"] == "OPEN"
    pm = [read_ball(q) for q in p["original_signed_p_chebyshev_moments_n0_to_n1499"]]
    assert len(pm) == DEGREE+1
    assert pm[0][1] < 0, "The certified original cell6 principal p is negative"
    for q in pm:
        assert q[1]-q[0] < F(1, 10**25)
    pz = ZERO
    for ai, mi in zip(a, pm):
        pz = add(pz, mul(ai, mi))
    # No new quadrature: exact Chebyshev product-to-sum and original
    # irrational-cell raw dx moment vector 0..2998.
    b = cheb_square_coefficients(a)
    z2 = ZERO
    for bi, ji in zip(b, moments):
        z2 = add(z2, mul(bi, ji))
    pmax = sum(map(abs_upper, a), F(0))
    cell_length = moments[0][1]
    pz_fee = EPS * (-pm[0][0])
    z2_fee = cell_length * (2*EPS*pmax + EPS**2)
    pz = (pz[0]-pz_fee, pz[1]+pz_fee)
    z2 = (z2[0]-z2_fee, z2[1]+z2_fee)
    signed = add(scale(4, pz), scale(2, z2))
    assert z2[1] >= 0
    return {
        "original_nf428_signed_principal_moments_sha256": p_sha,
        "true_original_cell6_pz_outward_interval": list(map(str, pz)),
        "true_original_cell6_z2_outward_interval": list(map(str, z2)),
        "true_original_cell6_2z2_plus_4pz_outward_interval": list(map(str, signed)),
        "original_signed_pz_tail_fee_exact": str(pz_fee),
        "original_z2_tail_fee_exact": str(z2_fee),
        "full_original_1500_coefficients_consumed": True,
        "true_cell6_integral_evaluated": True
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seams", default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--source", default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--bits", type=int, default=2048)
    ap.add_argument("--z-block", action="append", default=[])
    ap.add_argument("--p-moments")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    assert args.bits >= 1024
    seams, seams_sha = load(args.seams)
    source, source_sha = load(args.source)
    assert source["original_dimension"] == 242
    assert source["W_ODD_NEG"] == source["RH"] == "OPEN"
    assert exact_identity_tests()
    moments = original_raw_moments(seams, args.bits)
    receipt = {
        "pass": "NF429",
        "standing": "EXACT ORIGINAL CELL6 CHEBYSHEV PRODUCT CONTRACT AND ALL 2999 RAW dx MOMENTS; COMPLETE SIGNED INTEGRAL CONDITIONAL",
        "nf406_original_seams_sha256": seams_sha,
        "nf407_original_source_sha256": source_sha,
        "original_exact_rational_Chebyshev_product_and_independent_quadratic_tests": True,
        "original_actual_log7_log8_cell6": "(log(7)-11/10,log(8)-11/10)",
        "original_centre": str(C),
        "original_halfwidth": str(H),
        "native_bits": args.bits,
        "number_of_original_raw_dx_moments": MOMENTS,
        "original_cell6_raw_Chebyshev_dx_moments_n0_to_n2998":
            [[str(lo), str(hi)] for lo, hi in moments],
        "true_original_cell6_integral_evaluated": False,
        "original_nf404_complete_signed_scalar_decided": False,
        "W_ODD_NEG": "OPEN", "RH": "OPEN"
    }
    if args.z_block:
        coefficients, missing, digests = assemble_full_z(args.z_block, source_sha, seams_sha)
        receipt["provided_original_z_coefficients"] = len(coefficients)
        receipt["missing_original_z_coefficient_indices"] = missing
        receipt["original_z_block_sha256"] = digests
        if not missing:
            assert args.p_moments is not None
            p, p_sha = load(args.p_moments)
            assert p["nf407_original_full_source_sha256"] == source_sha
            assert p["nf406_original_seams_sha256"] == seams_sha
            receipt.update(finish_if_complete([coefficients[n] for n in range(DEGREE+1)],
                                               moments, p, p_sha))
            receipt["standing"] = "FULL ORIGINAL CELL6 SIGNED pz AND z2 CONTRACTED; NF410/NF404 WHOLE-SCALAR OPEN"
            receipt["true_original_cell6_integral_evaluated"] = True
    dest = Path(args.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(receipt, indent=2) + "\n")
    print("NF429 original raw Chebyshev 0..2998 moments and exact product identity PASS")
    if not receipt["true_original_cell6_integral_evaluated"]:
        print("NF429 true cell6 pz/z2 NOT EVALUATED: all 1500 original z balls required")
    else:
        print("NF429 true complete cell6 signed contribution EVALUATED (not whole NF404)")
if __name__ == "__main__":
    main()
