#!/usr/bin/env python3
"""EF27: original even pole-aware 2x2 source/cofinite Schur audit.

For native original first SI10 even source e and EF21-26 fixed f=F_h psi,
true pole-free signed A=q0(e,e), M=q0(e,f)<0, E=q0(f,f)>0.
True even physical pole c(x)=cosh(x/2):
  q_even=q0+2|<c,.>|²,
  u=<c,e>, v=<c,f>.
On span{e,f}, exact corrected Schur:
  S2=A-M²/E + [2/(1+2v²/E)]*(u-M*v/E)².

Original source, SI10 cofinite lower, EF25 physical upper and native
EF26 signed M give:
  0.48 < 2u² <0.50 (original first-source pole itself),
  0.46 < correction Delta <0.51 for THIS f,
  |v|<10^-700 from native original positive real-Laplace FIR,
  ||f||>10^186 using the ORIGINAL 340-digit a210 coefficient,
  |M*v/E|<10^-880, v²/E<10^-1700.
The above compare a full positive pole correction with the inverse
correction on ONE selected cofinite test, NOT the full 469D Schur.

Strong original first-source arch source ||a(D)e||<47 and
original 7-prime ||P||<=TWOC plus ||e||<3/2 give |A|<87.
Inherited EF24 arithmetic inverse upper and EF25 arch bound yield
0< M²/E <3.3*10^6, while EF26 provides >10^-193.
This ENORMOUS span cannot decide S2, let alone full finite S_even.

Exact Fraction/outward original source gates and an independently
verified rational 2x2 Sherman-Morrison identity are CI-checked.
Original analytic/form-domain and full Riesz/custody audit remain OPEN.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from validate_rpb108_si06_negative_band import B, PI as PI_SOURCE, TWOC
from validate_rpb108_si12_even_supported_inverse import sinh_bounds, cosh_bounds
from validate_rpb108_ef21_original_even_fixed_bell import R,H,N
from validate_rpb108_ef24_original_even_edge_intervals import (
    I, S, PI, recurrence_211_native, trig_pi
)
from validate_rpb108_ef26_original_even_arch_laplace import (
    actual_source,actual_laplace_filter,cosh_i,laplace_bell
)

ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)
C0=F(37,64)


def original_first_source_pole():
    # Exact original e(x)=cos(2*pi*c0*x) on [-B,B].
    # Source pole c(x)=cosh(x/2).
    # u=2[(1/2)sinh(B/2)cos(omega*B)+
    #       omega*cosh(B/2)sin(omega*B)]/(1/4+omega²)
    slo,shi=sinh_bounds(B/2)
    clo,chi=cosh_bounds(B/2)
    cth,sth=trig_pi(2*B*C0)
    assert cth.hi<0 and sth.hi<0
    omega=2*PI*C0
    numerator=2*(I.rational_bounds(slo,shi)*cth/2+
                 omega*I.rational_bounds(clo,chi)*sth)
    u=numerator/(F(1,4)+omega*omega)
    pole=2*u*u
    assert -F(1,2)*S<u.lo<=u.hi<-F(49,100)*S
    assert F(48,100)*S<pole.lo<=pole.hi<F(1,2)*S
    return u,pole


def original_f_pole_smallness():
    # Entire 469-factor native FIR positive real-Laplace response
    # at lambda=1/2. EF26 source script represents
    # Lambda_tilde=100^469*Lambda, not the original raw Lambda.
    a,coss,orders,cth,sth=actual_source()
    lam=I.rational(F(1,2))
    filt=actual_laplace_filter(lam,coss,orders)
    bell=laplace_bell(lam)
    vtilde=filt*cosh_i(lam*a)*bell
    assert vtilde.lo>0
    assert vtilde.hi<10**238*S, (
        "source v unexpectedly too large",vtilde.scaled())
    # Since 100^469=10^938 exactly, 0<v<1e-700.
    # This is the overlap of c with this SELECTED f,
    # not with the entire cofinite source complement.
    return vtilde


def original_physical_f_floor():
    coeff=recurrence_211_native()
    a210=coeff[210]
    assert a210.lo>0
    norm_floor=F(231,512)*R*F(a210.lo,S)**2
    assert norm_floor>F(10**372)
    return a210,norm_floor


def source_variational_and_pole_gates():
    u,pole=original_first_source_pole()
    vtilde=original_f_pole_smallness()
    a210,norm_floor=original_physical_f_floor()

    # First source ||e||²<=2B<9/4.
    # Original arch first-source bound 47 from EF25; true prime
    # physical multiplier op norm <=TWOC native SI06.
    # Thus |q0(e,f)| <(47+TWOC*3/2)||f||<58||f||.
    assert 2*B<F(9,4)
    assert TWOC<F(70751,10000)
    assert 47+TWOC*F(3,2)<58
    # Original E>=MU||f||². For THIS candidate f,
    # |M*v/E|<58/MU * |v|/||f||
    # <58/MU*10^-(700+186)<10^-880.
    mv_upper=F(58,1)/MU*F(1,10**886)
    assert mv_upper<F(1,10**880)
    # v²/E<10^-1400 / (MU*10^372) <10^-1700.
    t_upper=F(1,10**1772)/MU
    assert t_upper<F(1,10**1700)

    # u<-.49, so |u-Mv/E| >.49-1e-880 >.48.
    assert F(49,100)-mv_upper>F(48,100)
    delta_lo=2*F(48,100)**2/(1+2*t_upper)
    delta_hi=2*(F(1,2)+mv_upper)**2
    assert delta_lo>F(46,100)
    assert delta_hi<F(51,100)

    # EF26 original M sign<0 and nonzero inverse correction >1e-193.
    # For a broad inverse UPPER:
    # |Mprime|/sqrt(E)<1/20 native EF24;
    # |March|/sqrt(E)<47/sqrt(MU) native EF25.
    # Since sqrt(MU)>47/1810, R<(1810+1/20)^2<3.3e6.
    assert MU>(F(47,1810))**2
    R_upper=(F(1810)+F(1,20))**2
    assert R_upper<3300000
    # A0=q0(e,e): |arch|<=47||e|| <70.5
    # plus original prime source norm <=TWOC||e||² <~15.57,
    # hence |A0|<87, not a sign.
    A_upper=47*F(3,2)+TWOC*2*B
    assert A_upper<87
    print("EF27 TRUE original first even source pole u=<c,e>:",
          u.scaled(),"2u²:",pole.scaled(),flush=True)
    print("EF27 native true selected-f pole charge",
          "v*10^938:",vtilde.scaled(),
          "so 0<v<1e-700 (not full complement pole).",flush=True)
    print("EF27 native original a210",a210.scaled(),
          "physical ||f||² lower > 10^372 (exact rational)",flush=True)
    print("EF27 signed source/pole residual bounds:",
          "|M v/E|<1e-880, v²/E<1e-1700; exact",
          "2x2 pole-corrected Schur update Delta in (0.46,0.51).",
          flush=True)
    print("EF27 TRUE ORIGINAL first-source pole-free A0 bound:",
          "|A0|<87. Selected inverse correction R in",
          "(1e-193,3.3e6) from inherited EF26/EF24/EF25.",
          "No S2 sign can be asserted.",flush=True)


def exact_two_by_two_identity():
    # Sanity proof algebra for independent rational data:
    # S+=(A+2u²)-(M+2uv)²/(E+2v²)
    #   = (A-M²/E)+2/(1+2v²/E)*(u-Mv/E)².
    cases=[
        (F(11,3),F(-7,5),F(13,4),F(-2,7),F(3,8)),
        (F(-5,6),F(8,9),F(5,2),F(4,3),F(-2,5)),
        (F(0),F(1),F(3),F(1,3),F(0)),
    ]
    for A,M,E,u,v in cases:
        assert E>0
        left=A+2*u*u-(M+2*u*v)**2/(E+2*v*v)
        right=A-M*M/E+2*(u-M*v/E)**2/(1+2*v*v/E)
        assert left==right
    return len(cases)


def run():
    data=json.loads((ROOT/"research/obligations.json").read_text())
    obs={x["id"]:x for x in data["obligations"]}
    assert data["active_obligation"]=="W-EVEN-FORM"
    assert all(obs[x]["status"]=="open" for x in (
        "W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert "EF27" in obs["W-EVEN-FORM"]["evidence"]
    count=exact_two_by_two_identity()
    assert count==3
    source_variational_and_pole_gates()
    print("EF27 EXACT finite 2x2 signed pole Schur identity:",
          count,"independent Fraction cases PASS;",
          "no full finite 469D spectrum/PSD/RH.",flush=True)


if __name__=="__main__":
    run()
