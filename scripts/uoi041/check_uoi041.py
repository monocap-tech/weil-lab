#!/usr/bin/env python3
"""UOI041 reproducibility checks (arithmetic diagnostics, not Lean certification).

The mathematical divergence conclusion uses the classical PNT, not finite computation.
"""
from math import exp, isqrt, log, sqrt


def isprime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def primes_in(lo: int, hi: int):
    sieve = bytearray(b"\x01") * (hi + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(hi) + 1):
        if sieve[p]:
            sieve[p*p::p] = b"\x00" * (((hi - p*p) // p) + 1)
    return [p for p in range(lo, hi + 1) if sieve[p]]


def check_five_collar():
    p, N = 4099, 4096
    assert isprime(p)
    eps = log(p/N)
    delta0, delta4 = 1/1000, 1/(1000*N)
    w = delta4 / 16
    assert 0 < eps + w < delta0
    assert w < delta4/8
    assert 2*w < min(log(p/(p-1)), log((p+1)/p), eps)
    margin = log(p)/sqrt(p)
    assert margin > 0.12
    assert margin > (154834167288/456107421875 - 1/4)
    print("FIVE COLLARS: primality / shift / tiny-width checks PASS")
    print(f"  log(4099/4096)={eps:.15f}; delta4={delta4:.12g}")
    print(f"  ell_5 >= log(4099)/sqrt(4099) = {margin:.12f}")


def check_prime_band():
    eta = 1/4000
    # Finite examples are illustrations, not a proof of the PNT asymptotic.
    for d in range(5, 9):
        N = 8**d
        lo = int(N*exp(-eta))
        hi = int(N*exp(eta))+1
        ps = primes_in(lo, hi)
        S = sqrt(sum(log(p)**2/p for p in ps))
        asymptotic = sqrt(2*eta*log(N))
        w = 1/(10000*N)
        assert w < 1/(1000*N)/8
        assert all(abs(log(p/N))+w < 1/1000 for p in ps)
        assert 4*w < log(hi/(hi-1))
        print(f"d={d:2d} primes={len(ps):5d} exact_Rayleigh_S={S:.8f} PNT_scale={asymptotic:.8f}")


if __name__ == "__main__":
    check_five_collar()
    check_prime_band()
    print("PASS: numeric checks only; no Lean compilation and no finite test proves PNT.")
