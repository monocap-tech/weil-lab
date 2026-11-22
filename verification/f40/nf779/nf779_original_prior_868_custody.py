#!/usr/bin/env python3
"""NF779 source-only predecessor metadata gate. Never promotes a new Lean gate."""
import json
import os
import urllib.request
from pathlib import Path

RUN, JOB, ART = 45068094592, 137348682303, 14772855150
MAIN_SHA = "ce3c9a11d40144ca7452e4e857db25d0af0320dd"
SOURCE_SHA = "a431f903254000bb5ad8edbc276ccc8599da98f5"
DIGEST = "02798a1191d52b47d48cf3718df7c8940e90d40b37ea29958214ffa95b63de00"
NAME = "nf778-original-source-identical-cache-real-global-HD-A-184-191-Lean-kernel-audit"
COMPILE = "Direct kernel-compile eight actual original frozen NF702 NF703 global HD/A indexzero Col184 through Col191 gate source modules"
AXIOMS = "Strict 35-name original source-bound Lean theorem axiom and accepted prior cache-object audit"

def validate(run, jobs, artifacts):
    assert run["id"] == RUN and run["status"] == "completed"
    assert run["conclusion"] == "success" and run["event"] == "push"
    assert run["path"] == ".github/workflows/f40-nf778-single-lane.yml"
    assert run["head_sha"] == MAIN_SHA and run["head_branch"] == "main"
    assert run["run_attempt"] == 1
    j = [x for x in jobs["jobs"] if x["id"] == JOB]
    assert len(j) == 1 and j[0]["conclusion"] == "success"
    steps = j[0]["steps"]
    for name in (COMPILE, AXIOMS):
        assert sum(s["name"] == name and s["conclusion"] == "success" for s in steps) == 1
    a = [x for x in artifacts["artifacts"] if x["id"] == ART]
    assert len(a) == 1
    assert a[0]["name"] == NAME and a[0]["digest"] == "sha256:" + DIGEST
    assert a[0]["size_in_bytes"] == 53415 and a[0]["expired"] is False
    return {
        "schema": "NF779-live-NF778-868-metadata-nonpromoting-v1",
        "previous_accepted_original_HD_A_gates": 868,
        "previous_original_source_sha": SOURCE_SHA,
        "previous_successful_run_id": RUN,
        "previous_successful_job_id": JOB,
        "previous_source_bound_artifact_id": ART,
        "previous_archive_metadata_sha256": DIGEST,
        "new_indexzero_HD_candidate": list(range(192, 200)),
        "new_indexzero_A_candidate": list(range(192, 200)),
        "new_candidate_gate_instances": 16,
        "source_archive_bytes_independently_revalidated_by_this_script": False,
        "new_original_Lean_gates_accepted": False,
        "F41_complete_242x242_accepted": False,
        "F42_original_signed_Weil_accepted": False,
        "RH_proved": False,
    }

def fetch(endpoint):
    token = os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com/repos/monocap-tech/weil-lab/" + endpoint,
        headers={"Accept": "application/vnd.github+json",
                 "Authorization": "Bearer " + token,
                 "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        assert resp.status == 200
        return json.load(resp)

def live():
    data = validate(
        fetch(f"actions/runs/{RUN}"),
        fetch(f"actions/runs/{RUN}/jobs?per_page=100"),
        fetch(f"actions/runs/{RUN}/artifacts?per_page=100"))
    Path("nf779-prior868-live-metadata.json").write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("NF779 prior accepted 868: live GitHub run/job/artifact metadata PASS; no new Lean gate.")

def selftest():
    r = {"id": RUN, "status": "completed", "conclusion": "success", "event": "push", "head_sha": MAIN_SHA, "head_branch": "main",
         "path": ".github/workflows/f40-nf778-single-lane.yml", "run_attempt": 1}
    j = {"jobs": [{"id": JOB, "conclusion": "success", "steps": [{"name": COMPILE, "conclusion": "success"},
                                                                   {"name": AXIOMS, "conclusion": "success"}]}]}
    a = {"artifacts": [{"id": ART, "name": NAME, "digest": "sha256:" + DIGEST,
                         "size_in_bytes": 53415, "expired": False}]}
    assert validate(r, j, a)["new_original_Lean_gates_accepted"] is False
    for d, k, wrong in ((r, "conclusion", "failure"), (r, "head_sha", "0" * 40),
                        (j["jobs"][0]["steps"][1], "conclusion", "failure"),
                        (a["artifacts"][0], "digest", "sha256:" + "0" * 64)):
        old = d[k]
        d[k] = wrong
        try:
            validate(r, j, a)
        except AssertionError:
            pass
        else:
            raise AssertionError("invalid predecessor metadata accepted: " + k)
        d[k] = old
    print("NF779 synthetic source-only predecessor refusal tests PASS; NO Lean.")

if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 2 and sys.argv[1] in ("live", "selftest")
    live() if sys.argv[1] == "live" else selftest()
