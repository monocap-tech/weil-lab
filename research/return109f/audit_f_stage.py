#!/usr/bin/env python3
"""Execute exactly one staged F audit in a previously assembled Lean checkout.
Usage: python audit_f_stage.py F6_STAGED_AUDIT.json STAGE EVIDENCE_DIR
Requires the admitted E6 attachment and pinned 314-supplier closure.
"""
import hashlib, json, pathlib, re, subprocess, sys

PLAN_BLOB = "b1f9b37e663fc01face78baa404b1ab1b97be5e9"

E_BLOB = "67fc9656ae64efc72b084634e5ecee10b54aa2c8"
BASE_BLOB = "b25ed55d1ab8511a784cf3863aa630db9bb84a55"

def digest(b):
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def main():
    if not __debug__:
        raise RuntimeError("verification requires assertions enabled")
    assert len(sys.argv) == 4, __doc__
    path, stage, output = sys.argv[1:]
    raw = pathlib.Path(path).read_bytes()
    assert digest(raw) == PLAN_BLOB, "audit plan drift"
    plan = json.loads(raw)
    selected = [s for s in plan["stages"] if s["stage"] == stage]
    assert len(selected) == 1
    selected = selected[0]
    output = pathlib.Path(output)
    output.mkdir(parents=True, exist_ok=False)
    allowed = set(plan["allowed_axioms"])
    assert allowed == {"propext", "Classical.choice", "Quot.sound"}
    closure = json.loads(pathlib.Path("return109f-closure.json").read_text())
    assert closure["named_targets"] == 111
    results = []
    passed = False
    try:
        assert closure["admitted_E_blob"] == E_BLOB
        assert closure["base_assembler_blob"] == BASE_BLOB
        assert closure["supplier_count"] == 314
        assert digest(pathlib.Path("WeilDefect/MasterReturn/LogCarrierBoundedAnalysis.lean").read_bytes()) == E_BLOB
        for entry in selected["modules"]:
            module = entry["module"]
            source = pathlib.Path(module.replace(".", "/") + ".lean")
            assert digest(source.read_bytes()) == entry["blob"], module
            assert closure["staged"][str(source)]["blob"] == entry["blob"], module
            names = re.findall(r"^#print axioms (.+)$", source.read_text(), re.M)
            assert names == entry["targets"], module
            for suffix, cmd in [
                ("build", ["lake", "build", module]),
                ("audit", ["lake", "env", "lean", str(source)])]:
                with (output / (module + "." + suffix + ".log")).open("wb") as log:
                    p = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT)
                assert p.returncode == 0, (module, suffix, p.returncode)
            log = (output / (module + ".audit.log")).read_text()
            for name in names:
                matches = re.findall(r"'" + re.escape(name) + r"' depends on axioms: \[([^\]]*)\]", log)
                noax = log.count(f"'{name}' does not depend on any axioms")
                assert len(matches) + noax == 1, (name, "missing or duplicate audit")
                axioms = {x.strip() for x in matches[0].split(",") if x.strip()} if matches else set()
                assert axioms <= allowed, (name, sorted(axioms-allowed))
                results.append({"name": name, "axioms": sorted(axioms)})
            print("MODULE PASS", module, len(names), flush=True)
        assert len(results) == selected["count"]
        passed = True
        print("STAGE PASS", stage, len(results), flush=True)
    finally:
        (output / "receipt.json").write_text(json.dumps({
            "stage": stage, "expected": selected["count"], "audited": results,
            "complete": passed
        }, indent=2, sort_keys=True)+"\n")

if __name__ == "__main__":
    main()
