# SZ-KERNEL-EDGE-GERM-6 — Moment-shift rigidity and the recurrence gate

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-5  
**Target tested:** LOCAL QUASI-ANALYTIC MOMENT CONTROL  
**Public promotion:** forbidden

## 0. Objective

GERM-5 showed that qualitative regularity is below the true edge-rigidity
threshold.

Even:

- all logarithmic orders;
- all finite Sobolev orders;
- or \(C^\infty\) regularity

can coexist with a nonzero infinitely-flat Volterra edge germ.

The remaining hope is quantitative control of the explicit archimedean
moments from GERM-2:

\[
M_m(f)
=
\int
e^{-(2m+1/2)s}f(s)\,ds.
\]

This pass isolates the exact algebraic condition that would force rigidity.

The key result is:

\[
\boxed{
\text{any nontrivial constant-coefficient recurrence in the moment index
forces the }L^2\text{ source to vanish.}
}
\]

Equivalently, a nonzero finite-dimensional \(L^2\) source family cannot have a
shift-invariant archimedean moment image.

Thus moment-index shift closure would immediately eliminate the edge
obstruction.

However, the current prime-delay algebra acts **diagonally** on the moment
index rather than by shifts.

So the recurrence gate is not yet closed by the existing Weil structure.

---

# I. Archimedean moment map

## 1. Compact source interval

Let

\[
I=[a,b]\Subset(0,\infty)
\]

and

\[
f\in L^2(I).
\]

For

\[
m\ge1,
\]

define

\[
\boxed{
M_m(f)
=
\int_I
e^{-(2m+1/2)s}f(s)\,ds.
}
\]

GERM-2 proved that the family

\[
\{M_m:m\ge1\}
\]

separates \(L^2(I)\).

For a finite-dimensional subspace

\[
V\subset L^2(I),
\]

finitely many coordinates already separate \(V\).

That is a finite-detection statement.

It is not a recurrence statement.

---

# II. Polynomial recurrence rigidity

## 2. Recurrence hypothesis

Suppose there are complex coefficients

\[
a_0,\ldots,a_r,
\]

not all zero, and an integer

\[
m_0\ge1
\]

such that

\[
\boxed{
\sum_{j=0}^{r}
a_j M_{m+j}(f)
=
0
\qquad
\forall m\ge m_0.
}
\]

Let

\[
P(x)
=
\sum_{j=0}^{r}
a_jx^j.
\]

Then the recurrence is already fatal.

---

## 3. Change of variables

Set

\[
x=e^{-2s}.
\]

Then

\[
J
=
[e^{-2b},e^{-2a}]
\Subset(0,1).
\]

Since

\[
e^{-(2m+1/2)s}
=
x^{m+1/4},
\]

the Jacobian and the fixed fractional power may be absorbed into a
nonvanishing bounded weight.

Thus there exists

\[
h\in L^2(J)
\]

such that

\[
M_m(f)
=
C
\int_J
x^m h(x)\,dx
\]

for a fixed nonzero constant \(C\) depending only on the normalization.

The recurrence becomes

\[
\boxed{
\int_J
x^mP(x)h(x)\,dx
=
0
\qquad
\forall m\ge m_0.
}
\]

---

## 4. Density argument

Because

\[
J\Subset(0,1),
\]

the function

\[
x^{m_0}
\]

is bounded above and bounded away from zero on \(J\).

Therefore

\[
\operatorname{span}
\{x^m:m\ge m_0\}
=
x^{m_0}\operatorname{span}\{1,x,x^2,\ldots\}
\]

is dense in \(C(J)\), hence in \(L^2(J)\).

Consequently

\[
P(x)h(x)=0
\]

for almost every \(x\in J\).

A nonzero polynomial has only finitely many zeros.

Since an \(L^2\) function supported on a finite set is zero almost everywhere,

\[
h=0.
\]

Therefore

\[
f=0.
\]

We have proved:

\[
\boxed{
\text{nontrivial constant-coefficient moment recurrence}
\Longrightarrow
f=0.
}
\]

---

# III. Shift-invariant finite-dimensional moment spaces

## 5. Sequence space

Define the full moment map

\[
\mathcal M:
L^2(I)
\to
\mathbb C^{\mathbb N},
\qquad
\mathcal M(f)
=
(M_1(f),M_2(f),\ldots).
\]

Let

\[
S
\]

be the left shift

\[
S(z_1,z_2,z_3,\ldots)
=
(z_2,z_3,z_4,\ldots).
\]

Take a finite-dimensional source family

\[
V\subset L^2(I).
\]

Suppose

\[
\boxed{
S\mathcal M(V)
\subseteq
\mathcal M(V).
}
\]

Then

\[
W=\mathcal M(V)
\]

is a finite-dimensional \(S\)-invariant sequence space.

---

## 6. Cayley-Hamilton closure

On the finite-dimensional space \(W\), the operator

\[
S|_W
\]

satisfies its characteristic polynomial.

Hence there is a nonzero polynomial

\[
P
\]

such that

\[
P(S)w=0
\qquad
\forall w\in W.
\]

For every

\[
f\in V,
\]

this is a constant-coefficient recurrence in the sequence

\[
M_m(f).
\]

Section II then gives

\[
f=0.
\]

Therefore

\[
\boxed{
S\mathcal M(V)
\subseteq
\mathcal M(V)
\Longrightarrow
V=\{0\}.
}
\]

Equivalently:

\[
\boxed{
\text{no nonzero finite-dimensional }L^2\text{ source family has a
shift-invariant archimedean moment image.}
}
\]

This is the strongest algebraic rigidity obtained so far from the explicit
moment system.

---

# IV. Exact closure criterion for the edge obstruction

## 7. Finite-dimensional obstruction family

Let

\[
E_c
\simeq
\mathcal E_c
\]

be a finite-dimensional representative of the stabilized edge obstruction.

Take any local restriction of the corresponding endpoint-oriented sources to
a compact interval

\[
I\Subset(0,2c)
\]

on which GERM-2's moment system applies.

Let

\[
V_I
=
\{f_u|_I:u\in E_c\}.
\]

Then \(V_I\) is finite dimensional.

If the Weil kernel equation were to imply

\[
\boxed{
S\mathcal M(V_I)
\subseteq
\mathcal M(V_I),
}
\]

the theorem above would force

\[
V_I=0.
\]

If such shift closure held on enough local source intervals to cover the
one-sided visible set of GERM-3, then one-sided observability would give

\[
E_c=0,
\]

hence

\[
\mathcal E_c=0.
\]

Thus moment-shift closure is a sufficient finite-dimensional endpoint
rigidity theorem.

---

# V. Finite moment separation is strictly weaker

## 8. Why GERM-2 does not already imply closure

GERM-2 proved that for finite-dimensional \(V\) there exist finitely many
indices

\[
m_1<\cdots<m_r
\]

such that

\[
f
\longmapsto
(M_{m_1}(f),\ldots,M_{m_r}(f))
\]

is injective.

This gives an injective coordinate chart on \(V\).

But it does not relate

\[
M_{m+1}
\]

to the preceding coordinates uniformly in \(m\).

An arbitrary finite-dimensional family of \(L^2\) functions may have a moment
image that wanders through infinitely many linearly independent coordinate
directions under the shift.

Therefore

\[
\boxed{
\text{finite moment separation}
\not\Rightarrow
\text{moment recurrence}.
}
\]

This is exactly the gap between the current edge package and the recurrence
gate above.

---

# VI. Smooth flat families can have arbitrarily weak moment decay

## 9. Flat positive source family

Let

\[
\alpha>0
\]

and choose a smooth cutoff

\[
\chi\in C_c^\infty([0,\rho))
\]

with

\[
\chi=1
\]

near \(0\).

Define

\[
f_\alpha(s)
=
\chi(s)e^{-1/s^\alpha}
\qquad
(s>0),
\]

with

\[
f_\alpha(0)=0.
\]

Then

\[
f_\alpha\in C_c^\infty([0,\rho))
\]

and is flat at \(s=0\).

Consider

\[
M_m(f_\alpha)
=
\int_0^\rho
e^{-(2m+1/2)s}
e^{-1/s^\alpha}
\chi(s)\,ds.
\]

The exponent is governed by

\[
\Phi_m(s)
=
2ms+s^{-\alpha}.
\]

Its minimum occurs at scale

\[
s_m
\asymp
m^{-1/(\alpha+1)}.
\]

At that point

\[
\Phi_m(s_m)
\asymp
m^{\alpha/(\alpha+1)}.
\]

Standard one-dimensional Laplace estimates therefore give constants

\[
c_1,c_2,C_1,C_2>0
\]

such that for sufficiently large \(m\),

\[
\boxed{
C_1
e^{-c_2m^{\alpha/(\alpha+1)}}
\le
M_m(f_\alpha)
\le
C_2
e^{-c_1m^{\alpha/(\alpha+1)}}.
}
\]

Thus smooth flat sources naturally produce subexponential moment decay.

As

\[
\alpha
\]

varies, the exponent

\[
\frac{\alpha}{\alpha+1}
\]

ranges over all numbers in

\[
(0,1).
\]

So neither finite dimensionality nor \(C^\infty\) regularity provides a
universal exponential or quasi-analytic moment law.

---

# VII. Prime delays do not supply the missing shift

## 10. Laplace transform of a translation

Extend the endpoint-oriented source by zero outside its compact support and
define

\[
\mathcal Lf(z)
=
\int_{\mathbb R}
e^{-zs}f(s)\,ds.
\]

For a translation

\[
(T_\ell f)(s)
=
f(s-\ell),
\]

we have

\[
\boxed{
\mathcal L(T_\ell f)(z)
=
e^{-z\ell}\mathcal Lf(z).
}
\]

At the archimedean lattice

\[
z=\lambda_m=2m+\frac12,
\]

this gives

\[
\boxed{
M_m(T_\ell f)
=
e^{-(2m+1/2)\ell}M_m(f).
}
\]

If

\[
\ell=\log n,
\]

then

\[
\boxed{
M_m(T_{\log n}f)
=
n^{-(2m+1/2)}M_m(f).
}
\]

Thus arithmetic translations act by coordinatewise exponential multipliers in
the moment index.

They do **not** act by

\[
m\mapsto m+1.
\]

---

## 11. Consequence

The finite-delay arithmetic system naturally generates diagonal sequence
operators of the form

\[
D_n:
(z_m)_m
\longmapsto
(n^{-(2m+1/2)}z_m)_m.
\]

The recurrence theorem needs control of the shift operator

\[
S.
\]

There is no current identity converting the family of diagonal operators
\(\{D_n\}\) into shift invariance of the moment image.

Therefore

\[
\boxed{
\text{FINITE PRIME DELAYS}
\not\Rightarrow
\text{MOMENT-SHIFT CLOSURE}
}
\]

from the presently available algebra.

This is a precise no-go, not merely a missing calculation.

---

# VIII. Dilation interpretation

## 12. Multiplicative source coordinate

Under

\[
x=e^{-2s},
\]

translation by

\[
\ell=\log n
\]

becomes dilation:

\[
s\mapsto s+\ell
\qquad\Longleftrightarrow\qquad
x\mapsto n^{-2}x.
\]

Meanwhile moment-index shift corresponds multiplication by \(x\):

\[
M_{m+1}(f)
=
\int
x^{m+1}h(x)\,dx.
\]

So the two relevant actions are:

\[
\boxed{
\text{prime delay}
\leftrightarrow
\text{dilation }x\mapsto n^{-2}x,
}
\]

whereas

\[
\boxed{
\text{moment shift}
\leftrightarrow
\text{multiplication by }x.
}
\]

These are genuinely different operations.

The next useful interface should therefore seek a relation between the
arithmetic dilation algebra and multiplication by \(x\) on the finite kernel
family.

---

# IX. Result of this NF pass

The explicit archimedean moment system now has a sharp rigidity criterion:

\[
\boxed{
\text{moment-index recurrence}
\Longrightarrow
\text{source vanishing}.
}
\]

More strongly,

\[
\boxed{
\text{finite-dimensional shift-invariant moment image}
\Longrightarrow
\text{zero source family}.
}
\]

This gives a clean sufficient route to

\[
\mathcal E_c=0.
\]

But the current Weil arithmetic delays act diagonally/dilationally on the
moment lattice, not by index shift.

Therefore the sought quasi-analytic moment control has been reduced to an
algebraic custody problem:

\[
\boxed{
\text{can the Weil first-kind equation convert arithmetic dilations into
moment-shift closure on the finite edge-defect family?}
}
\]

Nothing currently proves that conversion.

---

# X. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-7 / MOMENT-DILATION CLOSURE}.
}
\]

The next pass should work in the multiplicative coordinate

\[
x=e^{-2s}
\]

and examine the finite-dimensional source family induced by
\(\mathcal E_c\).

The target is to determine whether the first-kind equation forces any
nontrivial relation between:

- multiplication by \(x\);
- the arithmetic dilations
  \[
  x\mapsto n^{-2}x;
  \]
- and the archimedean moment map.

Any polynomial relation that produces a nonzero polynomial in the moment
shift would force the local source family to vanish by the recurrence theorem
above.

No such dilation-to-shift closure is proved in this pass.

---

# XI. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified rigidity-criterion/no-go residue.

No public promotion and no canonical cursor movement are asserted.
