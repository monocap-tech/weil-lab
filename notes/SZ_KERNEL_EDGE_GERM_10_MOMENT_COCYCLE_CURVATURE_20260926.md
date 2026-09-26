# SZ-KERNEL-EDGE-GERM-10 — Endpoint-moment cocycle and compression curvature

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-9  
**Target tested:** MOMENT-INTERTWINING BOUNDARY COCYCLE  
**Public promotion:** forbidden

## 0. Objective

GERM-9 normalized the remaining obstruction as the moment-intertwining defect

\[
\mathfrak R_\ell
=
\mathcal M A_\ell
-
D_\ell\mathcal M
\]

for the canonical compression of a truncated translation to the orthogonal
edge-obstruction representative.

This pass derives that defect explicitly.

Two distinctions are essential.

First, in the right endpoint coordinate

\[
f_+(s)=u(c-s),
\qquad
0<s<L,\qquad L=2c,
\]

a positive physical translation acts as a **left shift**

\[
f(s)\mapsto f(s+\ell),
\]

so the ideal archimedean moment multiplier is

\[
e^{+\lambda_m\ell},
\qquad
\lambda_m=2m+\frac12.
\]

The decaying multiplier

\[
e^{-\lambda_m\ell}
\]

from GERM-6/7 corresponds to the opposite whole-line translation convention.
There is no contradiction; the orientation must be fixed before forming the
intertwiner.

Second, the raw truncation defect is an honest semigroup cocycle, but the
canonical quotient compression is not a representation of the translation
semigroup.  It carries an explicit curvature term.

The remaining edge problem is therefore:

\[
\boxed{
\text{endpoint-prefix moment cocycle}
+
\text{compression curvature}.
}
\]

---

# I. Endpoint-oriented source model

## 1. Source-coordinate unitary

Let

\[
H=L^2(0,L),
\qquad
L=2c.
\]

For the right edge define the unitary reflection/translation coordinate

\[
(U_+u)(s)
=
u(c-s).
\]

For

\[
u\in L^2(-c,c),
\]

write

\[
f=U_+u.
\]

The physical right boundary

\[
(c-\ell,c)
\]

corresponds exactly to the source prefix

\[
(0,\ell).
\]

---

## 2. Positive physical truncated translation

Let

\[
T_{\ell,c}
=
P_c\tau_\ell E_c
\]

with

\[
(\tau_\ell u)(y)=u(y-\ell).
\]

Transport it to \(H\):

\[
S_\ell
=
U_+T_{\ell,c}U_+^{-1}.
\]

Then

\[
\boxed{
(S_\ell f)(s)
=
\begin{cases}
f(s+\ell), & 0<s<L-\ell,\\
0, & L-\ell<s<L.
\end{cases}
}
\]

Thus positive physical translation is a truncated left shift in right-edge
source coordinates.

The operators satisfy the exact semigroup law

\[
\boxed{
S_\ell S_\mu
=
S_{\ell+\mu}
}
\]

whenever

\[
\ell,\mu>0,
\qquad
\ell+\mu\le L.
\]

---

# II. Exact moment formula

## 3. Archimedean moment lattice

For

\[
m\ge1,
\]

set

\[
\lambda_m=2m+\frac12
\]

and define

\[
\boxed{
M_m(f)
=
\int_0^L
e^{-\lambda_m s}f(s)\,ds.
}
\]

Let

\[
\mathcal M f
=
(M_1(f),M_2(f),\ldots).
\]

---

## 4. Prefix moment vector

For

\[
0<\ell<L,
\]

define

\[
\boxed{
J_{\ell,m}(f)
=
\int_0^\ell
e^{-\lambda_m t}f(t)\,dt
}
\]

and

\[
\mathcal J_\ell f
=
(J_{\ell,1}(f),J_{\ell,2}(f),\ldots).
\]

This is exactly the archimedean moment vector of the discarded physical
boundary strip.

---

## 5. Truncated-shift identity

Directly,

\[
\begin{aligned}
M_m(S_\ell f)
&=
\int_0^{L-\ell}
e^{-\lambda_m s}
f(s+\ell)\,ds\\
&=
e^{\lambda_m\ell}
\int_\ell^L
e^{-\lambda_m t}f(t)\,dt.
\end{aligned}
\]

Hence

\[
\boxed{
M_m(S_\ell f)
=
e^{\lambda_m\ell}
\left(
M_m(f)-J_{\ell,m}(f)
\right).
}
\]

Define the diagonal operator

\[
\boxed{
D_\ell^+
=
\operatorname{diag}
\left(
e^{\lambda_m\ell}
\right)_{m\ge1}.
}
\]

Then

\[
\boxed{
\mathcal M S_\ell
=
D_\ell^+
\left(
\mathcal M-\mathcal J_\ell
\right).
}
\]

Therefore the raw moment-intertwining defect is

\[
\boxed{
\beta_\ell
:=
\mathcal M S_\ell-D_\ell^+\mathcal M
=
-D_\ell^+\mathcal J_\ell.
}
\]

This is an exact formula.

---

# III. The raw defect sees exactly the discarded strip

## 6. Faithfulness of prefix moments

Suppose

\[
\beta_\ell(f)=0.
\]

Since \(D_\ell^+\) is invertible,

\[
\mathcal J_\ell f=0.
\]

Thus

\[
\int_0^\ell
e^{-\lambda_m t}f(t)\,dt
=
0
\qquad
\forall m\ge1.
\]

Apply the same change of variables as in GERM-2,

\[
x=e^{-2t}.
\]

The exponentials become polynomial moments on the compact interval

\[
[e^{-2\ell},1].
\]

Polynomial density gives

\[
f=0
\]

almost everywhere on

\[
(0,\ell).
\]

Conversely, if \(f=0\) there, then \(\beta_\ell(f)=0\).

Therefore

\[
\boxed{
\beta_\ell(f)=0
\iff
f|_{(0,\ell)}=0.
}
\]

The raw moment cocycle is a faithful detector of the discarded boundary
strip.

---

## 7. Finite-dimensional compression of the strip data

If

\[
V\subset H
\]

is finite dimensional, then the restriction image

\[
V|_{(0,\ell)}
\]

is finite dimensional.

Hence finitely many prefix moments

\[
J_{\ell,m_1},\ldots,J_{\ell,m_r}
\]

already separate the nonzero boundary-strip restrictions occurring in \(V\).

Thus the infinite raw defect \(\beta_\ell\) can always be represented by a
finite boundary moment matrix on the edge-obstruction family.

This is an existence statement; no canonical finite subset of indices is
selected.

---

# IV. Raw cocycle law

## 8. Semigroup cocycle

Because

\[
S_{\ell+\mu}=S_\ell S_\mu
\]

and

\[
D_{\ell+\mu}^+
=
D_\ell^+D_\mu^+,
\]

we obtain

\[
\begin{aligned}
\beta_{\ell+\mu}
&=
\mathcal M S_\ell S_\mu
-
D_\ell^+D_\mu^+\mathcal M\\
&=
\left(
\mathcal M S_\ell-D_\ell^+\mathcal M
\right)S_\mu
+
D_\ell^+
\left(
\mathcal M S_\mu-D_\mu^+\mathcal M
\right).
\end{aligned}
\]

Therefore

\[
\boxed{
\beta_{\ell+\mu}
=
\beta_\ell S_\mu
+
D_\ell^+\beta_\mu.
}
\]

This is an honest \(1\)-cocycle identity for the truncated-shift semigroup
with coefficient action \(D_\ell^+\).

---

## 9. Equivalent prefix identity

Using

\[
\beta_\ell=-D_\ell^+\mathcal J_\ell,
\]

the cocycle law is equivalent to

\[
\boxed{
\mathcal J_{\ell+\mu}
=
\mathcal J_\mu
+
(D_\mu^+)^{-1}
\mathcal J_\ell S_\mu.
}
\]

Coordinatewise this is simply the decomposition

\[
\int_0^{\ell+\mu}
=
\int_0^\mu
+
\int_\mu^{\ell+\mu}.
\]

So the cocycle is not formal decoration; it is exactly the nesting law for
discarded boundary strips.

---

# V. Transport the edge quotient into source coordinates

## 10. Canonical representative

Let

\[
P=P_c^+,
\qquad
F=F_\infty,
\qquad
E=F\cap P^\perp.
\]

Transport \(E\) into the right-oriented source space:

\[
\boxed{
E_+
=
U_+E
\subset H.
}
\]

Let

\[
\Pi
\]

be the orthogonal projection of \(H\) onto \(E_+\), and let

\[
Q=I-\Pi.
\]

The canonical compressed shift is

\[
\boxed{
A_\ell
=
\Pi S_\ell|_{E_+}.
}
\]

This is the source-coordinate version of GERM-9's canonical quotient
compression.

---

# VI. Explicit projected intertwining defect

## 11. Definition with the correct orientation

Define

\[
\boxed{
\mathfrak R_\ell
=
\mathcal M A_\ell
-
D_\ell^+\mathcal M|_{E_+}.
}
\]

For

\[
f\in E_+,
\]

we have

\[
A_\ell f
=
S_\ell f-QS_\ell f.
\]

Therefore

\[
\begin{aligned}
\mathfrak R_\ell f
&=
\mathcal M S_\ell f
-
D_\ell^+\mathcal M f
-
\mathcal M Q S_\ell f\\
&=
\beta_\ell f
-
\mathcal M Q S_\ell f.
\end{aligned}
\]

Hence

\[
\boxed{
\mathfrak R_\ell
=
-D_\ell^+\mathcal J_\ell
-
\mathcal M Q S_\ell
\quad
\text{on }E_+.
}
\]

This is the requested explicit formula.

---

# VII. Interpretation

## 12. Two exact pieces

The projected defect has exactly two terms.

### Boundary-prefix defect

\[
-D_\ell^+\mathcal J_\ell.
\]

This is the moment vector of the physical boundary strip discarded by support
truncation.

It is faithful to that strip.

### Projection/ejection defect

\[
-\mathcal M Q S_\ell.
\]

This is the moment vector of the part of the translated source removed by the
canonical projection back onto the edge-obstruction representative.

It contains:

- ejection outside \(F_\infty\);
- persistent mixing;
- and all other directions orthogonal to \(E\).

Thus

\[
\boxed{
\text{arithmetic intertwining}
\iff
\text{projection correction reproduces the boundary-prefix moments exactly}.
}
\]

More explicitly,

\[
\mathfrak R_\ell=0
\]

is equivalent to

\[
\boxed{
\mathcal M Q S_\ell
=
-D_\ell^+\mathcal J_\ell
\quad
\text{on }E_+.
}
\]

That is the exact boundary matching condition.

---

# VIII. A sign/custody warning

## 13. GERM-7 multiplier versus right-edge multiplier

GERM-7 used the whole-line convention

\[
(\tau_\ell f)(s)=f(s-\ell),
\]

for which

\[
M_m(\tau_\ell f)
=
e^{-\lambda_m\ell}M_m(f).
\]

The physical positive translation

\[
u(y)\mapsto u(y-\ell)
\]

becomes, in right endpoint coordinates,

\[
f(s)\mapsto f(s+\ell),
\]

which is the opposite source translation.

Therefore the correct ideal multiplier here is

\[
e^{+\lambda_m\ell}.
\]

The simple-spectrum argument remains available because the values

\[
e^{+\lambda_m\ell}
\]

are still pairwise distinct.

But future moment-custody statements must specify which orientation is being
used.

---

# IX. Compression curvature

## 14. Compressed shifts do not form a semigroup

For

\[
\ell,\mu>0,
\qquad
\ell+\mu\le L,
\]

define

\[
A_\ell=\Pi S_\ell|_{E_+}.
\]

Then

\[
A_\ell A_\mu
=
\Pi S_\ell\Pi S_\mu|_{E_+},
\]

whereas

\[
A_{\ell+\mu}
=
\Pi S_\ell S_\mu|_{E_+}.
\]

Subtracting gives

\[
\boxed{
K_{\ell,\mu}
:=
A_{\ell+\mu}-A_\ell A_\mu
=
\Pi S_\ell Q S_\mu|_{E_+}.
}
\]

This is the **compression curvature**.

It measures the failure of the quotient compression to inherit the
translation semigroup law.

---

## 15. Curved cocycle identity

Start from

\[
\mathfrak R_{\ell+\mu}
=
\mathcal M A_{\ell+\mu}
-
D_{\ell+\mu}^+\mathcal M.
\]

Use

\[
A_{\ell+\mu}
=
A_\ell A_\mu+K_{\ell,\mu}
\]

and

\[
D_{\ell+\mu}^+
=
D_\ell^+D_\mu^+.
\]

Then

\[
\begin{aligned}
\mathfrak R_{\ell+\mu}
&=
\mathcal M A_\ell A_\mu
+
\mathcal M K_{\ell,\mu}
-
D_\ell^+D_\mu^+\mathcal M\\
&=
\left(
D_\ell^+\mathcal M+\mathfrak R_\ell
\right)A_\mu
+
\mathcal M K_{\ell,\mu}
-
D_\ell^+D_\mu^+\mathcal M.
\end{aligned}
\]

Since

\[
\mathcal M A_\mu
=
D_\mu^+\mathcal M+\mathfrak R_\mu,
\]

we obtain

\[
\boxed{
\mathfrak R_{\ell+\mu}
=
D_\ell^+\mathfrak R_\mu
+
\mathfrak R_\ell A_\mu
+
\mathcal M K_{\ell,\mu}.
}
\]

Thus \(\mathfrak R\) is not an ordinary cocycle unless

\[
K_{\ell,\mu}=0.
\]

The extra term is precisely the curvature caused by quotient projection.

---

# X. Flatness of the curvature condition

## 16. When curvature vanishes

We have

\[
K_{\ell,\mu}=0
\]

if and only if

\[
\Pi S_\ell Q S_\mu f=0
\qquad
\forall f\in E_+.
\]

A sufficient condition is

\[
Q S_\mu(E_+)
\]

being mapped by \(S_\ell\) into \(E_+^\perp\).

Raw invariance

\[
S_\mu(E_+)\subseteq E_+
\]

would also imply zero curvature, but GERM-8 rules out such invariance for
small translations on a nonzero kernel obstruction.

Therefore any vanishing curvature on a nonzero obstruction would have to be a
more delicate orthogonality phenomenon, not ordinary invariance.

---

# XI. No automatic low-rank simplification

## 17. Finite rank is vacuous here

Because \(E_+\) is finite dimensional, all operators

\[
\mathfrak R_\ell,
\qquad
K_{\ell,\mu}
\]

are finite rank.

This alone provides no useful smallness.

Likewise, GERM-3 showed that sufficiently rich one-sided boundary data can
already determine the full kernel.

So there is no reason to expect the boundary-prefix term to be rank-small
merely because it is supported in a strip.

The useful property must be algebraic—triangularity, cocycle triviality, or
spectral incompatibility—not generic finite rank.

---

# XII. Exact closure criteria

## 18. Flat intertwining criterion

If for some

\[
\ell>0
\]

the projected defect vanishes,

\[
\mathfrak R_\ell=0,
\]

then

\[
\boxed{
\mathcal M A_\ell
=
D_\ell^+\mathcal M.
}
\]

If \(\mathcal M\) is injective on \(E_+\), the finite-dimensional moment image

\[
\mathcal M(E_+)
\]

is invariant under the simple diagonal operator \(D_\ell^+\).

The same minimal-polynomial argument as GERM-7 then forces

\[
E_+=0.
\]

Therefore

\[
\boxed{
\mathfrak R_\ell=0
\Longrightarrow
\mathcal E_c=0.
}
\]

---

## 19. Curved-family criterion

More generally, suppose a nonempty set of translations is available such that

\[
\mathfrak R_\ell=0
\]

for each of them.

Then the curved cocycle identity gives

\[
\mathcal M K_{\ell,\mu}=0.
\]

If the moment chart is injective on the range of \(K_{\ell,\mu}\), then

\[
K_{\ell,\mu}=0.
\]

Thus exact intertwining automatically tends to flatten the compression
curvature as well.

This shows that the boundary moment law and the semigroup law are not
independent constraints.

---

# XIII. Result of this NF pass

The "moment-intertwining boundary cocycle" is now explicit.

The raw support-truncation defect is

\[
\boxed{
\beta_\ell
=
-D_\ell^+\mathcal J_\ell,
}
\]

and satisfies the honest cocycle law

\[
\boxed{
\beta_{\ell+\mu}
=
\beta_\ell S_\mu
+
D_\ell^+\beta_\mu.
}
\]

The canonical quotient defect is

\[
\boxed{
\mathfrak R_\ell
=
-D_\ell^+\mathcal J_\ell
-
\mathcal M Q S_\ell.
}
\]

Its failure to satisfy an ordinary cocycle law is measured by

\[
\boxed{
K_{\ell,\mu}
=
\Pi S_\ell Q S_\mu|_{E_+},
}
\]

through

\[
\boxed{
\mathfrak R_{\ell+\mu}
=
D_\ell^+\mathfrak R_\mu
+
\mathfrak R_\ell A_\mu
+
\mathcal M K_{\ell,\mu}.
}
\]

Therefore the remaining edge obstruction is no longer a vague boundary
correction.

It is the exact requirement that canonical quotient projection reproduce the
discarded endpoint-strip moments while controlling the associated compression
curvature.

---

# XIV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-11 / ENDPOINT-MOMENT MATCHING}.
}
\]

The next pass should test the exact identity

\[
\boxed{
\mathcal M Q S_\ell
=
-D_\ell^+\mathcal J_\ell
}
\]

on the stabilized edge family.

Useful subtargets are:

1. decompose \(QS_\ell\) into
   - persistent projection,
   - flat-space ejection,
   - and orthogonal kernel/nonkernel pieces;
2. compare each piece with the finite prefix-moment chart;
3. test whether the endpoint-prefix moments are triangular under nested
   strip widths;
4. determine whether the curvature
   \[
   K_{\ell,\mu}
   \]
   has a nonzero finite-order component that prevents exact matching;
5. or prove that exact matching for even one nonzero \(\ell\) is impossible
   unless \(\mathcal E_c=0\).

No endpoint-moment matching theorem is proved in this pass.

---

# XV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified cocycle/curvature structural result.

No public promotion and no canonical cursor movement are asserted.
