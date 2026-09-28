# SZ edge recurrence 63 — multikappa parity atomization and mixed-return onset

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-62
Public promotion: forbidden

## Objective

Extend the first-return-free parity closure of series-62 into the chamber where the lower defect contains repeated kappa-returns.

Series-62 closed

0<e<=kappa,

where

kappa=k-5h,

h=log(81/80),

k=log(16/15).

The present pass proves that one-scale kappa-chain atomization remains complete substantially farther.

The exact endpoint is

boxed:
lambda_ret
=
h-kappa
=
6h-k.

Through

boxed:
kappa<e<=lambda_ret,

every generic lower-defect orbit is a finite kappa-chain, possibly one link longer on the moving remainder interval.

Only five constant orbit templates occur:

boxed:
124, 186, 248, 310, 372.

All five are certified nonresonant for both parity signs by outward interval LU.

At

e=lambda_ret

the next independent return only touches an endpoint.

For

e>lambda_ret

a second internal return becomes active:

t -> t+lambda_ret.

Since lambda_ret/kappa is irrational, one periodic kappa-chain atomization cannot remain globally complete beyond this threshold.

Thus this pass both extends the ambient prime-channel injectivity interval and identifies the exact onset of the genuine mixed-return cocycle.

## 1. Constants

Retain the parity-recurrence constants

j=log(9/8),

p=log(10/9),

h=j-p=log(81/80),

k=log(16/15),

kappa=k-5h.

Series-61 proves

kappa>0.

Define

boxed:
lambda_ret
=
h-kappa
=
6h-k.

Numerically,

kappa
=
0.0024259211447856...,

lambda_ret
=
0.0099965988537715...,

h
=
0.0124225199985571....

Also

boxed:
4 kappa
<
lambda_ret
<
5 kappa.

Indeed,

lambda_ret/kappa
=
h/kappa-1
=
4.1207435267....

The chamber treated here is

boxed:
kappa<e<=lambda_ret.

## 2. The existing kappa-return

Series-61 derives the exact lower-defect return

boxed:
t <-> t+kappa

between

0<t<e-kappa

and

kappa<t<e.

Thus the lower defect

(0,e)

is foliated by partial arithmetic chains with step kappa.

For the chamber of this pass no second independent internal return is yet present.

## 3. Kappa-chain decomposition

Write

boxed:
e
=
n kappa
+
rho,

with

n=floor(e/kappa),

0<=rho<kappa.

Since

kappa<e<=lambda_ret<5kappa,

one has

boxed:
n in {1,2,3,4}.

Fix a generic fundamental seed

y in(0,kappa),

avoiding:

- y=rho;
- reflection fixed points;
- recurrence boundaries and their finitely many affine preimages.

The lower-defect kappa-chain is

C_y
=
{
y,
y+kappa,
y+2kappa,
...
}
intersect(0,e).

Therefore:

if

0<y<rho,

the chain has

boxed:
n+1

points;

if

rho<y<kappa,

the chain has

boxed:
n

points.

At rho=0 only the n-point case occurs almost everywhere.

The exceptional seed set is finite modulo kappa and therefore null for the L2 problem.

## 4. Orbit-shell structure

Start with one lower-defect kappa-chain.

Close it under the exact parity recurrence:

- the parity reflection;
- the j-incidence path;
- the p-reflection path;
- the h-transfer chain;
- the k-sheet bridge;
- the exact tail equations.

Before the second return threshold lambda_ret, adding one extra lower-defect kappa point adds one fixed recurrence shell of

boxed:
62

source coordinates and 62 scalar rows.

Hence a chain with m lower-defect points produces a generic square orbit matrix of dimension

boxed:
62(m+1).

The initial +1 is the fixed reflected/tail shell already present in the first-return-free chamber.

Therefore the only possible generic dimensions are

m=1 -> 124,

m=2 -> 186,

m=3 -> 248,

m=4 -> 310,

m=5 -> 372.

This is the single-scale multikappa parity chamber registered in the terminology file.

## 5. Chamber/template table

Let

e=n kappa+rho.

For each n:

### n=1

kappa<e<2kappa.

Seeds

0<y<rho

give the 186 template.

Seeds

rho<y<kappa

give the 124 template.

### n=2

2kappa<e<3kappa.

The two templates are

248

and

186.

### n=3

3kappa<e<4kappa.

The two templates are

310

and

248.

### n=4

4kappa<e<=lambda_ret.

The two templates are

372

and

310.

At exact multiples of kappa the longer template has zero fundamental-seed width and disappears almost everywhere.

Thus the complete generic template library through lambda_ret is exactly

boxed:
{124,186,248,310,372}.

No e-dependent coefficients occur.

Only the combinatorial choice of template changes.

## 6. Coefficient species

As in series-62, the original parity recurrence uses only

1,

beta,

c=beta gamma,

d0=delta gamma,

and their parity-signed negatives.

With

gamma=1/sqrt2,

boxed:
beta
=
(log3/log2)sqrt(2/3),

boxed:
c
=
(log3/log2)/sqrt3,

boxed:
d0
=
(log5/log2)/sqrt5.

Therefore every template has the same three nontrivial scalar coefficient species.

## 7. Certified coefficient input

Use the exact rational logarithmic enclosures already employed in series-38 through series-62:

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

Outward interval square-root arithmetic supplies certified intervals for

beta,

c,

d0.

The helper is

tools/sz_parity_multikappa_audit.py.

The floating values of e and the generic seed in that helper choose topology only.

They do not enter the determinant coefficient intervals.

## 8. Representative templates

One generic representative of each topology is used:

dimension 124:
e=1.20 kappa,
seed=0.23 kappa;

dimension 186:
e=1.20 kappa,
seed=0.07 kappa;

dimension 248:
e=2.20 kappa,
seed=0.07 kappa;

dimension 310:
e=3.20 kappa,
seed=0.07 kappa;

dimension 372:
e=4.10 kappa,
seed=0.07 kappa.

Each representative lies strictly inside the corresponding combinatorial cell.

The geometry of Sections 3-5 proves that every generic orbit in the chamber is isomorphic to one of these templates.

## 9. Outward determinant audit

For both parity signs separately, outward interval LU gives:

### 124 template

boxed:
139.5135271107
<
det M_124
<
139.5382400239.

### 186 template

boxed:
-1620.655510627
<
det M_186
<
-1620.243521821.

### 248 template

boxed:
-18822.96256669
<
det M_248
<
-18816.69195700.

### 310 template

boxed:
218526.2185188
<
det M_310
<
218619.0210795.

### 372 template

boxed:
2537815.294361
<
det M_372
<
2539169.703261.

Every interval excludes zero by a wide margin.

Both parity signs are audited independently.

They happen to receive the same determinant enclosures under the chosen row/column convention; no parity symmetry theorem is needed.

## 10. Orbitwise consequence

Fix one generic orbit and one parity.

Its recurrence system is

M X=0

for one matrix from the five-template library.

Section 9 gives

det M !=0.

Therefore every coordinate in the orbit vanishes.

The exceptional seeds are a null set.

Hence

boxed:
x=0 almost everywhere

for both parity sectors throughout

boxed:
0<e<=lambda_ret.

By the exact reconstruction of series-60,

boxed:
ker P_c={0}

through the same interval.

## 11. Ambient injectivity extension

Recall

e=L-log(16/3).

Therefore series-31, series-62, and the present pass combine to give ambient four-delay prime-channel injectivity for

boxed:
0<L<=L_ret,

where

L_ret
=
log(16/3)+lambda_ret.

Since

lambda_ret
=
6log(81/80)-log(16/15),

one gets

exp(L_ret)
=
(16/3)
(81/80)^6
(15/16)

=
boxed:
3^24/(2^24 5^5).

Therefore

boxed:
L_ret
=
log(
3^24/(2^24 5^5)
)
=
1.68397303242544....

This strictly extends the series-62 endpoint

1.67640235471646....

## 12. Consequence for the regular kernel

Ambient prime silence is trivial throughout the new interval.

Therefore

boxed:
K_c^{ps}
=
K_c intersect ker P_c
=
{0}

for

boxed:
L<=L_ret.

So the fixed-scale prime-channel norm gap on the finite-dimensional regular kernel extends through L_ret.

No uniform lower bound as L varies is asserted.

## 13. The next return appears at lambda_ret

The single-scale closure ends for an exact geometric reason.

Series-61 gives an admissible h-step

t -> t+h

on the appropriate head interval and the inverse k-bridge

t -> t-k

for k<t<u.

Take

0<t<e-lambda_ret.

Apply six forward h-steps:

t
-> t+h
-> ...
-> t+6h.

Because

lambda_ret=6h-k,

the last point satisfies

t+6h>k

and, precisely under

t<e-lambda_ret,

lies below

u=k+e.

The inverse k-bridge is therefore admissible:

t+6h
->
t+6h-k
=
t+lambda_ret.

Hence

boxed:
t <-> t+lambda_ret

is a genuine internal return on

0<t<e-lambda_ret.

At

e=lambda_ret

the interval is empty.

For

e>lambda_ret

it has positive length.

This is the mixed-return onset registered in the terminology file.

## 14. Irrationality of the two scales

Because

lambda_ret
=
h-kappa,

if

lambda_ret/kappa

were rational, then

h/kappa
=
1+lambda_ret/kappa

would be rational.

Series-61 proves

h/kappa notin Q.

Therefore

boxed:
lambda_ret/kappa notin Q.

Once

e>lambda_ret,

both:

- the kappa-return;
- the lambda_ret-return

are internal on nonempty subintervals.

Thus the exact recurrence carries a two-scale partial irrational cocycle.

This sharpens the coarser series-61 statement that placed the decisive transition at e=h.

The first mixed return actually appears earlier:

boxed:
e=h-kappa.

## 15. Why the finite template library stops here

Through e=lambda_ret, every generic lower-defect return belongs to the one-dimensional arithmetic family

y+n kappa.

The orbit graph can therefore be atomized by the fundamental interval

(0,kappa).

For e>lambda_ret, the new return shifts the fundamental residue by

lambda_ret mod kappa.

Because the ratio is irrational, repeated legal compositions do not preserve a finite periodic residue alphabet.

This does not prove that individual orbits are infinite.

It proves that the chamber cannot be globally represented by the finite one-scale template library of Sections 3-9.

A new cocycle argument is required.

## 16. Relation to the series-61 low-head cocycle

Series-61 identified two internal scales

h

and

kappa

once e>h.

The present pass improves the onset analysis.

Before h itself fits wholly inside the lower defect, the composite path

6h-k
=
h-kappa

already produces a second independent return.

Therefore the corrected progression is:

### Return-free

0<e<=kappa.

Closed by series-62.

### Single-scale multikappa

kappa<e<=h-kappa.

Closed here.

### Mixed-return cocycle

h-kappa<e<=j.

Open.

Within the final branch the coefficient pattern still changes at

e=p,

but the two-scale return geometry is already present below p.

## 17. Result

The entire one-scale parity regime is now closed.

Positive:

1. repeated kappa-returns admit an exact fundamental-chain decomposition;
2. only five generic orbit templates occur;
3. all five determinants are certified nonzero for both parities;
4. ambient prime-channel injectivity extends to
   L<=log(3^24/(2^24 5^5));
5. K_c^{ps}=0 extends through the same interval;
6. the exact first mixed-return threshold is
   e=h-kappa.

Correction:

the genuine two-scale cocycle starts at

boxed:
e>h-kappa,

not only at e>h.

## Fixed-L status

The new load-bearing experimental ambient prime-channel range is

boxed:
0<L<=
log(
3^24/(2^24 5^5)
).

This remains an unratified residue theorem.

The canonical theorem cursor remains

boxed:
SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

boxed:
SZ-KERNEL-EDGE-GERM-64 / MIXED-RETURN PARITY COCYCLE.

The remaining chamber is

boxed:
h-kappa<e<=j.

The next pass should:

1. work with the two internal return scales
   kappa
   and
   lambda_ret=h-kappa;

2. derive the exact partial-return matrices, not only their incidence paths;

3. determine whether the two return maps commute, generate a contractive/hyperbolic cocycle, or preserve a common indefinite form;

4. exploit the parity reflection to reduce the cocycle to one fundamental interval whenever possible;

5. separate the coefficient subchambers
   h-kappa<e<p
   and
   p<=e<=j;

6. seek a norm-growth or spectral-separation theorem that rules out an L2 fixed section without requiring periodic residue closure.

A positive cocycle theorem would complete ambient four-delay prime-channel injectivity through L=log6.

No public promotion and no canonical cursor movement are asserted.
