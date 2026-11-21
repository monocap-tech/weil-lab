#!/usr/bin/env python3
"""CP016 exact ordinal-53 finite-height ZERO-RANK falsifier and source custody.

This script verifies conceptual source contracts and exact rational finite
model instances. It does NOT compile Lean, prove Zeta.hardyZ monotonicity,
prove the CP010 refined Euler interval contains a zero, or manufacture the
original intermediate first RS source-row endpoints.

Use the MANUAL/PR-LABEL kernel workflow for actual Zeta v4.35 .olean and
# print axioms; never accept a Python "PASS" as a Lean kernel certificate.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
SHAS={
    "Zeta/Zeros/Interval.lean": "152954545ca9997c2a2ddaead4d9161ffbbfe191",
    "Zeta/Zeros/CountCertificates.lean":
      "a3e729d23802c3731432de9a3c7d46d18252ba10",
    "Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean":
      "c2b1da101a580cc91cfb0a43d72d5839fd97265c",
    "Zeta/Zeros/HardyZ.lean":
      "9975442b0c14011c35f4624197d0bf26169c7665",
}
MATHLIB_REF="v4.35.0"
MATHLIB_REL="Mathlib/Data/Set/Finite/Lemmas.lean"
MATHLIB_SHA="de41c17e1d3056674b274a6b3e695a9e20c87a25"
SOURCE_016=ROOT/"cp011_zeta_v435/CP016FirstRSRank.lean"
SOURCE_ATTACH=ROOT/"cp011_zeta_v435/CP016MonotoneAttach.lean"
SOURCE_SEAM=ROOT/"cp011_zeta_v435/CP015SourceWitnesses.lean"


def sha_git_blob(path):
    size=path.stat().st_size
    hasher=hashlib.sha1(b"blob "+str(size).encode()+b"\0")
    with path.open("rb") as stream:
        for buf in iter(lambda:stream.read(1024*1024),b""):
            hasher.update(buf)
    return hasher.hexdigest()


def abstract_ordinal_model():
    """Pure exact Fraction model, no analytic zeta premise or numeric proof."""
    cut=F(299,2)
    euler=tuple(F(k,1) for k in range(1,53))
    # Simulate authentic distinct, disjoint witness zero sets:
    rs=(F(150), F(152), F(157))
    S=set(euler)|set(rs)
    assert len(euler)==52 and all(x<cut for x in euler)
    assert len(set(rs))==3 and all(x>cut for x in rs)
    assert len(S)==55
    first=min(rs)
    assert sum(x<first for x in S)==52
    assert not any(cut<x<first for x in S)
    # Rank of first RS witness is exactly 53, regardless of interval list
    # decimal endpoints or which method produced the source witnesses.
    assert sorted(S).index(first)+1==53
    # A NEW independently certified root may be in a narrow bracket,
    # but without a local count/monotonicity or source-index certificate
    # we cannot deduce it is the same global first RS zero.
    other=F(152)
    assert sorted(S).index(other)+1==54
    alternative_S=set(euler)|{F(1498,10),F(150053524,1000000)}
    new_candidate=F(150053524,1000000)
    assert sum(x<cut for x in alternative_S)==52
    assert sum(x<new_candidate for x in alternative_S)==53
    assert sorted(alternative_S).index(new_candidate)+1==54
    assert F(15005352,100000)<new_candidate<F(15005353,100000)
    # Exact first positive root index "53" follows for source least RS
    # without needing original internal row endpoints.
    print("CP016 EXACT ORIGINAL-FIRST-RS LEAST-ORDINAL-53 MODEL: PASS")
    print("CP016 NEGATIVE CONTROL: numeric narrow candidate may be ordinal54 WITHOUT a separate rank bridge: PASS")
    print("Synthetic zeros are abstract rationals, NOT actual zeta zeros.")


def actual_source_gate(upstream,mathlib,receipt):
    if not SOURCE_016.is_file() or not SOURCE_ATTACH.is_file() or not SOURCE_SEAM.is_file():
        raise ValueError("Missing tracked new Lean source")
    actual={}
    for relative,sha in SHAS.items():
        path=upstream/relative
        got=sha_git_blob(path)
        if got!=sha:
            raise ValueError(f"Original Zeta pinned Git blob mismatch {relative}: {got}")
        actual[relative]=path.read_text("utf-8")
    mp=mathlib/MATHLIB_REL
    if sha_git_blob(mp)!=MATHLIB_SHA:
        raise ValueError("Original Mathlib v4.35 source of Set.exists_min_image changed")
    if "theorem exists_min_image [LinearOrder β]" not in mp.read_text("utf-8"):
        raise ValueError("Missing real Mathlib finite-min image theorem")
    for term,path in [
        ("theorem CertifiedZeroIntervals.zeros_nodup","Zeta/Zeros/Interval.lean"),
        ("theorem CertifiedZeroIntervals.zeros_spec","Zeta/Zeros/Interval.lean"),
        ("theorem riemannZeta.N_gramPoint_eq","Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean"),
        ("theorem riemannZeta.order_eq_one_upto","Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean"),
        ("theorem hardyZ_eq_zero_iff_riemannZeta","Zeta/Zeros/HardyZ.lean"),
    ]:
        if term not in actual[path]:
            raise ValueError(f"Original source API drift: {path}: {term}")
    source=SOURCE_016.read_text("utf-8")
    attached=SOURCE_ATTACH.read_text("utf-8")
    seam=SOURCE_SEAM.read_text("utf-8")
    for target in [
        "theorem exists_least_original_RS_witness",
        "theorem original_roots_below_least_RS_are_exactly_Euler",
        "theorem N_at_original_least_RS_root_eq_52",
        "theorem original_53rd_positive_zeta_zero_exists",
        "theorem original_first_RS_zero_has_no_preceding_zero",
        "theorem original_least_RS_root_unique",
    ]:
        if target not in source:
            raise ValueError("Missing first-RS exact ordinal Lean source theorem "+target)
    for target in [
        "theorem refined_critical_root_is_RS_source_witness",
        "theorem refined_root_equals_original_53rd_of_hardy_monotone",
        "StrictMonoOn Zeta.hardyZ",
    ]:
        if target not in attached:
            raise ValueError("Missing explicit Hardy Z and new narrow-root conditional theorem "+target)
    if "private theorem eulerCutLtGram" not in seam or "exact eulerCutLtGram" not in seam:
        raise ValueError("Previously incorrect CP015 non-strict 149.5 root membership has not been repaired")
    for file,body in [(SOURCE_016,source),(SOURCE_ATTACH,attached)]:
        if "\nsorry\n" in body or "\naxiom " in body:
            raise ValueError("New Lean source has explicit sorry or additional axiom declaration "+str(file))
    receipt.write_text(json.dumps({
        "status":"CP016_PINNED_SOURCE_AND_ORDINAL_MODEL_PASS_NOT_LEAN",
        "original_zeta_sha":COMMIT,
        "original_source_blobs":SHAS,
        "original_mathlib_ref":MATHLIB_REF,
        "mathlib_minimum_source_sha":MATHLIB_SHA,
        "original_source_low_euler_count":52,
        "original_source_RS_only_count":1747950,
        "canonical_53rd_abstract_root_identification":"CP016FirstRSRank LEAN SOURCE CANDIDATE ONLY",
        "new_1495_strict_open_gram_repair":"SOURCE REVIEW PASS NOT LEAN",
        "narrow_candidate_same_root":"UNPROVED",
        "hardyZ_strict_mono_full_interval":"UNPROVED",
        "CP010_Euler_narrow_sign_certificate":"UNPROVED",
        "new_Lean_olean":None,
        "original_signed_Weil_spectral_equality":False
    },indent=2)+"\n","utf-8")
    print("CP016 PINNED SOURCE API AND STRICT-GRAM REPAIR: PASS — NOT LEAN KERNEL")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--upstream",type=Path)
    p.add_argument("--mathlib",type=Path)
    p.add_argument("--receipt",type=Path,default=Path("cp016-first-original-RS-ordinal-source.json"))
    a=p.parse_args()
    if bool(a.upstream)!=bool(a.mathlib):
        raise SystemExit("NOT_READY: source gate requires BOTH original pinned Zeta and original pinned mathlib")
    if a.self_test:
        abstract_ordinal_model()
    if a.upstream:
        try:
            actual_source_gate(a.upstream,a.mathlib,a.receipt)
        except (ValueError,OSError,UnicodeError,KeyError) as e:
            raise SystemExit("NOT_READY: "+str(e))
    if not (a.self_test or a.upstream):
        p.print_help()


if __name__=="__main__":
    main()
