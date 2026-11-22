#!/usr/bin/env python3
"""NF770: fail-closed authentic prior 724 original HD/A gate custody.

Calls unchanged NF769 seven-prior-batch verifier, then checks actual NF769
112–119 GitHub Lean run, 35 standard-only axiom audit, source identity and
immutable SHA-256 artifact. Preparation MUST NOT promote 120–127 gates.
"""
import hashlib, json, os
from pathlib import Path
import nf769_original_prior_708_custody as prior708
import nf768_original_prior_692_custody as github

OUT=Path("nf770-accepted-prior-724-kernel-custody.json")
BASE=Path("nf769-accepted-prior-708-kernel-custody.json")
RUN_ID=44990743795
JOB_ID=137111036750
SOURCE_SHA="a431f903254000bb5ad8edbc276ccc8599da98f5"
ARTIFACT_ID=14741942304
ARTIFACT_NAME="nf769-original-source-identical-cache-real-global-HD-A-112-119-Lean-kernel-audit"
ARTIFACT_DIGEST="08fd3d4f951989ce1c538219085995352bda3d61a2a652a572807a8102da46a4"
ARTIFACT_SIZE=46841

def main():
    assert os.environ.get("GITHUB_REPOSITORY")==github.REPO
    assert os.environ.get("GH_TOKEN"),"Read-only Actions API permission required"
    prior708.main()
    prev=json.loads(BASE.read_text())
    assert prev["schema"]=="NF769-original-prior-708-live-seven-batch-custody-v1"
    assert prev["accepted_original_HD_A_gate_instances"]==708
    assert prev["all_seven_prior_batches_checked"] is True
    assert prev["accepted_original_indexzero_positions_HD"]==list(range(112))
    assert prev["accepted_original_indexzero_positions_A"]==list(range(112))
    run=github.api(f"actions/runs/{RUN_ID}")
    assert run["status"]=="completed" and run["conclusion"]=="success"
    assert run["event"]=="workflow_dispatch" and run["head_sha"]==SOURCE_SHA
    assert run["run_attempt"]==1 and run["path"]==".github/workflows/rpb108-manual.yml"
    jobs=github.api(f"actions/runs/{RUN_ID}/jobs?per_page=100")["jobs"]
    found=[j for j in jobs if j["id"]==JOB_ID and j["conclusion"]=="success"]
    assert len(found)==1
    steps=found[0]["steps"]
    assert any(s["name"]=="Direct kernel-compile eight actual original frozen NF702 NF703 global HD/A indexzero Col112 through Col119 gate source modules" and s["conclusion"]=="success" for s in steps)
    assert any(s["name"]=="Strict 35-name original source-bound Lean theorem axiom and accepted prior cache-object audit" and s["conclusion"]=="success" for s in steps)
    arts=github.api(f"actions/runs/{RUN_ID}/artifacts?per_page=100")["artifacts"]
    matched=[a for a in arts if a["id"]==ARTIFACT_ID and a["name"]==ARTIFACT_NAME
        and a.get("digest")=="sha256:"+ARTIFACT_DIGEST and a["expired"] is False]
    assert len(matched)==1 and matched[0]["size_in_bytes"]==ARTIFACT_SIZE
    positions=prev["accepted_original_indexzero_positions_HD"]+list(range(112,120))
    assert positions==list(range(120)) and 708+16==724
    record={
      "schema":"NF770-original-prior-724-live-eight-batch-custody-v1",
      "accepted_original_HD_A_gate_instances":724,
      "accepted_original_indexzero_positions_HD":positions,
      "accepted_original_indexzero_positions_A":positions,
      "all_eight_prior_batches_checked":True,
      "nf769_original_112_to_119_success_and_digest_verified":True,
      "nf769_source_sha":SOURCE_SHA,
      "nf769_kernel_run_id":RUN_ID,
      "nf769_job_id":JOB_ID,
      "nf769_artifact_id":ARTIFACT_ID,
      "nf769_artifact_digest_sha256":ARTIFACT_DIGEST,
      "original_prior_708_receipt_sha256":hashlib.sha256(BASE.read_bytes()).hexdigest(),
      "candidate_new_original_indices":list(range(120,128)),
      "candidate_new_gates":16,
      "nf770_new_120_127_numerical_kernel_accepted":False,
      "complete_original_physical_matrix_enclosure":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False
    }
    OUT.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print("NF770 predecessor custody: accepted 724/968; 120–127 remains PENDING")

if __name__=="__main__":
    main()
