#!/usr/bin/env python3
"""IV024 independent Phase IV SOURCE-CHAIN and proof-frontier custody.

Why this exists:
  GitHub Actions original IV009 repair and IV018–IV023 full Lean runs
  were still QUEUED/PENDING at IV024 inspection. A syntactically
  impressive Lean proof source is NOT a proved theorem. This script
  inventories every original mathematical source stage IV009 and
  IV017–IV023, validates exact local theorem/axiom print target
  custody and the true named original imported source paths, and
  emits a SHA-256 source receipt that unambiguously says NOT KERNEL.

It neither runs Lean nor fabricates CI success. Existing per-stage
pinned workflows and rigorous real standard-only axiom auditors remain
the ONLY path to claims of kernel acceptance.

RUN FROM REPO ROOT:
  python scripts/iv024_phaseiv_source_chain_gate.py

The independent IV024 arithmetic prime-graph sentry is separate and
has its own exact Fraction proof/counterfactual controls.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path("WeilDefect/Arithmetic")
RECEIPT=Path("iv024-source-chain-readiness-only-NOT-LEAN.json")
STAGES={
 "IV009":("ActualZetaPhaseIVOriginalSchwartzPolarization.lean",),
 "IV017":(
   "ActualZetaPhaseIVOriginalNarrowSignedGamma.lean",
   "ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity.lean"),
 "IV018":(
   "ActualZetaPhaseIVOriginalThreeCellSignedEnvelope.lean",
   "ActualZetaPhaseIVOriginalThreeCellPrime9Transfer.lean"),
 "IV019":(
   "ActualZetaPhaseIVOriginalVariableWidthSignedBudget.lean",
   "ActualZetaPhaseIVOriginalWiderPrimeFreeBump.lean"),
 "IV020":(
   "ActualZetaPhaseIVOriginalWiderThreeCellSourceMeasure.lean",
   "ActualZetaPhaseIVOriginalWiderThreeCellPrime9Coercivity.lean"),
 "IV021":("ActualZetaPhaseIVOriginalWholeThreeCellSchwartzPartition.lean",),
 "IV022":(
   "ActualZetaPhaseIVOriginalSecondNewCellPrimeGeometry.lean",
   "ActualZetaPhaseIVOriginalFourCellSignedCapacity.lean"),
 "IV023":(
   "ActualZetaPhaseIVOriginalFourCellSmoothSchwartzPartition.lean",
   "ActualZetaPhaseIVOriginalFourCellPrimeTransferCoercivity.lean"),
}
ACTIVE_RUNS_AT_IV024_INSPECTION={
 "IV009":"44850887402",
 "IV018":"44850967574",
 "IV019":"44851439481",
 "IV020":"44851946887",
 "IV021":"44852596209",
 "IV022":"44853338807",
 "IV023":"44854690456",
}
INITIAL_INSPECTION_STATUS={
 "IV009":"queued",
 "IV018":"pending",
 "IV019":"queued",
 "IV020":"queued",
 "IV021":"queued",
 "IV022":"queued",
 "IV023":"queued",
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def inspect():
    report={}
    assert len(set(p for v in STAGES.values() for p in v))==sum(map(len,STAGES.values()))
    for stage,filenames in STAGES.items():
        for filename in filenames:
            path=ROOT/filename
            assert path.is_file(),("missing original theorem source",str(path))
            content=path.read_text()
            declared=re.findall(r"^theorem (neutralIV\d+\w+)",content,re.M)
            # Imported theorem anchors appear in the print list as well.
            audited=re.findall(r"^#print axioms (\w+)$",content,re.M)
            assert declared,("no actual source theorems",str(path))
            assert len(audited)==len(set(audited)),("duplicate axiom receipt",str(path))
            for name in declared:
                assert name in audited,("missing local strict source axiom target",str(path),name)
            assert not re.search(
              r"^\s*(?:axiom|sorry|admit|unsafe)\b",content,re.M
            ),("local unaccepted declaration/tactic",str(path))
            assert not re.search(r"\bsorryAx\b",content),("local forbidden axiom",str(path))
            dep_names=re.findall(
              r"^import WeilDefect\.Arithmetic\.([A-Za-z_][A-Za-z_0-9]*)$",
              content,re.M
            )
            for imported in dep_names:
                dep=ROOT/(imported+".lean")
                assert dep.is_file(),("unresolved actual original arithmetic import",str(path),str(dep))
            report[str(path)]={
              "SHA256_source":sha(path),
              "source_stage":stage,
              "local_theorem_count":len(declared),
              "direct_print_axioms_count":len(audited),
              "all_local_theorems_have_direct_print_axioms":True,
              "local_original_arithmetic_imports":dep_names,
              "actual_Lean_olean_verified":False,
              "standard_only_imported_axioms_verified":False,
              "kernel_certified":False,
            }

    # Check the exact source-specific IV009 repair was inherited into
    # current stacked original source, but DO NOT infer that it compiles.
    s=(ROOT/"ActualZetaPhaseIVOriginalSchwartzPolarization.lean").read_text()
    assert "have hpairFunction :" in s
    assert "neutralWindowCorrelation_rawTransform" in s
    assert "rw [hpairFunction] at hsource" in s
    assert "change Summable (neutralIV009OriginalPairTerm a f g) at hsource" not in s

    # Check prime transfer and signed positivity remain separate
    # named proof targets rather than a naive erased prime term.
    transfer=(ROOT/"ActualZetaPhaseIVOriginalFourCellPrimeTransferCoercivity.lean").read_text()
    signed=(ROOT/"ActualZetaPhaseIVOriginalFourCellSignedCapacity.lean").read_text()
    assert "neutralIV023EveryFourCell_originalPrime_eq_old" in transfer
    assert "neutralIV023WholeFourCellOriginalWeil_oneSixteenth" in transfer
    assert "neutralIV022FourCell_oneSixteenth_of_originalPrime" in signed
    assert "neutralNF600Prime_bound_actual" in transfer
    assert "neutralIV015FrozenConcrete_logCutoff" in transfer

    receipt={
      "schema":"IV024-original-Phase-IV-source-graph-proof-frontier-v1",
      "STAGE_INVENTORY":report,
      "IV009_source_repair_propagated_into_IV023_stack":True,
      "true_original_n9_prime_source_present":True,
      "independent_arithmetic_graph_script":
          "scripts/iv024_original_prime_interaction_graph.py",
      "observed_actions_run_IDs_not_authoritative_forever":ACTIVE_RUNS_AT_IV024_INSPECTION,
      "observed_initial_action_states_not_authoritative_forever":INITIAL_INSPECTION_STATUS,
      "SOURCE_ONLY_PRECHECK_PASS_is_NOT_LEAN_KERNEL":True,
      "actual_compiled_olean_objects_required_to_claim_LEAN_PASS":True,
      "direct_strict_standard_only_axiom_receipts_required":True,
      "IV009_to_IV023_kernel_recovery_completed":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "independent_spectral_equivalence_proved":False,
    }
    RECEIPT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
    print(
      "IV024 SOURCE-ONLY graph gate PASS:",
      len(report),"original source modules audited.",
      "ALL SOURCE LOGIC STILL REQUIRES REAL LEAN KERNEL.",
      "Observed queued/pending Actions are NOT successes."
    )
    return receipt

if __name__=="__main__":
    inspect()
