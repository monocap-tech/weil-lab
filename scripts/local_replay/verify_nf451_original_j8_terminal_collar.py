#!/usr/bin/env python3
"""NF451 exact-rational replay of the original J8 terminal positive collar.

Uses the ACCEPTED NF406 original n=9 seam, NF407 original source,
NF446 compact-kernel inequalities, NF418 dyadic center derivative bound,
and NF450 accepted outward z(B) interval.  No floating-point quadrature,
no source reselection, and no claim on full J7/J8 signs.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

B = Q(11, 10)
DELTA = Q(1, 10**15)
L = Q(400)  # accepted original physical sup |U'| is STRICTLY below L
U_MAX = Q(900)  # original physical sup |U| < U_MAX
V_MAX = Q(1)  # |v|<1 and v<0 from NF445/NF446 accepted
C0_MAX = Q(10)  # |psi(1/4)-log(pi)|<10, NF446
TAIL_MAX = Q(4)  # integral_{b}^inf K<4 for b>=2B
N_PRIMES = 7  # NF406 actual prime powers 2,3,4,5,7,8,9
CENTER_SLOPE_MAX = Q(2)  # NF418 original NF404 dyadic center
EXPECTED_SOURCE_SHA = "0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
EXPECTED_SEAMS_SHA = "c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()

def replay(source_path, seam_path, nf450_path):
    source, source_sha = load(source_path)
    seams, seams_sha = load(seam_path)
    endpoint, _ = load(nf450_path)
    assert source_sha == EXPECTED_SOURCE_SHA
    assert seams_sha == EXPECTED_SEAMS_SHA
    assert endpoint["source_SHA256"] == source_sha
    assert endpoint["seams_SHA256"] == seams_sha
    assert endpoint["complete_z_B_strictly_negative"] is True
    assert endpoint["original_source_selected_plus_critical"] == 246
    assert endpoint["original_physical_source_groups"] == 273
    assert source["original_dimension"] == 242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"]) == 4
    assert seams["original_support_half_width"] == "11/10"
    n9 = next(item for item in seams["original_prime_power_log_shifts"] if item["n"] == 9)
    # True J8 begins at log 9 - B. This terminal collar is wholly inside it.
    assert 2 * B - Q(n9["log_upper"]) > Q(1, 1000) > DELTA

    # For x=B-d, 0<d<=DELTA, a=2d, b=4B-2d.  The NF446 compact
    # kernel comparison gives each term below, all as strict d multiples.
    small_sym = 2 * L               # integral_[0,2d] first symmetric difference
    lost_low = L                   # missing x=B middle interval [0,2d]
    middle_flat = Q(3, 2) * L * 4 * B
    middle_log = Q(3, 2) * L         # multiplies d*log(2B/d)
    lost_high = (V_MAX + U_MAX) * (1 + 1 / (2 * B))
    scalar = V_MAX * (1 / B + 4) / 2
    arch_tail = L * TAIL_MAX + 2 * V_MAX * (1 + 1 / (2 * B))
    c0_term = C0_MAX * L
    primes = N_PRIMES * L
    center = CENTER_SLOPE_MAX
    flat = small_sym + lost_low + middle_flat + lost_high + scalar + arch_tail + c0_term + primes + center
    assert flat < 14000
    assert middle_log == 600
    # Since 2B/d>e, d*log(2B/d) increases on (0,DELTA].
    # e>8/3 from the first four exponential-series terms, so
    # (8/3)^39 > 2B/DELTA proves log(2B/DELTA)<39 exactly.
    assert 2 * B / DELTA > 3
    assert Q(8, 3) ** 39 > 2 * B / DELTA
    modulus = (Q(14000) + Q(600) * 39) * DELTA
    assert modulus == Q(37400) / 10**15

    z_lo, z_hi = (Q(x) for x in endpoint["complete_z_B_outward_24_decimal"])
    assert z_lo < z_hi < 0
    assert z_hi + modulus < -Q(4, 10**10)
    # On this ORIGINAL fixed J8 cell p=q+r<0, since v<0,
    # q=(v/2)*log(B/(B-x)) and r=v*sum_{n in primes} Lambda(n)/sqrt(n).
    # Thus 4pz>0 and 2z^2>2*(4e-10)^2, pointwise on the collar.
    signed_collar_lower = 2 * DELTA * (Q(4, 10**10) ** 2)
    assert signed_collar_lower == Q(32, 10**35)
    return {
        "pass": "NF451",
        "classification": "ANALYTIC TERMINAL-COLLAR LEMMA; fraction source-check only, not J7/J8 integral certification",
        "original_source_SHA256": source_sha,
        "original_seams_SHA256": seams_sha,
        "original_nf450_custody_branch": endpoint["branch"],
        "original_n9_cell_strictly_contains_collar": True,
        "delta": str(DELTA),
        "all_source_and_prime_shifts_unchanged": True,
        "flat_modulus_coefficient_strict_upper": "14000",
        "log_modulus_coefficient": "600",
        "log_at_delta_strict_upper": "39",
        "uniform_z_difference_strict_upper": str(modulus),
        "nf450_original_zB_outward_upper": str(z_hi),
        "collar_original_z_strict_upper": str(-Q(4, 10**10)),
        "collar_original_p_negative": True,
        "collar_original_D8_strict_lower": str(signed_collar_lower),
        "full_original_J7_J8_signed_integrals": "OPEN",
        "original_global_NF410_NF404_scalar": "OPEN",
        "W_ODD_NEG": "OPEN",
        "RH": "OPEN",
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams", default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--nf450", default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--output", default=None)
    args = ap.parse_args()
    result = replay(args.source, args.seams, args.nf450)
    if args.output:
        dest = Path(args.output)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
