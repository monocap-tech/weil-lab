#!/usr/bin/env python3
"""NF754: read-only live diagnosis of original numerical Lean CI backpressure.

The six prior exact numerical jobs were already submitted. This script does not
submit workflows, cancel other jobs, change sources, or promote any Lean theorem.
It observes GitHub API status and immutable artifact metadata only.
"""
import argparse
import json
import os
import subprocess
from pathlib import Path

from nf753_original_pending_numerical_status import SPECS as PRIOR_FIVE, assess

REPO = "monocap-tech/weil-lab"
OUT = Path("nf754-original-ci-queue-backpressure.json")
SELFTEST = Path("nf754-original-ci-queue-backpressure-selftest.json")
EXTRA = {
    "stage":"NF753",
    "run":44853095710,
    "job":136688825709,
    "name":"authenticate-reuse-and-kernel-actual-original-indexzero-096-103",
    "head_sha":"606a46cae925fd0c77e3e9510194e638d8aa0b6d",
    "artifact":"nf753-original-source-identical-cache-real-global-HD-A-096-103-Lean-kernel-audit",
    "coordinates":[96,103],
}
SPECS = (*PRIOR_FIVE, EXTRA)
OBSERVERS = (
    ("NF751",44852365336,136686458257),
    ("NF752",44852653444,136687397684),
    ("NF753",44853095580,136688825731),
)
JOBLESS_FAILURE_SAMPLES = (44854483794,44854482592)
OLD_ACCEPTED = 596
FRONTIER = 968

assert len(SPECS)==6
assert len({s["run"] for s in SPECS})==6
assert len({s["job"] for s in SPECS})==6
assert len(set(i for s in SPECS for i in range(s["coordinates"][0],s["coordinates"][1]+1)))==48
assert set(s["stage"] for s in SPECS)==set(f"NF{i}" for i in range(748,754))
assert OLD_ACCEPTED + len(SPECS)*16==692
assert FRONTIER-OLD_ACCEPTED==372

def api(endpoint):
    r=subprocess.run(["gh","api",f"repos/{REPO}/{endpoint}"],
                     capture_output=True,text=True,check=True)
    return json.loads(r.stdout)

def synthetic_tests():
    spec=EXTRA
    run={"id":spec["run"],"head_sha":spec["head_sha"],"status":"queued","conclusion":None}
    job={"id":spec["job"],"name":spec["name"],"status":"queued","conclusion":None,"steps":[]}
    cases=[]
    x=assess(spec,run,[job],[])
    assert x["blockers"] and not x["ready_for_separate_source_and_axiom_artifact_review"]
    assert x["original_HD_A_gate_instances_promoted_by_this_script"]==0
    cases.append("queued_exact_job_cannot_certify")
    run.update(status="completed",conclusion="failure")
    job.update(status="completed",conclusion="failure")
    assert not assess(spec,run,[job],[])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("failed_job_cannot_certify")
    run["conclusion"]="success";job["conclusion"]="success"
    assert not assess(spec,run,[job],[])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("job_success_without_axioms_cannot_certify")
    job["steps"]=[{"name":"Strict 35-name original source-bound Lean theorem axiom audit",
                   "status":"completed","conclusion":"success"}]
    assert not assess(spec,run,[job],[])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("strict_step_without_artifact_cannot_certify")
    art={"name":spec["artifact"],"id":1,"expired":False,"digest":"sha256:"+"b"*64}
    ready=assess(spec,run,[job],[art])
    assert ready["ready_for_separate_source_and_axiom_artifact_review"]
    assert not ready["LEAN_PASS_certified_by_this_script"]
    assert ready["original_HD_A_gate_instances_promoted_by_this_script"]==0
    cases.append("all_metadata_still_not_mathematical_certification")
    art["digest"]="sha256:fake"
    assert not assess(spec,run,[job],[art])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("bad_artifact_digest_fails_closed")
    art["digest"]="sha256:"+"b"*64;art["expired"]=True
    assert not assess(spec,run,[job],[art])["ready_for_separate_source_and_axiom_artifact_review"]
    cases.append("expired_artifact_fails_closed")
    try:
        assess(spec,{**run,"head_sha":"fake"},[job],[art])
    except AssertionError:
        cases.append("changed_source_revision_fails_closed")
    else:
        raise AssertionError("source revision mismatch was accepted")
    assert len(cases)==8
    report={"schema":"NF754-synthetic-nonpromotion-tests-v1",
            "cases":cases,"actual_Lean_kernels_tested":0,
            "new_original_numeric_gate_acceptances":0}
    SELFTEST.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print("NF754 8 synthetic negative controls PASS; 0 new original Lean numerical gates")

def live():
    # Supports gh auth login on a local workstation or GH_TOKEN in a CI shell.
    if os.environ.get("GITHUB_REPOSITORY") not in (None,REPO):
        raise AssertionError("wrong GitHub repository")
    statuses={}
    for status in ("queued","in_progress","waiting"):
        payload=api(f"actions/runs?status={status}&per_page=1")
        n=payload["total_count"]
        assert isinstance(n,int) and n>=0,(status,n)
        statuses[status]=n
    receipts=[]
    for spec in SPECS:
        run=api(f"actions/runs/{spec['run']}")
        job_data=api(f"actions/runs/{spec['run']}/jobs?per_page=100")
        artifact_data=api(f"actions/runs/{spec['run']}/artifacts?per_page=100")
        assert isinstance(job_data.get("jobs"),list)
        assert isinstance(artifact_data.get("artifacts"),list)
        receipt=assess(spec,run,job_data["jobs"],artifact_data["artifacts"])
        assert receipt["LEAN_PASS_certified_by_this_script"] is False
        assert receipt["original_HD_A_gate_instances_promoted_by_this_script"]==0
        receipts.append(receipt)
    observers=[]
    for label,run_id,job_id in OBSERVERS:
        run=api(f"actions/runs/{run_id}")
        jobs=api(f"actions/runs/{run_id}/jobs?per_page=100")["jobs"]
        match=[job for job in jobs if job.get("id")==job_id]
        assert run["id"]==run_id and len(match)==1,(label,run_id,job_id)
        observers.append({"stage":label,"run":run_id,"job":job_id,
                          "run_status":run["status"],"run_conclusion":run.get("conclusion"),
                          "job_status":match[0]["status"],
                          "job_conclusion":match[0].get("conclusion")})
    jobless=[]
    for run_id in JOBLESS_FAILURE_SAMPLES:
        run=api(f"actions/runs/{run_id}")
        jobs=api(f"actions/runs/{run_id}/jobs?per_page=100")["jobs"]
        # An example is diagnostic only, not a statement about its root cause.
        jobless.append({
            "run":run_id,"event":run.get("event"),"workflow_path":run.get("path"),
            "head_branch":run.get("head_branch"),"status":run.get("status"),
            "conclusion":run.get("conclusion"),"actual_job_count_returned":len(jobs),
            "completed_failure_with_zero_jobs":(
                run.get("status")=="completed" and run.get("conclusion")=="failure"
                and len(jobs)==0),
        })
    queued=[x["stage"] for x in receipts if x["run_status"] in ("queued","waiting","pending","requested")]
    record={
      "schema":"NF754-original-global-HD-A-CI-backpressure-observation-not-Lean-proof-v1",
      "repository":REPO,
      "queue_counts_at_request_time":statuses,
      "source_exact_six_pending_original_numerical_jobs":receipts,
      "old_accepted_original_frontier_gate_instances":OLD_ACCEPTED,
      "original_designated_two_frontier_gate_instances":FRONTIER,
      "new_gate_instances_accepted_by_this_observer":0,
      "independent_prior_status_audits":observers,
      "selected_zero_job_failure_examples":jobless,
      "withhold_new_heavy_numerical_batches_while_prior_queued":bool(queued),
      "pending_numerical_stages_at_snapshot":queued,
      "jobless_failure_root_cause_established":False,
      "repository_queue_root_cause_established":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "note":"Job status and digest metadata are not source-specific proof content. A completed numerical job requires independent strict 35-target axiom and immutable original source/artifact audit before any ledger promotion."
    }
    assert len(receipts)==6 and len(observers)==3
    assert record["new_gate_instances_accepted_by_this_observer"]==0
    OUT.write_text(json.dumps(record,sort_keys=True,indent=2)+"\n")
    print(f"NF754 REPO queue={statuses['queued']} in_progress={statuses['in_progress']}")
    print("NF754 genuine original numerical status: "+", ".join(
          f"{x['stage']}={x['run_status']}/{x['run_conclusion']}" for x in receipts))
    print("NF754 accepted original numerical HD/A frontier = 596/968; 0 newly certified")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("mode",choices=("live","selftest"))
    args=p.parse_args()
    if args.mode=="live":live()
    else:synthetic_tests()
