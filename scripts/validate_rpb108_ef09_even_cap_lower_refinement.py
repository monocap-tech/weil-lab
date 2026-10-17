#!/usr/bin/env python3
"""EF09: original EVEN EF06-cap same-vector physically supported refinement.

This test ONLY refines the integral lower bound for the existing full
nonnegative conservative CAP, not the original negative multiplier.
It retains the EF06 256 refined low leaf weights, the EF07 121 [1,4]
original weights and the 788 original high leaves (nonnegative, lower 0).
It subdivides [0,1] fourfold and [1,4] sixteenfold; every new lower
uses a Lipschitz enclosure of the ACTUAL supported cosine Fourier
transform throughout the entire subcell.

A strict cap lower > the previously certified exact EF08 original
positive-energy upper (877811/10^6) is only a NO-GO for the
conservative EF06 cap. The actual negative form may be smaller.
No inference of original even negativity or RH is permitted.
"""
from fractions import Fraction as F

from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_ef06_local_even_signed_cap import improve_original_leaf
from validate_rpb108_ef07_global_even_witness import physical_fourier_bounds

EF08_CERTIFIED_AE_UPPER = F(877811, 1000000)
OLD_EF07_CAP_LOWER = F(8023309563, 10**10)
OLD_EF07_MID_LOWER = F(676556251, 10**10)
OLD_EF07_LOW_LOWER = F(7346753311, 10**10)
LOW_SPLITS = 4
MID_SPLITS = 16


def refined_original_cap_lower():
    clusters, width, mass, old_mass = full_upper_leaves()
    assert len(clusters) == 107
    assert old_mass == F(1204033883, 32000000)
    whole_low = F(0)
    whole_mid = F(0)
    positive_mass = F(0)
    old_leaves = low_cells = mid_cells = far_cells = 0
    new_subcells = 0
    for cluster in clusters:
        for l, r, h in cluster:
            old_leaves += 1
            original_cap = h + KAPPA
            assert original_cap >= 0 and 0 <= l < r
            if r <= 1:
                refined = improve_original_leaf(l, r, h)
            else:
                refined = [(l, r, original_cap)]
            for a, b, weight in refined:
                assert weight >= 0 and l <= a < b <= r
                positive_mass += 2 * (b - a) * weight
                if a >= 4:
                    # The omitted far CAP quadratic is nonnegative.
                    # Thus zero is a rigorous lower bound, not a lost term.
                    far_cells += 1
                    continue
                assert b <= 4, "Missing crossing leaf"
                subdivisions = LOW_SPLITS if b <= 1 else MID_SPLITS
                width_sub = (b - a) / subdivisions
                for j in range(subdivisions):
                    u = a + width_sub * j
                    v = u + width_sub
                    # True physical supported transform, rigorous entire cell.
                    amp_lower, amp_upper = physical_fourier_bounds(u, v)
                    assert 0 <= amp_lower <= amp_upper
                    integral_lower = 2 * weight * (v - u) * amp_lower**2
                    assert integral_lower >= 0
                    if b <= 1:
                        whole_low += integral_lower
                    else:
                        whole_mid += integral_lower
                    new_subcells += 1
                if b <= 1:
                    low_cells += 1
                else:
                    mid_cells += 1
    assert old_leaves == 973 and low_cells == 256
    assert mid_cells == 121 and far_cells == 788
    assert new_subcells == 256 * LOW_SPLITS + 121 * MID_SPLITS
    assert abs(positive_mass - F(2960374846875, 10**11)) < F(1, 10**7)
    assert whole_low >= OLD_EF07_LOW_LOWER
    assert whole_mid >= OLD_EF07_MID_LOWER
    return whole_low, whole_mid, whole_low + whole_mid, new_subcells


def validate():
    lo, mid, total, n = refined_original_cap_lower()
    assert total > OLD_EF07_CAP_LOWER
    # The A_e upper is the separately established EF08 exact-rational
    # whole-original signed-positive certificate; we do not reconstruct
    # or silently re-prove it here. Pin that hypothesis explicitly.
    margin = total - EF08_CERTIFIED_AE_UPPER
    status = "CAP_METHOD_NO_GO" if margin > 0 else "STILL_INCONCLUSIVE"
    print("EF09 physical signed cap lower [0,1]:", float(lo), flush=True)
    print("EF09 physical signed cap lower [1,4]:", float(mid), flush=True)
    print("EF09 complete original conservative cap LOWER:", float(total),
          "validated physical subcells", n, flush=True)
    print("EF09 old EF07 complete cap lower >",
          float(OLD_EF07_CAP_LOWER), flush=True)
    print("EF09 independent EF08 actual original A_e UPPER <",
          float(EF08_CERTIFIED_AE_UPPER), flush=True)
    print("EF09 certified conservative cap-minus-A_e LOWER >",
          float(margin), flush=True)
    print("EF09 same-vector classification:", status, flush=True)
    if margin > 0:
        print("EF09: EF06/EF07 refined conservative CAP not Loewner",
              "dominated by actual A_e; original TRUE negative form",
              "K_true <= K_cap may still be dominated. NO original",
              "even negativity, full Weil or RH conclusion.",flush=True)
    else:
        print("EF09: interval gap still overlaps. Neither cap",
              "feasibility nor cap no-go is proved. Continue targeted",
              "tightening or pivot to true signed operator.", flush=True)
    print("EF09 PASS: original supported cap-method diagnostic only;",
          "W-EVEN-FORM, W-WHOLE-FORM, global bridge and RH OPEN.",
          flush=True)


if __name__ == "__main__":
    validate()
