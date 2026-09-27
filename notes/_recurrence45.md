# SZ edge recurrence 45 — relay-endpoint closure

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-44
Public promotion: forbidden

## Objective

Fold the nilpotent p-defect relay from series-44 back into the base k-sheet transfer and determine whether it contributes an independent boundary state.

The result is favorable:

the relay carries no independent entrance data.

Its initial h-strip is already the output of the exact P/J overlap transfer, its later values are explicit one-step base functionals, and its terminal condition Schur-eliminates to one scalar closure row with nonzero local coefficient.

Thus the global four-delay state does not need an additional free p-sheet.

The corrected architecture is:

finite k-sheet base state
+
causal k-predecessor
+
scalar relay closure rows.

No global fixed-L injectivity theorem is claimed yet because the resulting finite closure rows still need complete determinant certification.

## 1. Relay notation

Use

P(t)=X(p+t),

Q(t)=S(p+t),

0<t<e,

with

p=log(10/9),

h=log(81/80),

e=u-p.

Define the base forcing functionals

A(t)
=
[
G X(t)
+
delta S(t)
+
beta S(t+k)
]/mu,

and

B(t)
=
[
G S(t)
+
delta X(t)
+
beta 1_(t>k) X(t-k)
]/mu.

Series-44 gives, on

0<t<e-h,

P(t+h)=A(t),

Q(t+h)=B(t)-P(t).

These are the relay Schur variables registered in the terminology file.

## 2. The initial relay strip is not free

Take

0<t<min(h,e).

Set

x0=p+t-h.

Because

p>e

throughout the post-p chamber,

p+t>e,

so

x0>e-h.

Also

t<h

gives

x0<p,

and

t<e

gives

x0<u-h=p+e-h.

Therefore

e-h
<
x0
<
min(u-h,p).

So x0 lies in the exact P/J common-overlap domain from series-34.

The overlap transfer at x0 has output coordinate

x0+h=p+t.

Hence its first output sheet is exactly

V(p+t)
=
(P(t),Q(t))^T.

Therefore the initial relay strip

0<t<min(h,e)

is already determined by earlier base k-sheet data and the valid causal predecessor term.

It is not an independent relay seed.

## 3. Explicit later relay values

For h<t<e,

the first relay equation gives directly

P(t)=A(t-h).

The second gives

Q(t)=B(t-h)-P(t-h).

Therefore:

for

h<t<min(2h,e),

Q(t)
=
B(t-h)
-
P0(t-h),

where P0 denotes the already determined initial-strip P-output.

For

2h<t<e,

P(t-h)=A(t-2h),

so

Q(t)
=
B(t-h)
-
A(t-2h).

Thus after the first h-strip every relay coordinate is an explicit finite base functional.

There is no relay recurrence state left to propagate.

## 4. Three terminal relay regimes

The terminal relay strip is

T_e=(max(0,e-h),e).

The exact terminal condition is

P(t)=B(t).

There are only three geometries.

### Regime I: 0<e<=h

The entire terminal strip lies in the initial relay output.

Thus

P0(t)=B(t),

0<t<e.

### Regime II: h<e<2h

The terminal strip crosses t=h.

For

e-h<t<h,

the closure is

P0(t)=B(t).

For

h<t<e,

the explicit relay formula gives

A(t-h)=B(t).

### Regime III: e>=2h

The terminal strip lies entirely beyond the initial relay strip.

Hence the closure is uniformly

A(t-h)=B(t),

e-h<t<e.

So the relay-endpoint problem has only three fixed local forms.

## 5. Explicit scalar terminal row

On the derived branch t>h,

A(t-h)=B(t)

is

G X(t-h)
+
delta S(t-h)
+
beta S(t-h+k)

=
G S(t)
+
delta X(t)
+
beta 1_(t>k) X(t-k).

Equivalently,

G S(t)
=
G X(t-h)
+
delta S(t-h)
+
beta S(t+k-h)
-
delta X(t)
-
beta 1_(t>k) X(t-k).

The coefficient of the current S(t) is exactly G.

Hence this relay closure row is locally solvable with a uniform nonzero pivot.

It cannot create a local atom singularity.

Its future-looking term S(t+k-h) is already an internal coordinate of the stacked k-sheet state based at t-h, so it does not require another relay.

## 6. Initial-strip closure row

On the initial branch,

P0(t)=B(t).

The value P0(t) is the first coordinate of the exact overlap output at

x0=p+t-h.

Thus it depends only on the earlier valid stacked state at x0 and its causal predecessor.

It does not contain the current scalar S(t).

By contrast,

B(t)

contains the term

(G/mu) S(t).

Therefore the initial closure equation has current S(t)-coefficient

-G/mu,

which is nonzero.

So the initial relay closure is also locally solvable.

No local relay resonance exists in any of the three regimes.

## 7. Relay Schur elimination theorem

Combining Sections 2-6:

1. the relay has no free initial data;
2. every P(t),Q(t) is explicitly determined from the base stacked state;
3. the terminal relay condition becomes a finite scalar row on the base state;
4. every such row has a nonzero current-S pivot.

Therefore the p-defect relay can be Schur-eliminated completely.

The globally complete unknown state returns to the base finite k-sheet system.

What the relay contributes is not a new state variable but a finite family of terminal closure rows.

This is the relay Schur closure registered in the terminology file.

## 8. Corrected global architecture

The four-delay chamber now has the following complete structural pieces:

A. base stacked state:
   at most three k-sheets of V=(X,S);

B. homogeneous overlap scattering:
   K_1,K_2,K_3 on the exact P/J overlap domain;

C. causal predecessor:
   the rank-one X(y-k) correction from series-43;

D. lower-defect bridge:
   the Schur-eliminated p-relay rows from this pass;

E. terminal physical graph:
   always gate-free, S=R^(-1)X.

No independent p-sheet or p-lattice remains.

## 9. Parameter chamber structure

The relay introduces only two new moving comparisons:

e=h,

e=2h.

Together with the existing sheet/gate thresholds from series-42/43, the complete parameter interval is still cut by finitely many explicit arithmetic values.

Inside each final chamber:

- the active sheet count is fixed on each atom;
- the overlap K_r block is fixed;
- the causal predecessor pattern is fixed;
- the relay closure regime is fixed;
- every coefficient matrix is independent of L.

Thus complete fixed-L certification is again a finite matrix problem.

## 10. What remains to certify

After Schur elimination, one must construct the full base-state folded matrix containing:

- K_r propagation rows;
- causal predecessor rows;
- sheet-drop constraints;
- relay closure rows;
- entrance graph rows;
- terminal graph rows.

Because the relay rows are locally pivotable, they may be eliminated early.

The remaining determinant/singular-value certification is finite.

This pass does not perform that complete enumeration.

## 11. Status of earlier residue

Series-44 correctly identified the missing p-relay.

This pass strengthens it:

the relay is not an additional free state.

Series-42/43 remain non-global because their transfer domain omitted the lower defect, but their base-state atom library can now be repaired by adjoining the scalar relay closure rows rather than by enlarging the propagating state dimension.

The determinant audits from series 36-42 remain valid on the explicit subfamilies and domains they actually tested.

## 12. Fixed-L injectivity status

No new global injectivity theorem is claimed.

The load-bearing continuous positive range remains

0 < L <= log(16/3).

The post-log(16/3) work now has a structurally complete finite state and a Schur-eliminable lower-defect relay, but the full finite matrix list has not yet been certified.

## 13. Quantitative status

The new quantitative fact is local relay transversality:

the derived relay row has current-S coefficient G=sqrt(2),

and the initial relay row has current-S coefficient G/mu.

Thus relay elimination itself has a positive local pivot margin.

No global fixed-scale singular-value floor for the complete four-delay chamber is asserted.

No shrinking-collar estimate follows.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-46 / COMPLETE FOUR-DELAY MATRIX

The next pass should:

1. generate the final finite parameter chambers including e=h and e=2h;
2. build the complete folded base-state matrix in each chamber;
3. Schur-eliminate relay rows first;
4. certify the resulting determinant or smallest singular value with outward exact weight bounds.

This is now the first point in the chain where a globally complete four-delay fixed-L certification is structurally justified.

Even if successful, SZ-CROSS-COLLAR-3 must remain fixed until the shrinking-collar drilling interface is quantitatively controlled.

No public promotion and no canonical cursor movement are asserted.
