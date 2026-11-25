# RPB-39 — Exterior-tail Fourier--Carleman factorization

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS AS EXACT TAIL TYPING / ONE-SIDED CARLEMAN DOMAINS ARE DISJOINT / CONTINUATION CARRIES THE UNCANCELLED ZETA DIVISOR / ORDINARY WIENER--HOPF INDEX NOT AVAILABLE**  
**Dependencies:** RPB-35 through RPB-38; Suzuki Theorem 1.1 one-sided transform and growth estimate.  
**Promotion status:** none.

## 0. Objective

RPB-38 retyped hypothetical collar persistence as an exterior spatial-gap
problem.

Let

\`\`\`math
0\ne u
\in
\ker G_c,
\qquad
F_u=g*u,
\`\`\`

and suppose that for some strict enlargement \(a>c\),

\`\`\`math
F_u(x)=C
\qquad
(|x|<a).
\`\`\`

The proposed frequency route was to split the exterior output into left and
right tails and seek a Wiener--Hopf / Fourier--Carleman factorization.

RPB-39 makes this exact.

The tails do have canonical one-sided Fourier--Carleman transforms, but their
natural analytic half-planes are separated by the entire critical strip

\`\`\`math
|\Im z|\le\frac12.
\`\`\`

Meromorphic continuation across that strip is governed by

\`\`\`math
\frac{\xi'}{\xi}
\left(
\frac12\mp iz
\right),
\`\`\`

and RPB-38 proves that a nonzero compact source leaves
\(\gg T\log T\) simple critical poles uncancelled.

Thus there is no ordinary real-line Hardy/Wiener--Hopf boundary problem with a
finite topological index.

The exact next object is the divisor-cleared entire numerator.

---

## 1. Unconditional growth of the screw function

Suzuki proves

\`\`\`math
\boxed{
\Psi(t)
\ll
\exp\!\left(
\frac{t}{2}
-
\kappa\sqrt t
\right)
}
\qquad
(t\to+\infty)
\`\`\`

for some \(\kappa>0\).

Since

\`\`\`math
g=-\Psi
\`\`\`

and \(g\) is even,

\`\`\`math
\boxed{
g(t)
=
O\!\left(
e^{|t|/2-\kappa\sqrt{|t|}}
\right).
}
\`\`\`

### External source

Masatoshi Suzuki,
*Aspects of the screw function corresponding to the Riemann zeta-function*,
Theorem 1.1(3).

---

## 2. Compact convolution inherits the same exponential rate

Because

\`\`\`math
u\in L^2(-c,c)
\subset
L^1(-c,c),
\`\`\`

for \(x\to+\infty\),

\`\`\`math
\begin{aligned}
|F_u(x)|
&\le
\int_{-c}^{c}
|g(x-y)||u(y)|\,dy
\\
&\le
C_u
\exp\!\left(
\frac{x}{2}
-
\kappa_1\sqrt x
\right)
\end{aligned}
\`\`\`

for some \(\kappa_1>0\).

The same estimate holds as \(x\to-\infty\).

Subtracting the collar constant \(C\) does not change the exponential rate.

Thus the exterior residual

\`\`\`math
R(x)
=
F_u(x)-C
\`\`\`

has exponential type \(1/2\) in the weak one-sided sense relevant here.

---

## 3. Right and left exterior tails

Under the collar hypothesis, define

\`\`\`math
R_+(x)
=
\mathbf1_{[a,\infty)}(x)
R(x),
\`\`\`

and

\`\`\`math
R_-(x)
=
\mathbf1_{(-\infty,-a]}(x)
R(x).
\`\`\`

Then

\`\`\`math
R
=
R_-+R_+,
\qquad
R=0
\text{ on }(-a,a).
\`\`\`

Define the one-sided Fourier--Carleman transforms

\`\`\`math
\mathcal C_+(z)
=
\int_a^\infty
R(x)e^{izx}\,dx,
\`\`\`

and

\`\`\`math
\mathcal C_-(z)
=
\int_{-\infty}^{-a}
R(x)e^{izx}\,dx.
\`\`\`

The growth estimate of Section 2 gives absolute convergence for

\`\`\`math
\boxed{
\Im z>\frac12
}
\`\`\`

on the right and

\`\`\`math
\boxed{
\Im z<-\frac12
}
\`\`\`

on the left.

At the boundary lines \(\Im z=\pm1/2\), the extra factor
\(e^{-\kappa_1\sqrt{|x|}}\) still gives absolute integrability, but the open
half-planes above are the analytic domains.

---

## 4. There is no bilateral convergence strip

A bilateral transform of \(R\) would require simultaneously

\`\`\`math
\Im z>\frac12
\`\`\`

for the right tail and

\`\`\`math
\Im z<-\frac12
\`\`\`

for the left tail.

No \(z\) satisfies both conditions.

Therefore

\`\`\`math
\boxed{
\text{the exterior residual has no nonempty strip of ordinary bilateral Fourier--Laplace convergence}.
}
\`\`\`

This corrects the schematic real-axis transform language in RPB-38.

Unconditionally, the natural transform is the pair

\`\`\`math
(\mathcal C_-,\mathcal C_+),
\`\`\`

not one ordinary Fourier transform on \(\mathbb R\).

This is the half-strip Carleman separation.

---

## 5. Suzuki's one-sided transform

Suzuki's exact one-sided identity is

\`\`\`math
\int_0^\infty
\Psi(t)e^{izt}\,dt
=
-
\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right),
\qquad
\Im z>\frac12.
\`\`\`

Since \(g=-\Psi\),

\`\`\`math
\boxed{
G_+(z)
:=
\int_0^\infty
g(t)e^{izt}\,dt
=
\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right).
}
\`\`\`

By evenness,

\`\`\`math
G_-(z)
:=
\int_{-\infty}^{0}
g(t)e^{izt}\,dt
=
G_+(-z)
=
\frac1{z^2}
\frac{\xi'}{\xi}
\left(
\frac12+iz
\right)
\`\`\`

for

\`\`\`math
\Im z<-\frac12.
\`\`\`

### External source

Suzuki, Theorem 1.1(1), with \(g=-\Psi\).

---

## 6. Exact right-tail factorization

Define the compact-source entire transform

\`\`\`math
\boxed{
V(z)
=
\int_{-c}^{c}
u(y)e^{izy}\,dy.
}
\`\`\`

For \(\Im z>1/2\), Fubini is justified by Section 2, and

\`\`\`math
\begin{aligned}
\int_a^\infty
F_u(x)e^{izx}\,dx
&=
\int_{-c}^{c}
u(y)e^{izy}
\left[
\int_{a-y}^{\infty}
g(t)e^{izt}\,dt
\right]dy
\\
&=
V(z)G_+(z)
-
E_+(z),
\end{aligned}
\`\`\`

where

\`\`\`math
\boxed{
E_+(z)
=
\int_{-c}^{c}
u(y)e^{izy}
\left[
\int_0^{a-y}
g(t)e^{izt}\,dt
\right]dy.
}
\`\`\`

Because both integrations in \(E_+\) are over compact sets,

\`\`\`math
\boxed{
E_+
\text{ is entire}.
}
\`\`\`

Also

\`\`\`math
\int_a^\infty
e^{izx}\,dx
=
-
\frac{e^{iaz}}{iz}.
\`\`\`

Hence

\`\`\`math
\boxed{
\mathcal C_+(z)
=
\frac{V(z)}{z^2}
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right)
-
E_+(z)
+
\frac{C e^{iaz}}{iz},
\qquad
\Im z>\frac12.
}
\`\`\`

This is an exact tail factorization.

---

## 7. Exact left-tail factorization

Reflecting \(x\mapsto-x\) and using evenness of \(g\) gives the analogous
formula

\`\`\`math
\boxed{
\mathcal C_-(z)
=
\frac{V(z)}{z^2}
\frac{\xi'}{\xi}
\left(
\frac12+iz
\right)
-
E_-(z)
-
\frac{C e^{-iaz}}{iz},
\qquad
\Im z<-\frac12,
}
\`\`\`

where \(E_-\) is entire.

The exact form of \(E_-\) is the reflected finite-interval correction.

Its only structural properties needed below are:

1. it is entire;
2. it carries no zeta-divisor poles.

---

## 8. Meromorphic continuation crosses the full zeta divisor

The right formula continues meromorphically from

\`\`\`math
\Im z>\frac12
\`\`\`

to the complex plane through

\`\`\`math
\frac{\xi'}{\xi}
\left(
\frac12-iz
\right).
\`\`\`

Its possible divisor poles occur at

\`\`\`math
\boxed{
z_\rho
=
i\left(
\rho-\frac12
\right),
}
\`\`\`

where \(\rho\) is a nontrivial zero of \(\xi\).

Since

\`\`\`math
0<\Re\rho<1,
\`\`\`

all such poles satisfy

\`\`\`math
-\frac12
<
\Im z_\rho
<
\frac12.
\`\`\`

Thus precisely the strip separating the two original Carleman domains contains
the zeta divisor.

For a critical-line zero

\`\`\`math
\rho
=
\frac12+i\gamma,
\`\`\`

the corresponding \(z_\rho\) is real, up to the fixed sign convention:

\`\`\`math
z_\rho=-\gamma.
\`\`\`

The left continuation carries the reflected divisor.

---

## 9. The compact source does not cancel the critical divisor

At a simple zero \(\rho\), the finite-interval correction \(E_+\) is
holomorphic.

Therefore the residue of the right continuation can vanish only if the source
factor vanishes at the corresponding point:

\`\`\`math
V(z_\rho)=0.
\`\`\`

But RPB-38 proved that for a nonzero compact source, its entire transform can
vanish at only

\`\`\`math
O(T)
\`\`\`

points up to height \(T\), whereas Conrey supplies

\`\`\`math
\gg T\log T
\`\`\`

distinct simple critical-line zeta ordinates.

Hence

\`\`\`math
\boxed{
\mathcal C_+^{\rm mer}
\text{ has }
\gg T\log T
\text{ uncancelled simple real-axis poles up to }|z|\le T.
}
\`\`\`

The same conclusion holds for the left continuation.

Thus the divisor-bearing continuation is genuine.

---

## 10. Exact divisor-cleared numerator

Multiply the right-tail identity by

\`\`\`math
z^2
\xi\left(
\frac12-iz
\right).
\`\`\`

Define

\`\`\`math
\boxed{
N_+(z)
:=
z^2
\xi\left(
\frac12-iz
\right)
\mathcal C_+^{\rm mer}(z).
}
\`\`\`

Then

\`\`\`math
\boxed{
\begin{aligned}
N_+(z)
={}&
V(z)
\xi'\left(
\frac12-iz
\right)
\\
&-
z^2
\xi\left(
\frac12-iz
\right)
E_+(z)
\\
&+
\frac{Cz}{i}
e^{iaz}
\xi\left(
\frac12-iz
\right).
\end{aligned}
}
\`\`\`

Every term on the right is entire.

Therefore

\`\`\`math
\boxed{
N_+
\text{ is entire}.
}
\`\`\`

Similarly,

\`\`\`math
N_-(z)
=
z^2
\xi\left(
\frac12+iz
\right)
\mathcal C_-^{\rm mer}(z)
\`\`\`

is entire.

These are the divisor-cleared Carleman numerators.

---

## 11. Values at simple zeros retain source custody

Let \(\rho\) be a simple zero and put

\`\`\`math
z_\rho
=
i\left(
\rho-\frac12
\right).
\`\`\`

Because

\`\`\`math
\xi(\rho)=0,
\`\`\`

the entire correction terms in \(N_+\) carrying an explicit factor
\(\xi(\rho)\) vanish.

Thus

\`\`\`math
\boxed{
N_+(z_\rho)
=
V(z_\rho)\xi'(\rho).
}
\`\`\`

For a simple zero,

\`\`\`math
\xi'(\rho)\ne0.
\`\`\`

Hence

\`\`\`math
\boxed{
N_+(z_\rho)\ne0
\iff
V(z_\rho)\ne0.
}
\`\`\`

RPB-38 therefore implies that \(N_+\) is nonzero at
\(\gg T\log T\) simple critical divisor points.

This is an exact source-custody statement in the divisor-cleared numerator.

---

## 12. Why an ordinary Wiener--Hopf index is not available

The classical scalar Wiener--Hopf setup expects a boundary symbol on one
common contour, usually the real axis, together with upper/lower analytic
factors having compatible boundary values there.

Here that architecture fails twice.

### No common native boundary

The native tail transforms live only in

\`\`\`math
\Im z>\frac12
\`\`\`

and

\`\`\`math
\Im z<-\frac12.
\`\`\`

There is no common convergence strip reaching the real axis.

### The continuation has infinitely many contour poles

Meromorphic continuation across the intervening strip encounters the zeta
divisor.

By Section 9, a nonzero compact source leaves
\(\gg T\log T\) simple critical poles on the real axis.

Therefore the continued transform is not a nonvanishing continuous boundary
symbol on \(\mathbb R\).

Consequently

\`\`\`math
\boxed{
\text{the conventional finite winding-number Wiener--Hopf index is not presently defined for this tail factorization}.
}
\`\`\`

One would need a divisor-aware meromorphic factorization instead.

---

## 13. Multiplying by \(\xi\) does not preserve the Hardy class automatically

The divisor-clearing operation is algebraically exact.

But

\`\`\`math
\xi\left(
\frac12-iz
\right)
\`\`\`

is an entire function of order one.

Multiplying a one-sided Hardy/Carleman transform by this factor does not
preserve its original half-plane growth class automatically.

In particular, \(N_+\) is entire, but it is not known from the current data to
be:

- of finite exponential type;
- in a Paley--Wiener class;
- in a Cartwright class;
- a bounded-type function in both half-planes.

Thus the divisor-cleared identity is not yet a Jensen contradiction.

The \(T\log T\) density of zeta data is compatible with an order-one entire
function carrying the growth of \(\xi\).

---

## 14. Relation to the derivative/Weil output tail

RPB-35 gives

\`\`\`math
F_u'
=
-i\,W*h
\`\`\`

in the fixed project convention.

After subtracting the collar constant,

\`\`\`math
R'=F_u'.
\`\`\`

Thus the right/left transforms of the physical exterior Weil output are
obtained from \(\mathcal C_\pm\) by multiplication by \(z\), up to the fixed
Fourier convention and the vanishing boundary value \(R(\pm a)=0\).

Therefore:

1. the same half-strip separation holds;
2. the same zeta divisor appears;
3. the same absence of a conventional Wiener--Hopf contour holds.

Working with the potential residual loses no divisor information and avoids
unnecessary derivative regularity issues.

---

## 15. RPB-39 determination

\`\`\`math
\boxed{
\textbf{RPB-39 — THE EXTERIOR TAILS HAVE DISJOINT CARLEMAN HALF-PLANES, AND THEIR CONTINUATION CARRIES AN UNCANCELLED ZETA DIVISOR.}
}
\`\`\`

Exact positive results:

\`\`\`math
\boxed{
\mathcal C_+
\text{ analytic for }\Im z>\frac12,
\qquad
\mathcal C_-
\text{ analytic for }\Im z<-\frac12,
}
\`\`\`

and

\`\`\`math
\boxed{
N_\pm
=
z^2\xi\!\left(\frac12\mp iz\right)
\mathcal C_\pm^{\rm mer}
\text{ are entire}.
}
\`\`\`

At simple zeta zeros,

\`\`\`math
\boxed{
N_+(z_\rho)
=
V(z_\rho)\xi'(\rho),
}
\`\`\`

so the compact source retains explicit custody of the surviving divisor.

Exact negative result:

\`\`\`math
\boxed{
\text{ordinary real-line finite-index Wiener--Hopf factorization is not available}.
}
\`\`\`

The native half-planes do not overlap, and the meromorphic continuation has
infinitely many uncancelled real-axis zeta poles.

Next cursor:

\`\`\`text
RPB-40 / DIVISOR-CLEARED CARLEMAN NUMERATOR GROWTH TEST
\`\`\`

The next pass should study \(N_\pm\) as entire functions:

1. determine their order/type from the compact correction and \(\xi\);
2. test whether the collar hypothesis forces additional cancellation in
   \(N_\pm\);
3. ask whether \(N_\pm\) lies in a Cartwright/de Branges class after a lawful
   normalization;
4. determine whether the values
   \(N_+(z_\rho)=V(z_\rho)\xi'(\rho)\)
   create an interpolation-density contradiction or are fully compatible with
   the inherited order-one \(\xi\) growth.
