# SZ edge recurrence 34 — post-p overlap transfer

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-33, with scope correction below
Public promotion: forbidden

## Objective

Treat the genuine post-p chamber

log(50/9) < L <= log 6

without restarting threshold-by-threshold elimination.

Use the common boundary-transfer mechanism from the previous prime-channel experiments. The main goal is to identify the exact transfer state after u crosses

p = log(10/9).

Canonical theorem cursor remains fixed at SZ-CROSS-COLLAR-3.

## 1. Notation and the moving split

Set

a = log 2,
b = log 3,
c = log 4,
d = log 5,

s = d-c = log(5/4),
q = c-b = log(4/3),
p = a+d-2b = log(10/9),
j = 2b-3a = log(9/8),
h = j-p = log(81/80),
k = q-s = log(16/15).

Write

u = L-d.

In the post-p chamber,

p < u <= q-p = log(6/5).

Define the moving defect width

e = u-p > 0.

Then

0 < e <= q-2p = k+h.

This is the first important outward bound.

The head interval (0,u) splits canonically into

lower defect:  (0,e),

bulk:          (e,p),

upper defect:  (p,u).

The two defect strips have equal width e.

Also define

alpha = u-k = e + (p-k).

Since p-k = log(25/24) > 0,

alpha > e.

## 2. Exact lower-defect equations

Use the series-32 variables

X(t) = H(t),
S(t) = H(s+t),

and constants

beta = B/A,
gamma = C/A,
delta = D/A,
mu = beta^2,
G = 2 gamma = sqrt(2),

where

A = log2/sqrt(2),
B = log3/sqrt(3),
C = log2/2,
D = log5/sqrt(5).

For 0<t<e, the exact compact boundary equations reduce to

delta S(t)
=
mu X(j+t)
- G X(t)
- beta S(k+t),

and

G S(t)
=
mu X(p+t)
- delta X(t)
+ mu * 1_(t<e-h) S(j+t)
- beta * 1_(t>k) X(t-k).

These are the exact equations on the new head segment. No scalar h-recurrence has yet been used.

## 3. Exact P-overlap relation

For e<x<j, the evaluation p+x lies in the left/right overlap.

Comparing the two formulas for U(p+x) gives

mu S(x) = G X(p+x),                    e<x<h,

and

mu [S(x)+X(x-h)] = G X(p+x),           max(e,h)<x<j.

A second comparison at U(s+x) gives

mu X(p+x)
=
G S(x)
+ delta X(x)
+ beta * 1_(x>k) X(x-k).

Therefore the old P-relation becomes

S(x) = R X(x),                          e<x<h,

and

S(x)
=
R X(x)
- Q X(x-h)
+ Z * 1_(x>k) X(x-k),                  max(e,h)<x<j,

where

Delta = mu^2-G^2,

R = G*delta/Delta,
Q = mu^2/Delta,
Z = G*beta/Delta.

The extra X(x-k) term is load-bearing.

## 4. Exact J-overlap relation

For e-h<x<u-h, the evaluation j+x lies in the first right branch. Comparison gives

mu S(x+h) = G X(j+x) - mu X(x).

The left boundary formula for U(x) gives

mu X(j+x)
=
G X(x)
+ delta S(x)
+ beta * 1_(x<alpha) S(x+k).

Hence

S(x+h)
=
-T X(x)
+ E S(x)
+ F * 1_(x<alpha) S(x+k),

where

T = Delta/mu^2,
E = G*delta/mu^2,
F = G*beta/mu^2.

For the old terminal strip u-h<x<p, when that strip is nonempty, the second right branch gives

S(x)
=
R^(-1) X(x)
- (beta/delta) * 1_(x<alpha) S(x+k).

When u>=p+h=j, this old scalar terminal strip disappears entirely.

## 5. Exact finite-tap transfer

On the common overlap

e-h < x < min(u-h,p),

combine the J-relation at x with the P-relation at x+h.

Let

V(x) = (X(x), S(x))^T.

Then

V(x+h)
=
M0 V(x)
+ 1_(x<alpha) c_plus S(x+k)
- 1_(x>k-h) c_minus X(x-(k-h)),

where

M0 =
[ (Q-T)/R    E/R ]
[   -T        E  ],

c_plus =
[ F/R ]
[  F  ],

c_minus =
[ Z/R ]
[  0  ].

The exact coefficient identities are

det M0 = 1,

trace M0 = Theta,

with the same Theta as in the earlier scalar recurrence.

Numerically for the exact Weil weights,

Theta = 1.9797928499...,

det M0 = 1.

The tap coefficients are finite and nonzero:

F/R = 0.252848...,

F = 0.652522...,

Z/R = beta/delta = 0.881241....

Thus the post-p change is not a failure of the transfer mechanism. It is a change from a local 2-state transfer to a 2-state transfer with one forward and one backward finite tap.

## 6. Where the old scalar recurrence survives

If both tap indicators vanish, the transfer reduces to

V(x+h)=M0 V(x).

Then Cayley-Hamilton gives the old scalar law

X(x+h) = Theta X(x) - X(x-h).

The tap-free conditions are

x >= alpha

and

x <= k-h.

Hence the old scalar recurrence survives only on the gate-free overlap

alpha <= x <= k-h,

subject also to the P/J overlap bounds.

This interval is no longer the full bulk tail.

As e increases, alpha increases. Once alpha >= k-h, there is no open interval on which the transfer is purely scalar.

Therefore the requested backward propagation across the new head segment does not exist in the old one-component form.

## 7. Finite depth of the new k-overlap

Series-32 suggested a dense h/k closure. That is too pessimistic operationally.

The outward defect width satisfies

e <= k+h.

Therefore:

- if e<=k, a k-shift cannot map the lower defect back into itself;
- if e>k, it can do so only on the strip (0,e-k);
- that strip has width e-k<=h.

Thus the k-tap has depth at most one inside the moving defect.

There is no admissible infinite dense h/k orbit inside the boundary domains.

Irrationality of h/k remains true, but it is not by itself the right closure model.

## 8. Minimal enlarged state

The natural bulk state remains two-dimensional:

V(x)=(X(x),S(x)).

To write the defect problem as a local first-order system, one must also retain the translated copy sampled by the k-tap.

Equivalently, on 0<t<e use the two-sheet boundary state

W(t) = ( V(t), V(p+t) ).

This is four scalar components.

The exact lower- and upper-defect equations couple these two sheets to the finite k-shifts. Because the k-feedback depth is at most one, no further infinite hierarchy is generated in this chamber.

Thus the first genuine recurrence-type change is:

scalar second-order h-chain
    ->
two-component unimodular bulk transfer
    +
finite two-sheet defect state.

If one insists on a purely local first-order cocycle with all taps stored as coordinates, four scalar components are the minimal evident closed state. No claim of algebraic minimality below four is made.

## 9. Scope audit of series-33

Series-33 claimed that the scalar recurrence remained unchanged on

log(16/3) < L <= log(50/9).

That proof checked U(p+t) but omitted the new term entering through U(s+t).

For x>k,

U(s+x) = gamma S(x) + beta X(x-k),

which produces the Z X(x-k) term in the P-relation above.

Likewise for x<alpha, the J-relation contains the F S(x+k) term.

Therefore series-33 does not establish the stated injectivity extension.

Its conclusion is not disproved here, but its scalar proof is incomplete and should not be used load-bearing.

The last currently established fixed-L injectivity window remains the series-31 result:

0 < L <= log(16/3).

## 10. Resonance status

The bulk transfer itself is completely controlled:

det M0 = 1,

1.97 < trace M0 < 1.99 < 2.

Hence M0 is invertible and elliptic; no bulk singularity or scalar gain resonance occurs inside the constant-transfer portion.

The unresolved resonance problem is now a boundary matching problem for the finite defect state W, not a scalar terminal-gain equation.

The old rho test is insufficient once either tap is active.

No fixed-L injectivity theorem for the full post-p chamber is proved in this pass.

## 11. General prime-channel transfer principle

GERM-27 through this pass support one common mechanism.

For a fixed active arithmetic-delay set and one boundary-ordering chamber:

1. reduce the compactly supported source to finitely many boundary fibers using the shortest delay;
2. collect the surviving local fibers into a finite state;
3. on the bulk, propagate by a constant transfer matrix;
4. when an overlap threshold is crossed, add only the translated sheet actually sampled by the new gate;
5. outward support bounds make the number of such sheets finite;
6. fixed-L injectivity becomes transversality of the finite boundary transfer state, not a fresh threshold proof.

Earlier scalar recurrences are the one-sheet special case.

This is the reusable prime-channel injectivity interface suggested by the experimental chain.

## 12. Quantitative status

Fixed-L injectivity:
- proved by the current chain only through L<=log(16/3);
- not proved here for log(16/3)<L<=log6 after the series-33 audit.

Fixed-scale singular-value floor:
- whenever P_c restricted to K_c is injective, finite dimensionality gives a positive kappa_c(L);
- therefore the floor is currently justified through L<=log(16/3);
- no uniformity in L is asserted.

Shrinking-collar coercivity:
- still missing;
- even a general fixed-L prime injectivity theorem would not by itself give a power-law lower bound for the collar observation Delta_(c,c+epsilon);
- the missing drilling interface is a quantitative transfer from the fixed-scale arithmetic-delay norm to the shrinking edge/collar observation.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-35 / FINITE-DEFECT TRANSVERSALITY

The next pass should build the explicit boundary matching matrix/operator for W(t)=(V(t),V(p+t)) and test its determinant/transversality over the whole post-p chamber.

Priority should be a chamber-independent determinant or symplectic argument for the finite defect state, rather than another scalar threshold cascade.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
