#!/usr/bin/env python3
"""EF23 — ORIGINAL signed arithmetic mixed sparsity and FIR edge-prefix gate.

Native original SI10 even b9 source e=1_I cos(2pi*(37/64)x)
and fixed EF21/EF22 469-source FIR compact C5 cosine-six f.

Source cutoff geometry proves EXACT:
  q_prime,n3(e,f)=q_prime,n4(e,f)=q_prime,n8(e,f)=q_prime,n9(e,f)=0;
  q_prime,n2(e,f)>1.5e-6 (inherited native EF22 exact bound);
  q_prime,n5(e,f), q_prime,n7(e,f) remain nonzero UNKNOWN.

All original n5 included negative-center full bells are k=-258..469
(728 coefficients); use the exact native FIR source root at c0=37/64
to replace that sum by minus its omitted 211 coefficients k=-469..-259.
n7 uses k=431..469 (39 coefficients).

This is exact original source arithmetic reduction, NOT a numerical
sign/evaluation of n5,n7, arch mixed, energy or normalized Schur.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import SHIFTS,ACTIVE,B,WEIGHTS
from validate_rpb108_ef21_original_even_fixed_bell import (
    authentic_source_replay, bell_transform_identity,
    physical_support_and_disjointness, H,N,R,
)
from validate_rpb108_ef22_original_even_prime_energy_vanish import (
    original_primes_separate_all_f_supports,
    exact_partial_boundary_bell_classification,
    exact_original_n2_signed_mixed_lower,
)

ROOT=Path(__file__).resolve().parents[1]
C0=F(37,64)
EXPECTED={
    2:{"neg":(939,0,0,-N,N),"pos":(0,938,1,None,None)},
    3:{"neg":(939,0,0,-N,N),"pos":(0,939,0,None,None)},
    4:{"neg":(939,0,0,-N,N),"pos":(0,939,0,None,None)},
    5:{"neg":(728,211,0,-258,N),"pos":(0,939,0,None,None)},
    7:{"neg":(39,900,0,431,N),"pos":(0,939,0,None,None)},
    8:{"neg":(0,939,0,None,None),"pos":(0,939,0,None,None)},
    9:{"neg":(0,939,0,None,None),"pos":(0,939,0,None,None)},
}


def classify_actual_original_cutoff():
    l2lo,l2hi=SHIFTS[2]
    alo,ahi=B-l2hi+N*H,B-l2lo+N*H
    assert 0<alo<ahi<B
    assert set(ACTIVE)==set(EXPECTED)
    results={}
    checked=0
    for n in sorted(ACTIVE):
        nlo,nhi=SHIFTS[n]
        cutoff=(B-nhi,B-nlo)  # for e(x+ln n) upper right endpoint
        per={}
        for s,name in ((-1,"neg"),(1,"pos")):
            inside=[]
            outside=[]
            partial=[]
            for k in range(-N,N+1):
                clo,chi=(alo-k*H,ahi-k*H) if s==1 else (-ahi-k*H,-alo-k*H)
                # Actual 2r-wide compact bell interval:
                if chi+R<cutoff[0]:
                    inside.append(k)
                elif clo-R>cutoff[1]:
                    outside.append(k)
                else:
                    # Only true inherited n2 positive-center k=N
                    # is exactly centered on the original cutoff;
                    # all others must classify strictly.
                    assert n==2 and s==1 and k==N,(
                        "unexpected unresolved source cutoff",n,s,k)
                    assert clo<=cutoff[0]<=cutoff[1]<=chi
                    partial.append(k)
                checked+=1
            assert len(inside)+len(outside)+len(partial)==2*N+1
            actual=(len(inside),len(outside),len(partial),
                    inside[0] if inside else None,
                    inside[-1] if inside else None)
            assert actual==EXPECTED[n][name],(
                "native original SI10 cutoff count",n,name,actual)
            per[name]=actual
        results[n]=per
    assert checked==len(ACTIVE)*2*(2*N+1)==13146
    return results,checked


def exact_fir_source_root_and_prefixes():
    centers,orders=authentic_source_replay()
    assert centers[0]==C0 and sum(orders)==N
    # Exact rational positive c0 is ONE actual native SI10 root:
    # S_h(c0)=prod_j(2cos(2pi h c0)-2cos(2pi h cj))^pj=0,
    # j=0 factor zero, p0>=1.
    assert orders[0]>=1
    # FIR Laurent coefficients are exactly real and symmetric:
    # A_-k=A_k from the real symmetric product, A_+-N=1.
    # Therefore sum_-N^N A_k e^(-i omega k h)=S_h(c0)=0.
    k5_in=list(range(-258,N+1))
    k5_out=list(range(-N,-258))
    k7_in=list(range(431,N+1))
    assert (len(k5_in),len(k5_out),len(k7_in))==(728,211,39)
    assert len(k5_in)+len(k5_out)==2*N+1
    assert k5_out[-1]==-259
    assert k7_in[0]==431 and k7_in[-1]==N
    # For n=3,4, the whole negative lattice is included,
    # and its complete original FIR cosine sum is exactly 0.
    # For n=8,9, no original f lobe is included.
    # For n=5, retained 728-coefficient sum equals minus the
    # omitted 211-coefficient sum EXACTLY, not approximately.
    # For n=7, only 39 coefficients needed. Both remain
    # unevaluated and have no certified sign.
    return len(k5_out),len(k7_in)


def run():
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    obs={o["id"]:o for o in manifest["obligations"]}
    assert manifest["active_obligation"]=="W-EVEN-FORM"
    assert all(obs[x]["status"]=="open"
               for x in ("W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert all(x in obs["W-EVEN-FORM"]["evidence"]
               for x in ("EF21","EF22","EF23"))
    # Reuse and enforce parent actual original source receipts.
    parent=original_primes_separate_all_f_supports()
    clips,_=exact_partial_boundary_bell_classification()
    n2lo,n2hi,_=exact_original_n2_signed_mixed_lower()
    assert parent["pairs"]==13139 and len(clips)==2
    assert n2lo>F(15,10000000)
    counts,checks=classify_actual_original_cutoff()
    k5,k7=exact_fir_source_root_and_prefixes()
    mass,norm=bell_transform_identity()
    assert mass>0 and norm>0
    print("EF23 actual ORIGINAL SI10 even native source c0:",C0,
          "original 469-factor h:",H,"bell r:",R,flush=True)
    for n in sorted(counts):
        print("EF23 ORIGINAL prime",n,"sigma=+ cutoff:",
              "neg (inside,outside,partial,klo,khi)",counts[n]["neg"],
              "pos",counts[n]["pos"],flush=True)
    print("EF23 rigorous ORIGINAL source cutoff lattice comparisons:",
          checks,"plus EF22 source 13139 prime self-shift nonoverlaps.",
          flush=True)
    print("EF23 exactly ZERO original arithmetic MIXED channels:",
          "n=3,4 by complete actual FIR root S_h(c0)=0;",
          "n=8,9 by no support intersection.",flush=True)
    print("EF23 actual original signed n2 MIXED interval:",
          float(n2lo),float(n2hi),flush=True)
    print("EF23 remaining n5 original FIR mixed coefficient sum:",
          "728 included = -211 excluded (exact native source root),",
          "n7 exactly",k7,"included coefficients; still no signs.",
          flush=True)
    print("EF23 exact arithmetic decomposition:",
          "M_prime=M_2+M_5+M_7;",
          "M_5=+w5*H_r(c0)*Re(exp(i omega*(ln5-a))",
          "*sum_{k=-469}^{-259} A_k exp(-i omega k h));",
          "M_7=-w7*H_r(c0)*Re(exp(i omega*(ln7-a))",
          "*sum_{k=431}^{469} A_k exp(-i omega k h)).",
          flush=True)
    print("EF23 SCOPE STOP: no rigorous n5/n7 signed interval,"
          " no arch mixed M_arch, arch E upper, normalized inverse"
          " Schur, corrected full even PSD, odd/whole Weil or RH.",
          flush=True)


if __name__=="__main__":
    run()
