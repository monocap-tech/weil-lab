"""Floating-point feasibility diagnostic only; not interval arithmetic.
Assumes the staged signed-symbol estimates and exact pole annihilation.
Retained moments are counted separately from the two pole functionals.
"""
import math

C = 20 + abs(math.log(math.pi)) + math.log(6)

def prime_budget(t):
    N = math.floor(math.exp(2*t))
    total = 0.
    for p in range(2, N+1):
        if any(p % d == 0 for d in range(2, math.isqrt(p)+1)):
            continue
        n = p
        while n <= N:
            total += 2*math.log(p)/math.sqrt(n)
            n *= p
    return total

def row(t):
    P = prime_budget(t)
    M = C + 4*t*math.exp(t) + P
    crude_log10_n = (M+math.log(2*t)+math.log1p(-2*math.exp(-M)))/math.log(10)
    V = max(3, math.exp(4*(P+math.log(math.pi)+1+math.log(4)/4)/3))
    R = V/math.pi
    k = 2*V*t
    # Norm product <= sqrt(4*t*R/log(2)); elementary physical L1/L2
    # and zero-band embedding estimates, not yet attached in Lean.
    target = math.log(1/(8*(C+P)))
    n = None
    lg = 0.
    if 2*k < 2_000_000:
        for j in range(1, 2_000_000):
            lg += math.log(j)
            if j+1 >= 2*k and math.log(4*t*R/math.log(2))+2*(math.log(2)+j*math.log(k)-lg) < target:
                n = j
                break
    return t, P, M, crude_log10_n, R, n, math.ceil(2*k-1)

if __name__ == "__main__":
    print("t,prime_budget,uniform_budget,log10_crude_moment_floor,localized_R,localized_moments,ratio_floor")
    for t in (0.25,0.5,1,1.5,2):
        print(",".join(map(str,row(t))))
