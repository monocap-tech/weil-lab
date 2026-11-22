#!/usr/bin/env python3
"""NF772 real original HD/A index-zero 136..143 Lean proof-audit candidate.

This can run ONLY after authentic NF737 source restoration, NF743 original
cache ingestion, eight direct .olean compilations, source-pinned predecessor
custody and all 35 direct standard-only #print axioms. Its output is a local
kernel receipt, not independent historical-archive acceptance.
"""
import hashlib, json, re
from pathlib import Path

import nf772_original_indexzero_136_143_source_preflight as d
from nf708_global_matrix_attachment_driver import ALLOWED
from nf772_original_indexzero_import_order_guard import (
    RECEIPT as ORDER_RECEIPT, ORDER, ROOT, OBJECTS, check_order
)

OUT = Path("nf772-original-indexzero-136-143-kernel-audit.json")
TIMING = Path("nf772-indexzero-gates-time.log")
OBJECT_DIR = Path(".lake/build/lib/lean/WeilDefect/Generated/NF704Frontier")
CACHE_RECEIPT = Path("nf743-accepted-original-center-cache-reuse.json")
PRIOR_596 = Path("nf748-original-596-accepted-gate-rollforward.json")
PRIOR_692 = Path("nf768-accepted-prior-692-kernel-custody.json")
PRIOR_724 = Path("nf770-accepted-prior-724-kernel-custody.json")
PRIOR_740 = Path("nf771-prior740-live-metadata.json")
PRIOR_756 = Path("nf772-prior756-live-metadata.json")

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def record(path):
    assert path.is_file() and path.stat().st_size > 0, path
    return json.loads(path.read_text())

def compiled_objects():
    rows = TIMING.read_text().splitlines()
    assert rows, "Direct per-column lake env lean timing trace required"
    hashes = {}
    for i in range(136, 144):
        name = f"Col{i:03d}"
        src = d.SOURCE / (name + ".lean")
        obj = OBJECT_DIR / (name + ".olean")
        assert src.is_file() and obj.is_file() and obj.stat().st_size > 0, name
        matches = [r for r in rows if re.search(rf"\b{name}\.lean\b", r)
                   and "exit=0" in r and "lake env lean" in r]
        assert len(matches) == 1, ("Direct source-bound compiler receipt missing or duplicated", name, matches)
        hashes[name + ".olean"] = sha(obj)
    assert len(hashes) == 8 and len(set(hashes.values())) == 8
    return hashes, sha(TIMING)

def strict_axiom_receipt():
    expected = ["import WeilDefect.Generated.NF704Frontier.Common"] + [
        f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}" for i in range(136,144)
    ] + [f"#print axioms WeilDefect.{n}" for n in d.NAMES]
    assert d.AXFILE.read_text() == "\n".join(expected) + "\n", "Axiom query source mutated"
    log = d.AXLOG.read_text()
    found = {}
    for name, values in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if name in d.NAMES:
            assert name not in found
            found[name] = [t.strip() for t in values.split(",") if t.strip()]
    for name in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if name in d.NAMES:
            assert name not in found
            found[name] = []
    assert set(found) == set(d.NAMES) and len(found) == 35, (set(d.NAMES)-set(found), len(found))
    assert all(set(values) <= ALLOWED for values in found.values())
    assert not re.search(r"\berror:|sorryAx|declaration uses `sorry`", log, re.I)
    return found

def audit():
    full, hashes = d.authentic_source()
    b = record(d.BIND)
    assert b["schema"] == "NF772-authentic-original-global-indexzero-136-143-source-v1"
    assert b["upstream_full_schedule_sha256"] == sha(d.source737.BIND)
    assert b["original_full_source_manifest_sha256"] == sha(d.SOURCE/"manifest.json")
    assert b["source_global_common_sha256"] == sha(d.SOURCE/"Common.lean")
    assert b["accepted_first_24_original_source_module_hashes"] == full["accepted_prior_source_module_hashes"]
    assert b["actual_original_new_col_module_sha256"] == hashes
    assert b["new_indices_HD"] == b["new_indices_A"] == list(range(136, 144))
    assert b["new_gate_instances"] == 16 and b["new_declarations"] == 32
    assert b["strict_axiom_names"] == d.NAMES and b["new_numerical_kernel_accepted"] is False

    cache = record(CACHE_RECEIPT)
    assert cache["schema"] == "NF743-original-cache-source-equal-to-NF728-accepted-lean-object-v1"
    assert cache["source_manifest_sha256"] == sha(d.SOURCE/"manifest.json")
    assert cache["verified_against_original_NF728_complete_source_bank"] is True
    assert cache["cache_source_families_exactly_verified"] == ["NF702Inputs","NF703Cache"]
    assert cache["accepted_NF729_original_numeric_quad_000_job_success"] is True
    assert cache["accepted_NF729_compiled_olean_source_match"] is True
    assert cache["accepted_compiled_original_center_modules"] >= 1
    assert cache["current_NF737_NF681_local_source_files"] >= 242
    assert cache["NF681_local_corpus_distinct_from_cache_reuse_claim"] is True

    order = record(ORDER_RECEIPT)
    assert order["schema"] == "NF772-source-actual-original-indexzero-136-143-import-DAG-v1"
    assert order["compiler_order"] == list(ORDER)
    assert order["actual_recovered_Frontier_depends_on_NF681_Common"] is True
    assert order == check_order(ROOT, OBJECTS, ORDER), "Import dependencies changed after authentic plan"

    base = record(PRIOR_596)
    assert base["schema"] == "NF748-live-accepted-original-HD-A-596-kernel-rollforward-v1"
    assert base["original_gate_instances_accepted"] == 596
    prior692 = record(PRIOR_692)
    assert prior692["schema"] == "NF768-original-prior-692-live-six-batch-custody-v1"
    assert prior692["accepted_original_HD_A_gate_instances"] == 692
    prior724 = record(PRIOR_724)
    assert prior724["schema"] == "NF770-original-prior-724-live-eight-batch-custody-v1"
    assert prior724["accepted_original_HD_A_gate_instances"] == 724
    assert prior724["accepted_original_indexzero_positions_HD"] == list(range(120))
    assert prior724["accepted_original_indexzero_positions_A"] == list(range(120))
    prior740 = record(PRIOR_740)
    assert prior740["schema"] == "NF771-live-NF770-740-metadata-nonpromoting-v1"
    assert prior740["previous_accepted_original_HD_A_gates"] == 740
    assert prior740["previous_source_bound_artifact_id"] == 14743614902
    assert prior740["previous_archive_metadata_sha256"] == "8c33bdcfa7a1cc1b1fc26371a3a335eeb159a844107097045f14fbdace15ab54"
    assert prior740["new_indexzero_HD_candidate"] == prior740["new_indexzero_A_candidate"] == list(range(128,136))
    assert prior740["new_original_Lean_gates_accepted"] is False

    prior756 = record(PRIOR_756)
    assert prior756["schema"] == "NF772-live-NF771-756-metadata-nonpromoting-v1"
    assert prior756["previous_accepted_original_HD_A_gates"] == 756
    assert prior756["previous_source_bound_artifact_id"] == 14763746318
    assert prior756["previous_archive_metadata_sha256"] == "5726980f4b3d342fc6a41224e0c3840ac17231ef5d0d69b0429608a35a19eebb"
    assert prior756["new_indexzero_HD_candidate"] == prior756["new_indexzero_A_candidate"] == list(range(136,144))
    assert prior756["new_original_Lean_gates_accepted"] is False
    objs, timing_sha = compiled_objects()
    ax = strict_axiom_receipt()
    final = dict(b)
    final.update({
        "schema": "NF772-genuine-original-global-indexzero-136-143-local-Lean-kernel-audit-v1",
        "actual_eight_direct_olean_sha256": objs,
        "actual_direct_compiler_timing_sha256": timing_sha,
        "actual_35_named_standard_axioms": ax,
        "actual_axiom_log_sha256": sha(d.AXLOG),
        "actual_exact_axiom_source_sha256": sha(d.AXFILE),
        "NF737_full_source_schedule_sha256": sha(d.source737.BIND),
        "accepted_NF743_source_identical_original_cache_sha256": sha(CACHE_RECEIPT),
        "accepted_original_predecessor_596_sha256": sha(PRIOR_596),
        "accepted_original_predecessor_692_sha256": sha(PRIOR_692),
        "accepted_original_predecessor_724_sha256": sha(PRIOR_724),
        "accepted_original_predecessor_740_metadata_sha256": sha(PRIOR_740),
        "accepted_original_predecessor_756_metadata_sha256": sha(PRIOR_756),
        "source_bound_compiler_import_order_sha256": sha(ORDER_RECEIPT),
        "candidate_new_HD_indices_Lean_local_audit_PASS": list(range(136, 144)),
        "candidate_new_A_indices_Lean_local_audit_PASS": list(range(136, 144)),
        "local_combined_gate_count_if_independently_reconciled": 772,
        "actual_original_direct_Lean_compiler_and_axioms_passed": True,
        "independent_postrun_artifact_zip_reconciliation_done": False,
        "F41_complete_original_242x242_physical_matrix_proved": False,
        "F42_literal_original_signed_Weil_form_proved": False,
        "global_Weil_positivity_proved": False,
        "RH_proved": False
    })
    OUT.write_text(json.dumps(final, indent=2, sort_keys=True) + "\n")
    print("NF772 136..143: direct Lean eight objects + 35 genuine standard-only named axioms locally AUDITED; separate original ZIP reconciliation required before acceptance.")

if __name__ == "__main__":
    audit()
