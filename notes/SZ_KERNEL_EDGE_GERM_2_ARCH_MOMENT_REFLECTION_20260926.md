# SZ-KERNEL-EDGE-GERM-2 — Archimedean moment injectivity and reflection-resonance reduction

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-1  
**Target:** GLOBAL ANALYTIC BLIND-GERM COUPLING  
**Public promotion:** forbidden

## 0. Objective

GERM-1 showed that the old-interior first-kind equation converts the raw
exterior edge transform into a centered second difference and removes every
prime-hinge tail moment.

It also exposed an exact one-sided blind germ: a source germ immediately on
the outward-facing side of one prime hinge is invisible to that hinge under
inward motion, while it can produce nonzero infinitely-flat outward leakage.

The remaining possible control came from the rest of the screw kernel.

This pass shows that the archimedean part is much stronger than a generic
analytic background.

Away from the origin it generates a complete exponential moment system.
Consequently:

1. its one-sided analytic transform is injective modulo affine functions;
2. on any finite-dimensional blind-germ family, finitely many archimedean
   moments already separate the family;
3. a source supported only in isolated outward-facing prime-blind collars
   cannot lie in \(\ker G_c\);
4. the only direct rough prime coupling between the two edge orientations
   occurs through the arithmetic reflection relation
   \[
   \ell+\ell'=2c.
   \]

Thus the remaining nonanalytic germ network collapses to a finite
reflection-resonance problem plus the endpoint \(s=0\).

This pass does **not** yet prove

\[
\mathcal E_c=0.
\]

---

# I. Exact exponential form of the archimedean kernel

## 1. Suzuki's non-prime component

For \(t>0\), the ratified Suzuki pin gives

\[
a_\infty(t)
=
-4\left(e^{t/2}+e^{-t/2}-2\right)
-\kappa t
-\frac14
\left[
\Phi(1,2,1/4)
-
e^{-t/2}\Phi(e^{-2t},2,1/4)
\right],
\]

where

\[
\kappa
=
\frac12(\psi(1/4)-\log\pi).
\]

Using

\[
\Phi(e^{-2t},2,1/4)
=
\sum_{m=0}^{\infty}
\frac{e^{-2mt}}{(m+1/4)^2},
\]

we obtain

\[
e^{-t/2}\Phi(e^{-2t},2,1/4)
=
\sum_{m=0}^{\infty}
\frac{e^{-(2m+1/2)t}}{(m+1/4)^2}.
\]

The \(m=0\) term is

\[
16e^{-t/2}.
\]

After multiplication by \(1/4\), it is exactly

\[
4e^{-t/2},
\]

which cancels the \(-4e^{-t/2}\) already present.

Therefore

\[
\boxed{
a_\infty(t)
=
C_0+C_1t
-4e^{t/2}
+
\frac14
\sum_{m=1}^{\infty}
\frac{e^{-(2m+1/2)t}}{(m+1/4)^2},
\qquad
t>0,
}
\]

for fixed constants \(C_0,C_1\).

This cancellation is useful and was not needed in the earlier analyticity
pin.

---

## 2. Second derivative collapses further

Set

\[
\lambda_m=2m+\frac12
=
2\left(m+\frac14\right).
\]

Differentiating twice on \(t>0\),

\[
\frac14
\frac{\lambda_m^2}{(m+1/4)^2}
=
1.
\]

Hence

\[
\boxed{
a_\infty''(t)
=
-e^{t/2}
+
\sum_{m=1}^{\infty}
e^{-\lambda_m t},
\qquad
\lambda_m=2m+\frac12.
}
\]

Equivalently,

\[
a_\infty''(t)
=
-e^{t/2}
+
\frac{e^{-5t/2}}{1-e^{-2t}}.
\]

The discrete exponential form is the one used below.

---

# II. One-sided archimedean transform

## 3. Compact source interval away from the origin

Let

\[
I=[a,b]\Subset(0,\infty)
\]

and let

\[
f\in L^2(I).
\]

For \(|\delta|<a\), define the inward archimedean difference

\[
\mathscr A_f(\delta)
=
\int_I
\bigl[
a_\infty(s-\delta)-a_\infty(s)
\bigr]
f(s)\,ds.
\]

This is real analytic, indeed holomorphic in a complex neighborhood of
\(\delta=0\).

Its second derivative is

\[
\mathscr A_f''(\delta)
=
\int_I
a_\infty''(s-\delta)f(s)\,ds.
\]

Using the exponential expansion,

\[
\boxed{
\mathscr A_f''(\delta)
=
-
e^{-\delta/2}
M_+(f)
+
\sum_{m=1}^{\infty}
e^{\lambda_m\delta}
M_m(f),
}
\]

where

\[
M_+(f)
=
\int_I e^{s/2}f(s)\,ds
\]

and

\[
\boxed{
M_m(f)
=
\int_I
e^{-\lambda_m s}f(s)\,ds,
\qquad
m\ge1.
}
\]

Because \(a>0\),

\[
|M_m(f)|
\lesssim
e^{-\lambda_m a}\|f\|_{L^2(I)},
\]

so the exponential series converges normally for \(\Re\delta<a\).

---

# III. Archimedean injectivity modulo affine functions

## 4. Laurent uniqueness

Assume

\[
\mathscr A_f(\delta)
\]

is affine near \(\delta=0\).

Then

\[
\mathscr A_f''(\delta)=0
\]

near zero.

Set

\[
q=e^{\delta/2}.
\]

Since

\[
e^{-\delta/2}=q^{-1}
\]

and

\[
e^{\lambda_m\delta}
=
q^{4m+1},
\]

the identity becomes

\[
\boxed{
-
M_+(f)q^{-1}
+
\sum_{m=1}^{\infty}
M_m(f)q^{4m+1}
=
0
}
\]

on an annulus containing \(q=1\).

The series is a convergent Laurent series there.

Uniqueness of Laurent coefficients gives

\[
M_+(f)=0
\]

and

\[
\boxed{
M_m(f)=0
\qquad
\forall m\ge1.
}
\]

---

## 5. Completeness of the exponential moments

It remains to show that

\[
M_m(f)=0
\qquad
(m\ge1)
\]

forces \(f=0\).

Set

\[
x=e^{-2s}.
\]

The interval \(I=[a,b]\) maps to

\[
J=[e^{-2b},e^{-2a}]
\Subset(0,1).
\]

Since

\[
e^{-\lambda_m s}
=
e^{-(2m+1/2)s}
=
x^{m+1/4},
\]

the conditions \(M_m(f)=0\) become, after the change of variables,

\[
\int_J
x^m h(x)\,dx
=
0
\qquad
(m\ge1)
\]

for a fixed \(h\in L^2(J)\) obtained from \(f\) by multiplication by a
nonvanishing bounded weight.

Because \(J\) is bounded away from zero, multiplication by \(x\) is
invertible on \(C(J)\), and

\[
\operatorname{span}\{x^m:m\ge1\}
\]

is dense in \(C(J)\), hence dense in \(L^2(J)\).

Therefore

\[
h=0
\]

and hence

\[
f=0.
\]

We have proved:

\[
\boxed{
\mathscr A_f
\text{ affine near }0
\Longrightarrow
f=0
\qquad
(f\in L^2(I),\ I\Subset(0,\infty)).
}
\]

In particular,

\[
\boxed{
\mathscr A_f\equiv0
\Longrightarrow
f=0.
}
\]

This is a genuine Weil-archimedean injectivity theorem on compact source
regions separated from the endpoint.

---

# IV. Finite-dimensional compression

## 6. Finite moment separation

Let

\[
V\subset L^2(I)
\]

be finite dimensional.

The infinite family

\[
\{M_m:m\ge1\}
\]

separates \(V\).

Therefore a finite subfamily already separates \(V\).

Equivalently, there exist

\[
1\le m_1<\cdots<m_r
\]

with

\[
r\le\dim V
\]

such that

\[
\boxed{
f
\longmapsto
\left(
\int_I e^{-(2m_j+1/2)s}f(s)\,ds
\right)_{j=1}^{r}
}
\]

is injective on \(V\).

Thus on every finite-dimensional blind-germ family, the global
archimedean coupling reduces to a finite analytic moment matrix.

This is precisely the type of finite-dimensional coupling sought after
GERM-1.

---

# V. Pure blind-sector exclusion

## 7. Prime blind collars

Let

\[
\mathscr H_c
=
\{
\ell=\log n:
\Lambda(n)\ne0,\;
0<\ell\le L
\},
\qquad
L=2c.
\]

Choose

\[
\rho>0
\]

small enough that the left collars

\[
B_\ell
=
(\ell-\rho,\ell)
\]

are pairwise disjoint, lie in \((0,L)\), and are separated from every other
prime hinge.

Set

\[
B
=
\bigcup_{\ell\in\mathscr H_c}
B_\ell.
\]

These are exactly the outward-facing blind neighborhoods for the right-edge
inward motion.

---

## 8. Prime inward difference is affine on the pure blind sector

Suppose

\[
f\in L^2(0,L)
\]

is supported in \(B\).

Fix one prime hinge \(h_{\ell_0}(s)=(s-\ell_0)_+\).

For sufficiently small \(\delta\):

- on its own blind collar \(B_{\ell_0}\),
  \[
  h_{\ell_0}(s-\delta)-h_{\ell_0}(s)=0;
  \]
- on any collar strictly to the left of \(\ell_0\), the same difference is
  zero;
- on any collar strictly to the right of \(\ell_0\),
  \[
  h_{\ell_0}(s-\delta)-h_{\ell_0}(s)=-\delta.
  \]

Therefore the full prime contribution to the inward transform is exactly
affine, in fact linear, in \(\delta\).

If \(f\) came from a kernel vector supported entirely in \(B\), the exact
old-interior identity would imply

\[
\mathscr A_f(\delta)
+
\text{affine function of }\delta
=
0.
\]

Hence \(\mathscr A_f\) would be affine.

By the archimedean injectivity theorem,

\[
f=0.
\]

Thus

\[
\boxed{
\ker G_c
\cap
\{u:\operatorname{supp}f_+\subset B\}
=
\{0\}.
}
\]

There is no nonzero kernel vector supported purely in the union of
right-edge prime-blind collars.

The left-edge analogue holds identically.

---

# VI. What this says about the GERM-1 countermodel

## 9. The single-hinge flat germ cannot occur in isolation

GERM-1 constructed an abstract local blind germ satisfying

\[
I^-_\ell(f;\delta)=0
\]

while

\[
I^+_\ell(f;\delta)=e^{-1/\delta^2}.
\]

That construction is valid for the isolated prime hinge.

However, if the source has no compensating component outside that blind
collar, the archimedean inward transform is non-affine unless the germ is
zero.

Therefore the GERM-1 flat germ cannot by itself be an actual vector in

\[
\ker G_c.
\]

A genuine flat-but-leaking kernel mode must contain additional source
components whose non-affine singular channels cancel the archimedean moment
data.

This is the first direct exclusion of the local flat-germ countermodel using
the specific Suzuki archimedean kernel.

---

# VII. Reflection-resonance geometry of the rough prime channels

## 10. Two physical prime-site sets

For the right-edge orientation, the physical prime singular sites are

\[
S_+
=
\{
c-\ell:
\ell\in\mathscr H_c,\;
0<\ell<L
\}.
\]

For the left-edge orientation, they are

\[
S_-
=
\{
-c+\lambda:
\lambda\in\mathscr H_c,\;
0<\lambda<L
\}.
\]

A physical site belongs to both sets precisely when

\[
c-\ell
=
-c+\lambda,
\]

equivalently

\[
\boxed{
\ell+\lambda=L=2c.
}
\]

Define the reflection

\[
\boxed{
\rho_c(\ell)=L-\ell.
}
\]

Then cross-edge coincidence occurs exactly when

\[
\ell\in\mathscr H_c
\quad\text{and}\quad
\rho_c(\ell)\in\mathscr H_c.
\]

---

## 11. Arithmetic interpretation

Write

\[
\ell=\log n,
\qquad
\lambda=\log m,
\]

with \(n,m\) prime powers.

The reflection condition is

\[
\log n+\log m=2c,
\]

or

\[
\boxed{
nm=e^{2c}.
}
\]

Thus direct rough prime coupling across the two edge orientations is possible
only at arithmetic reflection resonances.

The reflection graph is an involution.

Its components are therefore:

- isolated prime hinges;
- reflected pairs
  \[
  \ell\leftrightarrow L-\ell;
  \]
- a possible fixed point
  \[
  \ell=c
  \]
  when \(c\) itself is a prime-power logarithm.

There is no larger rough prime-coupling graph.

---

## 12. Consequence for blind germs

A right-edge outward-facing blind germ at the physical site

\[
c-\ell
\]

becomes an inward-visible prime-local germ for the left-edge equation only if

\[
L-\ell
\]

is itself an active prime-power logarithm.

If no reflected hinge exists, the opposite edge sees that local source
through analytic/affine channels only.

Therefore the only mechanism by which nonanalytic prime-local information can
propagate directly from one edge orientation to the other is the finite
reflection-resonance graph.

This is substantially sharper than the earlier statement that there are
finitely many singular sites.

---

# VIII. Finite-dimensional implication for the obstruction

## 13. Blind data must be coupled to visible data

Let

\[
E_c\simeq\mathcal E_c
\]

be any finite-dimensional representative of the edge obstruction.

Take the image of \(E_c\) under restriction to a compact blind region

\[
B\Subset(0,L).
\]

This image is finite dimensional.

By Section 6, finitely many archimedean exponential moments separate it.

Hence no nonzero blind component can disappear from all global analytic
couplings.

For a flat-but-leaking vector to survive, its blind component must be balanced
by source components that contribute non-affine singular terms to the exact
interior identities.

Those compensating components can occur only in:

1. inward-visible sides of active prime hinges;
2. the endpoint \(s=0\), where the archimedean kernel is itself singular;
3. reflected cross-edge prime sites satisfying
   \[
   \ell+\ell'=2c.
   \]

Thus the possible obstruction has been reduced from arbitrary local germs to a
finite analytic/singular coupling problem on these channels.

---

# IX. What is not yet proved

## 14. No full elimination

The injective archimedean moment map does not by itself imply

\[
\mathcal E_c=0.
\]

Several local singular channels may coordinate so that their Volterra
contributions cancel the analytic archimedean moments.

The exact interior equation proves that such cancellation must be structured;
it does not yet prove that it is impossible.

In particular, this pass does not establish that the individual local germs
are analytic or possess nonzero traces.

---

# X. Result of this NF pass

The global analytic coupling is no longer an unspecified remainder.

For source intervals away from the endpoint, the Suzuki archimedean kernel
provides the explicit complete moment family

\[
\boxed{
f
\longmapsto
\left\{
\int
e^{-(2m+1/2)s}f(s)\,ds
\right\}_{m\ge1}.
}
\]

Its one-sided transform is injective modulo affine functions.

Therefore:

\[
\boxed{
\text{pure prime-blind support}
\cap
\ker G_c
=
\{0\}.
}
\]

A flat prime-blind germ must be accompanied by a compensating non-affine
singular channel.

Moreover, direct rough cross-edge prime coupling is governed solely by

\[
\boxed{
\ell+\ell'=2c.
}
\]

So the remaining edge obstruction lives on a finite
**reflection-resonance / endpoint coupling system**, not on an unrestricted
family of local \(L^2\) germs.

---

# XI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-3 / REFLECTION-RESONANCE SCHUR SYSTEM}.
}
\]

The next pass should:

1. decompose each singular site into inward-visible and outward-blind
   one-sided germs;
2. use the finite archimedean moment map to eliminate pure blind directions;
3. organize the remaining rough channels by the reflection involution
   \[
   \ell\mapsto2c-\ell;
   \]
4. form the finite-dimensional Schur coupling between blind moments and
   visible Volterra channels on \(\mathcal E_c\);
5. determine whether isolated reflection components are automatically
   eliminable and whether only reflected pairs / endpoint components can
   support a superflat defect.

No such Schur invertibility is proved in this pass.

---

# XII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified NF structural result.

No public promotion and no canonical cursor movement are asserted.
