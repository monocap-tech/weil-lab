#!/usr/bin/env python3
"""CP004: exact-rational NECESSARY finite spectral falsifier, never a proof of RH.

Input interval matrices must be certified externally. This checks their algebraic
compatibility against *conditional* CP003 tail bounds. The only positive verdict
is INCONCLUSIVE (not falsified); no comparison can be certified by this script.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

T = 2**20
H = F(1, 2000)
RADII = {F(1, 1000), F(1, 500)}
REQUIRED = ("original_source_blob", "original_lean_axiom_receipt",
            "full_arithmetic_interval_certificate", "finite_critical_line_theorem",
            "complete_zero_count_certificate", "zero_roster_digest",
            "finite_transform_quadrature_certificate", "full_mixed_dictionary_certificate")


def tail_upper(r):
    """Published zero-count + conditional CP003 bump estimates, all rational."""
    assert r in RADII
    C = lambda h: F(32) / h + 4 + h
    k = F(2, T**3) * (F(8, 7) * 21 + F(8, 49))
    return k * F(9, 4) * (2 * C(H)**2 / H + C(r)**2 / r)


def fraction(x):
    if not isinstance(x, str):
        raise ValueError("All numeric endpoints must be exact rational STRINGS")
    y = F(x)
    if str(y) == "nan":
        raise ValueError("Invalid rational")
    return y


def interval(raw):
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError("Interval must be a two-element [lower,upper] rational string list")
    a, b = map(fraction, raw)
    if a > b:
        raise ValueError("Outward interval inverted")
    return a, b


def parse_matrix(raw):
    if not isinstance(raw, dict):
        raise ValueError("Expected matrix with real and imag components")
    mats = []
    for key in ("real", "imag"):
        m = raw.get(key)
        if not isinstance(m, list) or len(m) != 3 or any(not isinstance(row, list) or len(row) != 3 for row in m):
            raise ValueError("Expected a 3x3 matrix")
        mats.append([[interval(v) for v in row] for row in m])
    return mats[0], mats[1]


def intersects(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


def intersect(a, b):
    return (max(a[0], b[0]), min(a[1], b[1])) if intersects(a, b) else None


def neg(a):
    return -a[1], -a[0]


def abs_min(a):
    if a[0] <= 0 <= a[1]:
        return F(0)
    return min(abs(a[0]), abs(a[1]))


def gap(a, b):
    """Rigorous lower separation between any points in intervals a and b."""
    if intersects(a, b):
        return F(0)
    return b[0] - a[1] if a[1] < b[0] else a[0] - b[1]


def iadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def ineg(a):
    return -a[1], -a[0]


def imul(a, b):
    p = [x*y for x in a for y in b]
    return min(p), max(p)


def isquare(a):
    return abs_min(a)**2, max(abs(a[0]), abs(a[1]))**2


def determinant_enclosure(m):
    # Symmetric real 3x3: a*d*f + 2*b*c*e - a*e² - d*c² - f*b²
    a,b,c = m[0]
    d,e = m[1][1],m[1][2]
    f = m[2][2]
    product = imul(imul(a,d),f)
    triple = imul((F(2), F(2)), imul(imul(b,c),e))
    negative_terms = (imul(a,isquare(e)), imul(d,isquare(c)), imul(f,isquare(b)))
    result = iadd(product,triple)
    for term in negative_terms:
        result = iadd(result,ineg(term))
    return result


def zero_side_structural_falsifiers(sr, si):
    errors = []
    symmetric = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if not (si[i][j][0] <= 0 <= si[i][j][1]):
                errors.append(f"zero matrix [{i},{j}] has nonzero imaginary component")
            if not intersects(sr[i][j], sr[j][i]):
                errors.append(f"zero matrix [{i},{j}] violates real symmetry")
            if not intersects(si[i][j], neg(si[j][i])):
                errors.append(f"zero matrix [{i},{j}] violates Hermitian symmetry")
            symmetric[i][j] = intersect(sr[i][j], sr[j][i])
    if not intersects(sr[0][0],sr[1][1]):
        errors.append("equal-shape old diagonal identity is impossible")
    for i in range(3):
        if sr[i][i][1] < 0:
            errors.append(f"zero-side Gram diagonal [{i},{i}] definitely negative")
    if errors or any(symmetric[i][j] is None for i in range(3) for j in range(3)):
        return errors
    # Sharpen both old diagonal enclosures with exact structural equality.
    common = intersect(symmetric[0][0], symmetric[1][1])
    if common is None:
        return ["equal-shape old diagonal identity is impossible"]
    symmetric[0][0] = common
    symmetric[1][1] = common
    for i in range(3):
        for j in range(i+1,3):
            dij = symmetric[i][i][1]*symmetric[j][j][1]
            if dij>=0 and abs_min(symmetric[i][j])**2>dij:
                errors.append(f"two-by-two zero-side Gram minor [{i},{j}] impossible")
    det = determinant_enclosure(symmetric)
    if det[1] < 0:
        errors.append("three-by-three zero-side Gram determinant definitely negative")
    return errors


def compare(data, check_provenance=True):
    if not isinstance(data, dict):
        return "NOT_READY", ["Manifest object missing"]
    missing = []
    if data.get("T") != T:
        missing.append("finite cutoff T=1048576 not supplied")
    try:
        r = fraction(data.get("radius"))
    except Exception:
        r = None
    if r not in RADII:
        missing.append("radius must be '1/1000' or '1/500'")
    p = data.get("provenance", {})
    if check_provenance:
        for key in REQUIRED:
            value = p.get(key) if isinstance(p, dict) else None
            if not isinstance(value, str) or not value.strip():
                missing.append(f"provenance.{key} missing")
    try:
        ar, ai = parse_matrix(data["arithmetic_full_original"])
        zr, zi = parse_matrix(data["spectral_complete_truncation"])
    except (ValueError, KeyError, TypeError) as exc:
        missing.append(f"interval matrix: {exc}")
        return "NOT_READY", missing
    if missing:
        return "NOT_READY", missing
    findings=zero_side_structural_falsifiers(zr,zi)
    for i in range(3):
        for j in range(3):
            if not intersects(ar[i][j],ar[j][i]):
                findings.append(f"arithmetic matrix real Hermitian symmetry [{i},{j}] impossible")
            if not intersects(ai[i][j],neg(ai[j][i])):
                findings.append(f"arithmetic matrix complex Hermitian symmetry [{i},{j}] impossible")
    E=tail_upper(r)
    assert E<F(1,500), "tail preflight failure"
    h=[H,H,r]
    for i in range(3):
        for j in range(3):
            bound=E*(h[i]+h[j])
            dr=gap(ar[i][j],zr[i][j])
            di=gap(ai[i][j],zi[i][j])
            if dr*dr+di*di>bound*bound:
                findings.append(f"entry [{i},{j}] rigorous real/imag separation exceeds conditional error allowance")
    if findings:
        return "FALSIFIED_CONDITIONAL_INTERFACE", sorted(set(findings))
    return "INCONCLUSIVE", [
        "No contradiction found. Provenance strings are NOT verified by this script.",
        "Original source Lean proof, exhaustive Turing count, transform quadrature and full mixed dictionary require independent verification.",
    ]


def selftest():
    for r in RADII:
        assert tail_upper(r)<F(1,500)
    z=lambda v: [str(v),str(v)]
    mat=lambda v: {"real":[[z(v if i==j else 0) for j in range(3)] for i in range(3)],
                   "imag":[[z(0) for j in range(3)] for i in range(3)]}
    good={"radius":"1/1000","T":T,"provenance":{k:"synthetic-test-only" for k in REQUIRED},
          "arithmetic_full_original":mat(1),"spectral_complete_truncation":mat(1)}
    assert compare(good)[0]=="INCONCLUSIVE"
    bad=dict(good,spectral_complete_truncation=mat(2))
    assert compare(bad)[0]=="FALSIFIED_CONDITIONAL_INTERFACE"
    asymmetric=mat(1)
    asymmetric["real"][0][0]=z(3)
    bad2=dict(good,spectral_complete_truncation=asymmetric)
    assert compare(bad2)[0]=="FALSIFIED_CONDITIONAL_INTERFACE"
    absent=dict(good,provenance={})
    assert compare(absent)[0]=="NOT_READY"
    spectral_neg=mat(-1)
    bad3=dict(good,spectral_complete_truncation=spectral_neg)
    assert compare(bad3)[0]=="FALSIFIED_CONDITIONAL_INTERFACE"
    print("CP004 PASS: exact-rational tail checks and four fail-closed synthetic negative controls")
    print("No real zero table or arithmetic interval certificate has been supplied or certified.")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--compare",type=Path,help="JSON manifest with full-original arithmetic and complete zero matrix intervals")
    parser.add_argument("--self-test",action="store_true")
    opts=parser.parse_args()
    if opts.self_test:
        selftest()
    if opts.compare:
        verdict, evidence=compare(json.loads(opts.compare.read_text(encoding="utf-8")))
        print(verdict)
        for item in evidence:
            print(" -",item)
        if verdict=="NOT_READY":
            raise SystemExit(2)
    if not opts.self_test and not opts.compare:
        parser.print_help()


if __name__=="__main__":
    main()
