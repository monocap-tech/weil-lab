#!/usr/bin/env bash
set -euo pipefail
# Arguments: isolated pristine pinned research checkout, manifest, evidence directory.
root="$(realpath "$1")"
manifest="$(realpath "$2")"
out="$(realpath -m "$3")"
mkdir -p "$out"
python3 "$(dirname "$manifest")/preflight.py" "$manifest" "$root" "$out" 2>&1 | tee "$out/preflight.log"
cd "$root"
lean --version | tee "$out/lean-version.txt"
lake exe cache get 2>&1 | tee "$out/cache.log"
mod=WeilDefect.Arithmetic.ActualZetaIV106W02SchurCompletion
src="${mod//./\/}.lean"
obj=".lake/build/lib/lean/${mod//./\/}.olean"
rm -f "$obj"
touch "$out/fresh.stamp"
lake build "$mod" 2>&1 | tee "$out/build.log"
test -s "$obj"
test "$obj" -nt "$out/fresh.stamp"
cp "$src" "$obj" "$out/"
sha256sum "$src" "$obj" > "$out/sha256.txt"
test -f lake-manifest.json
cp lake-manifest.json "$out/"
lake env lean "$out/audit.lean" 2>&1 | tee "$out/axioms.log"
python3 - "$out" <<'PY'
import pathlib,re,json,sys
p=pathlib.Path(sys.argv[1])
expected=json.loads((p/'expected_names.json').read_text())
s=(p/'axioms.log').read_text()
pattern=r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]"
ms=list(re.finditer(pattern,s,re.S))
assert len(ms)==len(expected)==5 and not re.sub(pattern,'',s,flags=re.S).strip()
assert {m[1] for m in ms}==set(expected)
assert all({x.strip() for x in m[2].split(',') if x.strip()} <= {'propext','Classical.choice','Quot.sound'} for m in ms)
print('STRICT NAMED AXIOMS PASS 5/5')
PY
