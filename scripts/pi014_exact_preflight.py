#!/usr/bin/env python3
"""PI014 exact Fraction coefficient and physical finite-kernel sanity checks.

No complex integration, Zeta23 source import, Lean compilation or operator
trace is verified by this independent arithmetic regression.
"""
from fractions import Fraction as F


def atom(n: int, r: F) -> F:
    a = F(n) + F(1, 4)
    return a / (a*a + (r / 2)**2)


def rational_fourier_atom(n: int, r: F) -> F:
    alpha = 2*F(n) + F(1, 2)
    return 2*alpha / (alpha*alpha+r*r)


def kernel_at_log_square(q: int, N: int) -> F:
    root = int(q**0.5)
    assert q>1 and root*root == q
    return sum((F(1, root*q**(2*n)) for n in range(N)),F())


def run() -> None:
    freqs=(F(-19,3),F(-1),F(-1,101),F(0),F(2,9),F(12,7),F(57))
    a_count=0; s_count=0; k_count=0
    for n in range(256):
        for r in freqs:
            assert atom(n,r) == rational_fourier_atom(n,r)
            assert atom(n,r) == atom(n,-r)
            a_count+=1
    for N in (0,1,2,3,7,16,32,63):
        for r in freqs:
            assert sum((atom(n,r) for n in range(N)),F()) == sum((rational_fourier_atom(n,r) for n in range(N)),F())
            s_count+=1
    for q in (4,9,16,25,36,49):
        root=int(q**0.5)
        K=F(1,root)/(1-F(1,q*q))
        for N in range(40):
            got=kernel_at_log_square(q,N)
            assert got == K * (1-F(1,q**(2*N)))
            k_count+=1
    assert kernel_at_log_square(9,1) == F(1,3)
    assert F(1,3)/(1-F(1,81)) == F(27,80)
    print('PI014 EXACT FRACTION PREFLIGHT PASS')
    print(f'{a_count} rational source Gamma/Fourier atoms; {s_count} finite sums; {k_count} physical kernel values')
    print('NOT verified: Lean, actual Zeta23.paperFT import, complex Fourier integrals, contact/trace, RH')


if __name__=='__main__':
    run()
