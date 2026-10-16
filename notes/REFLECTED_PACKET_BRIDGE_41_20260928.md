# RPB-41 — Carleman indicator support-edge matching

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS / INDICATOR MATCHES THE MAXIMAL COLLAR EDGE EXACTLY / SOURCE-EDGE TERMS CANCEL / NO SUPPORT-MISMATCH CONTRADICTION**  
**Dependencies:** RPB-39, RPB-40; Titchmarsh convolution/support theorem for the optional source-edge refinement.  
**Promotion status:** none.

## 0. Objective

RPB-40 proved that the right divisor-cleared numerator remembers the first
support point \(b_+\) of the right exterior residual through

\`\`\`math
\limsup_{Y\to\infty}
\frac{
\log|N_+(iY)|
-
\log\xi(1/2+Y)
}{Y}
=
-b_+.
\`\`\`

RPB-41 asks whether the same indicator, computed from the explicit entire
identity

\`\`\`math
N_+
=
V\xi'
-
z^2\xi E_{+,a}
+
\frac{Cz}{i}e^{iaz}\xi,
\`\`\`

forces \(b_+\) to equal:

1. the chosen collar cutoff \(a\);
2. a compact-source support endpoint;
3. an arithmetic shift of a source endpoint;
4. or another rigid value.

It does not.

The indicator calculation reproduces the **actual end of the constant
plateau** exactly.

The compact-source support edge appears in the first two entire terms, but
those source-edge contributions cancel identically when the terms are
recombined into the true exterior tail.

The collar cutoff itself is also artificial: the whole divisor-cleared
numerator is independent of where the cutoff is placed inside a constant
plateau.

Thus RPB-41 produces a precise no-gain theorem:

\`\`\`math
\boxed{
\text{the subleading Carleman indicator measures the maximal collar radius,
not an independent source-support constraint}.
}
\`\`\`

---

## 1. Setup

Let

\`\`\`math
0\ne u\in L_0^2(-c,c),
\qquad
F_u=g*u.
\`\`\`

Assume, in one parity block, that

\`\`\`math
F_u(x)=C
\qquad
(|x|<a)
\`\`\`

for some strict enlargement \(a>c\).

Define

\`\`\`math
R_+(x)
=
\mathbf1_{[a,\infty)}(x)
\bigl(F_u(x)-C\bigr),
\`\`\`

and

\`\`\`math
b_+
=
\inf\operatorname{ess\,supp}R_+.
\`\`\`

RPB-40 gives

\`\`\`math
a\le b_+<\infty.
\`\`\`

The upper finiteness follows because a globally constant screw potential would
produce the global compact Weil radical excluded by RPB-11.

---

## 2. Explicit right numerator on the positive imaginary axis

Recall

\`\`\`math
V(z)
=
\int_{-c}^{c}
u(y)e^{izy}\,dy
\`\`\`

and

\`\`\`math
E_{+,a}(z)
=
\int_{-c}^{c}
u(y)e^{izy}
\left[
\int_0^{a-y}
g(t)e^{izt}\,dt
\right]dy.
\`\`\`

RPB-39 gives

\`\`\`math
N_{+,a}(z)
=
V(z)
\xi'\!\left(
\frac12-iz
\right)
-
z^2
\xi\!\left(
\frac12-iz
\right)
E_{+,a}(z)
+
\frac{Cz}{i}
e^{iaz}
\xi\!\left(
\frac12-iz
\right).
\`\`\`

Put

\`\`\`math
z=iY,
\qquad
Y>\frac12.
\`\`\`

Then

\`\`\`math
\boxed{
\frac{
N_{+,a}(iY)
}{
\xi(1/2+Y)
}
=
V(iY)
\frac{\xi'}{\xi}
\!\left(
\frac12+Y
\right)
+
Y^2E_{+,a}(iY)
+
CYe^{-aY}.
}
\`\`\`

---

## 3. Exact source-edge cancellation identity

From the RPB-39 Fubini identity,

\`\`\`math
\int_a^\infty
F_u(x)e^{izx}\,dx
=
\frac{V(z)}{z^2}
\frac{\xi'}{\xi}
\!\left(
\frac12-iz
\right)
-
E_{+,a}(z).
\`\`\`

At \(z=iY\),

\`\`\`math
\boxed{
V(iY)
\frac{\xi'}{\xi}
\!\left(
\frac12+Y
\right)
+
Y^2E_{+,a}(iY)
=
-
Y^2
\int_a^\infty
F_u(x)e^{-Yx}\,dx.
}
\`\`\`

This identity is exact.

Therefore the first two entire terms are not independent asymptotic
contributions.

They are simply two pieces of the truncated convolution recombined into the
actual right potential tail.

---

## 4. Optional refinement: both first terms individually see the source edge

Let

\`\`\`math
\alpha
=
\inf\operatorname{ess\,supp}u.
\`\`\`

The compact-source transform satisfies the standard Laplace support formula

\`\`\`math
\boxed{
\limsup_{Y\to\infty}
\frac1Y
\log|V(iY)|
=
-\alpha.
}
\`\`\`

Since

\`\`\`math
\frac{\xi'}{\xi}
\!\left(
\frac12+Y
\right)
=
\frac12\log Y
+
O(1),
\`\`\`

the logarithmic derivative contributes no linear exponential indicator, so

\`\`\`math
\boxed{
\limsup_{Y\to\infty}
\frac1Y
\log
\left|
V(iY)
\frac{\xi'}{\xi}
\!\left(
\frac12+Y
\right)
\right|
=
-\alpha.
}
\`\`\`

The finite-interval term \(E_{+,a}\) may be viewed as the Laplace transform of
the one-sided convolution of \(u\) with the positive-half screw kernel,
truncated at \(a\).

The positive-half screw kernel has left support edge \(0\) and is not
identically zero in any right neighborhood of \(0\).

By the Titchmarsh convolution theorem, the resulting compact function has left
support edge \(\alpha\).

Hence

\`\`\`math
\boxed{
\limsup_{Y\to\infty}
\frac1Y
\log|E_{+,a}(iY)|
=
-\alpha.
}
\`\`\`

The polynomial factor \(Y^2\) does not change this indicator.

Thus both first terms individually carry the same source-edge indicator
\(-\alpha\).

### Contextual source

The support-additivity statement used here is the classical Titchmarsh
convolution theorem.

This refinement is not needed for the exact cancellation theorem of Section 3.

---

## 5. The source-edge indicator cancels completely

Since

\`\`\`math
\alpha<c<a,
\`\`\`

the individual source-edge scale \(e^{-\alpha Y}\) is exponentially larger
than the exterior scale \(e^{-aY}\).

Nevertheless Section 3 shows that the two terms cancel exactly down to the
actual tail

\`\`\`math
\int_a^\infty
F_u(x)e^{-Yx}\,dx.
\`\`\`

This is the **source-edge Carleman cancellation**:

\`\`\`math
\boxed{
\text{Paley--Wiener source edge}
+
\text{finite-interval correction}
\longrightarrow
\text{actual exterior potential edge}.
}
\`\`\`

Therefore comparing the separate Paley--Wiener indicators cannot produce a
contradiction.

The large cancellation is required algebraically by the way \(E_{+,a}\) was
created.

---

## 6. The collar constant produces a second exact cancellation

Because

\`\`\`math
F_u(x)=C
\qquad
(a<x<b_+),
\`\`\`

the uncentered tail in Section 3 contains the collar-constant contribution.

The elementary term

\`\`\`math
CYe^{-aY}
\`\`\`

removes it exactly:

\`\`\`math
\begin{aligned}
\frac{N_{+,a}(iY)}{\xi(1/2+Y)}
&=
-
Y^2
\int_a^\infty
F_u(x)e^{-Yx}\,dx
+
CYe^{-aY}
\\
&=
-
Y^2
\int_a^\infty
\bigl(
F_u(x)-C
\bigr)
e^{-Yx}\,dx.
\end{aligned}
\`\`\`

Hence

\`\`\`math
\boxed{
\frac{N_{+,a}(iY)}{\xi(1/2+Y)}
=
-
Y^2
\mathcal C_+(iY).
}
\`\`\`

This is precisely the RPB-40 support-indicator identity.

---

## 7. Exact collar-cutoff invariance

The numerator is independent of the chosen cutoff \(a\) as long as \(a\)
remains inside the same constant plateau.

Differentiate the finite-interval correction with respect to \(a\):

\`\`\`math
\begin{aligned}
\partial_aE_{+,a}(z)
&=
\int_{-c}^{c}
u(y)e^{izy}
g(a-y)e^{iz(a-y)}\,dy
\\
&=
e^{iaz}
\int_{-c}^{c}
g(a-y)u(y)\,dy
\\
&=
e^{iaz}
F_u(a).
\end{aligned}
\`\`\`

On the constant plateau,

\`\`\`math
F_u(a)=C.
\`\`\`

Therefore

\`\`\`math
\boxed{
\partial_aE_{+,a}(z)
=
C e^{iaz}.
}
\`\`\`

Now

\`\`\`math
\partial_a
\left[
-z^2\xi E_{+,a}
\right]
=
-Cz^2e^{iaz}\xi,
\`\`\`

while

\`\`\`math
\partial_a
\left[
\frac{Cz}{i}
e^{iaz}\xi
\right]
=
Cz^2e^{iaz}\xi.
\`\`\`

The two derivatives cancel.

Hence

\`\`\`math
\boxed{
\partial_aN_{+,a}(z)=0
}
\`\`\`

throughout every constant plateau.

This is **collar-cutoff invariance**.

---

## 8. Therefore the chosen collar edge \(a\) is not an invariant

Suppose

\`\`\`math
F_u=C
\`\`\`

on the larger interval

\`\`\`math
(-b,b),
\qquad
b>a.
\`\`\`

Then the divisor-cleared numerator computed using cutoff \(a\) is exactly the
same entire function as the numerator computed using cutoff \(b\).

Thus its vertical indicator cannot distinguish \(a\) from any other point in
the plateau.

In particular:

\`\`\`math
\boxed{
\text{the indicator is not forced to equal an arbitrarily chosen strict enlargement }a.
}
\`\`\`

Any attempt to derive such an equality would be coordinate/cutoff dependent.

---

## 9. Maximal screw-collar radius

Define the maximal symmetric collar radius

\`\`\`math
\boxed{
a_{\max}
=
\sup
\left\{
r>0:
F_u
\text{ is constant on }(-r,r)
\right\}.
}
\`\`\`

Because the endpoint mode is already constant on \((-c,c)\),

\`\`\`math
a_{\max}\ge c.
\`\`\`

Under the strict-persistence hypothesis,

\`\`\`math
a_{\max}>c.
\`\`\`

RPB-11 excludes

\`\`\`math
a_{\max}=\infty.
\`\`\`

Therefore

\`\`\`math
\boxed{
c<a_{\max}<\infty.
}
\`\`\`

---

## 10. The first exterior support point equals the maximal collar radius

Work in one parity block.

If \(F_u\) is even, the constant plateau is symmetric automatically.

If \(F_u\) is odd, a constant symmetric plateau must have

\`\`\`math
C=0.
\`\`\`

Thus right and left constancy radii agree.

By continuity of \(F_u\),

\`\`\`math
F_u=C
\`\`\`

on

\`\`\`math
(-a_{\max},a_{\max}).
\`\`\`

For every

\`\`\`math
\varepsilon>0,
\`\`\`

maximality gives a point in

\`\`\`math
(a_{\max},a_{\max}+\varepsilon)
\`\`\`

where

\`\`\`math
F_u-C\ne0.
\`\`\`

Continuity then gives a positive-measure neighborhood on which it is nonzero.

Hence

\`\`\`math
\boxed{
\inf
\operatorname{ess\,supp}
\left[
\mathbf1_{[a_{\max},\infty)}
(F_u-C)
\right]
=
a_{\max}.
}
\`\`\`

Therefore

\`\`\`math
\boxed{
b_+=a_{\max}.
}
\`\`\`

---

## 11. Exact indicator match

Combining RPB-40 with Section 10,

\`\`\`math
\boxed{
\limsup_{Y\to\infty}
\frac{
\log|N_+(iY)|
-
\log\xi(1/2+Y)
}{Y}
=
-a_{\max}.
}
\`\`\`

So the subleading vertical indicator has an exact interpretation:

\`\`\`math
\boxed{
\text{Carleman subleading indicator}
=
-\text{maximal screw-collar radius}.
}
\`\`\`

This is a positive identification theorem.

But it does not determine \(a_{\max}\) from upstream source data.

---

## 12. No source-support mismatch remains

The compact-source edge \(\alpha\) is visible in

\`\`\`math
V
\`\`\`

and in the finite-interval term

\`\`\`math
E_{+,a}.
\`\`\`

The maximal collar edge \(a_{\max}\) is visible only after their exact
cancellation and the collar-constant subtraction.

Hence

\`\`\`math
\boxed{
\alpha
\quad\text{and}\quad
a_{\max}
}
\`\`\`

live at different levels of the same identity.

There is no theorem of the form

\`\`\`math
a_{\max}
=
-\alpha,
\qquad
a_{\max}
=
c-\alpha,
\qquad
\text{or}
\qquad
a_{\max}
=
\alpha+\log n
\`\`\`

from Paley--Wiener indicators alone.

The finite correction \(E_{+,a}\) is precisely what invalidates such a direct
comparison.

---

## 13. Indicator matching is therefore taut but not vacuous

RPB-41 is not merely a restatement of the tail definition.

It proves three nontrivial structural facts:

1. the compact-source Paley--Wiener edge cancels exactly from the
   divisor-cleared numerator;
2. the numerator is invariant under movement of the artificial cutoff inside
   a constant plateau;
3. the surviving indicator records the **maximal** collar edge and nothing
   earlier.

Thus any future contradiction must enter at the point where constancy first
fails.

The indicator cannot determine that point before the first-activation geometry
is analyzed.

---

## 14. What remains at the maximal edge

At

\`\`\`math
x=a_{\max},
\`\`\`

the potential ceases to be constant immediately to the right.

The non-prime archimedean/pole pieces of the exterior potential are analytic
away from the compact source.

The arithmetic screw contribution contains moving kinks produced by the
prime-power delays.

Therefore the next local question is:

> can first activation at \(a_{\max}\) occur at an arbitrary exterior point,
> or must it lie in the closure of an arithmetic-shifted source support
> \(\log n+\operatorname{supp}u\)?

That question is not answered by the Carleman indicator itself.

It is a local support/kink geometry problem.

---

## 15. RPB-41 determination

\`\`\`math
\boxed{
\textbf{RPB-41 — THE CARLEMAN INDICATOR MATCHES THE MAXIMAL COLLAR EDGE EXACTLY, BUT PROVIDES NO INDEPENDENT SOURCE-SUPPORT CONTRADICTION.}
}
\`\`\`

Exact identities:

\`\`\`math
\boxed{
V(iY)
\frac{\xi'}{\xi}(1/2+Y)
+
Y^2E_{+,a}(iY)
=
-
Y^2
\int_a^\infty
F_u(x)e^{-Yx}\,dx,
}
\`\`\`

and

\`\`\`math
\boxed{
\partial_aN_{+,a}=0
\quad
\text{inside a constant plateau}.
}
\`\`\`

The final support indicator is

\`\`\`math
\boxed{
\limsup_{Y\to\infty}
\frac{
\log|N_+(iY)|
-
\log\xi(1/2+Y)
}{Y}
=
-a_{\max}.
}
\`\`\`

So the frequency-side support-edge matching is exact but self-consistent.

Next cursor:

\`\`\`text
RPB-42 / MAXIMAL COLLAR FIRST-ACTIVATION GEOMETRY
\`\`\`

The next pass should analyze the exterior potential locally at
\(a_{\max}\):

1. separate analytic archimedean/pole contributions from arithmetic moving
   kinks;
2. identify the shifted-source activation sets
   \(\log n+\operatorname{supp}u\);
3. determine whether maximality forces
   \(a_{\max}\) into their closure;
4. test whether parity and zero-mean/source constraints exclude such a first
   activation point or merely re-express the null-extension interface.
