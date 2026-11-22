# F40 NF776 candidate: no Lean execution or new acceptance.
#!/usr/bin/env python3
"""NF776: authenticate and independently kernel-certify genuine ORIGINAL NF702/NF703
matrix index-zero HD row 0 / A column 0 coordinates 168..175.

This is a SOURCE-ONLY prospective certification preparation, using the FULL
immutable NF737 source schedule. The NF734 24..31, NF737 32..39 and NF739 40..47 and NF742 48..55 pilots
are explicitly NOT prerequisites or assumed accepted. The old accepted
0..23 source is validated by NF737's SHA-pinned 242-column source audit.

No compiler, axiom audit or acceptance is performed here. Actual compiled
Lean objects and a complete exact 35-name axiom log remain separately due.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import nf737_original_indexzero_complete_source_shard_schedule as source737
from nf708_global_matrix_attachment_driver import ALLOWED, theorem_names

FIRST, STOP = 168, 176
N = 242
SOURCE = Path("WeilDefect/Generated/NF704Frontier")
INPUT = Path("WeilDefect/Generated/NF702Inputs")
CACHE = Path("WeilDefect/Generated/NF703Cache")
LOCAL = Path("WeilDefect/Generated/NF681")
BIND = Path("nf776-indexzero-168-175-source-binding.json")
AXFILE = Path("nf776OriginalIndexZero168Audit.lean")
AXLOG = Path("nf776-original-indexzero-168-175-axioms.log")
RESULT = Path("nf776-original-indexzero-168-175-kernel-audit.json")
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
        "schema":"NF776-authentic-original-global-indexzero-168-175-source-v1",
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
        "nf743_056_063_accepted_by_this_stage":False,
        "full_indexzero_universal_accepted":False,
        "full_global_matrix_accepted":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
        "scope":"Source-only until real Lean original NF702/NF703 numerical theorem build, all 35 strict axioms, and independent source audit succeed."
    }
    BIND.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print("NF776 ORIGINAL 168..175: 16 prospective HD/A gates, 35 axiom queries; NO NEW KERNEL ACCEPTANCE")


if __name__ == "__main__":
    import subprocess
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip() == "a431f903254000bb5ad8edbc276ccc8599da98f5", "Immutable NF769 research source checkout required"
    prepare()
