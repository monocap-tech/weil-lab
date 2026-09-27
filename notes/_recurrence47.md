# SZ edge recurrence 47 — matrix-generator audit and sliding-window correction

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-46
Public promotion: forbidden

## Objective

Implement the complete four-delay matrix generator proposed in series-46 and certify its rank.

The implementation audit exposes a structural flaw in the proposed fixed ten-residue column model.

The ten-symbol residue alphabet is a valid bound on possible directed path displacements, but it is not closed under all exact row equations when those residues are instantiated simultaneously as free columns.

Two independent failures occur:

1. a valid J-row can demand a third +k translate from an m=2 residue;
2. a valid relay row can demand a second +p translate from an epsilon=1 residue.

Therefore the series-46 "complete matrix" cannot be assembled by taking all ten residue classes and all exact rows.

The correct finite object must be a causal certificate subsystem built from sliding k-windows and whole-row provenance checks.

No rank theorem is claimed in this pass.

## 1. Why the audit was necessary

Series-46 proposed the alphabet

m kappa + epsilon rho mod h,

m in {-2,-1,0,1,2},

epsilon in {0,1},

and then suggested instantiating all ten residue classes at every admissible h-level.

That step silently changed a path bound into a simultaneous-state assertion.

The finite-depth results from series 41-45 only prove:

- a local k-window contains at most three consecutive k-translates;
- a directed causal path uses at most two k-predecessor steps;
- a directed relay path uses the one-way p-channel at most once.

They do not prove that every exact row applied to every one of the ten labels remains inside the same ten-label set.

The generator audit tests precisely that closure property.

## 2. Exact +k closure failure

Choose the legal chamber point

e = h/2,

and local coordinate

r = h/10.

Consider the residue-labeled coordinate

x
=
r + 2k - 8h
=
2k - 79h/10.

Numerically,

x = 0.0309391342....

The chamber values are

e-h = -h/2,

u-h = p-h/2 = 0.0991492556...,

alpha = p+h/2-k = 0.0470332545....

Hence

e-h < x < u-h,

and

x < alpha.

So the exact J-row from series-34 is valid at x and its forward k-gate is active:

S(x+h)
+
T X(x)
-
E S(x)
-
F S(x+k)
=
0.

Also

x+k
=
0.0954776554...
<
u
=
p+h/2
=
0.1115717756....

Thus S(x+k) is a genuine nonzero-support variable.

But x already carries the bookkeeping label m=2.

The term x+k would require m=3, outside the ten-symbol alphabet.

Therefore the ten-residue set is not closed under the full exact J-row library.

One may not simply drop the S(x+k) term.

## 3. Exact repeated-p closure failure

Use the same

e=h/2,

r=h/10.

Take the labeled coordinate

t
=
r-k+p-3h.

Numerically,

t=0.0047966865....

Since

0<t<e,

the relay-terminal row is valid:

mu X(p+t)
-
G S(t)
-
delta X(t)
=
0

(the t>k term is absent here).

The shifted coordinate satisfies

p+t
=
0.1101572021...
<
u
=
0.1115717756....

So X(p+t) is inside support.

But t carries epsilon=1 in the series-46 provenance labeling.

The required p+t variable would therefore be an epsilon=2 state.

Again the ten-symbol alphabet is not closed under the complete exact row system.

This does not mean the physical relay iterates twice along the intended causal derivation.

It means only that the same numerical coordinate may satisfy an exact relay row regardless of how a coarse residue label was assigned to it.

That distinction is load-bearing.

## 4. What the counterexamples do and do not show

They do show:

- the fixed ten-residue simultaneous column set is not a complete exact constraint matrix;
- exact rows cannot be applied solely by geometric coordinate membership while truncating provenance labels;
- the 300-column global bound in series-46 is not currently justified as a complete-row matrix bound.

They do not show:

- that the four-delay problem is infinite-state in the causal direction;
- that the sliding three-sheet transfer is wrong;
- that the relay or k-causal path depth bounds fail;
- that any actual nonzero prime-silent source exists.

The failure is one of matrix representation, not yet one of injectivity.

## 5. Whole-row rule

Suppose one wants to use the ten-label provenance budget as a finite certificate.

Then a retained exact row must satisfy:

every nonzero term in that row lies inside the finite provenance state.

If one term leaves the state budget, the term cannot be discarded.

Instead the entire row must be omitted from that certificate subsystem.

Any actual source still satisfies every retained row.

Therefore:

full column rank of such a retained subsystem
is sufficient
for injectivity of the actual source problem.

This is the causal certificate subsystem registered in the terminology file.

## 6. Why a fixed global m-label is unsafe

The labels

m=-2,-1,0,1,2

describe possible net k-displacements across different causal histories.

They do not describe five simultaneously present sheets.

The physical support bound is

u<3k.

Hence, at any fixed local base coordinate x, the only possible sheet stack is

V(x),
V(x+k),
V(x+2k),

with the final one or two terms removed when outside support.

That is the sliding k-window.

If the causal predecessor y-k is followed, the base coordinate of the window moves.

One must not implement that move by permanently adjoining an m=-1 column to the old window.

Likewise, repeated forward movement of the window is not the same as permitting m=3 inside one local stack.

This is the sliding k-window correction registered in the terminology file.

## 7. Safe state model

A sound finite generator should carry states of the form

(base coordinate,
active window width r in {1,2,3},
relay-used flag,
local provenance).

The local vector at a base coordinate is exactly one of

K_1 state:  V(x),

K_2 state:  (V(x),V(x+k)),

K_3 state:  (V(x),V(x+k),V(x+2k)).

Causal predecessor traversal changes the base coordinate.

Relay traversal changes the relay-used flag and lands in the terminal p-tail.

Neither operation enlarges one local k-window beyond width three.

## 8. Exact source of rows

The generator must use the exact all-t compact equations from series-32 as the custody source:

delta S(t)
=
mu H(j+t)
-
G H(t)
+
mu 1_(t>j) H(t-j)
-
beta 1_(t<alpha) S(k+t),

and

G S(t)
=
mu H(p+t)
-
delta H(t)
+
mu 1_(t<u-j) S(j+t)
-
beta 1_(t>k) H(t-k),

for 0<t<u,

together with the exact middle-overlap equations.

The later P/J transfer, K_r blocks, causal-path factorization, and p-relay formulas should be used only as Schur eliminations or local solving rules on the domains where they were derived.

They should not replace the global custody equations.

## 9. Two-fiber domain correction

Series-32 defines

H on 0<t<ell,

where

ell=s+u,

and

S(t)=H(s+t),

0<t<u.

Thus the primary H-domain is larger than (0,u).

This is another reason the series-46 300-column count should not be treated as final.

A safe implementation can avoid duplicating the entire H-domain by using a disjoint two-fiber split:

X(t)=H(t),   0<t<s,

S(t)=H(s+t), 0<t<u.

Since

s=p+j,

the compact equations convert exactly between X and S at the p/j thresholds.

This disjoint split is preferable for the next generator.

## 10. Exact compact equations in the disjoint split

For 0<t<u, the first compact equation becomes

for t<p:

delta S(t)
=
mu X(j+t)
-
G X(t)
+
mu 1_(t>j) X(t-j)
-
beta 1_(t<alpha) S(k+t);

for t>p:

delta S(t)
=
mu S(t-p)
-
G X(t)
+
mu 1_(t>j) X(t-j)
-
beta 1_(t<alpha) S(k+t).

The t>j term is empty in the t<p branch because p<j.

The second compact equation becomes

for t<j:

G S(t)
=
mu X(p+t)
-
delta X(t)
+
mu 1_(t<u-j) S(j+t)
-
beta 1_(t>k) X(t-k);

for t>j:

G S(t)
=
mu S(t-j)
-
delta X(t)
-
beta 1_(t>k) X(t-k),

because t>j implies t>u-j throughout this chamber.

These formulas are exact and globally valid on the stated t-branches.

They are a safer basis for a provenance-aware causal generator.

## 11. Generator status

A prototype fixed-column implementation was deliberately stopped after the closure counterexamples above.

No determinant or rank result from that unsafe implementation is retained.

The next generator must instead:

1. use the disjoint X/S custody split;
2. initialize only physically valid entrance data;
3. propagate sliding k-windows rather than all m-labels simultaneously;
4. use whole exact rows only;
5. record relay use as directed provenance;
6. use P/J and K_r formulas only as certified local eliminations.

Only then is a finite rank audit meaningful.

## 12. Fixed-L injectivity status

No new injectivity interval is claimed.

The load-bearing continuous range remains

0<L<=log(16/3).

The positive local scattering and endpoint determinants from series 36-45 remain valid on the subfamilies and domains explicitly certified there.

Series-46's ten-residue ordering remains a useful path-displacement catalogue, but its complete fixed-column matrix interpretation is withdrawn.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-48 / CAUSAL CERTIFICATE GENERATOR

The next pass should build the generator from the disjoint X/S compact system with sliding k-windows and whole-row provenance.

The first deliverable is not yet a theorem.

It should report:

1. the exact finite causal state types;
2. the exact number of chamber/row-pattern types;
3. whether a full-rank causal certificate subsystem exists in every chamber;
4. any chamber where the finite certificate fails and why.

Only a successful provenance-safe rank audit should be used to extend the fixed-L injectivity window.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
