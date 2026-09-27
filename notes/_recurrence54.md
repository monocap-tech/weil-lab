# SZ edge recurrence 54 — arithmetic field transport, holonomy, and the edge-Runge gate

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-53
Public promotion: forbidden

## Objective

Transport the shrinking interior arithmetic-field detector from series-53 to the physical edge or the ratified singular-site geometry.

A direct positive transport theorem is not obtained.

Instead this pass isolates the exact obstruction and extracts a stronger canonical replacement.

There are two results.

First, arithmetic recentering of a nonkernel field carries a boundary-strip cocycle. The H1 regularity of the field does not remove the original L2 source carriers.

Second, the path-order defect itself is strongly observable. The dyadic/nondyadic transport holonomy

Hhol=[D,N]

gives a six-step source detector with a weight-uniform lower bound on the entire ambient four-delay prime-silent space.

Thus the arbitrary interior detector of series-53 can be replaced by a canonical finite arithmetic-cell detector.

What remains missing is a local Runge/quasi-analytic theorem that moves that canonical cell detector to the prescribed edge or singular-site neighborhoods.

No fixed-L prime-silent triviality theorem is claimed.

## 1. Setup

Use the four-delay normalized prime split from series-51:

D
=
C_(log2)
+
gamma C_(log4),

N
=
beta C_(log3)
+
delta C_(log5).

Let

Z
=
ker(D+N)
=
ker P_c

in the four-delay chamber.

On Z,

Nf=-Df.

Series-53 works with a finite-dimensional regular-kernel branch

V=K_c^{ps} subset Z

and constructs shrinking field observations at finitely many adaptively chosen reachable arithmetic centers.

The present pass asks whether those centers can be transported to prescribed canonical locations.

## 2. One-step field transport

Let

T_(ell,+)

be the one-sided truncated translation and let

F_w(x)

be the screw potential of a zero-extended source w.

GERM-8 gives the global identity, valid without assuming w is a kernel vector,

boxed:
F_(T_(ell,+)w)(x)
=
F_w(x-ell)
-
B_(ell,+)w(x),

where

B_(ell,+)w

is the screw potential of the boundary strip discarded by the translation.

Equivalently,

boxed:
F_w(x-ell)
=
F_(T_(ell,+)w)(x)
+
B_(ell,+)w(x).

Thus moving one field sample by one arithmetic delay creates a new boundary-strip field.

The same statement holds for the opposite orientation.

## 3. Finite arithmetic words

Take a finite word

omega
=
(ell_1,sigma_1)
...
(ell_r,sigma_r)

in the active oriented delays.

Iterating Section 2 gives

boxed:
F_w(x-h_omega)
=
F_(T_omega w)(x)
+
sum_(j=1)^r
F_(q_(j,omega,w))(x),

where

h_omega

is the net signed displacement,

T_omega

is the corresponding composition of truncated translations,

and every

q_(j,omega,w)

is a boundary-strip source produced at the j-th step and transported by the later steps.

The exact coefficients/signs depend on the orientation word, but every correction is a finite strip source.

This is the field transport cocycle registered in the terminology file.

## 4. Why field regularity does not close recentering

For the series-53 escape family,

y=G_c w

lies in H1 and therefore has a continuous representative.

But the correction terms in Section 3 are generated from restrictions of the source w, not from restrictions of y.

Those strip sources are only L2 at the available regularity.

Therefore arithmetic recentering does not transport the finite-dimensional H1 field family into itself.

It regenerates the same rough boundary-source species that caused the source-side diagonal/edge obstruction in the earlier GERM chain.

So:

boxed:
H1 field regularity
does not make arithmetic recentering closed.

This is the first obstruction to replacing the adaptive centers of series-53 by prescribed edge points.

## 5. Exact path-order cancellation

There is nevertheless one way to cancel the terminal translated field.

Take two arithmetic words with the same whole-line net translation but different order.

Whole-line translations commute, so subtracting the two transport identities cancels the common translated source.

What remains is a pure sum of support-truncation boundary commutators.

For two symmetric translation blocks this is exactly their operator commutator.

This is the arithmetic transport holonomy.

## 6. Dyadic/nondyadic holonomy

Define

boxed:
Hhol
=
[D,N]
=
DN-ND.

Expand:

Hhol
=
beta [C_a,C_b]
+
delta [C_a,C_d]
+
gamma beta [C_(2a),C_b]
+
gamma delta [C_(2a),C_d],

where

a=log2,
b=log3,
d=log5.

Same-orientation one-sided shifts commute exactly.

Hence every term in Hhol is a sum of opposite-orientation truncation commutators.

The operator is therefore entirely boundary-generated.

## 7. Exact two-delay commutator formula

Let

0<x<y<L,

and write

L_x=S_x^+,
R_y=S_y^-.

Then

boxed:
[L_x,R_y]f(s)
=
[
1_(y-x,L-x)(s)
-
1_(y,L)(s)
]
f(s-(y-x)),

and

boxed:
[R_x,L_y]f(s)
=
[
1_(x,L-y+x)(s)
-
1_(0,L-y)(s)
]
f(s+(y-x)),

with empty intervals omitted.

The x>y case follows by antisymmetry.

Therefore

[C_x,C_y]

is a finite sum of translated restrictions to arithmetic boundary cells.

For the four active pairs, the shift gaps are

b-a
=
log(3/2),

d-a
=
log(5/2),

2a-b
=
log(4/3),

d-2a
=
log(5/4).

Thus Hhol is supported by the same finite ratio-cell geometry isolated earlier in GERM-21 through GERM-23.

No adaptive arithmetic center is involved.

## 8. Holonomy recursion on the prime-silent space

Take

f in Z,

so

Nf=-Df.

Set

K=Hhol=[D,N].

For every integer j>=1,

the commutator identity gives

N D^j
=
D^j N
-
sum_(r=0)^(j-1)
D^(j-1-r) K D^r.

Define

e_j
=
N^j f
-
(-D)^j f.

Then

e_1=0,

and

boxed:
e_(j+1)
=
N e_j
-
(-1)^j
sum_(r=0)^(j-1)
D^(j-1-r) K D^r f.

Hence for every

j<=7,

there is a constant C_j depending only on ||D|| and ||N|| such that

boxed:
||e_j||
<=
C_j
sum_(r=0)^(j-2)
||K D^r f||.

In particular e_7 depends only on the six channels

Kf,
KD f,
...,
KD^5 f.

## 9. Insert the nondyadic annihilating polynomial

Series-51 gives

p_N(N)=0,

with

deg p_N=7.

Using

N^j f
=
(-D)^j f+e_j,

we obtain

boxed:
||p_N(-D)f||
<=
C_N
sum_(r=0)^5
||K D^r f||,

for a constant C_N depending only on the fixed Weil weights.

The dyadic block satisfies

p_D(D)=0,

with deg p_D=5.

Series-51 also proves that

p_D(z)

and

p_N(-z)

are relatively prime.

Choose Bezout polynomials A(z),B(z) satisfying

A(z)p_D(z)
+
B(z)p_N(-z)
=
1.

Apply this at D.

Since

p_D(D)=0,

boxed:
f
=
B(D)p_N(-D)f.

Therefore

||f||
<=
C_B C_N
sum_(r=0)^5
||K D^r f||.

By Cauchy-Schwarz there is a constant

boxed:
c_hol>0

depending only on the four fixed Weil weights such that

boxed:
(
sum_(r=0)^5
||Hhol D^r f||^2
)^(1/2)
>=
c_hol ||f||

for every

f in Z.

This is six-step holonomy observability.

## 10. Ambient injectivity consequence

The preceding estimate is ambient.

No regular-kernel hypothesis and no finite-dimensionality are required.

In particular,

boxed:
intersection_(r=0)^5
ker(Hhol D^r|_Z)
=
{0}.

Thus every nonzero four-delay prime-silent source has a finite-depth nonzero arithmetic transport holonomy.

The source cannot be simultaneously path-order flat for the first six dyadic iterates.

## 11. Relation to the seven-step spectral ejection

Series-51 gave a seven-step projection-ejection detector

F B^m.

The present theorem gives a six-step ambient commutator detector

Hhol D^m.

The two statements measure the same failure from different sides:

- spectral ejection measures failure of the prime-silent space to be invariant under D;
- holonomy measures failure of the dyadic and nondyadic ambient translation blocks to commute along the prime-silent orbit.

The holonomy formulation has one major advantage for geometric return:

its source custody is explicit and finite.

Every channel is a finite sum of translated restrictions to arithmetic ratio cells.

## 12. Canonical ratio-cell detector

Define the six-channel map

O_hol f
=
(
Hhol f,
Hhol D f,
...,
Hhol D^5 f
).

For

f in Z,

Section 9 gives

boxed:
||O_hol f||
>=
c_hol ||f||.

Each component is assembled from the fixed four ratio gaps

log(3/2),
log(5/2),
log(4/3),
log(5/4)

and their reflected support cells.

Therefore the adaptive interior arithmetic detector from series-53 is no longer the only shrinking-return candidate.

There is now a canonical fixed arithmetic-cell source detector.

## 13. Kernel/nonkernel custody on V=K_c^{ps}

Now restrict to

V=K_c^{ps} subset K_c.

For every holonomy channel

h_r
=
Hhol D^r f,

split

h_r
=
k_r+n_r,

with

k_r=Pi_K h_r in K_c,

n_r=Q_K h_r in K_c^perp.

The six-step source floor gives

sum_r
(
||k_r||^2+||n_r||^2
)
>=
c_hol^2 ||f||^2.

If the primary nonkernel pieces n_r do not carry the floor, the kernel pieces k_r do.

But the two-stage nonkernel detector of series-52 applies to every k_r in K_c:

||Q_K T k_r||^2
+
||Q_K T^2 k_r||^2
>=
nu_K^2 ||k_r||^2.

Therefore an 18-channel nonkernel observation

n_r,
Q_K T k_r,
Q_K T^2 k_r,

r=0,...,5,

is injective on V with

boxed:
sum_(r=0)^5
[
||n_r||^2
+
||Q_K T k_r||^2
+
||Q_K T^2 k_r||^2
]
>=
c_hol^2 min(1,nu_K^2) ||f||^2.

So the canonical ratio-cell holonomy also admits finite escape into K_c^perp.

## 14. Fixed-scale field consequence

Let

W_hol,NK

be the finite-dimensional sum of the ranges of the 18 nonkernel channels.

Then

W_hol,NK subset K_c^perp.

Hence

G_c|_(W_hol,NK)

is injective.

Finite dimensionality gives a constant

tau_hol>0

such that the corresponding screw fields satisfy

boxed:
sum_i
||G_c L_i^hol f||^2
>=
tau_hol^2 c_hol^2 min(1,nu_K^2) ||f||^2.

Thus the transport holonomy produces a fixed-scale nonkernel field detector with canonical arithmetic-cell source custody.

## 15. Why this still does not give a physical-edge estimate

The holonomy source cells are canonical, but their boundaries include ratio locations such as

log(3/2),
log(4/3),
log(5/2),
log(5/4),

not only prime-power hinges or physical endpoints.

An L2 source restriction to one such cell may be nonzero while all of its shrinking germs at the cell endpoints are superflat.

Therefore fixed cell mass does not by itself produce a shrinking edge/singular-site lower bound.

This is the same rate obstruction that appeared in GERM-14 through GERM-23.

The holonomy theorem removes arbitrariness of the detector.

It does not make its L2 cell sources quasi-analytic.

## 16. The finite edge Runge gate

Let

W subset K_c^perp

be any finite-dimensional generated escape range and let

U subset(-c,c)

be a prescribed open set, for example:

- a physical edge collar;
- a union of neighborhoods of Sigma_c;
- a visible-germ neighborhood.

Define

R_U:
W -> L2(U),

R_U w
=
(G_c w)|_U.

The exact geometric transport condition needed to move the field detector into U is

boxed:
ker R_U={0}.

By self-adjointness of G_c,

R_U w=0

is equivalent to

<w,G_c phi>=0

for every test function phi supported in U.

Hence

boxed:
ker R_U={0}

iff

boxed:
W intersect
[
G_c(L2(U))
]^perp
=
{0}.

This is the finite edge Runge gate registered in the terminology file.

If it holds, finite dimensionality gives a positive fixed-U observation constant and finitely many U-supported test functions separating W.

For a shrinking family U_epsilon, an algebraic rate additionally requires finite-order/non-superflat behavior of those local fields.

## 17. Why the gate is not presently proved

Nothing in the current edge package proves local range density for the full threshold-aware Weil operator G_c.

The ratified QA-2 local restriction theorem applies to the original superflat kernel obstruction, not to arbitrary finite-dimensional subspaces of K_c^perp.

Generic compact self-adjoint integral operators can have nonzero finite-dimensional source families whose image vanishes on a prescribed open set.

Therefore:

boxed:
finite dimensionality
+
H1 field regularity
does not imply
the finite edge Runge gate.

A Weil-specific local range/unique-continuation theorem would be required.

## 18. Arithmetic recentering does not bypass the gate

One might try to move the adaptive arithmetic centers from series-53 into U by repeated prime-delay recentering.

Sections 2-4 show why this does not solve the problem.

Each recentering creates boundary-strip source terms.

Using two path orderings cancels the terminal translated field, but leaves exactly the holonomy channels of Sections 5-14.

Those channels are now canonical and strongly observable, but remain source-supported on finite ratio cells.

Thus arithmetic recentering converts:

adaptive interior field detection

into

canonical ratio-cell holonomy detection,

not directly into

physical-edge field detection.

The edge Runge/quasi-analytic gate remains.

## 19. Relation to GERM-23

GERM-23 found that movable-center source detection does not imply finite equation closure because every new center introduces a fresh diagonal source carrier.

The present field-side audit is the exact analogue.

The H1 field family can be detected quantitatively in the interior.

But transporting those observations by the arithmetic shift algebra introduces boundary-strip source carriers.

Path-order cancellation removes the transported field but leaves a finite ratio-cell holonomy.

Thus the diagonal-carrier obstruction has not disappeared; it has become a boundary-commutator/ratio-cell obstruction.

The positive difference is that the holonomy now carries a uniform six-step source floor.

## 20. Result

The arithmetic field-to-edge transport problem has a precise answer.

Positive:

1. the arbitrary arithmetic-center detector can be replaced by a canonical transport holonomy;
2. the holonomy is a finite ratio-cell source operator;
3. on the entire ambient prime-silent space,
   six holonomy channels satisfy a weight-uniform lower bound;
4. on K_c^{ps}, at most two further first-prime steps give an 18-channel K_c^perp detector;
5. the resulting finite-dimensional nonkernel field family has a fixed-scale screw-field floor.

Negative:

1. direct arithmetic recentering regenerates L2 boundary-strip sources;
2. the canonical holonomy cells include ratio sites outside Sigma_c;
3. no current theorem gives shrinking mass at their endpoints;
4. no current theorem proves the finite edge Runge gate for the generated nonkernel field family.

Therefore the missing statement is no longer an unspecified transport argument.

It is a Weil-specific local range/quasi-analyticity theorem for the finite holonomy escape family.

## Fixed-L status

This pass does not prove

K_c^{ps}=0

through the whole four-delay chamber.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-55 / HOLONOMY CELL RIGIDITY

The next pass should work directly with the six canonical ratio-cell holonomy sources.

Priority:

1. write each [C_x,C_y] channel as an explicit finite ratio-cell source map;
2. build the finite-dimensional cell-mass filtration of the holonomy image;
3. determine whether a superflat-at-all-cell-boundaries branch can coexist with the six-step holonomy lower bound;
4. use the double orientation/reflection geometry to identify which ratio-cell boundaries become visible prime or endpoint germs;
5. if the hard branch survives, state the exact local Runge/quasi-analytic theorem needed to move it into Sigma_c.

A positive cell-rigidity theorem would eliminate the remaining geometric transport obstruction without returning to arbitrary dense-center closure.

No public promotion and no canonical cursor movement are asserted.
