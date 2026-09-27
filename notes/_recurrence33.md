# SZ edge recurrence 33 — folded lower second chamber

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-32
Public promotion: forbidden

## Result

The scalar recurrence from series-31 survives farther than series-32 initially suggested.

For

log(16/3) < L <= log(50/9),

equivalently

k < u <= p,

where

u = L-log5,
k = log(16/15),
p = log(10/9),

the all-center finite arithmetic-delay operator remains injective:

ker P_c = {0}.

Hence the silent subspace of the regular zero family remains trivial for

0 < L <= log(50/9),

and the fixed-scale arithmetic-delay norm gap persists through this larger range.

## Why the new k-overlap does not yet alter the recurrence

Use the notation from series-32:

a = log2,
b = log3,
c = log4,
d = log5,

s = d-c,
p = a+d-2b = log(10/9),
j = 2b-3a = log(9/8),
h = j-p = log(81/80),

and define the two fibers

H(t) = f(t),
U(t) = f(a+t).

In the second chamber the new overlap terms live in the local intervals controlled by

alpha = u-k.

When u <= p one has

alpha < p < j.

Now inspect U(p+t), 0<t<u.

Because p >= u, p+t > u, so the right-hand interior formula applies. Also p+t > alpha, so the new q-overlap term from series-32 does not occur there.

For 0<t<h, p+t<j and the left formula is

U(p+t) = -gamma H(p+t).

For h<t<u, p+t>j and the left formula is

U(p+t) = -gamma H(p+t) + mu H(t-h).

The right formula is, throughout 0<t<u,

U(p+t) = gamma H(p+t) - mu H(s+t).

Thus exactly the same two P-relations as in series-31 follow.

Similarly inspect U(j+t).

Because j>p>=u, j+t>u. Also

j+t <= j+p = s < q,

so the new q-overlap term does not occur.

The left formula is

U(j+t) = -gamma H(j+t) + mu H(t).

The right formula is the first branch for t<u-h and the second branch for t>u-h.

Therefore the two J-relations are also exactly unchanged.

## Unchanged transfer system

Set

mu = beta^2,
G = 2 gamma = sqrt(2),
Delta = mu^2-G^2,

R = G*delta/Delta,
Q = mu^2/Delta,
T = Delta/mu^2,
E = G*delta/mu^2.

Write

X(x) = H(x),
S(x) = H(s+x).

Then the exact relations are again

S(x) = R X(x),                         0<x<h;

S(x) = R X(x) - Q X(x-h),            h<x<u;

S(x+h) = -T X(x) + E S(x),           0<x<u-h;

S(x) = R^(-1) X(x),                  u-h<x<u.

Since EQ/R=1, every residue fiber modulo h satisfies

X(x+h) = Theta X(x) - X(x-h),

with first step

X(x+h) = Theta X(x),

and terminal gain

X(x) = rho X(x-h).

The constants Theta and rho are the same as in series-31.

## Longer-chain nonresonance

For the exact Weil weights, direct interval arithmetic gives

1.58 < rho < 1.60,

1.97 < Theta < 1.99.

Let

P0 = 1,
P1 = Theta,
P(n+1) = Theta Pn - P(n-1).

A nonzero residue fiber must satisfy

P(N+1) = rho P(N)

at its terminal step.

The enlarged chamber has

u <= p = log(10/9) < 9 log(81/80) = 9h.

Hence only

N = 0,1,...,7

can occur.

For N=0, the required equality is Theta=rho, impossible.

Direct interval evaluation on 1.97<Theta<1.99 gives

P0,...,P8 > 0.

The recurrence ratios

r_n = P(n+1)/P(n)

therefore remain defined and positive through n=7.

Moreover

r_1 = Theta - 1/Theta
    < 1.99 - 1/1.99
    < 1.49
    < rho.

Since

r_(n+1) = Theta - 1/r_n

and this map is increasing for positive r_n, the inequality r_1<r_0 implies that the positive ratios decrease:

r_1 > r_2 > ... > r_7.

Thus

r_n < rho

for every n=1,...,7.

No terminal resonance exists.

Therefore every residue fiber vanishes and

ker P_c = {0}

for

log(16/3) < L <= log(50/9).

## Scope correction to series-32

The appearance of the incommensurate scale

k = log(16/15)

does not by itself destroy the scalar recurrence.

The correct statement is:

- k-overlap first appears at L=log(16/3);
- but the P/J overlap elimination still avoids the k-gated terms while u<=p;
- the genuine recurrence-type change occurs only after

u>p,

that is,

L>log(50/9).

So the dense two-scale discussion in series-32 should be read as a warning about the later subchamber, not as an obstruction throughout the entire interval immediately above log(16/3).

## Combined positive range

Combining series 27 through 31 with this pass:

the silent subspace of the regular zero family is trivial for

0 < L <= log(50/9).

Equivalently, the arithmetic-delay channel has a positive fixed-scale singular-value floor on every nonzero finite-dimensional regular zero family in this range.

No uniformity in L and no shrinking-collar rate are asserted.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-34 / POST-p OVERLAP TRANSFER

covering

log(50/9) < L <= log6.

Once u>p, the evaluation point p+t can lie below the right-fiber threshold u, so the P-relations cease to hold on the full head interval. The next pass should split the head fiber at u-p and determine whether the scalar recurrence can be recovered on the remaining tail and then propagated backward.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
