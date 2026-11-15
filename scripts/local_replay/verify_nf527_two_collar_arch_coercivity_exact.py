#!/usr/bin/env python3
"""NF527 exact rational gates for archimedean coercivity on two endpoint collars.

Mathematical gamma series, Fourier Plancherel, compact EF and original source
graph convergence are *analytic premises*, NOT executed/Lean-compiled here.
"""
import argparse,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F

B=F(11,10); delta=F(1,500); m=2*delta

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True)
    a=p.parse_args()
    # exp lower Taylor sums prove log2<7/10, log(pi)<6/5 using pi<22/7.
    assert sum((F(7,10)**k/F(math.factorial(k)) for k in range(4)),F(0))>2
    assert sum((F(6,5)**k/F(math.factorial(k)) for k in range(4)),F(0))>F(22,7)
    # EulerGamma<1, pi<22/7, 3log2<21/10, logpi<6/5.
    C0bound=F(1)+F(11,7)+F(21,10)+F(6,5)
    assert C0bound==F(411,70) and C0bound<F(59,10)
    y=F(15)
    gain=sum((y*y/((F(k)+F(1,4))*((F(k)+F(1,4))**2+y*y)) for k in range(20)),F(0))
    assert gain>F(67,10)
    assert F(67,10)-F(59,10)==F(4,5)
    # low Fourier energy is bounded by (30*m/pi)||f||² and pi>3.
    assert m==F(1,250)
    low_fraction=30*m/F(3)
    assert low_fraction==F(1,25)
    arch=F(4,5)*(1-low_fraction)-F(59,10)*low_fraction
    assert arch==F(133,250)
    # Exact prime selection n=9 is inherited from NF526.
    # log3<6/5 => lambda(9)/sqrt(9)<2/5; Cauchy overlap <||f||²/2.
    prime=F(2,5)
    # exp(B/2)<2, m support => two-pole Hermitian cross <8m||f||².
    pole=8*m
    assert pole==F(4,125)
    margin=arch-prime-pole
    assert margin==F(1,10) and margin>0
    # Original source nonzero certificate uses NF523's U(B)<-1e-11,
    # c'(d)<7e-4; no original 400-source data replay is performed.
    h=F(1,10**9); c0=F(5,10**12); derivative=F(7,10**4)
    assert c0-h*derivative>F(4,10**12)
    norm2=2*h*F(4,10**12)**2
    assert norm2==F(4,125*10**30)
    out={
      'pass':'NF527-two-collar-arch-coercivity-fraction-gates',
      'date':'2026-11-15 PT',
      'scope':'Exact rational inequalities; gamma series Fourier and original NF524/NF526 bridge ANALYTIC NOT COMPILED',
      'source_B':str(B), 'source_delta':str(delta), 'source_measure':str(m),
      'gamma_C0_bound':str(F(59,10)), 'gamma_gain_20_term_t30':str(gain),
      'gamma_gain_min':str(F(67,10)), 'arch_lower_per_L2_sq':str(arch),
      'only_original_prime_power':9, 'prime_upper_per_L2_sq':str(prime),
      'pole_upper_per_L2_sq':str(pole),'full_Weil_signed_lower_per_L2_sq':str(margin),
      'original_source_norm2_min_conditional_on_NF523':str(norm2),
      'original_signed_scalar_min_conditional_on_NF524_NF526':str(margin*norm2),
      'original_NF494_SHA256':'39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181',
      'original_U400_replayed_in_NF527':False,'new_Lean_compilation':False,
      'dedicated_GitHub_CI':'OPEN','RH':'OPEN','W_ODD_NEG':'OPEN'
    }
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
