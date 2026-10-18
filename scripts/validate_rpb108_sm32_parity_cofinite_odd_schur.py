#!/usr/bin/env python3
"""SM32: TRUE ORIGINAL ODD parity-compressed SI10 cofinite spectral index.

Exact original SI10 FULL seven-prime signed physical protected multiplier
  m(xi)>kappa outside its complete b9 unresolved frequency cover;
  SI10 original Weil Q[f] >17/25000 ||f||² on full source V9^perp.
Odd parity projects its reflected complex 2p_j source pairs onto
ONE odd real supported modulation for each k, plus odd pole s:
   dim E9_odd<=sum_j p_j+1<=470 (vs SI10 full dim<=939).
Hence original full signed ODD Q_o[f]>17/25000||f||² on E9_odd^perp,
and original negative index ind_-(W_o)<=470, NOT zero.

True original full-odd positivity requires complete subtractive
Feshbach A-C*D^-1 C >=0 on this <=470D exceptional space.
SM31 actual 2D positive packet G need not belong to E9, so the
augmented E9+G has dimension<=472 with same infinite complement
floor, and a CONDITIONAL coupling budget ||C_FG||²<17/4400000.
No original cross bound or <=470D sign is computed here.

Arithmetic: exact SI10 original all-real 973/107 cover, b=9
physical modulation orders, all original negative mass and protected
frequencies, odd/even projected dimension, exact Schur cross counter-
models, fail-closed canonical W-ODD-NEG O1/O2 and RH custody.
Analytic signed-Fourier/minmax/form-domain arguments need audit.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_si10_complement_positivity import (
    protected_outer_band, protected_inner_cover, KAPPA, B,
)
from validate_rpb108_si08_multiband_rank import taylor_order

ROOT=Path(__file__).resolve().parents[1]
BITS=9
MU=F(17,25000)
SM31_FLOOR=F(1,176)
COUPLING_BUDGET=F(17,4400000)


def true_original_odd_parity_source_count():
    # THE SAME original full signed original seven-prime cover as SI10.
    # Not a newly sampled or surrogate set of source frequencies.
    outer_leaves,outer_min=protected_outer_band()
    clusters,width,mass,n_unresolved,n_accepted=protected_inner_cover()
    assert outer_leaves==2535 and outer_min>KAPPA
    assert len(clusters)==107
    assert n_unresolved==973 and n_accepted==9261
    assert width==F(973,32) # original BOTH signs =30.40625
    assert mass<F(38)
    assert KAPPA==F(1,1000) and B==F(11,10)
    orders=[taylor_order(r-l,BITS)[0] for l,r,weight in clusters]
    assert len(orders)==107 and all(p>=1 for p in orders)
    sum_orders=sum(orders)
    original_full_dim_upper=2*sum_orders+1
    odd_dim_upper=sum_orders+1
    assert original_full_dim_upper<=939
    assert odd_dim_upper<=470
    # Odd projection of pair x^k e^(+/-2picx) is ONE odd REAL
    # x^k sin(2picx) if k even, x^k cos(2picx) if k odd.
    # The even reflected component is automatically orthogonal
    # to all odd f in genuine original centered support.
    even_k=sum((p+1)//2 for p in orders)
    odd_k=sum(p//2 for p in orders)
    assert even_k+odd_k==sum_orders
    assert even_k>0 and odd_k>0
    # Add ONE actual odd pole s=sinh(x/2) to exceptional basis.
    assert odd_dim_upper==even_k+odd_k+1
    # Same ORIGINAL protected frequency and negative multiplier
    # all-real measures W and M, from the genuine SI10 cover.
    eps2=F(1,2**(2*BITS))
    protect_loss=2*B*width*eps2
    neg_loss=2*B*mass*eps2
    actual_mu=KAPPA*(1-protect_loss)-neg_loss
    assert actual_mu>F(68,100000)==MU
    assert actual_mu>KAPPA/F(2)
    # Coercive original odd form on a closed L2-orthogonal
    # complement of at most 470 physically supported odd sources;
    # negative index must inject under projection to that span.
    return dict(nclusters=len(orders),nleaf=n_unresolved,
                protected=n_accepted,full_dim=original_full_dim_upper,
                odd_dim=odd_dim_upper,even_degree=even_k,
                odd_degree=odd_k,mu=actual_mu,cover_w=width,cap_mass=mass)


def exact_full_operator_schur_regressions():
    assert MU==F(68,100000)
    assert SM31_FLOOR==F(1,176)
    assert MU*SM31_FLOOR==COUPLING_BUDGET

    def det2(a,b,c):
        return a*b-c*c
    # Positive original-style SI10 full complement D>=mu and
    # independently positive SM31 G>=1/176 may combine into
    # an INDEFINITE full original block if mixed C is not paid.
    A=SM31_FLOOR
    D=MU
    c_good=F(1,1000)
    c_bad=F(1,100)
    assert det2(A,D,c_good)>0
    assert det2(A,D,c_bad)<0
    assert (A-c_good*c_good/D)>0
    assert (A-c_bad*c_bad/D)<0
    # The sign of the entire original corrected finite Schur,
    # NOT A alone, is decisive. This holds also for a 470×470
    # full finite block against the original infinite D.
    assert det2(A,D,c_bad)==D*(A-c_bad*c_bad/D)
    assert det2(A,D,c_good)==D*(A-c_good*c_good/D)

    # Even two coupled positive G modes do not remove an
    # independent exceptional negative mode; add one K mode.
    g1=F(1,176); g2=F(1,176); k=F(-1)
    assert g1>0 and g2>0 and k<0
    # With full complement D strictly positive, the FULL matrix
    # diag(g1,g2,k,D) still has negative index at least one.
    assert k<0 and D>0
    # If a finite positive reference has a negative K mode,
    # adjoining two positive G modes does not fix its sign.
    return c_good,c_bad,det2(A,D,c_good),det2(A,D,c_bad)


def run():
    custody=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in custody["obligations"] if o["id"]=="W-ODD-NEG")
    assert custody["active_obligation"]=="W-ODD-NEG"
    assert custody["objective"]["status"]=="open"
    assert custody["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open" and "O1/O2" in odd["acceptance"]
    assert "SM31" in odd["evidence"] and "SM32" in odd["evidence"]
    assert "SM31" in custody["evidence"] and "SM32" in custody["evidence"]
    assert "parity_cofinite_original_odd_gate" in custody["governance"]
    a=true_original_odd_parity_source_count()
    good,bad,dgood,dbad=exact_full_operator_schur_regressions()
    print("SM32 ORIGINAL full signed SI10 seven-prime protected cover",
          a["nleaf"],"unresolved leaves",a["nclusters"],"clusters",
          a["protected"],"positive cells",flush=True)
    print("SM32 SI10 full original parity-cofinite dimension upper",
          a["full_dim"],"STRICT odd parity reduction",
          a["odd_dim"],flush=True)
    print("SM32 true original odd source parity counts x^k sin/x^k cos",
          a["even_degree"],a["odd_degree"],"plus ONE odd pole",flush=True)
    print("SM32 TRUE ORIGINAL full signed odd coercive L2 complement floor",
          "exact Fraction acceptance >17/25000:",
          float(a["mu"]),flush=True)
    print("SM32 original odd spectral NEGATIVE INDEX UPPER",
          a["odd_dim"],"<=470, NOT zero",flush=True)
    print("SM32 full original odd O1/O2 equivalent to complete"
          " corrected finite form A-C*D^-1 C PSD on original E9"
          " parity dimension <=470; this gate remains OPEN",
          flush=True)
    print("SM32 SM31 original positive G 2D augmented exceptional"
          " dimension <=472, whole ORIGINAL physical infinity"
          " still D>=17/25000",flush=True)
    print("SM32 CONDITIONAL true original cross norm² budget",
          COUPLING_BUDGET,"(no bound claimed)",flush=True)
    print("SM32 2x2 exact rational physical Schur adversarial"
          " cross small/large determinant display",
          float(dgood),float(dbad),flush=True)
    print("SM32 PASS SCOPED: original signed 7-prime odd negative"
          " INDEX<=470 and strict infinite physical positive"
          " complement. Correct-sign 470-source ORIGINAL Feshbach"
          " acceptance and 472 augmented coupled SM31 acceptance"
          " specified but UNPROVED. No positivity for the finite"
          " entire exceptional Schur, no full original O1/O2,"
          " even E1-E4, full signed Weil, CC27 D-Riesz or RH.",
          flush=True)


if __name__=="__main__":
    run()
