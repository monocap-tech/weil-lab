#!/usr/bin/env python3
"""NF722: strict source-bounded audit of the generic 31-block Fin 242 gluing proof.

Only the accepted Mathlib/Lean core axioms are allowed. The three theorems
cannot be mistaken for authentic full original row-one gates: their 31 actual
global numerical premises must still be provided by independently checked
Lean modules from NF715..NF720 (including NF717).
"""
import hashlib
import json
import re
from pathlib import Path

SRC = Path("WeilDefect/Arithmetic/ActualZetaOriginalPhysicalPackedRowOneFiniteClosure.lean")
LOG = Path("nf722-axioms.log")
NAMES = {
    "neutralNF722Fin242OfPackedBlocks",
    "neutralNF722HDIndexOneOfPackedBlocks",
    "neutralNF722AIndexOneOfPackedBlocks"
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def source_plan():
    src = SRC.read_text()
    assert len(set(re.findall(r"\btheorem (neutralNF722\w+)", src))) == 3
    assert set(re.findall(r"\btheorem (neutralNF722\w+)", src)) == NAMES
    assert "sorry" not in src and "admit" not in src
    blocks = []
    for b in range(31):
        width = min(8, 242 - 8*b)
        assert width == (2 if b == 30 else 8)
        key = f"h{b:03d}"
        coordinate = (
            "(⟨k.val, by omega⟩ : Fin 242)" if b == 0
            else f"(⟨{8*b} + k.val, by omega⟩ : Fin 242)"
        )
        for kind in ("P", "HDGate", "AGate"):
            if kind == "P":
                check = f"({key} : ∀ k : Fin {width}, P {coordinate})"
            elif kind == "HDGate":
                check = (
                    f"({key} : ∀ k : Fin {width}, "
                    f"c.HDGate s (1 : Fin 242) {coordinate} = true)"
                )
            else:
                check = (
                    f"({key} : ∀ k : Fin {width}, "
                    f"c.AGate s {coordinate} (1 : Fin 242) = true)"
                )
            assert src.count(check) == 1, (b, kind, src.count(check))
        blocks.append({"block": b, "start": b*8,
                       "end": min((b+1)*8,242), "width": width})
    assert blocks[0]["start"] == 0 and blocks[-1]["end"] == 242
    assert sum(b["width"] for b in blocks) == 242
    return blocks


def verify():
    blocks = source_plan()
    log = LOG.read_text()
    found = {}
    for n, x in re.findall(
            r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]", log):
        if n in NAMES:
            assert n not in found, n
            found[n] = [s.strip() for s in x.split(",") if s.strip()]
    for n in re.findall(
            r"'WeilDefect\.(\w+)' does not depend on any axioms", log):
        if n in NAMES:
            assert n not in found, n
            found[n] = []
    assert set(found) == NAMES, (NAMES-set(found), set(found)-NAMES)
    assert all(set(z) <= ALLOWED for z in found.values())
    result = {
        "schema": "NF722-actual-original-row-one-packed-finite-gluing-v1",
        "source_sha256": hashlib.sha256(SRC.read_bytes()).hexdigest(),
        "theorems": sorted(NAMES),
        "axioms": found,
        "blocks": blocks,
        "coordinates": list(range(242)),
        "confirmed_numerical_premises": False,
        "full_original_index_one_HD_or_A_accepted": False,
        "scope": (
            "Certified generic Fin 242 finite-block assembly only. "
            "The accepted mathematical theorem takes 31 HD and 31 A "
            "authentic global product premise families; it does not prove "
            "any original numerical product gates. NF717 remains required."
        ),
    }
    Path("nf722-complete-audit.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("NF722 exact 31-block/242-index gluing: 3 declarations standard-axiom LEAN PASS; actual numerical all-coordinate application still OPEN")


if __name__ == "__main__":
    verify()
