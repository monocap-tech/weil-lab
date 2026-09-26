# SZ-COMPACT-COLLAR-UNIFORMITY-0 — C3 uniform bounds

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** AUDIT NORMALIZATION / AUXILIARY LEMMA  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Purpose:** discharge audit item C3  
**Depends on:** SZ-ZERO-SIDE-NORMALIZATION-0,
SZ-PRECOND-FORM-BRIDGE-2  
**Traversal movement:** none

## 0. Objective

The residual-square margin pass uses, for one fixed compact right collar

\[
c<b\le A,
\]

two uniform bounds:

\[
\sup_{c<b\le A}\|\sigma_b\|<\infty,
\]

and

\[
\sup_{c<b\le A}\|G_b\|<\infty.
\]

This note proves both with explicit constants.

No support continuity of Douglas maps, no coercivity, and no spectral
continuity are used.

---

## 1. Setup

Fix

\[
0<c<A<\infty.
\]

For \(b\in(c,A]\), let

\[
H_b=L_0^2(-b,b).
\]

Fix one finite selected off-critical packet \(\Pi\).

Let

\[
\Gamma_\Pi
\]

be the finite set of distinct Bombieri ordinates occurring in the packet
after multiplicity-null quotienting, and let

\[
m_\gamma
\]

be the multiplicity of the distinct ordinate \(\gamma\).

The selected negative-coordinate map on the regular screw carrier is

\[
\sigma_b:
H_b\to M_\Pi.
\]

Under C1 normalization it is obtained by:

1. applying \(D_b^{-1}\);
2. evaluating the normalized raw zero coordinates
   \[
   w_\gamma
   =
   \sqrt{m_\gamma}\,
   \widehat{D_b^{-1}u}(\gamma);
   \]
3. applying the unitary conjugate-pair transform;
4. orthogonally projecting to the selected negative coordinates.

Only Step 2 requires an estimate.

---

## 2. Uniform bound for one normalized raw selected coordinate

Take

\[
u\in H_b
\]

and set

\[
v=D_b^{-1}u\in H_0^1(-b,b).
\]

C1 gives

\[
\widehat v(\gamma)
=
\frac1{\gamma}
\int_{-b}^{b}
u(x)e^{i\gamma x}\,dx.
\]

Therefore

\[
w_\gamma(v)
=
\frac{\sqrt{m_\gamma}}{\gamma}
\int_{-b}^{b}
u(x)e^{i\gamma x}\,dx.
\]

By Cauchy–Schwarz,

\[
\left|
\int_{-b}^{b}
u(x)e^{i\gamma x}\,dx
\right|
\le
\|u\|_2
\left(
\int_{-b}^{b}
|e^{i\gamma x}|^2dx
\right)^{1/2}.
\]

Since

\[
|e^{i\gamma x}|
=
e^{-\operatorname{Im}(\gamma)x}
\le
e^{b|\operatorname{Im}\gamma|}
\le
e^{A|\operatorname{Im}\gamma|},
\]

we obtain

\[
\left(
\int_{-b}^{b}
|e^{i\gamma x}|^2dx
\right)^{1/2}
\le
\sqrt{2b}\,
e^{A|\operatorname{Im}\gamma|}
\le
\sqrt{2A}\,
e^{A|\operatorname{Im}\gamma|}.
\]

Hence

\[
\boxed{
|w_\gamma(D_b^{-1}u)|
\le
C_{\gamma,A}\|u\|_2,
}
\]

where

\[
\boxed{
C_{\gamma,A}
:=
\sqrt{
\frac{2A\,m_\gamma}{|\gamma|^2}
}
\,
e^{A|\operatorname{Im}\gamma|}.
}
\]

Every nontrivial zeta ordinate satisfies \(\gamma\ne0\), so the denominator is
legitimate.

---

## 3. Uniform bound for the finite selected raw block

Let

\[
W_{\Pi,b}u
:=
\left(
w_\gamma(D_b^{-1}u)
\right)_{\gamma\in\Gamma_\Pi}.
\]

Then

\[
\begin{aligned}
\|W_{\Pi,b}u\|_{\ell^2(\Gamma_\Pi)}^2
&=
\sum_{\gamma\in\Gamma_\Pi}
|w_\gamma(D_b^{-1}u)|^2\\
&\le
\left(
\sum_{\gamma\in\Gamma_\Pi}
C_{\gamma,A}^2
\right)
\|u\|_2^2.
\end{aligned}
\]

Define

\[
\boxed{
C_{\Pi,A}^2
:=
\sum_{\gamma\in\Gamma_\Pi}
\frac{2A\,m_\gamma}{|\gamma|^2}
e^{2A|\operatorname{Im}\gamma|}.
}
\]

Since \(\Pi\) is finite,

\[
C_{\Pi,A}<\infty.
\]

Therefore

\[
\boxed{
\|W_{\Pi,b}\|
\le
C_{\Pi,A}
\qquad
(c<b\le A).
}
\]

---

## 4. Pair transform and selected projection do not increase the norm

The analytic conjugate-pair map fixed in C1 is unitary:

\[
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

The map from the full pair-coordinate block to \(M_\Pi\) is an orthogonal
projection onto the selected negative coordinates.

Hence both operations have operator norm one.

Therefore

\[
\boxed{
\|\sigma_b\|
\le
C_{\Pi,A}
\qquad
(c<b\le A).
}
\]

In particular,

\[
\boxed{
\sup_{c<b\le A}
\|\sigma_b\|
\le
C_{\Pi,A}
<
\infty.
}
\]

This is the first C3 bound.

---

## 5. Symmetry-restricted sectors inherit the same bound

Let \(S\) be any symmetry sector covered by C2:

- complex parity;
- real carrier;
- real parity.

The sector-specific selected map is obtained by restricting the physical
domain and projecting/restricting the target to

\[
M_\Pi^S.
\]

Restriction of the domain and orthogonal projection of the target cannot
increase the operator norm.

Thus

\[
\boxed{
\|\sigma_b^S\|
\le
C_{\Pi,A}
}
\]

for the same constant.

So C3 is compatible with the C2 sector correction.

---

## 6. Uniform bound for the screw convolution on a compact support collar

Suzuki's screw function

\[
g:\mathbb R\to\mathbb R
\]

is continuous.

Therefore on the compact interval

\[
[-2A,2A]
\]

it has finite supremum

\[
\boxed{
M_g(A)
:=
\sup_{|t|\le2A}|g(t)|
<
\infty.
}
\]

For \(b\le A\), define the unprojected truncated convolution operator

\[
(\mathcal G_bu)(x)
=
\int_{-b}^{b}
g(x-y)u(y)\,dy,
\qquad
|x|<b.
\]

Its integral kernel is

\[
K_b(x,y)=g(x-y).
\]

For

\[
x,y\in(-b,b),
\]

we have

\[
|x-y|\le2b\le2A,
\]

so

\[
|K_b(x,y)|
\le
M_g(A).
\]

Hence the Hilbert–Schmidt norm satisfies

\[
\begin{aligned}
\|\mathcal G_b\|_{\mathrm{HS}}^2
&=
\int_{-b}^{b}
\int_{-b}^{b}
|g(x-y)|^2\,dx\,dy\\
&\le
(2b)^2M_g(A)^2\\
&\le
(2A)^2M_g(A)^2.
\end{aligned}
\]

Thus

\[
\boxed{
\|\mathcal G_b\|
\le
\|\mathcal G_b\|_{\mathrm{HS}}
\le
2A\,M_g(A).
}
\]

---

## 7. Zero-mean projection does not increase the norm

Suzuki's localized screw operator is

\[
G_b
=
P_b\mathcal G_bP_b
\]

on

\[
H_b=L_0^2(-b,b),
\]

where \(P_b\) is the orthogonal projection onto the zero-mean subspace.

Therefore

\[
\|P_b\|=1
\]

and

\[
\boxed{
\|G_b\|
\le
\|\mathcal G_b\|
\le
2A\,M_g(A).
}
\]

Hence

\[
\boxed{
\sup_{c<b\le A}
\|G_b\|
\le
M_A,
\qquad
M_A:=2A\,M_g(A)<\infty.
}
\]

This is the second C3 bound.

---

## 8. Explicit corrected-residual constant

Let

\[
R_c:
M_\Pi\to H_c
\]

be any fixed bounded right inverse of the old selected-coordinate map,

\[
\sigma_cR_c=I_{M_\Pi}.
\]

For

\[
r_b=G_bJ_{c,b}u
\]

define

\[
d_b
=
r_b
-
J_{c,b}R_c(\sigma_br_b).
\]

Then

\[
\begin{aligned}
\|d_b\|
&\le
\|r_b\|
+
\|R_c\|\,
\|\sigma_br_b\|\\
&\le
\left(
1+\|R_c\|C_{\Pi,A}
\right)
\|r_b\|.
\end{aligned}
\]

Thus with

\[
\boxed{
C_d(A,\Pi,R_c)
:=
1+\|R_c\|C_{\Pi,A},
}
\]

we have

\[
\boxed{
\|d_b\|
\le
C_d(A,\Pi,R_c)\,
\Delta_{c,b}(u)
}
\]

uniformly for

\[
c<b\le A.
\]

---

## 9. Explicit denominator estimate in the residual-square law

Using

\[
q_b(d_b)
=
\langle G_bd_b,d_b\rangle,
\]

Sections 7–8 give

\[
|q_b(d_b)|
\le
M_A
C_d(A,\Pi,R_c)^2
\Delta_{c,b}(u)^2.
\]

Therefore, whenever the finite-margin branch has

\[
q_b(d_b)>0,
\]

the affine-fiber formula gives

\[
\begin{aligned}
\mathfrak m_b(u)
&\ge
\frac{
|q_b(Ju,d_b)|^2
}{
q_b(d_b)
}\\
&=
\frac{
\Delta_{c,b}(u)^4
}{
q_b(d_b)
}\\
&\ge
\frac{
\Delta_{c,b}(u)^2
}{
M_A
C_d(A,\Pi,R_c)^2
}.
\end{aligned}
\]

Thus the constant in SZ-MARGIN-MV-FIRST-ORDER-0 can be taken explicitly as

\[
\boxed{
C_*
=
\frac1{
2A\,M_g(A)
\left(
1+\|R_c\|C_{\Pi,A}
\right)^2
}.
}
\]

If \(q_b(d_b)\le0\), the same-source margin is \(+\infty\), so the lower
bound remains true with the extended-value convention.

Hence

\[
\boxed{
\mathfrak m_b(u)
\ge
C_*
\Delta_{c,b}(u)^2
}
\]

uniformly on the fixed compact collar.

---

## 10. What was not used

The proof does not use:

- norm continuity of \(b\mapsto G_b\);
- continuity of any Douglas reduced solution;
- background admissibility;
- selected-preserving coercivity;
- continuity of \(\lambda_b\);
- positive Sobolev control.

Only the following are needed:

1. finiteness of the selected packet;
2. C1 Fourier/multiplicity normalization;
3. continuity of the screw kernel \(g\);
4. contractivity of the zero-mean projections;
5. one fixed bounded right inverse \(R_c\).

So the uniformity input does not reopen any of the inverse-stability seams
identified earlier.

---

## 11. Audit determination

Audit item C3 is discharged.

The two estimates required by the residual-square margin law are now explicit:

\[
\boxed{
\sup_{c<b\le A}\|\sigma_b\|
\le
C_{\Pi,A}
<\infty,
}
\]

and

\[
\boxed{
\sup_{c<b\le A}\|G_b\|
\le
2A\sup_{|t|\le2A}|g(t)|
<\infty.
}
\]

Therefore the regular-carrier lower law

\[
\boxed{
\mathfrak m_b(u)
\gtrsim_{A,\Pi,R_c}
\Delta_{c,b}(u)^2
}
\]

no longer contains an unproved compact-collar uniformity assumption.

After C3, the only remaining item from the audit list is C4, which is already
classified as an optional/non-load-bearing complex-analysis illustration and
is not required for the bridge or margin package.

**No canonical cursor movement is asserted by this audit-normalization pass.**
