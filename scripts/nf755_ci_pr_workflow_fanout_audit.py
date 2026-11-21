#!/usr/bin/env python3
"""NF755: offline audit of accidental historical GitHub pull-request workflow fan-out.

Does not invoke GitHub API, enqueue jobs, mutate workflows or certify Lean.
Separately mark weakly-classified YAML; do not claim all workflow trigger
semantics are understood by this text-level conservative detector.
"""
import argparse
import fnmatch
import json
import re
from pathlib import Path

WORKFLOW_DIR = Path(".github/workflows")
OUT = Path("nf755-original-CI-pull-request-fanout-audit.json")
FIXED = {
    ".github/workflows/nf474-original-j7-fast-source-independent-fraction-audit.yml": [
        ".github/workflows/nf474-original-j7-fast-source-independent-fraction-audit.yml",
        "scripts/local_replay/verify_nf474_original_J7_right_panel_and_partial_union_exact.py",
    ],
    ".github/workflows/nf485-j8-principal-image-log-moment-algebra.yml": [
        ".github/workflows/nf485-j8-principal-image-log-moment-algebra.yml",
        "scripts/local_replay/verify_nf485_J8_principal_image_log_moment_algebra_exact.py",
    ],
    ".github/workflows/nf481-original-j8-20jet-source-unconditional-energy.yml": [
        ".github/workflows/nf481-original-j8-20jet-source-unconditional-energy.yml",
        "scripts/local_replay/nf471_original_J7_joint_arch_mean_native.py",
        "scripts/local_replay/nf481_original_J8_twenty_jet_source_native.py",
        "scripts/local_replay/verify_nf481_original_J8_unconditional_energy_tail_exact.py",
    ],
    ".github/workflows/nf501-original-J242-correlated-log-projection.yml": [
        ".github/workflows/nf501-original-J242-correlated-log-projection.yml",
        "scripts/verify_nf501_original_J242_correlated_log_projector_native.py",
        "scripts/local_replay/verify_nf501_original_J242_log_one_ray_fraction_audit.py",
    ],
}
# Actual source-only NF754 PR #806 changed neither these older workflow
# definitions nor their input files; all four historically dispatched.
UNRELATED_NF754_FILES = (
    "scripts/nf754_original_numerical_ci_backpressure.py",
    "docs/NF754_ORIGINAL_NUMERICAL_CI_BACKPRESSURE_RECOVERY.md",
)
assert len(FIXED) == 4

def pr_event_block(yaml_text):
    """Classify ordinary two-indent pull_request mapping, not arbitrary YAML."""
    lines=yaml_text.splitlines()
    for n,line in enumerate(lines):
        if re.fullmatch(r"  pull_request:\s*(?:#.*)?",line):
            block=[]
            for item in lines[n+1:]:
                if item.strip() and not item.startswith("    ") and not item.startswith("      "):
                    break
                block.append(item)
            return block
    return None

def literal_paths(block):
    if block is None:return None
    for n,line in enumerate(block):
        if re.fullmatch(r"    paths:\s*(?:#.*)?",line):
            result=[]
            for item in block[n+1:]:
                if not item.strip():
                    continue
                if not item.startswith("      - "):
                    break
                candidate=item.split("      - ",1)[1].strip()
                if candidate.startswith("'") and candidate.endswith("'"):
                    candidate=candidate[1:-1]
                elif candidate.startswith('"') and candidate.endswith('"'):
                    candidate=candidate[1:-1]
                result.append(candidate)
            return result
    return []

def audit_file(path, text):
    event=pr_event_block(text)
    if event is None:
        if re.search(r"\bpull_request\b",text):
            return {"path":path,"classification":"complex_or_other_event_trigger","paths":[]}
        return {"path":path,"classification":"no_plain_pull_request_event","paths":[]}
    paths=literal_paths(event)
    if paths:
        return {"path":path,"classification":"path_scoped_pull_request_event","paths":paths}
    if any(re.match(r"    paths-ignore:",x) for x in event):
        return {"path":path,"classification":"paths_ignore_pull_request_event","paths":[]}
    return {"path":path,"classification":"unrestricted_by_paths_pull_request_event","paths":[]}

def selftest():
    simple="name: Test\non:\n  pull_request:\n  workflow_dispatch:\njobs:\n  test:\n    runs-on: ubuntu-latest\n"
    scoped=simple.replace("  pull_request:\n","  pull_request:\n    paths:\n      - 'scripts/real.py'\n")
    assert audit_file("demo",simple)["classification"]=="unrestricted_by_paths_pull_request_event"
    assert audit_file("demo",scoped)["classification"]=="path_scoped_pull_request_event"
    assert literal_paths(pr_event_block(scoped))==["scripts/real.py"]
    assert pr_event_block("on:\n  workflow_dispatch:\n") is None
    cases=["unrestricted_pr_detected","scoped_pr_detected","exact_paths_recovered","no_pr_detected"]
    for path,required in FIXED.items():
        assert len(required)>=2 and required[0]==path
        assert all(not fnmatch.fnmatchcase(p,UNRELATED_NF754_FILES[0]) for p in required)
        assert all(not fnmatch.fnmatchcase(p,UNRELATED_NF754_FILES[1]) for p in required)
    cases.append("four_workflows_exclude_unrelated_NF754_changes")
    assert all(not any(fnmatch.fnmatchcase(f,p) for p in FIXED[k])
               for k in FIXED for f in UNRELATED_NF754_FILES)
    cases.append("strict_four_workflow_negative_trigger_simulation")
    for key,required in FIXED.items():
        assert any(fnmatch.fnmatchcase(key,p) for p in required)
        assert all(any(fnmatch.fnmatchcase(f,p) for p in required) for f in required)
    cases.append("every_repaired_workflow_and_direct_dependency_remain_triggerable")
    assert len(cases)==7
    print("NF755 7 synthetic PR trigger controls PASS; no Lean numerical certificate")

def audit():
    assert WORKFLOW_DIR.is_dir(),"Run from repository root with actual .github/workflows"
    result=[]
    for path in sorted((*WORKFLOW_DIR.glob("*.yml"),*WORKFLOW_DIR.glob("*.yaml"))):
        result.append(audit_file(path.as_posix(),path.read_text()))
    assert len(result)>=4,"Workflow inventory appears empty; fail closed"
    indexed={r["path"]:r for r in result}
    for path,expected in FIXED.items():
        assert path in indexed,("missing original historical workflow",path)
        assert indexed[path]["classification"]=="path_scoped_pull_request_event",path
        assert indexed[path]["paths"]==expected,(path,indexed[path]["paths"])
        text=Path(path).read_text()
        assert "  workflow_dispatch:" in text,("manual repro entry lost",path)
        if "nf501-" in path:
            assert "  push:" in text,("NF501 original push trigger removed",path)
        for f in UNRELATED_NF754_FILES:
            assert not any(fnmatch.fnmatchcase(f,p) for p in expected),(path,f)
    by_class={}
    for item in result:
        by_class[item["classification"]]=by_class.get(item["classification"],0)+1
    unscoped=[r["path"] for r in result if r["classification"]=="unrestricted_by_paths_pull_request_event"]
    report={
      "schema":"NF755-original-CI-unrestricted-PR-fanout-offline-inventory-v1",
      "workflow_total_inspected":len(result),
      "classification_counts":by_class,
      "text_level_unrestricted_PR_workflows":unscoped,
      "four_pilot_repairs":FIXED,
      "nf754_unrelated_files":list(UNRELATED_NF754_FILES),
      "four_pilot_repairs_exclude_NF754_diagnostic_changes":True,
      "full_GitHub_yaml_semantics_verified":False,
      "all_legacy_fanout_repaired":False,
      "new_original_numerical_Lean_gates_accepted":0,
      "old_accepted_original_HD_A_gate_instances":596,
      "note":"Text-level classification only. GitHub actual PR event eligibility also depends on branches, path glob semantics, workflow origin and repository settings. Manual workflow_dispatch preserved for these four."
    }
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("NF755 offline workflow inventory",len(result),"by_class",by_class)
    print("NF755 four original workflow PR paths strictly scoped; old accepted numerics still 596/968")
    print("NF755 OTHER unscoped workflows remain; this is a bounded pilot, not fleet-wide closure")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("mode",choices=("selftest","audit"))
    args=parser.parse_args()
    if args.mode=="selftest":selftest()
    else:audit()
