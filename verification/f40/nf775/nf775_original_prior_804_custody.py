#!/usr/bin/env python3
"""NF775 source-only predecessor metadata gate. Never promotes a new Lean gate."""
import json
import os
import urllib.request
from pathlib import Path

RUN, JOB, ART = 45056999890, 137314324604, 14767539019
MAIN_SHA = "270b16fa1a34d4417c0bac911c4ed314eee5183a"
SOURCE_SHA = "a431f903254000bb5ad8edbc276ccc8599da98f5"
DIGEST = "60e9f472b3fd231908a7034914d2ff8b5f0ca602f42a9456e0e4fee5c53a1e3f"
NAME = "nf774-original-source-identical-cache-real-global-HD-A-152-159-Lean-kernel-audit"
COMPILE = "Direct kernel-compile eight actual original frozen NF702 NF703 global HD/A indexzero Col152 through Col159 gate source modules"
AXIOMS = "Strict 35-name original source-bound Lean theorem axiom and accepted prior cache-object audit"

def validate(run, jobs, artifacts):
    assert run["id"] == RUN and run["status"] == "completed"
    assert run["conclusion"] == "success" and run["event"] == "push"
    assert run["path"] == ".github/workflows/f40-nf774-single-lane.yml"
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
    assert a[0]["size_in_bytes"] == 50851 and a[0]["expired"] is False
    return {
        "schema": "NF775-live-NF774-804-metadata-nonpromoting-v1",
        "previous_accepted_original_HD_A_gates": 804,
        "previous_original_source_sha": SOURCE_SHA,
        "previous_successful_run_id": RUN,
        "previous_successful_job_id": JOB,
        "previous_source_bound_artifact_id": ART,
        "previous_archive_metadata_sha256": DIGEST,
        "new_indexzero_HD_candidate": list(range(160, 168)),
        "new_indexzero_A_candidate": list(range(160, 168)),
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
    Path("nf775-prior804-live-metadata.json").write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("NF775 prior accepted 804: live GitHub run/job/artifact metadata PASS; no new Lean gate.")

def selftest():
    r = {"id": RUN, "status": "completed", "conclusion": "success", "event": "push", "head_sha": MAIN_SHA, "head_branch": "main",
         "path": ".github/workflows/f40-nf774-single-lane.yml", "run_attempt": 1}
    j = {"jobs": [{"id": JOB, "conclusion": "success", "steps": [{"name": COMPILE, "conclusion": "success"},
                                                                   {"name": AXIOMS, "conclusion": "success"}]}]}
    a = {"artifacts": [{"id": ART, "name": NAME, "digest": "sha256:" + DIGEST,
                         "size_in_bytes": 50851, "expired": False}]}
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
    print("NF775 synthetic source-only predecessor refusal tests PASS; NO Lean.")

if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 2 and sys.argv[1] in ("live", "selftest")
    live() if sys.argv[1] == "live" else selftest()
