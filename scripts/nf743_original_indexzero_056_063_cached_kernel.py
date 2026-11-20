#!/usr/bin/env python3
"""NF743: authenticate and independently kernel-certify genuine ORIGINAL NF702/NF703
matrix index-zero HD row 0 / A column 0 coordinates 56..63.

This is an independent eighth-coordinate numerical pilot, using the FULL
immutable NF737 source schedule. The NF734 24..31, NF737 32..39 and NF739 40..47 and NF742 48..55 pilots
are explicitly NOT prerequisites or assumed accepted. The old accepted
0..23 source is validated by NF737's SHA-pinned 242-column source audit.

The 'prepare' phase is source-only; 'verify' requires actual successful
Lean compiles and a complete, exact 35-name #print axioms log.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import nf737_original_indexzero_complete_source_shard_schedule as source737
from nf708_global_matrix_attachment_driver import ALLOWED, theorem_names

FIRST, STOP = 56, 64
N = 242
SOURCE = Path("WeilDefect/Generated/NF704Frontier")
INPUT = Path("WeilDefect/Generated/NF702Inputs")
CACHE = Path("WeilDefect/Generated/NF703Cache")
LOCAL = Path("WeilDefect/Generated/NF681")
BIND = Path("nf743-indexzero-056-063-source-binding.json")
AXFILE = Path("nf743OriginalIndexZero056Audit.lean")
AXLOG = Path("nf743-original-indexzero-056-063-axioms.log")
RESULT = Path("nf743-original-indexzero-056-063-kernel-audit.json")
SHARED = theorem_names(0)
NAMES = SHARED + [
    f"nf704Col{i:03d}{tail}"
    for i in range(FIRST, STOP)
    for tail in ("DGate", "DProjection", "HD", "A")
]
assert len(SHARED) == 3 and len(NAMES) == 35
assert (FIRST, STOP) in source737.SHARDS
assert (FIRST, STOP) != (source737.NUMERICAL_PILOT_FIRST, source737.NUMERICAL_PILOT_END)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def authentic_source():
    """NF737 verifies 3 accepted source/axiom artifacts and ALL 242 source modules."""
    source737.verify()
    old = read(source737.BIND)
    assert old["schema"] == "NF737-original-indexzero-242-complete-global-HD-A-source-schedule-v1",old["schema"]
    assert old["new_original_numeric_kernel_pass"] is False
    assert old["complete_original_indexzero_universal_Lean_PASS"] is False
    assert old["original_indexzero_HD_accepted"] == old["original_indexzero_A_accepted"] == 24
    assert old["distinct_original_indexzero_and_indexone_currently_accepted_gates"] == 532
    assert old["original_global_source_manifest_sha256"] == sha(SOURCE / "manifest.json")
    assert all(x.exists() for x in (INPUT, CACHE, LOCAL))
    files = {}
    for i in range(FIRST, STOP):
        p = SOURCE / f"Col{i:03d}.lean"
        text = p.read_text()
        for tail in ("DGate", "DProjection", "HD", "A"):
            assert re.search(rf"\btheorem nf704Col{i:03d}{tail}\b",text),(i,tail)
        assert f"nf703OriginalCache.HDGate nf702OriginalInputs 0 ({i}:Fin 242) = true" in text
        assert f"nf703OriginalCache.AGate nf702OriginalInputs ({i}:Fin 242) 0 = true" in text
        assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",text,re.M)
        files[p.name] = sha(p)
    return old,files


def prepare():
    old,files=authentic_source()
    imports=["import WeilDefect.Generated.NF704Frontier.Common"]+[
        f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}"
        for i in range(FIRST,STOP)
    ]
    AXFILE.write_text("\n".join(imports+[
       f"#print axioms WeilDefect.{name}" for name in NAMES
    ])+"\n")
    assert AXFILE.read_text().count("#print axioms WeilDefect.")==35
    record={
        "schema":"NF743-authentic-original-global-indexzero-056-063-source-v1",
        "upstream_full_schedule_schema":old["schema"],
        "upstream_full_schedule_sha256":sha(source737.BIND),
        "original_full_source_manifest_sha256":sha(SOURCE/"manifest.json"),
        "source_global_common_sha256":sha(SOURCE/"Common.lean"),
        "accepted_first_24_original_source_module_hashes":
            old["accepted_prior_source_module_hashes"],
        "actual_original_new_col_module_sha256":files,
        "new_indices_HD":list(range(FIRST,STOP)),
        "new_indices_A":list(range(FIRST,STOP)),
        "new_gate_instances":16,
        "new_declarations":32,
        "shared_declarations":SHARED,
        "strict_axiom_names":NAMES,
        "old_indexzero_accepted_HD":list(range(24)),
        "old_indexzero_accepted_A":list(range(24)),
        "old_indexone_universal_HD":True,
        "old_indexone_universal_A":True,
        "cache_reuse_required":True,
        "cache_accepted_receipt_schema":"NF743-original-cache-source-equal-to-NF728-accepted-lean-object-v1",
        "new_numerical_kernel_accepted":False,
        "nf734_024_031_accepted_by_this_stage":False,
        "nf737_032_039_accepted_by_this_stage":False,
        "nf739_040_047_accepted_by_this_stage":False,
        "nf742_048_055_accepted_by_this_stage":False,
        "full_indexzero_universal_accepted":False,
        "full_global_matrix_accepted":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
        "scope":"Source-only until real Lean original NF702/NF703 numerical theorem build, all 35 strict axioms, and independent source audit succeed."
    }
    BIND.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print("NF743 8 HD row-zero + 8 A column-zero ORIGINAL numeric gate CANDIDATES for 056..063; 35 #print axioms prepared; earlier 24 real gates plus index-one universal theorems authenticated; no new kernel acceptance")


def audit():
    assert BIND.exists() and AXFILE.exists() and AXLOG.exists()
    cache_receipt=Path("nf743-accepted-original-center-cache-reuse.json")
    assert cache_receipt.is_file(),"NF743 original accepted compiled center cache SHA/provenance receipt is required"
    cache=json.loads(cache_receipt.read_text())
    assert cache["schema"]=="NF743-original-cache-source-equal-to-NF728-accepted-lean-object-v1"
    assert cache["source_manifest_sha256"]==sha(SOURCE/"manifest.json")
    assert cache["verified_against_original_NF728_complete_source_bank"] is True
    assert cache["accepted_NF729_original_numeric_quad_000_job_success"] is True
    assert cache["accepted_NF729_compiled_olean_source_match"] is True
    assert cache["accepted_compiled_original_center_modules"]>=1

    original,files=authentic_source()
    proposed=read(BIND)
    assert proposed["schema"]=="NF743-authentic-original-global-indexzero-056-063-source-v1"
    assert proposed["upstream_full_schedule_sha256"]==sha(source737.BIND)
    assert proposed["original_full_source_manifest_sha256"]==sha(SOURCE/"manifest.json")
    assert proposed["source_global_common_sha256"]==sha(SOURCE/"Common.lean")
    assert proposed["accepted_first_24_original_source_module_hashes"]==original["accepted_prior_source_module_hashes"]
    assert proposed["actual_original_new_col_module_sha256"]==files
    assert proposed["strict_axiom_names"]==NAMES
    assert proposed["new_numerical_kernel_accepted"] is False
    log=AXLOG.read_text()
    found={}
    for name,values in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log
    ):
        if name in NAMES:
            assert name not in found,name
            found[name]=[x.strip() for x in values.split(",") if x.strip()]
    for name in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms",log
    ):
        if name in NAMES:
            assert name not in found,name
            found[name]=[]
    assert set(found)==set(NAMES),(len(found),set(NAMES)-set(found))
    assert all(set(v) <= ALLOWED for v in found.values()),found
    assert not re.search(r"\berror:",log,re.I)
    assert not re.search(r"sorryAx|declaration uses `sorry`",log,re.I)
    assert len(found)==35
    complete=dict(proposed)
    complete.update({
        "schema":"NF743-authentic-original-global-indexzero-056-063-kernel-audit-v1",
        "new_numerical_kernel_accepted":True,
        "standard_axioms":found,
        "accepted_original_compiled_center_cache_receipt_sha256":sha(cache_receipt),
        "accepted_original_cache_module_count":cache["accepted_compiled_original_center_modules"],
        "cache_original_source_identity_verified":True,
        "axiom_log_sha256":sha(AXLOG),
        "axiom_source_sha256":sha(AXFILE),
        "new_original_HD_row_zero_indices_Lean_PASS":list(range(FIRST,STOP)),
        "new_original_A_col_zero_indices_Lean_PASS":list(range(FIRST,STOP)),
        "independently_evidenced_distinct_global_gate_instances_at_least":548,
        "source_scope":"Actual frozen NF702/NF703 original global numeric gates, old 0..23 and index-one certified; NF734 24..31, NF737 32..39 and NF739 40..47 and NF742 48..55 remain separate"
    })
    RESULT.write_text(json.dumps(complete,indent=2,sort_keys=True)+"\n")
    print("NF743 ORIGINAL HD row-zero 056..063 + A col-zero 056..063: genuine numerical LEAN PASS; 35 theorem strict axioms and source hash audit PASS; 16 NEW source-specific gates, NO indexzero universal or RH")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("stage",choices=("prepare","audit"))
    args=parser.parse_args()
    if args.stage=="prepare":prepare()
    else:audit()
