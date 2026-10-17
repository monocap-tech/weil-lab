#!/usr/bin/env python3
"""EF14: direct original even signed physical Rayleigh with rigorous midpoint
quadrature. Strengthens EF11 without returning to false EF06 cap.

For the SAME EF05/EF11 original cosine physical witness, prove a sharper
[0,4] signed m(ξ)|F(ξ)|² integral bound via the midpoint rule and a
GLOBAL certified second-derivative majorant on every rational cell.
The [4,128] fully signed and [128,infinity) tail are inherited from
independently exact-rational EF11; the real positive even pole is paid.
No original all-vector positivity or RH asserted.
"""
from fractions import Fraction as F
from functools import lru_cache

from validate_rpb108_si06_negative_band import (
    B, PI, LN, WEIGHTS, SHIFTS, ACTIVE, prime_interval,
    log_rational_bounds
)
from validate_rpb108_ef05_even_cap_obstruction import (
    DERIVATIVE, supported_even_fourier, absolute_lower, absolute_upper,
    rational_floor, rational_ceil, true_positive_pole_upper
)
from validate_rpb108_ef11_true_signed_even_rayleigh import (
    entire_finite_signed, true_signed_tail
)

N=1024
RIGHT=4
K=64
A=F(1,4)
GAMMA_K=512
# Original m' arch absolute bound:
# |d_y [y²/(u(u²+y²))]|=2yu/(u²+y²)² <= 1/u²,
# sum_{n>=0} (n+1/4)^-2 <= 1/a²+1/a=20.
ARCH_D1=PI[1]*20
PRIME_D1=F(69)
M_D1=ARCH_D1+PRIME_D1
# |d_y² [y²/(u(u²+y²))]|
# =2u|u²-3y²|/(u²+y²)^3 <= 6/u³,
# sum (n+1/4)^-3 <= 1/a³+1/(2a²)=72.
ARCH_D2=6*PI[1]**2*72
PRIME_D2=2*sum(
    (WEIGHTS[n][1]*(2*PI[1]*SHIFTS[n][1])**2
     for n in ACTIVE),F(0))
M_D2=ARCH_D2+PRIME_D2
F_D1=DERIVATIVE
# |F''(xi)|<= (2pi)^2 integral_{-B}^B x² |cos| dx
#               <=8 pi² B³/3.
F_D2=F(8,3)*PI[1]**2*B**3


@lru_cache(None)
def arch_constants():
    """Rigorous 0.57721 < gamma < 0.57722 via harmonic/log enclosure.
    Classical Euler harmonic bound:
    1/[2(n+1)] < H_n - ln(n) - gamma < 1/(2n).
    Hence H_n-ln(n)-1/(2n) < gamma <
          H_n-ln(n)-1/(2(n+1)).
    """
    h=sum((F(1,k) for k in range(1,GAMMA_K+1)),F(0))
    llo,lhi=log_rational_bounds(F(GAMMA_K))
    glo=h-lhi-F(1,2*GAMMA_K)
    ghi=h-llo-F(1,2*(GAMMA_K+1))
    gamma_lo=F(57721,100000)
    gamma_hi=F(57722,100000)
    assert glo>gamma_lo and ghi<gamma_hi,(float(glo),float(ghi))
    lplo,lphi=log_rational_bounds(PI[0])[0],log_rational_bounds(PI[1])[1]
    clo=gamma_lo+PI[0]/2+3*LN[2][0]+lplo
    chi=gamma_hi+PI[1]/2+3*LN[2][1]+lphi
    assert 0<clo<chi
    return clo,chi


@lru_cache(maxsize=4096)
def original_arch_mid(x):
    """Original digamma at rational point, exact outward Euler tail.

    Re psi(1/4+i*pi*x)-ln(pi) =
     -[gamma+pi/2+3ln2+lnpi] + sum_k
      y²/(u_k(u_k²+y²)), y=pi*x.
    The positive summand decreases in u_k; tail lies between its
    integral from K to infinity and that integral plus f(K).
    """
    assert x>=0
    lo_const,hi_const=arch_constants()
    yl=PI[0]*x
    yh=PI[1]*x
    partial_l=partial_h=F(0)
    for k in range(K):
        u=F(k)+A
        partial_l+=yl*yl/(u*(u*u+yl*yl))
        partial_h+=yh*yh/(u*(u*u+yh*yh))
    t=F(K)+A
    integral_lo=log_rational_bounds(1+(yl/t)**2)[0]/2
    integral_hi=log_rational_bounds(1+(yh/t)**2)[1]/2
    endfirst=yh*yh/(t*(t*t+yh*yh))
    low=partial_l+integral_lo-hi_const
    high=partial_h+integral_hi+endfirst-lo_const
    assert low<=high
    return rational_floor(low),rational_ceil(high)


def original_signed_low_midpoint():
    assert 0<F_D1<F(8) and F(0)<F_D2<F(36)
    assert M_D1<F(133) and ARCH_D2<F(4300)
    assert PRIME_D2<F(2000) and M_D2<F(6300)
    step=F(1,N)
    lower=upper=F(0)
    quadrature_budget=F(0)
    multiplier_width_cost=F(0)
    full_count=0
    for i in range(RIGHT*N):
        l=i*step
        mid=l+step/2
        arch_l,arch_h=original_arch_mid(mid)
        prime_l,prime_h=prime_interval(mid)
        ml=rational_floor(arch_l+prime_l)
        mh=rational_ceil(arch_h+prime_h)
        assert ml<=mh
        fmid=supported_even_fourier(mid)
        fl=rational_floor(absolute_lower(fmid))
        fh=rational_ceil(absolute_upper(fmid))
        assert 0<=fl<=fh
        pointlow=ml*fl**2 if ml>=0 else ml*fh**2
        pointhi=mh*fh**2 if mh>=0 else mh*fl**2
        assert pointlow<=pointhi
        # All actual x in a cell: |m'|<=M_D1 and |F'|<=F_D1.
        amp=fh+F_D1*step/2
        mx=max(abs(ml),abs(mh))+M_D1*step/2
        # (m F²)''=m''F² +4m'F F'
        #          +2m((F')²+F F'').
        second=(M_D2*amp**2
                +4*M_D1*amp*F_D1
                +2*mx*(F_D1**2+amp*F_D2))
        # For reflected 2 int_cell:
        # |2 int_cell w - 2 step w(mid)| <= second step³/12.
        loss=second*step**3/12
        lower+=2*step*pointlow-loss
        upper+=2*step*pointhi+loss
        quadrature_budget+=loss
        multiplier_width_cost+=2*step*(pointhi-pointlow)
        full_count+=1
    assert full_count==4096
    return lower,upper,quadrature_budget,multiplier_width_cost


def validate():
    lo,hi,err,width=original_signed_low_midpoint()
    # EF11 high-frequency [4,128] whole-interval enclosures:
    _,_,midlo,midhi,pc,nc,xc=entire_finite_signed()
    taillo,tailhi,archtail=true_signed_tail()
    polehi,overlap=true_positive_pole_upper()
    polelo=2*absolute_lower(overlap)**2
    Qlo=lo+midlo+taillo+polelo
    Qhi=hi+midhi+tailhi+polehi
    assert Qlo<=Qhi and 0<polelo<=polehi
    verdict=("SINGLE_ORIGINAL_POSITIVE" if Qlo>0 else
             "SINGLE_ORIGINAL_NEGATIVE_REQUIRES_AUDIT" if Qhi<0
             else "STILL_INCONCLUSIVE")
    print("EF14 genuine original signed m Fourier second derivative bound:",
          float(M_D2),flush=True)
    print("EF14 true physical Fourier second derivative bound:",
          float(F_D2),flush=True)
    print("EF14 original [0,4] 4096-cell SIGNED midpoint integral:",
          float(lo),float(hi),flush=True)
    print("EF14 low-range Taylor quadrature total error:",
          float(err),flush=True)
    print("EF14 low-range exact multiplier/amplitude midpoint width:",
          float(width),flush=True)
    print("EF14 inherited EF11 original [4,128] signed interval:",
          float(midlo),float(midhi),flush=True)
    print("EF14 inherited EF11 infinite signed tail interval:",
          float(taillo),float(tailhi),flush=True)
    print("EF14 original even positive pole interval:",
          float(polelo),float(polehi),flush=True)
    print("EF14 ACTUAL full original even signed physical Q interval:",
          float(Qlo),float(Qhi),flush=True)
    print("EF14 one-vector classification:",verdict,flush=True)
    print("EF14 PASS: conservative EF06 cap never used; original",
          "even PSD, whole Weil, global bridge and RH OPEN.",
          flush=True)


if __name__=="__main__":
    validate()
