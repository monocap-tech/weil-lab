#!/usr/bin/env python3
"""EF32: original signed 471-bell NEGATIVE SUFFICIENT-GATE method STOP.

Uses unchanged EF29 complete 471 original signed interval vector, original
first-source exact q_prime diagonal, original digamma via a real physical
Laplace covariance identity, and TRUE positive even pole.

This certifies delta^2 <= ||gtilde||_2^2 < 34*d*A_even, thereby proving
the EF28/EF31 *specific E<34||f||^2 sufficient negativity gate cannot
fire*. This is not even-sector positivity, a certified actual inverse,
a true original Schur sign, or an upper bound on all cofinite methods.
"""
import json,sys
from fractions import Fraction as F
from math import factorial
from functools import lru_cache
from pathlib import Path
from validate_rpb108_si06_negative_band import B,ln_bounds,log_rational_bounds
from validate_rpb108_ef24_original_even_edge_intervals import I,S,PI,trig_pi
from validate_rpb108_ef26_original_even_arch_laplace import epos,eneg
from validate_rpb108_ef29_original_even_mixed_vector import exp_minus,C0,OMEGA
from validate_rpb108_ef28_pole_neutral_moment_kernel import D,COUNT

N=256
T=2*B
ZERO=I(0)
ONE=I(S)

@lru_cache(maxsize=1)
def exp250_certificate():
    return sum((F(250)**k/factorial(k) for k in range(500)),F(0))>10**100

def rigor_exp_decay(x):
    """Exact real e^(-x); original exp engine below 250, strict tail above."""
    assert x.lo>0
    if x.hi<250*S: return exp_minus(x)
    assert x.lo>=250*S
    # exp(250)>10^100 by this *finite positive rational* Taylor sum.
    assert exp250_certificate()
    return I(0,S//10**100)

def e_covariance_single(n,s0,ct,st):
    """Exact double integral of cos(omega*x)cos(omega*y) exp(-lam|x-y|)
    over original [-B,B]^2; 340-digit outward intervals.
    C(t)=(s0-t/2)cos(omega t) -ct sin(omega t)/(2omega),
    F_n=2 int_0^(2B) e^(-lam*t) C(t)dt.
    """
    lam=I.rational(F(2*n)+F(1,2))
    E=rigor_exp_decay(lam*T)
    d=lam*lam+OMEGA*OMEGA
    jre=(lam*(ONE-E*ct)+OMEGA*E*st)/d
    jim=(OMEGA*(ONE-E*ct)-lam*E*st)/d
    qre=ONE-E*(ct*(ONE+lam*T)+st*OMEGA*T)
    qim=-E*(st*(ONE+lam*T)-ct*OMEGA*T)
    kre=(qre*(lam*lam-OMEGA*OMEGA)-qim*(2*lam*OMEGA))/(d*d)
    return 2*s0*jre-kre-(ct/OMEGA)*jim

def source_diagonal_arch():
    # Quarter-digamma exact original identity:
    # a_arch(xi)=-gamma-ln(pi)+sum_n[1/(n+1)
    #            -(n+1/4)/((n+1/4)^2+(pi*xi)^2)].
    # Inverse Fourier of each rational term is exp[-(2n+1/2)|x|].
    #
    # A_arch=(-gamma-ln pi)||e||^2+
    #            sum_n[||e||^2/(n+1)-<e,K_lambda_n e>].
    # All quantities below have original physical cutoff and source c0.
    ct,st=trig_pi(2*C0*T)
    s0=I.rational(B)+st/(2*OMEGA)
    assert F(11,10)<F(s0.lo,S)<F(s0.hi,S)<F(3,2)
    # Exact gamma inequality 1/(2(M+1)) < H_M-ln M-gamma <1/(2M).
    M=1024
    h=sum((F(1,k) for k in range(1,M+1)),F(0))
    ln2lo,ln2hi=ln_bounds(2,terms=450)
    gl=h-10*ln2hi-F(1,2*M)
    gu=h-10*ln2lo-F(1,2*(M+1))
    assert 0<gl<gu<1
    gam=I.rational_bounds(gl,gu)
    # Native SI06 rational logarithm enclosure monotone at original pi interval.
    lpi_lo=log_rational_bounds(F(PI.lo,S))[0]
    lpi_hi=log_rational_bounds(F(PI.hi,S))[1]
    lpi=I.rational_bounds(lpi_lo,lpi_hi)
    value=(-gam-lpi)*s0
    for n in range(N):
        value=value+s0/F(n+1)-e_covariance_single(n,s0,ct,st)
    # C(t)=autocorrelation of original truncated cosine for t>=0,
    # extended by zero after 2B. C(0)=s0, C(2B)=0;
    # |C'(t)| <= s0*omega+1 on ALL t>=0, hence
    # |<e,K_lambda e>-s0/(n+1/4)| <= L/(2(n+1/4)^2).
    # The difference between 1/(n+1) and 1/(n+1/4) is at
    # most 3/(4(n+1/4)^2). Integral test gives sum_{n>=N}
    # (n+1/4)^-2 <=1/(N-3/4) <1/(N-1).
    lips_upper=F((s0*OMEGA+1).hi,S)
    s0_upper=F(s0.hi,S)
    tail=(F(3,4)*s0_upper+lips_upper/2)/F(N-1)
    assert tail>0 and tail<F(1,40)
    out=value+I.rational_bounds(-tail,tail)
    print('EF32 original digamma A_arch outward:',out.scaled(),
          'tail certificate absolute <',str(tail),flush=True)
    return out,tail,s0

def original_even_pole_diagonal():
    ct,st=trig_pi(2*C0*B)
    z=I.rational(B/2)
    ch=(epos(z)+eneg(z))/2
    sh=(epos(z)-eneg(z))/2
    u=2*(F(1,2)*sh*ct+OMEGA*ch*st)/(F(1,4)+OMEGA*OMEGA)
    assert u.hi<0
    return 2*u*u,u

def main(path):
    doc=json.loads(Path(path).read_text())
    assert doc['vector_count']==471 and doc['rows']==470
    assert doc['digits']==340 and int(doc['scale'])==S
    signed=doc['vector_original_projected_signed_intervals']
    assert len(signed)==COUNT
    maxlohi=[max(abs(int(pair[0])),abs(int(pair[1]))) for pair in signed]
    g2_upper=F(sum(x*x for x in maxlohi),S*S)
    maxg=F(max(maxlohi),S)
    assert all(int(a)<=int(b) for a,b in signed)
    apr=I(*map(int,doc['prime_diagonal_A_prime_interval']))
    assert F(29,100)<F(apr.lo,S)<F(apr.hi,S)<F(31,100)
    arch,tail,s0=source_diagonal_arch()
    pole,u=original_even_pole_diagonal()
    original_even_diag=apr+arch+pole
    lower=F(original_even_diag.lo,S)
    gate_lower=34*D*lower
    print('EF32 EF29 original gtilde max absolute upper:',float(maxg),flush=True)
    print('EF32 ORIGINAL signed 471 gtilde norm squared upper:',float(g2_upper),flush=True)
    print('EF32 original A_prime:',apr.scaled(),'positive even pole:',pole.scaled(),flush=True)
    print('EF32 original A_even source diagonal:',original_even_diag.scaled(),flush=True)
    print('EF32 prior EF28 negative sufficient gate RHS lower:',float(gate_lower),
          'and residual squared upper:',float(g2_upper),flush=True)
    # Prove strict fail on the WHOLE exact original 1D pole/source kernel,
    # using delta^2<=||gtilde||^2, so no kernel conditioning assumption.
    assert lower>F(1,50), 'actual original first-source even diagonal not positive enough'
    assert g2_upper<gate_lower, 'EF28/EF31 34d sufficient method STOP not proved'
    print('EF32 ORIGINAL CERTIFIED METHOD STOP: for EVERY exact original'
          ' 470-row pole/source-neutral 471-bell test, delta^2 <= ||gtilde||^2'
          ' < 34*d*A_even. The original EF28 sufficient negative-even'
          ' gate is impossible with its E<=34d||w||^2 upper budget.',
          'NO sign of actual restricted correction / full even Schur /'
          ' odd / whole Weil / RH.',flush=True)
    if '--output' in sys.argv:
        dest=Path(sys.argv[sys.argv.index('--output')+1])
        dest.parent.mkdir(parents=True,exist_ok=True)
        data={'scope':'EF32 original original-operator EF28 fixed 34d negative sufficient gate METHOD STOP only',
              'parent_ef29_vector':'Actions 41234333164 artifact 13054987778; source regenerated in same run',
              'digits':340,'n_arch_terms':N,'scale':str(S),
              'A_prime_interval_scaled':[str(apr.lo),str(apr.hi)],
              'A_arch_interval_scaled':[str(arch.lo),str(arch.hi)],
              'even_pole_interval_scaled':[str(pole.lo),str(pole.hi)],
              'A_even_interval_scaled':[str(original_even_diag.lo),str(original_even_diag.hi)],
              'arch_omitted_tail_rational':str(tail),
              'gtilde_norm_sq_upper_rational':str(g2_upper),
              'gtilde_max_abs_upper_rational':str(maxg),
              'negative_sufficient_threshold_lower_rational':str(gate_lower),
              'strict_method_stop':True,
              'limitations':'Does not compute delta, actual energy denominator, Schur sign, or RH.'}
        dest.write_text(json.dumps(data,indent=1)+'\n')

if __name__=='__main__':
    assert '--input' in sys.argv, 'Pass exact original EF29 JSON via --input'
    main(sys.argv[sys.argv.index('--input')+1])
