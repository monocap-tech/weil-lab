#!/usr/bin/env python3
"""EF17 — original even Schur: EF16 pole-only shadow information STOP,
and exact residual-energy entry for the genuinely signed mixed map.

Mathematical identity for q_e=q0+2|<c,·>|², V=V_even_b9,
F=V^perp, C0=q0|F>=mu I, B0=q0(F,V), u=P_Vc, v=Q_Vc:

  S_even = (A0-B0* C0^-1 B0)
           + 2/(1+2<v,C0^-1v>) |u-B0* C0^-1v><...|.

No result on the true 469x469 S_even sign follows from pole-only
physical projection, even if A0 and C0 are individually known.

This exact-rational code checks adversarial fixed-data positive and
negative models, the sign and rank-one formula, and the rigorous
mixed-Riesz residual energy-dual error identity. Models are ABSTRACT
INFORMATION COUNTERMODELS, never alternate original Weil operators.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)
GAMMA_SOURCE=F(28698667287,41943040000000)


def schur_data(A,B,C,u,v):
    assert A>0 and C>=MU and u*v!=0
    base=A-B*B/C
    t=u-B*v/C
    alpha=F(2)/(1+2*v*v/C)
    full=base+alpha*t*t
    # Direct full original-shaped form matrix after actual rank-one pole.
    aa=A+2*u*u
    bb=B+2*u*v
    cc=C+2*v*v
    direct=aa-bb*bb/cc
    assert direct==full
    assert 0<alpha<2
    assert cc>0
    return dict(S0=base,t=t,alpha=alpha,S=full,
                determinant=aa*cc-bb*bb,positive_pole=alpha*t*t)


def same_pole_shadow_two_signs():
    # THESE FIXED DATA are the same in both mathematical models:
    # A0, C0, exact u=P_Vc, v=Q_Vc (and all pole-only Hilbert data).
    A=MU/2
    C=MU
    u=v=F(1)
    disconnected=schur_data(A,F(0),C,u,v)
    cancelled=schur_data(A,MU,C,u,v)
    assert disconnected["S"]>0 and disconnected["determinant"]>0
    assert cancelled["S"]<0 and cancelled["determinant"]<0
    assert disconnected["alpha"]==cancelled["alpha"]
    assert disconnected["t"]==1 and cancelled["t"]==0
    assert disconnected["S0"]>0 and cancelled["S0"]<0
    # Even knowing the EXACT original-shaped finite signed diagonal A
    # and exact positive complement C does not determine the sign
    # without its true signed mixed offdiagonal B.
    return disconnected,cancelled


def rank_one_information_limit():
    # In a 2D finite exceptional space, a positive rank-one update
    # leaves every direction orthogonal to t unchanged.
    S00=S11=F(-1)
    t0=F(1);t1=F(2)
    alpha=F(100)
    x0=F(2);x1=F(-1)
    assert t0*x0+t1*x1==0
    original=S00*x0*x0+S11*x1*x1
    corrected=original+alpha*(t0*x0+t1*x1)**2
    assert original==corrected==-5
    return original


def signed_mixed_residual_energy_gate():
    # C0 h=v, true signed mixed functional B0 w; arbitrary Ritz z.
    # Residual r=v-C0 z; error delta=C0^-1 r.
    # ||r||_(C0*)^2 =r²/C0<=rho².
    # ||B0||_(C0*)^2=B0²/C0<=beta².
    # |B0 delta|² <= rho² beta². Equality in one dimension.
    C=MU
    v=F(1)
    B=MU
    z=v/(2*C)
    r=v-C*z
    rho2=r*r/C
    beta2=B*B/C
    error=B*(v/C-z)
    assert error**2 == beta2*rho2
    effective=u=F(1)
    true_t=u-B*v/C
    trial_t=u-B*z
    assert true_t==0
    assert trial_t==F(1,2)
    assert (trial_t-true_t)**2==rho2*beta2
    # This formula remains valid for original infinite F with
    # actual q0-energy norm, certified original form residual rho,
    # and actual mixed functional beta; NONE is measured here.
    return rho2,beta2,error


def main():
    data=json.loads((ROOT/"research/obligations.json").read_text())
    obs={o["id"]:o for o in data["obligations"]}
    assert data["active_obligation"]=="W-EVEN-FORM"
    assert obs["W-EVEN-FORM"]["status"]=="open"
    assert obs["W-ODD-NEG"]["status"]=="open"
    assert obs["W-WHOLE-FORM"]["status"]=="open"
    assert "EF15" in obs["W-EVEN-FORM"]["evidence"]
    assert "EF16" in obs["W-EVEN-FORM"]["evidence"]
    assert GAMMA_SOURCE>MU
    pos,neg=same_pole_shadow_two_signs()
    unchanged=rank_one_information_limit()
    rho2,beta2,error=signed_mixed_residual_energy_gate()
    print("EF17 inherited source-pinned b9 gamma:",float(GAMMA_SOURCE),
          "> mu:",float(MU),flush=True)
    print("EF17 IDENTICAL physical pole and source A0/C0, unknown B0:",
          "model Spositive",pos["S"],"model Snegative",neg["S"],
          "same alpha",pos["alpha"],flush=True)
    print("EF17 cancellation of true effective pole source t:",
          "model1",pos["t"],"model2",neg["t"],flush=True)
    print("EF17 EXACT rank-one cannot fix orthogonal negative mode:",
          unchanged,flush=True)
    print("EF17 exact energy-dual Riesz residual squared, mixed dual squared:",
          rho2,beta2,"effective t error:",error,flush=True)
    print("EF17 SCOPED METHOD INFORMATION STOP: EF16 signed-original "
          "physical pole projection/alpha data alone, EVEN WITH A0,C0, "
          "cannot determine corrected finite Schur sign. Require "
          "ACTUAL original seven-prime/arch pole-FREE signed B0, "
          "whole cofinite C0 resolvent response and residual energy "
          "dual norm to certify effective t. These quantities UNMEASURED. "
          "W-EVEN-FORM, W-ODD-NEG, whole Weil and RH OPEN.",flush=True)


if __name__=="__main__":
    main()
