# SZ-KERNEL-EDGE-GERM-26 — Full Suzuki archimedean diagonal no-go

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-25  
**Target tested:** FULL ARCHIMEDEAN REMAINDER TEST  
**Public promotion:** forbidden

## 0. Objective

GERM-25 constructed a nonzero even local source whose centered field for the
principal kernel

\[
\frac12|t|\log|t|
\]

is superflat.

That pass deliberately left open whether the exact lower-order Suzuki
archimedean terms restore rigidity.

This pass answers that question.

They do not.

The one-sided full-Suzuki Stieltjes counterconstruction from GERM-20 extends
to every local radius

\[
\rho>0.
\]

If \(b\) is such a one-sided source and \(b_e\) is its even reflection, then
the complete centered archimedean field

\[
\int_0^\rho
\left[
a_\infty(t+\delta)
+
a_\infty(|t-\delta|)
-
2a_\infty(t)
\right]b(t)\,dt
\]

is \(C^\infty\)-flat at \(\delta=0\), even though

\[
b\ne0.
\]

Thus:

\[
\boxed{
\text{full Suzuki archimedean diagonal}
+
\text{nonzero even source}
\not\Rightarrow
\text{finite-order rigidity}.
}
\]

The lower-order exact archimedean remainder does not rescue the
quasi-analyticity route.

This is a stronger local no-go than GERM-25.

The remaining possible rigidity must use coupling to the **prime translation
channels or global kernel custody**, not the archimedean diagonal in
isolation.

---

# I. Exact one-sided full-Suzuki transform at arbitrary radius

## 1. Local interval

Fix

\[
\rho>0.
\]

For

\[
b\in L^2(0,\rho),
\]

define the one-sided full archimedean transform

\[
\boxed{
(\mathscr T_\rho b)(\eta)
=
\int_0^\rho
a_\infty''(\eta+r)b(r)\,dr,
\qquad
\eta>0.
}
\]

Suzuki's exact positive-axis formula is

\[
\boxed{
a_\infty''(t)
=
-e^{t/2}
+
\frac{e^{-5t/2}}{1-e^{-2t}}
=
-e^{t/2}
+
\sum_{m=1}^{\infty}
e^{-(2m+1/2)t}.
}
\]

---

# II. General-radius Stieltjes normal form

## 2. Exponential coordinates

Set

\[
z=e^{-2\eta},
\qquad
x=e^{-2r}.
\]

Then

\[
x\in[x_\rho,1),
\qquad
x_\rho=e^{-2\rho}.
\]

Write

\[
\widetilde b(x)
=
b\left(-\frac12\log x\right).
\]

Exactly as in GERM-18,

\[
\boxed{
(\mathscr T_\rho b)(\eta)
=
-z^{-1/4}A_+(b)
+
\frac12z^{5/4}
\int_{x_\rho}^{1}
\frac{x^{1/4}\widetilde b(x)}
{1-zx}\,dx,
}
\]

where

\[
A_+(b)
=
\int_0^\rho e^{r/2}b(r)\,dr.
\]

---

## 3. Half-line coordinate

Let

\[
s=1-z
\]

and set

\[
\boxed{
t=\frac{x}{1-x}.
}
\]

The lower endpoint becomes

\[
\boxed{
t_\rho
=
\frac{x_\rho}{1-x_\rho}
=
\frac{1}{e^{2\rho}-1}.
}
\]

Define

\[
\nu(t)
=
\frac{x(t)^{1/4}\widetilde b(x(t))}
{1+t}.
\]

Then

\[
\boxed{
z^{1/4}\mathscr T_\rho b
=
-A_+(b)
+
\frac12(1-s)^{3/2}
\int_{t_\rho}^{\infty}
\frac{\nu(t)}
{1+st}\,dt.
}
\]

Thus every local radius gives the same Stieltjes species, with only the finite
lower support endpoint \(t_\rho\) changed.

---

# III. Momentless half-line sources at arbitrary lower endpoint

## 4. Base Mellin family

Use the GERM-20 inverse-Mellin functions

\[
\mu_0,\mu_1
\]

on \((0,\infty)\) with:

\[
\int_0^\infty
y^k\mu_j(y)\,dy=0
\qquad
(k\ge0),
\]

and with smooth flat behavior at \(0\) and rapid decay at \(+\infty\).

Shift them to the exact support endpoint:

\[
\boxed{
\nu_j(t)
=
\begin{cases}
\mu_j(t-t_\rho), & t>t_\rho,\\
0, & t\le t_\rho.
\end{cases}
}
\]

Then each \(\nu_j\) is smooth on the half-line, flat at \(t_\rho\), rapidly
decreasing at infinity, and

\[
\boxed{
\int_{t_\rho}^{\infty}
t^k\nu_j(t)\,dt
=
0
\qquad
\forall k\ge0.
}
\]

---

# IV. Kill the \(A_+\) functional

## 5. One additional linear condition

The inverse coordinate map expresses

\[
A_+(b)
\]

as one continuous linear functional

\[
\boxed{
A_+(b)
=
\int_{t_\rho}^{\infty}
w_\rho(t)\nu(t)\,dt
}
\]

for a fixed smooth weight \(w_\rho\) with polynomial decay at infinity.

The exact displayed formula for \(w_\rho\) is not needed for the dimension
argument; it is obtained by the same elementary Jacobian calculation as in
GERM-20.

On the two-dimensional space

\[
\operatorname{span}\{\nu_0,\nu_1\},
\]

this is one scalar linear functional.

Therefore choose

\[
\boxed{
0\ne\nu
}
\]

in its kernel.

Map \(\nu\) back to a source

\[
\boxed{
0\ne b\in C^\infty(0,\rho)
}
\]

through the inverse Stieltjes coordinate.

Because \(\nu\) is flat at \(t_\rho\) and rapidly decreasing at infinity,
\(b\) extends by zero to a \(C^\infty\) function flat at both endpoints

\[
0,\rho.
\]

In particular,

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

# V. The one-sided exact transform is flat

## 6. Stieltjes jets

Let

\[
\mathcal S_\nu(s)
=
\int_{t_\rho}^{\infty}
\frac{\nu(t)}
{1+st}\,dt.
\]

Rapid decay permits differentiation at

\[
s=0.
\]

For every \(k\ge0\),

\[
\boxed{
\mathcal S_\nu^{(k)}(0)
=
(-1)^kk!
\int_{t_\rho}^{\infty}
t^k\nu(t)\,dt
=
0.
}
\]

Hence

\[
\boxed{
\mathcal S_\nu(s)
=
o(s^N)
\qquad
\forall N.
}
\]

Because

\[
A_+(b)=0,
\]

the exact Stieltjes normal form gives

\[
\boxed{
\mathscr T_\rho b(\eta)
=
o(\eta^N)
\qquad
\forall N.
}
\]

Moreover the construction gives a \(C^\infty\) extension to the boundary
\(\eta=0\) whose every jet vanishes.

---

# VI. Even extension

## 7. Full local source

Extend \(b\) evenly:

\[
\boxed{
b_e(t)
=
\begin{cases}
b(|t|), & |t|<\rho,\\
0, & |t|\ge\rho.
\end{cases}
}
\]

Because \(b\) is flat at both \(0\) and \(\rho\),

\[
\boxed{
b_e\in C_c^\infty(\mathbb R).
}
\]

It is even and nonzero.

---

# VII. Full centered archimedean field

## 8. Convolution form

Let the even extension of Suzuki's archimedean screw component again be
denoted by \(a_\infty\).

Define

\[
\boxed{
H(\delta)
=
(a_\infty*b_e)(\delta).
}
\]

Since \(a_\infty\) is a locally integrable tempered-distribution kernel and

\[
b_e\in C_c^\infty,
\]

the convolution satisfies

\[
\boxed{
H\in C^\infty(\mathbb R).
}
\]

Because both factors are even,

\[
\boxed{
H(-\delta)=H(\delta).
}
\]

The local centered field is

\[
\boxed{
D_b(\delta)
=
H(\delta)-H(0).
}
\]

Explicitly,

\[
D_b(\delta)
=
\int_0^\rho
\left[
a_\infty(t+\delta)
+
a_\infty(|t-\delta|)
-
2a_\infty(t)
\right]
b(t)\,dt.
\]

---

# VIII. Jet transfer from the one-sided transform

## 9. Even derivatives

Because \(b\) is flat at the singular endpoint, differentiation may be
performed distributionally without origin-supported cusp terms surviving.

For every integer

\[
k\ge1,
\]

\[
\boxed{
H^{(2k)}(0)
=
2
\int_0^\rho
a_\infty^{(2k)}(t)b(t)\,dt.
}
\]

On the other hand,

\[
\mathscr T_\rho b(\eta)
=
\int_0^\rho
a_\infty''(\eta+t)b(t)\,dt.
\]

Its boundary derivatives satisfy

\[
\boxed{
(\mathscr T_\rho b)^{(2k-2)}(0)
=
\int_0^\rho
a_\infty^{(2k)}(t)b(t)\,dt.
}
\]

Therefore

\[
\boxed{
H^{(2k)}(0)
=
2
(\mathscr T_\rho b)^{(2k-2)}(0)
=
0.
}
\]

---

## 10. Odd derivatives

Since \(H\) is even,

\[
\boxed{
H^{(2k+1)}(0)=0
\qquad
(k\ge0).
}
\]

Hence every derivative of

\[
D_b=H-H(0)
\]

vanishes at zero.

Thus

\[
\boxed{
D_b^{(k)}(0)=0
\qquad
\forall k\ge0.
}
\]

Because

\[
D_b\in C^\infty,
\]

Taylor's theorem gives

\[
\boxed{
D_b(\delta)
=
o(\delta^N)
\qquad
\forall N.
}
\]

The full exact Suzuki archimedean centered field is superflat.

---

# IX. This defeats the full remainder test

## 11. Exact, not principal-only

Unlike GERM-25, no decomposition

\[
a_\infty
=
\frac12|t|\log|t|
+
\text{remainder}
\]

is used in the final flatness argument.

The counterprofile is built against the exact transform

\[
\boxed{
a_\infty''(t)
=
-e^{t/2}
+
\frac{e^{-5t/2}}{1-e^{-2t}}.
}
\]

Therefore every lower-order archimedean term is already included.

So:

\[
\boxed{
\text{the exact Suzuki archimedean remainder supplies no local
quasi-analytic rescue}.
}
\]

---

# X. Relation to the GERM-24 finite-center branch

## 12. Local model at one selected center

Take one selected movable center \(h\) from GERM-24.

Place the even source \(b_e\) around that center:

\[
f_{\rm loc}(h+t)
=
b_e(t).
\]

Then

\[
\boxed{
\Sigma_{h,\rho}f_{\rm loc}
=
2b
\ne0.
}
\]

Yet the complete local archimedean diagonal channel is superflat.

Thus the implication

\[
\boxed{
\text{nonzero selected even source germ}
\Longrightarrow
\text{finite-order full archimedean diagonal field}
}
\]

is false even for the exact Suzuki kernel.

---

# XI. Scope guard

## 13. Still not an actual Weil kernel vector

The source constructed here is local.

It is not asserted to satisfy the full movable-center identity

\[
\mathscr D_h+\mathscr P_h=0
\]

for all centers, nor the global equation

\[
G_cu=0.
\]

In particular the construction does not enforce:

- prime-shift compatibility at \(h\pm\lambda\);
- ratio-incidence constraints;
- opposite-edge equations;
- collar persistence.

Its role is exact:

\[
\boxed{
\text{the full archimedean diagonal alone cannot provide the missing
finite-order rigidity}.
}
\]

Any successful theorem must use coupled prime/global custody.

---

# XII. Result of this NF pass

For every local radius

\[
\rho>0,
\]

there exists a nonzero smooth endpoint-flat source

\[
\boxed{
0\ne b\in C^\infty(0,\rho)
}
\]

such that its exact one-sided Suzuki transform

\[
\mathscr T_\rho b
\]

is \(C^\infty\)-flat at the boundary.

After even reflection, the exact centered field

\[
\boxed{
D_b(\delta)
=
\int_0^\rho
\left[
a_\infty(t+\delta)
+
a_\infty(|t-\delta|)
-
2a_\infty(t)
\right]
b(t)\,dt
}
\]

satisfies

\[
\boxed{
D_b(\delta)
=
o(\delta^N)
\qquad
\forall N,
}
\]

while

\[
b\ne0.
\]

Therefore:

\[
\boxed{
\text{FULL SUZUKI ARCHIMEDEAN DIAGONAL}
\not\Rightarrow
\text{LOCAL EDGE RIGIDITY}.
}
\]

The entire local archimedean/quasi-analytic route is now exhausted.

---

# XIII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-27 / PRIME-COUPLED MULTICENTER COMPATIBILITY}.
}
\]

Future progress must use what every local countermodel has omitted:

\[
\boxed{
\text{simultaneous prime-shift compatibility across multiple centers}.
}
\]

A useful next pass should take the finite selected center family from GERM-24
and impose the full vector system

\[
\mathscr D_{h_j}
+
\mathscr P_{h_j}
=
0
\qquad
(j=1,\ldots,M)
\]

on the same finite-dimensional source family.

The target is to determine whether the local full-archimedean flat
counterprofiles can be synchronized with the finite prime-tent couplings at
all selected centers.

No prime-coupled multicenter theorem is proved in this pass.

---

# XIV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified full-archimedean local no-go result.

No public promotion and no canonical cursor movement are asserted.
