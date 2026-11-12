# RPB-42 — Maximal collar first-activation geometry

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS / FIRST ACTIVATION MUST BE AN ARITHMETIC SHIFT OF SOURCE ANALYTIC SINGULAR SUPPORT / NO ENDPOINT CONTRADICTION FROM PARITY OR ZERO MEAN**  
**Dependencies:** RPB-35, RPB-41; Suzuki explicit screw formula (1.1); screw-source parity and zero-mean law.  
**Promotion status:** none.

## 0. Objective

RPB-41 identified the maximal constant collar radius

\`\`\`math
a_{\max}
=
\sup
\left\{
r>0:
F_u
\text{ is constant on }(-r,r)
\right\}
\`\`\`

and proved that the Carleman subleading indicator records exactly
\(-a_{\max}\).

RPB-42 asks where constancy can first fail.

The answer is arithmetic:

\`\`\`math
\boxed{
a_{\max}
\in
\bigcup_{n=p^m}
\left(
\log n+\operatorname{singsupp}_{\omega}u
\right).
}
\`\`\`

Thus first activation cannot occur at an arbitrary exterior point.

It must occur when a moving prime-power kink meets an analytic singularity of
the compact screw source.

This is stronger than membership in a shifted source support, but it does not
yet force activation at a support endpoint.

---

## 1. Suzuki's explicit positive-half screw formula

Suzuki defines

\`\`\`math
\Psi(t)
=
4(e^{t/2}+e^{-t/2}-2)
-
\sum_{n\le e^t}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)
+
\frac t2
\left[
\frac{\Gamma'}{\Gamma}\!\left(\frac14\right)
-\log\pi
\right]
+
\frac14
\left[
C-e^{-t/2}\Phi(e^{-2t},2,1/4)
\right]
\`\`\`

for \(t\ge0\), and \(g=-\Psi\).

Therefore, for \(t>0\),

\`\`\`math
\boxed{
g(t)
=
g_{\rm an}(t)
+
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+,
}
\`\`\`

where \(g_{\rm an}\) consists of the exponential, linear, gamma-constant, and
Lerch terms.

Because \(e^{-2t}\in(0,1)\) for \(t>0\), the Lerch term is real analytic there.

Hence

\`\`\`math
\boxed{
g_{\rm an}
\text{ is real analytic on }(0,\infty).
}
\`\`\`

### External source

Masatoshi Suzuki,
*Aspects of the screw function corresponding to the Riemann zeta-function*,
JLMS 108 (2023), formula (1.1).

---

## 2. Exterior convolution sees only the positive-half formula

Let

\`\`\`math
K_u
=
\operatorname{ess\,supp}u
\subset[-c,c].
\`\`\`

For every

\`\`\`math
x>c
\`\`\`

and every \(y\in K_u\),

\`\`\`math
x-y>0.
\`\`\`

Therefore

\`\`\`math
F_u(x)
=
\int_{-c}^{c}
g(x-y)u(y)\,dy
\`\`\`

may be decomposed using the positive-\(t\) formula:

\`\`\`math
\boxed{
F_u(x)
=
F_{{\rm an},u}(x)
+
\sum_{n\ge2}
P_{n,u}(x),
}
\`\`\`

where

\`\`\`math
F_{{\rm an},u}(x)
=
\int_{-c}^{c}
g_{\rm an}(x-y)u(y)\,dy
\`\`\`

and

\`\`\`math
P_{n,u}(x)
=
\frac{\Lambda(n)}{\sqrt n}
\int_{-c}^{c}
(x-y-\log n)_+
u(y)\,dy.
\`\`\`

On every compact exterior interval, only finitely many \(P_{n,u}\) are
non-affine.

---

## 3. The non-prime exterior potential is analytic

Fix

\`\`\`math
x_0>c.
\`\`\`

Choose a compact neighborhood \(J\ni x_0\) with

\`\`\`math
\inf J>c.
\`\`\`

Then

\`\`\`math
x-y
\ge
\inf J-c
>
0
\`\`\`

for \(x\in J\), \(y\in K_u\).

All derivatives of \(g_{\rm an}(x-y)\) are uniformly bounded on the resulting
compact \(t\)-range.

Since \(u\in L^1_c\), differentiation under the integral is lawful to every
order.

The local Taylor series also integrates termwise.

Thus

\`\`\`math
\boxed{
F_{{\rm an},u}
\text{ is real analytic on }(c,\infty).
}
\`\`\`

The non-prime part therefore cannot by itself create a first finite
nonanalytic activation point after a constant interval.

---

## 4. Prime-ramp second derivative

For one prime power, distributionally,

\`\`\`math
\frac{d^2}{dt^2}
(t-\log n)_+
=
\delta(t-\log n).
\`\`\`

Therefore

\`\`\`math
\boxed{
P_{n,u}''(x)
=
\frac{\Lambda(n)}{\sqrt n}
u(x-\log n)
}
\`\`\`

as distributions.

Equivalently, the only local obstruction to analyticity of \(P_{n,u}\) is the
translated analytic singular support

\`\`\`math
\log n
+
\operatorname{singsupp}_{\omega}u.
\`\`\`

If \(u(\,\cdot-\log n)\) is real analytic on an interval \(J\), then
\(P_{n,u}''\) is real analytic there, and hence \(P_{n,u}\) itself is real
analytic there up to an affine integration term.

---

## 5. Local finiteness of the shifted-source family

Fix a compact exterior interval

\`\`\`math
J\subset(c,\infty).
\`\`\`

A prime ramp can interact nontrivially with the source only when

\`\`\`math
x-\log n
\in
[-c,c]
\`\`\`

for some \(x\in J\).

Hence

\`\`\`math
\log n
\in
[\inf J-c,\sup J+c].
\`\`\`

Only finitely many prime powers lie in this bounded logarithmic interval.

Thus the family

\`\`\`math
\left\{
\log n+\operatorname{singsupp}_{\omega}u
\right\}_{n=p^m}
\`\`\`

is locally finite on \((c,\infty)\).

In particular its union is locally closed.

---

## 6. Analytic first-activation theorem

Suppose for contradiction that

\`\`\`math
a_{\max}
\notin
\bigcup_{n=p^m}
\left(
\log n+\operatorname{singsupp}_{\omega}u
\right).
\`\`\`

By local finiteness, there exists an open interval

\`\`\`math
J
=
(a_{\max}-\delta,a_{\max}+\delta)
\`\`\`

meeting none of the shifted analytic singular supports.

Hence every locally relevant \(u(\,\cdot-\log n)\) is real analytic on \(J\).

By Section 4, every prime contribution \(P_{n,u}\) is real analytic on \(J\).

By Section 3, the non-prime contribution is real analytic on \(J\).

Therefore

\`\`\`math
\boxed{
F_u
\text{ is real analytic on }J.
}
\`\`\`

But by definition of \(a_{\max}\),

\`\`\`math
F_u=C
\`\`\`

on the nonempty interval

\`\`\`math
J\cap(c,a_{\max}).
\`\`\`

The real-analytic identity theorem forces

\`\`\`math
F_u=C
\`\`\`

through all of \(J\).

This contradicts maximality of \(a_{\max}\).

Therefore

\`\`\`math
\boxed{
a_{\max}
\in
\bigcup_{n=p^m}
\left(
\log n+\operatorname{singsupp}_{\omega}u
\right).
}
\`\`\`

This is the analytic first-activation theorem.

---

## 7. Arithmetic activation shell

Since

\`\`\`math
\operatorname{singsupp}_{\omega}u
\subseteq
K_u
\subseteq[-c,c],
\`\`\`

there exist a prime power \(n=p^m\) and

\`\`\`math
y
\in
\operatorname{singsupp}_{\omega}u
\`\`\`

such that

\`\`\`math
\boxed{
a_{\max}
=
\log n+y.
}
\`\`\`

Therefore

\`\`\`math
a_{\max}-c
\le
\log n
\le
a_{\max}+c.
\`\`\`

Equivalently,

\`\`\`math
\boxed{
e^{a_{\max}-c}
\le
n
\le
e^{a_{\max}+c}.
}
\`\`\`

Thus only finitely many prime powers can own first activation at a given
maximal collar edge.

This is the analytic-singularity activation shell.

---

## 8. The weaker shifted-support theorem

Dropping analytic singular support gives immediately

\`\`\`math
\boxed{
a_{\max}
\in
\bigcup_{n=p^m}
\left(
\log n+K_u
\right).
}
\`\`\`

This is useful when one wants only support custody.

It says first activation cannot be caused by the smooth archimedean/pole
sector in isolation.

A prime-power moving kink must encounter the physical source.

---

## 9. The activation point need not be a source endpoint

The theorem does **not** prove

\`\`\`math
y
=
\inf K_u
\quad\text{or}\quad
y
=
\sup K_u.
\`\`\`

The source has only

\`\`\`math
u\in L^2(-c,c)
\`\`\`

at the screw level.

Its analytic singular support may fill a whole interval.

A point

\`\`\`math
y
\in
\operatorname{int}K_u
\`\`\`

can therefore be an analytic singularity.

Then

\`\`\`math
a_{\max}
=
\log n+y
\`\`\`

is compatible with first activation even though no support boundary is being
crossed.

So:

\`\`\`math
\boxed{
\text{first activation is arithmetic-singularity localized,
not endpoint localized}.
}
\`\`\`

---

## 10. Full-support sources make the support localization weak

If

\`\`\`math
K_u=[-c,c],
\`\`\`

then the weaker activation condition becomes

\`\`\`math
a_{\max}
\in
\bigcup_{n=p^m}
[\log n-c,\log n+c].
\`\`\`

Near the live neutral regime this union can cover the relevant exterior
region densely or even continuously through overlapping intervals.

Therefore the shifted-support version alone may give no useful numerical
restriction on \(a_{\max}\).

The analytic-singular-support refinement is the stronger statement.

But without additional regularity, even that singular support may occupy the
whole source interval.

---

## 11. Parity supplies no independent activation equation

Work in one parity block.

Because \(D=i\,d/dx\) flips parity, the screw source \(u\) has definite parity,
and therefore

\`\`\`math
K_u=-K_u
\`\`\`

and

\`\`\`math
\operatorname{singsupp}_{\omega}u
=
-
\operatorname{singsupp}_{\omega}u.
\`\`\`

The left first-activation condition at \(-a_{\max}\) is the reflected copy of
the right condition.

Thus parity gives no second independent arithmetic equation for
\(a_{\max}\).

It only symmetrizes the activation owner.

---

## 12. Zero mean supplies no local exclusion

The screw source satisfies

\`\`\`math
\int_{-c}^{c}u(y)\,dy
=
0.
\`\`\`

This is why a fully activated prime ramp becomes constant:

if

\`\`\`math
x-\log n
\ge
\sup K_u,
\`\`\`

then

\`\`\`math
\begin{aligned}
P_{n,u}(x)
&=
\frac{\Lambda(n)}{\sqrt n}
\int
(x-y-\log n)u(y)\,dy
\\
&=
-
\frac{\Lambda(n)}{\sqrt n}
\int
y\,u(y)\,dy,
\end{aligned}
\`\`\`

independent of \(x\).

But zero mean does not prevent

\`\`\`math
y
\in
\operatorname{singsupp}_{\omega}u.
\`\`\`

Hence it does not exclude any candidate first-activation owner supplied by
Section 7.

The moment law controls the fully activated far regime, not the local
singularity location.

---

## 13. What first activation now means

The maximal collar can therefore fail only when at least one arithmetic kink
is currently sweeping through a nonanalytic source location.

Locally, the second derivative has the form

\`\`\`math
\boxed{
F_u''(x)
=
A_u(x)
+
\sum_{\log n\in I_x}
\frac{\Lambda(n)}{\sqrt n}
u(x-\log n),
}
\`\`\`

where:

- \(A_u\) is real analytic near \(a_{\max}\);
- \(I_x\) is a locally finite set of relevant prime delays.

On the plateau,

\`\`\`math
F_u''=0
\`\`\`

distributionally.

At the maximal edge this cancellation ceases.

The theorem identifies where that loss of cancellation can occur, but not which
prime/source singularity owns it when several shifted singularities coincide.

---

## 14. Relation to the null-extension interface

RPB-42 makes the null-extension obstruction more concrete:

\`\`\`math
\boxed{
\text{first failure of neutral persistence}
\Longrightarrow
\text{prime-power delay meets source analytic singularity}.
}
\`\`\`

But the source analytic singularities are themselves not controlled by the
current Horizon-1 data.

The logarithmic-order compact-window equation does not supply positive
Sobolev or analytic regularity of \(u\).

Therefore RPB-42 does not close

\`\`\`text
AZ-FIN-WEIL-NULL-EXTENSION.
\`\`\`

It identifies the local owner of first activation rather than excluding it.

---

## 15. RPB-42 determination

\`\`\`math
\boxed{
\textbf{RPB-42 — MAXIMAL COLLAR FIRST ACTIVATION MUST OCCUR AT A PRIME-POWER SHIFT OF SOURCE ANALYTIC SINGULAR SUPPORT.}
}
\`\`\`

Exact localization:

\`\`\`math
\boxed{
a_{\max}
=
\log n+y,
\qquad
y\in\operatorname{singsupp}_{\omega}u
}
\`\`\`

for at least one prime power in the finite shell

\`\`\`math
\boxed{
e^{a_{\max}-c}
\le
n
\le
e^{a_{\max}+c}.
}
\`\`\`

The smooth archimedean/pole sector cannot generate the first activation by
itself.

However:

- the responsible \(y\) need not be a support endpoint;
- parity only reflects the same condition;
- zero mean does not exclude the local source singularity;
- current regularity allows analytic singular support throughout the source.

Next cursor:

\`\`\`text
RPB-43 / ANALYTIC-SINGULAR-SUPPORT PROPAGATION UNDER PRIME DELAYS
\`\`\`

The next pass should test whether the interior neutral equation propagates
analytic singularities along the active prime-log delay graph strongly enough
to force:

1. endpoint ownership of the activation singularity;
2. dense analytic singular support;
3. incompatibility with compact support;
4. or another explicit no-go showing that analytic-wavefront propagation does
   not improve the current null-extension interface.
