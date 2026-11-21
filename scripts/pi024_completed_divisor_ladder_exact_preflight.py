#!/usr/bin/env python3
"""PI024 exact finite arithmetic audit of the completed/finite zeta divisor seam.

Pure rational identities for a SIGNED point-mass surrogate of the smooth
PI019 derivative-bump phase probes. No zeros are computed, no gamma
function evaluated, no Lean compiled, and no spectral trace proved.

At a=log 9, let lambda_n=2n+1/2 and C=2 delta_0-delta_log4-delta_-log4.
The positive-translation kernel pairing is
  I_N(a)=2 K_N(log9)-K_N(log36)-K_N(log(9/4))
        =sum_{n<N} [2-4^lambda_n-4^-lambda_n]*9^-lambda_n.
Its shifted Laplace transform has poles at s=-lambda_n, namely the shifted
lattice of gamma poles at the finite-zeta arguments beta=-2n.

Those positions are NOT zeros of completed zeta: at beta=0 completed
Lambda has a pole, and for n>=1 the finite-zeta trivial zero cancels
Gamma(beta/2)'s pole. The above mathematical facts are documented from
Masullo sections 3.2 and 7.4 and standard zeta analytic continuation;
this script checks only their finite integer-index bookkeeping.
"""
from fractions import Fraction as Q
from math import isqrt


def rational_sqrt(x: Q) -> Q:
    n,d = isqrt(x.numerator),isqrt(x.denominator)
    assert x>0 and n*n==x.numerator and d*d==x.denominator
    return Q(n,d)


def finite_kernel_at_log_q(q: Q,N:int)->Q:
    assert q>1 and N>=0
    return sum((Q(1)/(rational_sqrt(q)*q**(2*n)) for n in range(N)),Q(0))


def lambda_n(n:int)->Q:
    assert n>=0
    return 2*Q(n)+Q(1,2)


def beta_n(n:int)->int:
    assert n>=0
    return -2*n


def gamma_ladder_weight_at_log9(n:int)->Q:
    # Exactly: 4^lambda_n=2*16^n, 9^-lambda_n=1/(3*81^n)
    u=2*Q(16)**n
    return (2-u-Q(1)/u)/(3*Q(81)**n)


def gamma_ladder_sum(N:int)->Q:
    return sum((gamma_ladder_weight_at_log9(n) for n in range(N)),Q(0))


def physical_signed_control(N:int)->Q:
    return (2*finite_kernel_at_log_q(Q(9),N)
        -finite_kernel_at_log_q(Q(36),N)
        -finite_kernel_at_log_q(Q(9,4),N))


def main()->None:
    levels=80
    assert lambda_n(0)==Q(1,2) and beta_n(0)==0
    assert gamma_ladder_weight_at_log9(0)==-Q(1,6)
    assert gamma_ladder_weight_at_log9(1)==-Q(961,7776)
    checked=0
    for n in range(levels):
        lam=lambda_n(n)
        beta=beta_n(n)
        shifted_pole=-lam
        assert shifted_pole==Q(beta)-Q(1,2)
        assert lam==Q(1,2)-beta
        assert shifted_pole <= -Q(1,2)
        assert gamma_ladder_weight_at_log9(n)<0
        # Gamma(s/2) log derivative has residue -1 at s=-2n;
        # finite zeta'/zeta has residue +1 only at n>=1.
        gamma_log_residue=-1
        finite_zeta_log_residue=(1 if n>=1 else 0)
        completed_log_residue=gamma_log_residue+finite_zeta_log_residue
        assert completed_log_residue==(-1 if n==0 else 0)
        checked+=1
    for N in range(levels+1):
        assert gamma_ladder_sum(N)==physical_signed_control(N)
    assert gamma_ladder_sum(1)==-Q(1,6)
    assert gamma_ladder_sum(2)==-Q(1,6)-Q(961,7776)
    # A correction at s=-1/2 cannot remove n=1,2,... poles.
    assert all(gamma_ladder_weight_at_log9(n)!=0 for n in range(1,levels))
    print('PI024 ANALYTIC-ONLY EXACT RATIONAL PREFLIGHT: PASS')
    print(f'{checked} gamma-ladder pole positions and completion-cancellation indices')
    print(f'{levels+1} exact finite physical signed-kernel / pole-weight identities')
    print('First two residues: -1/6 at s=-1/2, -961/7776 at s=-5/2')
    print('Completed-zeta log derivative: pole at beta=0; cancellation at beta=-2n (n>=1)')
    print('No zeta-zero roster, live PDF hash comparison, Masullo trace, Lean, Actions or RH')

if __name__=='__main__':
    main()
