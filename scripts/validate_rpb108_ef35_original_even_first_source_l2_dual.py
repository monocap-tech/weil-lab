#!/usr/bin/env python3
"""EF35 rigorous original FIRST SI10 even source L2 response / dual cap.

This checker validates exact rational constants in an analytic proof.
It neither calculates an inverse cofinite response nor the actual eta.

Original source e=1_[-B,B]cos(2pi c0 x), B=11/10,c0=37/64.
Original signed form a_arch(xi)=Re psi(1/4+i*pi*xi)-ln pi,
m_prime(xi)=-2 sum_{n=2,3,4,5,7,8,9} (ln p)/sqrt(n)
                       cos(2pi xi ln n),
plus genuine positive even pole 2|<cosh(x/2),e>|².

Analytic source lemma:
 a_arch=-C+sum_{k>=0} y²/((k+1/4)((k+1/4)²+y²)),
 y=pi*|xi|, 0<C<CONST_UP<6.
 Sum k0 <=4. For 0<=y<1, k>=1 sum <=3/2.
 For y>=1, N=floor(y), sum_{1..N}1/k<=1+log(y),
 sum_{k>N}y²/k³<=y²/(2N²)<2.
 So |a_arch(xi)|<=7+log(1+4|xi|), globally.

First-source Fourier bound:
 ||e||²<11/5<9/4.
 On |xi|<=2, |a_arch|<10 since log9<3.
 On |xi|>=2, |a_arch|<9+log|xi| since log5<2,
 and |e_hat|<=10/(21|xi|) by c0<3/5 and pi>3.
 Thus ||a_arch(D)e||² <
   100*(11/5)+(100/441)*(100+20+2)<256,
 with exact integration of (9+log t)^2/t^2 from t=2 to inf
 and log2<1. In particular ORIGINAL e is in arch strong L2
 domain (no physical differential order assumption).

Prime ||prime(D)e|| <= TWOC||e|| <11 (SI06 native TWOC<71/10).
Original pole 2u cosh(x/2) has L2 norm <2:
EF32 true 2u²<1/2, cosh(B/2)<6/5, ||e||<3/2
so ||cosh||<9/5. Hence original full gradient
g_e=P_I[m(D)e+2u cosh(x/2)] obeys ||g_e||<16+11+2=29.

Original SI10 lower q_even(v,v)>mu||v||² on
F=V469^perp, mu=17/25000, implies original total
source cofinite energy-dual squared <=||g_e||²/mu<
841*25000/17 = 21,025,000/17. EF34 eta on energy-
orthogonal F1 is <= this cap, but is not near S2>1/500.

A rigorous projected source-approximation sufficient gate:
find ANY real original 469-source combination v such that
||g_e-v||² < mu/500=17/12500000.
Then eta<=||P_F g_e||²/mu<1/500<S2
and the full first-source cofinite Schur is strictly positive.
The norm must be original L2 on I, pole included. This is
an actionable acceptance condition, NOT met at EF35.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import (
    B,TWOC,CONST_UP,PI as SI06_PI
)
from validate_rpb108_ef29_original_even_mixed_vector import C0
from validate_rpb108_ef32_even_471_bell_negative_gate_stop import (
    original_even_pole_diagonal
)
from validate_rpb108_ef24_original_even_edge_intervals import S

ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)
D_DIGAMMA=F(1,4)
ARCH_L2_UPPER_SQ=F(100)*F(11,5)+F(12200,441)
ETA_CAP=F(29**2)/MU
TARGET_ERROR_SQ=MU/F(500)

def exp_lower_bound(x,K):
    return sum((F(x)**k/factorial(k) for k in range(K+1)),F(0))

def certify_original_symbol_and_fourier_envelopes():
    assert B==F(11,10) and C0==F(37,64)
    assert CONST_UP<F(6) and CONST_UP>0
    assert SI06_PI[0]>F(3) and SI06_PI[1]<F(4)
    assert C0<F(3,5)
    # Exact finite rational exp partial sums: log2<1, log5<2,
    # log9<3. No float logarithm trusted for proof.
    for x,v in ((F(1),2),(F(2),5),(F(3),9)):
        assert exp_lower_bound(x,18)>v
    # Source Fourier L2 domain via physical support and Parseval.
    assert F(11,5)<F(9,4)
    # For t>=2, t-c0>=7*t/10, |e_hat|<10/(21 t).
    assert F(2)-C0>F(7,5)
    assert (F(100)*F(11,5)+
            2*F(100,441)*F(100+20+2,2))==ARCH_L2_UPPER_SQ
    assert ARCH_L2_UPPER_SQ<F(256),ARCH_L2_UPPER_SQ
    return ARCH_L2_UPPER_SQ

def certify_original_prime_and_pole_gradients():
    # Inherited SI06 original all-seven arithmetic weight sum.
    assert TWOC<F(70751,10000)<F(71,10)
    assert F(71,10)*F(3,2)<F(11)
    # Original cosh(t) bound by geometric series for |t|<=B/2.
    u=B/2
    bcosh=F(1)/(1-u*u/2)
    assert bcosh==F(800,679)<F(6,5)
    assert bcosh*F(3,2)<F(2)
    pole,uval=original_even_pole_diagonal()
    assert pole.hi < S//2, "EF32 original true pole 2u²<1/2"
    assert uval.hi<0
    # ||2u*cosh||<=sqrt(4u²)||cosh||<2.
    return pole

def certify_dual_cap_and_acceptance():
    assert MU==F(17,25000)
    assert TARGET_ERROR_SQ==F(17,12500000)
    assert ETA_CAP==F(21025000,17)
    assert ETA_CAP>F(10**6)
    assert TARGET_ERROR_SQ<F(1,10**5)
    assert ETA_CAP>F(1,500)*10**8
    # Source geometry: F=orthogonal complement in actual physical
    # L2, q_even coercive on F. Since first e gradient g_e in L2:
    # |q_even(e,v)|=|<g_e,v>| <=||g_e||||v||
    # <=||g_e||/sqrt(mu)*sqrt(q_even(v,v)).
    # Riesz response norm² <=||g_e||²/mu; eta after shorting
    # f* is a part, so eta is bounded by the same quantity.
    # The stronger source approximation gate is exact:
    # since all original protected v have <v,w>=0 on F,
    # ||P_F g_e|| <=||g_e-v||. If <sqrt(mu/500), positive
    # first-source full-cofinite Schur follows from S2>1/500.
    return ETA_CAP,TARGET_ERROR_SQ

def main():
    m=json.loads((ROOT/'research/obligations.json').read_text())
    byid={x['id']:x for x in m['obligations']}
    assert m['active_obligation']=='W-EVEN-FORM'
    assert all(byid[i]['status']=='open' for i in
               ('W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    arch_sq=certify_original_symbol_and_fourier_envelopes()
    pole=certify_original_prime_and_pole_gradients()
    cap,target=certify_dual_cap_and_acceptance()
    print('EF35 original SI10 e L2 strong-domain spectral certificate:'
          ' original entire quarter digamma norm² <',float(arch_sq),
          '<256, all seven prime-power source-gradient norm <11,'
          ' true positive even pole gradient norm <2.',flush=True)
    print('EF35 original first source FULL signed gradient'
          ' ||g_e||_L2(I)<29 (not a finite projection).',flush=True)
    print('EF35 inherited ORIGINAL SI10 even cofinite mu>',
          str(MU), 'Riesz original full first-source energy dual²',
          ' and EF34 unseen residual eta <',str(cap),
          ' (~',float(cap),').',flush=True)
    print('EF35 actionable original positive first-source gate:'
          ' ANY v in original real 469 SI10 protected source span'
          ' with ||g_e-v||_L2(I)² <',str(target),
          '(~',float(target),')'
          ' forces eta<1/500<S2; this approximation has NOT been'
          ' constructed or certified.',flush=True)
    print('EF35 method decision: universal full gradient L2 cap is'
          ' >1e6, while EF33 S2>0.002; insufficient to decide'
          ' original first-source full cofinite Schur. Precise'
          ' missing object is a SOURCE-PROJECTED L2 residual or'
          ' stronger energy-dual response. Complete 469D Schur,'
          ' odd, whole Weil and RH remain OPEN.',flush=True)

if __name__=='__main__':
    main()
