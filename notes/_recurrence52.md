# SZ edge recurrence 52 — spectral-ejection custody and two-stage nonkernel escape

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-51
Public promotion: forbidden

## Objective

Start from the dimension-free seven-step spectral ejection theorem of series-51 on

V = K_c^{ps}

and determine whether the observable escape can be absorbed entirely by regular-kernel directions outside V.

The answer is no.

In the four-delay chamber, any regular-kernel escape is forced into K_c^perp within at most two further one-sided first-prime shifts.

Consequently the seven-step spectral observable admits a finite 21-channel detector landing entirely in K_c^perp.

This is the desired finite escape-tree theorem.

It does not yet prove V=0, because a fixed-scale nonkernel escape field has not been transferred back to the shrinking collar.

## 1. Spectral-ejection input

Use the notation of series-51.

Let

V=K_c^{ps}

and let

Pi_V

be the orthogonal projection onto V.

Split the normalized prime operator into

D+N,

where

D=C_(log2)+gamma C_(log4)

and

N=beta C_(log3)+delta C_(log5).

On V,

N=-D.

Define

B=Pi_V D|_V,

F=(I-Pi_V)D|_V.

Series-51 proves the dimension-free estimate

boxed:
sum_(m=0)^6 ||F B^m f||^2
>=
nu_*^2 ||f||^2

for every f in V,

where nu_*>0 depends only on the fixed four-delay Weil weights.

## 2. Split the ejection by regular-kernel custody

Let

K=K_c,

Pi_K

be the orthogonal projection onto K, and

Q_K=I-Pi_K.

Since V subset K,

I-Pi_V
=
(Pi_K-Pi_V)+Q_K

orthogonally.

Define

H
=
(Pi_K-Pi_V)D|_V,

M
=
Q_K D|_V.

Then

F=H+M,

with

Ran(H) subset K intersect V^perp,

Ran(M) subset K^perp.

For

m=0,...,6,

write

H_m(f)=H B^m f,

M_m(f)=M B^m f.

The two outputs are orthogonal, so

boxed:
||F B^m f||^2
=
||H_m(f)||^2
+
||M_m(f)||^2.

Therefore the seven-step floor becomes

boxed:
sum_(m=0)^6
[
||H_m(f)||^2
+
||M_m(f)||^2
]
>=
nu_*^2 ||f||^2.

## 3. First-prime escape on the full kernel

Let

a=log2,

T=S_a^+

be the one-sided truncated first-prime shift in right-oriented source coordinates.

Throughout the four-delay chamber

log5<L<=log6,

one has

2a<L<3a.

Therefore

boxed:
T^3=0.

GERM-8 proves

boxed:
K intersect ker(T)={0}.

This is enough to obtain a dimension-free two-stage detector on the full regular kernel.

## 4. Two-stage nonkernel escape theorem

Define

J_K:
K -> K^perp direct_sum K^perp

by

J_K g
=
(
Q_K T g,
Q_K T^2 g
).

Claim:

boxed:
ker J_K={0}.

Suppose

Q_K T g=0

and

Q_K T^2 g=0.

Then

Tg in K,

T^2g in K.

Since

T^3g=0,

we have

T(T^2g)=0.

Because

T^2g in K intersect ker(T),

GERM-8 gives

T^2g=0.

Now

Tg in K

and

T(Tg)=0,

so again

Tg=0.

Finally

g in K

and

Tg=0,

so

g=0.

Thus J_K is injective.

This is the two-stage nonkernel escape detector registered in the terminology file.

## 5. Quantitative kernel escape floor

The regular kernel K is finite dimensional.

Therefore injectivity of J_K gives a fixed constant

nu_K>0

such that

boxed:
||Q_K T g||^2
+
||Q_K T^2 g||^2
>=
nu_K^2 ||g||^2

for every g in K.

This constant may depend on c and the regular kernel K_c.

No uniformity in c is asserted.

## 6. Apply the kernel detector to the H-block

For each

m=0,...,6,

the vector

H_m(f)

lies in K.

Therefore

||Q_K T H_m(f)||^2
+
||Q_K T^2 H_m(f)||^2

>=

nu_K^2 ||H_m(f)||^2.

Sum over m.

Define the 21-channel nonkernel observation

O_NK f

to consist of

M_m(f),

Q_K T H_m(f),

Q_K T^2 H_m(f),

for

m=0,...,6.

Every component lies in K^perp.

Its squared norm satisfies

||O_NK f||^2

=
sum_(m=0)^6
[
||M_m(f)||^2
+
||Q_K T H_m(f)||^2
+
||Q_K T^2 H_m(f)||^2
]

>=

sum_(m=0)^6
[
||M_m(f)||^2
+
nu_K^2 ||H_m(f)||^2
].

Hence

boxed:
||O_NK f||^2
>=
min(1,nu_K^2)
sum_(m=0)^6
[
||M_m(f)||^2+||H_m(f)||^2
].

Using the seven-step spectral floor,

boxed:
||O_NK f||
>=
nu_* min(1,nu_K) ||f||.

Therefore O_NK is injective on V.

This proves the finite escape-tree theorem.

## 7. Exact channel count

The detector has:

- seven primary channels
  M B^m;

- seven first-secondary channels
  Q_K T H B^m;

- seven second-secondary channels
  Q_K T^2 H B^m.

Thus there are exactly

boxed:
21

operator channels before any redundant channels are removed.

The depth is uniformly bounded:

spectral depth at most 7,
then kernel-escape depth at most 2.

Neither depth depends on dim(V).

## 8. No indefinite regular-kernel absorption

Suppose all seven primary nonkernel channels vanished:

M B^m f=0

for m=0,...,6.

Then the seven-step spectral floor is carried entirely by the regular-kernel escapes H_m.

But Section 6 shows that the first two dyadic translates of those H_m produce a nonkernel observation satisfying the same fixed-scale lower bound up to nu_K.

Therefore regular-kernel escape cannot absorb the spectral mismatch indefinitely.

Every nonzero f in V has a nonzero K^perp witness among the 21 channels.

This is the exact custody statement sought in series-51.

## 9. Fixed-scale screw-field detector

Let

W_NK

be the finite-dimensional sum of the ranges of the 21 nonkernel channels.

Then

W_NK subset K^perp.

Since

K=ker G_c,

the restriction

G_c|_(W_NK)

is injective.

Finite dimensionality gives

tau_NK>0

such that

||G_c w||
>=
tau_NK ||w||

for every w in W_NK.

Therefore

boxed:
sum over all 21 channels L_i of
||G_c L_i f||^2
>=
tau_NK^2 nu_*^2 min(1,nu_K^2) ||f||^2.

So the nonkernel escape is detectable not only in source norm but also through its old-interior screw field at fixed scale.

No global inverse estimate on all of K^perp is used.

Only the finite-dimensional generated escape range is inverted.

## 10. Boundary-strip interpretation of the primary channels

Take

g_m=B^m f in V subset K.

The primary channel is

M_m
=
Q_K D g_m

=
Q_K
[
C_a
+
gamma C_(2a)
]
g_m.

Each symmetric shift is a sum of two one-sided truncated translations.

For a kernel vector, GERM-13 identifies the nonkernel component of each one-sided translate with the nonconstant screw field generated by the boundary strip discarded by that translation.

Therefore the old-interior screw field of M_m is a fixed linear combination of:

- right and left a-strip screw fields;
- right and left 2a-strip screw fields.

The additive kernel constants disappear after applying Q_K / G_c.

Thus every primary nonkernel witness has explicit dyadic boundary-strip custody.

## 11. Boundary-strip interpretation of the secondary channels

Each

H_m in K.

The first-secondary channel is

Q_K T H_m,

which is the nonkernel escape of a one-sided a-shift of a kernel vector.

GERM-13 identifies its nonconstant interior screw field with the discarded a-strip potential of H_m.

The second-secondary channel is

Q_K T^2 H_m.

Since

T^2=S_(2a)^+,

its nonconstant interior field is the discarded 2a-strip potential of H_m.

Thus every one of the 21 detector channels has a fixed-width boundary-strip screw-field interpretation.

No abstract K^perp direction remains untyped.

## 12. What has been achieved

For a hypothetical nonzero

V=K_c^{ps},

the chain now gives:

1. prime silence splits into incompatible finite-spectrum dyadic/nondyadic blocks;
2. their shared ejection is observable in seven steps with weight-uniform constant nu_*;
3. any portion of that ejection landing back in the regular kernel is forced out of K in at most two further first-prime shifts;
4. the resulting 21-channel observation lands entirely in K^perp;
5. it has a positive fixed-scale source-norm floor;
6. on its finite-dimensional image it also has a positive old-interior screw-field floor;
7. every channel is an explicit a- or 2a-boundary-strip screw field.

Therefore the prime-silent problem has been reduced from spectral transport to a finite family of concrete nonkernel boundary-strip fields.

## 13. What is still missing

A nonzero fixed-scale nonkernel boundary-strip field is not itself a contradiction.

The original edge obstruction is controlled by the shrinking collar

epsilon -> 0.

The detector in this pass uses fixed arithmetic widths

a=log2,

2a=log4.

No theorem currently shows that a fixed positive lower bound on one of these 21 nonkernel fields forces a finite-order lower bound for the original shrinking collar observation.

This is the same fixed-scale-to-shrinking-scale interface isolated earlier in GERM-13 through GERM-17, but it is now reached from the prime-silent spectral route with a uniform finite-depth detector.

## 14. Fixed-L status

This pass still does not prove

K_c^{ps}=0

in the whole four-delay chamber.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-53 / NONKERNEL FIELD RETURN

The next pass should start from the 21-channel field floor

sum_i ||G_c L_i f||^2
>=
c_V^2 ||f||^2

and test whether the explicit a/2a boundary-strip fields can be returned to the original prime-silent/collar equations.

Priority:

1. write the 21 fields directly in terms of original source-cell restrictions of f and the compressed spectral orbit B^m f;
2. exploit prime silence to compare those dyadic strip fields with the log3/log5 edge algebra;
3. test whether the field detector can be localized at one of the finitely many ratified singular sites Sigma_c;
4. seek a finite-order lower bound for a shrinking local Volterra observation generated by at least one detector channel.

A positive return theorem would connect the fixed-scale prime-silent detector to the canonical shrinking-collar obstruction.

No public promotion and no canonical cursor movement are asserted.
