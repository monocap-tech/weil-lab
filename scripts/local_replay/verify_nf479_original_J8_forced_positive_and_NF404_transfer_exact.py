#!/usr/bin/env python3
"""NF479 exact original source operator-to-J8 signed transfer.

Replays immutable NF403/NF404/NF410/accepted original J1..J6 signed sources
through NF454 and the accepted NF478 original complete J7 signed artifact.

The NF462 original J7 negative condition was NECESSARY for NF404's
sufficient centered-energy cap, never sufficient by itself.
This audit closes a DIFFERENT fact: Bessel's original selected+two witness
lower plus the complete J7 signed integral force the original *entire*
J8 signed contribution to be strictly POSITIVE, even before J8 integration.

No finite projection or local scalar is a proof of W-ODD-NEG/RH.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse,hashlib,json,runpy,sys
from decimal import Decimal,localcontext
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/"notes/data/provisional"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def iv(v):
    a,b=map(Q,v)
    assert a<=b
    return a,b
def decimal(x):
    with localcontext() as c:
        c.prec=45
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf478-original-raw",required=True,
                    help="NF478 original independent seven-panel 4096-bit source Fraction artifact")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    # NF454 exact source-external call reads accepted original signed D1..D6
    # and principal power, without using any 2/4-node numerical pilot.
    ledger=runpy.run_path(str(ROOT/"scripts/local_replay/verify_nf454_gate.py"))
    nf403,h403=load(DATA/"NF403_original_joint_complement_power_exact.json")
    nf404,h404=load(DATA/"NF404_original_selected_pole_shear_exact.json")
    nf453,h453=load(DATA/"NF453_original_J7_J8_principal_and_island_custody.json")
    nf462,h462=load(DATA/"NF462_original_forced_J7_signed_deficit_custody.json")
    nf478,h478=load(DATA/"NF478_original_complete_J7_signed_seven_panel_custody.json")
    raw,hraw=load(args.nf478_original_raw)
    assert nf478["source_original_nf407_sha256"]==nf453["source_sha256"]==SRC
    assert nf478["source_original_nf406_seams_sha256"]==nf453["seams_sha256"]==SEAM
    assert nf462["original_source_nf407_sha256"]==SRC
    assert nf462["original_seams_nf406_sha256"]==SEAM
    assert nf478["source_native_CI"]["all_final_runs"]=="SUCCESS"
    assert nf478["source_native_CI"]["independent_exact_fraction_run"]==42442681289
    assert hraw==nf478["independent_full_J7_exact_fraction_artifact"]["json_sha256"]
    assert raw["pass"]=="NF478" and raw["original_COMPLETE_seven_panel_J7_signed_sign"]=="NEGATIVE"
    assert raw["whole_original_J7_physical_support"]==["log8-B","log9-B"]
    assert raw["original_nf407_source_sha256"]==SRC and raw["original_nf406_seams_sha256"]==SEAM
    assert raw["NF464_conditional_J7_negative_gate_source_certified"]
    assert raw["NF404"]==raw["W_ODD_NEG"]==raw["RH"]=="OPEN"
    assert nf404["original_dimension"]==242
    C=Q(nf404["exact_sufficient_new_full_supported_centered_scalar_power_upper_target"])
    Rlo=Q(nf404["original_selected_after_pole_shear_power_lower_exact"])
    gamma=Q(nf404["exact_source_original_full_complement_power_budget"])
    d12lo=Q(nf403["source_strict_joint_dual_power_lower"])
    d12hi=Q(nf403["source_strict_joint_dual_power_upper"])
    assert C==Rlo+gamma and Q(0)<d12lo<d12hi<gamma
    assert (nf403["original_nf389_joint_lower_report_sha256"] and
            nf403["original_nf389_joint_upper_report_sha256"])
    # Original physical energy Efull = K + D7 + D8. Original Bessel:
    # Efull >= Rlo + d12lo, with same centered original fourth source.
    Klo=ledger["pl"]+ledger["sl"]
    Khi=ledger["pu"]+ledger["su"]
    assert Q(0)<Klo<Khi<C+Q("5e-22")
    d7lo,d7hi=iv(raw["original_COMPLETE_seven_panel_J7_signed_interval"])
    b7lo,b7hi=iv(nf478["original_seven_panel_J7_signed_D_outward"])
    assert b7lo<=d7lo<=d7hi<=b7hi<0
    ep8lo,ep8hi=ledger["l8"],ledger["u8"]
    assert Q(0)<ep8lo<ep8hi
    # Historical NF462: Efull<=C IMPLIES D7 <= C-Klo+2Ep8hi.
    # It does NOT have converse. NF478 meets only this necessary gate.
    d7necessary=C-Klo+2*ep8hi
    assert d7hi<d7necessary<-Q("2e-22")
    # New theorem: original J8 true signed D8 MUST BE POSITIVE.
    # D8 = Efull - K - D7, and exact lower Efull >= Rlo+d12lo.
    d8positive_lower=Rlo+d12lo-Khi-d7hi
    assert Q("1e-22")<d8positive_lower<Q("2e-22")
    # The one-sided J8 energy floor -2Ep8hi was valid, but extremely
    # loose. The new LOWER is above zero on the ENTIRE original J8.
    old_j8_floor=-2*ep8hi
    assert old_j8_floor<0<d8positive_lower
    # The full NF404 sufficient scalar inequality holds IF this original
    # J8 signed UPPER is certified. That actual upper is still OPEN.
    d8sufficient_upper=C-Khi-d7hi
    # It definitely fails if a true ORIGINAL J8 lower exceeds this boundary.
    d8certain_failure_lower=C-Klo-d7lo
    assert d8positive_lower<d8sufficient_upper<d8certain_failure_lower
    # An exact and VERY NARROW "conditional corridor" at fixed true K,D7:
    # if NF404 cap holds, the coupled J8 signed response must satisfy
    #  Rlo+d12lo-K-D7 <= D8 <= C-K-D7,
    # whose width is EXACTLY gamma-d12lo, irrespective of individual K,D7.
    corridor=C-Rlo-d12lo
    assert d8sufficient_upper-d8positive_lower==corridor==gamma-d12lo
    assert Q(0)<corridor<Q("5e-26")
    # Uncorrelated K and J7 outward intervals make the FAIL threshold
    # wider: exact interval widths must be paid, never ignored.
    independent_width=(Khi-Klo)+(d7hi-d7lo)
    assert d8certain_failure_lower-d8sufficient_upper==independent_width
    assert independent_width>corridor
    # Alternate nonnegative energy E8=int_J8 (p+z)^2:
    # D8=2(E8-Ep8), with Ep8 in the original accepted source interval.
    e8minimum=ep8lo+d8positive_lower/2
    e8sufficient_upper=ep8lo+d8sufficient_upper/2
    e8certain_failure_lower=ep8hi+d8certain_failure_lower/2
    assert Q(0)<e8minimum<e8sufficient_upper<e8certain_failure_lower
    # The true original entire squared energy lower:
    elo=Klo+d7lo+d8positive_lower
    # Not used as a bound: Efull Bessel already dominates.
    assert Rlo+d12lo<C
    out={
      "pass":"NF479",
      "standing":"ACCEPTED exact original Bessel+full J7 source FORCES entire J8 signed POSITIVE; original NF404 sufficient cap transfer remains OPEN",
      "source_original_nf407_sha256":SRC,
      "source_original_nf406_seams_sha256":SEAM,
      "original_nf478_exact_source_raw_sha256":hraw,
      "original_source_receipts_sha256":{"NF403":h403,"NF404":h404,"NF453":h453,"NF462":h462},
      "actual_original_full_source_identity":"Efull=K+D7+D8=R+d12+T, K=Ep+sum_{j=1}^6 D_j",
      "Bessel_original_lower_identity":"Efull>=Rlo+d12lo",
      "original_NF404_exact_C":str(C),
      "original_NF404_exact_selected_Rlo":str(Rlo),
      "original_NF404_exact_complement_budget_gamma2":str(gamma),
      "original_exact_2D_joint_projection_lower":str(d12lo),
      "original_K_interval":[str(Klo),str(Khi)],
      "original_complete_J7_exact_signed_interval":[str(d7lo),str(d7hi)],
      "NF462_necessary_J7_negative_threshold":str(d7necessary),
      "NF462_necessary_J7_negative_condition":"PASS but is NOT sufficient for NF404",
      "original_J8_old_principal_only_D8_floor":str(old_j8_floor),
      "original_FULL_J8_strict_signed_D8_lower":str(d8positive_lower),
      "original_FULL_J8_strict_signed_D8_lower_decimal":decimal(d8positive_lower),
      "original_FULL_J8_signed_sign":"POSITIVE (derived from global original physical Bessel lower and complete J7)",
      "original_J8_signed_upper": "OPEN",
      "original_J8_signed_sufficient_upper_for_NF404":str(d8sufficient_upper),
      "original_J8_signed_sufficient_upper_decimal":decimal(d8sufficient_upper),
      "original_J8_signed_certain_failure_lower_for_NF404":str(d8certain_failure_lower),
      "original_J8_signed_certain_failure_lower_decimal":decimal(d8certain_failure_lower),
      "original_exact_coupled_conditioned_J8_corridor_width":str(corridor),
      "original_exact_coupled_conditioned_J8_corridor_width_decimal":decimal(corridor),
      "original_independent_K_D7_uncertainty_width":str(independent_width),
      "original_independent_K_D7_uncertainty_width_decimal":decimal(independent_width),
      "original_principal_J8_energy_interval":[str(ep8lo),str(ep8hi)],
      "original_J8_E8_strict_lower":str(e8minimum),
      "original_J8_E8_sufficient_upper_for_NF404":str(e8sufficient_upper),
      "original_J8_E8_certain_failure_lower_for_NF404":str(e8certain_failure_lower),
      "original_NF404_cap_decided":False,
      "actual_original_J8_signed_full_integral_measured":False,
      "original_J8_signed_sign_inferred_from_fully_global_coupled_source":True,
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF480 source-correlated genuine original J8 signed upper and direct global energy correlation to sub 3.32e-26; preserve physical n9 seam and B endpoint logarithm"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF479 original full J8 SIGN strictly positive; rigorous lower",decimal(d8positive_lower),flush=True)
    print("NF479 original J8 signed sufficient UPPER target",decimal(d8sufficient_upper),flush=True)
    print("NF479 original J8 signed certain FAIL lower",decimal(d8certain_failure_lower),flush=True)
    print("NF479 *fixed actual K,D7* conditional corridor WIDTH",decimal(corridor),flush=True)
    print("NF479 NF404, W-ODD-NEG, RH OPEN",flush=True)
if __name__=="__main__":main()
