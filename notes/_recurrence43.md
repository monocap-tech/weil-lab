# SZ edge recurrence 43 — causal-lag closure

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-42
Public promotion: forbidden

## Objective

Close the sole remaining nonlocal ingredient from series-42:

X(x-(k-h)).

The main result is structural and exact.

After rewriting the recurrence at the output coordinate, the external lag is a genuine causal k-predecessor. It does not create a feedback cycle.

Moreover its injection factors universally through every sheet-scattering block K_r.

Therefore the complete four-delay prime-channel transfer admits a finite causal path expansion with:

- at most fourteen h-steps;
- at most two k-steps;
- no lag-generated cycles;
- and a finite endpoint path library.

The coefficient eta<9/10 is useful conditioning, but contraction is not the proof mechanism.

No new global fixed-L injectivity interval is claimed yet.

## 1. Output-coordinate form

Series-42 gives, at input coordinate x,

W_r(x+h)
=
K_r W_r(x)
+
1_(x>k-h) b_r X(x-(k-h)).

Set

y=x+h.

Then

x-(k-h)
=
y-k.

Therefore the exact recurrence is

W_r(y)
=
K_r W_r(y-h)
+
1_(y>k) b_r X(y-k).

This is the correct causal form.

Every dependency of the state at y comes from an earlier absolute coordinate:

y-h < y,

y-k < y.

Hence the transfer graph is directed by increasing absolute coordinate.

The causal lag cannot by itself create a directed cycle.

## 2. Universal pre-scattering factorization

Recall

K_r=L_r U_r,

and

b_r
=
(
-eta e1,
eta^2 e1,
...,
(-1)^r eta^r e1
)^T,

where

eta=beta/delta.

Because b_r is produced by the lower-triangular backward-coupling factor L_r acting on the first-sheet source

(-eta e1,0,...,0)^T,

one has

L_r^(-1) b_r
=
(-eta e1,0,...,0)^T.

Now U_r is block upper bidiagonal.

Solving

U_r z
=
(-eta e1,0,...,0)^T

from the last sheet backward forces every sheet except the first to vanish.

Thus

K_r^(-1)b_r
=
(
M0^(-1)(-eta e1),
0,
...,
0
)^T.

The exact two-state identity is

M0^(-1)(eta e1)
=
(F,F/R)^T.

Therefore, for every r=1,2,3,

K_r^(-1)b_r
=
-
(
F,
F/R,
0,
...,
0
)^T.

Define

d=(F,F/R)^T,

d_r=(d,0,...,0)^T.

Then the recurrence factors as

W_r(y)
=
K_r
[
W_r(y-h)
-
1_(y>k) d_r X(y-k)
].

This factorization is independent of the number of active k-sheets.

It is the universal causal-path form registered in the terminology file.

## 3. Contraction is not the right mechanism

The exact lag coefficient satisfies

eta<9/10.

However the homogeneous scattering blocks are not contractions in the Euclidean norm.

Numerically,

||K_1||_2 approximately 1.280,

||K_2||_2 approximately 1.949,

||K_3||_2 approximately 2.557.

So eta<1 does not imply a direct norm contraction for the full recurrence.

Likewise K_2 and K_3 contain hyperbolic singular directions.

Therefore a Neumann/contraction proof would require a nontrivial adapted norm and is not justified by the current estimates.

The correct mechanism is causality plus finite support.

## 4. Causal path expansion

A backward dependency path from a terminal coordinate y is a word in two step types:

H: y -> y-h,

K: y -> y-k.

Every step strictly decreases y.

Repeated substitution therefore terminates when the coordinate exits the support or reaches an entrance atom.

The weight attached to an H-step is the appropriate homogeneous scattering block K_r or its sheet-drop restriction.

The weight attached to a K-step is rank one: it selects the first X-coordinate at y-k and injects it through b_r, equivalently through the universal pre-scattering vector d_r.

Thus the terminal state is a finite sum over causal path words.

There is no denominator and no infinite series.

## 5. Exact path-depth bounds

Across the whole four-delay chamber,

u <= log(6/5).

Also

u/h < 15,

so a path with no K-step has at most fourteen H-steps.

Because

u < 3k,

a path has at most two K-steps.

More sharply:

zero K-steps:
at most 14 H-steps;

one K-step:
(u-k)/h < 10,
so at most 9 H-steps;

two K-steps:
(u-2k)/h < 5,
so at most 4 H-steps.

A third K-step is impossible.

Therefore every causal dependency word has one of the finite types

H^m,

H^a K H^b,

H^a K H^b K H^c,

with the corresponding total H-count bounded by 14, 9, or 4.

## 6. Crude finite word count

Ignoring sheet/gate restrictions and counting only H/K ordering gives a useful universal upper bound.

For zero K-steps there are at most

15

possible H-lengths m=0,...,14.

For one K-step and total H-count m<=9, there are m+1 possible positions of the K-step, giving at most

1+2+...+10
=
55

words.

For two K-steps and total H-count m<=4, there are

C(m+2,2)

placements, giving

1+3+6+10+15
=
35

words.

Hence there are at most

15+55+35
=
105

bare causal H/K word types before imposing the actual sheet-count and gate restrictions.

For a fixed parameter atom, most of these words are inadmissible and the surviving word weights are uniquely determined.

Thus the remaining global audit is genuinely finite.

## 7. Finite parameter chambers

The active sheet boundaries are

zeta=u-2k,

alpha=u-k,

and the causal gate is at

k.

The atomization also involves bounded preimages under h and k.

A path combinatorics change can occur only when one of these moving boundaries crosses a finite displacement

m h + n k

with

0<=m<=14,

0<=n<=2.

Therefore the L-parameter interval is divided by finitely many arithmetic threshold values.

Inside each open parameter chamber:

- the atom graph is constant;
- the admissible causal path set is constant;
- every endpoint transfer matrix is a fixed rational expression in the Weil weights;
- it does not vary continuously with L except through the discrete choice of chamber.

This is the key reduction needed for a finite certification pass.

## 8. Causal lag as a nilpotent dependency, not a monodromy

Series 35-41 repeatedly described possible global failures using cycle or monodromy language.

After the three-sheet repair, the causal dependency orientation shows that the lag itself contributes no directed cycle.

The only true two-point issue is endpoint transversality:

entrance data are propagated forward through a finite DAG and then tested against the terminal endpoint graph.

Thus the remaining determinant is an endpoint transfer determinant built from a finite causal path sum.

There is no additional lag-monodromy determinant.

This corrects the interpretation of the causal term without invalidating the already certified subfamily determinant audits.

## 9. Quantitative implication

For a fixed parameter chamber, let

T_L

be the finite endpoint transfer matrix obtained by summing all admissible causal path weights.

If

sigma_min(T_L)>0,

then the complete four-delay arithmetic-delay operator has a fixed-scale boundary floor on that folded component.

Because only finitely many parameter chambers and finitely many path words occur, a chamber-uniform fixed-scale floor would follow from a positive minimum over the finite certified determinant/singular-value list.

This is still a fixed-scale statement.

It does not provide a shrinking-collar power law.

## 10. What remains

This pass proves:

1. the lag is strictly causal;
2. it creates no feedback cycle;
3. its injection factors universally through K_r;
4. contraction is unnecessary;
5. every endpoint transfer has a finite path expansion;
6. at most two causal K-steps can occur;
7. the remaining certification problem is finite.

This pass does not yet enumerate every parameter chamber or compute every complete endpoint path-sum determinant.

Therefore no new global fixed-L injectivity theorem is claimed.

The load-bearing continuous positive range remains

0 < L <= log(16/3).

## 11. General prime-channel mechanism

The four-delay architecture is now:

finite k-sheet stack
+
unimodular local scattering K_r
+
one universal rank-one pre-scattering causal correction
+
finite endpoint path sum.

This is naturally extensible.

At later arithmetic thresholds, one should:

1. enlarge the sheet stack only when another translate fits in the support;
2. factor the new unmatched backward terms into causal predecessors;
3. bound the number of causal steps by support;
4. certify a finite endpoint path library.

No threshold-by-threshold source reconstruction is required.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-44 / FINITE CAUSAL PATH CERTIFICATION

The next pass should:

1. enumerate the finite parameter chambers generated by the moving sheet boundaries and the displacements m h + n k;
2. build the exact endpoint path-sum matrix in each chamber;
3. certify every determinant/minimal singular value using outward rational weight bounds;
4. determine whether the four-delay prime-channel operator is injective for the full chamber.

If successful, this would give the first globally complete fixed-L four-delay prime-channel injectivity theorem.

Even then, SZ-CROSS-COLLAR-3 must remain fixed until a quantitative shrinking-collar bridge is proved.

No public promotion and no canonical cursor movement are asserted.
