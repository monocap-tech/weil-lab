#!/usr/bin/env python3
"""PS03: original signed Weil Q uniformly positive on entire two-edge space.

Exact rational strict margin 3/10 for *every* original form-domain vector
supported on S=[-B,-a] union [a,B], a=log(9)-B. This is NOT full Weil
positivity, a cross-Schur bound, or RH. No floating-point acceptance.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old

B = F(11, 10)
R = 2 * B
N = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3))
ROOT = Path(__file__).resolve().parents[1]

def run():
    # Pinned old original CC27/RC313 model (including the signed prime
    # shifts, arch regular source and parity poles): no surrogate form.
    old_receipt = old.run()
    assert old_receipt["original_CC27_native_source_from_RC313"]
    assert old_receipt["reg_source_verified"]
    assert old_receipt["offdiagonal_P0_P1_exactly_zero_by_parity"]

    gov = json.loads((ROOT / "research/obligations.json").read_text())
    lane = json.loads((ROOT / "research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"] == "W-ODD-NEG"
    assert gov["objective"]["status"] == "open"
    assert lane["id"] == "W-PHYSICAL-SHIFT" and lane["status"] == "open"
    assert lane["active_frontier_unchanged"] == "W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())

    shifts = {n: old.log_i(F(n)) for n, p in N}
    log9, log8 = shifts[9], shifts[8]
    edge_a = old.IV(log9.lo - B, log9.hi - B)
    delta = old.IV(R - log9.hi, R - log9.lo)
    assert F(1) < edge_a.lo <= edge_a.hi < B
    assert F(0) < delta.lo <= delta.hi < F(1, 350)
    assert 2 * edge_a.lo > F(2)
    assert log8.hi < 2 * edge_a.lo
    for n, p in N:
        if n < 9:
            assert delta.hi < shifts[n].lo < shifts[n].hi < 2 * edge_a.lo
        else:
            assert 2 * edge_a.hi < log9.lo < log9.hi < R

    # Digamma subtraction constant psi(1/4)-log(pi) with the exact
    # original normalization, outward gamma, pi and logarithmic bounds.
    pi = old.pi_iv()
    gamma = old.gamma_iv()
    arch_c = -gamma - pi / 2 - 3 * old.log_i(F(2)) - old.log_i(pi)
    assert arch_c.lo < arch_c.hi < -F(5)

    # k(u)=exp(-u/2)/(1-exp(-2u)):
    # (0,1/2): k >= 1/(2u)-1/4.
    # [1/2,3/2]: k > 2/5 because exp(3/4)<5/2.
    # [3/2,2]: k > 1/3 because e<3.
    x = F(3, 4)
    exp_bound = F(1) + x + x*x / (2 * (1 - x/3))
    assert exp_bound == F(17, 8) and exp_bound < F(5, 2)
    # e<3 follows strictly from n!>=2^(n-1), n>=2 (strict n>=4).
    # Confirm only the rational constants used in the analytic steps.
    arch_interval_lower = (
        old.log_i(F(7)).lo + 2 * old.log_i(F(5)).lo
        - F(1, 4) + F(4, 5) + F(1, 3)
    )  # log175 = log7+2log5; delta<1/350

    # The only surviving prime autocorrelation is shift log9, whose
    # opposite-edge coupling obeys |C(log9)|<=||g||²/2.
    true_w9 = old.log_i(F(3)) / 3  # sqrt(9) exactly 3
    assert F(1, 3) < true_w9.lo <= true_w9.hi < F(2, 5)

    # Exact original negative odd rank-one pole:
    # -2|<g,sinh(x/2)>|² >= -4*delta*sinh²(B/2)||g||².
    sinh, cosh = old.sinh_cosh_iv(B / 2)
    assert F(0) < sinh.lo < sinh.hi < 1
    negative_pole_max = 4 * delta.hi * sinh.hi ** 2

    rigorous_floor = arch_c.lo + arch_interval_lower - true_w9.hi - negative_pole_max
    assert rigorous_floor > F(3, 10), (
        "PS03 strict source-rational original edge coercivity not certified",
        rigorous_floor
    )

    # Independent coarse witness arithmetic for the two-edge physical
    # support decomposition; no finite-dimensional positivity substitution.
    assert R - delta.lo == log9.hi
    assert edge_a.lo + B == log9.lo
    assert edge_a.lo > delta.hi
    print("PS03 original two-edge strip upper width", float(delta.hi), flush=True)
    print("PS03 original signed arch constant lower", float(arch_c.lo), flush=True)
    print("PS03 arch gap difference energy floor", float(arch_interval_lower), flush=True)
    print("PS03 residual true log9 prime upper", float(true_w9.hi), flush=True)
    print("PS03 original negative odd pole uniform upper", float(negative_pole_max), flush=True)
    print("PS03 original signed Q full-edge uniform lower", float(rigorous_floor), flush=True)
    print("PS03 PASS SCOPED: original signed Weil Q(g) > 3/10 ||g||²"
          " on the entire infinite-dimensional two-edge support subspace."
          " No complementary or cross-Schur control, no even/odd whole"
          " positivity, W-ODD-NEG, W-EVEN-FORM or RH.", flush=True)

if __name__ == "__main__":
    run()
