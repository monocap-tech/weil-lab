#!/usr/bin/env python3
"""NF768: fail-closed prior 692 certified original HD/A source and Lean custody."""
import json
import os
import subprocess
from pathlib import Path

REPO="monocap-tech/weil-lab"
OUT=Path("nf768-accepted-prior-692-kernel-custody.json")
# NF, run, job, original SHA, audit artifact ID, artifact name, SHA256, first, exclusive stop
ROWS=[
  [
    748,
    44846764448,
    136668270768,
    "a509af347d6f800dba4b0125542b66ca9c3296f3",
    14687773915,
    "nf748-original-source-identical-cache-real-global-HD-A-064-071-Lean-kernel-audit",
    "34938431ffbb051d7d24d451e3943cfc5fe5428cf2cf6bf9043d04a5fa002659",
    64,
    72
  ],
  [
    749,
    44847296036,
    136670051321,
    "b428ff2e72e2b1a833ebdc7574510a48f5006669",
    14689552264,
    "nf749-original-source-identical-cache-real-global-HD-A-024-031-Lean-kernel-audit",
    "8353d86e538f455ab3e47e480f45df02c0d8ff42f51a36ed9ef0f7b9ce79a775",
    24,
    32
  ],
  [
    750,
    44851970198,
    136685181507,
    "dd3ea7ea37bf870633fd71b501bb080b21fb9eb0",
    14694359757,
    "nf750-original-source-identical-cache-real-global-HD-A-072-079-Lean-kernel-audit",
    "281980d4fa1a4304ed7c26a60cdb53b9bb93942fe532eb9978801d7eb062c704",
    72,
    80
  ],
  [
    751,
    44852365683,
    136686459933,
    "cfaf080b52b5d5101ac489dcd580802b9764d71e",
    14695173253,
    "nf751-original-source-identical-cache-real-global-HD-A-080-087-Lean-kernel-audit",
    "4f4c42ded7b7a4a868aceab1952cb39e69b88560d1fe2b01b60cab35574ea8de",
    80,
    88
  ],
  [
    752,
    44852653466,
    136687397543,
    "865ddbb28e0da1e2b51fcd0acee6cd34782195ab",
    14695178998,
    "nf752-original-source-identical-cache-real-global-HD-A-088-095-Lean-kernel-audit",
    "2755b4078de2ea04d9a5219fe99ec430df48ea65fac766b5b1ae1fd0fc11e6ec",
    88,
    96
  ],
  [
    753,
    44853095710,
    136688825709,
    "606a46cae925fd0c77e3e9510194e638d8aa0b6d",
    14696425250,
    "nf753-original-source-identical-cache-real-global-HD-A-096-103-Lean-kernel-audit",
    "c855163f03ad3e953c840bdf5ce5ee507871b2ab166d8f7a7e870935388a6218",
    96,
    104
  ]
]

def api(path):
    p=subprocess.run(["gh","api",f"repos/{REPO}/{path}"],text=True,
                     capture_output=True,check=True)
    return json.loads(p.stdout)

def main():
    assert os.environ.get("GITHUB_REPOSITORY")==REPO
    assert os.environ.get("GH_TOKEN"),"GitHub Actions read token missing"
    positions=list(range(24))+list(range(32,64))
    assert len(positions)==56
    checks=[]
    for nf,run_id,job_id,source_sha,artifact_id,artifact_name,digest,first,stop in ROWS:
        assert stop-first==8
        run=api(f"actions/runs/{run_id}")
        assert run["status"]=="completed" and run["conclusion"]=="success",(nf,"run")
        assert run["head_sha"]==source_sha and run["event"]=="pull_request",(nf,"source")
        jobs=api(f"actions/runs/{run_id}/jobs?per_page=100")["jobs"]
        good=[j for j in jobs if j["id"]==job_id and j["conclusion"]=="success"]
        assert len(good)==1,(nf,"kernel job")
        steps=good[0]["steps"]
        assert any(s["name"].startswith("Direct kernel-compile eight actual original frozen NF702 NF703") and s["conclusion"]=="success" for s in steps),(nf,"direct Lean")
        assert any(s["name"].startswith("Strict 35-name original source-bound Lean theorem axiom") and s["conclusion"]=="success" for s in steps),(nf,"strict axioms")
        arts=api(f"actions/runs/{run_id}/artifacts?per_page=100")["artifacts"]
        found=[a for a in arts if a["id"]==artifact_id and a["name"]==artifact_name and a.get("digest")=="sha256:"+digest and not a["expired"]]
        assert len(found)==1,(nf,"artifact digest")
        positions.extend(range(first,stop))
        checks.append({"nf":nf,"run_id":run_id,"job_id":job_id,"head_sha":source_sha,
          "artifact_id":artifact_id,"artifact_name":artifact_name,
          "artifact_sha256":digest,"indices":list(range(first,stop)),
          "kernel_and_strict_35_axioms":"PASS"})
    assert sorted(positions)==list(range(104))
    assert len(set(positions))==104
    assert 596+16*len(checks)==692
    report={"schema":"NF768-original-prior-692-live-six-batch-custody-v1",
      "baseline_original_gate_instances":596,
      "accepted_original_HD_A_gate_instances":692,
      "accepted_original_indexzero_positions_HD":list(range(104)),
      "accepted_original_indexzero_positions_A":list(range(104)),
      "all_six_prior_batches_checked":True,
      "prior_kernel_runs":checks,
      "new_104_to_111_original_kernel_accepted":False,
      "complete_physical_matrix_enclosed":False,
      "global_Weil_positivity_proved":False,"RH_proved":False}
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("NF768 six immutable prior original HD/A Lean batches PASS: 692/968 baseline; 104–111 still pending")

if __name__=="__main__":
    main()
