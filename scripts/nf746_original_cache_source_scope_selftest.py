#!/usr/bin/env python3
"""NF746: source-only synthetic negative tests for repaired NF743 cache equality.

These tests use fake LOCAL files and a fake historical ZIP. They never
authenticate any real original Lean theorem, historical archive, or .olean.
The separate real NF743 kernel workflow must still pass independently.
"""
import hashlib
import importlib.util
import json
import tempfile
import warnings
import zipfile
from pathlib import Path

MODULE_PATH=Path(__file__).with_name("nf743_reuse_accepted_original_nf703_cache.py")
spec=importlib.util.spec_from_file_location("nf743_cache_source",MODULE_PATH)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

CACHE={
    "NF702Inputs/Data.lean":"-- literal frozen original inputs\n",
    "NF703Cache/Data.lean":"-- literal frozen original center data\n",
    "NF703Cache/Frontier.lean":"-- original center frontier\n",
}
RECEIPT=Path("nf746-original-cache-source-scope-selftest.json")

def setup(root):
    generated=root/"WeilDefect"/"Generated"
    for name,contents in CACHE.items():
        p=generated/name
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(contents)
    for i in range(242):
        p=generated/"NF681"/f"Col{i:03d}.lean"
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(f"-- genuine NF737 local source candidate {i}\n")
    frontier=generated/"NF704Frontier"/"manifest.json"
    frontier.parent.mkdir(parents=True,exist_ok=True)
    frontier.write_text(json.dumps({"test":"synthetic only"}))
    mod.BASE=generated
    mod.FULL_SOURCE=frontier
    mod.SOURCE_ZIP=root/"old-NF728-source.zip"
    return generated

def archive(files,rooted=True):
    with zipfile.ZipFile(mod.SOURCE_ZIP,"w") as z:
        for name,content in files.items():
            z.writestr(("WeilDefect/Generated/" if rooted else "")+name,content)
    mod.EXPECTED_SRC_DIGEST=hashlib.sha256(mod.SOURCE_ZIP.read_bytes()).hexdigest()

def rejects():
    try:
        mod.assert_original_source_matches()
    except AssertionError:
        return True
    return False

def run():
    tests=[]
    with tempfile.TemporaryDirectory(prefix="nf746-scope-") as d:
        generated=setup(Path(d))
        archive(CACHE)
        cache,old_local,new_local=mod.assert_original_source_matches()
        assert len(cache)==3 and not old_local and len(new_local)==242
        tests.append("historic_cache_without_NF681_is_valid_cache_only")

        archive(CACHE,rooted=False)
        assert len(mod.assert_original_source_matches()[0])==3
        tests.append("accepted_upload_artifact_rootless_layout")

        archive(CACHE)
        altered=generated/"NF703Cache"/"Data.lean"
        altered.write_text("wrong current source")
        assert rejects()
        altered.write_text(CACHE["NF703Cache/Data.lean"])
        tests.append("byte_mismatched_cache_rejected")

        extra=generated/"NF703Cache"/"Injected.lean"
        extra.write_text("bad extra source")
        assert rejects()
        extra.unlink()
        tests.append("extra_current_cache_module_rejected")

        archive({k:v for k,v in CACHE.items() if k!="NF703Cache/Data.lean"})
        assert rejects()
        tests.append("missing_historical_required_cache_module_rejected")

        archive(CACHE)
        victim=generated/"NF681"/"Col056.lean"
        original=victim.read_text()
        victim.unlink()
        assert rejects()
        victim.write_text(original)
        tests.append("missing_separate_full_NF737_local_source_rejected")

        archive({**CACHE,"NF681/Col056.lean":"not source-equal"})
        assert rejects()
        tests.append("historical_optional_NF681_overlap_mismatch_rejected")

        archive({**CACHE,"NF681/Col056.lean":original})
        _,overlap,localsrc=mod.assert_original_source_matches()
        assert len(overlap)==1 and len(localsrc)==242
        tests.append("matching_optional_NF681_overlap_checked")

    out={
        "schema":"NF746-synthetic-cache-source-scope-selftest-v1",
        "passed_cases":tests,
        "real_original_NF728_NF737_artifact_compared":False,
        "real_original_numerical_Lean_kernel_checked":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False
    }
    RECEIPT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("NF746 synthetic source-scope tests PASS:",len(tests),"; original Lean kernel remains separate")

if __name__=="__main__":
    run()
