#!/usr/bin/env bash
# W02-NF-08/09: isolated native gate. No workflow dispatch or publication.
# Run from any existing Weil-Lab checkout with bash, git, python3, elan, lean, lake.
# Usage: bash scripts/local_replay/NF618W02NativeGate.sh /absolute/evidence-directory
set -euo pipefail
PIN=5801507d416e4a699c002920b2441f5aa0c19aef
MATHLIB=5ed2965256430c3649e86755f9576b54eca72435
SRC=notes/provisional/NF618W02RootAttachment
ARITH=WeilDefect/Arithmetic
for x in git python3 elan lean lake; do command -v "$x" >/dev/null || { echo "Missing $x; install pinned Lean using Elan" >&2; exit 2; }; done
repo=$(git rev-parse --show-toplevel)
git -C "$repo" cat-file -e "$PIN^{commit}"
out=$(python3 -c 'import os,sys;print(os.path.abspath(sys.argv[1]))' "${1:-./nf618-w02-native-evidence}")
mkdir "$out" # refuse to overwrite earlier evidence
exec > >(tee "$out/runner.log") 2>&1
tmp=$(mktemp -d)
work="$tmp/checkout"
cleanup() { git -C "$repo" worktree remove --force "$work" || true; rmdir "$tmp" || true; }
trap cleanup EXIT
git -C "$repo" worktree add --detach "$work" "$PIN"
cd "$work"
test "$(git rev-parse HEAD)" = "$PIN"
printf '%s\n' "$PIN" > "$out/source-commit.txt"
test "$(cat lean-toolchain)" = leanprover/lean4:v4.34.0
cp lean-toolchain lakefile.toml "$out/"
check_blob() { test "$(git hash-object "$1")" = "$2" || { echo "Source identity mismatch: $1" >&2; exit 3; }; }
check_blob "$SRC/ActualZetaOriginalPhysicalSemanticEndpointCache.lean.txt" 66273c57a9dac69913c72f7826aaf0e6c3860eeb
check_blob "$SRC/ActualZetaOriginalPhysicalHybridEndpoint.lean.txt" ffc05cf064b4db7e355bf6624c5463545ac02f65
check_blob "$SRC/RootAttachmentCandidate.lean.txt" bed8b192f3741c88f27f877ce82a3e8952e82bf9
printf '%s  %s\n' c28806932277661273bc6f48a34a4119fae242a9dbd88e296c7dfd83477e3d3f "$SRC/ActualZetaOriginalPhysicalSemanticEndpointCache.lean.txt" 4c37c0b40eacc78583aa0c74222446166f764d86c0fc53c4ff482c938730dc55 "$SRC/ActualZetaOriginalPhysicalHybridEndpoint.lean.txt" | sha256sum -c -
for name in ActualZetaOriginalPhysicalSemanticEndpointCache ActualZetaOriginalPhysicalHybridEndpoint; do
  dst="$ARITH/$name.lean"
  if test -e "$dst"; then cmp "$SRC/$name.lean.txt" "$dst"; else cp "$SRC/$name.lean.txt" "$dst"; fi
  cp "$dst" "$out/"
done
candidate="$ARITH/NF618W02RootAttachmentCandidate.lean"
test ! -e "$candidate"
cp "$SRC/RootAttachmentCandidate.lean.txt" "$candidate"
cp "$candidate" "$out/"
# Preflight local import closure. Missing project sources are reported, never stubbed.
python3 - "$candidate" "$out" <<'PY'
import json,re,subprocess,sys
from pathlib import Path
todo=[Path(sys.argv[1])]
seen={}
missing=[]
while todo:
    p=todo.pop()
    if str(p) in seen: continue
    if not p.is_file():
        missing.append(str(p));seen[str(p)]=None;continue
    seen[str(p)]=subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
    for line in p.read_text().splitlines():
        m=re.match(r'^\s*(?:(?:public|private)\s+)?import\s+(.+)$',line)
        if m:
            for mod in m.group(1).split('--',1)[0].split():
                if mod.startswith('WeilDefect.'):
                    todo.append(Path(mod.replace('.','/')+'.lean'))
Path(sys.argv[2],'project-imports.json').write_text(json.dumps({'files':seen,'missing':missing},indent=2)+'\n')
if missing: raise SystemExit('Missing project imports: '+', '.join(sorted(set(missing))))
PY
elan toolchain install "$(cat lean-toolchain)"
lean --version | tee "$out/lean-version.txt"
lake --version | tee "$out/lake-version.txt"
lake update 2>&1 | tee "$out/lake-update.log"
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = "$MATHLIB"
cp lake-manifest.json "$out/"
lake exe cache get 2>&1 | tee "$out/mathlib-cache.log"
lake build WeilDefect.Arithmetic.ActualZetaOriginalPhysicalHybridEndpoint 2>&1 | tee "$out/adapter-build.log"
lake env lean "$candidate" 2>&1 | tee "$out/candidate-axioms.log"
python3 - "$out" <<'PY'
import hashlib,json,re,sys
from pathlib import Path
p=Path(sys.argv[1])
expected={'nf618W02RectPow_sound','nf618W02Phase_add','nf618W02Phase_nat','nf618W02Phase_turn','nf618W02Phase_decompose','nf618W02PhaseRect_sound','nf618W02RootTable_sound'}
allowed={'propext','Classical.choice','Quot.sound'}
found={}
log=(p/'candidate-axioms.log').read_text()
for m in re.finditer(r"'(?:WeilDefect\.)?(\w+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",log):
    name=m.group(1)
    if name not in expected: continue
    if name in found: raise SystemExit('Duplicate audit: '+name)
    axioms=[x.strip() for x in (m.group(2) or '').split(',') if x.strip()]
    if not set(axioms)<=allowed: raise SystemExit('Unexpected axioms: '+str((name,axioms)))
    found[name]=axioms
if set(found)!=expected: raise SystemExit('Missing named audits: '+str(sorted(expected-set(found))))
files={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.is_file() and f.name!='runner.log'}
(p/'audit.json').write_text(json.dumps({'scope':'generic root attachment only','source_commit':'5801507d416e4a699c002920b2441f5aa0c19aef','mathlib_commit':'5ed2965256430c3649e86755f9576b54eca72435','theorems':found,'evidence_sha256':files,'new_native_moment_admissions':0,'mathematical_head':'Batch24R1'},indent=2)+'\n')
print('NF618 W02 ROOT ATTACHMENT: 7/7 NAMED AXIOM AUDITS PASS')
PY
echo "Evidence directory: $out (not yet in repository custody)"
