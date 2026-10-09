#!/usr/bin/env python3
"""DNE11 actual native constant-mode source norm, NONCERTIFIED numeric probe.

Uses untruncated exact CC56 physical source, all prime powers 2,3,4,5,7,8,
both translations and both positive-even pole functionals. Splits the
physical integral at ALL prime panel boundaries, and leaves endpoint
logarithms untruncated. No interval enclosure, full E112 projection, or
full high Schur certificate is claimed. Requires mpmath.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
PINNED=ROOT/"notes/data/RPB108_CC40_NATIVE_PARITY_LOW2_INPUT_20261008.json"

def probe(dps=65):
    mp.mp.dps=dps
    a=mp.mpf(53)/50
    primes=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2))
    terms=[(mp.log(p)/mp.sqrt(n),mp.log(n)) for n,p in primes]
    a0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
    def J(t):
        q=mp.exp(-t/2)
        return mp.atanh(q)+mp.atan(q)
    def parts(x):
        arch=a0+J(a-x)+J(a+x)
        prime=-sum((c*(int(-a < x+ell < a)+int(-a < x-ell < a))
                    for c,ell in terms),mp.mpf(0))
        pole=8*mp.sinh(a/2)*mp.cosh(x/2)
        return arch,prime,pole
    cuts=sorted(set([-a,mp.mpf(0),a]+
                    [s for _,ell in terms for s in (ell-a,a-ell)
                     if -a<s<a]))
    arch=prm=pole=norm_h=norm_q=mp.mpf(0)
    norm_arch=norm_prime=norm_pole=norm_prime_pole=mp.mpf(0)
    for lo,hi in zip(cuts,cuts[1:]):
        arch+=mp.quad(lambda x:parts(x)[0],[lo,hi])
        prm +=mp.quad(lambda x:parts(x)[1],[lo,hi])
        pole+=mp.quad(lambda x:parts(x)[2],[lo,hi])
        norm_h+=mp.quad(lambda x:(parts(x)[0]+parts(x)[1])**2,[lo,hi])
        norm_q+=mp.quad(lambda x:sum(parts(x))**2,[lo,hi])
        norm_arch+=mp.quad(lambda x:parts(x)[0]**2,[lo,hi])
        norm_prime+=mp.quad(lambda x:parts(x)[1]**2,[lo,hi])
        norm_pole+=mp.quad(lambda x:parts(x)[2]**2,[lo,hi])
        norm_prime_pole+=mp.quad(lambda x:(parts(x)[1]+parts(x)[2])**2,[lo,hi])
    h00=(arch+prm)/(2*a)
    q00=(arch+prm+pole)/(2*a)
    norm_h/=2*a;norm_q/=2*a
    norm_arch/=2*a;norm_prime/=2*a;norm_pole/=2*a
    norm_prime_pole/=2*a
    comparisons=None
    if PINNED.is_file():
        pinned=json.loads(PINNED.read_text())
        g=int(pinned["grid_denominator"])
        row=pinned["source_intervals"]["0,0"]
        def in_interval(v,names):
            low=sum((int(row[k][0]) for k in names))
            high=sum((int(row[k][1]) for k in names))
            return mp.mpf(low)/g <= v <= mp.mpf(high)/g
        comparisons=dict(
            H00_in_pinned_nf12_interval=in_interval(h00,("arch","prime")),
            Q00_in_pinned_nf12_interval=in_interval(q00,("full",))
        )
    def strv(v):return mp.nstr(v,42)
    return dict(stage="DNE11 exact-original-source scalar numerical probe",
                category="NONCERTIFIED_NUMERICAL_SANITY_CHECK",
                dps=dps,aperture="53/50",integration_subintervals=len(cuts)-1,
                h00=strv(h00),q00=strv(q00),
                physical_source_H_e0_squared=strv(norm_h),
                physical_source_Q_e0_squared=strv(norm_q),
                physical_arch_source_e0_squared=strv(norm_arch),
                physical_prime_source_e0_squared=strv(norm_prime),
                physical_pole_source_e0_squared=strv(norm_pole),
                physical_prime_plus_pole_source_e0_squared=strv(norm_prime_pole),
                doubled_arch_vs_prime_pole_cross=strv(norm_q-norm_arch-norm_prime_pole),
                residual_Q_excluding_E0_ONLY=strv(norm_q-q00*q00),
                residual_H_excluding_E0_ONLY=strv(norm_h-h00*h00),
                compared_against_pinned_NF12=comparisons,
                entire_E112_low_projection_subtracted=False,
                verified_interval_quadrature=False,
                high_response_inverted=False,
                RH_proved=False,lean_certified=False)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--dps",type=int,default=65)
    args=parser.parse_args()
    print(json.dumps(probe(args.dps),indent=2))
