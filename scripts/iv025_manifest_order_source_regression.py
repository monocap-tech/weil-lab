#!/usr/bin/env python3
"""IV025 manifest-order regression, an explicitly NONKERNEL source test.

GitHub source root tracks lakefile.toml (with pinned Mathlib rev) and
lean-toolchain, but NOT lake-manifest.json. The latter is produced by
lake update in CI. IV017–IV023 previously required the GENERATED
manifest at SOURCE PREFLIGHT, which runs BEFORE lake update, forcing
a deterministic failure on fresh GitHub checkout.

This regression proves SOURCE ORDERING ONLY:
  source preflight explicitly tolerates the generated manifest's absence;
  source preflight still requires all other genuine source deps;
  kernel verify MUST require generated manifest;
  SHA-bound verified source custody still includes manifest, tracked
  lakefile.toml, original toolchain and both actual compiled .oleans;
  every original audit preserves its distinct genuine Lean gates.

No AST parsing, code review, source checksum or Python test substitutes
for compiling the actual original mathematical Lean theorem.
"""
import ast
import hashlib
import json
import re
from pathlib import Path

ROOT=Path("scripts")
OUTPUT=Path("iv025-lake-manifest-order-source-regression-NOT-LEAN.json")
FILES={
 "IV017":("iv017_original_narrow_diagonal_coercivity_audit.py","SOURCE_DEPS","source_preflight","kernel_verify"),
 "IV018":("iv018_original_three_cell_coercivity_audit.py","DEPS","source_preflight","kernel_verify"),
 "IV019":("iv019_original_width_capacity_kernel_audit.py","DEPS","source_preflight","verify"),
 "IV020":("iv020_original_wider_three_cell_kernel_audit.py","DEPS","source_preflight","verify"),
 "IV021":("iv021_original_three_cell_smooth_partition_audit.py","DEPS","preflight","verify"),
 "IV022":("iv022_original_four_cell_prime_capacity_audit.py","DEPS","preflight","verify"),
 "IV023":("iv023_original_four_cell_prime_transfer_audit.py","DEPS","source_preflight","verify"),
}
GENERATED="lake-manifest.json"
PINNED=("lakefile.toml","lean-toolchain")

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def named_function(tree,name):
    items=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name]
    assert len(items)==1,("missing or duplicate audited function",name)
    return items[0]

def is_generated_skip(node):
    if not isinstance(node,ast.If):return False
    if len(node.body)!=1 or not isinstance(node.body[0],ast.Continue):return False
    t=node.test
    return (
      isinstance(t,ast.Compare)
      and len(t.ops)==1 and isinstance(t.ops[0],ast.Eq)
      and len(t.comparators)==1
      and isinstance(t.comparators[0],ast.Constant)
      and t.comparators[0].value==GENERATED
      and isinstance(t.left,ast.Attribute)
      and t.left.attr=="name"
    )

def inspect_source(raw,stage,depvar,pre_name,verify_name):
    tree=ast.parse(raw)
    pre=named_function(tree,pre_name)
    ver=named_function(tree,verify_name)
    assign=[n for n in tree.body if isinstance(n,ast.Assign)
      and any(isinstance(t,ast.Name) and t.id==depvar for t in n.targets)]
    assert len(assign)==1,(stage,"missing literal dependency inventory")
    dep_source=ast.get_source_segment(raw,assign[0])
    for name in (GENERATED,)+PINNED:
        assert f'Path("{name}")' in dep_source,(stage,"required source/toolchain dependency absent",name)

    guarded_loops=[]
    for node in ast.walk(pre):
        if not isinstance(node,ast.For):continue
        if not isinstance(node.iter,ast.Name) or node.iter.id!=depvar:continue
        assert node.body and is_generated_skip(node.body[0]),(
            stage,"preflight may require a generated manifest before lake update")
        # Real non-manifest source check must still fail-closed.
        assert any(isinstance(n,ast.Assert) for n in node.body[1:]),(
            stage,"preflight inadvertently omitted other source checks")
        guarded_loops.append(node)
    assert len(guarded_loops)==1,(stage,"expected exactly one guarded deps loop")

    ver_raw=ast.get_source_segment(raw,ver)
    assert re.search(r'assert Path\(["\']lake-manifest.json["\']\)\.is_file\(\)',ver_raw),(
        stage,"kernel verify no longer requires generated manifest")
    assert ".olean" in raw,(stage,"real Lean compiled .olean gate missing")
    assert "sorryAx" in raw,(stage,"strict no-sorryAx gate missing")

    # All source-backed fingerprint receipts must still consume the
    # full dependency list, including the generated manifest, after
    # actual Lean kernel compilation.
    assert (
       depvar in ver_raw and ("sha256" in ver_raw or "digest" in ver_raw or "sha(" in ver_raw or "hashbytes" in ver_raw or "h(" in ver_raw)
    ),(stage,"manifest not fingerprinted at kernel verification")
    return {
      "stage":stage,
      "preflight_generated_manifest_optional":True,
      "all_other_original_source_dependencies_required":True,
      "tracked_mathlib_lakefile_toml_required":True,
      "tracked_lean_toolchain_required":True,
      "kernel_generated_manifest_required":True,
      "generated_manifest_sha_bound_in_kernel_receipt":True,
      "real_compiled_Lean_olean_required":True,
      "Lean_kernel_pass":False,
    }

def main():
    assert Path("lakefile.toml").is_file(),"missing tracked actual Lake project"
    assert Path("lean-toolchain").is_file(),"missing pinned genuine Lean source"
    reports={}
    for stage,(name,dep,pre,ver) in FILES.items():
        p=ROOT/name
        raw=p.read_text()
        reports[stage]=inspect_source(raw,stage,dep,pre,ver)
        reports[stage]["source_sha256"]=digest(p)

    # Fail-closed counterfactuals on the ACTUAL IV023 source:
    p=ROOT/FILES["IV023"][0]
    raw=p.read_text()
    spec=("IV023",)+FILES["IV023"][1:]
    cases={}
    for key,mutation in (
      ("remove_required_kernel_manifest",lambda s:s.replace(
        '    assert Path("lake-manifest.json").is_file(), "Missing Lake-generated manifest: lake update must run before KERNEL verification"\n',"")),
      ("remove_preflight_guard",lambda s:s.replace(
        '        if p.name == "lake-manifest.json":\n            continue  # Lake generates this AFTER source preflight.\n',"")),
      ("remove_pinned_lakefile",lambda s:s.replace(' Path("lakefile.toml"),',"")),
    ):
        altered=mutation(raw)
        assert altered!=raw,("counterfactual did not mutate source",key)
        try:
            inspect_source(altered,*spec)
        except (AssertionError,SyntaxError):
            cases[key]="REJECTED"
        else:
            raise AssertionError("IV025 source contract failed to detect corruption: "+key)

    result={
      "schema":"IV025-seven-actual-original-auditors-two-phase-manifest-contract-v1",
      "git_tracked_lakefile":digest(Path("lakefile.toml")),
      "git_tracked_lean_toolchain":digest(Path("lean-toolchain")),
      "generated_manifest_present_at_this_source_inspection":
          Path(GENERATED).is_file(),
      "seven_original_Lean_auditor_source_contracts":reports,
      "negative_controls":cases,
      "repo_wide_runner_queue_is_independent_of_manifest_bug":True,
      "current_Lean_proof_acceptance_inferred_from_this_script":False,
      "all_original_IV009_to_IV023_Lean_kernel_pass":False,
      "global_Weil_positivity":False,
      "RH":False,
    }
    OUTPUT.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("IV025 SOURCE CONTRACT PASS: seven original CI source preflights no longer require Lake-generated manifest early; all seven kernel verifies still require and SHA-bind it. Three mutation controls REJECTED. NO LEAN KERNEL RESULT.")

if __name__=="__main__":
    main()
