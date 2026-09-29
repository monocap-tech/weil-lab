# RPB-43 — Analytic-singular-support propagation under prime delays

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS / INTERIOR ANALYTICITY COLLAPSES SOURCE SINGULAR SUPPORT TO THE TWO ENDPOINTS / FIRST ACTIVATION IS ENDPOINT-ARITHMETIC / ONLY PAIRED ENDPOINT RESONANCES CAN BE CROSSED**  
**Dependencies:** RPB-31, RPB-33, RPB-42; RPB-EXT-A1 analytic elliptic regularity.  
**Promotion status:** none.

## 0. Objective

RPB-42 proved that if a screw-visible neutral potential has a maximal strict
constant collar radius

\`\`\`math
a_{\max}>c,
\`\`\`

then

\`\`\`math
a_{\max}
\in
\bigcup_{n=p^m}
\left(
\log n+\operatorname{singsupp}_{\omega}u
\right),
\`\`\`

where \(u=Dh\) is the compact screw source.

The unresolved question was whether the interior neutral equation propagates
analytic singularities through the prime-delay graph, potentially producing a
dense analytic singular set.

RPB-43 finds the opposite structure.

Once the finite prime translations are regrouped with the archimedean
multiplier into the **full compact-window scalar symbol**, that operator is
analytic-elliptic at high frequency.

Therefore the neutral core mode is real analytic throughout the open support.

Consequently:

\`\`\`math
\boxed{
\operatorname{singsupp}_{\omega}u
=
\{-c,c\}.
}
\`\`\`

So first activation is endpoint-owned:

\`\`\`math
\boxed{
a_{\max}
=
c+\log n
\quad\text{or}\quad
a_{\max}
=
\log n-c.
}
\`\`\`

The only way a constant collar can cross such an endpoint activation is through
a paired right-exit/left-entry collision, which requires

\`\`\`math
\boxed{
e^{2c}
=
\frac{m}{n}
}
\`\`\`

for prime powers \(m,n\), plus a nontrivial analytic germ-matching condition.

---

## 1. Interior neutral equation

Let

\`\`\`math
0\ne h
\in
H_0^1(-c,c)
\`\`\`

be a screw-visible endpoint neutral mode:

\`\`\`math
A_ch=0.
\`\`\`

Write the translation-invariant whole-line part as

\`\`\`math
\boxed{
\mathcal P_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
\left(
\tau_{\log n}
+
\tau_{-\log n}
\right),
}
\`\`\`

with the endpoint finite-prime convention appropriate to \(A_c\).

Its Fourier multiplier is

\`\`\`math
\boxed{
\Psi_c(\xi)
=
\Re\psi\!\left(
\frac14+\frac{i\xi}{2}
\right)
-
\log\pi
-
\sum_{\log n<2c}
\frac{2\Lambda(n)}{\sqrt n}
\cos(\xi\log n).
}
\`\`\`

The neutral equation is

\`\`\`math
\boxed{
\mathcal P_ch
=
-
\mathcal R_{\rm pole}h
}
\`\`\`

on the interior interval.

---

## 2. The full scalar symbol is analytic-elliptic at high frequency

The digamma term is real analytic on the real frequency axis.

The prime contribution is a finite trigonometric polynomial.

Therefore

\`\`\`math
\Psi_c
\in
C^\omega(\mathbb R).
\`\`\`

Moreover,

\`\`\`math
\Psi_c(\xi)
=
\log|\xi|
+
O_c(1)
\qquad
(|\xi|\to\infty).
\`\`\`

Hence there exist \(R_c\) and \(m_c>0\) such that

\`\`\`math
|\Psi_c(\xi)|
\ge
m_c\log(e+|\xi|)
\qquad
(|\xi|\ge R_c).
\`\`\`

The symbol is therefore noncharacteristic at all sufficiently large
frequencies.

The derivatives of the digamma multiplier satisfy the usual analytic symbol
bounds, while the finite trigonometric polynomial has entire frequency
dependence.

Thus \(\mathcal P_c\) is analytically elliptic in the microlocal
high-frequency sense.

### External pin

RPB-EXT-A1 records Hörmander,
*Analysis of Linear Partial Differential Operators I*,
Theorem 9.5.1:

\`\`\`math
WF_A(\mathcal P_ch)
\subseteq
WF_A(h)
\subseteq
\operatorname{Char}(\mathcal P_c)
\cup
WF_A(\mathcal P_ch).
\`\`\`

Since the high-frequency characteristic set is empty,

\`\`\`math
WF_A(h)
=
WF_A(\mathcal P_ch)
\`\`\`

in the interior.

---

## 3. The pole/evaluation range is analytic

The compact-window pole/evaluation contribution is finite rank.

The evaluation

\`\`\`math
H(i/2)
=
\int_{-c}^{c}
h(x)e^{x/2}\,dx
\`\`\`

and its Hermitian/reflected counterpart generate physical rank-one/rank-two
ranges spanned by fixed exponential functions of the form

\`\`\`math
e^{x/2},
\qquad
e^{-x/2},
\`\`\`

up to the fixed normalization convention.

These range functions are real analytic.

Therefore

\`\`\`math
\boxed{
\mathcal R_{\rm pole}h
\in
C^\omega(-c,c).
}
\`\`\`

So the right-hand side of the interior neutral equation is analytic.

---

## 4. Interior analytic regularity

By Sections 2 and 3 and analytic elliptic regularity,

\`\`\`math
\boxed{
h
\in
C^\omega(-c,c).
}
\`\`\`

The screw source is

\`\`\`math
u
=
Dh
=
i h'.
\`\`\`

Hence

\`\`\`math
\boxed{
u
\in
C^\omega(-c,c).
}
\`\`\`

This is a substantial strengthening of the earlier domain statements.

It does **not** contradict RPB-28--31:

those passes concerned zero-extension Sobolev regularity and boundary layers.

Interior analyticity is compatible with singular behavior at the support
endpoints.

---

## 5. The source is nonzero and has full interior support

If

\`\`\`math
u=0,
\`\`\`

then \(h\) is constant on \((-c,c)\).

Since

\`\`\`math
h\in H_0^1(-c,c),
\`\`\`

the boundary trace forces

\`\`\`math
h=0,
\`\`\`

contradicting the nonzero neutral mode.

Thus

\`\`\`math
u\ne0.
\`\`\`

Now suppose \(u\) vanished on a nonempty open subinterval of \((-c,c)\).

Because \(u\) is real analytic on the connected interval \((-c,c)\), the
identity theorem would give

\`\`\`math
u\equiv0.
\`\`\`

Contradiction.

Therefore

\`\`\`math
\boxed{
\operatorname{ess\,supp}u
=
[-c,c].
}
\`\`\`

The source may have isolated interior zeros, but it has no open support gap.

---

## 6. Analytic singular support of the zero extension

Extend \(u\) by zero outside \([-c,c]\).

The extension is analytic on:

- the whole open interior \((-c,c)\);
- the two exterior half-lines.

Therefore

\`\`\`math
\operatorname{singsupp}_{\omega}u
\subseteq
\{-c,c\}.
\`\`\`

Neither endpoint can be analytically regular.

Indeed, suppose the zero extension were real analytic in a neighborhood of
\(c\).

It vanishes on the exterior subinterval

\`\`\`math
(c,c+\varepsilon).
\`\`\`

Analytic continuation would then force it to vanish on an interior
neighborhood

\`\`\`math
(c-\varepsilon,c),
\`\`\`

and Section 5 would imply

\`\`\`math
u\equiv0.
\`\`\`

The same argument applies at \(-c\).

Hence

\`\`\`math
\boxed{
\operatorname{singsupp}_{\omega}u
=
\{-c,c\}.
}
\`\`\`

This is the endpoint-only analytic singular support theorem.

---

## 7. RPB-42 collapses to endpoint activation

RPB-42 proved

\`\`\`math
a_{\max}
\in
\bigcup_{n=p^m}
\left(
\log n+\operatorname{singsupp}_{\omega}u
\right).
\`\`\`

Substituting Section 6 gives

\`\`\`math
\boxed{
a_{\max}
\in
\left\{
\log n-c,\,
\log n+c:
n=p^m
\right\}.
}
\`\`\`

Because

\`\`\`math
a_{\max}>c,
\`\`\`

the right-endpoint family is

\`\`\`math
\boxed{
a_{\max}
=
c+\log n,
}
\`\`\`

while the left-endpoint family requires

\`\`\`math
\log n>2c
\`\`\`

and has

\`\`\`math
\boxed{
a_{\max}
=
\log n-c.
}
\`\`\`

So the maximal collar edge belongs to a discrete arithmetic activation
spectrum.

---

## 8. Local form of an endpoint activation event

Let

\`\`\`math
x_0
=
c+\log n.
\`\`\`

This is a **right-endpoint exit** event.

Write

\`\`\`math
s=x-x_0.
\`\`\`

Then the singular part of the second derivative of the corresponding prime
ramp is

\`\`\`math
\boxed{
\frac{\Lambda(n)}{\sqrt n}
u(c+s).
}
\`\`\`

For \(s<0\), the argument lies inside the source.

For \(s>0\), it lies outside and the zero extension vanishes.

Likewise a **left-endpoint entry** event

\`\`\`math
x_0
=
\log m-c
\`\`\`

has singular part

\`\`\`math
\boxed{
\frac{\Lambda(m)}{\sqrt m}
u(-c+s),
}
\`\`\`

which vanishes for \(s<0\) and enters the source for \(s>0\).

All prime terms whose shifted endpoints do not equal \(x_0\), together with
the non-prime screw contribution, are real analytic in a neighborhood of
\(x_0\).

---

## 9. An unpaired endpoint event cannot be crossed by a constant plateau

Assume the potential is constant on both sides of an endpoint event \(x_0\).

Then

\`\`\`math
F_u''=0
\`\`\`

on a punctured neighborhood on each side.

Suppose \(x_0\) is a right-endpoint exit with no simultaneous left-endpoint
entry.

All other contributions are analytic through \(x_0\).

Therefore

\`\`\`math
\frac{\Lambda(n)}{\sqrt n}
u(c+s)
\qquad
(s<0)
\`\`\`

must agree with the restriction of an analytic germ across \(s=0\).

But for \(s>0\) that same translated zero extension is identically zero.

If the plateau crossed \(x_0\) without another endpoint singularity, the
translated source would be analytically regular across the endpoint.

Section 6 excludes this.

Therefore

\`\`\`math
\boxed{
\text{a constant plateau cannot cross an unpaired endpoint activation}.
}
\`\`\`

The reflected statement holds for an unpaired left-endpoint entry.

---

## 10. The only possible crossing mechanism is a paired collision

A right-endpoint exit

\`\`\`math
c+\log n
\`\`\`

and a left-endpoint entry

\`\`\`math
\log m-c
\`\`\`

coincide exactly when

\`\`\`math
c+\log n
=
\log m-c.
\`\`\`

Equivalently,

\`\`\`math
\boxed{
2c
=
\log\frac{m}{n},
}
\`\`\`

or

\`\`\`math
\boxed{
e^{2c}
=
\frac{m}{n}.
}
\`\`\`

Here \(m,n\) are prime powers.

No two distinct right-endpoint exit events can coincide.

No two distinct left-endpoint entry events can coincide.

Thus an endpoint activation point contains at most one singular germ from each
side of the source.

The only possible cancellation geometry is a paired exit/entry collision.

---

## 11. Germ matching at a paired collision

Let

\`\`\`math
x_0
=
c+\log n
=
\log m-c.
\`\`\`

Near \(s=0\), the singular pieces are:

for \(s<0\),

\`\`\`math
\frac{\Lambda(n)}{\sqrt n}
u(c+s),
\`\`\`

and for \(s>0\),

\`\`\`math
\frac{\Lambda(m)}{\sqrt m}
u(-c+s).
\`\`\`

Let \(A(s)\) denote the sum of all contributions analytic through \(s=0\).

If the constant plateau crosses the collision, then

\`\`\`math
A(s)
+
\frac{\Lambda(n)}{\sqrt n}
u(c+s)
=
0
\qquad
(s<0),
\`\`\`

while

\`\`\`math
A(s)
+
\frac{\Lambda(m)}{\sqrt m}
u(-c+s)
=
0
\qquad
(s>0).
\`\`\`

Thus the two weighted endpoint germs must be opposite restrictions of the same
analytic germ.

For a parity eigenmode,

\`\`\`math
u(-x)
=
\varepsilon_u u(x),
\qquad
\varepsilon_u\in\{+1,-1\},
\`\`\`

so the condition becomes a weighted reflected endpoint-germ matching relation.

This is a genuine additional obligation.

Arithmetic collision alone is not sufficient.

---

## 12. Nonresonant case

Assume

\`\`\`math
\boxed{
e^{2c}
\notin
\left\{
\frac{m}{n}:
m,n\text{ prime powers}
\right\}.
}
\`\`\`

Then no paired endpoint collision exists.

Let

\`\`\`math
n_+(c)
=
\min
\left\{
p^m:
\log(p^m)>2c
\right\}.
\`\`\`

The first right-endpoint exit above \(c\) occurs at

\`\`\`math
c+\log2.
\`\`\`

The first left-endpoint entry above \(c\) occurs at

\`\`\`math
\log n_+(c)-c.
\`\`\`

Hence the first activation radius is

\`\`\`math
\boxed{
a_1(c)
=
\min
\left\{
c+\log2,\,
\log n_+(c)-c
\right\}.
}
\`\`\`

If a strict constant collar exists at all, Section 9 prevents it from crossing
this first activation.

Therefore

\`\`\`math
\boxed{
a_{\max}
=
a_1(c)
}
\`\`\`

in the nonresonant case.

This is an exact arithmetic quantization of the maximal collar radius.

---

## 13. Resonant case

If

\`\`\`math
e^{2c}
=
\frac{m}{n}
\`\`\`

for prime powers \(m,n\), then paired endpoint collisions exist.

A constant collar may cross such a collision only if the weighted endpoint
germs satisfy the analytic matching condition of Section 11.

The current RPB data do not determine those boundary germs.

In particular:

- \(H_0^1\) gives the boundary trace of \(h\), not an analytic boundary jet for
  \(u=ih'\);
- parity relates the two endpoint germs but does not fix their magnitude;
- zero mean is a global integral constraint and does not determine the
  one-sided analytic continuation germ.

Therefore resonance remains a genuine branch.

---

## 14. Relation to the dense delay orbit

RPB-37 found that the additive group generated by the active prime logarithms
is dense.

RPB-43 shows that this does **not** imply dense analytic singular support of
the neutral source.

The reason is that the delay-by-delay picture is not the correct interior
microlocal organization.

Once the finite translations are grouped into the full scalar symbol
\(\Psi_c\), that symbol is analytic-elliptic and removes all interior analytic
wavefront.

Thus:

\`\`\`math
\boxed{
\text{dense delay orbit}
\quad\text{and}\quad
\text{endpoint-only analytic singular support}
}
\`\`\`

are compatible.

The dense orbit concerns value coupling.

The analytic wavefront is controlled by the full elliptic symbol.

---

## 15. RPB-43 determination

\`\`\`math
\boxed{
\textbf{RPB-43 — CORE-NEUTRAL ANALYTIC SINGULAR SUPPORT IS ENDPOINT-ONLY; MAXIMAL COLLAR ACTIVATION IS DISCRETE AND ENDPOINT-ARITHMETIC.}
}
\`\`\`

Exact interior theorem:

\`\`\`math
\boxed{
h,u
\in
C^\omega(-c,c),
\qquad
\operatorname{singsupp}_{\omega}u
=
\{-c,c\}.
}
\`\`\`

Exact activation spectrum:

\`\`\`math
\boxed{
a_{\max}
\in
\{c+\log n,\ \log n-c:n=p^m\}.
}
\`\`\`

Crossing criterion:

\`\`\`math
\boxed{
\text{an unpaired activation cannot be crossed}.
}
\`\`\`

The only possible crossing mechanism is

\`\`\`math
\boxed{
e^{2c}=m/n
}
\`\`\`

together with weighted analytic endpoint-germ matching.

In the nonresonant case,

\`\`\`math
\boxed{
a_{\max}
=
\min\{c+\log2,\ \log n_+(c)-c\}.
}
\`\`\`

Next cursor:

\`\`\`text
RPB-44 / PAIRED ENDPOINT COLLISION RESONANCE AND GERM MATCHING
\`\`\`

The next pass should analyze the resonant branch

\`\`\`math
e^{2c}=m/n
\`\`\`

for prime powers \(m,n\):

1. use parity to write the exact endpoint-germ matching equation;
2. determine whether the von Mangoldt weights can satisfy it;
3. test whether crossing one collision forces an infinite collision ladder;
4. determine whether such a ladder is compatible with the finite maximal
   collar radius and with the nonzero/global-radical exclusion.
