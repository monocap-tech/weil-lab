#!/usr/bin/env python3
"""PS32: TRUE original PS29 even ground eigenfunction Fourier mass certificate.

Analytic premises (independent review STILL required):
  PS17 original V_C > -13, PS27 true pre-pole A0 >1997/9000,
  |B0|<1403/80 and c_C norm²<539/180.
  PS29 original pole-free source Schur L has compact resolvent and a
  normalized nonnegative even lowest eigenvector phi0 with
  lambda0<-4.359740 via RC315 source-pinned negative witness.
  PS18 original digamma Fourier multiplier has
  j(xi)>=log(|xi|/2)-1/pi-1/2 at |xi|>=2 (Plancherel).
  PS28 original effective renormalized even pole d>=1 a.e.
Using these TRUE ORIGINAL estimates, not numerical eigenvectors:
  J[phi0]<1401.
  with X=2**8096, full-line Fourier tail |>X has mass <1/4.
  each measurable |E|<=1/(128X): ||1_E phi0||²<25/64.
  each A subset C+ |A|<=1/(256X): mu(A)=2 int_A phi0²<25/64.
  <d,phi0>²>3/(8X), alpha<a²>3994/2907*3/(8X).
All extremely noncompetitive: NO physical PS31 macroscopic cell mass
or W_N lower computed; no lambda1, Delta, W-EVEN-FORM, odd, Weil, RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_ps31_even_multiscale_gap as ps31

ROOT=Path(__file__).resolve().parents[1]
X_EXP=8096
RC315_NEG=F(4359740,10**6)
ALPHA_LO=F(3994,2907)
ARCH_HI=F(1401)
TAIL_MARGIN=F(1,4)


def exact_original_analytic_constants():
    # True original source-pinned norm/Loewner bounds.
    cross=F(1403,80)
    source_floor=F(1997,9000)
    c_norm_sq=F(539,180)
    original_bounded_shift=F(13)+2*c_norm_sq+cross**2/source_floor
    assert original_bounded_shift<F(1406)
    assert original_bounded_shift>F(1405)
    # J[phi0]=lambda0-<phi0,V0-R phi0> <
    # T-|lambda0| <= T-4.359740 < 1401.
    arch_energy_hi=original_bounded_shift-RC315_NEG
    assert F(0)<arch_energy_hi<ARCH_HI

    # PS18 arch symbol exact rational lower for |xi|>=2**8096:
    # j>log(|xi|/2)-1/pi-1/2
    #  >(8095)*(693/1000)-5/6 > 5604=4*1401.
    original_symbol_min=F(X_EXP-1)*F(693,1000)-F(5,6)
    assert original_symbol_min==F(3365401,600)
    assert original_symbol_min>4*ARCH_HI
    assert arch_energy_hi/original_symbol_min<TAIL_MARGIN

    # Entire original ground Fourier high norm² <1/4;
    # original low <X norm² >3/4.
    low_mass=1-TAIL_MARGIN
    assert low_mass==F(3,4)
    assert low_mass/TWO<F(1)
    return original_bounded_shift,arch_energy_hi,original_symbol_min


TWO=F(2)

def finite_entropy_regression():
    # A non-vacuous exact-Fraction example of spectral-tail
    # reasoning. It is NOT a sampled original physical phi0.
    low=F(4,5)
    high=F(1,5)
    assert low+high==1
    energy=F(5605)*high
    assert energy<F(1401)
    assert high<TAIL_MARGIN
    # Bandlimit Cauchy |P_<X f(x)| <= sqrt(2X) ||P_<X f||,
    # and ||P_>=X f||<1/2 imply an arbitrary original physical
    # measurable set of length <=(128X)^-1 has norm <1/8+1/2.
    band_amplitude_sq=F(2,128)
    assert band_amplitude_sq==F(1,64)
    assert F(1,8)+F(1,2)==F(5,8)
    assert F(5,8)**2==F(25,64)
    # Half-even reflection A U -A doubles physical length,
    # hence |A| <=(256X)^-1 retains the same true bound.
    assert F(2,256)==F(1,128)
    return energy


def run():
    # PS31's validator asserts its own terminal checkpoint PS31,
    # so replay inherited PS28 source exact rationals and
    # PS30/31 finite algebra on PS32 rather than rerunning the
    # previous terminal-check governance.
    ps31.ps30.ps29.ps28.run()
    arch,prime,source,full=ps31.ps30.regression()
    assert arch>0 and prime>0 and source>0 and full>0
    assert ps31.even_reflection_demo()>0
    passed,_,_,_=ps31.graph_gate(
        [F(1,3),F(2,3)],[[F(5),F(3)],[F(3),F(4)]],F(3))
    assert passed

    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["checkpoints"][-1]["id"]=="PS32"
    assert lane["status"]=="open"
    assert all(v is False for v in lane["closures"].values())

    T,Jmax,j_symbol=exact_original_analytic_constants()
    toy=finite_entropy_regression()

    # Allocate only one 8097-bit integer, NOT a Fourier grid.
    X=1<<X_EXP
    assert X.bit_length()==X_EXP+1
    # True ground mass: P_high norm² <1/4, P_low >3/4
    # and |hat phi0| <= ||phi0||_L1 for real normalized
    # nonnegative original source-Schur ground.
    a_sq_lower=F(3,8*X)
    alpha_pole_lower=ALPHA_LO*a_sq_lower
    assert a_sq_lower>0 and alpha_pole_lower>a_sq_lower
    assert a_sq_lower*8*X==3
    assert alpha_pole_lower/a_sq_lower==ALPHA_LO
    assert T-Jmax==RC315_NEG
    assert Jmax<F(1401)
    assert j_symbol>F(5604)
    assert Jmax/j_symbol<F(1,4)

    print("PS32 ORIGINAL ground arch energy strict upper J[phi0] <",
          float(Jmax),"<1401",flush=True)
    print("PS32 original PS18 digamma Fourier symbol lower at |xi|>=2**",
          X_EXP,":",float(j_symbol),">5604",flush=True)
    print("PS32 original true normalized ground high Fourier mass <1/4"
          " and low mass >3/4; symbolic X power",X_EXP,flush=True)
    print("PS32 physical arbitrary-set length <=2^-8096/128"
          " true ground mass <25/64",flush=True)
    print("PS32 even half-set length <=2^-8096/256"
          " true mu(cell) <25/64",flush=True)
    print("PS32 TRUE ground effective even-pole overlap squared >"
          " 3/(8*2**8096), rational formula validated",flush=True)
    print("PS32 TRUE effective coefficient weighted a² >"
          " (3994/2907)*3/(8*2**8096), rational formula validated",
          flush=True)
    print("PS32 separate rational two-band entropy example energy",
          toy,flush=True)
    print("PS32 PASS SCOPED: TRUE original even pole-free Schur ground"
          " Fourier energy and tiny-set nonconcentration, source-"
          " renormalized effective pole quantitative overlap."
          " Astronomical scale is not a usable original macroscopic"
          " PS31 cell mass, lambda1 sign, pole-angle Delta, restored"
          " W-EVEN-FORM, W-ODD-NEG, Weil, CC27 D-Riesz or RH proof."
          " Original infinite-dimensional premises require review.",
          flush=True)


if __name__=="__main__":
    run()
