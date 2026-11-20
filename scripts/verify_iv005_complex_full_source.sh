#!/usr/bin/env bash
# IV005: manual-only source-specific Lean verification; no CI trigger.
# Usage:
#   bash scripts/verify_iv005_complex_full_source.sh core
#   bash scripts/verify_iv005_complex_full_source.sh composite
# The composite mode additionally verifies IV004 and the combined mixed EF.
set -euo pipefail

MODE="${1:-core}"
case "$MODE" in
  core|composite) ;;
  *) echo "Usage: $0 {core|composite}" >&2; exit 2 ;;
esac
OUT=".iv005-audit/${MODE}"
mkdir -p "$OUT"

modules=(
  "ActualZetaPhaseIVComplexReflection"
  "ActualZetaPhaseIVComplexSchwartzFullSource"
)
if [[ "$MODE" == composite ]]; then
  modules+=("ActualZetaPhaseIVExactMixedGraph" "ActualZetaPhaseIVMixedWeilEF" "ActualZetaPhaseIVAnyComplexMixedEF")
fi

echo "IV005 ${MODE}: actual full-multiplicity zeta source, original complex Schwartz test"
echo "Manual only: no GitHub Actions workflow or numerical runner is triggered."

for stem in "${modules[@]}"; do
  mod="WeilDefect.Arithmetic.${stem}"
  src="WeilDefect/Arithmetic/${stem}.lean"
  echo "=== Build ${mod} ==="
  lake build "$mod" 2>&1 | tee "$OUT/${stem}.build.log"
  echo "=== Strict axiom listing ${stem} ==="
  lake env lean "$src" 2>&1 | tee "$OUT/${stem}.axioms.log"
done

python3 - "$MODE" "$OUT" <<'PY'
import hashlib, json, re, sys
from pathlib import Path

mode=sys.argv[1]
out=Path(sys.argv[2])
checks={
  "ActualZetaPhaseIVComplexReflection": [
    "neutralIV005ConjugateReflection_apply",
    "neutralIV005ConjugateReflection_supported",
    "neutralIV005WindowSchwartz_ae",
    "neutralIV005RawTransform_reflected",
    "neutralIV005WindowEvaluation_reflected",
  ],
  "ActualZetaPhaseIVComplexSchwartzFullSource": [
    "neutralIV005ReflectedMixedCorrelation_C2",
    "neutralIV005ComplexWindowSample_sq_summable",
    "neutralIV005ComplexPartnerSample_sq_summable",
    "neutralIV005ComplexSchwartz_fullSource",
    "neutralIV005CompactComplexSmooth_fullSource",
  ],
}
if mode=="composite":
  checks["ActualZetaPhaseIVExactMixedGraph"] = [
    "neutralIV003GraphMixed_linear_first_add",
    "neutralIV003GraphMixed_linear_first_smul",
    "neutralIV003GraphMixed_hermitian",
    "neutralIV003GraphMixed_self",
    "neutralIV003GraphMixed_self_re",
    "neutralIV003GraphMixed_continuous",
    "neutralIV003GraphMixed_coordinate",
    "neutralIV003LocalGraphDiagonal_coercive",
  ]
  checks["ActualZetaPhaseIVMixedWeilEF"] = [
    "neutralIV004SourceMixed_fullDivisorSum",
    "neutralIV004GraphMixed_eq_literature_of_C2",
    "neutralIV004GraphMixed_eq_literature_of_smoothRepresentative",
    "neutralIV004OriginalCollarsMixedEF",
  ]
  checks["ActualZetaPhaseIVAnyComplexMixedEF"] = [
    "neutralIV005AnyComplexPair_mixedEF",
  ]
results={}
source_hashes={}
olean_hashes={}
for stem,names in checks.items():
  path=Path(f"WeilDefect/Arithmetic/{stem}.lean")
  txt=path.read_text()
  assert not re.search(r"^\s*(sorry|admit|axiom|unsafe)\b",txt,re.M),(stem,"forbidden declaration")
  source_hashes[path.as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
  olean=Path(f".lake/build/lib/lean/WeilDefect/Arithmetic/{stem}.olean")
  assert olean.exists() and olean.stat().st_size>0,(stem,"missing built .olean")
  olean_hashes[stem]=hashlib.sha256(olean.read_bytes()).hexdigest()
  log=(out/f"{stem}.axioms.log").read_text()
  for name in names:
    full="'WeilDefect."+name+"'"
    m=re.search(re.escape(full)+r" depends on axioms: \[([^\]]*)\]",log,re.S)
    if m:
      axs=[x.strip() for x in m.group(1).split(",") if x.strip()]
    else:
      assert full+" does not depend on any axioms" in log,(stem,name,"missing axiom receipt")
      axs=[]
    assert set(axs)<={"propext","Classical.choice","Quot.sound"},(stem,name,axs)
    results[name]=axs
assert len(results)==sum(map(len,checks.values()))
source_inputs=[
  "WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormulaAutomatic.lean",
  "WeilDefect/Arithmetic/ActualZetaSmoothCorrelationRegularity.lean",
  "WeilDefect/Arithmetic/ActualZetaRawSamplesToFullSourceGraph.lean",
  "WeilDefect/Arithmetic/ActualZetaLogCarrierSchwartzCompact.lean",
  "WeilDefect/Arithmetic/ActualZetaWeilZeroForm.lean",
]
for path in source_inputs:
  p=Path(path)
  assert p.exists(),path
  source_hashes[path]=hashlib.sha256(p.read_bytes()).hexdigest()

record={
  "schema":"IV005-authentic-complex-Schwartz-full-zeta-source-v1",
  "mode":mode,
  "sha256":source_hashes,
  "olean_sha256":olean_hashes,
  "standard_axiom_declarations":results,
  "scope":"Exact arbitrary complex finite-window Schwartz full source lift; composite also includes conditional-by-import mixed EF. NO global Weil positivity / RH."
}
(out/"audit.json").write_text(json.dumps(record,indent=2)+"\n")
print(f"IV005 {mode}: {len(results)} actual source declarations LEAN KERNEL PASS, standard axioms only")
PY
