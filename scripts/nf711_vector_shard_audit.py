#!/usr/bin/env python3
"""NF711: independently audit NF710's exhaustive original vector proof shards.

This runner never promotes source generation to Lean success. All 242
NF709 global vector gates, 16 NF710 shard gates and both terminal theorems
must be individually kernel-audited with only standard axioms.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

N, WIDTH = 242, ALLOWED = 242, 16, {"propext", "Classical.choice", "Quot.sound"}
LOCAL_SUFFIXES = ("VGate", "VProjection", "DColGate", "DColProjection",
                  "ARowGate", "ARowProjection", "CacheB", "CacheAy", "CacheDy",
                  "VwGlobal", "BGlobal", "AyGlobal", "DyGlobal", "Vector")
COMMON = ("nf709YGate", "nf709YProjection", "nf709WGate", "nf709WProjection",
          "nf709VwGate", "nf709VwProjection")
FINAL = ("nf710EveryOriginalVector", "nf710OriginalVectorCheck")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_files(d):
    m = json.loads((d / "manifest.json").read_text())
    for f in m["files"]:
        assert sha(d / f["file"]) == f["sha256"], (d, f["file"])
    return m


def read_proposals(root):
    source = root / "NF709"
    aggregate = root / "NF710Vectors"
    sm, am = check_files(source), check_files(aggregate)
    assert sm["schema"] == "NF709-global-original-vector-attachments-v1"
    assert am["schema"] == "NF710-global-original-vector-aggregation-v1"
    assert sm["first"] == 0 and sm["count"] == am["rows"] == N
    assert sm["rows"] == list(range(N))
    assert sm["source_manifests"] == am["source_manifests"]
    assert sm["accepted_audits"] == am["accepted_prior_audits"]
    assert am["local_source_manifest_sha256"] == sha(source / "manifest.json")
    assert am["global_vector_gates"] == N
    assert am["source_declarations"] == 6 + 14*N
    assert am["width"] == WIDTH and len(am["shards"]) == 16
    assert am["shard_theorems"] == [s["theorem"] for s in am["shards"]]
    assert am["terminal_theorems"] == list(FINAL)
    assert len(sm["files"]) == N + 1 and len(am["files"]) == 17
    expected_local = list(COMMON) + [
        f"nf709Row{i:03d}{x}" for i in range(N) for x in LOCAL_SUFFIXES]
    assert sm["theorems"] == expected_local
    assert len(expected_local) == len(set(expected_local)) == 3394
    rows = []
    for k, shard in enumerate(am["shards"]):
        first = k*WIDTH
        last = min(first+WIDTH, N)
        assert (shard["start"], shard["end"], shard["rows"]) == (
            first, last, list(range(first,last)))
        assert shard["module"] == f"Shard{first:03d}"
        assert shard["theorem"] == f"nf710VectorShard{first:03d}"
        rows += shard["rows"]
    assert rows == list(range(N))
    return sm, am


def proof_names(shard):
    return list(COMMON) + [
        f"nf709Row{i:03d}{x}" for i in shard["rows"] for x in LOCAL_SUFFIXES
    ] + [shard["theorem"]]


def preflight():
    from emit_nf710_complete_global_vector_schedule import emit_shard
    rows, names = [], []
    for first in range(0, N, WIDTH):
        end = min(first+WIDTH,N)
        name, theorem, source = emit_shard(first,end)
        assert name == f"Shard{first:03d}"
        assert theorem == f"nf710VectorShard{first:03d}"
        assert f"Fin {end-first}" in source
        assert source.count("fin_cases j") == 1
        assert source.count("· exact nf709Row") == end-first
        assert "by omega" in source
        rows += list(range(first,end))
        names.append(theorem)
    assert rows == list(range(N)) and len(names)==16 and len(set(names))==16
    print("NF711 static shard-design preflight PASS: 16 disjoint shards, all 242 indices; kernel not run")


def axiom_file(path, imports, names):
    path.write_text("\n".join(
        [f"import {x}" for x in imports]
        + [f"#print axioms WeilDefect.{n}" for n in names]
    ) + "\n")


def parse_axioms(log, required):
    expected = set(required)
    assert len(expected) == len(required)
    found = {}
    for n, x in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if n in expected:
            assert n not in found, n
            found[n] = [v.strip() for v in x.split(",") if v.strip()]
    for n in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if n in expected:
            assert n not in found, n
            found[n] = []
    assert set(found) == expected, (sorted(expected-set(found)), sorted(set(found)-expected))
    assert all(set(v) <= ALLOWED for v in found.values())
    return found


def main():
    p = argparse.ArgumentParser()
    p.add_argument("mode",choices=("preflight","make-shard","audit-shard","make-final","audit-final"))
    p.add_argument("--root",type=Path,default=Path("WeilDefect/Generated"))
    p.add_argument("--shard",type=int,default=0)
    p.add_argument("--out",type=Path,default=Path("."))
    p.add_argument("--audit-dir",type=Path,default=Path("nf711-shard-audits"))
    a=p.parse_args()
    if a.mode=="preflight":
        preflight()
        return
    sm, am=read_proposals(a.root)
    a.out.mkdir(parents=True,exist_ok=True)
    if a.mode in ("make-shard","audit-shard"):
        assert a.shard in range(16)
        shard=am["shards"][a.shard]
        names=proof_names(shard)
        stem=f"nf711-{shard['module'].lower()}"
        if a.mode=="make-shard":
            imports=[f"WeilDefect.Generated.NF710Vectors.{shard['module']}"]
            axiom_file(a.out/(stem+"-axioms.lean"),imports,names)
            print(f"NF711 {shard['module']} {len(shard['rows'])} indices, {len(names)} axiom targets")
            return
        log=(a.out/(stem+"-axioms.log")).read_text()
        found=parse_axioms(log,names)
        report={
            "schema":"NF711-original-global-vector-shard-audit-v1",
            "shard":a.shard,"start":shard["start"],"end":shard["end"],
            "rows":shard["rows"],"theorems":found,
            "nf709_manifest_sha256":sha(a.root/"NF709/manifest.json"),
            "nf710_manifest_sha256":sha(a.root/"NF710Vectors/manifest.json"),
            "source_manifests":sm["source_manifests"],
            "prior_audits":sm["accepted_audits"],
        }
        (a.out/(stem+"-audit.json")).write_text(json.dumps(report,indent=2)+"\n")
        print(f"NF711 {shard['module']}: {len(names)} source-specific declarations LEAN PASS")
        return
    if a.mode=="make-final":
        axiom_file(a.out/"nf711-final-axioms.lean",
                   ["WeilDefect.Generated.NF710Vectors.All"],list(FINAL))
        print("NF711 terminal vector source audit prepared; Lean pending")
        return
    found_final=parse_axioms((a.out/"nf711-final-axioms.log").read_text(),list(FINAL))
    receipts=sorted(a.audit_dir.rglob("nf711-shard*-audit.json"))
    assert len(receipts)==16,(len(receipts),receipts)
    combined={}
    covered=[]
    for k,p0 in enumerate(receipts):
        a0=json.loads(p0.read_text())
        shard=am["shards"][k]
        assert a0["schema"]=="NF711-original-global-vector-shard-audit-v1"
        assert (a0["shard"],a0["start"],a0["end"],a0["rows"])==(
            k,shard["start"],shard["end"],shard["rows"])
        assert a0["nf709_manifest_sha256"]==sha(a.root/"NF709/manifest.json")
        assert a0["nf710_manifest_sha256"]==sha(a.root/"NF710Vectors/manifest.json")
        assert a0["source_manifests"]==sm["source_manifests"]
        assert a0["prior_audits"]==sm["accepted_audits"]
        assert set(a0["theorems"])==set(proof_names(shard))
        assert all(set(x)<=ALLOWED for x in a0["theorems"].values())
        covered+=shard["rows"]
        for name,axioms in a0["theorems"].items():
            if name in combined:
                assert combined[name]==axioms
            else:
                combined[name]=axioms
    assert covered==list(range(N))
    combined.update(found_final)
    expected=set(sm["theorems"])|set(am["shard_theorems"])|set(FINAL)
    assert set(combined)==expected and len(expected)==3394+16+2
    result={"schema":"NF711-complete-original-global-vector-audit-v1",
            "rows":N,"shards":16,"theorems":combined,
            "nf709_manifest_sha256":sha(a.root/"NF709/manifest.json"),
            "nf710_manifest_sha256":sha(a.root/"NF710Vectors/manifest.json"),
            "source_manifests":sm["source_manifests"],
            "prior_audits":sm["accepted_audits"],
            "scope":"All original global vector gates; independent HD/A and payment validity remain open."}
    (a.out/"nf711-complete-audit.json").write_text(json.dumps(result,indent=2)+"\n")
    print("NF711 original 242-vector global gate aggregate: 3412 standard-axiom declarations LEAN PASS")


if __name__=="__main__":
    main()
