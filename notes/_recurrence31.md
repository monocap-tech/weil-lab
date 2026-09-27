# SZ edge recurrence 31

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Public promotion: forbidden

For log 5 < L <= log(16/3), the four active arithmetic delays log 2, log 3, log 4, log 5 give an injective all-center finite translation operator on zero-extended L2(0,L).

Set a=log2, b=log3, c=log4, d=log5, u=L-d, s=d-c, q=c-b, ell=L-c=s+u. The chamber condition is 0<u<=q-s=log(16/15).

Boundary propagation reduces a candidate source to two fibers H(t)=f(t) and U(t)=f(a+t). With p=log(10/9), j=log(9/8), and h=j-p=log(81/80), eliminating U gives a scalar residue-fiber recurrence

x_(n+1) = Theta*x_n - x_(n-1)

with first step x_1=Theta*x_0 and terminal condition x_(N+1)=rho*x_N.

For the exact arithmetic weights one has

1.5 < rho < 1.8 < Theta < 2

and

Theta - 1/Theta < 1.5 < rho.

Since u < 6h, only N=0,1,2,3,4 can occur. N=0 would require Theta=rho. For N>=1 the positive recurrence ratios decrease from Theta-1/Theta, already below rho. Therefore no terminal resonance exists.

Hence the all-center arithmetic-delay operator has zero kernel for

log 5 < L <= log(16/3).

Combined with the preceding passes, the corresponding silent subspace of the regular zero family remains trivial for

0 < L <= log(16/3),

so a fixed-scale norm gap persists there. No uniformity in c and no shrinking-collar rate are asserted.

Next target: series 32, second post-log5 recurrence chamber,

log(16/3) < L <= log 6.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.
