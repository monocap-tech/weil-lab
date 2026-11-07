#!/usr/bin/env python3
"""NF464: exact-rational, original-source J7 rearrangement necessity.

Replays inherited NF463/462 source and seam custody. Proves that IF the
original NF404 sufficient scalar cap holds, the negative density of the
genuine J7 D=4*p*z+2*z*z must occupy >16/625 of J7. Also validates
seven genuine macroscopic panel endpoint/pole-clearance gates.

This does NOT integrate the unknown original z over any macroscopic panel.
"""
import json
import runpy
import sys
from fractions import Fraction as Q
from pathlib import Path

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[2]
parent = runpy.run_path(str(ROOT / "scripts/local_replay/verify_nf463_original_j7_island_and_spatial_necessity.py"))

S = "0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
G = "c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
assert parent["S"] == S and parent["G"] == G
B = Q(11, 10)
A = -parent["j7necessary"]
assert A > Q("2.03475e-22")
assert parent["vlow"] < parent["vhigh"] < 0
assert 0 < -parent["vlow"] < Q(117, 10**13)
assert 0 < parent["c7lo"] < parent["c7hi"] < Q(793, 250)

log8lo, log8hi = parent["log8lo"], parent["log8hi"]
log9lo, log9hi = parent["log9lo"], parent["log9hi"]
a_lo, a_hi = log8lo - B, log8hi - B
b_lo, b_hi = log9lo - B, log9hi - B
assert a_lo < a_hi < b_lo < b_hi < B
assert b_hi - a_lo < Q(59, 500)  # genuine J7 width <0.118
dmin_lower = 2*B - log9hi
d0 = Q(27, 10000)
assert dmin_lower > d0  # actual original n9 seam; NOT a model endpoint

# Independent exact-rational log enclosure, 32 artanh terms and a
# positive, rigorously bounded geometric tail; normalize to [1,2).
N = 32
def unit_log(y):
    assert Q(1) <= y <= Q(2)
    r = (y-Q(1))/(y+Q(1))
    partial = 2*sum((r**(2*j+1)/Q(2*j+1) for j in range(N)), Q(0))
    rem = 2*r**(2*N+1)/(Q(2*N+1)*(1-r*r))
    assert rem >= 0
    return partial, partial + rem
log2lo, log2hi = unit_log(Q(2))

def log_bounds(x):
    assert x >= 1
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    lo, hi = unit_log(x)
    return lo+k*log2lo, hi+k*log2hi

Cmax = Q(793, 250)
vmax = Q(117, 10**13)
m0 = Q(16, 625)   # 0.0256; 21.6%+ of true original J7
def primitive(d, upper):
    loglo, loghi = log_bounds(B/d)
    q = Cmax + (loghi if upper else loglo)/2
    return d*(q*q + q + Q(1, 2))

# For d_min >= d0, monotonicity gives
# int_[b-m0,b] p(x)^2 dx < vmax^2 int_[d0,d0+m0] q(d)^2 dd.
# The exact primitive is d*[q(d)^2+q(d)+1/2].
tail_energy_upper = vmax*vmax*(primitive(d0+m0, True)-primitive(d0, False))
assert tail_energy_upper > 0
assert 2*tail_energy_upper < Q("2.03354e-22")
assert Q("2.03354e-22") < Q("2.03475e-22") < A
# For an increasing p^2, every measurable N of measure <=m0 has
# int_N p^2 <= int_[b-m0,b] p^2. Since D>=-2p^2 and D>=0
# off its strict negative set, D7<=-A forces meas(N)>m0.
assert m0 > Q(27, 125) * Q(59, 500)  # >21.6% of J7
assert m0 > parent["min_negative_measure"]

# Macroscopic, source-seam-typed panels for the NEXT original-z
# quadrature. This tests only real coverage and a 3/2 Bernstein-ellipse
# clearance from the x=B logarithmic singularity, not full source
# analyticity or any z approximation tail.
interior = [Q(1), Q(26,25), Q(53,50), Q(27,25),
            Q(109,100), Q(219,200)]
assert a_hi < interior[0] and all(x<y for x,y in zip(interior,interior[1:]))
assert interior[-1] < b_lo
cuts = [(a_lo,a_hi)] + [(x,x) for x in interior] + [(b_lo,b_hi)]
panel_outer = []
for i in range(len(cuts)-1):
    lo = cuts[i][0]
    hi = cuts[i+1][1]
    assert lo < hi
    # For ellipse rho=3/2, real rightmost = hi+(hi-lo)/24.
    assert B - hi > (hi-lo)/24
    panel_outer.append([str(lo), str(hi)])

out = {
    "pass": "NF464",
    "standing": "SOURCE-REPLAYED, exact-rational CONDITIONAL J7 macroscopic necessary coverage; original signed whole J7 still OPEN",
    "inherited_original_nf407_sha256": S,
    "inherited_original_nf406_sha256": G,
    "genuine_J7": "(log(8)-B, log(9)-B)",
    "nf404_cap_assumption": "CONDITIONAL",
    "original_full_J7_signed_D7": "OPEN",
    "original_whole_J8_signed_D8": "OPEN",
    "if_NF404_original_J7_negative_density_measure_strict_gt": str(m0),
    "if_NF404_original_J7_negative_density_fraction_strict_gt": "21.6%",
    "actual_monotone_original_J7_principal_end_tail_integral_double_strict_lt": "2.03354e-22",
    "necessary_full_original_J7_negative_deficit_strict_gt": "2.03475e-22",
    "number_of_real_J7_partition_panels": len(panel_outer),
    "rho_3_over_2_B_pole_clearance_only": True,
    "full_source_analytic_panel_tail_certified": False,
    "actual_macroscopic_J7_z_integrated": False,
    "RH": "OPEN",
    "next": "NF465 original-source correlated signed J7 integrals on the seven panels, with NF433 prime branches and NF446 compact-source kernel; stop repeating principal-only coverage improvements"
}
print(json.dumps(out, indent=2))
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.output:
        dest = Path(args.output)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(out, indent=2)+"\n")
