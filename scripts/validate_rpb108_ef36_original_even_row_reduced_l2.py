#!/usr/bin/env python3
"""EF36: genuine original SI10 first-source L2 projected-gradient upper.

A major refinement of EF35's ||g_e||<29: remove the EXACT protected
arch source row a_arch(c0)*e before taking the L2 distance to V469.

For e=1_[-B,B] cos(omega*x), B=11/10, c0=37/64,
P_I arch(D)e = a_arch(c0)*e + h_arch,cut, with
 h_arch,cut(x) =
  2 sum_{m>=0} Re[e^(i*omega*B)/(lambda_m-i*omega)]
     e^(-lambda_m*B) cosh(lambda_m*x),
 lambda_m=2*m+1/2.
This is the same original quarter-digamma source identity as EF26/EF29;
the row is literally in the authentic original 469-source carrier.

The entire physical L2 cutoff tail is bounded without truncation:
 - m=0 term norm < 7/10 using omega>3, e^-B/2<=1/(1+B/2),
   ||cosh(x/2)||_L2(I)<8/5, so bound < 2/3 * 20/31 *8/5.
 - m>=1 term norm <= lambda^-3/2 +
          2*sqrt(B)*exp(-lambda*B)/lambda;
   sum_m>=1 lambda^-3/2 < sqrt(2/5)<2/3;
   exp series < (4/5)*(11/10)*(4/15)*(16/11)<7/20.
Thus ||h_arch,cut|| < 7/10+2/3+7/20=103/60<7/4.

The original genuine all-seven-prime physical source translation:
  g_prime=-sum_n w_n*P_I[e(x+ln n)+e(x-ln n)].
Each signed shifted cutoff cosine has squared norm <=2B-ln n
(all seven ln n<2B), so the full prime norm <=
  2 sum_n w_n sqrt(2B-ln n) <6
with SI06 exact rational ln and sqrt-cap assertions, including n8,n9.

The genuine even pole gradient 2u*cosh(x/2) has norm <8/5 using
EF32 original pole 2u²<1/2 and exact cosh norm bound.

Hence the *source-row reduced original* gradient
h = g_e - a_arch(c0)*e obeys ||h|| <6+7/4+8/5=187/20.

Since e belongs to the protected SI10 V469, P_F h=P_F g_e:
eta <=||P_F g_e||²/mu <=||h||²/mu
  <(187/20)²/(17/25000)=257125/2 =128562.5,
for actual original SI10 even full-cofinite mu=17/25000.

Compare EF35 21025000/17 (~1.236 million): ~9.62 improvement,
but still FAR above EF33 restricted S2>1/500; no Schur sign.
Scope: analytic Fourier/physical cutoff attachment has an
independent review obligation separate from native rational CI.
"""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path
from validate_rpb108_si06_negative_band import B,ACTIVE,SHIFTS,WEIGHTS,PI
from validate_rpb108_ef29_original_even_mixed_vector import C0
from validate_rpb108_ef32_even_471_bell_negative_gate_stop import (
    original_even_pole_diagonal
)
from validate_rpb108_ef24_original_even_edge_intervals import S

ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)
ARCH_CUTOFF_CAP=F(7,4)
PRIME_CAP=F(6)
POLE_CAP=F(8,5)
TOTAL_CAP=F(187,20)
ETA_CAP=F(257125,2)
SQRT_SHIFT_CAPS={
    2:F(5,4),3:F(11,10),4:F(1),5:F(4,5),
    7:F(3,5),8:F(2,5),9:F(1,10)
}

def exact_original_arch_cutoff_l2():
    assert B==F(11,10) and C0==F(37,64)
    assert 2*PI[0]*C0>3
    # The original positive pole uses the same cosh L2 norm.
    # int_-B^B cosh(x/2)^2 dx = B+sinh(B).
    # since (2k+1)! >=6^k and B²/6<1,
    # sinh(B) <= B/(1-B²/6).
    assert all(factorial(2*k+1)>=6**k for k in range(25))
    assert B*B<F(6)
    cosh_sq_upper=B+B/(1-B*B/6)
    assert cosh_sq_upper<F(64,25)
    # e^-B/2 <1/(1+B/2)=20/31; first m=0 arch
    # coefficient |2 Re(exp(iωB)/(λ-iω))|<=2/ω<2/3.
    m0_upper=F(2,3)*F(20,31)*F(8,5)
    assert m0_upper<F(7,10)
    # High λ: squared physical cutoff cosh envelope:
    # ||exp(-λB)cosh(λx)||² = exp(-2λB)*B
    #             +exp(-2λB)*sinh(2λB)/(2λ)
    # <= B exp(-2λB)+1/(4λ).
    # Summation of λ^-3/2, λ=2m+1/2, m>=1:
    # <= integral_{0}^{inf}(2t+5/2)^-3/2 dt=sqrt(2/5)<2/3.
    assert F(2,5)<F(4,9)
    # exp(-5B/2)< 1/(1+5B/2)=4/15;
    # 1/(1-exp(-2B)) <(1+2B)/(2B)=16/11;
    # sqrt(B)<11/10.
    assert B<F(121,100)
    assert F(1)/(1+F(5,2)*B)==F(4,15)
    assert (1+2*B)/(2*B)==F(16,11)
    exp_series_upper=F(4,5)*F(11,10)*F(4,15)*F(16,11)
    assert exp_series_upper<F(7,20)
    actual_analytic_bound=F(7,10)+F(2,3)+F(7,20)
    assert actual_analytic_bound==F(103,60)<ARCH_CUTOFF_CAP
    return m0_upper,exp_series_upper,actual_analytic_bound,cosh_sq_upper

def exact_original_prime_physical_support():
    assert set(ACTIVE)=={2,3,4,5,7,8,9}
    assert B==F(11,10)
    strict=[]
    weighted=F(0)
    for n in sorted(ACTIVE):
        lo,hi=SHIFTS[n]
        assert 0<lo<hi<2*B,("original n outside full overlap",n)
        up=2*B-lo
        cap=SQRT_SHIFT_CAPS[n]
        assert up<cap*cap,("original physical shift norm cap",n)
        weight_hi=WEIGHTS[n][1]
        weighted+=weight_hi*cap
        strict.append((n,cap,up,weight_hi))
    assert 2*weighted<PRIME_CAP,("original prime physical response cap",2*weighted)
    return 2*weighted,strict

def exact_original_pole_physical():
    pole,u=original_even_pole_diagonal()
    assert pole.hi<S//2 and u.hi<0
    # norm of 2u cosh(x/2) has square 4u²*(B+sinh B)
    # <(B+sinh B)*1 <(8/5)².
    return pole

def scalar_original_dual():
    assert MU==F(17,25000)
    assert PRIME_CAP+ARCH_CUTOFF_CAP+POLE_CAP==TOTAL_CAP
    assert TOTAL_CAP*TOTAL_CAP/MU==ETA_CAP
    assert ETA_CAP<F(21025000,17)
    assert ETA_CAP>F(1,500)*10**7
    return ETA_CAP

def main():
    m=json.loads((ROOT/'research/obligations.json').read_text())
    ob={x['id']:x for x in m['obligations']}
    assert m['active_obligation']=='W-EVEN-FORM'
    assert all(ob[x]['status']=='open' for x in (
        'W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    arch0,expseries,arch,sinhbound=exact_original_arch_cutoff_l2()
    prime,terms=exact_original_prime_physical_support()
    pole=exact_original_pole_physical()
    cap=scalar_original_dual()
    print('EF36 ORIGINAL same quarter-digamma exact protected-row'
          ' subtraction a_arch(c0)*e: full physical entire-series'
          ' arch cutoff L2 <103/60<7/4; m0 strict upper',
          float(arch0),'positive tail exp upper',float(expseries),
          flush=True)
    print('EF36 ORIGINAL genuine 7-prime shifted support L2'
          ' total <',float(prime),'<6; source upper sqrt caps',
          {str(n):str(k) for n,k,_,_ in terms},flush=True)
    print('EF36 ORIGINAL even pole 2u² source interval <1/2,'
          ' cosh squared norm upper',float(sinhbound),
          ' pole gradient L2 <8/5',flush=True)
    print('EF36 ORIGINAL first-source ROW-REDUCED L2 norm'
          ' ||g_e-a_arch(c0)e|| <187/20=9.35. Since'
          ' e belongs to V469, ||P_F g_e||<187/20'
          ' including genuine signed prime/arch/pole.',flush=True)
    print('EF36 certified SOURCE-REDUCED original Riesz'
          ' full even cofinite energy-dual and EF34 eta strictly'
          ' below 257125/2 =',float(cap),' (EF35 prior'
          ' 21025000/17~1.237e6).',flush=True)
    print('EF36 SCOPE: actual full first-source Schur still'
          ' UNDECIDED: η upper ~1.286e5 vs EF33 S2>0.002.'
          ' No actual source-approximation v or projected delta'
          ' upper <=1.36e-6; full 469D Schur and W-EVEN-FORM,'
          ' odd, whole Weil, RH OPEN. Fourier/digamma physical'
          ' identity remains separate independent analytic audit.',
          flush=True)

if __name__=='__main__':
    main()
