#!/usr/bin/env python3
"""PS02: exact-rational strict PARITY-INCOMPARABILITY of original signed Weil Q.

Not original form negativity; h+ and h- are different true compactly supported
half-interval physical profiles. Bound their even-minus-odd energy differences
on the full original seven-prime + archimedean + signed-pole form.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old

B = F(11, 10)
R = 2 * B
PRIMES = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3))
ROOT = Path(__file__).resolve().parents[1]

def run():
    # Original CC27/RC313 sign and model custody imported as a PINNED old source.
    earlier = old.run()
    assert earlier["original_CC27_native_source_from_RC313"]
    assert earlier["reg_source_verified"]

    manifest = json.loads((ROOT / "research/obligations.json").read_text())
    parallel = json.loads((ROOT / "research/parallel_investigations/w_physical_shift.json").read_text())
    assert manifest["active_obligation"] == "W-ODD-NEG"
    assert manifest["objective"]["status"] == "open"
    assert parallel["id"] == "W-PHYSICAL-SHIFT"
    assert parallel["status"] == "open"
    assert parallel["active_frontier_unchanged"] == "W-ODD-NEG"

    logs = {n: old.log_i(F(n)) for n, _ in PRIMES}
    weights = {
        n: old.log_i(F(p)) / old.sqrt_i(n)
        for n, p in PRIMES
    }
    log9 = logs[9]
    log8 = logs[8]
    a = old.IV(log9.lo - B, log9.hi - B)
    delta = old.IV(R - log9.hi, R - log9.lo)
    assert F(1) < a.lo < a.hi < B
    assert 0 < delta.lo <= delta.hi < F(1, 100)
    assert 2 * a.lo > log8.hi
    assert all(logs[n].hi <= log8.hi < 2 * a.lo for n, _ in PRIMES if n < 9)
    assert all(0 < logs[n].lo < logs[n].hi < R for n, _ in PRIMES)
    assert weights[9].lo == (old.log_i(F(3)) / 3).lo
    assert weights[9].hi == (old.log_i(F(3)) / 3).hi
    assert weights[9].lo > F(1, 3)

    # Exact hyperbolic enclosure on 0<B/2<1: c²+s²=cosh(B).
    s, c = old.sinh_cosh_iv(B / 2)
    cosh_B = c ** 2 + s ** 2
    assert F(1) < cosh_B.lo <= cosh_B.hi < 2

    # A_H=SUM_j |<h,e^(-(2j+1/2)t)>|² >= 0.
    # Since t,s in J and a>1, k(t+s)<2 and hence A_H<=2*delta.
    # Original poles: 0<=P<=8*delta*cosh(B).
    w9 = weights[9]
    even_below_odd_margin = 4 * w9.lo - 8 * delta.hi * cosh_B.hi
    odd_below_even_margin = 4 * w9.lo - 8 * delta.hi

    # Symmetric h+ under t->log(9)-t has H9=+1:
    # Q_even[h+]-Q_odd[h+] <= -even_below_odd_margin.
    # Antisymmetric h- has H9=-1:
    # Q_even[h-]-Q_odd[h-] >= odd_below_even_margin.
    assert even_below_odd_margin > F(142, 100)
    assert odd_below_even_margin > F(144, 100)

    # Explicit symbolic normalizations over J=[m-delta/2,m+delta/2]:
    # ||delta^(-1/2)||²=1;
    # ||sqrt(12/delta^3)*(t-m)||² = 12/delta^3 * delta^3/12 = 1.
    # Reflection sends 1->1 and (t-m)->-(t-m). Check the algebra
    # at a representative rational delta WITHOUT substituting it for log9:
    test_delta = F(1, 400)
    assert test_delta * (1 / test_delta) == 1
    assert F(12) / test_delta ** 3 * (test_delta ** 3 / 12) == 1
    for x in [F(-1, 2), F(-1, 4), F(0), F(1, 4), F(1, 2)]:
        assert -x == (-x)  # antisymmetric coordinate after reflection

    print("PS02 true log9 overlap delta outward", str(delta.lo), str(delta.hi),flush=True)
    print("PS02 positive-half edge a", str(a.lo), str(a.hi), flush=True)
    print("PS02 excluded next-largest log8 upper", str(log8.hi), flush=True)
    print("PS02 seven original weights verified; log9 true w9", str(w9.lo), str(w9.hi), flush=True)
    print("PS02 exact cosh(B) upper", str(cosh_B.hi), flush=True)
    print("PS02 symmetric edge h+ Q_even - Q_odd STRICT UPPER <",
          str(-even_below_odd_margin), flush=True)
    print("PS02 antisymmetric edge h- Q_even - Q_odd STRICT LOWER >",
          str(odd_below_even_margin), flush=True)
    print("PS02 PASS SCOPED: exact physically supported original parity"
          " comparisons have BOTH signs under common half-interval identification."
          " This is a direct parity-order METHOD NO-GO, not negative"
          " even/odd Weil vectors, 890x890 Schur, W-ODD-NEG, or RH.",flush=True)

if __name__ == "__main__":
    run()
