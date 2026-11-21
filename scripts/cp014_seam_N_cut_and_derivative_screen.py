#!/usr/bin/env python3
"""CP014 exact 149.5 cut-count logical preflight and pinned real source interface.

NOT a Lean kernel theorem, rigorous zeta derivative enclosure, local root
count N(150.05353), source row index 53, or original signed Weil equality.

The actual new CP014 Lean sources are separately compiled only in manual
external-v4.35 CI. This cheap gate tests the FINITE-CARDINALITY deduction
and source theorem/proof-status boundary without replacing the compiler.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
C = F(299,2)
H53_R = F(15005353,100000)
SOURCES = {
    "Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean":
        "c2b1da101a580cc91cfb0a43d72d5839fd97265c",
    "Zeta/Zeros/CountCertificates.lean":
        "a3e729d23802c3731432de9a3c7d46d18252ba10",
    "Zeta/Zeros/Certificates/Basic.lean":
        "128e19e4bb056332b0fd71a8c107f4075cd8cd07",
    "Zeta/Zeros/HardyZ.lean":
        "9975442b0c14011c35f4624197d0bf26169c7665",
}
FILES = {
    "CP014EulerCutLower.lean": (
        "fifty_two_le_N_at_original_Euler_seam",
        "riemannZeta.le_N_of_certifiedZeroIntervals",
        "riemannZeta.N_mono"
    ),
    "CP014FiniteCut.lean": (
        "exhausted_by_two_disjoint_parts",
        "exact_low_partition",
        "original_seam_root_cardinality"
    ),
    "CP014ZetaCut.lean": (
        "N_eq_card_below_original_gram",
        "original_full_source_finite_zero_card",
        "N_at_Euler_RS_seam_eq_52_of_source_witnesses",
        "hEsub", "hRsub", "hdisjoint", "hEbelow", "hRabove"
    )
}


def gitblob(path):
    n=path.stat().st_size
    h=hashlib.sha1(b"blob "+str(n).encode()+b"\0")
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def cardinality_deduction(S,E,R,c):
    assert len(E)==len(set(E)) and len(R)==len(set(R))
    assert E.isdisjoint(R)
    assert E|R<=S
    assert len(E)+len(R)==len(S)
    assert all(x<c for x in E)
    assert all(c<x for x in R)
    return len({x for x in S if x<c})


def abstract_model():
    E={F(1,2)}
    R={F(3,2),F(5,2)}
    S=E|R
    assert cardinality_deduction(S,E,R,F(1))==1
    # The full cardinality and two disjoint source partitions are NECESSARY.
    for f in [
        lambda:cardinality_deduction(S,{F(1,2)},{F(3,2)},F(1)),
        lambda:cardinality_deduction(S,{F(1,2)},{F(1,2),F(5,2)},F(1)),
        lambda:cardinality_deduction(S,{F(1,2)},{F(3,4),F(5,2)},F(1)),
    ]:
        try:
            f()
        except AssertionError:
            pass
        else:
            raise AssertionError("CP014 prerequisite negative control failed")

    # N(c)=52, a root in the candidate narrow interval, and the original
    # complete count do NOT imply ordinal rank 53, absent a local upper bound.
    euler=[F(i,1) for i in range(1,53)]
    assert all(x<C for x in euler)
    candidate=F(150053524,1000000) # 150.053524, inside CP010 candidate
    assert F(15005352,100000)<candidate<H53_R
    model_no_earlier=sorted(euler+[candidate,F(151,1)])
    model_earlier=sorted(euler+[F(749,5),candidate]) # 149.8 before candidate
    assert sum(x<C for x in model_no_earlier)==52
    assert sum(x<C for x in model_earlier)==52
    assert model_no_earlier.index(candidate)+1==53
    assert model_earlier.index(candidate)+1==54
    # Both can be extended to a full model of 1,748,002 roots without
    # changing low-seam count; this is about logical insufficiency.
    assert H53_R<C+F(1,1)
    print("CP014 EXACT FINITE ROOT-COUNT EXHAUSTION AND CUT NEGATIVE CONTROLS: PASS")
    print("CP014 NUMBER-53 RANK NOT IDENTIFIED BY N(149.5)=52 ALONE")


def inspect_sources(source_root,report):
    actual={}
    for relative,sha in SOURCES.items():
        file=source_root/relative
        if gitblob(file)!=sha:
            raise ValueError(f"Original Zeta external source SHA mismatch at {relative}")
        actual[relative]=file.read_text("utf-8")
    body=actual["Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean"]
    assert "theorem riemannZeta.N_gramPoint_eq" in body
    assert "theorem riemannZeta.order_eq_one_upto" in body
    assert "riemannZeta.N_eq_sum" in body
    assert "theorem riemannZeta.le_N_of_zeros" in body
    cc=actual["Zeta/Zeros/CountCertificates.lean"]
    assert "noncomputable def certifiedZeroCount : CertifiedZeroCount" in cc
    basic=actual["Zeta/Zeros/Certificates/Basic.lean"]
    assert "abbrev BatchSpec (n an ad bn bd : ℕ) : Prop" in basic
    hz=actual["Zeta/Zeros/HardyZ.lean"]
    assert "noncomputable def Zeta.hardyZ (t : ℝ) : ℝ" in hz
    assert "theorem hardyZ_eq_zero_iff_riemannZeta" in hz

    for name,strings in FILES.items():
        local=(ROOT/"cp011_zeta_v435"/name).read_text("utf-8")
        for text in strings:
            if text not in local:
                raise ValueError(f"Missing explicit CP014 Lean source prerequisite: {name}: {text}")
        if "sorry" in local.split("@[expose] public section")[-1]:
            raise ValueError(f"Actual CP014 Lean theorem section includes sorry: {name}")
    receipt={
        "status":"CP014_SOURCE_SIGNATURE_AND_EXACT_LOGIC_PASS_NOT_KERNEL",
        "original_upstream_commit":SOURCE_COMMIT,
        "original_upstream_lean_blobs":SOURCES,
        "cut":"149500/1000",
        "certified_upstream_original_total":1748002,
        "first_euler_certified_source_slots":52,
        "separate_rs_certified_source_slots":1747950,
        "new_N_cut_exact_Lean_kernel":None,
        "new_source_witness_finset_cover_Lean_kernel":None,
        "local_ordinal_53_bound_proved":False,
        "original_Weil_spectral_dictionary_proved":False,
    }
    report.write_text(json.dumps(receipt,indent=2)+"\n","utf-8")
    print(receipt["status"])
    print("All conclusions conditional on ACTUAL independent original Lean receipts.")


def numeric_derivative_screen():
    import mpmath as mp
    mp.mp.dps=50
    def mprat(r):
        return mp.mpf(r.numerator)/r.denominator
    a=C
    b=H53_R
    samples=[]
    for i in range(17):
        x=a+(b-a)*i/16
        t=mprat(x)
        z=mp.siegelz(t)
        dz=mp.diff(mp.siegelz,t)
        samples.append((x,dz))
        print("NUMERICAL-NONRIGOROUS: t=",str(x),
              "  HardyZ=",mp.nstr(z,16),
              "  Zprime=",mp.nstr(dz,16))
    assert min(d for _,d in samples)>0
    print("CP014 17/17 POSITIVE HARDY Z DERIVATIVE SAMPLES — NONRIGOROUS ONLY")
    print("This is NOT a uniform derivative enclosure, unique-root theorem or N(150.05353)=53.")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--source-root",type=Path)
    p.add_argument("--numeric-derivative-screen",action="store_true")
    p.add_argument("--receipt",type=Path,default=Path("cp014-source-seam-count-preflight.json"))
    a=p.parse_args()
    if a.self_test:
        abstract_model()
    if a.source_root:
        try:
            inspect_sources(a.source_root,a.receipt)
        except (OSError,ValueError,AssertionError,UnicodeError,KeyError) as e:
            raise SystemExit(f"NOT_READY: {e}")
    if a.numeric_derivative_screen:
        numeric_derivative_screen()
    if not (a.self_test or a.source_root or a.numeric_derivative_screen):
        p.print_help()


if __name__=="__main__":
    main()
