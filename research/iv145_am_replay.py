"""Replay pinned AM source and audit all fixed-cell inequalities.
Usage: python research/iv145_am_replay.py AM.zip output.json
Requires numpy for the deterministic proposal; final checks use Python integers.
This is not a Lean certificate of the original continuum operator.
"""
import hashlib, json, pathlib, sys, zipfile
from fractions import Fraction as F

archive, output = map(pathlib.Path, sys.argv[1:])
expected = "52529ba3c21926ada5bbb1a97cb8175660b94a510c4e57b4d248f042c417aa2d"
assert hashlib.sha256(archive.read_bytes()).hexdigest() == expected
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    source = z.read("am_prime.py")
ns = {"__name__": "__main__"}
exec(compile(source, "pinned-AM/am_prime.py", "exec"), ns)
M, W, h, shifts = (ns[k] for k in ("M", "W", "h", "shifts"))
assert M == 16384 and W == 10**9 and len(shifts) == 48
assert len(h) == M and min(h) == 39499328 and max(h) == 100000000
assert all(isinstance(x, int) for x in h)
def v(i):
    return h[i] if 0 <= i < M else 0
rows = [sum(u * max(v(i+j), v(i+j+1)) for j,u in shifts) for i in range(M)]
slacks = [399*W*y-50*x for x,y in zip(rows,h)]
assert min(slacks) == 696395853981550
assert all(1000000*x < 7979648*W*y for x,y in zip(rows,h))
ratios = [F(x,W*y) for x,y in zip(rows,h)]
q = max(ratios)
assert q == F(31581430071841747,3957747500000000)
assert ratios.index(q) == 6572
raw = json.dumps({"M":M,"W":W,"shifts":shifts,"h":h},separators=(",",":")).encode()
digest = hashlib.sha256(raw).hexdigest()
assert digest == "2b149c79f469b594ce7c308e44c278da00e9e41fbd9da1436cad0b0dca9d294a"
with output.open("xb") as f:
    f.write(raw)
print(json.dumps({"cells":M,"shifts":len(shifts),"min_h":min(h),
    "max_h":max(h),"min_integer_slack":min(slacks),"worst_cell_zero_based":6572,
    "max_ratio_exact":str(q),"strict_upper":"7979648/1000000",
    "data_sha256":digest},indent=2))
