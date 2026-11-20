#!/usr/bin/env python3
"""NF743: fail-closed reuse of previously LEAN-ACCEPTED original NF703 cache.

Source of truth: the immutable successful original NF728 SOURCE archive and
immutable successful NF729 original numerical quad000 KERNEL archive.
NF737's independently authenticated source archive reconstructs the *same*
frozen NF702Inputs / NF703Cache / NF681 original physical data.

Never promote an old .olean because its basename matches. For every file in
these three generated source families compare exact bytes (SHA256) against
the immutable original NF728 source ZIP that produced the NF729 successful
kernel artifacts. Then take only Lean objects from the successful accepted
NF729 numerical artifact, with exact compressed ZIP digest verification.

This is an optimization of the *trusted original compiler path*, not a new
mathematical proof, not a source-only numerical acceptance.
"""
import argparse
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path

BASE=Path("WeilDefect/Generated")
FAMILIES=("NF702Inputs","NF703Cache","NF681")
SOURCE_ZIP=Path("nf743-nf728-accepted-original-source.zip")
OBJECT_ZIP=Path("nf743-nf729-accepted-original-quad000-objects.zip")
OUTPUT=Path("nf743-accepted-original-center-cache-reuse.json")
LIB=Path(".lake/build/lib/lean/WeilDefect")
FULL_SOURCE=BASE/"NF704Frontier"/"manifest.json"
EXPECTED_SRC_DIGEST="12bb99f055e9fe8843b33ca110877729114331b6e68361b98f8b449357ae3a55"
EXPECTED_OBJ_DIGEST="e9f31c3780a7ea2c52a6b4f3df0e9c22f351b123fe9fde94be0161eec2c6a687"
OLD_RUN_ID=44764979145
ACCEPTED_OBJECT_RUN_ID=44767040253
OLD_SOURCE_ARTIFACT_ID=14644051272
ACCEPTED_OBJECT_ARTIFACT_ID=14647164240
ORIGINAL_KERNEL_JOB_ID=136399712401

def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as file:
        while part:=file.read(1024*1024):
            h.update(part)
    return h.hexdigest()

def file_hash(stream):
    h=hashlib.sha256()
    while part:=stream.read(1024*1024):
        h.update(part)
    return h.hexdigest()

def assert_original_source_matches():
    assert sha(SOURCE_ZIP)==EXPECTED_SRC_DIGEST, "Immutable NF728 original source ZIP artifact digest mismatch"
    assert FULL_SOURCE.is_file()
    fromzip={}
    with zipfile.ZipFile(SOURCE_ZIP) as z:
        for entry in z.infolist():
            # GitHub upload-artifact may record the ZIP with a hidden
            # leading root; normalize only by exact known directory marker.
            if entry.is_dir() or not entry.filename.endswith(".lean"):
                continue
            name=entry.filename
            marker="WeilDefect/Generated/"
            ix=name.find(marker)
            if ix<0:
                continue
            name=name[ix+len(marker):]
            if not any(name.startswith(family+"/") for family in FAMILIES):
                continue
            assert name not in fromzip,(name,"duplicate historic source")
            with z.open(entry) as src:
                fromzip[name]=file_hash(src)
    current={}
    for family in FAMILIES:
        folder=BASE/family
        assert folder.is_dir(),folder
        for p in folder.rglob("*.lean"):
            name=p.relative_to(BASE).as_posix()
            current[name]=sha(p)
    assert all(any(name.startswith(fam+"/") for name in fromzip)
             for fam in FAMILIES),("Missing required genuine original source family",FAMILIES)
    assert len(fromzip)>=300,("Incomplete genuine original numeric source ancestry",len(fromzip))
    assert set(fromzip)==set(current),(
        "NF728 accepted original source / NF737 full original source family does NOT match",
        len(fromzip),len(current),
        sorted(set(fromzip)-set(current))[:20],
        sorted(set(current)-set(fromzip))[:20])
    assert fromzip==current,"Actual original generated NF702/NF703/NF681 source file SHA mismatch"
    assert "NF702Inputs/Data.lean" in fromzip
    assert "NF703Cache/Data.lean" in fromzip
    assert "NF703Cache/Frontier.lean" in fromzip
    assert any(name.startswith("NF681/Col056.lean") for name in fromzip)
    return current

def install_accepted_compiled_objects():
    assert sha(OBJECT_ZIP)==EXPECTED_OBJ_DIGEST,"NF729 successful original compiled object ZIP mismatch"
    LIB.mkdir(parents=True,exist_ok=True)
    written={}
    existing={}
    with zipfile.ZipFile(OBJECT_ZIP) as z:
        eligible=[]
        for entry in z.infolist():
            if entry.is_dir() or not entry.filename.endswith(".olean"):
                continue
            path=entry.filename
            marker="WeilDefect/"
            ix=path.find(marker)
            assert ix>=0 and ".lake/build/lib/lean/" in path[:ix],(
                "Unexpected path for accepted original Lean object",path)
            relative=Path(path[ix+len(marker):])
            assert ".." not in relative.parts and not relative.is_absolute()
            eligible.append((entry,relative))
        assert len(eligible)>=20,len(eligible)
        # The capsule provides ALL original upstream Lean theorem/dependency
        # objects to preserve import closure. Only source-provenance-identical
        # NF702/NF703/NF681 families are used as original numeric inputs.
        for entry,rel in eligible:
            target=LIB/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.is_file():
                with z.open(entry) as src:
                    accepted_hash=file_hash(src)
                assert sha(target)==accepted_hash,(
                    "Overlapping original compiled proof object is not byte-identical",str(rel))
                existing[str(rel)]=accepted_hash
                continue
            with z.open(entry) as src,target.open("wb") as dst:
                shutil.copyfileobj(src,dst,length=1024*1024)
            assert target.stat().st_size>0,(entry.filename,target)
            written[str(rel)]=sha(target)
    all_objects={**written,**existing}
    # Those exact objects were genuinely kernel-accepted in an original
    # source-bound NF729 job, not synthesized from arbitrary .olean files.
    required=(
        "Generated/NF702Inputs/Data.olean",
        "Generated/NF703Cache/Data.olean",
    )
    assert all(key in all_objects for key in required),(
        "Accepted original compiled object archive lacks complete original center cache",
        list(required),len(all_objects))
    assert len(all_objects)==len(eligible)
    for family in ("NF702Inputs","NF703Cache"):
        assert sum(x.startswith("Generated/"+family+"/")
                   for x in all_objects)>=2,(family,"incomplete original source cache objects")
    return written,existing

def ingest():
    sources=assert_original_source_matches()
    new,reused=install_accepted_compiled_objects()
    meta={
      "schema":"NF743-original-cache-source-equal-to-NF728-accepted-lean-object-v1",
      "old_original_source_run_id":OLD_RUN_ID,
      "old_original_source_artifact_id":OLD_SOURCE_ARTIFACT_ID,
      "old_original_source_archive_sha256":EXPECTED_SRC_DIGEST,
      "accepted_NF729_original_numerical_run_id":ACCEPTED_OBJECT_RUN_ID,
      "accepted_NF729_original_numerical_quad_job_id":ORIGINAL_KERNEL_JOB_ID,
      "accepted_NF729_original_numerical_quad_artifact_id":ACCEPTED_OBJECT_ARTIFACT_ID,
      "accepted_NF729_numerical_olean_archive_sha256":EXPECTED_OBJ_DIGEST,
      "source_manifest_sha256":sha(FULL_SOURCE),
      "verified_against_original_NF728_complete_source_bank":True,
      "accepted_NF729_original_numeric_quad_000_job_success":True,
      "accepted_NF729_compiled_olean_source_match":True,
      "matched_original_source_files_sha256":sources,
      "matched_original_source_file_count":len(sources),
      "accepted_compiled_original_center_modules":
          sum(x.startswith("Generated/NF703Cache/")
              for x in list(new)+list(reused)),
      "reused_accepted_original_lean_object_sha256":new,
      "preexisting_byte_identical_accepted_lean_object_sha256":reused,
      "accepted_source_equal_original_cache_only":True,
      "new_original_indexzero_numerical_gate_accepted":False,
      "full_global_original_matrix_closed":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "scope":"Only cache reuse from accepted NF729 original numerical Lean job with byte-identical NF728 vs NF737 frozen numerical sources. Actual NF743 HD/A indices 56..63 require separate Lean kernels and axioms."
    }
    OUTPUT.write_text(json.dumps(meta,indent=2,sort_keys=True)+"\n")
    print("NF743 original NF703 Lean cache: exact NF728/NF737 source file hashes",len(sources),
          "PASS; only successful NF729 original numerical compiled .olean files accepted",
          len(new),"new +",len(reused),"byte-identical reuse, center modules",
          meta["accepted_compiled_original_center_modules"],
          "; NEW original 056–063 numerical gates not yet proved")

def check():
    assert OUTPUT.is_file()
    m=json.loads(OUTPUT.read_text())
    assert m["schema"]=="NF743-original-cache-source-equal-to-NF728-accepted-lean-object-v1"
    assert m["source_manifest_sha256"]==sha(FULL_SOURCE)
    assert m["accepted_NF729_original_numerical_quad_job_id"]==ORIGINAL_KERNEL_JOB_ID
    assert m["accepted_NF729_original_numerical_quad_artifact_id"]==ACCEPTED_OBJECT_ARTIFACT_ID
    assert m["verified_against_original_NF728_complete_source_bank"] is True
    assert m["accepted_NF729_compiled_olean_source_match"] is True
    assert m["matched_original_source_file_count"]>=300
    assert m["new_original_indexzero_numerical_gate_accepted"] is False
    for name,digest in {**m["reused_accepted_original_lean_object_sha256"],
                        **m["preexisting_byte_identical_accepted_lean_object_sha256"]}.items():
        assert sha(LIB/name)==digest,(name,digest)
    assert (LIB/"Generated/NF703Cache/Data.olean").stat().st_size>1024
    assert (LIB/"Generated/NF702Inputs/Data.olean").stat().st_size>1024
    print("NF743 accepted original compiled cache objects and exact current original source SHA custody PASS; independent numerical kernel still required")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("ingest","check"))
    a=p.parse_args()
    if a.stage=="ingest":ingest()
    else:check()
