# SZ edge recurrence 62 — first-return-free parity closure

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-61
Public promotion: forbidden

## Objective

Close the first genuinely uniform subchamber of the parity edge recurrence from series-61.

Series-61 reduced the post-log(16/3) four-delay prime-silent problem to one scalar parity recurrence with parameter

e=L-log(16/3),

0<e<=j=log(9/8),

and isolated the short lower-defect return

kappa=k-5h.

The original next target proposed the larger interval

0<e<=h.

That is too ambitious for one constant orbit template: once translated lower-defect returns become active, additional orbit types appear.

The present pass therefore closes only the exact first-return-free chamber

boxed:
0<e<=kappa.

In that chamber every generic orbit has one fixed 124-by-124 coefficient matrix, and an outward interval determinant audit excludes resonance for both parity signs.

This gives the first load-bearing ambient prime-channel injectivity extension beyond

L=log(16/3).

## 1. Constants

Retain

h=log(81/80),

k=log(16/15),

and define

boxed:
kappa
=
k-5h
=
log[
(16/15)(80/81)^5
].

Series-61 proved

kappa>0.

Numerically,

kappa
approximately
0.0024259211448.

The chamber closed here is

boxed:
0<e<=kappa.

## 2. Why this is the first return-free chamber

The exact parity recurrence incidence graph has:

- the old h-translation path;
- one k-sheet bridge;
- the first short lower-defect return

t
->
t+k
->
t+k-h
->
...
->
t+k-5h
=
t+kappa.

For a translated lower-defect return to remain strictly inside

(0,e),

one needs a nonempty interval

0<t<e-kappa.

Hence when

boxed:
e<=kappa,

the first translated return has empty interior.

In the exact recurrence graph, the only generic lower-defect companion of a point

t in (0,e)

is therefore its parity reflection

e-t.

The boundary case

e=kappa

creates only endpoint contact and changes no L2 statement.

This is the first-return-free parity chamber registered in the terminology file.

## 3. Generic orbit template

Fix one parity

epsilon in {+1,-1}.

Choose a generic seed

t in (0,e)

that avoids all recurrence boundaries and their finitely many affine preimages.

Starting from the exact scalar equations of series-60/61 and recursively adjoining every sampled coordinate gives a finite orbit.

In the first-return-free chamber:

boxed:
the generic orbit has 124 distinct source coordinates,

and

boxed:
the exact recurrence supplies 124 scalar rows.

The coefficient pattern is independent of:

- e in (0,kappa];
- the generic seed t;
- the location of the orbit inside the chamber;

up to coordinate relabeling.

The parity sign changes only the signs of the reflected coefficients.

The exceptional seeds form a finite union of affine points and hence have measure zero.

Therefore the L2 recurrence decomposes almost everywhere into copies of one finite orbit matrix for each parity.

## 4. Exact coefficient species

The original parity recurrence uses only the scalar coefficients

1,

beta,

c=beta gamma,

d0=delta gamma,

and their parity-signed negatives.

With

gamma=1/sqrt2,

one has

boxed:
beta
=
(log3/log2)
sqrt(2/3),

boxed:
c
=
(log3/log2)/sqrt3,

boxed:
d0
=
(log5/log2)/sqrt5.

Thus the determinant certificate needs only the two logarithmic ratios and elementary square roots.

## 5. Certified input intervals

Reuse the exact rational logarithmic enclosures from the earlier scattering audits:

boxed:
1.5849625
<
log3/log2
<
1.5849626,

boxed:
2.3219280
<
log5/log2
<
2.3219281.

Together with outward interval square-root evaluation, these give certified intervals for

beta,

c,

d0.

No floating logarithm is used as a load-bearing determinant input.

The audit helper is

tools/sz_parity_first_return_audit.py.

## 6. Representative template

Because Section 3 proves the coefficient template is chamber-independent, one generic representative may be used to instantiate it.

The audit script uses, only for topology selection,

e=0.001,

t=0.000137.

For either parity this produces a

124-by-124

sparse matrix with

320

nonzero entries.

Only the coefficient intervals of Section 5 enter the determinant certification.

## 7. Outward interval LU audit

A fixed partial-pivot LU ordering is chosen from the midpoint matrix.

Every corresponding interval pivot excludes zero.

Outward interval elimination then gives, for parity

epsilon=+1,

boxed:
139.5135271107
<
det M_+
<
139.5382400239.

For parity

epsilon=-1,

the separate audit gives the same certified enclosure:

boxed:
139.5135271107
<
det M_-
<
139.5382400239.

In particular,

boxed:
det M_epsilon !=0

for both parity signs.

The numerical equality of the two determinant intervals is not used as a symmetry theorem; both signs are audited separately.

## 8. Orbitwise consequence

Take one generic orbit.

The 124 recurrence rows form a homogeneous linear system

M_epsilon X=0.

Section 7 gives

det M_epsilon !=0.

Therefore

X=0.

Thus the source profile vanishes at every point of every generic orbit.

Since the exceptional orbit seeds are null,

boxed:
x=0 almost everywhere

for either parity.

By the exact reconstruction of series-60, the corresponding edge source h and original source f are also zero.

## 9. Ambient prime-channel injectivity extension

The parity decomposition exhausts the ambient four-delay prime-silent space.

Therefore

boxed:
ker P_c
=
{0}

through

boxed:
0<e<=kappa.

Combining with the previously load-bearing interval through e=0 gives ambient prime-channel injectivity for

boxed:
0<L<=L_kappa,

where

L_kappa
=
log(16/3)+kappa.

Exponentiating,

exp(L_kappa)
=
(16/3)(16/15)(80/81)^5

=
boxed:
2^28 5^4 / 3^22.

Hence

boxed:
L_kappa
=
log(
2^28 5^4 / 3^22
)
approximately
1.67640235471646.

This strictly extends the previous endpoint

log(16/3)
approximately
1.67397643357167.

## 10. Consequence for the regular kernel branch

Since ambient prime silence is trivial,

boxed:
K_c^{ps}
=
K_c intersect ker P_c
=
{0}

through the same extended interval.

Therefore the fixed-scale prime-channel norm gap on the finite-dimensional regular kernel extends through

L<=L_kappa.

No uniformity in L is asserted.

## 11. Scope correction to the series-61 next target

Series-61 proposed treating

0<e<=h

as one small-defect finite-depth branch.

The present pass shows that one **constant orbit template** is justified only in the first-return-free subchamber

0<e<=kappa.

Once

e>kappa,

the lower defect contains a genuine translated kappa-return interval.

The recurrence is still finite on many individual orbit atoms, but the atom library is no longer the single 124-point template.

Thus the correct progression is:

1. first-return-free chamber:
   0<e<=kappa
   — CLOSED here;

2. multi-kappa return chamber:
   kappa<e<=h
   — still to be atomized/certified;

3. upper return-cocycle chamber:
   h<e<=j
   — series-61 already shows that one periodic residue mesh is not globally valid.

No statement here rules out a finite piecewise atomization inside the second branch.

## 12. Relation to the earlier recurrence experiments

The direct orbit reconnaissance in series-61 found:

- 124-point generic orbits for small e;
- larger finite orbit templates as e increased;
- rapid growth near the top of the proposed small-defect range.

The present theorem identifies the 124-point regime exactly:

boxed:
0<e<=kappa.

So the numerical transition was not accidental.

It is the activation of the first nontrivial lower-defect translated return.

## 13. Result

The first post-log(16/3) parity chamber is closed.

Positive:

1. the exact lower defect is return-free for
   0<e<=kappa;
2. every generic parity orbit has one 124-by-124 constant matrix template;
3. both parity determinants have certified positive interval
   (139.5135,139.5383);
4. therefore the ambient four-delay prime operator remains injective;
5. the regular prime-silent branch remains trivial;
6. the load-bearing fixed-L positive interval extends strictly beyond log(16/3).

The new load-bearing experimental range is

boxed:
0<L<=
log(
2^28 5^4 / 3^22
).

This is still an unratified residue result and does not move the canonical theorem cursor.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-63 / MULTI-KAPPA PARITY ATOMIZATION

The next pass should treat

boxed:
kappa<e<=h.

Priority:

1. use the lower-defect kappa-chain decomposition;
2. partition the fundamental seed interval by the moving terminal remainder
   e mod kappa;
3. enumerate the finitely many orbit templates before the h-return becomes fully internal;
4. certify each parity determinant by the same outward interval method;
5. determine the maximal finite-atom endpoint before the genuine two-scale cocycle takes over.

Canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
