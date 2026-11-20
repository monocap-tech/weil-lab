#!/usr/bin/env python3
"""NF723: attach all 31 accepted original HD/A packed blocks to NF722's
genuine 242-coordinate gluing theorem on the actual NF702/NF703 objects.

Unlike the NF721 JSON inventory, this emits actual Lean theorems:
  ∀ j, nf703OriginalCache.HDGate nf702OriginalInputs 1 j = true
  ∀ i, nf703OriginalCache.AGate nf702OriginalInputs i 1 = true.

The exact source-specific 12+24+32+64+64+56 = 252 previous theorem
declarations, accepted source manifests, standard axiom audits, 31 packed
blocks and accepted terminal Fin 2 source are mandatory prior evidence.
Kernel acceptance of the two NEW universal declarations is independent and
must not be inferred from this generator alone.
"""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
N = 242
STAGES = (
    ("nf715", 0, 1, "nf715-complete-audit.json"),
    ("nf716", 1, 4, "nf716-complete-audit.json"),
    ("nf717", 4, 8, "nf717-complete-audit.json"),
    ("nf718", 8, 16, "nf718-shard-audit.json"),
    ("nf719", 16, 24, "nf719-shard-audit.json"),
    ("nf720", 24, 31, "nf720-shard-audit.json"),
)
SHARDS = {
    "nf718": ((8, 12, "nf718-a"), (12, 16, "nf718-b")),
    "nf719": ((16, 20, "nf719-a"), (20, 24, "nf719-b")),
    "nf720": ((24, 28, "nf720-a"), (28, 31, "nf720-b")),
}
AUDIT_COUNT = {"nf715":12, "nf716":24, "nf717":32,
               "nf718":64, "nf719":64, "nf720":56}
OUTPUT = Path("WeilDefect/Generated/NF723")
MOD = "WeilDefect.Generated.NF723"
NEW = ["nf723OriginalHDRowOneAll", "nf723OriginalAColumnOneAll"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def exactly_one(root, filename):
    candidates = sorted(root.rglob(filename))
    assert len(candidates) == 1, (root, filename, candidates)
    return candidates[0]


def module_manifest(root, module):
    found = [x for x in root.rglob("manifest.json") if x.parent.name == module]
    assert len(found) == 1, (root, module, found)
    path = found[0]
    m = read(path)
    for f in m["files"]:
        assert sha(path.parent / f["file"]) == f["sha256"], (path, f)
    assert len({f["file"] for f in m["files"]}) == len(m["files"])
    return path, m


def audit_names(audit, expected_count):
    data = audit["axioms"]
    assert len(data) == expected_count
    assert all(isinstance(a, list) and set(a) <= ALLOWED
               for a in data.values())
    return set(data)


def names_for_stage(stage, lo, hi):
    if stage == "nf715":
        return {
            "nf715HRow1Gate", "nf715HRow1Projection",
            "nf715HDCol1Gate", "nf715HDCol1Projection"
        } | {f"nf715Block000{s}" for s in SUFFIXES}
    return {f"{stage}Block{i:03d}{s}"
            for i in range(lo,hi) for s in SUFFIXES}


SUFFIXES = (
    "DGate", "DProjection", "HDTargetGate", "HDTargetProjection",
    "ATargetGate", "ATargetProjection", "GlobalHD", "GlobalA"
)


def check_source_and_audit(root, stage, lo, hi, audit_name, baseline, nf715_audit_sha):
    module = stage.upper()
    manifest_path, manifest = module_manifest(root,module)
    audit_path = exactly_one(root,audit_name)
    audit = read(audit_path)
    cert_names = audit_names(audit, 12 if stage == "nf715" else 8*(hi-lo))
    assert cert_names == names_for_stage(stage,lo,hi), (
        stage, sorted(names_for_stage(stage,lo,hi)-cert_names))
    digest = sha(manifest_path)

    if stage == "nf715":
        assert manifest["schema"] == audit["schema"] == (
            "NF715-second-original-global-matrix-block-v1")
        assert manifest["audit_theorems"] == audit["audit_theorems"]
        assert (manifest["row"],manifest["column"],manifest["first"],manifest["end"]) == (1,1,0,8)
        assert manifest["actual_global_HD_gates"] == manifest["actual_global_A_gates"] == 8
        assert len(manifest["files"]) == 2
        assert audit["attachment_manifest_sha256"] == digest
        old_sources = manifest["source_manifests"]
        old_audits = manifest["accepted_audits"]
    elif stage in ("nf716","nf717"):
        assert audit["source_manifest_sha256" if stage == "nf716" else "manifest_sha256"] == digest
        assert (manifest["first"],manifest["end"]) == (8*lo,min(8*hi,N))
        assert manifest["audit_theorems"] == [
            f"{stage}Block{i:03d}{s}" for i in range(lo,hi) for s in SUFFIXES]
        assert len(manifest["files"]) == hi-lo
        assert manifest["accepted_nf715_audit_sha256"] == nf715_audit_sha
        assert manifest["source_manifests"] == baseline["source_manifests"]
        old_sources = manifest["source_manifests"]
        old_audits = manifest["accepted_source_audits"]
    else:
        assert audit["manifest_sha256"] == digest
        assert (manifest["first_block"],manifest["end_block"]) == (lo,hi)
        assert (manifest["first"],manifest["end"]) == (8*lo,min(8*hi,N))
        assert manifest["coordinates"] == list(range(8*lo,min(8*hi,N)))
        assert manifest["audit_theorems"] == [
            f"{stage}Block{i:03d}{s}" for i in range(lo,hi) for s in SUFFIXES]
        assert len(manifest["files"]) == hi-lo
        assert audit["audit_theorems"] == manifest["audit_theorems"]
        assert audit["accepted_nf715_audit_sha256"] == nf715_audit_sha
        assert audit["source_manifests"] == manifest["source_manifests"]
        assert audit["accepted_source_audits"] == manifest["accepted_source_audits"]
        old_sources = audit["source_manifests"]
        old_audits = audit["accepted_source_audits"]
    assert old_sources == baseline["source_manifests"] and (
        old_audits == baseline["accepted_audits"])
    assert sha(manifest_path) == digest
    for k in ("nf702","nf703","nf700"):
        assert k.upper() not in str(manifest_path)
    return {
        "stage":stage, "first_block":lo, "end_block":hi,
        "manifest_path":str(manifest_path),
        "manifest_sha256":digest,
        "audit_path":str(audit_path),
        "audit_sha256":sha(audit_path),
        "source_files":{f["file"]:f["sha256"] for f in manifest["files"]},
        "theorems":sorted(cert_names)
    }


def authenticate(a):
    assert a.prior.is_dir()
    first_path, first = module_manifest(a.prior/"nf715","NF715")
    first_audit = exactly_one(a.prior/"nf715","nf715-complete-audit.json")
    assert first["source_manifests"] == a.baseline["source_manifests"]
    assert first["accepted_audits"] == a.baseline["accepted_audits"]
    nf715_audit_sha = sha(first_audit)

    # NF715 is generated anew from the original accepted NF702/NF703/NF700
    # sources before this driver is run. Even its first global gate source must
    # match the exact previously compiled proof text byte-for-byte.
    generated = Path("WeilDefect/Generated/NF715")
    gen_mpath, gen_m = module_manifest(Path("WeilDefect/Generated"),"NF715")
    assert gen_m == first and sha(gen_mpath) == sha(first_path)

    all_names, all_coords, stage_records = set(), [], []
    written = {"NF715":{f["file"]:f["sha256"] for f in gen_m["files"]}}
    for stage,lo,hi,audit_file in STAGES:
        if stage in SHARDS:
            pieces = SHARDS[stage]
        else:
            pieces = ((lo,hi,stage),)
        names = set()
        coords = []
        for first_block,end_block,folder in pieces:
            record = check_source_and_audit(
                a.prior/folder, stage, first_block, end_block, audit_file,
                a.baseline,nf715_audit_sha)
            stage_records.append(record)
            names.update(record["theorems"])
            coords += list(range(8*first_block,min(8*end_block,N)))
            assert not (set(record["theorems"]) & all_names), stage
            all_names.update(record["theorems"])
            module = stage.upper()
            mpath,_ = module_manifest(a.prior/folder,module)
            target = Path("WeilDefect/Generated")/module
            target.mkdir(parents=True,exist_ok=True)
            if module not in written:
                written[module] = {}
            for file, digest in record["source_files"].items():
                src = mpath.parent/file
                dest = target/file
                assert sha(src) == digest
                if dest.exists():
                    assert sha(dest) == digest
                else:
                    shutil.copy2(src,dest)
                if file in written[module]:
                    # NF715's authentic source was independently regenerated
                    # from the original input/cache/packed bank above.
                    assert stage == "nf715" and written[module][file] == digest
                else:
                    written[module][file] = digest
        assert len(names) == AUDIT_COUNT[stage], stage
        assert coords == list(range(8*lo,min(8*hi,N))), stage
        all_coords.extend(coords)

    assert all_coords == list(range(N))
    assert len(all_names) == sum(AUDIT_COUNT.values()) == 252

    # The independently successful NF721 source-specific audit intentionally
    # excluded NF717. Its precise 210-coordinate inventory plus NF717's
    # separately kernel-accepted [32,64) is required to equal Fin 242.
    ledger_path = exactly_one(a.ledger,"nf721-accepted-original-row-one-inventory.json")
    ledger = read(ledger_path)
    assert ledger["schema"] == (
        "NF721-source-specific-original-global-row-one-accepted-inventory-v1")
    previous = list(range(32)) + list(range(64,242))
    assert ledger["accepted_coordinates"] == previous
    assert ledger["unproved_coordinates"] == list(range(32,64))
    assert ledger["total_accepted_original_HD_row_one_gates"] == 210
    assert ledger["total_accepted_original_A_column_one_gates"] == 210
    assert ledger["accepted_lean_declarations"] == 220
    assert ledger["full_row_one_certified"] is False
    assert ledger["source_manifests"] == a.baseline["source_manifests"]
    assert ledger["accepted_local_source_audits"] == a.baseline["accepted_audits"]
    assert ledger["authenticated_accepted_stages"] == [
        "nf715","nf716","nf718","nf719","nf720"]
    ledger_cert_paths = {
        "nf715": exactly_one(a.prior/"nf715","nf715-complete-audit.json"),
        "nf716": exactly_one(a.prior/"nf716","nf716-complete-audit.json"),
        "nf718": exactly_one(a.aggregate/"nf718","nf718-complete-audit.json"),
        "nf719": exactly_one(a.aggregate/"nf719","nf719-complete-audit.json"),
        "nf720": exactly_one(a.aggregate/"nf720","nf720-complete-audit.json"),
    }
    assert set(ledger["stage_evidence"]) == set(ledger_cert_paths)
    for stage,path in ledger_cert_paths.items():
        # Exact identity, not merely matching declared coordinate counts.
        assert ledger["stage_evidence"][stage]["certificate_sha256"] == sha(path),stage
        assert ledger["stage_evidence"][stage]["source_manifests"] == (
            a.baseline["source_manifests"])
        assert ledger["stage_evidence"][stage]["accepted_source_audits"] == (
            a.baseline["accepted_audits"])
    ledger_coords = set(ledger["accepted_coordinates"])
    nf717_coords = set(range(32,64))
    assert ledger_coords.isdisjoint(nf717_coords)
    assert ledger_coords | nf717_coords == set(range(N))
    assert {r["stage"] for r in stage_records} == set(
        x[0] for x in STAGES)
    ledger_audit_sha = sha(ledger_path)

    # NF718–NF720's accepted aggregate gate certificates are authenticated
    # independently against the individual accepted kernel shard audits.
    for stage in ("nf718","nf719","nf720"):
        aggpath = exactly_one(a.aggregate/stage, f"{stage}-complete-audit.json")
        agg = read(aggpath)
        recs = [r for r in stage_records if r["stage"]==stage]
        expected_shas = [r["audit_sha256"] for r in recs]
        assert agg["shard_audit_sha256"] == expected_shas, (
            stage,agg["shard_audit_sha256"],expected_shas)
        assert agg["source_manifests"] == a.baseline["source_manifests"]
        assert agg["accepted_source_audits"] == a.baseline["accepted_audits"]
        assert agg["accepted_nf715_audit_sha256"] == nf715_audit_sha
        assert agg["axioms"].keys() == {n:None for r in recs for n in r["theorems"]}.keys()
        assert all(set(v) <= ALLOWED for v in agg["axioms"].values())
        assert agg["coordinates"] == list(range(64,128) if stage=="nf718"
            else range(128,192) if stage=="nf719" else range(192,242))

    binding = {
        "schema":"NF723-actual-original-complete-row-one-source-attachment-v1",
        "actual_source_manifests":a.baseline["source_manifests"],
        "accepted_original_source_audits":a.baseline["accepted_audits"],
        "nf715_accepted_audit_sha256":nf715_audit_sha,
        "nf721_independently_accepted_210_coordinate_ledger_sha256":ledger_audit_sha,
        "nf717_newly_closed_coordinate_interval":[32,64],
        "accepted_stages":stage_records,
        "source_files":written,
        "accepted_prior_theorem_declarations":len(all_names),
        "accepted_original_coordinate_pairs":N,
        "expected_original_hd_gates":N,
        "expected_original_a_gates":N,
        "new_universal_theorems":NEW,
        "proof_status":"source-bound candidate; needs new independent Lean kernel and strict axiom audit",
        "scope":"Actual NF702/NF703 complete HD row index 1 and A column index 1 only. Full physical cache, all physical/payment rows, all 242 vector rows, global Weil positivity and RH remain OPEN."
    }
    return binding


def emit(a,binding):
    dest = OUTPUT
    assert not dest.exists(),dest
    dest.mkdir(parents=True)
    imports = [
        "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedRowOneFiniteClosure",
        "WeilDefect.Generated.NF715.Block000"
    ] + [f"WeilDefect.Generated.{stage.upper()}.Block{i:03d}"
         for stage,lo,hi,_ in STAGES if stage!="nf715" for i in range(lo,hi)]
    assert len(imports) == 32
    local = lambda i,typ: (
        f"nf715Block000Global{typ}" if i==0
        else f"nf{(715 if i==0 else 716 if i<4 else 717 if i<8 else 718 if i<16 else 719 if i<24 else 720)}Block{i:03d}Global{typ}"
    )
    for typ in ("HD","A"):
        assert len({local(i,typ) for i in range(31)})==31
    body = (
        "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
        "/-! NF723: genuine original complete HD index-one row and A index-one column.\n"
        "This module uses 31 separately kernel-accepted original projected\n"
        "packed-coordinate product families and the NF722 Fin 242 gluing lemma.\n"
        "No unproved center-cache validity or numerical oracle is assumed. -/\n\n"
        "theorem nf723OriginalHDRowOneAll :\n"
        "    ∀ j : Fin 242, nf703OriginalCache.HDGate nf702OriginalInputs (1 : Fin 242) j = true := by\n"
        "  exact neutralNF722HDIndexOneOfPackedBlocks\n"
        "    nf702OriginalInputs nf703OriginalCache\n"
        + "".join(f"    {local(i,'HD')}\n" for i in range(31))
        + "\n"
        "theorem nf723OriginalAColumnOneAll :\n"
        "    ∀ i : Fin 242, nf703OriginalCache.AGate nf702OriginalInputs i (1 : Fin 242) = true := by\n"
        "  exact neutralNF722AIndexOneOfPackedBlocks\n"
        "    nf702OriginalInputs nf703OriginalCache\n"
        + "".join(f"    {local(i,'A')}\n" for i in range(31))
        + "\n"
        "#print axioms nf723OriginalHDRowOneAll\n"
        "#print axioms nf723OriginalAColumnOneAll\n"
    )
    file = dest/"OriginalRowOne.lean"
    file.write_text(filetext(imports,body))
    binding["new_source_sha256"] = sha(file)
    binding["new_module"] = MOD+".OriginalRowOne"
    (dest/"manifest.json").write_text(json.dumps(binding,indent=2,sort_keys=True)+"\n")
    Path("nf723-binding.json").write_text(
        json.dumps(binding,indent=2,sort_keys=True)+"\n")
    print("NF723 31 accepted original packed blocks source authenticated; actual complete row-one HD/A Lean candidate generated; kernel still pending")


def verify(a):
    binding = read(Path("nf723-binding.json"))
    m = read(OUTPUT/"manifest.json")
    assert m == binding
    assert sha(OUTPUT/"OriginalRowOne.lean") == binding["new_source_sha256"]
    assert binding["accepted_prior_theorem_declarations"] == 252
    assert binding["accepted_original_coordinate_pairs"] == N
    log = Path("nf723-axioms.log").read_text()
    found={}
    for n,x in re.findall(
            r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if n in NEW:
            assert n not in found
            found[n]=[x.strip() for x in x.split(",") if x.strip()]
    for n in re.findall(
            r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if n in NEW:
            assert n not in found
            found[n]=[]
    assert set(found)==set(NEW)
    assert all(set(v)<=ALLOWED for v in found.values())
    binding["axioms"]=found
    binding["proof_status"]="LEAN KERNEL PASS, strict two-declaration standard-axiom audit PASS"
    Path("nf723-complete-audit.json").write_text(
        json.dumps(binding,indent=2,sort_keys=True)+"\n")
    print("NF723 source-bound original complete global HD row one (242) and A column one (242) LEAN PASS: 484 authentic product gate identities / 2 all-coordinate theorems")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("prepare","verify"))
    p.add_argument("--prior",type=Path,default=Path("nf723-accepted"))
    p.add_argument("--aggregate",type=Path,default=Path("nf723-aggregates"))
    p.add_argument("--ledger",type=Path,default=Path("nf723-accepted-ledger"))
    a=p.parse_args()
    if a.stage=="prepare":
        baseline_path = Path("WeilDefect/Generated/NF715/manifest.json")
        assert baseline_path.is_file()
        a.baseline=read(baseline_path)
        assert (set(a.baseline["source_manifests"]) ==
                set(a.baseline["accepted_audits"]) ==
                {"inputs","cache","packed"})
        b=authenticate(a)
        emit(a,b)
    else:
        verify(a)


if __name__=="__main__":
    main()
