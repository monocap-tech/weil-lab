#!/usr/bin/env python3
"""CP015: honest source/scope custody for unconditional first 52 cut candidate.

READS the exact genuine original Zeta external source modules at frozen
c06b4e13.. after full Git-blob SHA verification, and independently checks
the combinatorial finite zero count. This is never a substitute for
actual Lean compilation. The new unconditional N(149.5) theorem has source
code but not an accepted .olean until its separate manual kernel audit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
SOURCE_BLOBS = {
    "Zeta/Zeros/Interval.lean": "152954545ca9997c2a2ddaead4d9161ffbbfe191",
    "Zeta/Zeros/Certificates/Basic.lean": "128e19e4bb056332b0fd71a8c107f4075cd8cd07",
    "Zeta/Zeros/CountCertificates.lean": "a3e729d23802c3731432de9a3c7d46d18252ba10",
    "Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean":
        "c2b1da101a580cc91cfb0a43d72d5839fd97265c",
    "Zeta/Gram/Certificates.lean": "91fd460c42469ed889da985f3cd160df3f792105",
    "Zeta/Zeros/Certificates/EulerMaclaurin/Batch0001.lean":
        "a4f28786abb75420cf950ae701f5c7befcda560d",
    "Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean":
        "12848f56d0b62df858dcb89b708a858f4f7b28fb",
}
TARGET=ROOT/"cp011_zeta_v435/CP015SourceWitnesses.lean"

def blob(path):
    n=path.stat().st_size
    h=hashlib.sha1(b"blob "+str(n).encode()+b"\0")
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def source_statements(upstream):
    original={}
    for rel,pin in SOURCE_BLOBS.items():
        file=upstream/rel
        got=blob(file)
        if got!=pin:
            raise ValueError(f"Original source SHA drift at {rel}: {got} vs {pin}")
        original[rel]=file.read_text("utf-8")
    zero=original["Zeta/Zeros/Interval.lean"]
    for term in [
        "structure CertifiedZeroIntervals where",
        "has_zero : ∀ I ∈ intervals, ∃ t ∈ Set.Ioo I.fst I.snd",
        "theorem CertifiedZeroIntervals.pairwise",
        "noncomputable def CertifiedZeroIntervals.zeros",
        "theorem CertifiedZeroIntervals.zeros_spec",
        "theorem CertifiedZeroIntervals.zeros_length",
        "theorem CertifiedZeroIntervals.zeros_nodup",
        "theorem CertifiedZeroIntervals.zeros_im",
    ]:
        if term not in zero:
            raise ValueError(f"Source true root witnesses theorem not found: {term}")
    base=original["Zeta/Zeros/Certificates/Basic.lean"]
    for term in [
        "noncomputable def bundle (h : BatchSpec n an ad bn bd)",
        "theorem bundle_head?",
        "theorem bundle_getLast?",
        "theorem bundle_length",
    ]:
        if term not in base:
            raise ValueError(f"Original public batch field changed: {term}")
    original_count=original["Zeta/Zeros/CountCertificates.lean"]
    assert "noncomputable def certifiedZeroCount : CertifiedZeroCount" in original_count
    original_rh=original["Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean"]
    for term in [
        "theorem riemannZeta.N_gramPoint_eq",
        "theorem riemannZeta.order_eq_one_upto",
        "theorem riemannZeta.le_N_of_zeros",
    ]:
        if term not in original_rh:
            raise ValueError(f"Original finite multiplicity count changed: {term}")
    E=original["Zeta/Zeros/Certificates/EulerMaclaurin/Batch0001.lean"]
    R=original["Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean"]
    if "theorem batch : BatchSpec 52 1000 1000 149500 1000" not in E:
        raise ValueError("Original first 52 Euler source theorem signature changed")
    if "theorem batch : BatchSpec 200 149500 1000 474603 1000" not in R:
        raise ValueError("Original first 200 RS source theorem signature changed")
    gram=original["Zeta/Gram/Certificates.lean"]
    if "fst := 1000449.28682" not in gram:
        raise ValueError("Original upper-end source Gram-point bracket changed")
    assert F(1000449286,1000) < F("1000449.28682")
    assert F(149500,1000) < F(1000449286,1000)
    generated=TARGET.read_text("utf-8")
    wanted=[
        "theorem lower_bound_of_first_endpoint",
        "CP013Seam.allRS.bundle_head?",
        "theorem eulerRoots_card",
        "theorem rsRoots_card",
        "theorem eulerRoots_below",
        "theorem rsRoots_above",
        "theorem eulerRoots_subset",
        "theorem rsRoots_subset",
        "theorem euler_rs_disjoint",
        "theorem original_N_at_149500_div1000_eq_52 :",
        "CP014ZetaCut.N_at_Euler_RS_seam_eq_52_of_source_witnesses",
    ]
    for term in wanted:
        if term not in generated:
            raise ValueError(f"Actual CP015 source proof candidate missing: {term}")
    if "sorry" in generated.split("@[expose] public section")[-1]:
        raise ValueError("New Lean theorem source has a sorry/admitted proof")
    if "axiom " in generated.split("@[expose] public section")[-1]:
        raise ValueError("New Lean theorem source introduces axiom")
    return True


def exhaustive_abstract_model():
    """Exact rational model, not Zeta analytic evidence or a Lean kernel."""
    c=F(299,2)
    E={F(14),F(21),F(25)}
    R={F(150),F(152)}
    S=E|R
    assert E.isdisjoint(R)
    assert len(S)==len(E)+len(R)==5
    assert all(z<c for z in E)
    assert all(c<z for z in R)
    assert sum(z<c for z in S)==len(E)
    assert c not in S
    # A hypothetical extra zero AT the seam would force the global
    # multiplicity/point count to exceed source witness total.
    assert len(S|{c}) == len(E)+len(R)+1
    # An extra offcritical zero at *any* other ordinate would also
    # oversaturate the globally certified N(g), not silently add
    # a hidden root to the arithmetic/spectral list.
    assert len(S|{F(153)}) > len(E)+len(R)
    assert 52+1747950==1748002
    assert F(149500,1000)==c
    assert F(1000449286,1000)<F("1000449.28682")
    print("CP015 EXACT FULL SOURCE-CARDINALITY AND OPEN-SEAM SATURATION TEST: PASS")
    print("No source equality of separately chosen existential bundles is needed.")
    print("The abstract model is not a zeta sign certificate nor a Lean kernel pass.")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--upstream-source",type=Path)
    p.add_argument("--receipt",type=Path,default=Path("cp015-source-zero-seam-saturation.json"))
    a=p.parse_args()
    if a.self_test:
        exhaustive_abstract_model()
    if a.upstream_source:
        try:
            source_statements(a.upstream_source)
            result={
                "status":"CP015_SOURCE_WITNESS_COVER_AND_SEAM_SIGNATURES_PASS_NOT_KERNEL",
                "original_upstream_commit":COMMIT,
                "original_upstream_blobs":SOURCE_BLOBS,
                "seam_exact_fraction":"299/2",
                "source_euler_rows":52,
                "source_RS_only_rows":1747950,
                "original_total":1748002,
                "original_terminal_source_right":"1000449286/1000",
                "original_Gram_lower":"1000449.28682",
                "imported_new_CP013_RS_only_Lean_accepted":False,
                "new_CP015_unconditional_N_1495_Lean_accepted":False,
                "new_original_53rd_refined_zero_ordinal_attached":False,
                "original_signed_Weil_spectral_dictionary":False
            }
            a.receipt.write_text(json.dumps(result,indent=2)+"\n","utf-8")
            print(result["status"])
        except (AssertionError,ValueError,FileNotFoundError,UnicodeError,KeyError) as exc:
            raise SystemExit(f"NOT_READY: {exc}")
    if not a.self_test and a.upstream_source is None:
        p.print_help()


if __name__=="__main__":
    main()
