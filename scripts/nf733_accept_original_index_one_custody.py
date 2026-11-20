#!/usr/bin/env python3
"""NF733: permanent source-bound custody of NF732's REAL Lean kernel PASS.

Only the GitHub-successful NF732 original full numerical run is an eligible
upstream. This does not itself prove another theorem: it validates the source,
numerical input .olean SHA attestations, both theorem names, the full original
index-one propositions, the exact Lean axiom output and the accepted artifact
identity, then writes an immutable-source-compatible machine-readable ledger.

The source and kernel artifacts must be restored independently from the
completed upstream NF732 run. A missing object, unknown proof identity or
source mismatch is a failure, never a fallback to a synthetic certificate.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

SOURCE=Path("nf733-accepted-original-source")
KERNEL=Path("nf733-accepted-original-kernel")
OUT=Path("nf733-original-index-one-custody.json")
STARTS=(0,4,8,12,16,20,24,28)
THEOREMS=["nf732OriginalHDRowOneAll","nf732OriginalAColumnOneAll"]
ALLOWED={"propext","Classical.choice","Quot.sound"}
RUN_ID=44774641598
KERNEL_JOB=136435817033
SOURCE_ARTIFACT=14650533188
KERNEL_ARTIFACT=14652985322
PURE_ARTIFACT=14651825109
SOURCE_PATH=SOURCE/"WeilDefect/Generated/NF732/ActualOriginalFull.lean"
SOURCE_MANIFEST=SOURCE/"WeilDefect/Generated/NF732/manifest.json"
PROOF_MANIFEST=KERNEL/"WeilDefect/Generated/NF732/manifest.json"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def json_file(path):
    return json.loads(Path(path).read_text())


def only_axioms(log):
    data={}
    for name,raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in THEOREMS:
            assert name not in data,name
            data[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in THEOREMS:
            assert name not in data
            data[name]=[]
    assert set(data)==set(THEOREMS),(data,THEOREMS)
    assert all(set(xs)<=ALLOWED for xs in data.values()),data
    assert not re.search(r"^.*(?:error:|##\[error\])",log,re.I|re.M), "Lean errors present"
    return data


def verify():
    assert SOURCE_PATH.is_file() and SOURCE_MANIFEST.is_file()
    assert PROOF_MANIFEST.is_file()
    assert digest(SOURCE_MANIFEST)==digest(PROOF_MANIFEST)
    src=SOURCE_PATH.read_text()
    assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",src,re.M)
    assert re.findall(r"^theorem (nf732Original\w+)",src,re.M)==THEOREMS
    assert (
       "∀ i : Fin 242, nf703OriginalCache.HDGate nf702OriginalInputs (1 : Fin 242) i = true"
       in src
    )
    assert (
       "∀ i : Fin 242, nf703OriginalCache.AGate nf702OriginalInputs i (1 : Fin 242) = true"
       in src
    )
    manifest=json_file(SOURCE_MANIFEST)
    assert manifest["schema"]=="NF732-exact-original-physical-global-HD-A-index-one-8-quad-full-source-v1"
    assert manifest["source_sha256"]==digest(SOURCE_PATH)
    assert manifest["new_original_universal_theorems"]==THEOREMS
    assert manifest["accepted_original_global_gate_coordinate_counts"]=={"HD":242,"A":242}
    assert manifest["accepted_prior_original_theorem_declarations"]==252
    assert manifest["nf729_original_source_preflight_run_id"]==44767040253
    assert manifest["nf729_original_source_preflight_artifact_id"]==14645281954
    assert len(manifest["required_NF729_numerical_quad_modules"])==8
    assert manifest["required_NF729_numerical_quad_modules"]==[
        f"WeilDefect.Generated.NF729.Quad{x:03d}Original" for x in STARTS
    ]
    expected_numeric=[
        f"nf729Original{typ}Quad{b:03d}"
        for b in STARTS for typ in ("HD","A")
    ]
    assert manifest["required_NF729_numerical_quad_theorems"]==expected_numeric
    assert re.findall(r"^    (nf729Original(?:HD|A)Quad\d{3})$",src,re.M)==[
        f"nf729OriginalHDQuad{b:03d}" for b in STARTS
    ]+[f"nf729OriginalAQuad{b:03d}" for b in STARTS]
    for q in STARTS:
        assert (SOURCE/f"WeilDefect/Generated/NF729/Quad{q:03d}Original.lean").is_file()
    assert len(manifest["accepted_prior_NF728_original_bank_manifest_sha256"])==64
    kernel_file=KERNEL/"nf732-original-complete-audit.json"
    assert kernel_file.is_file()
    accepted=json_file(kernel_file)
    assert accepted["schema"]=="NF732-actual-original-HD-and-A-complete-index-one-lean-kernel-v1"
    assert accepted["source_sha256"]==digest(SOURCE_PATH)
    assert accepted["source_manifest_sha256"]==digest(SOURCE_MANIFEST)
    assert accepted["theorems"]==THEOREMS
    assert accepted["HD_row_index"]==1 and accepted["A_column_index"]==1
    assert accepted["HD_actual_original_gate_coordinates"]==242
    assert accepted["A_actual_original_gate_coordinates"]==242
    assert "KERNEL PASS" in accepted["status"]
    original_log=KERNEL/"nf732-original-axioms.log"
    assert original_log.is_file()
    axioms=only_axioms(original_log.read_text())
    assert accepted["axioms"]==axioms
    proof_inputs=KERNEL/"nf732-accepted-original-numerical-inputs.json"
    assert proof_inputs.is_file()
    numeric=json_file(proof_inputs)
    assert numeric["schema"]=="NF732-original-eight-accepted-NF729-numerical-quad-olean-inputs-v1"
    assert numeric["upstream_run_id"]==44767040253
    assert numeric["all_eight_accepted_original_quad_kernel_runs"] is True
    assert numeric["eight_original_gate_ranges_complete_Fin242"] is True
    assert numeric["original_HD_gate_range_claims"]==8
    assert numeric["original_A_gate_range_claims"]==8
    assert len(numeric["sources"])==8
    assert [x["quad"] for x in numeric["sources"]]==list(STARTS)
    assert accepted["upstream_8_accepted_quad_lean_objects_sha256"]==digest(proof_inputs)
    for x in numeric["sources"]:
        b=x["quad"]
        assert x["proof_theorems"]==[
           f"nf729OriginalHDQuad{b:03d}", f"nf729OriginalAQuad{b:03d}"]
        assert x["original_source_sha256"]==digest(
           SOURCE/f"WeilDefect/Generated/NF729/Quad{b:03d}Original.lean"
        )
        assert x["source_manifest_sha256"]==manifest["accepted_source_provenance_manifest_sha256"]
        assert re.fullmatch(r"[0-9a-f]{64}",x["olean_sha256"])
        assert re.fullmatch(r"[0-9a-f]{64}",x["accepted_original_numerical_audit_sha256"])
    assert sorted(numeric["installed_compiled_modules"])==sorted(
        set(numeric["installed_compiled_modules"]))
    for path,h in numeric["installed_compiled_modules"].items():
        assert not path.startswith("/") and ".." not in Path(path).parts
        assert re.fullmatch(r"[0-9a-f]{64}",h)
    final={
      "schema":"NF733-accepted-original-global-HD-row-one-A-column-one-Lean-custody-v1",
      "source_run":RUN_ID,
      "accepted_original_universal_kernel_job":KERNEL_JOB,
      "accepted_kernel_artifact":KERNEL_ARTIFACT,
      "accepted_original_source_artifact":SOURCE_ARTIFACT,
      "accepted_generic_full_Fin242_kernel_artifact":PURE_ARTIFACT,
      "original_global_universal_theorems":THEOREMS,
      "original_global_HDGates_row_one":242,
      "original_global_AGates_column_one":242,
      "original_complete_index_one_product_gates":484,
      "accepted_independent_numerical_quads":list(STARTS),
      "accepted_actual_original_numerical_quad_theorems":expected_numeric,
      "standard_axioms":axioms,
      "source_sha256":digest(SOURCE_PATH),
      "source_manifest_sha256":digest(SOURCE_MANIFEST),
      "accepted_kernel_audit_sha256":digest(kernel_file),
      "accepted_numerical_inputs_sha256":digest(proof_inputs),
      "accepted_axioms_log_sha256":digest(original_log),
      "original_all_other_matrix_indices_kernel_accepted":False,
      "original_complete_numerical_enclosure_closed":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "standing":"The two full actual index-one universal gate statements are accepted by Lean with exact original NF702/NF703 source and eight independently accepted original numerical quad objects. This is not complete matrix, vector, payment or global Weil positivity."
    }
    OUT.write_text(json.dumps(final,indent=2,sort_keys=True)+"\n")
    print("NF733 SOURCE AND KERNEL CUSTODY PASS: original HD row1 242/242 and original A column1 242/242, 2 Lean universal declarations, strict axioms and 8 accepted numerical quad provenance receipts. All other global matrix/payment/Weil goals OPEN.")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("verify",))
    a=p.parse_args()
    verify()
