# SZ-KERNEL-EDGE-GERM-24 — Finite-center diagonal filtration and parity reduction

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-23  
**Target tested:** FINITE-CENTER DIAGONAL FILTRATION  
**Public promotion:** forbidden

## 0. Objective

GERM-23 proved that the finite-dimensional ratio-incidence branch

\[
V:=W_\infty^{\rm inc}
\]

is detectable by finitely many reachable arithmetic center neighborhoods, but
that each such movable-center equation introduces a logarithmic diagonal
channel.

This pass applies finite-dimensional flatness filtration directly to those
diagonal channels and audits their exact source custody.

The principal new point is a parity reduction.

At one center \(h\), the local logarithmic diagonal channel depends only on
the **diagonal symmetrization**

\[
\Sigma_{h,\rho}f(t)
=
f(h+t)+f(h-t).
\]

Thus a locally odd germ is exactly invisible to that one centered channel.

However, parity blindness does not survive arbitrary center motion.

When the arithmetic center lattice is dense, the family of diagonal
symmetrizations over reachable centers is jointly injective on
\(L^2(0,L)\).  Hence on the finite-dimensional branch \(V\), finitely many
reachable centers can be chosen whose symmetrizations already separate \(V\).

Therefore the simultaneous superflat diagonal branch cannot be explained by
pure local oddness at every selected center.

Any nonzero survivor must carry a genuinely nonzero **even** local germ at at
least one selected center while its logarithmic-diagonal field is still
superflat there.

This isolates the true remaining issue as local non-quasi-analyticity of the
even logarithmic-diagonal carrier.

---

# I. Movable-center archimedean channel

## 1. Source coordinates

Work on

\[
H=L^2(0,L),
\qquad
L=2c.
\]

For an interior source center

\[
h\in(0,L)
\]

and

\[
0<\delta<\min(h,L-h),
\]

define the centered archimedean channel

\[
\boxed{
(\mathscr D_h(\delta)f)
=
\int_0^L
\Delta_\delta^2 a_\infty(h-s)\,
f(s)\,ds,
}
\]

where

\[
\Delta_\delta^2a_\infty(t)
=
a_\infty(t+\delta)
+
a_\infty(t-\delta)
-
2a_\infty(t).
\]

The even extension of the archimedean screw component is understood.

For a true kernel vector, the full movable-center identity is

\[
\boxed{
\mathscr D_h(\delta)f
+
\mathscr P_h(\delta)f
=
0,
}
\]

where \(\mathscr P_h\) is the finite sum of prime tent channels centered at
\(h\pm\lambda\).

---

# II. Local/far decomposition

## 2. Choose a local radius

Fix

\[
0<\rho<\min(h,L-h).
\]

Split

\[
f
=
f_{\rm loc}
+
f_{\rm far}
\]

using the interval

\[
(h-\rho,h+\rho).
\]

For

\[
0<\delta<\rho/2,
\]

the far kernel argument stays uniformly separated from the diagonal
singularity.

Hence

\[
\boxed{
\mathscr D_h
=
\mathscr D_{h,\rho}^{\rm loc}
+
\mathscr A_{h,\rho}^{\rm far},
}
\]

where

\[
\mathscr A_{h,\rho}^{\rm far}(\delta)f
\]

is real analytic in \(\delta\) near \(0\).

All nonanalytic diagonal behavior is contained in
\(\mathscr D_{h,\rho}^{\rm loc}\).

---

# III. Exact diagonal symmetrization

## 3. Local coordinate

Set

\[
s=h+t.
\]

Because

\[
\Delta_\delta^2a_\infty(t)
\]

is even in \(t\), the local channel satisfies

\[
\begin{aligned}
\mathscr D_{h,\rho}^{\rm loc}(\delta)f
&=
\int_{-\rho}^{\rho}
\Delta_\delta^2a_\infty(t)\,
f(h+t)\,dt\\
&=
\int_0^\rho
\Delta_\delta^2a_\infty(t)
\left[
f(h+t)+f(h-t)
\right]dt.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathscr D_{h,\rho}^{\rm loc}(\delta)f
=
\int_0^\rho
\Delta_\delta^2a_\infty(t)\,
(\Sigma_{h,\rho}f)(t)\,dt.
}
\]

So the local diagonal channel depends only on the diagonal symmetrization.

---

# IV. Exact parity kernel

## 4. Local oddness

If

\[
f(h+t)=-f(h-t)
\]

for almost every

\[
0<t<\rho,
\]

then

\[
\boxed{
\Sigma_{h,\rho}f=0
}
\]

and consequently

\[
\boxed{
\mathscr D_{h,\rho}^{\rm loc}(\delta)f=0
}
\]

for every sufficiently small \(\delta\).

Thus one centered logarithmic-diagonal channel has an exact odd-germ kernel.

This is stronger than superflatness.

It is genuine local blindness.

---

# V. Center motion removes global parity blindness

## 5. Continuum joint injectivity

Consider the family

\[
\left\{
\Sigma_{h,\rho}:
h\in(0,L),\;
0<\rho<\min(h,L-h)
\right\}.
\]

Suppose

\[
f\in L^2(0,L)
\]

lies in the kernel of every such map.

Then for every interior center \(h\),

\[
f(h+t)+f(h-t)=0
\]

for almost every sufficiently small \(t\).

Integrating in \(t\) gives

\[
\int_{h-r}^{h+r}f(s)\,ds=0
\]

for every sufficiently small \(r\).

At almost every Lebesgue point \(h\),

\[
\lim_{r\downarrow0}
\frac1{2r}
\int_{h-r}^{h+r}f(s)\,ds
=
f(h).
\]

Hence

\[
f(h)=0
\]

for almost every \(h\).

Therefore

\[
\boxed{
\bigcap_{h,\rho}
\ker\Sigma_{h,\rho}
=
\{0\}.
}
\]

So a source cannot be locally odd about every center unless it is zero.

---

# VI. Dense reachable centers suffice

## 6. Arithmetic center lattice

Assume the multi-prime regime

\[
L>\log3.
\]

GERM-23 gives a dense arithmetic center lattice

\[
\Gamma_c\cap(0,L).
\]

For a fixed interior compact subinterval and fixed sufficiently small radius,
translation/reflection is strongly continuous in \(L^2\) as the center varies.

Hence if

\[
\Sigma_{h,\rho}f=0
\]

for all reachable \(h\) in a dense subset and all admissible sufficiently
small radii, the same identity extends to every interior center.

Section V then gives

\[
f=0.
\]

Therefore:

\[
\boxed{
\text{reachable-center diagonal symmetrizations are jointly injective}.
}
\]

---

# VII. Finite extraction on the incidence branch

## 7. Finite-dimensionality

Now restrict to

\[
V=W_\infty^{\rm inc}.
\]

Because \(V\) is finite dimensional and the reachable-center symmetrization
family is jointly injective, finitely many maps suffice.

Thus there exist reachable centers

\[
\boxed{
h_1,\ldots,h_M\in\Gamma_c\cap(0,L)
}
\]

and radii

\[
\rho_1,\ldots,\rho_M>0
\]

such that

\[
\boxed{
\Sigma:
V
\to
\bigoplus_{j=1}^{M}
L^2(0,\rho_j),
\qquad
\Sigma f
=
\left(
\Sigma_{h_j,\rho_j}f
\right)_{j=1}^{M},
}
\]

is injective.

Therefore there is a constant

\[
\sigma_V>0
\]

such that

\[
\boxed{
\|\Sigma f\|
\ge
\sigma_V\|f\|
\qquad
(f\in V).
}
\]

This eliminates pure parity as a simultaneous hiding mechanism on \(V\).

---

# VIII. Finite-center diagonal flatness filtration

## 8. Joint diagonal observation

For the selected centers define

\[
\boxed{
\mathcal D_\varepsilon:
V
\to
\bigoplus_{j=1}^{M}
L^2(0,\varepsilon),
}
\]

with

\[
(\mathcal D_\varepsilon f)_j
=
\mathscr D_{h_j}(\cdot)f
\Big|_{(0,\varepsilon)},
\]

for \(\varepsilon\) below all geometric admissibility radii.

---

## 9. Filtration

For

\[
N\ge0,
\]

define

\[
\boxed{
V_N^{\rm diag}
=
\left\{
f\in V:
\|\mathcal D_\varepsilon f\|
=
o(\varepsilon^N)
\right\}.
}
\]

Then

\[
V_{N+1}^{\rm diag}
\subseteq
V_N^{\rm diag}.
\]

Finite dimensionality gives a stabilization index

\[
N_{\rm diag}<\infty
\]

such that

\[
\boxed{
V_\infty^{\rm diag}
:=
\bigcap_N
V_N^{\rm diag}
=
V_{N_{\rm diag}}^{\rm diag}.
}
\]

So every incidence-kernel direction lies in one of two branches:

1. finite-order diagonal visibility at some selected center;
2. simultaneous all-orders diagonal flatness at every selected center.

---

# IX. Uniformity on the hard branch

## 10. Operator-superflat diagonal family

On

\[
V_\infty^{\rm diag},
\]

choose a basis.

Finite-dimensional norm equivalence gives

\[
\boxed{
\|
\mathcal D_\varepsilon
|_{V_\infty^{\rm diag}}
\|
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Thus the selected diagonal channels are uniformly superflat on the stabilized
hard branch.

---

# X. Prime output inherits the same flatness

## 11. Exact kernel equation

Every vector in

\[
V\subseteq K_c
\]

satisfies at each selected center

\[
\mathscr D_{h_j}
+
\mathscr P_{h_j}
=
0.
\]

Therefore on

\[
V_\infty^{\rm diag},
\]

\[
\boxed{
\|
\mathscr P_{h_j}(\cdot)f
\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N,
}
\]

uniformly in \(f\).

So simultaneous diagonal superflatness forces simultaneous superflatness of
the corresponding finite prime-tent combinations.

This creates additional arithmetic constraints, but does not yet separate the
individual shifted germs.

---

# XI. Parity has been removed from the hard branch

## 12. Nonzero even local carrier must survive

Take

\[
0\ne f\in V_\infty^{\rm diag}.
\]

Because

\[
\Sigma:V\to\bigoplus_jL^2(0,\rho_j)
\]

is injective,

\[
\Sigma f\ne0.
\]

Hence for at least one selected center

\[
h_j,
\]

\[
\boxed{
\Sigma_{h_j,\rho_j}f\ne0.
}
\]

But the corresponding diagonal field is superflat:

\[
\boxed{
\mathscr D_{h_j}(\delta)f
=
o(\delta^N)
\quad
\text{in local }L^2
\text{ for every }N.
}
\]

Therefore the surviving branch contains a genuinely nonzero even local source
carrier whose logarithmic-diagonal observation is infinitely flat.

The hard branch is not an artifact of odd parity.

---

# XII. Local singular/far cancellation

## 13. Decompose at the detected center

At the selected center from Section XI,

\[
\mathscr D_{h_j}
=
\mathscr D_{h_j,\rho_j}^{\rm loc}
+
\mathscr A_{h_j,\rho_j}^{\rm far}.
\]

The far term is analytic in the collar variable.

The local term is generated by the nonzero symmetrized source

\[
\Sigma_{h_j,\rho_j}f.
\]

Thus simultaneous diagonal superflatness requires

\[
\boxed{
\text{nonzero local logarithmic singular channel}
+
\text{analytic far channel}
=
\text{superflat}.
}
\]

This is the exact local cancellation that a future rigidity theorem would
need to exclude.

---

# XIII. Why finite-center selection still does not close

## 14. No quasi-analytic theorem for the even local carrier

GERM-5 already showed that:

- all logarithmic regularity orders;
- all finite Sobolev orders;
- even \(C^\infty\) source regularity

do not by themselves imply edge quasi-analyticity.

The present pass removes the exact odd-germ kernel but supplies no new
quantitative derivative-growth law for the nonzero even germ.

Therefore no current theorem implies

\[
\boxed{
\mathscr D_{h_j}
\text{ superflat}
\Longrightarrow
\Sigma_{h_j,\rho_j}f=0.
}
\]

That implication is the remaining local diagonal rigidity statement.

---

# XIV. One-prime-base regime

## 15. Scope when \(L\le\log3\)

If

\[
\log2<L\le\log3,
\]

the arithmetic center lattice is not dense; only the base-\(2\) chain is
active.

The finite-center density argument of Sections VI--VII does not apply.

In that regime the minimal-hinge / one-cell obstruction from
GERM-17--20 remains the sharper description.

Thus GERM-24 is primarily a multi-prime refinement.

---

# XV. Result of this NF pass

The finite-center log-diagonal branch now has a complete finite-dimensional
flatness classification.

On the incidence branch

\[
V=W_\infty^{\rm inc},
\]

one can choose finitely many reachable centers so that their diagonal
symmetrizations are injective:

\[
\boxed{
f\mapsto
\left(
\Sigma_{h_j,\rho_j}f
\right)_{j=1}^{M}
}
\]

has zero kernel.

The selected diagonal channels admit a stabilized flatness subspace

\[
\boxed{
V_\infty^{\rm diag}
=
V_{N_{\rm diag}}^{\rm diag}.
}
\]

Every direction outside this subspace exposes a finite-order logarithmic
diagonal field.

Every nonzero direction inside it has:

\[
\boxed{
\text{a nonzero even local source germ at some selected center}
}
\]

while simultaneously

\[
\boxed{
\text{all selected diagonal fields are superflat}.
}
\]

Thus exact parity blindness has been eliminated.

The only remaining finite-center diagonal obstruction is genuine
non-quasi-analytic flatness of a nonzero even local logarithmic carrier.

---

# XVI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-25 / EVEN-DIAGONAL CAUCHY NORMAL FORM}.
}
\]

The next pass should isolate one selected center with

\[
\Sigma_{h,\rho}f\ne0
\]

and derive the exact Cauchy/Stieltjes normal form of its local even
logarithmic-diagonal channel.

The target is to determine whether the **two-sided centered** logarithmic
singularity has stronger rigidity than the one-sided Stieltjes transforms
already defeated in GERM-20.

A positive result would eliminate

\[
V_\infty^{\rm diag}.
\]

A negative result would show that even after parity removal and finite-center
selection, the logarithmic diagonal admits a local superflat countermodel.

No such even-diagonal normal-form theorem is proved in this pass.

---

# XVII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified finite-center diagonal-filtration / parity-reduction
result.

No public promotion and no canonical cursor movement are asserted.
