# SZ-KERNEL-EDGE-GERM-1 — Centered second-difference reduction and blind-germ obstruction

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-DET-1  
**Target tested:** FIRST-KIND FLAT-DIVISOR EXCLUSION  
**Public promotion:** forbidden

## 0. Objective

The previous determinant no-go showed that:

- canonical positivity;
- finite-dimensionality;
- rank-\(\le2\) Gramian growth;
- finite singular-site localization;
- and local second-order Volterra structure

do not exclude a positive infinitely-flat edge obstruction.

The missing input was identified as the actual first-kind equation

\[
G_cu=0.
\]

This pass inserts that equation directly into the non-differentiated
first-difference transform.

The result is a sharper exact normal form:

\[
\boxed{
\text{exterior edge residual}
=
\text{centered second difference of the screw transform}.
}
\]

For every interior prime hinge, the analytic tail moment from QA-1 cancels
exactly.  What remains is a compact two-sided tent moment of the source germ.

This is genuine progress.

However, the same calculation exposes a one-sided **blind-germ obstruction**:
the inward first-kind identity does not see the outward-facing germ of an
individual prime hinge through that hinge itself.

Thus the first-kind equation has not yet excluded the flat-divisor
countermodel.

The remaining load-bearing problem is the global analytic coupling of those
blind germs through the rest of the Weil kernel.

---

# I. Exact inward first-difference identity

## 1. Right-edge coordinates

Let

\[
L=2c
\]

and, for

\[
u\in K_c:=\ker G_c,
\]

write

\[
f_+(s)=u(c-s),
\qquad
0<s<L.
\]

Recall

\[
F_u(x)
=
\int_{-c}^{c}
g(x-y)u(y)\,dy.
\]

Since

\[
u\in\ker G_c,
\]

the screw potential is constant on the old interval:

\[
\boxed{
F_u(x)=C_u
\qquad
(|x|<c).
}
\]

At the right edge,

\[
F_u(c+\delta)
=
\int_0^L
g(s+\delta)f_+(s)\,ds.
\]

For the corresponding inward point,

\[
F_u(c-\delta)
=
\int_0^L
g(s-\delta)f_+(s)\,ds,
\]

where evenness of \(g\) is understood when \(s-\delta<0\).

Because \(c-\delta\in(-c,c)\),

\[
F_u(c-\delta)=C_u.
\]

Hence the first-kind equation gives the exact inward identity

\[
\boxed{
0
=
\int_0^L
\bigl[g(s-\delta)-g(s)\bigr]
f_+(s)\,ds.
}
\]

This is the missing companion to the ratified exterior formula

\[
F_u(c+\delta)-C_u
=
\int_0^L
\bigl[g(s+\delta)-g(s)\bigr]
f_+(s)\,ds.
\]

No differentiation of a superflat collar germ is used.

---

## 2. Centered second-difference formula

Add the zero inward identity to the exterior identity.

Then

\[
\boxed{
r_+(\delta)
:=
F_u(c+\delta)-C_u
=
\int_0^L
\Delta_\delta^2 g(s)\,
f_+(s)\,ds,
}
\]

where

\[
\boxed{
\Delta_\delta^2g(s)
=
g(s+\delta)+g(s-\delta)-2g(s).
}
\]

Thus the exterior residual of a true kernel vector is not an arbitrary
one-sided first-difference transform.

It is a centered second-difference transform.

This is an exact consequence of the old-interior first-kind equation.

---

# II. Left-edge analogue

## 3. Left-oriented source

Define

\[
f_-(s)=u(-c+s),
\qquad
0<s<L.
\]

Evenness of \(g\) and interior constancy give

\[
\boxed{
r_-(\delta)
:=
F_u(-c-\delta)-C_u
=
\int_0^L
\Delta_\delta^2g(s)\,
f_-(s)\,ds.
}
\]

Therefore both raw exterior edge residuals are produced by the same centered
second-difference kernel:

\[
\boxed{
r_\pm(\delta)
=
\mathcal S_{c,\delta}f_\pm,
}
\]

with

\[
\mathcal S_{c,\delta}f
=
\int_0^L
\Delta_\delta^2g(s)f(s)\,ds.
\]

The two edge channels differ only in the orientation of the source.

---

# III. Prime hinges become compact tent moments

## 4. One active interior hinge

Fix a prime power \(n\) with

\[
\ell=\log n,
\qquad
0<\ell<L,
\]

and write

\[
a_n=\frac{\Lambda(n)}{\sqrt n}.
\]

On the positive axis its screw contribution is

\[
h_\ell(s)
=
a_n(s-\ell)_+.
\]

Take

\[
0<\delta<\min(\ell,L-\ell).
\]

A direct calculation gives

\[
\boxed{
\Delta_\delta^2 h_\ell(s)
=
a_n
(\delta-|s-\ell|)_+.
}
\]

Therefore the prime-hinge contribution to the exterior residual is exactly

\[
\boxed{
a_n
\int_{\ell-\delta}^{\ell+\delta}
(\delta-|s-\ell|)f(s)\,ds.
}
\]

Equivalently,

\[
\boxed{
a_n
\int_0^\delta
(\delta-t)
\bigl(
f(\ell-t)+f(\ell+t)
\bigr)\,dt.
}
\]

This is a compact two-sided tent moment.

---

## 5. Cancellation of the QA-1 tail moment

QA-1 gave the exterior \(+\delta\) hinge contribution

\[
a_n
\left[
\delta\int_\ell^L f(s)\,ds
+
\int_0^\delta
(\delta-t)f(\ell-t)\,dt
\right].
\]

The inward \(-\delta\) difference is

\[
\boxed{
a_n
\left[
-\delta\int_\ell^L f(s)\,ds
+
\int_0^\delta
(\delta-t)f(\ell+t)\,dt
\right].
}
\]

Since the full inward transform is zero on a true kernel vector, adding it to
the exterior transform cancels the linear tail moment:

\[
\delta\int_\ell^L f
-
\delta\int_\ell^L f
=
0.
\]

Thus the actual first-kind equation removes the nonlocal prime tail from the
edge residual.

For true kernel vectors, the prime contribution is genuinely local at the
hinge.

---

# IV. Threshold geometry

## 6. Exact threshold

Suppose

\[
\ell=L=2c
\]

for a prime power.

On \(0<s<L\),

\[
(s-L)_+=0.
\]

Hence the inward difference of this threshold hinge vanishes identically.

The centered second difference reduces to the exterior activation

\[
\boxed{
a_n
\int_{L-\delta}^{L}
(s+\delta-L)f(s)\,ds
=
a_n
\int_0^\delta
(\delta-t)f(L-t)\,dt.
}
\]

Therefore the exact threshold remains a one-sided endpoint germ.

In physical coordinates this is the direct opposite-edge coupling already
ratified in EDGE-PROP.

The first-kind inward identity supplies no second side at threshold because
the hinge is still inactive everywhere in the old support.

---

# V. Archimedean part

## 7. Centered archimedean transform

Write the positive-axis screw kernel as

\[
g
=
g_{\rm prime}
+
g_\infty.
\]

By the ratified Suzuki source pin,

\[
g_\infty
\]

is real analytic on every compact subset of \((0,\infty)\).

Therefore for any source region separated from \(s=0\),

\[
\Delta_\delta^2g_\infty(s)
\]

is jointly real analytic in \((s,\delta)\) near \(\delta=0\).

The only nonanalytic archimedean contribution to the centered transform is
therefore generated by the endpoint germ near

\[
s=0.
\]

Consequently the centered second-difference normal form preserves the finite
singular-site localization:

- endpoint \(s=0\): archimedean edge germ;
- interior \(s=\log n\): compact two-sided prime tent;
- threshold \(s=L\): one-sided opposite-endpoint tent.

There are no prime tail moments left.

---

# VI. Mean correction introduces no new singular carrier

## 8. Moving mean

Let

\[
r_\pm(\delta)
=
F_u(\pm(c+\delta))-C_u
\]

with the obvious sign convention on the left edge.

The ratified mean identity is

\[
m(c+\delta)-C_u
=
\frac{
\int_0^\delta r_+(s)\,ds
+
\int_0^\delta r_-(s)\,ds
}{
2(c+\delta)
}.
\]

Hence the mean-corrected edge observation

\[
\Gamma_u(\delta)
=
\left(
r_+(\delta)-\mu_u(\delta),
r_-(\delta)-\mu_u(\delta)
\right),
\]

where

\[
\mu_u(\delta)=m(c+\delta)-C_u,
\]

is obtained from the two centered raw residuals by one further Volterra
integration and a nonvanishing analytic denominator.

Thus the moving mean creates no new singular site.

All possible nonanalyticity remains localized to the centered endpoint/hinge
germs.

---

# VII. The blind-germ obstruction

## 9. What the inward identity sees at one prime hinge

Consider only the contribution of one interior hinge \(\ell\).

Its inward first difference is

\[
I^-_\ell(f;\delta)
=
a_n
\left[
-\delta\int_\ell^L f(s)\,ds
+
\int_0^\delta
(\delta-t)f(\ell+t)\,dt
\right].
\]

This depends on:

- the tail mass to the right of the hinge;
- the **right-hand germ**
  \[
  f(\ell+t).
  \]

It contains no local dependence on

\[
f(\ell-t).
\]

Therefore the same hinge is blind, under inward motion, to its
outward-facing left-hand source germ.

---

## 10. Exact local blindness model

Let \(f\) be supported in a sufficiently small interval

\[
(\ell-\rho,\ell)
\]

strictly to the left of the hinge.

Then

\[
\int_\ell^L f(s)\,ds=0
\]

and

\[
f(\ell+t)=0
\qquad
(0<t<\rho).
\]

Consequently

\[
\boxed{
I^-_\ell(f;\delta)=0
\qquad
(0<\delta<\rho).
}
\]

But the exterior hinge contribution is

\[
\boxed{
I^+_\ell(f;\delta)
=
a_n
\int_0^\delta
(\delta-t)f(\ell-t)\,dt,
}
\]

which can be nonzero.

Thus the local first-kind inward identity of the hinge itself places no
constraint on precisely the one-sided germ that becomes newly visible under
outward support enlargement.

This is the **blind-germ obstruction**.

---

## 11. The blind germ can be infinitely flat

Let

\[
h(\delta)=e^{-1/\delta^2}
\qquad
(\delta>0).
\]

Set, for \(0<t<\rho\),

\[
f(\ell-t)
=
a_n^{-1}h''(t)
\]

and set \(f=0\) on the right side of the hinge.

Then

\[
f\in L^2
\]

locally and

\[
I^-_\ell(f;\delta)=0,
\]

while

\[
I^+_\ell(f;\delta)
=
h(\delta)
\]

for sufficiently small \(\delta\).

Hence one individual prime hinge is fully compatible with the pattern

\[
\boxed{
\text{exact inward invisibility}
+
\text{nonzero infinitely-flat outward leakage}.
}
\]

Therefore the first-kind identity cannot be used hinge-by-hinge to exclude
the determinant countermodel.

---

# VIII. Where the true global equation still acts

## 12. Other screw components do see the blind germ

The preceding blindness statement concerns the hinge at its own singular
location.

The same source germ is still seen by:

- the archimedean component of \(g\);
- all other prime hinges whose singular locations are separated from it;
- the screw kernel at other interior center points.

Because those kernels are nonsingular on a sufficiently small neighborhood of
this particular germ, their dependence on a collar parameter is analytic.

Thus the actual global equation does not leave the blind germ completely
free.

Instead it constrains it through an **analytic background moment map**.

Schematically, for the blind germ \(f_{\ell,-}\),

\[
\boxed{
\text{local singular channel: blind inward},
}
\]

but

\[
\boxed{
\text{rest of }G_c:
f_{\ell,-}
\longmapsto
\text{analytic moment family}.
}
\]

This is the only remaining place where Weil-specific rigidity can enter.

---

# IX. Refined finite-site normal form

## 13. Singular versus analytic channels

For a finite collection of disjoint neighborhoods of the singular sites,
decompose the source schematically as

\[
u
=
u_{\rm sing}
+
u_{\rm bulk},
\]

where \(u_{\rm sing}\) is the sum of local \(L^2\) germs near
\(\Sigma_c\).

Then the first-kind/edge system has the form

\[
\boxed{
\Gamma_u(\delta)
=
\mathcal V_\delta u_{\rm sing}
+
\mathcal A_\delta u,
}
\]

where:

- \(\mathcal V_\delta\) is a finite direct sum of centered tent/endpoint
  Volterra channels;
- \(\mathcal A_\delta\) is analytic in \(\delta\) on the chosen separated
  pieces.

The old-interior equation supplies additional identities

\[
\boxed{
0
=
\mathcal V^-_\delta u_{\rm sing}
+
\mathcal A^-_\delta u.
}
\]

The blind-germ calculation shows that

\[
\mathcal V^-_\delta
\]

is not injective on the one-sided singular-germ data.

Thus the unresolved question is exactly whether the analytic background maps

\[
\mathcal A^-_\delta
\]

recover the missing one-sided information on the actual finite-dimensional
kernel family.

---

# X. Result of this NF pass

The actual first-kind equation improves the edge package in a precise way.

For every true kernel vector,

\[
\boxed{
F_u(c+\delta)-C_u
=
\int_0^{2c}
[g(s+\delta)+g(s-\delta)-2g(s)]
u(c-s)\,ds,
}
\]

and analogously at the left edge.

Consequences:

1. every interior prime tail moment cancels exactly;
2. every interior prime hinge reduces to a compact two-sided tent moment;
3. the threshold remains a one-sided endpoint tent;
4. the archimedean nonanalyticity remains confined to the endpoint;
5. the moving mean introduces no new singular carrier.

However, a prime hinge has an exact one-sided blind germ:

\[
\boxed{
\text{inward motion does not see the outward-facing germ through that hinge}.
}
\]

Such a blind germ can generate nonzero infinitely-flat outward leakage while
the hinge's own inward identity remains exactly zero.

Therefore

\[
\boxed{
\text{FIRST-KIND IDENTITY}
+
\text{LOCAL HINGE STRUCTURE}
\not\Rightarrow
\text{FLAT-DIVISOR EXCLUSION}.
}
\]

The missing information is now isolated to the global analytic moment coupling
of the blind germs through the rest of the screw kernel.

---

# XI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-2 / GLOBAL ANALYTIC BLIND-GERM COUPLING}.
}
\]

The next pass should:

1. choose disjoint neighborhoods of the finite singular set \(\Sigma_c\);
2. write the interior identities for each one-sided germ;
3. separate the singular tent channels from the analytic cross-couplings;
4. form the finite-dimensional analytic moment map induced on
   \(\mathcal E_c\);
5. test whether its kernel can contain a nonzero family carrying a common
   infinitely-flat outward divisor.

A positive result would turn the centered local normal form into genuine
edge rigidity.

A negative result would identify a still deeper missing interface.

No such global analytic injectivity is proved in this pass.

---

# XII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified NF structural/no-go residue.

No public promotion and no canonical cursor movement are asserted.
