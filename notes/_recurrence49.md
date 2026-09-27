# SZ edge recurrence 49 — regular-kernel irrational cocycle and dynamic ejection observability

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-48
Public promotion: forbidden

## Objective

Use the finite-dimensional regular-kernel hypothesis in the post-log(16/3) irrational-cocycle problem.

Series-48 showed that the ambient prime-silent equations do not admit a globally closed finite residue matrix. The natural next hope was:

finite-dimensional K_c^{ps}
+
dense arithmetic translation orbit
=>
finite-dimensional translation representation.

That implication is false.

Finite-dimensionality alone does not make translated local data remain inside the same finite-dimensional source space. In fact GERM-8 proves something stronger and opposite:

every nonzero regular-kernel branch must eject under every sufficiently short raw truncated translation.

This pass extracts the correct finite-dimensional theorem.

The raw first-prime ejection is dynamically observable on every nonzero finite-dimensional subspace of K_c.

For a prime-silent regular-kernel branch, the prime equation forces the remaining arithmetic translation channels to reproduce that dynamically separating ejection family exactly.

Thus the correct kernel-restricted problem is not finite translation invariance.

It is finite-dimensional ejection compensation.

No fixed-L injectivity extension is claimed.

## 1. Finite-dimensionality alone cannot kill the ambient cocycle

Let

Z_c = ker P_c

be the ambient prime-silent source space.

If

0 != f in Z_c,

then

V_f = span{f}

is already a one-dimensional family satisfying every prime-silent compact equation.

Therefore no theorem whose only inputs are

- V is finite dimensional;
- P_c V = 0;

can imply

V=0.

Any successful use of

K_c^{ps}=K_c intersect Z_c

must use an additional property of the regular screw kernel K_c, not merely its finite dimension.

This is a logical guard on the route opened in series-48.

## 2. Source orientation and first-prime shift

Work in the right-oriented source space

H=L2(0,L),

L=2c.

Let

a=log2.

Let

S_a^+

be the truncated left shift

(S_a^+ f)(s)
=
f(s+a)

for 0<s<L-a, and zero on the terminal strip.

This is the source-coordinate form of the positive physical truncated translation from GERM-8.

GERM-8 proves:

for every nonzero subspace W subset K_c,

S_a^+ W subset W

is impossible.

More generally the same statement holds for every

0<ell<=log2.

## 3. Compression and ejection

Let

0 != V subset K_c

be finite dimensional.

Let

d=dim V,

Pi=orthogonal projection onto V,

Q=I-Pi.

Define

A
=
Pi S_a^+|_V,

and

E
=
Q S_a^+|_V.

Thus

S_a^+|_V
=
A+E.

A is the compressed first-prime shift.

E is its raw ejection from V.

If

E=0,

then

S_a^+ V subset V,

contradicting GERM-8.

Hence every nonzero V subset K_c satisfies

E != 0.

But one nonzero ejection vector is not yet enough.

The correct statement is dynamic.

## 4. Dynamic ejection observability theorem

Claim:

intersection_{m=0}^{d-1} ker(E A^m)
=
{0}.

Proof.

Suppose f in V satisfies

E A^m f=0

for

m=0,...,d-1.

Let chi_A be the characteristic polynomial of A.

By Cayley-Hamilton, every power A^n with n>=d is a linear combination of

I,A,...,A^(d-1).

Therefore

E A^m f=0

for every m>=0.

Let

W_f
=
span{A^m f:m>=0}.

Then W_f subset V subset K_c.

For every m,

S_a^+(A^m f)
=
A^(m+1)f
+
E A^m f
=
A^(m+1)f.

Hence

S_a^+ W_f subset W_f.

If f !=0, then W_f is a nonzero S_a^+-invariant subspace of K_c.

GERM-8 forbids this.

Therefore f=0.

So

boxed:
intersection_{m=0}^{d-1} ker(E A^m)={0}.

This is dynamic ejection observability, registered in the terminology file.

## 5. Fixed-scale ejection floor

Define

O_E:
V -> (V^perp)^d

by

O_E f
=
(
E f,
E A f,
...,
E A^(d-1)f
).

Section 4 proves O_E is injective.

Since V is finite dimensional, there exists

nu_V>0

such that

boxed:
sum_{m=0}^{d-1}
||E A^m f||^2
>=
nu_V^2 ||f||^2

for every f in V.

This is a fixed-scale quantitative theorem.

It uses:

- regular-kernel membership through GERM-8;
- finite dimensionality through Cayley-Hamilton and compactness of the unit sphere.

It uses no endpoint regularity.

## 6. Four-delay prime operator

In the four-delay chamber

log5 < L <= log6,

the active prime-power delays are

a=log2,
b=log3,
c4=log4,
d5=log5.

Use the exact weights

A2=log2/sqrt2,

A3=log3/sqrt3,

A4=log2/2,

A5=log5/sqrt5.

Write

beta=A3/A2,

gamma=A4/A2=1/sqrt2,

delta=A5/A2.

Let

S_lambda^+

be the truncated left shift by lambda and

S_lambda^-

the truncated right shift by lambda.

Then

P_c
=
A2(S_a^+ + S_a^-)
+
A3(S_b^+ + S_b^-)
+
A4(S_c4^+ + S_c4^-)
+
A5(S_d5^+ + S_d5^-).

## 7. Prime-silent branch and operator splitting

Now take

V
=
K_c^{ps}
=
K_c intersect ker P_c

in right-oriented source coordinates.

Assume

d=dim V>0.

For every active delay and orientation define

A_{lambda,sigma}
=
Pi S_lambda^sigma|_V,

E_{lambda,sigma}
=
Q S_lambda^sigma|_V.

Because

P_c|_V=0,

orthogonal projection onto V gives

A_{a,+}
+
A_{a,-}
+
beta(A_{b,+}+A_{b,-})
+
gamma(A_{c4,+}+A_{c4,-})
+
delta(A_{d5,+}+A_{d5,-})
=
0.

Projection onto V^perp gives independently

E_{a,+}
+
E_{a,-}
+
beta(E_{b,+}+E_{b,-})
+
gamma(E_{c4,+}+E_{c4,-})
+
delta(E_{d5,+}+E_{d5,-})
=
0.

This second identity is the exact ejection balance.

## 8. First-prime compensator

Use

A=A_{a,+},

E=E_{a,+}.

Define the compensator ejection operator

C
=
E_{a,-}
+
beta(E_{b,+}+E_{b,-})
+
gamma(E_{c4,+}+E_{c4,-})
+
delta(E_{d5,+}+E_{d5,-}).

Then prime silence gives the exact operator identity

boxed:
E=-C
on V.

Therefore for every m>=0,

E A^m
=
-C A^m.

Combining this with dynamic ejection observability gives

boxed:
intersection_{m=0}^{d-1}
ker(C A^m)
=
{0}.

So the compensator channels are themselves dynamically separating on V.

## 9. Quantitative compensator burden

The fixed-scale floor from Section 5 transfers exactly:

boxed:
sum_{m=0}^{d-1}
||C A^m f||^2
>=
nu_V^2 ||f||^2.

Thus a hypothetical nonzero prime-silent regular-kernel branch cannot hide the first-prime ejection.

The opposite first-prime direction and the log3/log4/log5 channels must reproduce it with full finite-dimensional observability through the first d compressed iterates.

This is the strongest correct finite-dimensional consequence presently available from prime silence.

## 10. Why this is not a translation representation

One might try to identify

A

with an action of the first-prime translation on V.

That is incorrect.

The exact semigroup defect is

A_{ell+mu}
-
A_ell A_mu
=
Pi S_ell Q S_mu|_V.

The right side is compression curvature.

For the first-prime shift, E is dynamically observable and therefore cannot vanish on a nonzero V.

So the arithmetic action on V is necessarily curved by ejection.

There is no honest finite-dimensional translation representation to which the standard exponential-polynomial theorem can be applied.

The failure of invariance is not an inconvenience.

It is forced by the regular-kernel geometry.

## 11. Why local restriction transport does not repair this

For a finite-dimensional V one may choose finitely many local restrictions that separate V.

Every other local restriction along the dense arithmetic orbit can then be expressed as a linear map of those finite detector coordinates.

But the image subspaces of translated restrictions may move through infinitely many directions in the ambient L2 window.

Even for

dim V=1,

the local translates of one generic compactly supported function may span an infinite-dimensional translation orbit.

Therefore:

finite source dimension
does not imply
finite-dimensional translated-range invariance.

A representation theorem requires an invariant translated range, not merely a finite-dimensional parameter space of source vectors.

## 12. Relation to the ambient no-go of series 48

Series-48 showed that the exact compact equations generate an irrational sliding-window cocycle on the ambient source space.

The present pass shows what changes after intersection with K_c:

not the residue geometry;

not the dense arithmetic orbit;

not raw translation invariance.

What changes is that raw translation ejection becomes dynamically observable because a nonzero invariant subspace inside K_c is impossible.

Thus the kernel restriction turns the ambient cocycle into a finite-dimensional ejection-matching problem.

That is the correct use of finite dimensionality.

## 13. Relation to GERM-11 and GERM-16

GERM-11 proved dynamic observability of the moment-intertwining defect on a finite-dimensional edge obstruction.

The present theorem is the source-side analogue:

boxed:
raw ejection itself is dynamically observable.

GERM-16 proved a dyadic escape filtration for a jointly-superflat visible family.

The present theorem does not require visible superflatness.

It applies to every finite-dimensional

V subset K_c.

The price is that it detects ejection from V, not necessarily immediate escape from the entire regular kernel K_c.

## 14. Kernel/nonkernel split of the ejection burden

Let

Pi_K

be the orthogonal projection onto the full regular kernel K_c.

For each arithmetic shift split

E_{lambda,sigma}
=
H_{lambda,sigma}
+
N_{lambda,sigma},

where

H_{lambda,sigma}
=
(Pi_K-Pi)S_lambda^sigma|_V

lies in

K_c intersect V^perp,

and

N_{lambda,sigma}
=
(I-Pi_K)S_lambda^sigma|_V

lies in

K_c^perp.

The prime ejection balance splits orthogonally into

H_{a,+}
+
H_{a,-}
+
beta(H_{b,+}+H_{b,-})
+
gamma(H_{c4,+}+H_{c4,-})
+
delta(H_{d5,+}+H_{d5,-})
=
0,

and

N_{a,+}
+
N_{a,-}
+
beta(N_{b,+}+N_{b,-})
+
gamma(N_{c4,+}+N_{c4,-})
+
delta(N_{d5,+}+N_{d5,-})
=
0.

Thus the compensator burden is separately carried by:

- regular-kernel escape outside V;
- genuine nonkernel escape.

This is the correct interface with GERM-13/16.

## 15. What would now prove V=0

The dynamic theorem says the first-prime ejection family

{E A^m}_{m<d}

separates V.

Prime silence says the compensator family

{C A^m}_{m<d}

is exactly its negative.

Therefore it would suffice to prove any one of:

1. compensator rank defect:
   the family {C A^m}_{m<d} cannot separate a nonzero V;

2. support separation:
   the first-prime ejection has a carrier not reachable by the compensator delays;

3. moment spectral separation:
   a finite moment chart distinguishes E A^m from C A^m by incompatible delay multipliers;

4. kernel/nonkernel mismatch:
   the blockwise balance in Section 14 is incompatible with the GERM-13 boundary-strip screw fields;

5. near-return holonomy mismatch:
   irrational arithmetic returns force two distinct compensator words to approximate the same source translation while inducing incompatible finite-dimensional compressed operators.

None is proved here.

## 16. Fixed-L status

This pass does not prove

K_c^{ps}=0

beyond the existing positive range.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

Series 33-48 remain non-load-bearing for any claimed extension beyond that threshold.

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-50 / EJECTION COMPENSATOR SEPARATION

The next pass should attack the exact identity

E_{a,+}
=
-
[
E_{a,-}
+
beta(E_{b,+}+E_{b,-})
+
gamma(E_{c4,+}+E_{c4,-})
+
delta(E_{d5,+}+E_{d5,-})
]

on a hypothetical nonzero V=K_c^{ps}.

Priority:

1. project the identity into K_c^perp and K_c intersect V^perp;
2. use GERM-13 to express each nonkernel block by its boundary-strip screw field;
3. exploit the nested strip widths a<b<c4<d5 to seek a triangular support or moment separation;
4. apply the identity to the compressed first-prime orbit A^m V, m<d, where dynamic ejection observability gives a fixed-scale lower bound.

A separation theorem at this stage would finally use both prime silence and the full regular-kernel structure and could prove K_c^{ps}=0 in the four-delay chamber.

No public promotion and no canonical cursor movement are asserted.
