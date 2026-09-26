# SZ-KERNEL-EDGE-GERM-3 — One-sided observability and reflection-Schur reconstruction

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-2  
**Target:** REFLECTION-RESONANCE SCHUR SYSTEM  
**Public promotion:** forbidden

## 0. Objective

GERM-2 proved two facts:

1. the Suzuki archimedean kernel supplies a complete exponential moment
   system away from the origin;
2. direct coincidence of right- and left-edge prime singular sites is governed
   by the reflection relation
   \[
   \ell+\ell'=2c.
   \]

The intended next step was to build a finite Schur system on reflected prime
components.

A stronger statement appears first.

For either edge orientation, the full kernel

\[
K_c=\ker G_c
\]

is already determined by:

- one endpoint collar; and
- only the **inward-visible half** of each interior prime hinge.

Thus the outward-blind halves are not independent degrees of freedom at all.
They are reconstructed linearly from the visible one-sided data by the global
first-kind equation.

Reflection resonance then has a precise role:

- at a reflected prime site, the two edge orientations expose opposite halves
  of the same physical neighborhood;
- at an isolated prime site, only one half is directly rough-visible and the
  other half is supplied by a nonlocal Schur reconstruction operator.

The remaining obstruction is therefore not a free blind-germ space.  It is
the regularity and edge behavior of this reconstruction operator on the
finite-dimensional kernel quotient.

---

# I. Right-oriented visible set

## 1. Active interior hinges

Let

\[
L=2c
\]

and define the interior prime-hinge set

\[
\mathscr H_c^\circ
=
\left\{
\ell=\log n:
\Lambda(n)\ne0,\;
0<\ell<L
\right\}.
\]

This set is finite.

Choose

\[
\rho>0
\]

so small that:

1. \(\rho<L\);
2. the intervals
   \[
   (\ell-\rho,\ell+\rho),
   \qquad
   \ell\in\mathscr H_c^\circ,
   \]
   are pairwise disjoint;
3. every such interval lies in \((0,L)\).

If \(\mathscr H_c^\circ=\varnothing\), only the endpoint interval below is
used.

---

## 2. Right-oriented source coordinates

For

\[
u\in K_c,
\]

write

\[
f_+(s)=u(c-s),
\qquad
0<s<L.
\]

The inward first-kind identity is

\[
\boxed{
0
=
\int_0^L
[g(s-\delta)-g(s)]
f_+(s)\,ds
}
\]

for every sufficiently small

\[
0<\delta<\rho.
\]

Define the right-oriented visible source set

\[
\boxed{
W_{+,\rho}^{(s)}
=
(0,\rho)
\cup
\bigcup_{\ell\in\mathscr H_c^\circ}
(\ell,\ell+\rho).
}
\]

It contains:

- the archimedean endpoint side \(s=0\);
- the right side of every interior prime hinge in \(s\)-coordinates.

Recall from GERM-1 that these right-hinge sides are exactly the sides seen by
the inward prime Volterra terms.

---

# II. One-sided observability theorem

## 3. Statement

Suppose

\[
u\in K_c
\]

satisfies

\[
f_+=0
\quad\text{a.e. on }W_{+,\rho}^{(s)}.
\]

Then

\[
\boxed{
u=0.
}
\]

Equivalently, restriction to the one-sided visible set is injective on the
**full** kernel, not merely on the stabilized edge quotient.

---

## 4. Prime part becomes affine

Assume

\[
\operatorname{supp}f_+
\subset
(0,L)\setminus W_{+,\rho}^{(s)}
\]

in the essential-support sense.

Fix one interior hinge

\[
h_\ell(s)=(s-\ell)_+.
\]

For

\[
0<\delta<\rho,
\]

the support of \(f_+\) contains no points in

\[
(\ell,\ell+\rho).
\]

Hence, on the support of \(f_+\),

\[
h_\ell(s-\delta)-h_\ell(s)
=
\begin{cases}
0, & s\le\ell,\\
-\delta, & s\ge\ell+\rho.
\end{cases}
\]

Therefore

\[
\boxed{
\int_0^L
[h_\ell(s-\delta)-h_\ell(s)]
f_+(s)\,ds
=
-\delta
\int_{\ell+\rho}^{L}
f_+(s)\,ds.
}
\]

This is exactly linear in \(\delta\).

If an exact threshold hinge

\[
\ell=L
\]

exists, then

\[
(s-L)_+=0
\]

throughout the old support, so its inward contribution is identically zero.

Summing over all prime powers, the entire prime part of the inward
first-difference identity is affine in \(\delta\).

---

## 5. The support is separated from the archimedean origin

Because

\[
f_+=0
\quad\text{on }(0,\rho),
\]

its support is contained in

\[
[\rho,L].
\]

Thus the source is separated from the only archimedean singular point

\[
s=0.
\]

The GERM-2 archimedean injectivity theorem therefore applies on this compact
support, including disconnected unions of intervals.

The same proof works because after

\[
x=e^{-2s},
\]

polynomials remain dense on the resulting compact subset of \((0,1)\).

---

## 6. Conclusion

The exact inward identity has the form

\[
\mathscr A_{f_+}(\delta)
+
\text{affine function of }\delta
=
0.
\]

Therefore

\[
\mathscr A_{f_+}
\]

is affine near zero.

GERM-2 gives

\[
f_+=0.
\]

Since

\[
f_+(s)=u(c-s),
\]

we conclude

\[
u=0.
\]

Hence

\[
\boxed{
R_{+,\rho}:
K_c
\longrightarrow
L^2(W_{+,\rho}^{(s)}),
\qquad
R_{+,\rho}u=f_+|_{W_{+,\rho}^{(s)}}
}
\]

is injective.

---

# III. Physical-space form

## 7. Visible half-collars

Under

\[
y=c-s,
\]

the endpoint interval

\[
(0,\rho)
\]

becomes

\[
(c-\rho,c).
\]

For a right-edge prime hinge

\[
\ell\in\mathscr H_c^\circ,
\]

the interval

\[
(\ell,\ell+\rho)
\]

becomes

\[
(c-\ell-\rho,c-\ell).
\]

Thus define the physical right-oriented visible set

\[
\boxed{
W_{+,\rho}
=
(c-\rho,c)
\cup
\bigcup_{\ell\in\mathscr H_c^\circ}
(c-\ell-\rho,c-\ell).
}
\]

Then restriction

\[
\boxed{
u\longmapsto u|_{W_{+,\rho}}
}
\]

is injective on \(K_c\).

At each right-edge physical prime site

\[
x_\ell=c-\ell,
\]

the visible half is the **left** half

\[
(x_\ell-\rho,x_\ell).
\]

The right half

\[
(x_\ell,x_\ell+\rho)
\]

is the outward-blind half from GERM-1.

---

# IV. Left-oriented theorem

## 8. Mirror statement

For the left edge,

\[
f_-(s)=u(-c+s).
\]

Define

\[
W_{-,\rho}^{(s)}
=
(0,\rho)
\cup
\bigcup_{\ell\in\mathscr H_c^\circ}
(\ell,\ell+\rho).
\]

The same inward argument gives an injective restriction on \(K_c\).

In physical coordinates,

\[
\boxed{
W_{-,\rho}
=
(-c,-c+\rho)
\cup
\bigcup_{\ell\in\mathscr H_c^\circ}
(-c+\ell,-c+\ell+\rho).
}
\]

At a left-edge physical prime site

\[
x_\ell^-=-c+\ell,
\]

the visible half is the **right** half

\[
(x_\ell^-,x_\ell^-+\rho).
\]

Therefore either edge orientation alone gives a one-sided observation set on
which \(K_c\) is faithfully represented.

---

# V. Quantitative finite-dimensional consequence

## 9. One-sided local mass bound

Since \(K_c\) is finite dimensional and

\[
R_{+,\rho}
\]

is injective, there exists

\[
\eta_{+,\rho}>0
\]

such that

\[
\boxed{
\|u\|_{L^2(W_{+,\rho})}
\ge
\eta_{+,\rho}
\|u\|_{L^2(-c,c)}
\qquad
(u\in K_c).
}
\]

Likewise,

\[
\boxed{
\|u\|_{L^2(W_{-,\rho})}
\ge
\eta_{-,\rho}
\|u\|_2.
}
\]

This is stronger than the earlier two-sided singular-site localization:

- it applies to the full regular zero kernel \(K_c\);
- it uses only one side of each interior prime singularity;
- no superflatness hypothesis is needed.

No uniform lower bound as

\[
\rho\downarrow0
\]

is asserted.

---

# VI. Canonical Schur reconstruction

## 10. Visible image

Let

\[
V_{+,\rho}
=
R_{+,\rho}(K_c)
\subset
L^2(W_{+,\rho}).
\]

Because \(R_{+,\rho}\) is injective,

\[
R_{+,\rho}:
K_c
\to
V_{+,\rho}
\]

is an isomorphism of finite-dimensional Hilbert spaces.

Hence it has a canonical inverse on its image:

\[
\boxed{
J_{+,\rho}
=
R_{+,\rho}^{-1}:
V_{+,\rho}
\to
K_c.
}
\]

No arbitrary complement of \(K_c\) is involved.

---

## 11. Blind and bulk reconstruction

Let

\[
B_{+,\rho}
=
(-c,c)\setminus W_{+,\rho}
\]

up to null boundary sets, and let

\[
Q_{+,\rho}:
K_c
\to
L^2(B_{+,\rho})
\]

be restriction.

Define the Schur reconstruction operator

\[
\boxed{
S_{+,\rho}
=
Q_{+,\rho}J_{+,\rho}:
V_{+,\rho}
\to
L^2(B_{+,\rho}).
}
\]

Then every kernel vector has the exact graph form

\[
\boxed{
u
=
v
\oplus
S_{+,\rho}v,
\qquad
v=R_{+,\rho}u\in V_{+,\rho},
}
\]

under the decomposition

\[
L^2(-c,c)
=
L^2(W_{+,\rho})
\oplus
L^2(B_{+,\rho}).
\]

Thus the blind halves and all analytic bulk data are not independent.

They are finite-dimensional linear reconstructions from the right-oriented
visible data.

An analogous operator

\[
S_{-,\rho}
\]

exists for the left orientation.

---

# VII. Reflection resonance revisited

## 12. Reflected physical sites

Take a right-edge hinge

\[
\ell\in\mathscr H_c^\circ
\]

with physical site

\[
x=c-\ell.
\]

A left-edge hinge

\[
\lambda\in\mathscr H_c^\circ
\]

has the same physical site exactly when

\[
-c+\lambda=c-\ell,
\]

that is,

\[
\boxed{
\lambda=L-\ell.
}
\]

This is the reflection relation from GERM-2.

---

## 13. Reflected pairs expose both halves

At the shared physical site

\[
x=c-\ell=-c+(L-\ell),
\]

the right-oriented visible set contains

\[
(x-\rho,x),
\]

while the left-oriented visible set contains

\[
(x,x+\rho).
\]

Therefore, for a reflected pair,

\[
\boxed{
W_{+,\rho}
\cup
W_{-,\rho}
\text{ contains a full two-sided neighborhood of }x.
}
\]

At a reflection fixed point

\[
\ell=c,
\]

the same conclusion holds at

\[
x=0.
\]

Hence reflected prime sites require no blind-half reconstruction if both edge
orientations are used.

---

## 14. Isolated sites

If

\[
L-\ell
\notin
\mathscr H_c^\circ,
\]

then the right-edge physical site

\[
x=c-\ell
\]

is not a left-edge prime singular site.

The right-oriented observation directly sees only

\[
(x-\rho,x).
\]

The opposite half

\[
(x,x+\rho)
\]

is not exposed as a rough prime-local channel by the left edge.

However, it is not free: it is determined by

\[
S_{+,\rho}
\]

from all right-oriented visible data.

Thus an isolated component is not automatically zero.

Instead,

\[
\boxed{
\text{isolated blind half}
=
\text{nonlocal Schur function of visible data}.
}
\]

This is the precise correction to the naive hope that isolated reflection
components could simply be deleted.

---

# VIII. Schur form of the edge observation

## 15. Reduction to visible data

Let

\[
\Gamma_\delta:
K_c\to\mathbb C^2
\]

be the two-edge mean-corrected observation.

Using

\[
u=J_{+,\rho}v,
\]

define the reduced observation

\[
\boxed{
\widetilde\Gamma_{+,\rho}(\delta)
=
\Gamma_\delta J_{+,\rho}
:
V_{+,\rho}\to\mathbb C^2.
}
\]

Then

\[
\Gamma_\delta u
=
\widetilde\Gamma_{+,\rho}(\delta)
R_{+,\rho}u.
\]

All blind, bulk, and reflected contributions have been absorbed into one
finite-dimensional Schur-reduced observation family on visible one-sided
data.

On the stabilized quotient

\[
\mathcal E_c=F_\infty/P_c^+,
\]

the same construction descends after taking the corresponding quotient image.

---

## 16. What the reduction does not supply

The reconstruction operator

\[
S_{+,\rho}
\]

is bounded because its domain is finite dimensional.

But the current argument gives no explicit formula for it and no edge
regularity as \(\rho\downarrow0\).

In particular, one-sided observability alone does **not** imply that

\[
\widetilde\Gamma_{+,\rho}(\delta)
\]

belongs to a quasi-analytic class in \(\delta\).

An arbitrary finite-dimensional graph reconstruction can still arrange
high-order or infinite-order cancellations between visible and reconstructed
blind data.

Therefore Schur reduction is a custody improvement, not yet a rigidity
theorem.

---

# IX. Relation to the canonical Gramian

## 17. Reduced Gramian

The canonical edge Gramian from QA-3 can be written on the visible image as

\[
\boxed{
\widetilde A_{+,\rho}(\varepsilon)
=
\int_0^\varepsilon
\widetilde\Gamma_{+,\rho}(\delta)^*
\widetilde\Gamma_{+,\rho}(\delta)
\,d\delta.
}
\]

Via the isomorphism

\[
J_{+,\rho},
\]

this is congruent to the original Gramian on the kernel quotient.

Thus no information is lost.

The advantage is structural:

\[
\boxed{
\text{the remaining determinant problem has no independent blind variables}.
}
\]

Every possible flat cancellation is encoded in the Schur reconstruction of
visible data.

---

# X. Result of this NF pass

The reflection-resonance analysis admits a sharper formulation.

For sufficiently small fixed \(\rho\):

\[
\boxed{
R_{+,\rho}:K_c\to L^2(W_{+,\rho})
\text{ is injective},
}
\]

and likewise for the left orientation.

Therefore:

1. endpoint plus inward-visible prime half-collars already determine every
   regular kernel vector;
2. blind prime halves and bulk source data are Schur-reconstructed from that
   visible data;
3. reflected prime pairs expose both physical halves directly when the two
   edge orientations are combined;
4. isolated prime sites retain only a nonlocal reconstructed blind half, not
   an independent blind degree of freedom.

So the remaining obstruction is not a reflection graph with free vertices.

It is a finite-dimensional **graph reconstruction problem**:

\[
\boxed{
\text{visible one-sided germ data}
\overset{J_{\pm,\rho}}{\longmapsto}
\text{full kernel vector}
\overset{\Gamma_\delta}{\longmapsto}
\text{edge observation}.
}
\]

The missing rigidity is now concentrated in the reconstruction map

\[
J_{\pm,\rho}
\]

or equivalently

\[
S_{\pm,\rho}.
\]

---

# XI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-4 / SCHUR RECONSTRUCTION REGULARITY}.
}
\]

The next pass should determine whether the explicit first-kind equation gives
additional structure to

\[
S_{\pm,\rho},
\]

for example:

1. a triangular/Volterra form after ordering the prime hinges;
2. an analytic finite-moment formula on the finite-dimensional kernel image;
3. a contraction or invertibility estimate on sufficiently small half-collars;
4. a finite-order asymptotic for the reduced observation
   \[
   \widetilde\Gamma_{\pm,\rho}(\delta);
   \]
5. or a new no-go showing that arbitrary flat cancellation can survive even
   after one-sided reconstruction.

Any finite-order control of the reduced observation on the nonpersistent
quotient would eliminate the superflat obstruction.

No such regularity is proved in this pass.

---

# XII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified NF structural result.

No public promotion and no canonical cursor movement are asserted.
