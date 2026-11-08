#!/usr/bin/env python3
"""NF481: unconditional genuine original J8 high-image energy ERROR certificate.

Reuses native 4096-bit 273-mode full-source 360-jet resolvent from NF481,
accepted original NF446 full compact |z|<25000, true seven-prime J8 support
and NF404 principal, original NF480 source logarithm cancellation.

We prove an ACTUAL norm bound for w=(p+z) on BOTH J8 sides from original
physical compact-source and analytic log-square integration. Consequently
the finite-18000 plus full-source first-k analytic-jet comparator's
ENERGY error is no longer conditional on an unproved ||g||<=4e-11.

No direct J8 D8 value, upper, or NF404 cap is certified here.
"""
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal,localcontext
import argparse,json,hashlib,math,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/"notes/data/provisional"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
M=18000;N=360
def iv(a):
    x,y=map(F,a);assert x<=y
    return x,y
def abslower(a):
    x,y=iv(a)
    return min(abs(x),abs(y)) if x>0 or y<0 else F(0)
def absupper(a):
    x,y=iv(a)
    return max(abs(x),abs(y))
def load(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def dec(x,digits=46):
    with localcontext() as c:
        c.prec=digits
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def log9_rational(K=100):
    t=F(4,5)
    lower=sum((2*t**(2*j+1)/F(2*j+1) for j in range(K)),F(0))
    upper=lower+2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
    return lower,upper
def exp6_lower():
    return sum((F(6**j,math.factorial(j)) for j in range(9)),F(0))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    d,h=load(args.native)
    n446,_=load(DATA/"NF446_original_joint_compact_kernel_J7_J8_custody_index.json")
    n450,_=load(DATA/"NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    n451,_=load(DATA/"NF451_original_J8_terminal_collar_custody_index.json")
    n480,_=load(DATA/"NF480_original_J8_endpoint_source_12jet_L2_custody.json")
    n479,_=load(DATA/"NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    orig,srcsha=load(DATA/"NF407_original_fourth_physical_coefficients_native.json")
    seam,seamsha=load(DATA/"NF406_original_prime_support_partition_exact.json")
    assert d["pass"]=="NF481" and d["original_full_twenty_jets_native_correlation"]
    assert d["original_parent_NF477_360jet_architecture_unchanged"]
    assert d["original_nf407_sha256"]==SRC==srcsha and d["original_nf406_sha256"]==SEAM==seamsha
    assert d["original_246_generators"] and d["original_273_modes"] and d["original_99_frequency_groups"] and d["original_odd_sinh_pole"]
    assert d["native_precision_bits"]==4096
    assert d["source_resolvent_lower_m"]==M and d["source_resolvent_contracted_order"]==N
    assert d["source_correlated_infinite_tail_result"]=="CERTIFIED"
    assert d["genuine_original_source_input_radius_lt"]=="1e-700"
    assert orig["original_dimension"]==242
    assert len(orig["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(orig["original_source_critical_sine_frequencies"])==32
    assert n446["original_nf407_source_sha256"]==n450["source_SHA256"]==n451["original_source_sha256"]==SRC
    assert n446["original_nf406_prime_seam_sha256"]==n450["seams_SHA256"]==n451["original_seams_sha256"]==SEAM
    assert n446["standing"].startswith("ACCEPTED")
    assert n446["derived_true_J7_J8_z_sup_lt"]==25000
    assert n446["derived_true_compact_Uprime_sup_lt"]==400
    assert n446["derived_true_compact_U_sup_lt"]==900
    assert n450["original_CI_result"]==n451["CI_result"]=="SUCCESS"
    assert n450["original_source_selected_plus_critical"]==246
    assert n480["original_nf407_source_sha256"]==n479["original_nf407_source_sha256"]==SRC
    assert n480["original_nf406_seams_sha256"]==n479["original_nf406_seams_sha256"]==SEAM
    assert n479["original_full_J8_signed_sign"].startswith("STRICT POSITIVE")
    assert n480["original_infinite_image_cutoff_M"]==M
    z0,z1=iv(n450["complete_z_B_outward_24_decimal"])
    assert F(-1,10**9)<z0<z1<0
    # The genuine original J8 physical length is
    # L=2B-log9, NOT an artificially rational substitute.
    loglo,loghi=log9_rational()
    Llo=F(11,5)-loghi
    Lhi=F(11,5)-loglo
    assert F(0)<Llo<Lhi<F(1,300)
    # The original odd centered physical response obeys the *accepted*
    # original NF446 compact actual J8 |z|<25000, including x=B.
    # The principal p=v[C8+(1/2)log(B/d)], |v|<1, with genuine
    # n=2,3,4,5,7,8,9 all active and each Lambda(n)/sqrt(n)<1:
    # log(n)<sqrt(n) for n>=1 (minimum sqrt(x)-log x at x=4,
    # log 4<2), hence 0<C8<7 on genuine J8.
    #
    # For L<=1/300, positive integrand and log330<6 imply:
    # integral_0^L log(B/d) <= (1/300)*(6+1)
    # integral_0^L log^2(B/d) <= (1/300)*(6^2+2*6+2).
    # Thus integral_0^L |p|^2 <=
    # (49+7*(6+1)+(6^2+2*6+2)/4)/300 =221/600<1/2.
    assert exp6_lower()>330
    p2_pos=F(49+7*7,300)+F(36+12+2,4*300)
    assert p2_pos==F(221,600) and 2*p2_pos<1
    # Source |z|<25000 on two genuine J8 halves: total length <2/300.
    # Choose sqrt(150)>12, so ||z||_2 < 25000/12.
    assert 12**2<150
    genuine_two_sided_z_L2=F(25000,12)
    # p has ||p||_2<1 on two sides by the explicit integrated log-square.
    # Hence the FULL original physical w=p+z obeys ||w||_2<2100.
    original_actual_w_L2_bound=F(2100)
    assert genuine_two_sided_z_L2+1<original_actual_w_L2_bound
    # The principal p itself diverges at x=B; NO claim p,z,w uniformly
    # bounded there, and the original D8 remains a log-improper integral.
    # This is genuine physical L2/energy control, not a sup norm of w.
    jets=d["original_first_twenty_source_jets_outward"]
    assert len(jets)==20
    leading=F(d["post_contraction_original_360_jet_absolute_sum"])
    rem=F(d["exact_absolute_binomial_remainder"])
    assert F(0)<rem<F(1,10**130)
    assert F(d["source_uniform_all_m_amplitude_bound"])>=leading+rem
    source_input_overcharge=F(5,10**700*M)
    spent=F(0);sweep=[]
    for k in range(1,21):
        spent+=abslower(jets[k-1])/F(M)**k
        W=leading-spent+rem+source_input_overcharge
        assert W>0
        U=W*F(M+k,2*k)
        # Same genuine original source NF480 endpoint proof:
        # |r_k(B-d)|<=U exp(-2Md), d∈[0, L].
        # Original odd J8 reflection doubles squared norm.
        assert 189**2<2*M
        eps=U/F(189)
        # r_k = w-g_k, and ||w||_2<2100 from the certified genuine
        # full source physical compact bound. Thus ||g_k||_2<2100+eps.
        # Exact quadratic energy difference bound:
        # | ||w||^2-||g_k||^2 | <=2||w|| eps + eps².
        # This is an UNCONDITIONAL inequality, unlike NF480's unproved
        # ||g12|| <4e-11 hypothesis.
        energy_fee=2*original_actual_w_L2_bound*eps+eps**2
        sweep.append({
          "extracted_true_original_source_jet_count":k,
          "source_20jet_remaining_abs_amplitude_at_M":str(W),
          "genuine_J8_endpoint_uniform_Uk":str(U),
          "original_two_sided_J8_L2_residual_rootfree_upper":str(eps),
          "original_TWO_J8_energy_fee_unconditional":str(energy_fee),
          "original_TWO_J8_energy_fee_unconditional_decimal":dec(energy_fee),
          "below_NF479_projector_gap_1e_minus26":energy_fee<F(1,10**26),
          "below_strong_error_gate_1e_minus28":energy_fee<F(1,10**28)
        })
        if k>=2:
            assert F(sweep[-1]["original_two_sided_J8_L2_residual_rootfree_upper"])<F(sweep[-2]["original_two_sided_J8_L2_residual_rootfree_upper"])
    assert sweep[11]["below_NF479_projector_gap_1e_minus26"]==False
    passing=[r for r in sweep if r["below_strong_error_gate_1e_minus28"]]
    assert len(passing)>0, "METHOD STOP: source-contracted twenty jets not sufficiently small"
    minpass=passing[0]["extracted_true_original_source_jet_count"]
    last=sweep[-1]
    assert last["below_strong_error_gate_1e_minus28"]
    # Exact NF479 conditional projector gap ~3.3105784e-26.
    nf479_gap=F(n479["original_coupled_exact_K_D7_conditional_corridor_width_approx"])
    assert nf479_gap>F(33,10**27) and nf479_gap<F(34,10**27)
    assert F(last["original_TWO_J8_energy_fee_unconditional"])<nf479_gap/F(100)
    # Need to retain full 18k original matched images, exact H-principal,
    # genuine n9 regular support and first k-1 nonleading source Phi's.
    # Those are part of the (NOT YET INTEGRATED) source comparator g_k.
    out={
      "pass":"NF481",
      "standing":"ACCEPTED ORIGINAL exact source twenty-jet endpoint energy truncation UNCONDITIONAL after NF446 full original physical |z| and exact J8 principal log² bounds; original J8 D8 numerical upper and NF404 OPEN",
      "original_nf407_source_sha256":SRC,
      "original_nf406_source_support_sha256":SEAM,
      "original_nf481_native_4096bit_full_273mode_raw_sha256":h,
      "same_original_nf477_360_resolvent_architecture":True,
      "original_j8_true_positive_physical_interval":["log9-B","B"],
      "original_j8_positive_physical_length_exact_rational":[str(Llo),str(Lhi)],
      "source_accepted_nf446_true_original_z_sup_strict":25000,
      "source_accepted_nf450_exact_original_zB_interval":[str(z0),str(z1)],
      "original_true_J8_principal_7_minus_shifts":[2,3,4,5,7,8,9],
      "original_true_principal_bound":"|v|<1, C8=sum_{n2,3,4,5,7,8,9} Lambda(n)/sqrt(n)<7",
      "original_principal_unnormalized_single_J8_L2_squared_strict_upper":str(p2_pos),
      "source_original_z_two_sided_J8_L2_strict_upper":"25000/12",
      "source_original_p_two_sided_J8_L2_strict_upper":"1",
      "source_original_FULL_w_equal_p_plus_z_two_sided_J8_L2_strict_upper":"2100",
      "source_original_full_w_sup_bound_at_B":"NONE: principal logarithm diverges",
      "source_complete_360jet_absolute_sum":str(leading),
      "source_exact_positive_binomial_resolvent_remainder":str(rem),
      "source_original_dyadic_input_extra_overcharge":str(source_input_overcharge),
      "source_resolvent_M":M,
      "source_first_twenty_original_jet_count":20,
      "original_unconditional_energy_fee_sweep":sweep,
      "first_source_jet_count_for_unconditional_true_J8_energy_fee_lt_1e_minus28":minpass,
      "source_original_twenty_jet_J8_two_sided_L2_rootfree_upper":last["original_two_sided_J8_L2_residual_rootfree_upper"],
      "source_original_twenty_jet_J8_two_sided_L2_rootfree_decimal":dec(F(last["original_two_sided_J8_L2_residual_rootfree_upper"])),
      "source_original_twenty_jet_J8_full_energy_fee_UNCONDITIONAL_upper":last["original_TWO_J8_energy_fee_unconditional"],
      "source_original_twenty_jet_J8_full_energy_fee_UNCONDITIONAL_decimal":dec(F(last["original_TWO_J8_energy_fee_unconditional"])),
      "source_original_J8_full_energy_fee_lt_1e_minus28":True,
      "source_original_energy_charge_below_nf479_gap_over_100":True,
      "actual_original_J8_direct_signed_upper":"OPEN",
      "actual_nf404_global_energy_upper":"OPEN",
      "canonical_W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF482 integrate the genuine original finite m<18000 and the 19 analytic full-source Phi jets with exact B endpoint p-log cancellation and n9 support; compare actual original J8 signed upper/whole Efull against NF404"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF481 ORIGINAL true J8 full physical p+z L2<2100, no false bounded-p claim")
    print("NF481 first original source jet count with UNCONDITIONAL energy fee <1e-28",minpass)
    print("NF481 original 20-jet two-sided J8 source L2 tail",dec(F(last["original_two_sided_J8_L2_residual_rootfree_upper"])))
    print("NF481 original 20-jet true full J8 energy truncation fee UNCONDITIONAL",dec(F(last["original_TWO_J8_energy_fee_unconditional"])))
    print("NF481 full J8 signed upper, NF404, W-ODD-NEG, RH OPEN")
if __name__=="__main__":main()
