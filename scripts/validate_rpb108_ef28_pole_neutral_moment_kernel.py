#!/usr/bin/env python3
"""EF28: native original SI10 469 EVEN sources plus positive-pole-neutral
471-bell finite moment kernel.

This proves a source-adaptive exact PHYSICAL existence/energy lemma
without EF20's 469-fold product filter, and states the finite source
residual acceptance gate precisely. It does NOT evaluate the actual
470x471 source moments or g, and does NOT decide a Schur sign/RH.

469 native real-even source rows + one TRUE pole row = 470 constraints.
471 disjoint compact even C5 bell pairs give nullity >=1 for ANY
exact real source moment matrix. For f from that nullspace, the true
original signed source/cofinite form is mu||f||²<=q0(f,f)<34||f||².
If g_j=q0(e,phi_j), delta=dist(g,range(Htilde^T)) then
R_original(e) >= delta²/(34*d) whenever delta>0,
d=231*r/1024. Since the pole overlap on f is exactly zero,
the even full physical form is NEGATIVE if
delta²/(34*d)>q0(e,e)+2<cosh(x/2),e>².
These are conditional acceptance criteria, not numerical discoveries.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

from validate_rpb108_si06_negative_band import B,TWOC
from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover,protected_outer_band,KAPPA
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_ef21_original_even_fixed_bell import (
    bell_transform_identity
)

ROOT=Path(__file__).resolve().parents[1]
COUNT=471
SOURCE_ROWS=469
TOTAL_ROWS=SOURCE_ROWS+1
GRID=F(1,512)
R=F(1,8192)
D=F(231,1024)*R
MU=F(17,25000)


def original_source_and_geometry():
    leaves,minimum=protected_outer_band()
    clusters,width,mass,unresolved,accepted=protected_inner_cover()
    assert (leaves,len(clusters),unresolved,accepted)==(2535,107,973,9261)
    assert width==F(973,32) and minimum>KAPPA
    centers=[(l+r)/2 for l,r,_ in clusters]
    orders=[taylor_order(r-l,9)[0] for l,r,_ in clusters]
    assert sum(orders)==SOURCE_ROWS and centers[0]==F(37,64)
    assert all(p>=1 for p in orders)
    xs=[(j+1)*GRID for j in range(COUNT)]
    assert xs[0]==GRID and xs[-1]==F(471,512)
    # Positive and negative bell supports; all 942 physical lobes
    # mutually disjoint, with no FIR-translated tail.
    assert 2*R<GRID and 2*R<2*xs[0]
    assert xs[-1]+R < B
    assert xs[0]-R>0
    assert COUNT==TOTAL_ROWS+1
    assert 2*COUNT==942 and len(centers)==107
    return centers,orders,xs


def exact_bell_l2_and_energy():
    # Each phi_l=[b_r(x-x_l)+b_r(x+x_l)]/2 has two disjoint
    # amplitude 1/2 copies of the native cos^6 bell.
    # Norm² = (1/2)*(231r/512)=231r/1024=D.
    # Derivative norm ratio is independent of all coefficients
    # because all 942 translates are disjoint.
    assert D==F(231,8388608)
    norm_b=F(231,512)*R
    assert D==norm_b/2
    ratio_over_pi2=F(9,11)/R**2
    fourier_second_moment=ratio_over_pi2/4
    assert fourier_second_moment==F(9,44)/R**2

    # Genuine ORIGINAL arch a(xi)<8+ln(1+|xi|)
    # and Jensen imply q_arch(f,f)/||f||²
    # <8+ln2+ln(1+9/(44r²))<26 since
    # X=1+9/(44r²)< exp17 and ln2<1.
    X=1+fourier_second_moment
    assert X==F(150994955,11)
    exp17_partial=sum((F(17)**k/factorial(k) for k in range(41)),F(0))
    assert X<exp17_partial and 8+1+17==26
    # Genuine ORIGINAL seven-prime absolute form operator norm
    # <=TWOC<8, without any source support vanishing claim for f.
    assert TWOC<F(70751,10000)<8
    assert 26+8==34
    assert 0<MU<34
    return X


def independent_rational_finite_projection_regression():
    """True linear-algebra identity: δ=||Proj_ker H g||.

    Toy only, never substituted for original 470x471 H and g.
    Rational 3x4 H with one pole row, 1D kernel
    span{(0,0,1,-1)} and g=(0,0,2,0):
    P g=(0,0,1,-1), δ²=2.
    If a general positive physical form E=beta*d||a||²,
    the projected source inverse variational correction exactly
    delta²/(beta*d); this checks all factors, not original M/E.
    """
    H=((F(1),F(0),F(0),F(0)),
       (F(0),F(1),F(0),F(0)),
       (F(0),F(0),F(1),F(1)))
    g=(F(0),F(0),F(2),F(0))
    p=(F(0),F(0),F(1),F(-1))
    assert all(sum((x*y for x,y in zip(row,p)),F(0))==0 for row in H)
    delta2=sum((x*x for x in p),F(0))
    assert delta2==2
    M=sum((x*y for x,y in zip(g,p)),F(0))
    assert M==delta2
    E=34*D*delta2
    Rtrial=M*M/E
    assert Rtrial==delta2/(34*D)
    # Scalar minimized pole-neutral (true pole overlap=0) quadratic
    A,u=F(1),F(1,2)
    val=A+2*u*u-Rtrial
    t=-M/E
    direct=A+2*u*u+2*t*M+t*t*E
    assert direct==val
    return delta2,Rtrial


def run():
    data=json.loads((ROOT/"research/obligations.json").read_text())
    o={v["id"]:v for v in data["obligations"]}
    assert data["active_obligation"]=="W-EVEN-FORM"
    assert all(o[k]["status"]=="open" for k in (
        "W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert all(x in o["W-EVEN-FORM"]["evidence"] for x in ("EF27","EF28"))
    centers,orders,xs=original_source_and_geometry()
    X=exact_bell_l2_and_energy()
    dt,rt=independent_rational_finite_projection_regression()
    print("EF28 original native SI10 source:",len(centers),"clusters",
          sum(orders),"true even source Taylor rows; +1 original"
          " cosh(x/2) pole row =",TOTAL_ROWS,"constraints,",
          COUNT,"disjoint even physical cosine6 bell pairs,",
          2*COUNT,"individual lobes.",flush=True)
    print("EF28 fixed ORIGINAL support x_l=(l+1)/512,",
          "l=0..470, r=1/8192; first",xs[0],"last",xs[-1],
          "all strictly in I and physically disjoint.",flush=True)
    print("EF28 EXACT true native physical weighted Euclidean norm:",
          "||sum_l a_l phi_l||²=d*sum_l a_l², d=",D,
          "; ||f'||²/(pi²||f||²)=9/(11r²).",flush=True)
    print("EF28 original arch+prime q0 physical ENERGY UPPER",
          "forall f in the 471-bell span: q0(f,f)<34||f||².",
          "Exact source X=1+9/(44r²)=",X,
          "< original exp17 rational partial sum,",
          "prime norm TWOC<8; no false prime cancellation.",flush=True)
    print("EF28 EXACT original source+pole cofinite existence:",
          "for ANY genuine real 470x471 SI10 moment matrix Htilde,",
          "dim ker Htilde>=1, so nonzero compact C5 even f",
          "satisfies all original 469 source constraints AND",
          "<cosh(x/2),f>=0 exactly.",flush=True)
    print("EF28 ORIGINAL moment-matrix entries are analytic:",
          "H[(j,k),l]=int phi_l(x)*x^k * cos(2*pi*c_j*x)"
          " [k even] or sin(2*pi*c_j*x) [k odd];"
          " pole row=cosh(x_l/2) up to common positive J_r(1/2).",
          " Equivalently derivative of H_r(xi)*cos(2*pi*xi*x_l).",
          flush=True)
    print("EF28 EXACT finite acceptance gate:",
          "g_l=q0(e,phi_l) ORIGINAL signed source;",
          "delta=dist(g,range Htilde^T). If delta>0,"
          " original R(e)>=delta²/(34*d)."
          " An actual NEGATIVE even direction follows if"
          " delta²>34*d*(A+2*u²), A=q0(e,e), u=<c,e>.",
          " Original delta and A NOT evaluated!",flush=True)
    print("EF28 independent exact Fraction projection toy",
          "delta²=",dt,"R=",rt,"PASS; TOY NEVER"
          " promoted to original signed source witness.",flush=True)
    print("EF28 SCOPE: No 470x471 numerical source moment/kernel"
          " or original signed g values; matrix condition and delta"
          " UNKNOWN; complete original finite even 469D Schur,"
          " odd/whole Weil/RH OPEN.",flush=True)


if __name__=="__main__":
    run()
