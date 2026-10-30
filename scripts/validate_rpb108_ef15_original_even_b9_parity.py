#!/usr/bin/env python3
"""EF15: source-pinned exact-rational b=9 EVEN parity/cofinite entry.

Rebuild the original SI10 signed seven-prime protected cover and Taylor
orders, independently of SM32's odd-specific validator and its active
obligation. Transfer the parity projection *mathematically*, not the
odd-pole statement. The actual original even pole is nonnegative.

This checks exact arithmetic and source counts; it is not independent
analytic/form-domain review or a computed finite Schur sign.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from validate_rpb108_si10_complement_positivity import (
    KAPPA, B, protected_inner_cover, protected_outer_band,
)
from validate_rpb108_si08_multiband_rank import taylor_order

ROOT = Path(__file__).resolve().parents[1]
MU9 = F(17, 25000)
GAMMA24_GATE = F(999, 10**6)
BITS9 = 9
BITS24 = 24


def source_replay():
    outer, outer_lower = protected_outer_band()
    clusters, reflected_width, cap_mass, n_leaves, n_protected = (
        protected_inner_cover()
    )
    assert outer == 2535 and outer_lower > KAPPA
    assert n_leaves == 973 and n_protected == 9261
    assert len(clusters) == 107
    assert reflected_width == F(973, 32)
    assert F(0) < cap_mass < F(38)
    assert (KAPPA, B) == (F(1,1000), F(11,10))

    # Strictly positive disjoint centers. These are the exact original
    # SI10 whole-frequency clusters, not chosen new trial frequencies.
    centers = [(left + right)/2 for left,right,_ in clusters]
    assert len(set(centers)) == 107
    assert all(c > 0 for c in centers)
    assert all(clusters[j][1] < clusters[j+1][0]
               for j in range(len(clusters)-1))

    orders9 = [taylor_order(right-left, BITS9)[0]
               for left,right,_ in clusters]
    orders24 = [taylor_order(right-left, BITS24)[0]
                for left,right,_ in clusters]
    assert all(a >= 1 and b >= a for a,b in zip(orders9, orders24))
    assert sum(orders9) == 469
    assert sum(orders24) == 890

    # For even f, the original +/- Taylor pair has only ONE
    # nontrivial even projection for each k:
    #    u_jk=1_I (2*pi*x)^k/k! cos(2*pi*c_j*x+k*pi/2).
    # For k even: even polynomial*cos; for k odd: odd polynomial*sin.
    # The opposite-parity projection is exactly orthogonal to even f.
    even_k = sum((p+1)//2 for p in orders9)
    odd_k = sum(p//2 for p in orders9)
    assert (even_k, odd_k) == (260, 209)
    assert even_k + odd_k == 469
    # Odd SM32 has one *negative odd pole* as extra exceptional column.
    # The EVEN pole is +2|<f,cosh(x/2)>|^2 and costs no source column.
    assert 2*sum(orders9)+1 == 939

    total_mass = cap_mass + KAPPA*reflected_width
    # Freeze the exact original SI10/SM10 source-cover fingerprint.
    assert total_mass == F(1204033883, 32000000)
    gamma9 = KAPPA - 2*B*total_mass*F(1, 2**(2*BITS9))
    gamma24 = KAPPA - 2*B*total_mass*F(1, 2**(2*BITS24))
    assert gamma9 == F(28698667287, 41943040000000)
    assert gamma9 > MU9 and gamma24 > GAMMA24_GATE
    assert gamma24 > gamma9
    # SI10 signed original even form q_e on the even physical carrier:
    # q_e(f,f) >= gamma9||f||^2 whenever f is orthogonal to
    # ALL these 469 even original generators, under inherited
    # original Fourier/form domain. This does not classify the
    # finite exceptional block or the whole q_e.
    return {
        "clusters": len(clusters), "leaves": n_leaves,
        "protected": n_protected, "outer": outer,
        "even_b9": sum(orders9), "even_b24": sum(orders24),
        "even_k": even_k, "odd_k": odd_k,
        "gamma9": gamma9, "gamma24": gamma24,
        "width": reflected_width, "mass": cap_mass,
    }


def schur_sign_regression():
    # Countermodel to the invalid inference:
    # A>0 and infinite complement D>=mu do NOT imply full form PSD.
    d = MU9
    a = F(1, 100)
    good = F(1, 500)
    bad = F(1, 100)
    assert a > 0 and d > 0
    assert a - good**2/d > 0
    assert a - bad**2/d < 0
    return a - good**2/d, a - bad**2/d


def validate():
    data = json.loads((ROOT/"research/obligations.json").read_text())
    ob = {o["id"]: o for o in data["obligations"]}
    assert data["active_obligation"] == "W-EVEN-FORM"
    assert data["objective"]["status"] == "open"
    assert data["governance"]["no_automatic_promotion"] is True
    assert ob["W-EVEN-FORM"]["status"] == "open"
    assert ob["W-ODD-NEG"]["status"] == "open"
    assert ob["W-WHOLE-FORM"]["status"] == "open"
    assert "EF14" in ob["W-EVEN-FORM"]["evidence"]
    r = source_replay()
    pos, neg = schur_sign_regression()
    print("EF15 source-pinned original SI10 cover: "
          f"{r['clusters']} clusters, {r['leaves']} unresolved leaves, "
          f"{r['protected']} protected cells", flush=True)
    print("EF15 original even b=24 dimension:", r["even_b24"],
          "reduced original even b=9 dimension:", r["even_b9"],
          "parity polynomial counts:", r["even_k"], r["odd_k"], flush=True)
    print("EF15 exact original even signed cofinite floor b=9 >17/25000:",
          float(r["gamma9"]), flush=True)
    print("EF15 original b=24 cofinite floor:", float(r["gamma24"]),
          flush=True)
    print("EF15 exact sign-sensitive Schur countermodel:",
          float(pos), float(neg), flush=True)
    print("EF15 SCOPED PASS: original signed even cofinite positive "
          "on b9 469-generator complement under inherited SI10 analytic "
          "premises; even low-spectrum index <=469. Actual finite "
          "signed block, complete mixed inverse, form-domain attachment, "
          "whole even/odd Weil and RH OPEN.", flush=True)


if __name__ == "__main__":
    validate()
