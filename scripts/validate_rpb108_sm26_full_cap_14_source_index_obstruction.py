#!/usr/bin/env python3
"""SM26: complete 890-source 14-feature SURROGATE odd Schur ind_- >=3.

TRUE ORIGINAL finite-rank spectral inputs:
  SM11 full 17 ORIGINAL continuous seven-prime negative windows,
  complete physical signed Jensen Gram and Rayleigh bound
      Kneg >= gamma G G*, gamma=2/125, G*G > 4/5 I.
  SI29 original physical 14 continuous positive features with
      B14 = kappa I + P14 - 2|s><s|, P14 PSD rank<=14,
      B14 >= kappa_star I > eta.
  SM10 full ORIGINAL signed negative all-frequency upper
      Kneg <= U D U* + eta I, D=(1+tau)C SPD and
      U the complete original 890-column odd Taylor synthesis.

True 17-mode subspace intersects ker(P14) in dimension >=3;
B14-Kneg <-59/5000 there. Cap comparison gives
ind_-(B14-eta I-U D U*)>=3; invertible Schur congruence
gives ind_-(D^-1-U*(B14-eta I)^-1 U)>=3.
NO conclusion about the TRUE Astar=A_o-2ss*, because Astar>=B14:
its genuine cap Schur is >= the indefinite reference Schur.

Exact Fraction replay tests original SM11/SM10 and a genuinely
complete finite 17-mode rank14+odd-pole block inertial witness.
It does NOT numerically assemble the true original 890x890 Schur,
does not independently verify infinite-dimensional theory, and
cannot prove RH / full original odd positivity or negativity.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from validate_rpb108_sm11_rank17_c16_nogo import (
    certify_all_negative_windows,certify_physical_rank,N,DELTA,RADIUS
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves,TAU,BITS
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA,KAPPA_STAR,ETA_UP
)
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES

ROOT=Path(__file__).resolve().parents[1]


def original_certified_bounds():
    # SM11 actual original seven-prime full continuous
    # negative-frequency packet windows and ALL signed cross terms.
    worst=certify_all_negative_windows()
    lower,actual_lam,eps,min_diag,max_off=certify_physical_rank()
    gamma=4*RADIUS*DELTA
    nu=gamma*F(4,5)
    delta=nu-KAPPA
    assert N==17 and len(FEATURES)==14 and 17-14==3
    assert worst<-DELTA and lower>F(4,5)
    assert gamma==F(2,125)
    assert nu==F(8,625)
    assert delta==F(59,5000) and delta>0
    assert actual_lam>nu and actual_lam==gamma*lower

    # Full original signed negative cap 973 leaves, all 107
    # covariance blocks and ACTUAL total 890 Taylor directions.
    clusters,width,mass,total=full_upper_leaves()
    orders=[taylor_order(c[-1][1]-c[0][0],BITS)[0] for c in clusters]
    assert len(clusters)==107 and sum(orders)==890
    assert all(k>0 for k in orders)
    assert F(0)<ETA_UP<KAPPA_STAR<KAPPA
    assert TAU==F(1,1024)
    # This exact result uses the COMPLETE 890-source cap and
    # full eta:  B14-eta-Q <= B14-Kneg.
    assert KAPPA_STAR-ETA_UP>0
    return nu,delta,actual_lam,len(orders),sum(orders),mass


def finite_complete_block_inertia_regression():
    """17-mode algebra only; illustrates FULL Schur inertia, not Kneg.

    Positive-reference rank 14 and negative odd pole live on the
    first 14 coordinates. Three feature-null directions are
    negative after ALL 17 cap sources are coupled through the
    exact inverse Schur, though B14-eta and D are SPD.
    """
    assert len(FEATURES)==14
    nu=F(8,625)
    eta=ETA_UP
    # A = B14-eta I: scalar 1/1000 on true reference feature-null,
    # positive original-reference-style 1 on 14 selected features.
    # Negative odd pole subtracts kappa/4 on first reference mode.
    b=[KAPPA+(F(1) if i<14 else F(0))
       -(KAPPA/F(4) if i==0 else F(0)) for i in range(17)]
    assert all(x>KAPPA_STAR for x in b)
    A=[v-eta for v in b]
    assert all(x>0 for x in A)
    D=[nu]*17
    assert all(x>0 for x in D)
    # Block congruence between A-U D U* and D^-1-U*A^-1 U:
    # U=I17. Exact index, no decoupled "one-column" assumption.
    primal=[A[i]-D[i] for i in range(17)]
    dual=[1/D[i]-1/A[i] for i in range(17)]
    assert sum(x<0 for x in primal)==3
    assert sum(x<0 for x in dual)==3
    assert all((primal[i]<0)==(dual[i]<0) for i in range(17))
    assert primal[-1] < -F(59,5000)
    # True positive operator could supply extra missing continuum
    # response on all 17 and restore positivity: NO odd-negative
    # Weil witness is inferred from the surrogate.
    true_A=[A[i]+F(1) for i in range(17)]
    true_dual=[1/D[i]-1/true_A[i] for i in range(17)]
    assert all(x>0 for x in true_dual)
    # Even exact 2-column SPD does not establish whole 17x17.
    assert dual[0]>0 and dual[1]>0 and any(x<0 for x in dual[14:])
    return primal[-1],dual[-1],len(dual)


def run():
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert "SM11" in gov["evidence"] and "SM25" in gov["evidence"] and "SM26" in gov["evidence"]
    odd=next(v for v in gov["obligations"] if v["id"]=="W-ODD-NEG")
    assert odd["status"]=="open"
    assert "SM26" in odd["evidence"] and "SM24" in odd["evidence"]
    assert "O1/O2" in odd["acceptance"]
    nu,delta,actual_lam,nblocks,ncolumns,mass=original_certified_bounds()
    primal,dual,n=finite_complete_block_inertia_regression()
    print("SM26 original true 17 independent negative Jensen packets nu >",nu,
          "source actual > ",float(actual_lam),flush=True)
    print("SM26 original 14 SI29 positive reference features;"
          " dimension intersection >=17-14=3",flush=True)
    print("SM26 physical ORIGINAL reference-minus-Kneg"
          " three-direction strict spectral margin >",delta,flush=True)
    print("SM26 full actual SM10 original negative cap source blocks",
          nblocks,"total odd columns",ncolumns,"mass",float(mass),flush=True)
    print("SM26 original SI29 B14-eta positive floor >",
          KAPPA_STAR-ETA_UP,flush=True)
    print("SM26 derived original full 890-source SI29 surrogate"
          " cap Schur NEGATIVE INDEX >=3 (complete-block inertia),"
          " without numerically constructing its 890x890 entries",flush=True)
    print("SM26 exact full 17-mode block inertia toy negative diagonals",
          primal,dual,"size",n,flush=True)
    print("SM26 PASS SCOPED: COMPLETE ORIGINAL negative-cap induced"
          " rank14 PRECONDITIONER NO-GO. 17 true signed-frequency"
          " modes minus 14 SI29 positive reference features leave"
          " >=3 strictly negative full surrogate Schur directions."
          " Does NOT establish negativity of true original Astar,"
          " W-ODD-NEG complete O1/O2, original even E1-E4,"
          " whole Weil, CC27 D-Riesz or RH. Original analytic"
          " premises and source/frequency identification"
          " need independent audit.",flush=True)


if __name__=="__main__":
    run()
