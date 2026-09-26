# SZ-KERNEL-EDGE-GERM-18 — Blind-transform filtration and Stieltjes boundary normal form

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-17  
**Target tested:** BLIND-TRANSFORM FILTRATION  
**Public promotion:** forbidden

## 0. Objective

GERM-17 derived the exact first-prime threshold equation

\[
\frac{\log2}{\sqrt2}\,g(\eta)
+
\int_0^{\log2}
a_\infty''(\eta+r)g(\log2-r)\,dr
=
0
\]

at every dyadic step that remains in the regular kernel.

The visible endpoint term is superflat on the terminal visible-germ
obstruction.

Hence the remaining local carrier is the archimedean transform of the
one-sided blind source cell.

This pass treats that transform as the primary object.

The main results are:

1. the blind transform is injective as a function germ on every fixed blind
   cell;
2. on every finite-dimensional blind-cell family, its flatness filtration
   stabilizes at finite order;
3. on the stabilized superflat-transform subspace, superflatness is uniform in
   operator norm;
4. a nonzero superflat-transform source must remain locally nontrivial in
   **every** neighborhood of the blind hinge;
5. the transform has an exact Stieltjes boundary normal form at
   \[
   z=1,
   \]
   so the surviving branch is precisely a finite-dimensional family of
   Stieltjes boundary germs.

Thus the dyadic reduction has reached a sharply typed local obstruction.

It has not yet eliminated it.

---

# I. First-prime blind-cell operator

## 1. Cell width

Set

\[
a=\log2.
\]

For a blind-cell profile

\[
b\in L^2(0,a),
\]

define

\[
\boxed{
(\mathscr T b)(\eta)
=
\int_0^a
a_\infty''(\eta+r)b(r)\,dr,
\qquad
\eta>0.
}
\]

This is the blind transform registered in the terminology file.

For the dyadic threshold equation of GERM-17,

\[
b(r)=g(a-r).
\]

Thus \(r=0\) is the blind side of the next dyadic hinge.

---

# II. Explicit exponential form

## 2. Suzuki archimedean second derivative

GERM-2 proved

\[
\boxed{
a_\infty''(t)
=
-e^{t/2}
+
\sum_{m=1}^\infty
e^{-\lambda_m t},
\qquad
\lambda_m=2m+\frac12.
}
\]

For every fixed

\[
\eta>0,
\]

the exponential series may be integrated termwise against \(b\in L^2(0,a)\).

Define

\[
\boxed{
A_+(b)
=
\int_0^a e^{r/2}b(r)\,dr
}
\]

and

\[
\boxed{
A_m(b)
=
\int_0^a e^{-\lambda_m r}b(r)\,dr.
}
\]

Then

\[
\boxed{
(\mathscr T b)(\eta)
=
-e^{\eta/2}A_+(b)
+
\sum_{m=1}^\infty
e^{-\lambda_m\eta}A_m(b).
}
\]

For \(\eta>0\) the series converges normally on compact subsets.

---

# III. Injectivity of the blind transform

## 3. Vanishing transform

Suppose

\[
\mathscr T b=0
\]

on a nonempty open \(\eta\)-interval.

Set

\[
q=e^{-\eta/2}.
\]

Then

\[
0<q<1,
\]

and

\[
e^{\eta/2}=q^{-1},
\qquad
e^{-\lambda_m\eta}=q^{4m+1}.
\]

Therefore

\[
\boxed{
-A_+(b)q^{-1}
+
\sum_{m=1}^{\infty}
A_m(b)q^{4m+1}
=
0
}
\]

on a nonempty interval inside the unit disk.

The left side is a convergent Laurent/power series there.

Uniqueness gives

\[
A_+(b)=0
\]

and

\[
A_m(b)=0
\qquad
\forall m\ge1.
\]

---

## 4. Moment completeness

Set

\[
x=e^{-2r}.
\]

Then

\[
r\in(0,a)
\quad\Longleftrightarrow\quad
x\in(1/4,1).
\]

The moments \(A_m(b)\) become polynomial moments

\[
\int_{1/4}^{1}
x^m h(x)\,dx
\]

after multiplication by a fixed nonvanishing weight.

Polynomials are dense in

\[
L^2(1/4,1).
\]

Hence

\[
A_m(b)=0
\quad
\forall m\ge1
\]

forces

\[
b=0.
\]

Therefore

\[
\boxed{
\mathscr T b\equiv0
\Longrightarrow
b=0.
}
\]

Equivalently, for every fixed \(\varepsilon>0\),

\[
\boxed{
b\longmapsto
\mathscr T b|_{(0,\varepsilon)}
}
\]

is injective.

---

# IV. Blind-cell families from dyadic escape layers

## 5. Cell map

Take one dyadic escape layer

\[
L_j
\]

from GERM-16.

For

\[
f\in L_j,
\]

the last kernel-contained iterate is

\[
g_f=S_a^jf.
\]

Define its reversed blind cell

\[
\boxed{
(\mathcal C_jf)(r)
=
g_f(a-r),
\qquad
0<r<a.
}
\]

Let

\[
\boxed{
V_j
=
\mathcal C_j(L_j)
\subset
L^2(0,a).
}
\]

This is finite dimensional.

The map

\[
\mathcal C_j:L_j\to V_j
\]

need not be injective; a first nonkernel escape can also carry custody through
the opposite entry zone.

The present pass concerns the blind-cell image \(V_j\) itself.

---

# V. Blind-transform flatness filtration

## 6. Definition

For every integer

\[
N\ge0,
\]

define

\[
\boxed{
V_{j,N}^{\rm blind}
=
\left\{
b\in V_j:
\|\mathscr T b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\text{ as }\varepsilon\downarrow0
\right\}.
}
\]

This is a linear subspace, and

\[
\boxed{
V_{j,N+1}^{\rm blind}
\subseteq
V_{j,N}^{\rm blind}.
}
\]

Define

\[
\boxed{
V_{j,\infty}^{\rm blind}
=
\bigcap_{N\ge0}
V_{j,N}^{\rm blind}.
}
\]

---

# VI. Finite stabilization

## 7. Dimension argument

Because

\[
V_j
\]

is finite dimensional, the descending chain stabilizes.

There exists a finite integer

\[
\boxed{
N_j^{\rm blind}<\infty
}
\]

such that

\[
\boxed{
V_{j,N}^{\rm blind}
=
V_{j,N_j^{\rm blind}}^{\rm blind}
\qquad
(N\ge N_j^{\rm blind}).
}
\]

Hence

\[
\boxed{
V_{j,\infty}^{\rm blind}
=
V_{j,N_j^{\rm blind}}^{\rm blind}.
}
\]

Thus all-orders blind-transform flatness is already detected by one finite,
although unknown, order on the actual finite-dimensional cell family.

---

# VII. Uniform superflatness on the stabilized subspace

## 8. Operator form

Let

\[
W_j^{\rm blind}
=
V_{j,\infty}^{\rm blind}.
\]

Choose a basis

\[
b_1,\ldots,b_r.
\]

For every \(N\),

\[
\|\mathscr Tb_\nu\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\]

for each basis vector.

Finite-dimensional norm equivalence gives

\[
\boxed{
\|
\mathscr T|_{W_j^{\rm blind}}
\|_{W_j^{\rm blind}\to L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

So transform superflatness is uniform on the stabilized blind family.

---

# VIII. Finite-order branch

## 9. Immediate local field

If

\[
b\in V_j\setminus V_{j,\infty}^{\rm blind},
\]

then

\[
\mathscr Tb
\]

fails the stabilized finite-order condition.

Thus the blind-side archimedean field already carries a finite-order local
signature.

Via GERM-17:

- on a kernel-contained dyadic step, this branch is impossible when the
  visible endpoint germ is superflat, because the exact threshold equation
  forces the blind transform to be superflat;
- at the first nonkernel escape, a finite-order blind transform gives the same
  finite-order behavior to the escape-field second derivative up to a
  superflat visible term.

So the genuinely difficult branch is exactly

\[
\boxed{
W_j^{\rm blind}.
}
\]

---

# IX. Analytic-gap lemma for the blind cell

## 10. Source separated from the blind hinge

Take

\[
0\ne b\in W_j^{\rm blind}.
\]

Suppose for some

\[
\rho>0
\]

that

\[
b=0
\quad\text{a.e. on }(0,\rho).
\]

Then the kernel

\[
a_\infty''(\eta+r)
\]

is jointly real analytic for

\[
|\eta|<\rho/2
\]

on the support of \(b\).

Therefore

\[
\mathscr Tb
\]

extends real analytically through

\[
\eta=0.
\]

But by definition it is superflat in \(L^2(0,\varepsilon)\).

A nonzero analytic germ has a finite first Taylor order and cannot have
\(L^2\)-mass smaller than every power.

Hence

\[
\mathscr Tb
\equiv0
\]

near zero.

Section III then gives

\[
b=0,
\]

contradiction.

Therefore:

\[
\boxed{
0\ne b\in W_j^{\rm blind}
\Longrightarrow
b
\text{ is nonzero on every neighborhood of }r=0.
}
\]

So a nonzero superflat blind transform requires genuine source contact with
the blind hinge.

---

# X. Fixed-radius local detectability

## 11. Restriction injectivity

For every fixed

\[
\rho>0,
\]

define

\[
R_\rho^{\rm blind}b
=
b|_{(0,\rho)}.
\]

Section IX implies

\[
\boxed{
R_\rho^{\rm blind}
\text{ is injective on }
W_j^{\rm blind}.
}
\]

Therefore finite dimensionality gives a constant

\[
\eta_{j,\rho}>0
\]

such that

\[
\boxed{
\|b\|_{L^2(0,\rho)}
\ge
\eta_{j,\rho}\|b\|_{L^2(0,a)}
\qquad
(b\in W_j^{\rm blind}).
}
\]

No uniform lower bound as

\[
\rho\downarrow0
\]

is asserted.

Thus the hard blind-transform branch is locally detectable at every fixed
scale but may remain superalgebraically thin as the hinge is approached.

---

# XI. Stieltjes boundary normal form

## 12. Closed form of \(a_\infty''\)

GERM-2 also gives

\[
\boxed{
a_\infty''(t)
=
-e^{t/2}
+
\frac{e^{-5t/2}}{1-e^{-2t}}.
}
\]

Set

\[
z=e^{-2\eta},
\qquad
x=e^{-2r}.
\]

Then

\[
0<z<1,
\qquad
1/4<x<1.
\]

Write

\[
\widetilde b(x)
=
b\!\left(-\frac12\log x\right).
\]

A direct change of variables gives

\[
\boxed{
(\mathscr Tb)(\eta)
=
-z^{-1/4}A_+(b)
+
\frac12
z^{5/4}
\int_{1/4}^{1}
\frac{x^{1/4}\widetilde b(x)}
{1-zx}
\,dx.
}
\]

Multiplying by \(z^{1/4}\),

\[
\boxed{
z^{1/4}(\mathscr Tb)(\eta)
=
-A_+(b)
+
\frac12
z^{3/2}
\int_{1/4}^{1}
\frac{x^{1/4}\widetilde b(x)}
{1-zx}
\,dx.
}
\]

Thus the blind transform is exactly a weighted Stieltjes/Cauchy transform
approaching the boundary point

\[
\boxed{
z=1^-.
}
\]

---

# XII. Meaning of superflat blind transforms

## 13. Boundary flatness

Since

\[
1-z
=
1-e^{-2\eta}
\asymp
\eta
\]

as

\[
\eta\downarrow0,
\]

all-orders flatness in \(\eta\) is equivalent, up to analytic nonvanishing
factors, to all-orders boundary flatness of the Stieltjes expression at

\[
z=1^-.
\]

Therefore the hard branch is no longer an unspecified
“non-quasi-analytic archimedean remainder.”

It is precisely:

\[
\boxed{
\text{a finite-dimensional family of weighted Stieltjes boundary germs
flat at }z=1.
}
\]

This identifies the analytic species of the remaining obstruction.

---

# XIII. Relation to the dyadic threshold equation

## 14. Kernel-contained step

If both

\[
g
\quad\text{and}\quad
S_ag
\]

belong to \(K_c\), GERM-17 gives

\[
d_2g(\eta)+\mathscr Tb(\eta)=0,
\qquad
d_2=\frac{\log2}{\sqrt2}.
\]

For the jointly-visible-superflat branch,

\[
g(\eta)
\]

is superflat.

Hence automatically

\[
b\in
V_{j,\infty}^{\rm blind}.
\]

So every dyadic step that remains in the kernel pushes the source into the
hard blind-transform branch.

---

## 15. First nonkernel escape

At the first nonkernel escape,

\[
n=(I-\Pi_K)S_ag,
\]

GERM-17 gives

\[
F_n''(c-\eta)
=
-d_2g(\eta)-\mathscr Tb(\eta).
\]

Therefore:

- if \(b\notin V_{j,\infty}^{\rm blind}\), the escape field has a finite-order
  boundary signature;
- if \(b\in V_{j,\infty}^{\rm blind}\), the escape field may remain superflat
  locally even though \(n\ne0\).

Thus the blind-transform filtration precisely classifies the last unresolved
escape behavior.

---

# XIV. What the filtration does not prove

## 16. Transform superflatness is not source-mass superflatness

The fixed-radius estimate in Section X does not imply

\[
\|b\|_{L^2(0,\rho)}
=
o(\rho^N).
\]

Indeed, it points in the opposite qualitative direction: every nonzero hard
blind source remains present in every fixed neighborhood of the hinge.

What remains uncontrolled is the decay rate as

\[
\rho\downarrow0.
\]

So the same rate barrier encountered in GERM-14 reappears here in a more
localized Stieltjes form.

---

# XV. Result of this NF pass

The blind-side carrier from GERM-17 now has a complete finite-dimensional
flatness classification.

For each dyadic escape layer, its blind-cell image \(V_j\) has a stabilized
subspace

\[
\boxed{
V_{j,\infty}^{\rm blind}
=
V_{j,N_j^{\rm blind}}^{\rm blind}.
}
\]

Every direction outside this subspace exposes a finite-order blind-side field.

Every nonzero direction inside it satisfies:

\[
\boxed{
\mathscr Tb
\text{ is operator-superflat},
}
\]

but also

\[
\boxed{
b
\text{ is locally nontrivial in every neighborhood of the blind hinge}.
}
\]

And the transform has the exact boundary representation

\[
\boxed{
z^{1/4}\mathscr Tb
=
-A_+(b)
+
\frac12 z^{3/2}
\int_{1/4}^{1}
\frac{x^{1/4}\widetilde b(x)}
{1-zx}\,dx,
\qquad
z\uparrow1.
}
\]

Thus the residual problem has become a finite-dimensional
**Stieltjes boundary-flatness problem tied to a one-sided blind germ**.

---

# XVI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-19 / BLIND-SIDE REFLECTION TRANSFER}.
}
\]

The next pass should compare the blind physical half isolated here with the
opposite-edge visible half from the reflection geometry of GERM-2/3.

In particular:

1. when the dyadic hinge has an active reflected partner, determine whether
   bilateral visible-mass filtration forces a finite-order channel;
2. separate reflected dyadic sites from isolated dyadic sites;
3. test whether only isolated nonreflected blind contacts can support the
   Stieltjes-superflat branch;
4. use the two edge orientations to determine whether repeated blind contact
   creates a finite dimension drop.

No reflection-side elimination is proved in this pass.

---

# XVII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified blind-transform-filtration / Stieltjes-normalization
result.

No public promotion and no canonical cursor movement are asserted.
