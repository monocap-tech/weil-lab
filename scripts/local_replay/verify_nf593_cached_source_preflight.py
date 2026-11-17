#!/usr/bin/env python3
"""NF593: check every compiled Lean cached interval endpoint against NF591.
This is an executable receipt comparison, not a Lean proof of the check Boolean.
"""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
raw = Path(sys.argv[1]).read_text()
expected = json.loads((root / "notes/data/provisional/NF591_original_fixedpoint_receipt.json").read_text())
assert expected["pass"] == "NF591-exact-fixedpoint-full-box"
assert expected["scale_digits"] == 250
assert expected["primitive_summands"] == 374
assert "NF593_LEAN_EXECUTABLE_PASS" in raw.splitlines()
rows = re.findall(r"^NF593_ROW (\d+) (-?\d+) (-?\d+)$", raw, re.M)
assert len(rows) == 400, len(rows)
assert [int(n) for n, _, _ in rows] == list(range(400))
for (n, lo, hi), (elo, ehi) in zip(rows, expected["intervals"]):
    assert int(lo) == int(elo) and int(hi) == int(ehi), (n,lo,hi,elo,ehi)
print("NF593 compiled cached Lean / NF591 integer replay: ALL 800 endpoints identical")
