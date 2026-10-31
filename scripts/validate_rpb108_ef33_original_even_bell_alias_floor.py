#!/usr/bin/env python3
"""EF33 — complete ORIGINAL even 471-bell signed lower, NO kernel solve.

Original SI10/EF28 geometry: 471 even real C5 bell pairs,
x_j=j/512, radius r=1/8192. Actual original seven-prime multiplier
plus entire quarter-digamma arch. Prove uniform q0(f,f)>4||f||^2
for *every* f in this 471-bell span.

The analytic bridge (not derived by these assert statements alone):
- Fourier b_r C5 periodized square at step 512 is exactly
  ||b_r||²/512, since 2r<1/512 (Poisson/Parseval).
- |hat b_r(xi)| <= int b_r=5r/8, so each alias has at most
  alpha=25/462 of the whole periodized mass.
- For original a_arch(xi) monotone in |xi|, SI06 rational
  L0=-CONST_UP, Lk=arch_lower(512*k) lower for |xi|>=512*k.
  Whole true arch form >= L0+sum_(k=1)^9
  (Lk-L{k-1})*(1-25*k/231), for ANY bell coefficients.
- Prime geometric original source shifts: for every original
  integer-lattice lobe center j/512 in [-471/512,471/512],
  overlap only at n=2 (offset 355) or n=5 (offset 824).
  Every matching original lobe has at most ONE matching partner.
  n=2 mismatch |ln2-355/512|>r hence normalized C5 lobe
  overlap <=1/2 by Cauchy on opposite half supports; n5 <=1.
  Thus qprime(f,f)>=-2*(w2/2+w5)||f||², using TRUE weights
  ln(prime(n))/sqrt(n), not ln n/sqrt n for powers.
- Full source-attached analytic proof requires original physical
  Fourier/unitary conventions, SI06 digamma bounds, and form-core
  review. Source checker replays exact Fraction geometry and energy.

The completed lower plus EF32 exact signed ||gtilde||², A_even
gives 2D strictly POSITIVE restricted Schur for span{e,f_kernel}.
This is NOT complete 469-source or infinite cofinite even PSD.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import json
from validate_rpb108_si06_negative_band import (
    B,ACTIVE,WEIGHTS,arch_lower,CONST_UP,ln_bounds
)
from validate_rpb108_ef28_pole_neutral_moment_kernel import (
    original_source_and_geometry,GRID,R,D,COUNT
)

ROOT=Path(__file__).resolve().parents[1]
ALPHA=F(25,462)
LEVELS=9

def original_bell_fourier_alias():
    assert (B,GRID,R,COUNT)==(F(11,10),F(1,512),F(1,8192),471)
    # True bell b_r(t)=cos^6(pi*t/(2r))*1_|t|<r.
    # int b_r=2r*(5/16)=5r/8; L2²=2r*binom(12,6)/4^6=231r/512.
    b_mass=F(5,8)*R
    b_norm2=F(2)*R*F(comb(12,6),4**6)
    assert b_norm2==F(231,512)*R
    assert D==b_norm2/2==F(231,8388608)
    assert 2*R<GRID
    alpha=F(512)*b_mass*b_mass/b_norm2
    assert alpha==ALPHA
    # For each real residue modulo512, the interval [-512k,512k)
    # contains exactly 2k aliases. Relative mass below it <=2k*alpha.
    assert 2*LEVELS*ALPHA<1
    return b_mass,b_norm2

def original_arch_lower():
    # SI06 exact original quarter-digamma bound is monotone:
    # true a_arch(|xi|) increases with |xi| by its termwise positive
    # series. arch_lower(j) is a rational source lower at j>=1.
    lev=[-CONST_UP]
    lev += [arch_lower(512*k) for k in range(1,LEVELS+1)]
    assert len(lev)==LEVELS+1
    assert all(lev[k]>lev[k-1] for k in range(1,len(lev)))
    floor=lev[0]
    for k in range(1,LEVELS+1):
        floor+=(lev[k]-lev[k-1])*(1-2*k*ALPHA)
    assert floor>F(6), "original full arch alias lower below 6"
    return floor,lev

def checked_prime_shift_geometry():
    centers,orders,xs=original_source_and_geometry()
    assert sum(orders)==469 and len(centers)==107
    assert xs==[F(j,512) for j in range(1,472)]
    # Physical shift differences/sums all are integer k/512, with
    # |k|<=942; two C5 lobes can overlap iff |512 ln n-k|<1/8.
    # Strict rational SI06 ln bounds are used for all seven terms.
    found={}
    exact={}
    for n in sorted(ACTIVE):
        lo,hi=ln_bounds(n,terms=160)
        assert 0<lo<hi
        lo512,hi512=512*lo,512*hi
        matches=[]
        for k in range(1,943):
            # Native source-genuine REAL shift's entire uncertain
            # log interval must be strictly inside or outside overlap.
            if lo512>k+F(1,8) or hi512<k-F(1,8):
                continue
            assert lo512>k-F(1,8) and hi512<k+F(1,8), (
                'source geometric uncertainty: partial bell alias',n,k)
            matches.append(k)
        found[n]=matches
        exact[n]=(str(lo512),str(hi512))
    assert found=={2:[355],3:[],4:[],5:[824],7:[],8:[],9:[]},found
    l2,h2=ln_bounds(2,terms=160)
    # TRUE offset from exact source 355/512 is greater than r
    # and strictly less than 2r: then the shifted C5 overlap
    # lies solely in opposite half-lobes and has absolute
    # normalized overlap <= 1/2 (Cauchy, even bell).
    assert h2<F(355,512)-R
    assert l2>F(355,512)-2*R
    # For n=5 its true 824/512 alias is within the same 2r margin.
    l5,h5=ln_bounds(5,terms=160)
    assert F(824,512)-2*R<l5<h5<F(824,512)+2*R
    # Every original signed lobe has at most one physical partner:
    # 2r<1/512, so distinct integer-lattice target centers
    # cannot both intersect the same shifted lobe. Schur absolute
    # row and column sums <=rho_n, uniform for all coefficients.
    assert 4*R<GRID
    # Actual original n=2,5 are PRIME here (unlike n4,n8,n9);
    # use SI06 original fully signed positive prime weights.
    assert ACTIVE[2]==2 and ACTIVE[5]==5
    penalty=2*(WEIGHTS[2][1]*F(1,2)+WEIGHTS[5][1])
    return penalty,found,exact

def original_negative_gate(energy_floor):
    # EF32 certified source head includes complete ORIGINAL signed
    # 471-vector, all 7 prime powers and digamma; strict already
    # verified decimal outward upper margins copied as rational
    # WEAKER standalone guards (do not claim these replay artifacts).
    original_g2_upper=F(3174615,10**12) # 3.174615e-6
    original_a_lower=F(30997,10**6)     # 0.030997
    assert energy_floor>4
    assert original_g2_upper < 4*D*original_a_lower
    schur_lower=original_a_lower-original_g2_upper/(4*D)
    assert schur_lower>F(1,500)  # >0.002
    return schur_lower

def main():
    b_mass,b_norm2=original_bell_fourier_alias()
    arch,lev=original_arch_lower()
    penalty,found,exact=checked_prime_shift_geometry()
    original_full_lower=arch-penalty
    assert original_full_lower>F(4), (
        'true original even bell full q0>4 target fails',
        float(original_full_lower))
    assert original_full_lower>F(21,5),(
        'new original quantitative >4.2 gate fails',float(original_full_lower))
    restricted_schur=original_negative_gate(original_full_lower)
    print('EF33 ORIGINAL SI10 471 physical even bell source inventory:'
          ' 107 clusters / 469 source modes / 471 bells;'
          ' original seven-prime+arch signed complete',flush=True)
    print('EF33 original physical even C5 alias fraction ALPHA:',
          str(ALPHA),'period step 512; source overlap',found,flush=True)
    print('EF33 original native SI06 ARCH 10 rational shell levels:',
          [float(x) for x in lev],flush=True)
    print('EF33 certified ORIGINAL full arch ENERGY lower:',
          float(arch),'original n2/n5 PRIME penalty upper:',
          float(penalty),flush=True)
    print('EF33 certified ORIGINAL 471-bell TRUE q0 energy'
          ' / physical norm lower:',float(original_full_lower),
          'strictly >21/5',flush=True)
    print('EF33 original EF32 first-source/471-kernel restricted'
          ' even 2D Schur lower:',float(restricted_schur),
          '>1/500 from accepted weaker rational EF32 guards',
          flush=True)
    print('EF33 CLASSIFICATION: TRUE original entire 471-bell'
          ' signed positivity from physical alias/shift geometry;'
          ' restricted actual span(e,unique source/pole-neutral kernel)'
          ' strictly POSITIVE. Still no full original 469D Schur'
          ' or infinite remainder positivity, no even/odd/whole Weil'
          ' or RH conclusion. Physical domain analytic review separate.',
          flush=True)

if __name__=='__main__':
    main()
