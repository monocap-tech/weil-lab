#!/usr/bin/env bash
set -euo pipefail
# Run from a clean, authenticated checkout of the existing execution branch.
# No workflow dispatch. A successful invocation commits the original ZIP bytes
# and checks them against the independently authenticated original SHA-256.
branch=formalization/iv106-w02-primitive-pole-audit
test "$(git branch --show-current)" = "$branch"
test -z "$(git status --porcelain)"
git fetch --no-tags origin "$branch"
test "$(git rev-parse HEAD)" = "$(git rev-parse FETCH_HEAD)"
p="verification/iv106/regroup_001/w02_primitive_pole_audit/repair_01/evidence/failed_run_45980919877.zip"
mkdir -p "$(dirname "$p")"
test ! -e "$p"
gh api repos/monocap-tech/weil-lab/actions/artifacts/15190273514/zip > "$p"
test "$(wc -c < "$p")" -eq 84719
printf '%s  %s\n' 936b7e0311b88b96b9a46533380497629025b854e5d8c191d3379c569c434567 "$p" | sha256sum -c -
python3 - "$p" <<'PY'
import sys, zipfile
with zipfile.ZipFile(sys.argv[1]) as z:
    assert len(z.namelist()) == 17 and z.testzip() is None
PY
git add -- "$p"
git commit -m "IV106 W02: preserve original failed native audit ZIP [skip ci]"
git push origin "HEAD:refs/heads/$branch"
git fetch --no-tags origin "$branch"
test "$(git rev-parse HEAD)" = "$(git rev-parse FETCH_HEAD)"
git show "FETCH_HEAD:$p" | sha256sum | grep -Fx '936b7e0311b88b96b9a46533380497629025b854e5d8c191d3379c569c434567  -'
