#!/usr/bin/env python3
"""NF756: offline direct-source PR fan-out guard; NOT a numerical Lean audit.

This checks only a frozen set of historically unrestricted legacy PR workflows.
Manual workflow_dispatch allows intentional runs for transitive dependency edits.
GitHub's full YAML event semantics, branch settings and actual runner queue are
not proved by this parser.
"""
import argparse
import json
import re
from pathlib import Path

DEFINITIONS = {
  ".github/workflows/nf470-original-j7-native-regular-mean-joint-nodes.yml": [
    ".github/workflows/nf470-original-j7-native-regular-mean-joint-nodes.yml",
    "scripts/local_replay/nf470_original_J7_native_regular_mean_and_joint_point.py",
    "scripts/local_replay/verify_nf470_original_J7_second_signed_island_exact.py"
  ],
  ".github/workflows/nf473-original-j7-left-panel-correlated-signed-moments.yml": [
    ".github/workflows/nf473-original-j7-left-panel-correlated-signed-moments.yml",
    "scripts/local_replay/nf471_original_J7_joint_arch_mean_native.py",
    "scripts/local_replay/nf473_original_J7_left_macro_signed_native.py",
    "scripts/local_replay/verify_nf473_original_J7_left_panel_and_partial_union_exact.py"
  ],
  ".github/workflows/nf474-original-j7-right-panel-correlated-signed-moments.yml": [
    ".github/workflows/nf474-original-j7-right-panel-correlated-signed-moments.yml",
    "scripts/local_replay/nf471_original_J7_joint_arch_mean_native.py",
    "scripts/local_replay/nf474_original_J7_right_macro_signed_native.py",
    "scripts/local_replay/nf474_original_J7_left_boundary_compact_joint_native.py",
    "scripts/local_replay/verify_nf474_original_J7_right_panel_and_partial_union_exact.py"
  ],
  ".github/workflows/nf493-original-J8-400-source-log-square.yml": [
    ".github/workflows/nf493-original-J8-400-source-log-square.yml",
    "scripts/local_replay/nf493_original_J8_400_true_source_log_jets_native.py",
    "scripts/local_replay/verify_nf493_original_J8_400_source_log_square_exact.py"
  ],
  ".github/workflows/nf500-original-J242-all-mixed-log-source-exact.yml": [
    ".github/workflows/nf500-original-J242-all-mixed-log-source-exact.yml",
    "scripts/local_replay/nf500_original_J242_full_smooth_log_mixed_source_native.py",
    "scripts/local_replay/verify_nf500_original_J242_all_smooth_log_moments_source_exact.py"
  ],
  ".github/workflows/nf455-original-j78-projection-floor.yml": [
    ".github/workflows/nf455-original-j78-projection-floor.yml",
    "scripts/local_replay/verify_nf455_projection_energy_floor.py"
  ],
  ".github/workflows/nf462-original-forced-j7-sign.yml": [
    ".github/workflows/nf462-original-forced-j7-sign.yml",
    "scripts/local_replay/verify_nf462_original_j7_required_signed_deficit.py"
  ],
  ".github/workflows/nf466-j7-correlated-moment-algebra.yml": [
    ".github/workflows/nf466-j7-correlated-moment-algebra.yml",
    "scripts/local_replay/verify_nf466_j7_correlated_moment_identity.py"
  ],
  ".github/workflows/nf467-j7-mean-operator-algebra.yml": [
    ".github/workflows/nf467-j7-mean-operator-algebra.yml",
    "scripts/local_replay/verify_nf467_j7_mean_operator_identity.py"
  ],
  ".github/workflows/nf468-j7-original-mean-coarse-enclosure.yml": [
    ".github/workflows/nf468-j7-original-mean-coarse-enclosure.yml",
    "scripts/local_replay/verify_nf468_j7_original_mean_coarse_enclosure.py"
  ],
  ".github/workflows/nf469-j7-native-jet-order-gate.yml": [
    ".github/workflows/nf469-j7-native-jet-order-gate.yml",
    "scripts/local_replay/verify_nf469_j7_native_jet_order_gate.py"
  ]
}
OUT = Path("nf756-pr-trigger-scope-source-audit.json")
DIAGNOSTIC_FILES = (
    "scripts/nf754_original_numerical_ci_backpressure.py",
    "docs/NF754_ORIGINAL_NUMERICAL_CI_BACKPRESSURE_RECOVERY.md",
    "scripts/nf755_ci_pr_workflow_fanout_audit.py",
    "docs/NF755_GITHUB_ACTIONS_PR_FANOUT_SCOPING_AND_ORIGINAL_LEAN_CUSTODY.md",
)
assert len(DEFINITIONS)==11

def exact_paths(text):
    lines = text.splitlines()
    found = [i for i,line in enumerate(lines) if line == "  pull_request:"]
    assert len(found)==1,("expected one literal PR trigger",found)
    n=found[0]
    assert n+1<len(lines) and lines[n+1]=="    paths:"
    out=[]
    for line in lines[n+2:]:
        if not line.startswith("      - "):
            break
        assert re.fullmatch(r"      - '[^']+'",line),line
        out.append(line[9:-1])
    assert out and len(out)==len(set(out))
    return out

def selftest():
    base="name: test\non:\n  pull_request:\n    paths:\n      - 'script.py'\n  workflow_dispatch:\njobs:\n  check:\n    runs-on: ubuntu-latest\n"
    assert exact_paths(base)==["script.py"]
    cases=["literal_scoped_pr_parser"]
    for v in DIAGNOSTIC_FILES:
        for _,paths in DEFINITIONS.items():
            assert v not in paths
    cases.append("four_diagnostic_changes_excluded_by_all_11")
    for p,paths in DEFINITIONS.items():
        assert paths[0]==p
        assert len(paths)>=2
        assert len(paths)==len(set(paths))
    cases.append("direct_original_workflow_always_in_own_scope")
    assert len(set(DEFINITIONS))==11
    cases.append("distinct_11_workflows")
    for p,paths in DEFINITIONS.items():
        assert all(x.startswith("scripts/") for x in paths[1:])
    cases.append("only_direct_python_source_dependencies")
    try:
        exact_paths(base.replace("    paths:\n",""))
    except AssertionError:
        cases.append("unscoped_PR_rejected")
    else:
        raise AssertionError("bare PR event was accepted")
    assert len(cases)==6
    print("NF756 six source-only synthetic trigger checks PASS; NO Lean theorem is certified")

def audit():
    rows=[]
    for path,required in DEFINITIONS.items():
        f=Path(path)
        assert f.is_file(),("workflow not checked out",path)
        s=f.read_text()
        got=exact_paths(s)
        assert got==required,(path,got,required)
        assert "  workflow_dispatch:\n" in s
        assert "\njobs:\n" in s
        for source in required[1:]:
            assert Path(source).is_file(),("direct input script missing",path,source)
        assert not any(v in got for v in DIAGNOSTIC_FILES)
        rows.append({"workflow":path,"verified_auto_PR_paths":got,
                     "manual_dispatch_preserved":True,
                     "direct_scripts_exist":True,
                     "new_original_Lean_gates_accepted":0})
    out={"schema":"NF756-second-wave-11-legacy-workflows-direct-PR-scopes-v1",
         "workflows_scoped_by_this_wave":len(rows),
         "verified_direct_path_scopes":rows,
         "synthetic_unrelated_PR_files_excluded":list(DIAGNOSTIC_FILES),
         "prior_NF755_scoped_workflows":4,
         "fleet_wide_complete":False,
         "GitHub_runner_queue_reduction_measured":False,
         "historical_preexisting_queued_runs_cancelled":False,
         "old_accepted_original_HD_A_gates":596,
         "new_actual_original_numeric_Lean_acceptances":0,
         "full_GitHub_workflow_semantics_proved":False,
         "caveat":"PR paths can skip required checks on unrelated changes. Manual dispatch retained for transitive dependencies and explicit verification, subject to branch-protection configuration."}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("NF756 exact source-only PR scopes PASS",len(rows),"historical workflows; numerics 596/968 unchanged")
    print("No actual GitHub CI fan-out reduction, global Weil positivity or RH has been established")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("mode",choices=("selftest","audit"))
    args=p.parse_args()
    if args.mode=="selftest":
        selftest()
    else:
        audit()
