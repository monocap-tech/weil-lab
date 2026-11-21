#!/usr/bin/env python3
"""NF748: fail-closed direct Lean import order for recovered original NF748.

This verifies only the dependency order of source-authenticated NF681,
NF703Cache, NF704Frontier modules, and existence of required previously
accepted compiled .olean imports. It does NOT assert any numerical theorem.
The separate NF748 real kernel job and 35-name axiom audit remain mandatory.
"""
import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path

ROOT=Path("WeilDefect")
OBJECTS=Path(".lake/build/lib/lean/WeilDefect")
ORDER=(
    "Generated.NF681.Common",
    "Generated.NF703Cache.Frontier",
    *(f"Generated.NF681.Col{i:03d}" for i in range(64,72)),
    "Generated.NF704Frontier.Common",
)
RECEIPT=Path("nf748-original-indexzero-compiler-import-order.json")

def imports(text):
    """Only genuine import declarations, never matching doc comments."""
    return re.findall(r"^[ \t]*import[ \t]+WeilDefect\.([A-Za-z0-9_.]+)\s*$",text,re.M)

def source_for(module,root):
    return root/Path(module.replace(".","/")+".lean")

def object_for(module,objects):
    return objects/Path(module.replace(".","/")+".olean")

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def check_order(root,objects,order):
    assert len(order)==len(set(order)),("duplicate declared module",order)
    assert len(order)>=2
    positions={m:i for i,m in enumerate(order)}
    edges=[]
    reused=[]
    source_hashes={}
    reused_hashes={}
    for i,module in enumerate(order):
        src=source_for(module,root)
        assert src.is_file(),("required original generated Lean source missing",str(src))
        source_hashes[module]=sha(src)
        imported=imports(src.read_text())
        assert len(imported)==len(set(imported)),("duplicate original imports",module)
        for dep in imported:
            assert dep!=module,("self-import",module)
            if dep in positions:
                assert positions[dep]<i,(
                    "compile order violates actual original Lean import dependency",
                    module,dep,i,positions[dep])
                edges.append([dep,module])
            elif dep.startswith("Generated."):
                obj=object_for(dep,objects)
                assert obj.is_file() and obj.stat().st_size>0,(
                    "unplanned missing original compiled dependency",
                    module,dep,str(obj))
                reused.append(dep)
                reused_hashes[dep]=sha(obj)
    # This precise historical error occurred after source/cache equality
    # succeeded: Frontier requires NF681.Common. A later source rewrite that
    # changes this edge is NOT silently accepted as the historical repair.
    frontier="Generated.NF703Cache.Frontier"
    common="Generated.NF681.Common"
    assert common in imports(source_for(frontier,root).read_text()),(
        "actual original Frontier no longer has recovered NF681.Common import")
    assert [common,frontier] in edges,("specific original missing-import edge not covered")
    return {
        "schema":"NF748-source-actual-original-indexzero-064-071-import-DAG-v1",
        "compiler_order":list(order),
        "in_plan_direct_import_edges":edges,
        "out_of_plan_olean_imports_present":sorted(set(reused)),
        "original_source_sha256":source_hashes,
        "prior_compiled_dependency_olean_sha256":reused_hashes,
        "actual_recovered_Frontier_depends_on_NF681_Common":True,
        "new_original_numerical_kernel_pass":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }

def verify():
    result=check_order(ROOT,OBJECTS,ORDER)
    RECEIPT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF748 original prerequisite order PASS:",
          "NF681.Common precedes NF703Cache.Frontier;",
          len(ORDER),"source-specific modules checked; new numerical Lean proof still required")

def selftest():
    with tempfile.TemporaryDirectory(prefix="nf748-import-") as folder:
        root=Path(folder)/"WeilDefect"
        objects=Path(folder)/"oleans"
        first,second=ORDER[:2]
        s1=source_for(first,root)
        s2=source_for(second,root)
        s1.parent.mkdir(parents=True,exist_ok=True)
        s2.parent.mkdir(parents=True,exist_ok=True)
        s1.write_text("import WeilDefect.Generated.NF702Inputs.Data\n")
        s2.write_text("import WeilDefect.Generated.NF681.Common\n")
        accepted=object_for("Generated.NF702Inputs.Data",objects)
        accepted.parent.mkdir(parents=True,exist_ok=True)
        accepted.write_bytes(b"synthetic accepted module placeholder, NOT REAL LEAN")
        assert check_order(root,objects,(first,second))[
            "actual_recovered_Frontier_depends_on_NF681_Common"]
        cases=["correct_direct_import_order"]
        try:
            check_order(root,objects,(second,first))
        except AssertionError:
            cases.append("inverted_original_import_order_rejected")
        else:
            raise AssertionError("inverted import order falsely accepted")
        accepted.unlink()
        try:
            check_order(root,objects,(first,second))
        except AssertionError:
            cases.append("missing_other_original_olean_dependency_rejected")
        else:
            raise AssertionError("unbound prerequisite falsely accepted")
        accepted.write_bytes(b"synthetic accepted module placeholder, NOT REAL LEAN")
        s2.write_text("-- import WeilDefect.Generated.NF681.Common\n")
        try:
            check_order(root,objects,(first,second))
        except AssertionError:
            cases.append("comment_cannot_satisfy_required_import_edge")
        else:
            raise AssertionError("comment falsely accepted")
    print("NF748 four synthetically scoped import DAG tests PASS;",
          "no actual source/Lean kernel verified")
    return cases

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("verify","selftest"))
    args=p.parse_args()
    if args.stage=="verify":
        verify()
    else:
        selftest()
