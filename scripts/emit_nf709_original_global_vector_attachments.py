#!/usr/bin/env python3
"""NF709: attach accepted NF680 original local vector receipts to full inputs/cache.

Every original source and accepted Lean receipt is hash-bound. The generated
global equalities are proof candidates until Lean checks their declarations.
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

N = 242
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
MOD = "WeilDefect.Generated.NF709"
OPT = "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
SUFFIXES = ("VGate", "VProjection", "DColGate", "DColProjection",
            "ARowGate", "ARowProjection", "CacheB", "CacheAy", "CacheDy",
            "VwGlobal", "BGlobal", "AyGlobal", "DyGlobal", "Vector")
COMMON = ("nf709YGate", "nf709YProjection", "nf709WGate", "nf709WProjection",
          "nf709VwGate", "nf709VwProjection")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_stage(root, stage):
    found = [p.parent for p in root.rglob("manifest.json") if p.parent.name == stage]
    assert len(found) == 1, (root, stage, found)
    return found[0]


def find_receipt(root, name):
    found = list(root.rglob(name))
    assert len(found) == 1, (root, name, found)
    return found[0]


def check_manifest(d):
    m = json.loads((d / "manifest.json").read_text())
    for f in m["files"]:
        assert sha(d / f["file"]) == f["sha256"], (d, f["file"])
    return m


def check_audit(path, manifest_path, names, field):
    a = json.loads(path.read_text())
    assert a["manifest_sha256"] == sha(manifest_path)
    assert set(a[field]) == set(names), (path, len(a[field]), len(names))
    assert all(set(v) <= ALLOWED for v in a[field].values())
    return a


def row_names(i):
    return [f"nf709Row{i:03d}{s}" for s in SUFFIXES]


def common_gate(name, left, right, n):
    return f"""theorem nf709{name}Gate :
    (List.finRange {n}).all (fun j =>
      decide ({left} j = {right} j)) = true := by
  decide +kernel

theorem nf709{name}Projection : {left} = {right} :=
  funext (fun j =>
    of_decide_eq_true ((List.all_eq_true.mp nf709{name}Gate) j (by simp)))

"""


def row_code(i):
    k = f"{i:03d}"
    z = f"nf709Row{k}"
    v = f"nf680Row{k}"
    scalar = f"nf639Row{k}"
    ii = f"({i}:Fin 242)"
    text = f"""theorem {z}VGate :
    (List.finRange 4).all (fun j =>
      decide ({v}V j = nf702OriginalInputs.V {ii} j)) = true := by
  decide +kernel

theorem {z}VProjection :
    {v}V = nf702OriginalInputs.V {ii} :=
  funext (fun j =>
    of_decide_eq_true ((List.all_eq_true.mp {z}VGate) j (by simp)))

theorem {z}DColGate :
    (List.finRange 242).all (fun j =>
      decide ({v}Col j = nf702OriginalInputs.D j {ii})) = true := by
  decide +kernel

theorem {z}DColProjection :
    {v}Col = (fun j => nf702OriginalInputs.D j {ii}) :=
  funext (fun j =>
    of_decide_eq_true ((List.all_eq_true.mp {z}DColGate) j (by simp)))

theorem {z}ARowGate :
    (List.finRange 242).all (fun j =>
      decide ({v}A j = nf703OriginalCache.A {ii} j)) = true := by
  decide +kernel

theorem {z}ARowProjection :
    {v}A = nf703OriginalCache.A {ii} :=
  funext (fun j =>
    of_decide_eq_true ((List.all_eq_true.mp {z}ARowGate) j (by simp)))

theorem {z}CacheB :
    {scalar}.b = nf703OriginalCache.b {ii} := by
  decide +kernel

theorem {z}CacheAy :
    {scalar}.Ay = nf703OriginalCache.Ay {ii} := by
  decide +kernel

theorem {z}CacheDy :
    {scalar}.Dy = nf703OriginalCache.Dy {ii} := by
  decide +kernel

theorem {z}VwGlobal :
    nf703OriginalCache.Vw {ii} =
      neutralNF626Dot (nf702OriginalInputs.V {ii}) nf702OriginalInputs.w := by
  calc
    _ = nf680Vw {ii} := congrFun nf709VwProjection.symm {ii}
    _ = neutralNF626Dot {v}V nf680W := {v}Vw
    _ = neutralNF626Dot (nf702OriginalInputs.V {ii}) nf702OriginalInputs.w := by
      rw [{z}VProjection, nf709WProjection]

theorem {z}BGlobal :
    {scalar}.b =
      neutralNF626Dot (fun j => nf702OriginalInputs.D j {ii})
        nf703OriginalCache.Vw := by
  calc
    _ = neutralNF626Dot {v}Col nf680Vw := {v}B
    _ = neutralNF626Dot (fun j => nf702OriginalInputs.D j {ii})
          nf703OriginalCache.Vw := by
      rw [{z}DColProjection, nf709VwProjection]

theorem {z}AyGlobal :
    {scalar}.Ay =
      neutralNF626Dot (nf703OriginalCache.A {ii}) nf702OriginalInputs.y := by
  calc
    _ = neutralNF626Dot {v}A nf680Y := {v}Ay
    _ = neutralNF626Dot (nf703OriginalCache.A {ii}) nf702OriginalInputs.y := by
      rw [{z}ARowProjection, nf709YProjection]

theorem {z}DyGlobal :
    {scalar}.Dy =
      neutralNF626Dot (nf702OriginalInputs.D {ii}) nf702OriginalInputs.y := by
  decide +kernel

theorem {z}Vector :
    nf703OriginalCache.vectorGate nf702OriginalInputs {ii} = true := by
  exact neutralNF680VectorGate_of_receipts
    nf703OriginalCache nf702OriginalInputs {ii} {scalar}
    {z}CacheB {z}CacheAy {z}CacheDy
    {z}VwGlobal {z}BGlobal {z}AyGlobal {z}DyGlobal

"""
    return text + "\n".join(f"#print axioms {n}" for n in row_names(i)) + "\n"


def main():
    p = argparse.ArgumentParser()
    for v in ("inputs", "cache", "vectors", "input_audit", "cache_audit",
              "vector_audit", "output"):
        p.add_argument("--" + v.replace("_", "-"), type=Path, required=True)
    p.add_argument("--first", type=int, default=0)
    p.add_argument("--count", type=int, default=16)
    a = p.parse_args()
    assert 0 <= a.first < N and 0 < a.count <= N - a.first
    si = find_stage(a.inputs, "NF702Inputs")
    ca = find_stage(a.cache, "NF703Cache")
    ve = find_stage(a.vectors, "NF680")
    sc = find_stage(a.vectors, "NF639")
    sm, cm, vm, xm = [check_manifest(d) for d in (si, ca, ve, sc)
                        if d != sc] + [json.loads((sc / "manifest.json").read_text())]
    for r in xm["files"]:
        if r["file"] != "Params.lean":
            assert sha(sc / r["file"]) == r["sha256"]
    assert sm["rows"] == cm["rows"] == vm["rows"] == N
    assert sm["entries_sha256"] == cm["entry_sha256"] == vm["entry_sha256"]
    assert sm["historical_sha256"] == cm["historical_sha256"] == vm["historical_sha256"]
    assert sm["payment_sha256"] == cm["payment_sha256"] == vm["payment_sha256"]
    assert sm["source_frame_sha256"] == vm["frame_sha256"]
    assert cm["cache_sha256"] == vm["cache_sha256"]
    assert vm["scalar_manifest_sha256"] == sha(sc / "manifest.json")
    expected_in = {"nf702InputH_symm", "nf702OriginalW"} | {
        t for r in sm["projection_rows"] for t in r["theorems"]
    }
    assert len(expected_in) == 50
    assert len(cm["audit_theorems"]) == 7
    expected_local = {f"nf680Row{i:03d}{s}" for i in range(N)
                      for s in ("Vw", "B", "Ay", "Defect", "CacheLiterals")}
    assert len(expected_local) == 1210
    receipts = {
        "input": (a.input_audit, si, expected_in, "axioms"),
        "cache": (a.cache_audit, ca, cm["audit_theorems"], "axioms"),
        "vectors": (a.vector_audit, ve, expected_local, "theorems")
    }
    for name, (path, directory, names, field) in receipts.items():
        check_audit(find_receipt(path, path.name) if path.is_dir() else path,
                    directory / "manifest.json", names, field)
    root = Path("WeilDefect/Generated")
    for src, stage in ((si, "NF702Inputs"), (ca, "NF703Cache"), (ve, "NF680"), (sc, "NF639")):
        dst = root / stage
        assert not dst.exists(), dst
        shutil.copytree(src, dst)
    a.output.mkdir(parents=True, exist_ok=True)
    files = []
    def write(name, imports, body):
        f = a.output / (name + ".lean")
        f.write_text(filetext(imports, OPT + body))
        files.append({"file": f.name, "sha256": sha(f)})
    common = (
        common_gate("Y", "nf680Y", "nf702OriginalInputs.y", 242)
        + common_gate("W", "nf680W", "nf702OriginalInputs.w", 4)
        + common_gate("Vw", "nf680Vw", "nf703OriginalCache.Vw", 242)
        + "\n".join(f"#print axioms {n}" for n in COMMON) + "\n"
    )
    write("Common", ["WeilDefect.Generated.NF702Inputs.Data",
                     "WeilDefect.Generated.NF703Cache.Data",
                     "WeilDefect.Generated.NF680.Common"], common)
    rows = list(range(a.first, a.first + a.count))
    for i in rows:
        write(f"Row{i:03d}",
              [MOD + ".Common", f"WeilDefect.Generated.NF680.Row{i:03d}"],
              row_code(i))
    all_names = list(COMMON) + [n for i in rows for n in row_names(i)]
    assert len(all_names) == 6 + 14*a.count and len(all_names) == len(set(all_names))
    report = {
        "schema": "NF709-global-original-vector-attachments-v1",
        "first": a.first, "count": a.count, "rows": rows,
        "theorems": all_names, "files": files,
        "source_manifests": {"input": sha(si/"manifest.json"),
                             "cache": sha(ca/"manifest.json"),
                             "vectors": sha(ve/"manifest.json"),
                             "scalar": sha(sc/"manifest.json")},
        "accepted_audits": {k: sha(find_receipt(t[0], t[0].name) if t[0].is_dir() else t[0])
                            for k, t in receipts.items()},
        "scope": "Source-specific global vector gates for specified rows; full HD/A, remaining vector gates and cache validity stay separate."
    }
    (a.output / "manifest.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"NF709 {a.count} authentic original global vector-gate candidates / {len(all_names)} declarations emitted; kernel pending")


if __name__ == "__main__":
    main()
