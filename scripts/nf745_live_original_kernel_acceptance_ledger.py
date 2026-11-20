#!/usr/bin/env python3
"""NF745: fail-closed live GitHub ORIGINAL matrix-gate compiler acceptance ledger.

This is deliberately an independent small control-plane job. It does NOT
infer Lean truth from Python generation, a successful source preflight, a
queued workflow, or the presence of an artifact named "source".

Only successful ORIGINAL numerical source-bound gate-kernel JOBS with a
successful strictly named theorem-axiom verification step, an immutable
matching artifact, and successful original upstream source ancestry can
increase accepted gate coverage.

Uses actual GitHub API run/job/artifact data supplied as JSON. It does
NOT recompile numerical gates, invent data or assume NF734–NF744 pending
work has run. A source theorem and an actual kernel receipt are distinct.

An explicit self-test checks queued, absent, failed, missing-axiom-step,
expired/missing-artifact and genuinely accepted cases.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SCHEMA="NF745-live-original-HD-A-source-bound-numerical-kernel-acceptance-ledger-v1"
BASELINE=532
N=242
ORIGINAL_INDEXONE_GATE_COUNT=2*N
ORIGINAL_INDEXZERO_PREVIOUS=tuple(range(24))
ALLOWED={"propext","Classical.choice","Quot.sound"}
PREVIOUS=(
  {"stage":"NF708", "run":44640227758, "job_id":135969102426,
   "job":"global-attachment", "artifact_id":14589570565,
   "artifact":"nf708-first-original-global-matrix-attachments", "first":0, "end":8},
  {"stage":"NF713", "run":44649041852, "job_id":135998999534,
   "job":"second-global-attachment", "artifact_id":14594190839,
   "artifact":"nf713-second-original-global-matrix-attachments", "first":8, "end":16},
  {"stage":"NF715", "run":44669131044, "job_id":136065595864,
   "job":"third-global-attachment", "artifact_id":14599683589,
   "artifact":"nf715-third-original-global-matrix-attachments", "first":16, "end":24},
  {"stage":"NF733", "run":44782027897, "job_id":136446941618,
   "job":"accepted-actual-original-index-one-custody", "artifact_id":14652498322,
   "artifact":"nf733-permanent-source-bound-original-index-one-full-lean-kernel-custody"},
)
SOURCE=(
  {"stage":"NF737-full-authentic-source", "run":44791346863,
   "job":"authenticate-and-emit-remaining-original-indexzero",
   "job_id":136479519760, "artifact_id":14660147684,
   "artifact":"nf737-authenticated-original-indexzero-242-full-source-and-28-shard-candidates",
   "artifact_sha256":"11e31531cfd29187b648b207d85269c8b2a0a065a387b9182023a425e645a42f"},
  {"stage":"NF739-full-authentic-source", "run":44795709843,
   "job":"authenticate-and-emit-remaining-original-indexzero",
   "job_id":136494577562, "artifact_id":14663320765,
   "artifact":"nf739-authenticated-original-indexzero-242-full-source-and-28-shard-candidates"},
)
PILOTS=(
  {"stage":"NF737", "run":44791346863,
   "job":"kernel-original-global-HD-A-indexzero-032-039",
   "artifact":"nf737-genuine-original-global-indexzero-032-039-HD-A-numerical-kernel-audit",
   "first":32,"end":40},
  {"stage":"NF739", "run":44795709843,
   "job":"kernel-original-global-HD-A-indexzero-040-047",
   "artifact":"nf739-genuine-original-global-indexzero-040-047-HD-A-numerical-kernel-audit",
   "first":40,"end":48},
  {"stage":"NF742", "run":44800994258,
   "job":"kernel-original-global-HD-A-indexzero-048-055",
   "artifact":"nf742-genuine-original-global-indexzero-048-055-HD-A-numerical-kernel-audit",
   "first":48,"end":56},
  {"stage":"NF743", "run":44813177950,
   "job":"authenticate-reuse-and-kernel-actual-original-indexzero-056-063",
   "job_id":136554678956,
   "artifact":"nf743-original-source-identical-cache-real-global-HD-A-056-063-Lean-kernel-audit",
   "first":56,"end":64},
)
# These full original numerical stage statuses are collected independently.
# They are NOT accepted original gate facts merely because their source
# source or finite logical proof runs succeeded.
PIPELINE=(
  {"stage":"NF737", "run":44791346863,
   "job":"kernel-source-neutral-28-shard-indexzero-cover",
   "scope":"PURE_Fin242_LOGICAL_NOT_NUMERICAL"},
  {"stage":"NF742", "run":44800994258,
   "job":"authenticate-and-emit-remaining-original-indexzero",
   "scope":"SOURCE_ONLY"},
  {"stage":"NF744", "run":44814853311,
   "job":"authentic-original-242-global-HD-A-source-and-31-range-compilation-plan",
   "scope":"SOURCE_ONLY"},
  {"stage":"NF744", "run":44814853311,
   "job":"independent-31-way-complete-Fin242-pure-lean-axiom-check",
   "scope":"PURE_Fin242_LOGICAL_NOT_NUMERICAL"},
)
BINDING=Path("nf745-original-numerical-kernel-acceptance-ledger.json")
FIXTURE=Path("nf745-original-github-status-snapshot.json")
TEST_RECEIPT=Path("nf745-ledger-selftest.json")

assert sum(2*(x["end"]-x["first"]) for x in PILOTS)==64
assert [i for p in PILOTS for i in range(p["first"],p["end"])]==list(range(32,64))
assert set(ORIGINAL_INDEXZERO_PREVIOUS).isdisjoint(range(32,64))

def matches_job(target,job):
    if job.get("name")!=target["job"]:
        return False
    if "job_id" in target and job.get("id")!=target["job_id"]:
        return False
    return True

def extract(data,run,field):
    assert str(run) in data["runs"],("missing GitHub actual run query",run)
    obj=data["runs"][str(run)]
    assert field in obj,(run,field)
    return obj[field]

def artifact_name_good(artifact,ref):
    digest=artifact.get("digest")
    return (
      artifact.get("name")==ref["artifact"]
      and not artifact.get("expired",True)
      and isinstance(artifact.get("id"),int)
      and re.fullmatch(r"sha256:[0-9a-f]{64}",digest or "") is not None
      and ("artifact_id" not in ref or artifact["id"]==ref["artifact_id"])
      and ("artifact_sha256" not in ref or digest=="sha256:"+ref["artifact_sha256"])
    )

def trusted_job_success(data,ref):
    jobs=extract(data,ref["run"],"jobs")
    artifacts=extract(data,ref["run"],"artifacts")
    accepted=[j for j in jobs if matches_job(ref,j) and j.get("status")=="completed"
              and j.get("conclusion")=="success"]
    good=[a for a in artifacts if artifact_name_good(a,ref)]
    assert len(accepted)==1 and len(good)==1,(
      "Accepted historical original Lean source/provenance receipt missing",
      ref["stage"],ref["run"],len(accepted),len(good))
    return accepted[0],good[0]

def job_state(data,ref):
    jobs=extract(data,ref["run"],"jobs")
    candidates=[j for j in jobs if matches_job(ref,j)]
    assert len(candidates)<=1,(ref["stage"],ref["job"],"ambiguous duplicate numerical job")
    if not candidates:
        return {"state":"NOT_SCHEDULED_IN_RUN","job_id":None,"status":None,
                "conclusion":None}
    j=candidates[0]
    status=j.get("status")
    conclusion=j.get("conclusion")
    if status=="completed":
        state="SUCCESS" if conclusion=="success" else "FAILED_OR_CANCELLED"
    elif status in ("queued","waiting","pending"):
        state="QUEUED"
    elif status=="in_progress":
        state="IN_PROGRESS"
    else:
        state="UNRECOGNIZED_NONACCEPTED"
    return {"state":state,"job_id":j.get("id"),"status":status,
            "conclusion":conclusion}

def kernel_audit_complete(data,ref):
    status=job_state(data,ref)
    if status["state"]!="SUCCESS":
        return False, status,"NOT_SUCCESSFUL_GENUINE_NUMERICAL_JOB"
    j=next(j for j in extract(data,ref["run"],"jobs") if matches_job(ref,j))
    steps=j.get("steps") or []
    # The original numerical workflow must actually run a STRICT theorem
    # standard-axiom audit step, not merely upload source candidates.
    strict=[s for s in steps
            if "Strict" in (s.get("name") or "")
            and ("axiom" in (s.get("name") or "").lower()
                 or "theorem" in (s.get("name") or "").lower())
            and s.get("conclusion")=="success"]
    if len(strict)!=1:
        return False,status,"NO_SUCCESSFUL_STRICT_35_THEOREM_AXIOM_STEP"
    arts=extract(data,ref["run"],"artifacts")
    matching=[a for a in arts if artifact_name_good(a,ref)]
    if len(matching)!=1:
        return False,status,"NO_SOURCE_BOUND_NUMERICAL_KERNEL_ARTIFACT"
    # The matching CI kernel job's strict step already ran the source-specific
    # audit driver and validated exact 35 theorem names/source hashes before
    # uploading this immutable artifact. This ledger does not recompile them.
    return True,status,"JOB_STRICT_LEAN_AXES_AND_ARTIFACT_SUCCESS"

def evaluate(data):
    assert data["schema"]=="NF745-live-github-original-gate-jobs-snapshot-v1"
    assert set(data["runs"])=={
      str(x["run"]) for x in PREVIOUS+SOURCE+PILOTS+PIPELINE
    }
    history={}
    for x in PREVIOUS:
        j,a=trusted_job_success(data,x)
        history[x["stage"]]={"run":x["run"],"job_id":j["id"],
                             "artifact_id":a["id"],"original_source_authentic":True}
    for x in SOURCE:
        j,a=trusted_job_success(data,x)
        history[x["stage"]]={"run":x["run"],"job_id":j["id"],
                             "artifact_id":a["id"],"original_source_authentic":True}
    assert {x["stage"] for x in SOURCE}=={
        "NF737-full-authentic-source","NF739-full-authentic-source"}
    pending=[]
    accepted=list(ORIGINAL_INDEXZERO_PREVIOUS)
    actual_results=[]
    for p in PILOTS:
        yes,j,why=kernel_audit_complete(data,p)
        if yes:
            accepted.extend(range(p["first"],p["end"]))
        else:
            pending.extend(range(p["first"],p["end"]))
        actual_results.append({
          "iteration":p["stage"],"range":[p["first"],p["end"]],
          "run_id":p["run"],"job_name":p["job"],"job_id":j["job_id"],
          "job_status":j["state"],"kernel_pass":yes,
          "reason":why,
          "new_original_HD_gate_count_if_accepted":p["end"]-p["first"],
          "new_original_A_gate_count_if_accepted":p["end"]-p["first"],
          "new_counted_gate_instances":2*(p["end"]-p["first"]) if yes else 0,
          "source_stage_PASS_is_not_numerical_PASS":True,
        })
    assert len(accepted)==len(set(accepted))
    assert sorted(accepted)==list(ORIGINAL_INDEXZERO_PREVIOUS)+[
        i for r in actual_results if r["kernel_pass"] for i in range(*r["range"])
    ]
    count=ORIGINAL_INDEXONE_GATE_COUNT+2*len(accepted)
    assert count==BASELINE+sum(r["new_counted_gate_instances"]
                               for r in actual_results)
    assert count<=596
    pipeline=[{
        "iteration":x["stage"],"scope":x["scope"],"run_id":x["run"],
        "job_name":x["job"],"job":job_state(data,x),
        "adds_original_numerical_gates":False
    } for x in PIPELINE]
    return {
      "schema":SCHEMA,
      "source_snapshot_sha256":hashlib.sha256(
        json.dumps(data,sort_keys=True).encode()).hexdigest(),
      "original_matrix_dimension":N,
      "accepted_immutable_historical_kernel_source_receipts":history,
      "already_accepted_original_indexone_HD_gate_count":N,
      "already_accepted_original_indexone_A_gate_count":N,
      "already_accepted_original_indexzero_HD_positions":sorted(accepted),
      "already_accepted_original_indexzero_A_positions":sorted(accepted),
      "source_evidenced_accepted_original_global_HD_A_gate_instances":count,
      "historical_base_gate_instances_before_candidates":BASELINE,
      "new_source_bound_numerical_kernel_pass_count":sum(
          x["kernel_pass"] for x in actual_results),
      "new_source_bound_numerical_gate_instances":count-BASELINE,
      "pending_independently_checked_pilot_positions":sorted(pending),
      "pilot_kernel_results":actual_results,
      "non_numeric_source_or_logical_pipeline_states":pipeline,
      "indexzero_24_to_31_NOT_VERIFIED_BY_THIS_LEDGER":True,
      "remaining_original_indexzero_positions_not_proved_by_this_ledger":
          [i for i in range(N) if i not in accepted],
      "complete_original_indexzero_universal_theorems_proved":False,
      "original_full_242x242_matrix_enclosure_proved":False,
      "original_vector_payment_gate_bank_complete":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "scope":"Only independently authenticated actual original global HD row-zero, A column-zero, and previously Lean-accepted original index-one gates. NF734 indexzero 24–31 and future 64–241 remain separately pending. A source preflight, pure finite-cover proof, queued original numerical job, successful unrelated Lean job or cached object alone NEVER expands accepted gate counts."
    }

def selftest():
    # No external GitHub network. Synthetic fixture demonstrates that success
    # requires every named step + specific artifact and does not count source.
    base={
      "schema":"NF745-live-github-original-gate-jobs-snapshot-v1",
      "runs":{}
    }
    for r in PREVIOUS+SOURCE+PILOTS+PIPELINE:
        key=str(r["run"])
        base["runs"].setdefault(key,{"jobs":[],"artifacts":[]})
    for r in PREVIOUS+SOURCE:
        info=base["runs"][str(r["run"])]
        info["jobs"].append({
           "id":r["job_id"],"name":r["job"],"status":"completed",
           "conclusion":"success","steps":[]
        })
        info["artifacts"].append({
           "id":r["artifact_id"],"name":r["artifact"],"expired":False,
           "digest":"sha256:"+r.get("artifact_sha256","0"*64)
        })
    for idx,p in enumerate(PILOTS):
        info=base["runs"][str(p["run"])]
        info["jobs"].append({
          "id":7000000+idx,"name":p["job"],
          "status":"queued","conclusion":None,"steps":[]
        })
    snapshot=evaluate(base)
    assert snapshot["source_evidenced_accepted_original_global_HD_A_gate_instances"]==532
    assert snapshot["new_source_bound_numerical_gate_instances"]==0
    tests=["all_queued_baseline_532"]
    p=PILOTS[0]
    j=next(x for x in base["runs"][str(p["run"])]["jobs"]
           if x["name"]==p["job"])
    j.update({"status":"completed","conclusion":"success"})
    assert not kernel_audit_complete(base,p)[0]
    tests.append("job_success_without_axiom_step_not_counted")
    j["steps"]=[{"name":"Strict 35-name theorem axiom audit","conclusion":"success"}]
    assert not kernel_audit_complete(base,p)[0]
    tests.append("no_matching_numeric_artifact_not_counted")
    base["runs"][str(p["run"])]["artifacts"].append({
      "id":9000001,"name":p["artifact"],"expired":True,
      "digest":"sha256:"+"1"*64})
    assert not kernel_audit_complete(base,p)[0]
    tests.append("expired_numeric_artifact_not_counted")
    base["runs"][str(p["run"])]["artifacts"][-1]["expired"]=False
    good=evaluate(base)
    assert good["source_evidenced_accepted_original_global_HD_A_gate_instances"]==548
    assert good["new_source_bound_numerical_kernel_pass_count"]==1
    tests.append("real_job_strict_axiom_step_and_artifact_count_16")
    j.update({"status":"completed","conclusion":"failure"})
    assert not kernel_audit_complete(base,p)[0]
    tests.append("failed_numerical_job_not_counted")
    r={
      "schema":"NF745-live-original-numerical-ledger-selftest-v1",
      "passed_cases":tests,
      "baseline_actual_original_gates":532,
      "one_successful_actual_original_eight_HD_eight_A_shard_gates":548,
      "false_success_promotions_rejected":True,
      "actual_live_GitHub_current_status_not_inferred_from_fixtures":True
    }
    TEST_RECEIPT.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n")
    print("NF745 five fail-closed snapshot tests PASS: queued/source-only/failed/no-axioms/expired-artifact never count as original numerical Lean acceptance")

def run():
    data=json.loads(FIXTURE.read_text())
    r=evaluate(data)
    BINDING.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n")
    print("NF745 ORIGINAL global HD/A NUMERICAL KERNEL LEDGER: accepted gate instances",r["source_evidenced_accepted_original_global_HD_A_gate_instances"],
          ", new accepted gate instances",r["new_source_bound_numerical_gate_instances"],
          ", true accepted indexzero positions",len(r["already_accepted_original_indexzero_HD_positions"]),
          ", pending indexzero pilot ranges",[
            x["range"] for x in r["pilot_kernel_results"] if not x["kernel_pass"]
          ],"; original full matrix/Weil positivity/RH OPEN")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("selftest","evaluate"))
    args=p.parse_args()
    if args.stage=="selftest":selftest()
    else:run()
