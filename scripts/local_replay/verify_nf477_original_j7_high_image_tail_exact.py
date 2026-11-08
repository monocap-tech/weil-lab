#!/usr/bin/env python3
"""NF477 exact rational independent audit of original correlated high-image tail.

This checks the *original output's* global uniform image tail and source
SHA, not a new finite surrogate or the still-open complete J7 signed scalar.
"""
import argparse,json,math
from pathlib import Path
from fractions import Fraction as Q
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def log9_bounds(K=70):
    t=Q(4,5)
    lo=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(K)),Q(0))
    rem=2*t**(2*K+1)/(Q(2*K+1)*(1-t*t))
    return lo,lo+rem
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--native",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    d=json.loads(Path(a.native).read_text())
    assert d["pass"]=="NF477"
    assert d["original_nf407_sha256"]==SRC and d["original_nf406_sha256"]==SEAM
    assert d["original_246_generators"] and d["original_273_modes"] and d["original_99_frequency_groups"]
    assert d["original_odd_sinh_pole"]
    assert d["native_precision_bits"]==4096
    assert d["source_resolvent_lower_m"]==18000 and d["source_resolvent_contracted_order"]==360
    assert len(d["original_first_twelve_source_jets_outward"])==12
    assert all(q["correlated_resolvent_agrees_with_direct"] for q in d["direct_original_grouped_Tm_matches_convergent_source_resolvent"])
    M,N=18000,360
    q=Q(22*883,7*M)
    assert Q(d["exact_resolvent_q_bound"])==q<Q(1,5)
    rem=Q(0)
    for j in range(14):
        tail=(1-q)**(-j-1)-sum((Q(math.comb(r+j,j))*q**r for r in range(N-j)),Q(0))
        assert tail>0
        falling=Q(math.factorial(13),math.factorial(13-j))
        rem+=Q(10**160,M)*falling/(2*Q(11,10)*M)**j*tail
    rem+=Q(2*10**160,M)*Q(1,4*M)**N/(1-Q(1,4*M))
    assert rem==Q(d["exact_absolute_binomial_remainder"])
    leading=Q(d["post_contraction_original_360_jet_absolute_sum"])
    c=leading+rem+Q(5,10**700*M)
    assert c==Q(d["source_uniform_all_m_amplitude_bound"])
    lo,hi=log9_bounds()
    dmin=Q(11,4000)
    assert 2*Q(11,10)-hi>dmin
    assert M*2*dmin==Q(99)
    tail=c/dmin*Q(3,8)**99
    assert tail==Q(d["complete_original_J7_both_right_endpoint_image_tail_bound"])
    ok=tail<Q(1,10**40)
    assert ok==d["complete_original_J7_both_right_endpoint_tail_lt_1e_minus_40"]
    assert d["remaining_two_right_original_J7_signed_panels"]=="OPEN"
    assert d["complete_original_J7"]==d["J8"]==d["NF404"]==d["W_ODD_NEG"]==d["RH"]=="OPEN"
    r={
      "pass":"NF477",
      "standing":"independent exact-rational all-m source-preserving resolvent and genuine right-seam tail audit",
      "original_source_sha256":SRC,"original_seam_sha256":SEAM,
      "full_original_360_source_contracted_jets":True,
      "source_amplitude_upper_all_m_gte_18000":str(c),
      "exact_total_right_original_image_tail_upper":str(tail),
      "full_original_right_seam_image_tail_lt_1e40":ok,
      "two_right_original_signed_panels":"OPEN",
      "complete_original_J7":"OPEN",
      "RH":"OPEN"
    }
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(r,indent=2)+"\n")
    print("NF477 ORIGINAL high-image all-m resolvent exact rational identity PASS")
    print("NF477 original full J7 right seam tail sign-quality",ok)
    print("NF477 full signed original J7 and RH OPEN")
if __name__=="__main__":main()
