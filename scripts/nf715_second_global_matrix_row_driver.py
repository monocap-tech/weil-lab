#!/usr/bin/env python3
"""NF715: certify the second actual HD row and A column from NF700 packed receipts.

The NF700 source-specific bounded signed-digit local proofs (527 declarations)
are genuine Lean certificates but not yet global cache identities. This
driver first authenticates the original NF702 input, NF703 full center cache,
NF700 local packed theorem bank, and their exact standard-axiom audits. It
then emits an eight-coordinate block of global projection and product gates
for authentic matrix index 1, using the accepted NF704 packed-receipt bridge.

A generated source file, external checksum, or successful finite replay is
not a kernel proof. The 12 proposed declarations require a full Lean build and
strict axiom audit before claiming any new global identity.
"""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

N = 242
WIDTH = 8
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
MODULE = "WeilDefect.Generated.NF715"
OPTIONS = "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
DECLARATIONS = [
    "nf715HRow1Gate",
    "nf715HRow1Projection",
    "nf715HDCol1Gate",
    "nf715HDCol1Projection",
    "nf715Block000DGate",
    "nf715Block000DProjection",
    "nf715Block000HDTargetGate",
    "nf715Block000HDTargetProjection",
    "nf715Block000ATargetGate",
    "nf715Block000ATargetProjection",
    "nf715Block000GlobalHD",
    "nf715Block000GlobalA",
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def locate(root, name):
    found = sorted(root.rglob(name))
    assert len(found) == 1, (root, name, found)
    return found[0]


def load_stage(root):
    path = locate(root, "manifest.json")
    folder = path.parent
    m = json.loads(path.read_text())
    files = m["files"]
    assert len({x["file"] for x in files}) == len(files)
    for f in files:
        assert sha(folder / f["file"]) == f["sha256"], (folder, f["file"])
    return folder, m


def accept(root, filename, stage, expected, field):
    f = locate(root, filename)
    audit = json.loads(f.read_text())
    assert audit["manifest_sha256"] == sha(stage / "manifest.json")
    assert set(audit[field]) == expected
    assert all(set(v) <= ALLOWED for v in audit[field].values())
    return f, audit


def sources(a):
    ins, sm = load_stage(a.receipts / "input")
    cache, cm = load_stage(a.receipts / "cache-proposals")
    packed, pm = load_stage(a.receipts / "packed-proposals")
    assert sm["rows"] == cm["rows"] == N
    assert (pm["H_source_row"], pm["HD_source_column"]) == (1, 1)
    assert pm["schema"] == "NF700-original-packed-second-matrix-frontier-v1"
    assert pm["HD_exact_external"] == pm["A_exact_external"] == N
    assert len(pm["blocks"]) == 31 and len(pm["files"]) == 32
    assert [j for b in pm["blocks"] for j in range(b["start"], b["stop"])] == list(range(N))
    assert all(len(b["theorems"]) == 17 for b in pm["blocks"])
    assert (pm["blocks"][0]["start"], pm["blocks"][0]["stop"],
            pm["blocks"][0]["module"]) == (0, WIDTH, "Block000")
    for src_field, cache_field, local_field in (
        ("entries_sha256", "entry_sha256", "entry_sha256"),
        ("historical_sha256", "historical_sha256", "historical_sha256"),
        ("payment_sha256", "payment_sha256", "payment_sha256"),
    ):
        assert sm[src_field] == cm[cache_field] == pm[local_field]
    assert cm["cache_sha256"] == pm["cache_sha256"]
    assert sm["source_frame_sha256"] == pm["frame_sha256"]
    assert pm["blocks"][0]["width"] == WIDTH
    first_names = set(pm["blocks"][0]["theorems"])
    assert {"nf700Block000HDAllCoordinates",
            "nf700Block000AAllCoordinates"} <= first_names
    source_expected = {"nf702InputH_symm", "nf702OriginalW"} | {
        x for row in sm["projection_rows"] for x in row["theorems"]
    }
    assert len(source_expected) == 50
    cache_expected = set(cm["audit_theorems"])
    assert len(cache_expected) == 7
    packed_expected = {name for block in pm["blocks"] for name in block["theorems"]}
    assert len(packed_expected) == 527
    receipts = {
        "inputs": accept(a.receipts / "input", "nf702-input-complete-audit.json",
                         ins, source_expected, "axioms"),
        "cache": accept(a.receipts / "cache-audit", "nf703-cache-complete-audit.json",
                        cache, cache_expected, "axioms"),
        "packed": accept(a.receipts / "packed-audit", "nf700-complete-audit.json",
                         packed, packed_expected, "theorems"),
    }
    for src, dest in ((ins, "NF702Inputs"), (cache, "NF703Cache"),
                      (packed, "NF700")):
        target = Path("WeilDefect/Generated") / dest
        assert not target.exists(), target
        shutil.copytree(src, target)
    return {
        "source_manifests": {
            "inputs": sha(ins / "manifest.json"),
            "cache": sha(cache / "manifest.json"),
            "packed": sha(packed / "manifest.json"),
        },
        "accepted_audits": {
            name: sha(record[0]) for name, record in receipts.items()
        },
        "first_local_packed_block": {
            "module": pm["blocks"][0]["module"],
            "theorems": sorted(first_names),
            "source_sha256": sha(packed / "Block000.lean"),
        },
    }


def common_source():
    return """theorem nf715HRow1Gate :
    (List.finRange 242).all (fun k : Fin 242 =>
      decide (nf700HRow1 k = nf702OriginalInputs.H 1 k)) = true := by
  decide +kernel

theorem nf715HRow1Projection :
    nf700HRow1 = nf702OriginalInputs.H 1 :=
  funext (fun k =>
    of_decide_eq_true ((List.all_eq_true.mp nf715HRow1Gate) k (by simp)))

theorem nf715HDCol1Gate :
    (List.finRange 242).all (fun k : Fin 242 =>
      decide (nf700HDCol1 k = nf703OriginalCache.HD k 1)) = true := by
  decide +kernel

theorem nf715HDCol1Projection :
    nf700HDCol1 = (fun k => nf703OriginalCache.HD k 1) :=
  funext (fun k =>
    of_decide_eq_true ((List.all_eq_true.mp nf715HDCol1Gate) k (by simp)))

"""


def block_source():
    return """theorem nf715Block000DGate :
    (List.finRange 8).all (fun j : Fin 8 =>
      (List.finRange 242).all (fun k : Fin 242 =>
        decide (nf700Block000Y k j =
          nf702OriginalInputs.D k (⟨j.val, by omega⟩ : Fin 242)))) = true := by
  decide +kernel

theorem nf715Block000DProjection (j : Fin 8) :
    (fun k => nf700Block000Y k j) =
    (fun k => nf702OriginalInputs.D k (⟨j.val, by omega⟩ : Fin 242)) := by
  funext k
  have hj := (List.all_eq_true.mp nf715Block000DGate) j (by simp)
  exact of_decide_eq_true ((List.all_eq_true.mp hj) k (by simp))

theorem nf715Block000HDTargetGate :
    (List.finRange 8).all (fun j : Fin 8 =>
      decide (nf700Block000HDTarget j =
        nf703OriginalCache.HD 1 (⟨j.val, by omega⟩ : Fin 242))) = true := by
  decide +kernel

theorem nf715Block000HDTargetProjection (j : Fin 8) :
    nf700Block000HDTarget j =
      nf703OriginalCache.HD 1 (⟨j.val, by omega⟩ : Fin 242) :=
  of_decide_eq_true ((List.all_eq_true.mp nf715Block000HDTargetGate) j (by simp))

theorem nf715Block000ATargetGate :
    (List.finRange 8).all (fun j : Fin 8 =>
      decide (nf700Block000ATarget j =
        nf703OriginalCache.A (⟨j.val, by omega⟩ : Fin 242) 1)) = true := by
  decide +kernel

theorem nf715Block000ATargetProjection (j : Fin 8) :
    nf700Block000ATarget j =
      nf703OriginalCache.A (⟨j.val, by omega⟩ : Fin 242) 1 :=
  of_decide_eq_true ((List.all_eq_true.mp nf715Block000ATargetGate) j (by simp))

/-- Eight genuine HD products for original physical row 1.
    NF700 supplies already-certified local dot products; every projection
    into the original complete input and cache is proved above. -/
theorem nf715Block000GlobalHD (j : Fin 8) :
    nf703OriginalCache.HDGate nf702OriginalInputs
      1 (⟨j.val, by omega⟩ : Fin 242) = true := by
  exact neutralNF704HD_of_packed_receipt
    nf702OriginalInputs nf703OriginalCache (1 : Fin 242)
    (fun j : Fin 8 => (⟨j.val, by omega⟩ : Fin 242))
    nf700HRow1
    (fun j k => nf700Block000Y k j)
    nf700Block000HDTarget
    nf715HRow1Projection
    (fun j => nf715Block000DProjection j)
    (fun j => nf715Block000HDTargetProjection j)
    nf700Block000HDAllCoordinates j

/-- Eight genuine A products for original physical column 1.
    No entire cache validity theorem is asserted by this local batch. -/
theorem nf715Block000GlobalA (j : Fin 8) :
    nf703OriginalCache.AGate nf702OriginalInputs
      (⟨j.val, by omega⟩ : Fin 242) 1 = true := by
  exact neutralNF704A_of_packed_receipt
    nf702OriginalInputs nf703OriginalCache (1 : Fin 242)
    (fun j : Fin 8 => (⟨j.val, by omega⟩ : Fin 242))
    nf700HDCol1
    (fun j k => nf700Block000Y k j)
    nf700Block000ATarget
    nf715HDCol1Projection
    (fun j => nf715Block000DProjection j)
    (fun j => nf715Block000ATargetProjection j)
    nf700Block000AAllCoordinates j

"""


def generate(a):
    provenance = sources(a)
    a.output.mkdir(parents=True, exist_ok=True)
    common = a.output / "Common.lean"
    block = a.output / "Block000.lean"
    src_common = OPTIONS + common_source() + "\n".join(
        f"#print axioms {name}" for name in DECLARATIONS[:4]) + "\n"
    src_block = OPTIONS + block_source() + "\n".join(
        f"#print axioms {name}" for name in DECLARATIONS[4:]) + "\n"
    common.write_text(filetext([
        "WeilDefect.Generated.NF702Inputs.Data",
        "WeilDefect.Generated.NF703Cache.Data",
        "WeilDefect.Generated.NF700.Block000",
        "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTriangularCacheAssembly",
    ], src_common))
    block.write_text(filetext([MODULE + ".Common"], src_block))
    m = {
        "schema": "NF715-second-original-global-matrix-block-v1",
        "row": 1, "column": 1,
        "first": 0, "end": WIDTH,
        "actual_global_HD_gates": WIDTH,
        "actual_global_A_gates": WIDTH,
        "audit_theorems": DECLARATIONS,
        "files": [
            {"file": f.name, "sha256": sha(f)} for f in (common, block)
        ],
        **provenance,
        "scope": "Original HD row 1, A column 1, first 8 entries. Complete matrix and cache validity remain independent obligations.",
    }
    (a.output / "manifest.json").write_text(json.dumps(m, indent=2) + "\n")
    print("NF715 exact original source and 577 accepted upstream theorem declarations authenticated; 16 global row1/column1 product candidates, 12 new declarations; kernel pending")


def make_axioms(a):
    m = json.loads((a.output / "manifest.json").read_text())
    assert m["audit_theorems"] == DECLARATIONS
    assert len(DECLARATIONS) == 12
    lines = [f"import {MODULE}.Block000"] + [
        f"#print axioms WeilDefect.{n}" for n in DECLARATIONS
    ]
    Path("nf715Audit.lean").write_text("\n".join(lines) + "\n")


def verify(a):
    m = json.loads((a.output / "manifest.json").read_text())
    assert m["audit_theorems"] == DECLARATIONS
    for f in m["files"]:
        assert sha(a.output / f["file"]) == f["sha256"]
    log = Path("nf715-axioms.log").read_text()
    observed = {}
    for n, raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log
    ):
        if n in DECLARATIONS:
            assert n not in observed
            observed[n] = [x.strip() for x in raw.split(",") if x.strip()]
    for n in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms", log
    ):
        if n in DECLARATIONS:
            assert n not in observed
            observed[n] = []
    assert set(observed) == set(DECLARATIONS)
    assert all(set(v) <= ALLOWED for v in observed.values())
    m["axioms"] = observed
    m["attachment_manifest_sha256"] = sha(a.output / "manifest.json")
    Path("nf715-complete-audit.json").write_text(json.dumps(m, indent=2) + "\n")
    print("NF715 second actual original global HD row/A column first eight entries: 16 gates, 12 Lean declarations PASS")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("prepare", "axiom-file", "verify"))
    p.add_argument("--receipts", type=Path, default=Path("nf715-receipts"))
    p.add_argument("--output", type=Path, default=Path("WeilDefect/Generated/NF715"))
    a = p.parse_args()
    {"prepare": generate, "axiom-file": make_axioms, "verify": verify}[a.stage](a)


if __name__ == "__main__":
    main()
