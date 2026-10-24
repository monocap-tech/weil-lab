#!/usr/bin/env python3
"""SM34 sharpened ORIGINAL full-infinite odd Schur threshold.

No new source dimensionality, no sampled Fourier frequency data.
On F=E0^perp, original odd pole vanishes because s belongs to E0.
Original Ao >= kappa I and Knegative|F <= epsilon I imply the
strict stronger signed complement floor mu_new=kappa-epsilon.
Thus relative correction epsilon/mu_new, and the full-infinite
sufficient dual-source threshold is mu_new/(mu_new+epsilon)
=1-epsilon/kappa, better than old 51/56.

Use the simultaneously valid SI10 negative original height h_old
and the SM40 refined complete original signed-negative step w40
pointwise (min) on EACH of the full 3,892 rational subcells.
This can lower the same 107 b9 cluster-specific epsilon without
changing a single original 470 source or dropping any frequency.
All arithmetic is Fraction. Independent original Hilbert-space /
Fourier form and domain review remains necessary. W-ODD-NEG OPEN.
"""
import json
from fractions import Fraction as F
from validate_rpb108_si10_complement_positivity import KAPPA,B
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm33_original_odd_negative_mixed_bound import (
    full_original_clusterwise_negative_mixed
)
from validate_rpb108_sm40_endpoint_curvature_negative_cap import (
    refined_original_endpoint_curvature
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm32_parity_cofinite_odd_schur import BITS,MU
from validate_rpb108_sm34_positive_energy_dual_schur import CLEAN_THRESHOLD
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def new_threshold():
    old=full_original_clusterwise_negative_mixed()
    old_leaves,W,mass_old,total_old=full_upper_leaves()
    prev39,new40,orders,stats=refined_original_endpoint_curvature()
    assert len(old_leaves)==len(new40)==len(prev39)==107
    assert old["source_count"]==470 and sum(orders)==890
    assert old["leaves"]==973
    assert old['legacy_h_only_mass']==mass_old
    assert old['mass']==mass_old+KAPPA*W
    assert old['neg_global_norm']==2*B*(mass_old+KAPPA*W)
    assert stats["all_original_signed_subcells"]==3892
    assert stats["original_exact_SPD_pivots"]==890
    assert KAPPA==F(1,1000) and B==F(11,10)
    assert BITS==9 and MU==F(17,25000)
    assert CLEAN_THRESHOLD==F(51,56)
    mass_eff=F(0)
    weighted_eff=F(0)
    num=0
    count_sources=1
    strict_weight=0
    strictly_refined_clusters=0
    cap_order_strictly_greater_than_b9=0
    for parent,new,cap_order_24 in zip(old_leaves,new40,orders):
        # SM40 is exactly a FOUR-WAY refinement of each one of the
        # 973 original SM10 physical negative-frequency leaves.
        assert len(new)==4*len(parent)
        start,end=parent[0][0],parent[-1][1]
        assert new[0][0]==start and new[-1][1]==end
        p,e=taylor_order(end-start,BITS)
        # CRITICAL: the same cluster supports TWO DISTINCT truncations:
        # b9: 469 exceptional generators (+pole=470) and error e_j;
        # b24: 890 negative-cap source columns and moment covariance.
        assert p<=cap_order_24 and F(0)<e<F(1,2**BITS)
        assert cap_order_24==taylor_order(end-start,24)[0]
        cap_order_strictly_greater_than_b9+=int(cap_order_24>p)
        count_sources+=p
        local_mass=F(0)
        old_local=F(0)
        for i,(l,r,h) in enumerate(new):
            pa,pb,old_h=parent[i//4]
            assert pa<=l<r<=pb
            assert h+KAPPA>0 and old_h>=0
            if i%4==0: assert l==pa
            if i%4==3: assert r==pb
            old_local+=2*(r-l)*old_h
            # BOTH terms are independent complete original real
            # multiplier NEGATIVE uppers. Their pointwise minimum
            # is a valid true bound and no 24-bit Taylor cap eta
            # belongs in this direct complement restriction.
            effective=min(old_h+KAPPA,h+KAPPA)
            assert effective>=0
            assert effective<=old_h+KAPPA and effective<=h+KAPPA
            strict_weight+=int(effective<old_h+KAPPA)
            local_mass+=2*(r-l)*effective
            num+=1
        assert local_mass<=old_local+2*KAPPA*(end-start)
        strictly_refined_clusters+=int(local_mass<old_local+2*KAPPA*(end-start))
        mass_eff+=local_mass
        weighted_eff+=local_mass*e*e
    assert count_sources==470 and sum(orders)==890 and num==3892
    assert cap_order_strictly_greater_than_b9>0
    assert strict_weight>0 and strictly_refined_clusters>0
    assert mass_eff<=mass_old+KAPPA*W
    eps_eff=2*B*weighted_eff
    old_missing_kappa_upper=2*B*KAPPA*W*F(1,2**(2*BITS))
    assert old['legacy_h_only_leakage_UNDERPAID']<F(66247,10**9)
    assert old['legacy_h_only_leakage_UNDERPAID']+old_missing_kappa_upper<F(1,15000)
    assert F(0)<eps_eff<=old['leak']<F(1,15000)
    mu_eff=KAPPA-eps_eff
    assert mu_eff>F(0) and mu_eff>MU
    threshold=mu_eff/(mu_eff+eps_eff)
    assert threshold==F(1)-eps_eff/KAPPA
    assert threshold>F(14,15)>CLEAN_THRESHOLD
    # Independently sharpen the global Knegative operator norm
    # using the SAME all-frequency true effective step envelope.
    H_eff=2*B*mass_eff
    assert H_eff<=old["neg_global_norm"]
    result={
       "status":"CONDITIONAL_EXACT_ORIGINAL_470D_COMPLEMENT_SCHUR_THRESHOLD",
       "canonical_W_ODD_NEG":"OPEN",
       "original_source_dim":470,
       "original_negative_clusters":107,
       "original_signed_real_subcells":num,
       "original_SM40_cap_columns":890,
       "b9_and_b24_orders_differ_in_clusters":cap_order_strictly_greater_than_b9,
       "new_pointwise_effective_negative_mass":str(mass_eff),
       "old_SM33_negative_mass":str(mass_old),
       "refined_real_subcells_strict_smaller":strict_weight,
       "clusters_strictly_improved":strictly_refined_clusters,
       "old_SM33_epsilon_UNDERPAID_kappa":str(old['legacy_h_only_leakage_UNDERPAID']),
       "old_SM33_epsilon_REPAIRED_kappa":str(old["leak"]),
       "old_SM33_missing_kappa_leakage_exact_upper":str(old_missing_kappa_upper),
       "old_SM33_missing_kappa_global_norm_upper":str(2*B*KAPPA*W),
       "old_SM33_Knegative_norm_has_been_repaired":True,
       "new_all470_complement_epsilon":str(eps_eff),
       "certified_fully_paid_old_SI10_epsilon_upper":str(old["leak"]),
       "old_SM34_mu_floor":str(MU),
       "new_positive_signed_complement_mu":str(mu_eff),
       "old_SM34_threshold":str(CLEAN_THRESHOLD),
       "new_sharp_sufficient_source_threshold":str(threshold),
       "new_threshold_decimal_display":float(threshold),
       "guaranteed_exceeds_14_over_15":True,
       "new_original_whole_Knegative_norm_upper":str(H_eff),
       "old_original_whole_Knegative_norm_repaired_kappa":str(old["neg_global_norm"]),
       "full470_G_N_evaluated":False,
       "entire_odd_even_Weil_CC27_RH":"OPEN",
       "independent_form_domain_identification_audit":"OPEN"
    }
    return result

def main():
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(z for z in m["obligations"] if z["id"]=="W-ODD-NEG")
    assert odd["status"]==m["objective"]["status"]=="open"
    assert m["active_obligation"]=="W-ODD-NEG"
    r=new_threshold()
    print("Original full 470d old->new sufficient theta:",
          r["old_SM34_threshold"],"->",
          r["new_sharp_sufficient_source_threshold"],
          "(decimal)",r["new_threshold_decimal_display"],flush=True)
    print("Original complete negative cap mass and complement leakage:",
          r["new_pointwise_effective_negative_mass"],
          r["new_all470_complement_epsilon"],flush=True)
    print(json.dumps(r,indent=2))
    print("PASS scoped threshold theorem; original signed W-ODD-NEG OPEN",flush=True)

if __name__=="__main__":
    main()
