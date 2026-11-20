#!/usr/bin/env bash
# IV004 local/manual proof audit. Not registered as an automatic Actions job.
set -euo pipefail

SOURCE="WeilDefect/Arithmetic/ActualZetaPhaseIVMixedWeilEF.lean"
MODULE="WeilDefect.Arithmetic.ActualZetaPhaseIVMixedWeilEF"
OUT="${1:-.iv004-audit}"
mkdir -p "$OUT"

echo "IV004 — source-specific source graph / mixed genuine Weil EF"
echo "No GitHub CI trigger; this verifier must be run explicitly."
lake build "$MODULE" 2>&1 | tee "$OUT/lean-build.log"
lake env lean "$SOURCE" 2>&1 | tee "$OUT/lean-axioms.log"

python3 - "$SOURCE" "$OUT" <<'PY'
import hashlib, json, re, sys
from pathlib import Path

source=Path(sys.argv[1])
audit=Path(sys.argv[2])
log=(audit/"lean-axioms.log").read_text()
raw=source.read_text()
assert not re.search(r"^\s*(sorry|admit|axiom|unsafe)\b",raw,re.M), "Forbidden source declaration"
names=(
 "neutralIV004SourceMixed_fullDivisorSum",
 "neutralIV004GraphMixed_eq_literature_of_C2",
 "neutralIV004GraphMixed_eq_literature_of_smoothRepresentative",
 "neutralIV004OriginalCollarsMixedEF",
)
records={}
for name in names:
  full="'WeilDefect."+name+"'"
  m=re.search(re.escape(full)+r" depends on axioms: \[([^\]]*)\]",log,re.S)
  if m:
    axs=[x.strip() for x in m.group(1).split(",") if x.strip()]
  else:
    assert full+" does not depend on any axioms" in log,("Missing theorem axiom receipt",name)
    axs=[]
  assert "sorryAx" not in axs,(name,axs)
  assert set(axs)<={"propext","Classical.choice","Quot.sound"},(name,axs)
  records[name]=axs
assert len(records)==4
inputs={}
for file in [
 "WeilDefect/Arithmetic/ActualZetaPhaseIVExactMixedGraph.lean",
 "WeilDefect/Arithmetic/ActualZetaPhaseIVMixedWeilEF.lean",
 "WeilDefect/Arithmetic/ActualZetaSourceDecomposition.lean",
 "WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormulaAutomatic.lean",
 "WeilDefect/Arithmetic/ActualZetaSmoothCorrelationRegularity.lean",
]:
  p=Path(file)
  assert p.exists(),file
  inputs[file]=hashlib.sha256(p.read_bytes()).hexdigest()
rec={
 "schema":"IV004-source-bound-two-argument-mixed-Weil-EF-v1",
 "input_source_sha256":inputs,
 "accepted_new_theorems":records,
 "scope":"Actual full-multiplicity source graph and literal mixed WINDOWED EF, conditional on C² correlation or exact compact-smooth representative; no universal signed positivity, arbitrary Schwartz graph lift, or RH."
}
(audit/"audit.json").write_text(json.dumps(rec,indent=2)+"\n")
print("IV004: four exact genuine mixed Weil EF declarations kernel/standard-axiom PASS")
PY
