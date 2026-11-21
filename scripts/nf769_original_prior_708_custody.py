#!/usr/bin/env python3
"""NF769: fail-closed independent custody for 708 accepted original HD/A gates.

Calls the inherited NF768 six-batch (596+96=692) source verifier, then
verifies NF768's genuine original 104..111 direct Lean job, 35-axiom step,
single source SHA and SHA-256-pinned final uploaded kernel audit archive.
Does not promote any new 112..119 candidates.
"""
import hashlib
import json
import os
from pathlib import Path
import nf768_original_prior_692_custody as old

OUT=Path("nf769-accepted-prior-708-kernel-custody.json")
BASE=Path("nf768-accepted-prior-692-kernel-custody.json")
RUN_ID=44909033680
JOB_ID=136860695139
SOURCE_SHA="b477d9a8eb6c33781a8eee7c1208de93c705f307"
ARTIFACT_ID=14709495695
ARTIFACT_NAME="nf768-original-source-identical-cache-real-global-HD-A-104-111-Lean-kernel-audit"
ARTIFACT_DIGEST="20ac8f7dfa9a83f866d0aeee1c77497b180741c00785203dff54376f2f37dc78"

def main():
    assert os.environ.get("GITHUB_REPOSITORY")==old.REPO
    assert os.environ.get("GH_TOKEN"),"GitHub Actions read permission required"
    old.main()
    prev=json.loads(BASE.read_text())
    assert prev["schema"]=="NF768-original-prior-692-live-six-batch-custody-v1"
    assert prev["accepted_original_HD_A_gate_instances"]==692
    assert prev["all_six_prior_batches_checked"] is True
    assert prev["accepted_original_indexzero_positions_HD"]==list(range(104))
    assert prev["accepted_original_indexzero_positions_A"]==list(range(104))
    run=old.api(f"actions/runs/{RUN_ID}")
    assert run["status"]=="completed" and run["conclusion"]=="success"
    assert run["event"]=="workflow_dispatch" and run["head_sha"]==SOURCE_SHA
    assert run.get("run_attempt")==1 and run["path"]==".github/workflows/rpb108-manual.yml"
    jobs=old.api(f"actions/runs/{RUN_ID}/jobs?per_page=100")["jobs"]
    matching=[j for j in jobs if j["id"]==JOB_ID and j["conclusion"]=="success"]
    assert len(matching)==1, "Original NF768 job identity or status mismatch"
    steps=matching[0]["steps"]
    assert any(s["name"]=="Direct kernel-compile eight actual original frozen NF702 NF703 global HD/A indexzero Col104 through Col111 gate source modules" and s["conclusion"]=="success" for s in steps)
    assert any(s["name"]=="Strict 35-name original source-bound Lean theorem axiom and accepted prior cache-object audit" and s["conclusion"]=="success" for s in steps)
    artifacts=old.api(f"actions/runs/{RUN_ID}/artifacts?per_page=100")["artifacts"]
    matched=[a for a in artifacts if a["id"]==ARTIFACT_ID and a["name"]==ARTIFACT_NAME and a.get("digest")=="sha256:"+ARTIFACT_DIGEST and a["expired"] is False]
    assert len(matched)==1,"Original NF768 immutable artifact, SHA256 or retention mismatch"
    assert matched[0]["size_in_bytes"]==45795
    positions=prev["accepted_original_indexzero_positions_HD"]+list(range(104,112))
    assert positions==list(range(112)) and len(set(positions))==112
    assert 692+16==708
    record={
      "schema":"NF769-original-prior-708-live-seven-batch-custody-v1",
      "accepted_original_HD_A_gate_instances":708,
      "accepted_original_indexzero_positions_HD":positions,
      "accepted_original_indexzero_positions_A":positions,
      "all_seven_prior_batches_checked":True,
      "nf768_original_104_to_111_success_and_digest_verified":True,
      "nf768_source_sha":SOURCE_SHA,
      "nf768_kernel_run_id":RUN_ID,
      "nf768_job_id":JOB_ID,
      "nf768_artifact_id":ARTIFACT_ID,
      "nf768_artifact_digest_sha256":ARTIFACT_DIGEST,
      "original_prior_692_receipt_sha256":hashlib.sha256(BASE.read_bytes()).hexdigest(),
      "candidate_new_original_indices":list(range(112,120)),
      "candidate_new_gates":16,
      "nf769_new_112_119_numerical_kernel_accepted":False,
      "complete_original_physical_matrix_enclosure":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
    }
    OUT.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print("NF769 prior accepted 708 original HD/A gate instances authenticated; new original 112–119 kernel PENDING")

if __name__=="__main__":
    main()
