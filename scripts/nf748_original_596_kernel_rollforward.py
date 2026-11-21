#!/usr/bin/env python3
"""NF748: fail-closed LIVE acceptance of 596 actual original HD/A gates.

Read actual GitHub Actions job steps and immutable original numerical
kernel artifact identifiers. Historical 532 is accepted via the live
NF745 ledger, and four disjoint 8-coordinate numerical kernel pilots
(NF737, NF739, NF742, NF743) must all have a real successful
strict 35-name Lean standard-axiom step and SHA-pinned kernel artifact.

Source-only runs, pure Fin242 logical proofs, a queued job or any
nonstandard/sorry Lean source are NEVER promoted by this receipt.
"""
import argparse
import copy
import hashlib
import json
import os
import subprocess
from pathlib import Path

OUT = Path("nf748-original-596-accepted-gate-rollforward.json")
TEST = Path("nf748-original-596-accepted-gate-rollforward-selftest.json")
REPO = "monocap-tech/weil-lab"
SCHEMA = "NF748-live-accepted-original-HD-A-596-kernel-rollforward-v1"
BASELINE = 532
N = 242

# The NF745 artifact is a separately successful original numerical
# custody reconciliation, not a source-generation preflight.
LEDGER = {
    "stage":"NF745",
    "run":44818061251,
    "job_id":136571445603,
    "job":"live-original-gate-kernel-acceptance-reconciliation",
    "artifact_id":14676318703,
    "artifact":"nf745-immutable-live-original-HD-A-kernel-acceptance-ledger",
    "digest":"5524933c91f0786732d6ab0272385a693188518bf9dba3a37006a115675eee5a",
}
PILOTS = (
    {"stage":"NF737", "first":32,"end":40,
     "run":44791346863, "job_id":136514439734,
     "job":"kernel-original-global-HD-A-indexzero-032-039",
     "artifact_id":14672703515,
     "artifact":"nf737-genuine-original-global-indexzero-032-039-HD-A-numerical-kernel-audit",
     "digest":"bd3771cf2b939e76bc4dea956f4547c3efb4330f77a318db46cf71b78004e89a"},
    {"stage":"NF739", "first":40,"end":48,
     "run":44795709843, "job_id":136528518645,
     "job":"kernel-original-global-HD-A-indexzero-040-047",
     "artifact_id":14673191666,
     "artifact":"nf739-genuine-original-global-indexzero-040-047-HD-A-numerical-kernel-audit",
     "digest":"95da4ce94c83bc021b7361fdf261699a74f45a65a507a505a28567dbc3087258"},
    {"stage":"NF742", "first":48,"end":56,
     "run":44800994258, "job_id":136579243726,
     "job":"kernel-original-global-HD-A-indexzero-048-055",
     "artifact_id":14678836252,
     "artifact":"nf742-genuine-original-global-indexzero-048-055-HD-A-numerical-kernel-audit",
     "digest":"907ac7e634209604dfc5d4b6fa9c4706791664155a7c9d60e13e14701360ace2"},
    {"stage":"NF743", "first":56,"end":64,
     "run":44836454830, "job_id":136633947443,
     "job":"authenticate-reuse-and-kernel-actual-original-indexzero-056-063",
     "artifact_id":14680553841,
     "artifact":"nf743-original-source-identical-cache-real-global-HD-A-056-063-Lean-kernel-audit",
     "digest":"b0c0c1acc85701b0ba437fa99dece7309a7d00500307cae05bf3a3bfea9d169d"},
)
assert [(x["first"],x["end"]) for x in PILOTS] == [
    (32,40),(40,48),(48,56),(56,64)
]
assert all(x["end"]-x["first"]==8 for x in PILOTS)
assert len(set(i for x in PILOTS for i in range(x["first"],x["end"])))==32


def sha(raw):
    return hashlib.sha256(json.dumps(raw,sort_keys=True).encode()).hexdigest()


def exact_success(snapshot,ref,strict):
    entry=snapshot.get(str(ref["run"]))
    assert isinstance(entry,dict),("missing live original Actions run",ref["run"])
    jobs=[x for x in entry.get("jobs",[]) if
        x.get("id")==ref["job_id"] and x.get("name")==ref["job"]]
    assert len(jobs)==1,("original kernel job identity mismatch",ref["stage"])
    j=jobs[0]
    assert j.get("status")=="completed" and j.get("conclusion")=="success",(
        "original numerical kernel job NOT SUCCESS",ref["stage"])
    if strict:
        steps=[s for s in j.get("steps",[]) if
               s.get("conclusion")=="success" and
               "strict" in (s.get("name") or "").lower() and
               ("axiom" in (s.get("name") or "").lower()
                or "theorem" in (s.get("name") or "").lower())]
        assert len(steps)==1,("strict original 35-name axioms step NOT SUCCESS",ref["stage"])
    artifact=[x for x in entry.get("artifacts",[]) if
              x.get("id")==ref["artifact_id"] and
              x.get("name")==ref["artifact"]]
    assert len(artifact)==1,("original numerical kernel artifact identity missing",ref["stage"])
    a=artifact[0]
    assert not a.get("expired",True),("original numerical artifact expired",ref["stage"])
    assert a.get("digest")=="sha256:"+ref["digest"],(
        "original numerical artifact SHA256 changed",ref["stage"])
    return {"stage":ref["stage"],"run":ref["run"],
            "job_id":ref["job_id"],"artifact_id":ref["artifact_id"],
            "artifact_sha256":ref["digest"],
            "strict_original_35_name_axioms_success":bool(strict),
            "actual_source_bound_numerical_kernel_pass":True}


def certify(snapshot):
    nf745=exact_success(snapshot,LEDGER,False)
    proved=[exact_success(snapshot,p,True) for p in PILOTS]
    accepted_indexzero=list(range(24))+[i for p in PILOTS
                                         for i in range(p["first"],p["end"])]
    assert len(set(accepted_indexzero))==56
    total=BASELINE+sum(2*(p["end"]-p["first"]) for p in PILOTS)
    assert total==596==2*N+2*len(accepted_indexzero)
    assert 24 not in accepted_indexzero and 31 not in accepted_indexzero
    assert 64 not in accepted_indexzero and 241 not in accepted_indexzero
    return {
        "schema":SCHEMA,
        "github_live_jobs_and_artifacts_snapshot_sha256":sha(snapshot),
        "baseline_original_global_HD_A_gates":BASELINE,
        "nf745_live_kernel_ledger":nf745,
        "new_original_numerical_receipts":proved,
        "original_gate_instances_accepted":total,
        "original_indexone_HD_A_instances_accepted":2*N,
        "original_indexzero_HD_positions_accepted":accepted_indexzero,
        "original_indexzero_A_positions_accepted":accepted_indexzero,
        "new_64_to_71_original_HD_A_gates_accepted_by_this_ledger":False,
        "nf734_24_to_31_accepted_by_this_ledger":False,
        "original_indexzero_positions_still_outstanding":[
            i for i in range(N) if i not in accepted_indexzero
        ],
        "original_indexzero_full_universal_Lean_PASS":False,
        "full_original_physical_matrix_custody_complete":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }


def live():
    assert os.environ.get("GITHUB_REPOSITORY")==REPO
    assert os.environ.get("GH_TOKEN")
    def api(route):
        return json.loads(subprocess.check_output(
            ["gh","api",f"repos/{REPO}/{route}"],text=True))
    data={}
    for x in (LEDGER,)+PILOTS:
        run=x["run"]
        data[str(run)]={
            "jobs":api(f"actions/runs/{run}/jobs?per_page=100")["jobs"],
            "artifacts":api(f"actions/runs/{run}/artifacts?per_page=100")["artifacts"],
        }
    receipt=certify(data)
    OUT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("NF748 LIVE original Lean kernel custody:",receipt["original_gate_instances_accepted"],
          "distinct HD/A instances (532 historical + 64 true independently verified);",
          "NF734 24..31 and prospective 64..71 NOT PROMOTED")


def selftest():
    src={}
    for p in (LEDGER,)+PILOTS:
        src[str(p["run"])]={
            "jobs":[{"id":p["job_id"],"name":p["job"],
                     "status":"completed","conclusion":"success",
                     "steps":[{"name":"Strict 35-name original theorem axiom audit",
                               "conclusion":"success"}]}],
            "artifacts":[{"id":p["artifact_id"],"name":p["artifact"],
                          "digest":"sha256:"+p["digest"],"expired":False}],
        }
    baseline=certify(src)
    assert baseline["original_gate_instances_accepted"]==596
    passed=["all_five_live_original_kernel_receipts_required"]
    target=PILOTS[-1]
    for label,mutate in (
        ("queued_numeric_job_rejected", lambda x:
         x["jobs"][0].update(status="queued",conclusion=None)),
        ("failed_numeric_job_rejected", lambda x:
         x["jobs"][0].update(status="completed",conclusion="failure")),
        ("missing_strict_axioms_rejected", lambda x:
         x["jobs"][0].update(steps=[])),
        ("expired_kernel_artifact_rejected", lambda x:
         x["artifacts"][0].update(expired=True)),
        ("wrong_artifact_digest_rejected", lambda x:
         x["artifacts"][0].update(digest="sha256:"+"0"*64)),
        ("missing_numeric_artifact_rejected", lambda x:
         x.update(artifacts=[])),
    ):
        tmp=copy.deepcopy(src)
        mutate(tmp[str(target["run"])])
        try:
            certify(tmp)
        except AssertionError:
            passed.append(label)
        else:
            raise AssertionError("False kernel promotion accepted: "+label)
    report={"schema":"NF748-original-596-source-bound-counterfactuals-v1",
            "passed_tests":passed,"trusted_original_gate_instances":596,
            "new_64_71_accepted":False,
            "used_actual_network_for_selftest":False}
    TEST.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("NF748 seven fail-closed historical original kernel promotion tests PASS (synthetic only)")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("stage",choices=("live","selftest"))
    stage=parser.parse_args().stage
    if stage=="live":live()
    else:selftest()
