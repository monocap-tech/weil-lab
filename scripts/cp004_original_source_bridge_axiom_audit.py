#!/usr/bin/env python3
"""Fail-closed CP004 original IV011 source-bridge Lean audit.

Only a genuinely compiled .olean and real Lean #print axioms output count.
This does NOT certify the frozen three-bump overlap table; hypotheses are
explicit in the source theorem statements.
"""
import hashlib
import json
import re
from pathlib import Path

SOURCE=Path("WeilDefect/Arithmetic/ActualZetaCrossProjectionPrimeAttachment.lean")
OLEAN=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaCrossProjectionPrimeAttachment.olean")
LOG=Path("cp004-original-iv011-axioms.log")
RECEIPT=Path("cp004-original-source-bridge-audit.json")
NAMES=[
 "neutralCP004OriginalCorrelationIntegral",
 "neutralCP004OriginalPrimeFiniteTen",
 "neutralCP004OriginalPrimeSingleN9_of_otherTermsZero",
 "neutralCP004OriginalPrimeZero_of_allTermsZero",
]
ALLOWED={"propext","Classical.choice","Quot.sound"}

def main():
    assert SOURCE.is_file() and OLEAN.is_file() and LOG.is_file(), "Real source, olean, or axiom log missing"
    text=SOURCE.read_text(encoding="utf-8")
    output=LOG.read_text(encoding="utf-8")
    assert "sorry" not in re.sub(r"/-.*?-/", "", text, flags=re.S), "Sorry text found: fail closed"
    assert "sorryAx" not in output and "error:" not in output, "Compiler/axiom error: fail closed"
    ax={}
    for name in NAMES:
        assert re.search(r"\btheorem\s+"+re.escape(name)+r"\b",text), f"Missing exact theorem {name}"
        rex=re.compile(r"(?m)^.*?WeilDefect\."+re.escape(name)+r"['\s].*?(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on (?:any )?axioms)")
        matches=rex.findall(output)
        assert len(matches)==1, f"Expected one real Lean axiom print for {name}, found {len(matches)}"
        deps={x.strip() for x in matches[0].split(",") if x.strip()}
        assert deps<=ALLOWED, f"Nonstandard axioms for {name}: {deps-ALLOWED}"
        ax[name]=sorted(deps)
    receipt={"result":"LEAN_SOURCE_BRIDGE_PASS",
             "scope":"conditional IV011 correlation / finite prime wrappers only, NOT frozen-bump source closure",
             "source_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
             "olean_sha256":hashlib.sha256(OLEAN.read_bytes()).hexdigest(),
             "axioms":ax}
    RECEIPT.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(receipt["result"])

if __name__=="__main__":
    main()
