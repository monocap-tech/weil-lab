# SZ-KERNEL-EDGE-GERM-20 — Hausdorff-range jet rigidity fails locally

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-19  
**Target tested:** HAUSDORFF-RANGE JET RIGIDITY  
**Public promotion:** forbidden

## 0. Objective

GERM-19 isolated the strongest reflected local branch obtained so far.

For a first-prime blind cell

\[
b\in L^2(0,\log2),
\]

the reflected hard branch satisfies simultaneously:

\[
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N,
\]

and

\[
\|\mathscr Tb\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N,
\]

where

\[
(\mathscr Tb)(\eta)
=
\int_0^{\log2}
a_\infty''(\eta+r)b(r)\,dr.
\]

Equivalently, the associated Hausdorff/Laplace moments are rapidly decreasing
and satisfy the complete boundary jet system.

The previous pass asked whether the additional fact that those coefficients
come from one actual Hausdorff source forces

\[
b=0.
\]

The answer is negative at the level of the **local blind-cell problem**.

There exist nonzero blind-cell sources satisfying both:

1. superflat source mass at the reflected hinge;
2. superflat blind archimedean transform.

The construction respects the exact Stieltjes support interval produced by the
Suzuki change of variables.

Therefore:

\[
\boxed{
\text{Hausdorff/Laplace range}
+
\text{source superflatness}
+
\text{all blind-transform jets zero}
\not\Rightarrow
b=0
}
\]

without additional global first-kind coupling.

This closes the local reflected-rigidity experiment negatively.

---

# I. Exact Stieltjes coordinates

## 1. Recall the GERM-18 normal form

Set

\[
a=\log2,
\qquad
z=e^{-2\eta},
\qquad
x=e^{-2r}.
\]

GERM-18 gives

\[
\boxed{
z^{1/4}\mathscr Tb
=
-A_+(b)
+
\frac12 z^{3/2}
\int_{1/4}^{1}
\frac{x^{1/4}\widetilde b(x)}
{1-zx}\,dx.
}
\]

Here

\[
\widetilde b(x)
=
b\!\left(-\frac12\log x\right).
\]

Let

\[
s=1-z.
\]

Then

\[
s\downarrow0
\]

is the same boundary limit as

\[
\eta\downarrow0.
\]

---

# II. Move the finite Hausdorff interval to a half-line

## 2. Möbius coordinate

Set

\[
\boxed{
t=\frac{x}{1-x}.
}
\]

Since

\[
x\in[1/4,1),
\]

we have

\[
\boxed{
t\in[1/3,\infty).
}
\]

Also,

\[
x=\frac{t}{1+t},
\qquad
dx=\frac{dt}{(1+t)^2},
\]

and

\[
1-zx
=
\frac{1+st}{1+t}.
\]

Define

\[
\boxed{
\nu(t)
=
\frac{
x(t)^{1/4}\widetilde b(x(t))
}{
1+t
}.
}
\]

Then

\[
\boxed{
\int_{1/4}^{1}
\frac{x^{1/4}\widetilde b(x)}
{1-zx}\,dx
=
\int_{1/3}^{\infty}
\frac{\nu(t)}
{1+st}\,dt.
}
\]

Therefore

\[
\boxed{
z^{1/4}\mathscr Tb
=
-A_+(b)
+
\frac12(1-s)^{3/2}
\mathcal S_\nu(s),
}
\]

where

\[
\boxed{
\mathcal S_\nu(s)
=
\int_{1/3}^{\infty}
\frac{\nu(t)}
{1+st}\,dt.
}
\]

This is now a standard Stieltjes transform at the boundary point \(s=0^+\).

---

# III. Source-superflatness becomes rapid half-line decay

## 3. Inverse map

The relation defining \(\nu\) is invertible:

\[
\widetilde b(x)
=
\frac{\nu(t)}{x^{1/4}(1-x)},
\qquad
t=\frac{x}{1-x}.
\]

Since

\[
1-x=\frac1{1+t},
\]

we obtain

\[
\boxed{
b(r(t))
=
\nu(t)
(1+t)^{5/4}t^{-1/4},
}
\]

where

\[
r(t)
=
\frac12\log\left(\frac{1+t}{t}\right).
\]

As

\[
t\to\infty,
\]

\[
r(t)\sim\frac1{2t}.
\]

Therefore any \(\nu\) that decreases faster than every inverse power of \(t\)
produces a source \(b\) that is superflat at

\[
r=0.
\]

More precisely, if \(\nu\) is Schwartz at \(+\infty\), then

\[
\boxed{
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

---

# IV. The \(A_+\) functional in half-line coordinates

## 4. Exact weight

Recall

\[
A_+(b)
=
\int_0^a e^{r/2}b(r)\,dr.
\]

Using

\[
dr
=
-\frac{dt}{2t(1+t)}
\]

and the inverse map above gives

\[
\boxed{
A_+(b)
=
\int_{1/3}^{\infty}
w(t)\nu(t)\,dt,
}
\]

with

\[
\boxed{
w(t)
=
\frac12
(1+t)^{1/2}t^{-3/2}.
}
\]

The weight \(w\) is smooth on

\[
[1/3,\infty)
\]

and behaves like

\[
\frac1{2t}
\]

at infinity.

Thus \(A_+\) is a continuous linear functional on every rapidly decreasing
half-line source class used below.

---

# V. Momentless rapidly decreasing half-line densities

## 5. Mellin construction

We now construct nonzero smooth functions on

\[
(0,\infty)
\]

that:

- are flat at \(0\);
- decrease faster than every power at \(+\infty\);
- have all nonnegative polynomial moments equal to zero.

For \(j=0,1\), define the entire functions

\[
\boxed{
M_j(\sigma)
=
\sigma^j
\sin(\pi\sigma)
e^{\sigma^2}.
}
\]

On every vertical line

\[
\sigma=c+i\tau,
\]

the Gaussian factor contributes

\[
e^{-\tau^2},
\]

while the sine factor grows only exponentially in \(|\tau|\).

Hence

\[
M_j(c+i\tau)
\]

decays rapidly in \(\tau\) on every vertical line.

Define its inverse Mellin transform by

\[
\boxed{
\mu_j(t)
=
\frac1{2\pi i}
\int_{c-i\infty}^{c+i\infty}
M_j(\sigma)t^{-\sigma}\,d\sigma,
\qquad
t>0.
}
\]

Because the integrand is entire and vertically rapidly decreasing, the contour
may be moved to arbitrary real \(c\).

Moving the contour far to the left or right gives:

\[
\boxed{
\mu_j(t)
=
O_N(t^N)
\quad
(t\downarrow0)
}
\]

and

\[
\boxed{
\mu_j(t)
=
O_N(t^{-N})
\quad
(t\to\infty)
}
\]

for every \(N\), with the same property for derivatives.

Thus \(\mu_j\) is smooth, flat at \(0\), and rapidly decreasing at infinity.

---

## 6. Vanishing moments

By Mellin inversion,

\[
\int_0^\infty
t^k\mu_j(t)\,dt
=
M_j(k+1).
\]

But

\[
\sin(\pi(k+1))=0
\]

for every integer

\[
k\ge0.
\]

Therefore

\[
\boxed{
\int_0^\infty
t^k\mu_j(t)\,dt
=
0
\qquad
\forall k\ge0.
}
\]

The two functions are linearly independent because their Mellin transforms

\[
M_0,
\qquad
M_1
\]

are linearly independent.

---

# VI. Shift to the exact Suzuki support

## 7. Translation to \(t\ge1/3\)

Define

\[
\boxed{
\nu_j(t)
=
\begin{cases}
\mu_j(t-1/3), & t>1/3,\\
0, & t\le1/3.
\end{cases}
}
\]

Because \(\mu_j\) is flat at zero, \(\nu_j\) is smooth across

\[
t=1/3.
\]

It is rapidly decreasing at infinity.

For every integer \(k\ge0\),

\[
\begin{aligned}
\int_{1/3}^{\infty}
t^k\nu_j(t)\,dt
&=
\int_0^\infty
(s+1/3)^k\mu_j(s)\,ds\\
&=
\sum_{r=0}^{k}
\binom{k}{r}
(1/3)^{k-r}
\int_0^\infty
s^r\mu_j(s)\,ds\\
&=0.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_{1/3}^{\infty}
t^k\nu_j(t)\,dt
=
0
\qquad
\forall k\ge0.
}
\]

So the exact Suzuki half-line support admits a two-dimensional space of
nonzero rapidly decreasing densities with all polynomial moments zero.

---

# VII. Impose the \(A_+=0\) condition

## 8. One extra linear constraint

Let

\[
V
=
\operatorname{span}\{\nu_0,\nu_1\}.
\]

Every element of \(V\) has all polynomial moments zero.

The functional

\[
\nu
\longmapsto
\int_{1/3}^{\infty}
w(t)\nu(t)\,dt
\]

maps the two-dimensional space \(V\) to \(\mathbb C\).

Therefore its kernel contains a nonzero vector.

Choose

\[
\boxed{
0\ne\nu\in V
}
\]

such that

\[
\boxed{
\int_{1/3}^{\infty}
w(t)\nu(t)\,dt=0.
}
\]

Under the inverse source map, this is exactly

\[
\boxed{
A_+(b)=0.
}
\]

---

# VIII. The Stieltjes transform is \(C^\infty\)-flat

## 9. Boundary derivatives

Because \(\nu\) is rapidly decreasing,

\[
\mathcal S_\nu(s)
=
\int_{1/3}^{\infty}
\frac{\nu(t)}
{1+st}\,dt
\]

extends \(C^\infty\) to

\[
s=0^+.
\]

Differentiating under the integral gives

\[
\boxed{
\mathcal S_\nu^{(k)}(0)
=
(-1)^k k!
\int_{1/3}^{\infty}
t^k\nu(t)\,dt.
}
\]

All polynomial moments vanish.

Hence

\[
\boxed{
\mathcal S_\nu^{(k)}(0)=0
\qquad
\forall k\ge0.
}
\]

Therefore

\[
\boxed{
\mathcal S_\nu(s)
=
o(s^N)
\qquad
\forall N.
}
\]

---

# IX. Map back to a blind source

## 10. Define \(b\)

Use the inverse coordinate map

\[
\boxed{
b(r(t))
=
\nu(t)
(1+t)^{5/4}t^{-1/4}.
}
\]

Because the map is pointwise invertible and

\[
\nu\ne0,
\]

we have

\[
\boxed{
b\ne0.
}
\]

The rapid decay of \(\nu\) gives

\[
b\in L^2(0,a)
\]

and

\[
\boxed{
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Thus \(b\) satisfies the reflected source-mass superflatness condition.

---

# X. The blind transform is also superflat

## 11. Insert the two constraints

Recall

\[
z^{1/4}\mathscr Tb
=
-A_+(b)
+
\frac12(1-s)^{3/2}\mathcal S_\nu(s),
\qquad
s=1-z.
\]

By construction,

\[
A_+(b)=0,
\]

and

\[
\mathcal S_\nu(s)
=
o(s^N)
\qquad
\forall N.
\]

The factors

\[
z^{-1/4},
\qquad
(1-s)^{3/2}
\]

are analytic and nonvanishing near

\[
s=0.
\]

Therefore

\[
\boxed{
\mathscr Tb(\eta)
=
o(\eta^N)
\qquad
\forall N.
}
\]

In particular,

\[
\boxed{
\|\mathscr Tb\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

So the same nonzero \(b\) lies simultaneously in the source-superflat and
transform-superflat classes.

---

# XI. Consequence for the GERM-19 jet system

## 12. All jets vanish automatically

The constructed \(b\) has rapidly decreasing Laplace moments and a
\(C^\infty\)-flat blind transform.

Therefore its moment coefficients satisfy the full GERM-19 jet system

\[
\boxed{
\sum_{m\ge1}
(-\lambda_m)^kA_m
=
\left(\frac12\right)^kA_+
\qquad
(k\ge0).
}
\]

Here

\[
A_+=0,
\]

so

\[
\boxed{
\sum_{m\ge1}
(-\lambda_m)^kA_m
=
0
\qquad
\forall k\ge0.
}
\]

Thus the infinite discrete jet identities do not force the Hausdorff moment
source to vanish.

---

# XII. What has been disproved

## 13. Local rigidity statement

The following proposed local theorem is false:

> If
> \[
> b\in L^2(0,\log2)
> \]
> has superflat source mass at \(0\), and its blind archimedean transform is
> superflat at the same boundary, then \(b=0\).

The construction above gives a counterexample.

Equivalently:

\[
\boxed{
\text{reflected source superflatness}
+
\text{Hausdorff-range membership}
+
\text{all blind-transform jets zero}
}
\]

do not imply local source vanishing.

---

# XIII. Scope guard

## 14. This is not an actual Weil kernel orbit

The constructed \(b\) is a local blind-cell source.

It is **not** asserted to arise from a vector

\[
u\in K_c,
\]

let alone from

\[
u\in F_\infty.
\]

In particular, the construction does not solve the coupled equations on:

- the neighboring visible cells;
- the opposite edge;
- the remaining prime hinges;
- the full old-interior first-kind equation.

Its role is exact and limited:

\[
\boxed{
\text{the local reflected/Hausdorff conditions alone are insufficient}.
}
\]

Therefore any successful closure must use multi-cell or global kernel
compatibility.

---

# XIV. Impact on dyadic-resonant support lengths

## 15. Reflection closure is still not enough locally

GERM-19 showed that when

\[
2c=N\log2,
\]

the full dyadic spine is reflection-closed.

The present pass shows that even at each reflected cell, the strongest local
bilateral conditions admit nonzero abstract source profiles.

Thus:

\[
\boxed{
\text{full dyadic reflection closure}
\not\Rightarrow
\text{cellwise local rigidity}.
}
\]

The exceptional dyadic-resonant support geometry therefore remains open only
through **global compatibility across cells**, not through one-cell
quasi-analyticity.

---

# XV. Result of this NF pass

Hausdorff-range jet rigidity fails at the local cell level.

There exist

\[
\boxed{
0\ne b\in L^2(0,\log2)
}
\]

such that simultaneously

\[
\boxed{
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N,
}
\]

and

\[
\boxed{
\|\mathscr Tb\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

The construction respects the exact Suzuki Stieltjes support geometry and
automatically satisfies the complete discrete moment-jet system.

Therefore the quasi-analyticity barrier survives even after:

- bilateral reflection;
- source-mass superflatness;
- rapid Hausdorff moment decay;
- and all boundary jets.

This is a genuine local no-go.

---

# XVI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-21 / MULTI-CELL FIRST-KIND COMPATIBILITY}.
}
\]

The next pass should stop testing one blind cell in isolation.

It should assemble the finite dyadic/prime cell system imposed by

\[
G_cu=0
\]

simultaneously across:

1. all right-visible and right-blind cells;
2. the left-oriented reflected cells;
3. the finite dyadic escape filtration;
4. the archimedean moment coupling;
5. the nonkernel escape fields.

The target is to determine whether the local momentless/Stieltjes-flat
profiles constructed here can coexist **simultaneously** with the full
finite-delay first-kind system.

A positive incompatibility theorem would finally use information unavailable
to all preceding local countermodels.

No such global compatibility theorem is proved in this pass.

---

# XVII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified local Hausdorff-range no-go result.

No public promotion and no canonical cursor movement are asserted.
