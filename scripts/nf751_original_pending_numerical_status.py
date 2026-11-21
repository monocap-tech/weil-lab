#!/usr/bin/env python3
"""NF751: fail-closed observation of THREE independently submitted original Lean numerical CI jobs.

This is an OBSERVATION RECEIPT, never numerical gate acceptance.
Even a successful workflow and uploaded artifact only make a stage eligible
for independent source/axiom/digest scrutiny, not certified by this script.
"""
import argparse
import json
import os
import subprocess
from pathlib import Path

REPO = "monocap-tech/weil-lab"
OUT = Path("nf751-prior-three-original-numerical-ci-status.json")
TEST = Path("nf751-original-numerical-status-selftest.json")
SPECS = (
    {"stage":"NF748","run":44846764448,"job":136668270768,
     "name":"authenticate-reuse-and-kernel-actual-original-indexzero-064-071",
     "head_sha":"a509af347d6f800dba4b0125542b66ca9c3296f3",
     "artifact":"nf748-original-source-identical-cache-real-global-HD-A-064-071-Lean-kernel-audit",
     "coordinates":[64,71]},
    {"stage":"NF749","run":44847296036,"job":136670051321,
     "name":"authenticate-reuse-and-kernel-actual-original-indexzero-024-031",
     "head_sha":"b428ff2e72e2b1a833ebdc7574510a48f5006669",
     "artifact":"nf749-original-source-identical-cache-real-global-HD-A-024-031-Lean-kernel-audit",
     "coordinates":[24,31]},
    {"stage":"NF750","run":44851970198,"job":136685181507,
     "name":"authenticate-reuse-and-kernel-actual-original-indexzero-072-079",
     "head_sha":"dd3ea7ea37bf870633fd71b501bb080b21fb9eb0",
     "artifact":"nf750-original-source-identical-cache-real-global-HD-A-072-079-Lean-kernel-audit",
     "coordinates":[72,79]},
)
assert len({x["run"] for x in SPECS}) == 3
assert not (set(range(24,32)) & (set(range(64,72)) | set(range(72,80))))

def assess(spec, run, jobs, artifacts):
    assert run.get("id") == spec["run"], ("run ID mismatch",spec["stage"])
    assert run.get("head_sha") == spec["head_sha"], ("head source revision changed",spec["stage"])
    assert run.get("status") in ("queued","waiting","pending","in_progress","completed","requested"),run.get("status")
    matches = [j for j in jobs if j.get("id")==spec["job"] and j.get("name")==spec["name"]]
    assert len(matches)==1, ("missing or ambiguous genuine original numerical job",spec["stage"])
    job=matches[0]
    terminal_success=(
        run.get("status")=="completed" and run.get("conclusion")=="success"
        and job.get("status")=="completed" and job.get("conclusion")=="success"
    )
    strict=[s for s in job.get("steps",[]) if
       "strict" in (s.get("name") or "").lower()
       and ("axiom" in (s.get("name") or "").lower() or "theorem" in (s.get("name") or "").lower())
    ]
    strict_ok = len(strict)==1 and strict[0].get("status")=="completed" and strict[0].get("conclusion")=="success"
    exact = [a for a in artifacts if a.get("name")==spec["artifact"]]
    valid = [a for a in exact if
       isinstance(a.get("id"),int) and a.get("id")>0
       and a.get("expired") is False
       and isinstance(a.get("digest"),str)
       and a["digest"].startswith("sha256:")
       and len(a["digest"])==71
       and all(c in "0123456789abcdef" for c in a["digest"][7:])]
    artifact_ok = len(exact)==len(valid)==1
    readiness = terminal_success and strict_ok and artifact_ok
    blockers=[]
    if not terminal_success:blockers.append("numerical_job_not_success")
    if not strict_ok:blockers.append("strict_axiom_step_not_success")
    if not artifact_ok:blockers.append("immutable_numerical_artifact_missing_or_invalid")
    return {
       "stage":spec["stage"],"original_indexzero_coordinates":spec["coordinates"],
       "run":spec["run"],"run_status":run["status"],"run_conclusion":run.get("conclusion"),
       "job":spec["job"],"job_status":job.get("status"),"job_conclusion":job.get("conclusion"),
       "head_sha":spec["head_sha"],"strict_axiom_step_completed_successfully":strict_ok,
       "artifact_id":valid[0]["id"] if artifact_ok else None,
       "artifact_digest":valid[0]["digest"] if artifact_ok else None,
       "artifact_expired":False if artifact_ok else None,
       "ready_for_separate_source_and_axiom_artifact_review":readiness,
       "blockers":blockers,
       "original_HD_A_gate_instances_promoted_by_this_script":0,
       "LEAN_PASS_certified_by_this_script":False
    }

def call_api(path):
    return json.loads(subprocess.check_output(["gh","api",f"repos/{REPO}/{path}"],text=True))

def live():
    assert os.environ.get("GITHUB_REPOSITORY")==REPO,"wrong repository for numerical custody"
    assert os.environ.get("GH_TOKEN"),"GitHub Actions read token required"
    results=[]
    for spec in SPECS:
        run=call_api(f"actions/runs/{spec['run']}")
        js=call_api(f"actions/runs/{spec['run']}/jobs?per_page=100")
        arts=call_api(f"actions/runs/{spec['run']}/artifacts?per_page=100")
        assert isinstance(js.get("jobs"),list) and isinstance(arts.get("artifacts"),list)
        results.append(assess(spec,run,js["jobs"],arts["artifacts"]))
    receipt={
       "schema":"NF751-observation-not-acceptance-of-prior-original-numerical-batches-v1",
       "historical_accepted_original_HD_A_frontier_gates":596,
       "observed_stages":results,
       "total_original_gate_instances_promoted_by_this_observer":0,
       "global_original_242x242_matrix_complete":False,
       "global_Weil_positivity_proved":False,
       "RH_proved":False,
       "scope":"Actual CI status and artifact metadata only. Source-bound kernel/axiom content, immutable artifact SHA binding, and full numerical acceptance still require independent audit."
    }
    assert len(results)==3 and all(x["LEAN_PASS_certified_by_this_script"] is False for x in results)
    OUT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    for r in results:
        print(r["stage"],"run",r["run_status"],r["run_conclusion"],
              "artifact_ready",r["ready_for_separate_source_and_axiom_artifact_review"],
              "certified_here",False)
    print("NF751 immutable historical acceptance remains 596; no queued/source-only gate promoted")

def selftest():
    spec=SPECS[0]
    run={"id":spec["run"],"head_sha":spec["head_sha"],"status":"queued","conclusion":None}
    job={"id":spec["job"],"name":spec["name"],"status":"queued","conclusion":None,"steps":[]}
    result=assess(spec,run,[job],[])
    assert not result["ready_for_separate_source_and_axiom_artifact_review"] and result["LEAN_PASS_certified_by_this_script"] is False
    cases=["queued_job_rejected"]
    run["status"]="completed";run["conclusion"]="failure"
    job["status"]="completed";job["conclusion"]="failure"
    assert not assess(spec,run,[job],[])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("failed_workflow_rejected")
    run["conclusion"]="success";job["conclusion"]="success"
    assert not assess(spec,run,[job],[])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("success_without_axioms_or_artifact_rejected")
    job["steps"]=[{"name":"Strict 35-name original source-bound Lean theorem axiom audit",
                   "status":"completed","conclusion":"success"}]
    assert not assess(spec,run,[job],[])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("success_without_numerical_artifact_rejected")
    artifact={"name":spec["artifact"],"id":123,"expired":False,"digest":"sha256:"+"a"*64}
    x=assess(spec,run,[job],[artifact])
    assert x["ready_for_separate_source_and_axiom_artifact_review"]
    assert x["LEAN_PASS_certified_by_this_script"] is False
    cases.append("metadata_ready_still_not_certified")
    artifact["expired"]=True
    assert not assess(spec,run,[job],[artifact])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("expired_artifact_rejected")
    artifact["expired"]=False;artifact["digest"]="sha256:invalid"
    assert not assess(spec,run,[job],[artifact])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("bad_digest_rejected")
    try:
       assess(spec,{**run,"head_sha":"wrong"},[job],[])
    except AssertionError:
       cases.append("wrong_source_revision_rejected")
    else:
       raise AssertionError("wrong source accepted")
    assert len(cases)==8
    TEST.write_text(json.dumps({"schema":"NF751-synthetic-status-tests-v1","tests":cases,
                                "not_actual_Lean_or_original_source_certificate":True},indent=2)+"\n")
    print("NF751 eight fail-closed SYNTHETIC status tests passed; not an actual Lean numerical audit")

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("mode",choices=("live","selftest"))
    args=p.parse_args()
    if args.mode=="live":live()
    else:selftest()
