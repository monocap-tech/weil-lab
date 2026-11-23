#!/usr/bin/env python3
"""F41-001: audit literal immutable original H/V entry-certification contracts.

This is a SOURCE-ONLY custody/obligation enumerator. It cannot assert any
data-dependent Boolean check, physical enclosure, positivity, or RH.
"""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

ORIGINAL_SHA = "a431f903254000bb5ad8edbc276ccc8599da98f5"
N = 242
MIXED_WIDTH = 4
SCHEMA = "F41-001-immutable-original-physical-HV-entry-contract-nonpromoting-v1"

# Names and declarations from the frozen source, not invented F40 extrapolations.
REQUIRED = {
    "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalSolveResidual.lean": (
        "def neutralNF606PhysicalH (i j : Fin 242) : ℝ :=",
        "def neutralNF606PhysicalV (i : Fin 242) (j : Fin 4) : ℝ :=",
        "theorem neutralNF606PhysicalH_symm (i j : Fin 242) :",
        "def neutralNF606TransformedH (D : Fin 242 → Fin 242 → ℝ)",
        "def neutralNF606TransformedRHS (D : Fin 242 → Fin 242 → ℝ)",
    ),
    "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalExecutableEntryChecks.lean": (
        "def neutralNF673LowerHEntryCheck",
        "if j.val ≤ i.val then neutralNF625EntryHCheck M p i j else true",
        "def neutralNF673CenterSymmetryCheck",
        "decide (p.H0 i j = p.H0 j i)",
        "def neutralNF673MixedVEntryCheck",
        "(List.finRange 4).all (neutralNF625EntryVCheck M p i)",
        "def neutralNF673EntryCheck",
        "def neutralNF674OriginalRowCheck (M : NF622Moments)",
        "neutralNF674LowerRow M p i",
        "neutralNF674CenterRow p i",
        "neutralNF674MixedRow M p i",
    ),
    "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalTriangularEntryCustody.lean": (
        "theorem neutralNF673EntryCheck_sound",
        "(hM : neutralNF624AllMomentsSound M)",
        "theorem neutralNF673OriginalPhysical_of_triangular_fast_checks",
        "(hbank : neutralNF624BankCheck bank = true)",
        "(hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)",
        "(htri : neutralNF673EntryCheck",
        "(hcache : c.check s = true)",
        "(hpay : c.fastPayCheck s = true)",
    ),
    "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalShardedEntryCustody.lean": (
        "theorem neutralNF674Rows_imply_original_entry",
        "theorem neutralNF674Rows_iff_original_entry",
        "theorem neutralNF674Rows_sound",
        "(hrows : ∀ i : Fin 242,",
        "neutralNF674OriginalRowCheck M p i = true",
    ),
    "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalEnclosurePropagation.lean": (
        "theorem neutralNF613Gram_enclosure",
        "theorem neutralNF613RHS_enclosure",
        "theorem neutralNF613Rows_of_enclosures",
        "theorem neutralNF613Residual_of_enclosures",
    ),
    "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalIntegerCenters.lean": (
        "structure NF626ScaledInputs where",
        "structure NF626CenterCache where",
        "def NF626CenterCache.HDGate",
        "def NF626CenterCache.AGate",
        "def NF626CenterCache.check",
        "theorem NF626CenterCache.check_sound",
    ),
    "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramSchurAlgebra.lean": (
        "theorem neutralNF669Schur_completion",
        "theorem neutralNF669Schur_sufficient",
        "theorem neutralNF669Schur_necessary",
    ),
}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def verify_texts(texts):
    assert set(texts) == set(REQUIRED), "Exact original source inventory changed"
    for path, tokens in REQUIRED.items():
        data = texts[path]
        assert isinstance(data, str) and data.strip(), path
        for token in tokens:
            assert data.count(token) == 1, (path, "missing/duplicated exact source anchor", token)
    full = texts["WeilDefect/Arithmetic/ActualZetaOriginalPhysicalExecutableEntryChecks.lean"]
    assert "neutralNF673LowerHEntryCheck M p &&" in full
    assert "neutralNF673CenterSymmetryCheck p) &&" in full
    assert "neutralNF673MixedVEntryCheck M p" in full
    return True

def entries():
    rows = []
    lower = 0
    for i in range(N):
        h = i + 1
        lower += h
        rows.append({
            "original_source_row": i,
            "H_lower_triangle_comparisons_required": h,
            "H_proposed_center_symmetry_checks_in_row": N,
            "V_mixed_entry_comparisons_required": MIXED_WIDTH,
            "data_dependent_row_check_accepted_by_this_audit": False,
        })
    assert len(rows) == N
    assert lower == N * (N + 1) // 2 == 29403
    assert sum(r["V_mixed_entry_comparisons_required"] for r in rows) == 968
    assert sum(r["H_proposed_center_symmetry_checks_in_row"] for r in rows) == N * N
    return rows

def receipt(root):
    root = Path(root)
    assert root.is_dir(), root
    git = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()
    assert git == ORIGINAL_SHA, ("historical original source pin changed", git)
    texts = {}
    hashes = {}
    for name in REQUIRED:
        p = root / name
        assert p.is_file() and p.stat().st_size > 0, name
        texts[name] = p.read_text(encoding="utf-8")
        hashes[name] = sha(p)
    verify_texts(texts)
    rows = entries()
    return {
        "schema": SCHEMA,
        "historical_original_immutable_source_commit": ORIGINAL_SHA,
        "source_sha256": hashes,
        "source_anchor_checks": sum(map(len, REQUIRED.values())),
        "F40_original_HD_A_axis_gate_inventory_accepted_by_prior_independent_custody": 968,
        "F40_claim_reverified_by_this_source_only_run": False,
        "F40_HD_A_gate_space_distinct_from_physical_H_V_enclosures": True,
        "physical_H_full_entries": N * N,
        "physical_H_independent_lower_triangle_entry_comparisons": N * (N + 1) // 2,
        "physical_V_full_mixed_entries": N * MIXED_WIDTH,
        "rational_center_symmetry_checks_at_literal_original_source": N * N,
        "literal_original_H_symmetry_Lean_theorem_source_present": True,
        "source_specific_HV_rows_to_certify": rows,
        "row_wise_entry_check_predicate": "neutralNF674OriginalRowCheck",
        "row_cover_implies_global_check_theorem": "neutralNF674Rows_imply_original_entry",
        "original_integral_entry_soundness_theorem": "neutralNF673EntryCheck_sound",
        "additional_data_dependent_predicates_due": [
            "neutralNF624BankCheck",
            "neutralNF624CoverageCheck",
            "neutralNF674OriginalRowCheck (all 242 original rows)",
            "NF626CenterCache.check",
            "NF626CenterCache.fastPayCheck",
        ],
        "analytical_original_moment_soundness_due": True,
        "historical_D_and_original_HV_entry_center_radius_binding_due": True,
        "inverse_residual_perturbation_and_conditioning_checks_due": True,
        "data_dependent_full_HV_entry_check_proved": False,
        "physical_full_matrix_certified": False,
        "original_signed_Weil_form_attached": False,
        "support_independent_positivity_proved": False,
        "RH_proved": False,
        "scope": "F41 source-contract inventory only; no Lean compilation or Boolean truth promotion",
    }

def selftest():
    assert len(entries()) == 242
    assert sum(r["H_lower_triangle_comparisons_required"] for r in entries()) == 29403
    synthetic = {path: "\n".join(tokens) for path, tokens in REQUIRED.items()}
    # The production executable-source composition is not fabricated as true:
    k = "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalExecutableEntryChecks.lean"
    synthetic[k] += ("\nneutralNF673LowerHEntryCheck M p &&"
                     "\nneutralNF673CenterSymmetryCheck p) &&"
                     "\nneutralNF673MixedVEntryCheck M p\n")
    verify_texts(synthetic)
    p = "WeilDefect/Arithmetic/ActualZetaOriginalPhysicalTriangularEntryCustody.lean"
    bad = dict(synthetic)
    bad[p] = bad[p].replace("(htri : neutralNF673EntryCheck",
                            "(htri : SOME_UNCHECKED_BOOLEAN")
    try:
        verify_texts(bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("missing original physical triangular gate falsely accepted")
    bad = dict(synthetic)
    bad[k] = bad[k].replace("if j.val ≤ i.val then neutralNF625EntryHCheck M p i j else true",
                          "if j.val ≤ i.val then true else true")
    try:
        verify_texts(bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("unconditional lower-triangle truth falsely accepted")
    bad = dict(synthetic)
    bad.pop("WeilDefect/Arithmetic/ActualZetaOriginalPhysicalShardedEntryCustody.lean")
    try:
        verify_texts(bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("missing source row-cover theorem falsely accepted")
    print("F41-001 242-row ledger, real-source contract anchors and 3 synthetic refusals PASS; NO NEW LEAN")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["selftest", "source"])
    ap.add_argument("--source-root", default="original")
    ap.add_argument("--out", default="f41-001-original-physical-HV-contract.json")
    args = ap.parse_args()
    if args.stage == "selftest":
        selftest()
    else:
        data = receipt(args.source_root)
        Path(args.out).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        print("F41-001 original SHA-pinned H/V source-contract PASS:",
              data["physical_H_independent_lower_triangle_entry_comparisons"],
              "H lower comparisons,",
              data["physical_V_full_mixed_entries"], "V comparisons,",
              "242 check rows, ZERO new numerical certification")

if __name__ == "__main__":
    main()
