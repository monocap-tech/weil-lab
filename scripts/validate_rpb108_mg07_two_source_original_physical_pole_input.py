#!/usr/bin/env python3
"""NF: exact physical norm and genuine odd-pole payment for TWO original rays.

Every input is the TRUE physical original odd carrier, not FFT:
  f=a*1_{[-B,B]}sin(2*pi*(37/64)*x)+b*1_{[-B,B]}sinh(x/2)
  B=11/10.
The original 470 exceptional source J includes the b9 cluster-0
degree-0 sine and the genuine sinh pole. SI18 exact trig/pi bounds
and SI12 Taylor sinh bounds give ALL physical 2x2 Gram entries.

Output full outward Fraction intervals for ||f||², <f,s>, and
2|<f,s>|². The pole subtraction in Astar=Ao-2ss* is thereby
exactly paid in scalar original-source coordinates. This is a
GATE INPUT, not Astar(f) upper, SM40 cap lower, signed odd proof,
or a claimed rigorous method obstruction.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_si06_negative_band import B
from validate_rpb108_si12_even_supported_inverse import sinh_bounds
from validate_rpb108_si18_odd_rank_two_woodbury import gram,signed_odd_overlap
from validate_rpb108_si21_odd_jensen_four import outward

ROOT=Path(__file__).resolve().parents[1]
CENTER=F(37,64)
RAYS=((12001,16384,"direct_Knegative_selected"),
      (3013,4096,"SM40_cap_selected"))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    z=tuple(a*b for a in x for b in y)
    return min(z),max(z)
def sq(x):
    lo,hi=x
    return ((min(lo*lo,hi*hi) if lo*hi>0 else F(0)),
            max(lo*lo,hi*hi))
def scl(a,x):return mul((F(a),F(a)),x)
def subtract(x,y):return (x[0]-y[1],x[1]-y[0])
def render(x):return [str(z) for z in x]
def evaluate():
    assert B==F(11,10) and CENTER==F(37,64)
    Gss=outward(gram(CENTER,CENTER),15)
    q=outward(signed_odd_overlap(CENTER),15)
    sl,sh=sinh_bounds(B)
    S=outward((sl-B,sh-B),15)
    assert F(963,1000)<Gss[0]<Gss[1]<F(965,1000)
    assert F(140,1000)<q[0]<q[1]<F(141,1000)
    assert F(235,1000)<S[0]<S[1]<F(236,1000)
    det=subtract(mul(Gss,S),sq(q))
    assert det[0]>F(1,10)
    rays=[]
    for a,b,label in RAYS:
        L2=add(add(scl(a*a,Gss),scl(2*a*b,q)),scl(b*b,S))
        pole_overlap=add(scl(a,q),scl(b,S))
        pole_payment=scl(2,sq(pole_overlap))
        assert L2[0]>0 and pole_overlap[0]>0
        # Scalar relative pole budget is a STRICT true physical
        # input to the positive Astar form, not a signed-form result.
        assert pole_payment[1]<L2[0]/4
        if label.startswith("direct"):
            assert F(257000000)<L2[0]<L2[1]<F(258000000)
            assert F(61000000)<pole_payment[0]<pole_payment[1]<F(62000000)
        else:
            assert F(16000000)<L2[0]<L2[1]<F(17000000)
            assert F(3800000)<pole_payment[0]<pole_payment[1]<F(3900000)
        rays.append({
            "origin":"genuine_original_b9_cluster0_sine_and_sinh_pole",
            "purpose":label,
            "sine_frequency_exact":str(CENTER),
            "rational_sine_coefficient":a,
            "rational_pole_coefficient":b,
            "complete_true_physical_norm_squared_interval":render(L2),
            "true_pole_overlap_interval":render(pole_overlap),
            "genuine_Astar_pole_subtraction_2overlap_squared_interval":render(pole_payment),
            "pole_payment_relative_upper":str(pole_payment[1]/L2[0]),
            "true_entire_original_Ao_quadratic_computed":False,
            "full_matched_original_SM40_Kcap_lower_computed":False,
            "full_signed_Wodd_sign_test":"OPEN"})
    return {
      "status":"CERTIFIED_EXACT_RATIONAL_ORIGINAL_TWO_RAY_PHYSICAL_POLE_INPUT_ONLY",
      "original_odd_b9_total_source_dim":470,
      "exact_source_cluster_center":str(CENTER),
      "physical_sine_self_Gram_interval":render(Gss),
      "physical_sine_sinh_cross_Gram_interval":render(q),
      "physical_sinh_self_Gram_interval":render(S),
      "true_physical_two_source_Gram_determinant_lower":str(det[0]),
      "two_distinct_archived_numerical_candidates_kept_separate":True,
      "rays":rays,
      "complete_original_signed_odd_positive":"OPEN",
      "even_CC27_Weil_RH":"OPEN"}
if __name__=="__main__":
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert ledger["objective"]["status"]=="open"
    print(json.dumps(evaluate(),indent=2))
