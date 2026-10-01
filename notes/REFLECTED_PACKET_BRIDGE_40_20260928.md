# RPB-40 — Divisor-cleared Carleman numerator growth test

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS / DIVISOR-CLEARED NUMERATORS ARE ORDER-ONE MAXIMAL TYPE / CARTWRIGHT ROUTE EXCLUDED / SUBLEADING INDICATOR RETAINS THE EXTERIOR SUPPORT EDGE**  
**Dependencies:** RPB-11, RPB-33, RPB-38, RPB-39; Stirling asymptotics for \(\Gamma\); standard Laplace support theorem.  
**Promotion status:** none.

## 0. Objective

RPB-39 produced the entire divisor-cleared right and left Carleman numerators

\`\`\`math
N_+(z)
=
z^2
\xi\!\left(
\frac12-iz
\right)
\mathcal C_+^{\rm mer}(z),
\`\`\`

and

\`\`\`math
N_-(z)
=
z^2
\xi\!\left(
\frac12+iz
\right)
\mathcal C_-^{\rm mer}(z).
\`\`\`

At a simple zeta zero,

\`\`\`math
N_+(z_\rho)
=
V(z_\rho)\xi'(\rho).
\`\`\`

RPB-40 asks:

1. what entire growth class do \(N_\pm\) belong to?
2. can they be placed in Cartwright or a de Branges class?
3. does the surviving \(\gg T\log T\) zeta interpolation density contradict
   their growth?
4. does the collar hypothesis force any stronger cancellation?

The answers are:

\`\`\`math
\boxed{
\operatorname{ord}(N_\pm)=1,
\qquad
\operatorname{type}_1(N_\pm)=\infty
}
\`\`\`

for the nonzero exterior tails.

Thus the direct Cartwright/Jensen finite-type route is unavailable.

The same calculation leaves one useful invariant: after subtracting the
universal \(\xi\)-growth, the linear indicator records the first support point
of the exterior tail.

---

## 1. Entire representation

RPB-39 gives

\`\`\`math
\boxed{
\begin{aligned}
N_+(z)
={}&
V(z)
\xi'\!\left(
\frac12-iz
\right)
\\
&-
z^2
\xi\!\left(
\frac12-iz
\right)
E_+(z)
\\
&+
\frac{Cz}{i}
e^{iaz}
\xi\!\left(
\frac12-iz
\right),
\end{aligned}
}
\`\`\`

where:

- \(V\) is the compact-source transform;
- \(E_+\) is the finite-interval correction;
- \(C\) is the collar constant.

The functions \(V\), \(E_+\), and \(e^{iaz}\) are entire of finite exponential
type.

The same holds for the reflected left numerator.

---

## 2. Upper entire order is at most one

The Riemann \(\xi\)-function is entire of order one.

Its derivative has the same entire order.

Multiplication by a finite-exponential-type entire function does not raise
the order above one, and finite sums preserve the upper order bound.

Therefore

\`\`\`math
\boxed{
\operatorname{ord}(N_\pm)
\le1.
}
\`\`\`

The issue is whether the type at order one can be finite.

### External context

The standard classical statement is stronger: \(\xi(s)\) is an entire
function of order one and maximal type.

See the *Encyclopedia of Mathematics*, entry “Riemann xi-function.”

---

## 3. The exterior tails are nonzero

Choose the screw-visible endpoint neutral mode in one parity block.

This is lawful because the compact-window screw operator commutes with
reflection.

Then:

- if the screw potential \(F_u\) is even, the collar residual
  \[
  R=F_u-C
  \]
  is even;
- if \(F_u\) is odd, collar constancy forces \(C=0\), so \(R=F_u\) is odd.

Thus the right and left exterior tails vanish simultaneously.

Suppose

\`\`\`math
R_+\equiv0.
\`\`\`

Parity then gives

\`\`\`math
R_-\equiv0.
\`\`\`

Hence

\`\`\`math
F_u\equiv C
\`\`\`

globally.

RPB-35 gives

\`\`\`math
F_u'
=
-i\,W*h.
\`\`\`

Therefore

\`\`\`math
W*h=0
\`\`\`

globally.

This makes the nonzero compact mode \(h\) a global Weil radical vector, which
RPB-11 excludes unconditionally.

Hence

\`\`\`math
\boxed{
R_+\ne0,
\qquad
R_-\ne0.
}
\`\`\`

---

## 4. Growth of \(\xi\) on the positive real axis

Put

\`\`\`math
s
=
\frac12+Y,
\qquad
Y\to+\infty.
\`\`\`

Using

\`\`\`math
\xi(s)
=
\frac12
s(s-1)
\pi^{-s/2}
\Gamma(s/2)
\zeta(s),
\`\`\`

together with

\`\`\`math
\zeta(s)\to1
\`\`\`

and Stirling's formula,

\`\`\`math
\log\Gamma(s/2)
=
\left(
\frac{s}{2}-\frac12
\right)
\log(s/2)
-
\frac{s}{2}
+
O(\log s),
\`\`\`

we obtain

\`\`\`math
\boxed{
\log
\xi\!\left(
\frac12+Y
\right)
=
\frac{Y}{2}\log Y
+
O(Y).
}
\`\`\`

In particular, for every fixed \(A>0\),

\`\`\`math
\xi\!\left(
\frac12+Y
\right)
e^{-AY}
\to
+\infty
\`\`\`

along the positive real axis.

This is the maximal-type growth that will dominate any finite exponential
support factor.

---

## 5. Native right-tail identity on the imaginary axis

For \(Y>1/2\), put

\`\`\`math
z=iY.
\`\`\`

Then

\`\`\`math
\frac12-iz
=
\frac12+Y.
\`\`\`

From the defining identity

\`\`\`math
N_+(z)
=
z^2
\xi\!\left(
\frac12-iz
\right)
\mathcal C_+(z),
\`\`\`

valid on the native right Carleman half-plane, we get

\`\`\`math
\boxed{
|N_+(iY)|
=
Y^2
\xi\!\left(
\frac12+Y
\right)
|\mathcal C_+(iY)|.
}
\`\`\`

But

\`\`\`math
\mathcal C_+(iY)
=
\int_a^\infty
R_+(x)e^{-Yx}\,dx.
\`\`\`

Thus \(\mathcal C_+(iY)\) is the ordinary Laplace transform of the nonzero
right exterior tail.

---

## 6. Finite exponential type would force superexponential tail decay

Assume for contradiction that \(N_+\) has finite exponential type.

Then there exists \(\tau<\infty\) such that

\`\`\`math
\log|N_+(iY)|
\le
\tau Y
+
o(Y).
\`\`\`

Section 5 gives

\`\`\`math
\log|\mathcal C_+(iY)|
\le
\tau Y
-
\log\xi\!\left(
\frac12+Y
\right)
+
O(\log Y).
\`\`\`

By Section 4,

\`\`\`math
\boxed{
\log|\mathcal C_+(iY)|
\le
-\frac{Y}{2}\log Y
+
O(Y).
}
\`\`\`

Therefore, for every \(A>0\),

\`\`\`math
\boxed{
\mathcal C_+(iY)
=
O_A(e^{-AY}).
}
\`\`\`

So finite exponential type of \(N_+\) would force the right-tail Laplace
transform to decay faster than every exponential.

---

## 7. Laplace support theorem excludes that decay

Let

\`\`\`math
b_+
=
\inf\operatorname{ess\,supp}R_+.
\`\`\`

Because \(R_+\ne0\) and is supported in a finite-left-edge half-line,

\`\`\`math
a
\le
b_+
<
\infty.
\`\`\`

The standard Laplace support theorem gives

\`\`\`math
\boxed{
\limsup_{Y\to+\infty}
\frac1Y
\log
|\mathcal C_+(iY)|
=
-b_+.
}
\`\`\`

Equivalently, a nonzero tail with finite left support edge cannot have a
Laplace transform decaying faster than every exponential.

This contradicts Section 6.

Hence

\`\`\`math
\boxed{
N_+
\text{ is not of finite exponential type}.
}
\`\`\`

The reflected argument gives the same conclusion for \(N_-\).

### Scope

Only the support theorem for a one-sided Laplace transform is consumed here.

No positivity or fixed sign of \(R_\pm\) is required.

---

## 8. Exact order/type classification

Section 2 gave

\`\`\`math
\operatorname{ord}(N_\pm)\le1.
\`\`\`

Section 7 shows that \(N_\pm\) do not have finite exponential type.

An entire function of order strictly less than one has zero exponential type
when measured at order one.

Therefore the order cannot be \(<1\).

Thus

\`\`\`math
\boxed{
\operatorname{ord}(N_\pm)=1.
}
\`\`\`

And at order one,

\`\`\`math
\boxed{
\operatorname{type}_1(N_\pm)=\infty.
}
\`\`\`

So \(N_\pm\) are order-one maximal-type entire functions.

This is not merely inherited as a loose upper bound from \(\xi\).

It is forced by the coexistence of:

1. the \(\xi\) factor;
2. a nonzero exterior tail with finite support onset.

---

## 9. Cartwright route is excluded

A Cartwright entire function has finite exponential type and satisfies the
usual logarithmic-integrability condition on the real axis.

Section 8 already fails the first requirement.

Hence

\`\`\`math
\boxed{
N_\pm
\notin
\text{Cartwright class}.
}
\`\`\`

Therefore the finite-type zero-density machinery used for compact
Paley--Wiener transforms in RPB-11 and RPB-38 cannot be transplanted to the
divisor-cleared Carleman numerators.

This closes the direct Cartwright route.

---

## 10. The \(T\log T\) interpolation density is compatible with maximal type

At a simple zeta zero,

\`\`\`math
N_+(z_\rho)
=
V(z_\rho)\xi'(\rho).
\`\`\`

RPB-38 shows that this is nonzero at

\`\`\`math
\gg
T\log T
\`\`\`

simple critical divisor points up to height \(T\).

For a finite-exponential-type entire function, divisor-scale data of this
density would invite a Jensen/Paley--Wiener contradiction.

For an order-one maximal-type entire function, however, \(T\log T\) divisor
complexity is fully compatible with the growth class.

Indeed \(\xi\) itself is the basic model: it is order one of maximal type and
has zeta-zero counting of \(T\log T\) scale.

Therefore

\`\`\`math
\boxed{
\text{the surviving zeta interpolation density does not contradict the growth class of }N_\pm.
}
\`\`\`

The density is source custody, not yet rigidity.

---

## 11. Collar persistence cannot secretly lower the numerator to finite type

One possible loophole is that the collar equation might force exceptional
cancellation among the three entire terms in the explicit formula for
\(N_+\), reducing the numerator to finite type.

Sections 5--7 exclude this.

Any such reduction would imply the superexponential decay of
\(\mathcal C_+(iY)\), and hence

\`\`\`math
R_+\equiv0.
\`\`\`

By parity this would force

\`\`\`math
R\equiv0,
\`\`\`

which RPB-11 excludes for a nonzero compact neutral mode.

Thus

\`\`\`math
\boxed{
\text{no hidden collar cancellation can place }N_\pm
\text{ in finite exponential type}.
}
\`\`\`

The maximal-type obstruction is intrinsic.

---

## 12. Direct xi-based de Branges normalization is not unconditional

A natural xi-based function in the current literature is

\`\`\`math
E_\xi(z)
=
\xi\!\left(
\frac12-iz
\right)
+
\xi'\!\left(
\frac12-iz
\right).
\`\`\`

The Lagarias/Suzuki framework places \(E_\xi\) in the Hermite--Biehler class
**under the Riemann hypothesis**.

That assumption is explicit.

Therefore this natural de Branges structure cannot be used as an
unconditional input to close an RH-facing branch.

### External source

Masatoshi Suzuki,
*On the Hilbert space derived from the Weil distribution*,
Canadian Journal of Mathematics, published online 2025.

The introduction states that \(E_\xi\) belongs to the Hermite--Biehler class
under RH and constructs the associated de Branges/model spaces under that
hypothesis.

---

## 13. Dividing by \(\xi\) is not an unconditional de Branges substitute

One might instead divide the numerator by the maximal-type factor:

\`\`\`math
\frac{N_+(z)}
{\xi(1/2-iz)}
=
z^2
\mathcal C_+^{\rm mer}(z).
\`\`\`

But RPB-39 shows that

\`\`\`math
\mathcal C_+^{\rm mer}
\`\`\`

has infinitely many uncancelled zeta poles.

Thus the quotient is meromorphic, not entire.

It does not define a de Branges generating function.

Any further entire normalization would have to reinsert a divisor-clearing
factor and hence restore essentially the same \(\xi\)-scale growth.

No lawful unconditional de Branges normalization is presently available.

---

## 14. Support edge survives in the subleading indicator

Although the leading growth is universal and maximal,

\`\`\`math
\frac{Y}{2}\log Y,
\`\`\`

the tail still leaves a precise linear-order trace.

The Laplace support theorem gives

\`\`\`math
\limsup_{Y\to+\infty}
\frac1Y
\log
|\mathcal C_+(iY)|
=
-b_+.
\`\`\`

Therefore Section 5 yields

\`\`\`math
\boxed{
\limsup_{Y\to+\infty}
\frac{
\log|N_+(iY)|
-
\log\xi(1/2+Y)
}{
Y
}
=
-b_+.
}
\`\`\`

The polynomial factor \(Y^2\) contributes only

\`\`\`math
\frac{2\log Y}{Y}\to0.
\`\`\`

Thus the divisor-cleared numerator remembers the first exterior support point
after the universal xi growth is removed.

The left numerator analogously records the rightmost point of the left tail.

This is the exact surviving growth datum.

---

## 15. RPB-40 determination

\`\`\`math
\boxed{
\textbf{RPB-40 — DIVISOR-CLEARED CARLEMAN NUMERATORS ARE ORDER-ONE MAXIMAL TYPE; CARTWRIGHT/UNCONDITIONAL DE BRANGES CLOSURE FAILS.}
}
\`\`\`

Exact growth classification:

\`\`\`math
\boxed{
\operatorname{ord}(N_\pm)=1,
\qquad
\operatorname{type}_1(N_\pm)=\infty.
}
\`\`\`

Exact support-indicator remnant:

\`\`\`math
\boxed{
\limsup_{Y\to\infty}
\frac{
\log|N_+(iY)|
-
\log\xi(1/2+Y)
}{Y}
=
-b_+.
}
\`\`\`

Consequences:

- \(N_\pm\) are not Cartwright;
- \(T\log T\)-scale zeta interpolation is compatible with their growth;
- the natural xi-based de Branges structure is RH-conditional;
- dividing out \(\xi\) restores the uncancelled divisor and loses entire
  structure.

The next viable frequency-side datum is therefore not zero density but the
**subleading support indicator**.

Next cursor:

\`\`\`text
RPB-41 / CARLEMAN INDICATOR SUPPORT-EDGE MATCHING
\`\`\`

The next pass should compute the same vertical indicator from the explicit
entire identity

\`\`\`math
N_+
=
V\xi'
-
z^2\xi E_+
+
\frac{Cz}{i}e^{iaz}\xi
\`\`\`

and test whether endpoint Paley--Wiener indicators of \(V\) and \(E_+\) force
the tail onset \(b_+\) to equal the collar edge \(a\), a source-support
endpoint, or another rigid arithmetic value.

A mismatch would exclude strict collar persistence without requiring
Cartwright or quasianalytic spectral synthesis.
