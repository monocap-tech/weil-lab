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
FAMILIES=("NF702Inputs","NF703Cache")  # cached source ancestry only
LOCAL_FAMILY="NF681"  # NF737 source verified independently, not assumed in NF728
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
    """Require exact byte-identical old/new CACHE sources, not unrelated NF681.

    NF728's original index-one proof used the NF700 packed blocks. Its source
    archive need not contain NF737's later index-zero NF681 local source bank.
    Absence of that unrelated family must not be confused with a difference
    in the immutable old NF702/NF703 cache source.
    """
    assert sha(SOURCE_ZIP)==EXPECTED_SRC_DIGEST, "Immutable NF728 original source ZIP artifact digest mismatch"
    assert FULL_SOURCE.is_file()
    fromzip={}
    historic_local={}
    with zipfile.ZipFile(SOURCE_ZIP) as z:
        for entry in z.infolist():
            if entry.is_dir() or not entry.filename.endswith(".lean"):
                continue
            path=entry.filename
            marker="WeilDefect/Generated/"
            # Account for exactly the two GitHub upload-artifact root layouts.
            if marker in path:
                name=path[path.index(marker)+len(marker):]
            elif path.startswith(tuple(fam+"/" for fam in FAMILIES+(LOCAL_FAMILY,))):
                name=path
            else:
                continue
            assert ".." not in Path(name).parts and not Path(name).is_absolute(),name
            if any(name.startswith(family+"/") for family in FAMILIES):
                dest=fromzip
            elif name.startswith(LOCAL_FAMILY+"/"):
                dest=historic_local
            else:
                continue
            assert name not in dest,(name,"duplicate historic source")
            with z.open(entry) as src:
                dest[name]=file_hash(src)

    current={}
    for family in FAMILIES:
        folder=BASE/family
        assert folder.is_dir(),folder
        for p in folder.rglob("*.lean"):
            name=p.relative_to(BASE).as_posix()
            current[name]=sha(p)
    historical_families={
        family:sum(k.startswith(family+"/") for k in fromzip)
        for family in FAMILIES
    }
    assert all(historical_families.values()),(
        "NF728 lacks REQUIRED accepted original center/input cache family",
        historical_families,sorted(fromzip)[:12],sorted(historic_local)[:12])
    assert len(fromzip)>=3,(
        "NF728 accepted center/input cache source corpus incomplete",len(fromzip))
    assert set(fromzip)==set(current),(
        "Historical NF728 vs current NF737 source-set mismatch for reused CACHE ONLY",
        len(fromzip),len(current),
        sorted(set(fromzip)-set(current))[:20],
        sorted(set(current)-set(fromzip))[:20])
    assert fromzip==current,(
        "Actual original NF702/NF703 cache source SHA mismatch",
        [x for x in fromzip if fromzip[x]!=current[x]][:20])
    for required in ("NF702Inputs/Data.lean",
                     "NF703Cache/Data.lean","NF703Cache/Frontier.lean"):
        assert required in fromzip,("Required genuine original cache source missing",required)

    # The separate preceding NF737 verify step authenticates all original
    # NF681 local sources. Do not attribute this family to NF728.
    local={}
    folder=BASE/LOCAL_FAMILY
    assert folder.is_dir(),folder
    for p in folder.rglob("*.lean"):
        local[p.relative_to(BASE).as_posix()]=sha(p)
    assert all(f"NF681/Col{i:03d}.lean" in local for i in range(242)),(
        "Full genuine NF737 NF681 local source corpus missing",len(local))
    for name,digest in historic_local.items():
        assert name in local and local[name]==digest,(
            "Optional overlapping NF728/NF737 NF681 source differs",name)
    return current,historic_local,local

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
    sources,old_local,current_local=assert_original_source_matches()
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
      "cache_source_families_exactly_verified":["NF702Inputs","NF703Cache"],
      "compared_entire_NF728_archive_to_NF737":False,
      "historical_NF681_overlapping_files_compared":len(old_local),
      "current_NF737_NF681_local_source_files":len(current_local),
      "NF681_local_corpus_distinct_from_cache_reuse_claim":True,
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
      "scope":"Cache-only NF702Inputs/NF703Cache byte equivalence from accepted NF728 to NF737, optional historical NF681 overlap, and separate NF737-verified 242 NF681 original local sources. No new NF743 HD/A 56..63 numerical kernel theorem is inferred."
    }
    OUTPUT.write_text(json.dumps(meta,indent=2,sort_keys=True)+"\n")
    print("NF746 repaired NF743 cache: exact NF728/NF737 NF702/NF703 cache source hashes",len(sources),
          "PASS; optional historic NF681 overlap",len(old_local),"independent NF737 NF681 sources",len(current_local),
          "; only successful NF729 original numerical compiled .olean files accepted",
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
    assert m["matched_original_source_file_count"]>=3
    assert m["cache_source_families_exactly_verified"]==["NF702Inputs","NF703Cache"]
    assert m["compared_entire_NF728_archive_to_NF737"] is False
    assert m["current_NF737_NF681_local_source_files"]>=242
    assert m["NF681_local_corpus_distinct_from_cache_reuse_claim"] is True
    assert m["new_original_indexzero_numerical_gate_accepted"] is False
    for name,digest in {**m["reused_accepted_original_lean_object_sha256"],
                        **m["preexisting_byte_identical_accepted_lean_object_sha256"]}.items():
        assert sha(LIB/name)==digest,(name,digest)
    assert (LIB/"Generated/NF703Cache/Data.olean").stat().st_size>1024
    assert (LIB/"Generated/NF702Inputs/Data.olean").stat().st_size>1024
    print("NF746 recovered NF743 accepted original cache objects, exact NF702/NF703 source SHA; NF681 separate source custody; numerical kernel still required")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("ingest","check"))
    a=p.parse_args()
    if a.stage=="ingest":ingest()
    else:check()
