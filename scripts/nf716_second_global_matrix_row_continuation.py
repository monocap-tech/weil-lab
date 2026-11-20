#!/usr/bin/env python3
"""NF716: second original HD row and A column, packed blocks 001..003.

Depends on a *passing* NF715 standard-axiom kernel audit for block 000;
regenerates NF715 from its original input/cache/NF700 local receipts and
compares its source digest with the accepted NF715 artifact. Only then emits
new genuine global matrix product proof candidates for indices 8..31.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from emit_nf630_original_literal_payments import filetext
from nf715_second_global_matrix_row_driver import (
    ALLOWED, DECLARATIONS as OLD_NAMES, sha
)

START_BLOCK = 1
END_BLOCK = 4
WIDTH = 8
MODULE = "WeilDefect.Generated.NF716"
OPTIONS = "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
SUFFIXES = ("DGate", "DProjection", "HDTargetGate",
            "HDTargetProjection", "ATargetGate", "ATargetProjection",
            "GlobalHD", "GlobalA")


def unique(root, name):
    paths = sorted(root.rglob(name))
    assert len(paths) == 1, (root, name, paths)
    return paths[0]


def source_manifest(folder):
    path = folder / "manifest.json"
    m = json.loads(path.read_text())
    for entry in m["files"]:
        assert sha(folder / entry["file"]) == entry["sha256"], entry
    return m


def decls(block):
    prefix = f"nf716Block{block:03d}"
    return [prefix + suffix for suffix in SUFFIXES]


def generated_block(block, *, stage="nf716", lower=START_BLOCK, upper=END_BLOCK):
    assert lower <= block < upper
    prefix = f"{stage}Block{block:03d}"
    source = f"nf700Block{block:03d}"
    start = block * WIDTH
    assert start + WIDTH <= 242
    idx = f"(⟨{start} + j.val, by omega⟩ : Fin 242)"
    return f"""theorem {prefix}DGate :
    (List.finRange 8).all (fun j : Fin 8 =>
      (List.finRange 242).all (fun k : Fin 242 =>
        decide ({source}Y k j = nf702OriginalInputs.D k {idx}))) = true := by
  decide +kernel

theorem {prefix}DProjection (j : Fin 8) :
    (fun k => {source}Y k j) =
    (fun k => nf702OriginalInputs.D k {idx}) := by
  funext k
  have hj := (List.all_eq_true.mp {prefix}DGate) j (by simp)
  exact of_decide_eq_true ((List.all_eq_true.mp hj) k (by simp))

theorem {prefix}HDTargetGate :
    (List.finRange 8).all (fun j : Fin 8 =>
      decide ({source}HDTarget j = nf703OriginalCache.HD 1 {idx})) = true := by
  decide +kernel

theorem {prefix}HDTargetProjection (j : Fin 8) :
    {source}HDTarget j = nf703OriginalCache.HD 1 {idx} :=
  of_decide_eq_true ((List.all_eq_true.mp {prefix}HDTargetGate) j (by simp))

theorem {prefix}ATargetGate :
    (List.finRange 8).all (fun j : Fin 8 =>
      decide ({source}ATarget j = nf703OriginalCache.A {idx} 1)) = true := by
  decide +kernel

theorem {prefix}ATargetProjection (j : Fin 8) :
    {source}ATarget j = nf703OriginalCache.A {idx} 1 :=
  of_decide_eq_true ((List.all_eq_true.mp {prefix}ATargetGate) j (by simp))

/-- Eight actual global original HD row-one product gates.
    NF700's complete source-bound packed dot-products are already accepted. -/
theorem {prefix}GlobalHD (j : Fin 8) :
    nf703OriginalCache.HDGate nf702OriginalInputs 1 {idx} = true := by
  exact neutralNF704HD_of_packed_receipt
    nf702OriginalInputs nf703OriginalCache (1 : Fin 242)
    (fun j : Fin 8 => {idx})
    nf700HRow1
    (fun j k => {source}Y k j)
    {source}HDTarget
    nf715HRow1Projection
    (fun j => {prefix}DProjection j)
    (fun j => {prefix}HDTargetProjection j)
    {source}HDAllCoordinates j

/-- Eight actual global original A column-one product gates. -/
theorem {prefix}GlobalA (j : Fin 8) :
    nf703OriginalCache.AGate nf702OriginalInputs {idx} 1 = true := by
  exact neutralNF704A_of_packed_receipt
    nf702OriginalInputs nf703OriginalCache (1 : Fin 242)
    (fun j : Fin 8 => {idx})
    nf700HDCol1
    (fun j k => {source}Y k j)
    {source}ATarget
    nf715HDCol1Projection
    (fun j => {prefix}DProjection j)
    (fun j => {prefix}ATargetProjection j)
    {source}AAllCoordinates j

"""


def reproduce_nf715(a):
    call = ["python", "scripts/nf715_second_global_matrix_row_driver.py",
            "prepare", "--receipts", str(a.receipts),
            "--output", "WeilDefect/Generated/NF715"]
    subprocess.run(call, check=True)
    actual = Path("WeilDefect/Generated/NF715")
    current = source_manifest(actual)
    previous_manifest = unique(a.prior, "manifest.json")
    assert previous_manifest.parent.name == "NF715"
    previous = source_manifest(previous_manifest.parent)
    audit_file = unique(a.prior, "nf715-complete-audit.json")
    audit = json.loads(audit_file.read_text())
    assert previous == current
    assert sha(previous_manifest) == sha(actual / "manifest.json")
    assert audit["schema"] == "NF715-second-original-global-matrix-block-v1"
    assert audit["attachment_manifest_sha256"] == sha(previous_manifest)
    assert audit["audit_theorems"] == OLD_NAMES == current["audit_theorems"]
    assert set(audit["axioms"]) == set(OLD_NAMES)
    assert all(set(axioms) <= ALLOWED for axioms in audit["axioms"].values())
    assert audit["source_manifests"] == current["source_manifests"]
    assert audit["accepted_audits"] == current["accepted_audits"]
    assert previous["first"] == 0 and previous["end"] == 8
    assert previous["actual_global_HD_gates"] == previous["actual_global_A_gates"] == 8
    assert {f["file"] for f in current["files"]} == {"Common.lean", "Block000.lean"}
    return actual, current, audit_file


def prepare(a):
    original, accepted, accepted_audit_file = reproduce_nf715(a)
    packed = source_manifest(Path("WeilDefect/Generated/NF700"))
    assert packed["schema"] == "NF700-original-packed-second-matrix-frontier-v1"
    blocks = packed["blocks"]
    assert len(blocks) == 31
    a.output.mkdir(parents=True, exist_ok=True)
    names, files, gates = [], [], []
    for block in range(START_BLOCK, END_BLOCK):
        local = blocks[block]
        assert local["module"] == f"Block{block:03d}"
        assert local["start"] == WIDTH * block and local["stop"] == WIDTH * (block+1)
        assert local["width"] == WIDTH
        assert {f"nf700Block{block:03d}HDAllCoordinates",
                f"nf700Block{block:03d}AAllCoordinates"} <= set(local["theorems"])
        body = generated_block(block)
        new_names = decls(block)
        body += "\n".join(f"#print axioms {n}" for n in new_names) + "\n"
        path = a.output / f"Block{block:03d}.lean"
        path.write_text(filetext([
            "WeilDefect.Generated.NF715.Common",
            f"WeilDefect.Generated.NF700.Block{block:03d}"
        ], OPTIONS + body))
        files.append({"file": path.name, "sha256": sha(path)})
        names += new_names
        gates.extend({"index": i, "row": 1, "column": 1}
                     for i in range(WIDTH*block, WIDTH*(block+1)))
    assert len(names) == len(set(names)) == 24
    assert len(gates) == 24
    m = {
        "schema": "NF716-second-original-global-matrix-row-continuation-v1",
        "original_index": 1,
        "first": WIDTH*START_BLOCK,
        "end": WIDTH*END_BLOCK,
        "blocks": list(range(START_BLOCK, END_BLOCK)),
        "new_HD_gates": 24, "new_A_gates": 24,
        "gate_coordinates": gates,
        "audit_theorems": names,
        "files": files,
        "accepted_nf715_manifest_sha256": sha(original / "manifest.json"),
        "accepted_nf715_audit_sha256": sha(accepted_audit_file),
        "source_manifests": accepted["source_manifests"],
        "accepted_source_audits": accepted["accepted_audits"],
        "packed_source_manifest_sha256": sha(Path("WeilDefect/Generated/NF700/manifest.json")),
        "scope": "Actual original global HD row 1 and A column 1 for coordinates 8..31 only. Source equality and prior accepted NF715 audit required. Full 242-dimensional matrix validity and Weil positivity remain open.",
    }
    (a.output / "manifest.json").write_text(json.dumps(m, indent=2) + "\n")
    print("NF716 accepted NF715 12-theorem audit and identical source verified; 48 new actual HD/A global gate candidates, 24 new theorems; Lean pending")


def axiom_file(a):
    m = source_manifest(a.output)
    assert m["schema"] == "NF716-second-original-global-matrix-row-continuation-v1"
    names = [n for block in range(START_BLOCK, END_BLOCK) for n in decls(block)]
    assert m["audit_theorems"] == names
    imports = [f"import {MODULE}.Block{block:03d}"
               for block in range(START_BLOCK, END_BLOCK)]
    Path("nf716Audit.lean").write_text(
        "\n".join(imports + [f"#print axioms WeilDefect.{n}" for n in names]) + "\n")


def verify(a):
    m = source_manifest(a.output)
    assert m["schema"] == "NF716-second-original-global-matrix-row-continuation-v1"
    assert m["blocks"] == list(range(START_BLOCK, END_BLOCK))
    assert m["audit_theorems"] == [
        n for block in range(START_BLOCK, END_BLOCK) for n in decls(block)]
    assert m["new_HD_gates"] == m["new_A_gates"] == 24
    log = Path("nf716-axioms.log").read_text()
    found = {}
    for name, raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if name in m["audit_theorems"]:
            assert name not in found
            found[name] = [x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if name in m["audit_theorems"]:
            assert name not in found
            found[name] = []
    assert set(found) == set(m["audit_theorems"])
    assert len(found) == 24
    assert all(set(x) <= ALLOWED for x in found.values())
    result = {
        "schema": "NF716-second-original-global-matrix-row-continuation-audit-v1",
        "source_manifest_sha256": sha(a.output / "manifest.json"),
        **m,
        "axioms": found,
        "cumulative_original_HD_A_gates_if_passed": 32 + 16 + 48,
    }
    Path("nf716-complete-audit.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print("NF716 original HD row 1 + A column 1 indices 8..31: 48 new gates / 24 declarations LEAN PASS")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=("prepare", "axiom-file", "verify"))
    p.add_argument("--receipts", type=Path, default=Path("nf716-receipts"))
    p.add_argument("--prior", type=Path, default=Path("nf716-prior"))
    p.add_argument("--output", type=Path,
                   default=Path("WeilDefect/Generated/NF716"))
    a = p.parse_args()
    {"prepare": prepare, "axiom-file": axiom_file, "verify": verify}[a.stage](a)


if __name__ == "__main__":
    main()
