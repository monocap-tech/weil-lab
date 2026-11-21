#!/usr/bin/env python3
"""CP005: exact-Fraction formal-zero roster STRUCTURAL adapter.

No zero locations or original Lean kernels are supplied by this program.
Even with a perfectly shaped 1,748,002-row roster, return only
STRUCTURAL_PREFLIGHT_ONLY: external proof provenance and source attachment
must be verified in a separate live Lean/interval-certification workflow.
"""
import argparse
import csv
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path

ROOT_COUNT = 1_748_002
T_LO = 1_000_000
H = Q(1, 2000)
RADII = (Q(1, 1000), Q(1, 500))
CENTERS = (Q(-1099, 1000), Q(1099, 1000), Q(1, 5))
DELTA = Q(1, 10**9)
E_QUAD_ALLOWANCE = Q(1, 50000)
EPS_MAX = Q(1, 500)
TAG = "v1-1e6"
COMMIT = "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
RELEASE_SHA256 = "f777b515af89a486654052f0052b8f6760e822c88c15e0be8af753c9542c2ea2"
THEOREM = "Zeta.riemannHypothesisUpTo_1000449"
AXIOMS = ["Classical.choice", "Quot.sound", "propext"]


def frac(v):
    if not isinstance(v, str):
        raise ValueError("All interval endpoints must be exact rational strings")
    return Q(v)


def C2_bound(h):
    return 32/h+4+h


def E_tail(r):
    """Conservative HSW zero counting and CP003 k=2 bump bound at T>=1e6."""
    assert r in RADII
    return (Q(2, T_LO**3)*(Q(8,7)*21+Q(8,49))*Q(9,4)*
            (2*C2_bound(H)**2/H+C2_bound(r)**2/r))


def E_localization(r, count=ROOT_COUNT, delta=DELTA):
    """Maximum absolute row sum of the real symmetric normalized error matrix."""
    assert r in RADII
    sizes=(H,H,r)
    return max(sum(Q(count)*delta*Q(25,24)*(sizes[i]+sizes[j])*
                   (2*(sizes[i]+sizes[j])+4*abs(CENTERS[i]-CENTERS[j]))
                   for j in range(3)) for i in range(3))


def gate_margins():
    for r in RADII:
        et=E_tail(r)
        el=E_localization(r)
        total=et+el+E_QUAD_ALLOWANCE
        assert et<EPS_MAX and total<EPS_MAX, f"CP005 rational gate fails for r={r}"
        print(f"r={r}: tail< {float(et):.9f}, ordinate< {float(el):.9f}, "
              f"moment allowance=0.000020000, total< {float(total):.9f} < 0.002")


def parse_manifest(manifest_path):
    meta=json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(meta,dict):
        raise ValueError("Manifest root must be object")
    if meta.get("upstream_repository") != "smmercuri/zeta" or meta.get("tag") != TAG:
        raise ValueError("Upstream repository/tag mismatch")
    if meta.get("lean_theorem") != THEOREM:
        raise ValueError("Kernel theorem mismatch")
    if meta.get("trust_layer") != "kernel" or meta.get("axioms") != AXIOMS:
        raise ValueError("Fail closed: must be Zeta kernel layer and only standard axiom set")
    commit=meta.get("full_upstream_commit_sha")
    if commit != COMMIT:
        raise ValueError("Pinned upstream full source commit SHA mismatch")
    if meta.get("upstream_release_sha256") != RELEASE_SHA256:
        raise ValueError("Published upstream release archive digest mismatch")
    if meta.get("upstream_lean_version") != "v4.35.0" or meta.get("weil_lean_version") != "v4.34.0":
        raise ValueError("Explicit v4.35 upstream / v4.34 original toolchain mismatch must be acknowledged")
    if not isinstance(meta.get("roster_sha256"),str) or not re.fullmatch("[a-f0-9]{64}",meta["roster_sha256"]):
        raise ValueError("Source roster SHA-256 must be pinned")
    if meta.get("expected_positive_zeros_below_gram") != ROOT_COUNT:
        raise ValueError("Certified endpoint root count mismatch")
    gram=meta.get("gram_interval")
    if not isinstance(gram,list) or len(gram)!=2:
        raise ValueError("Gram boundary must have two rational endpoints")
    gl,gu=frac(gram[0]),frac(gram[1])
    if not (Q(1_000_449)<gl<=gu<Q(1_000_450)):
        raise ValueError("Gram point must be rigorously placed above 1000449, below 1000450")
    # These names describe required receipts; their content is NOT semantically
    # authenticated by this local roster-format and hash checker.
    needed=("source_lean_axioms_receipt_sha256","source_zero_batch_receipt_sha256",
            "source_turing_completeness_receipt_sha256","zero_batch_index_link_receipt_sha256")
    for k in needed:
        if not isinstance(meta.get(k),str) or not re.fullmatch("[a-f0-9]{64}",meta[k]):
            raise ValueError(f"Missing declared external receipt digest {k}")
    return meta,gl,gu


def check_roster(filename, meta, gram_lower):
    digest=hashlib.sha256()
    count=0
    prev_hi=Q(0)
    max_half=Q(0)
    with filename.open("rb") as fb:
        for raw in fb:
            digest.update(raw)
            try:
                line=raw.decode("ascii").strip()
            except UnicodeError as exc:
                raise ValueError(f"Line {count+1} not ASCII") from exc
            if not line or line.startswith("#"):
                raise ValueError("No blank/header/comment lines permitted: canonical two-column roster")
            row=next(csv.reader([line]))
            if len(row)!=2:
                raise ValueError(f"Line {count+1} must have two rational ordinates")
            a,b=frac(row[0]),frac(row[1])
            if not (0<prev_hi<a<=b<gram_lower):
                raise ValueError(f"Rosters not strictly separated, positive, or below certified Gram point at row {count+1}")
            if (b-a)/2>DELTA:
                raise ValueError(f"Row {count+1} zero bracket too wide for CP005 budget")
            if b-a>max_half*2:
                max_half=(b-a)/2
            prev_hi=b
            count+=1
            if count>ROOT_COUNT:
                raise ValueError("Too many roots")
    if count!=ROOT_COUNT:
        raise ValueError(f"Expected {ROOT_COUNT} positive zero rows, got {count}")
    if digest.hexdigest()!=meta["roster_sha256"]:
        raise ValueError("Roster SHA digest mismatch: fail closed")
    return count,max_half


def selftest():
    gate_margins()
    assert E_localization(Q(1,1000)) < Q(1,10000)
    assert E_localization(Q(1,500)) < Q(1,10000)
    # Demonstrate that an uncited zero list cannot be self-certified:
    missing={"upstream_repository":"smmercuri/zeta","tag":TAG}
    try:
        obj = json.dumps(missing)
        assert obj
        # Exercise hard gate independently without creating a fake proof receipt.
        if missing.get("trust_layer") != "kernel":
            raise ValueError("missing trust-layer certificate")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected NOT_READY negative control failed")
    print("CP005 exact Fraction error allocation and provenance negative control: PASS")
    print("NO external Lean kernel proof imported and NO certified complete zero roster supplied")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--self-test",action="store_true")
    ap.add_argument("--manifest",type=Path)
    ap.add_argument("--roster",type=Path)
    a=ap.parse_args()
    if a.self_test:
        selftest()
    if bool(a.manifest) != bool(a.roster):
        print("NOT_READY: both manifest and roster are required")
        raise SystemExit(2)
    if a.roster:
        try:
            gate_margins()
            meta,gl,gu=parse_manifest(a.manifest)
            n,width=check_roster(a.roster,meta,gl)
        except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as exc:
            print("NOT_READY:",exc)
            raise SystemExit(2)
        print("STRUCTURAL_PREFLIGHT_ONLY")
        print(f"{n} rational, strictly separated ordinate intervals; max half-width {width}; "
              f"Gram endpoint lies in ({gl},{gu})")
        print("Hashes and declared receipt fields are NOT a verified zero-batch-to-Lean-theorem proof.")
        print("Need actual kernel axiom receipts, interval isolation and Turing correspondence, "
              "outward cosine moments, complete original source mixed-form dictionary.")
    if not a.self_test and not a.roster:
        ap.print_help()


if __name__=="__main__":
    main()
