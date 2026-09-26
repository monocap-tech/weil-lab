# SZ-KERNEL-EDGE-GERM-9 — Corrected-lift no-go and the moment-intertwining defect

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-8  
**Target tested:** PERSISTENT-CORRECTION LIFT  
**Public promotion:** forbidden

## 0. Objective

GERM-8 proved that no nonzero subspace of the regular kernel can be invariant
under a raw truncated translation

\[
T_{\ell,c}=P_c\tau_\ell E_c
\]

for

\[
0<\ell\le\log2.
\]

It therefore proposed a corrected action

\[
\widehat T_{\ell,c}
=
T_{\ell,c}-C_{\ell,c}
\]

that would preserve the stabilized flat space and persistence space.

The present pass audits how much content such a correction actually carries.

The result is a sharp separation.

1. A correction whose range is persistent, or even merely contained in
   \(F_\infty\), cannot repair failure of raw \(F_\infty\)-invariance.
2. If arbitrary corrections are allowed, a corrected lift always exists and
   can realize an arbitrary quotient operator.
3. There is a canonical Hilbert-space compression to the quotient, but its
   arithmetic moment spectrum is no longer controlled.
4. Therefore the only non-tautological remaining datum is the
   **moment-intertwining defect** between the compressed translation and the
   simple arithmetic moment multiplier.

So "construct a corrected lift" is not itself a valid frontier.

The frontier is to prove that the boundary correction obeys a specific
intertwining law.

---

# I. Canonical quotient realization

## 1. Stabilized spaces

Let

\[
P=P_c^+,
\qquad
F=F_\infty.
\]

Both are finite-dimensional subspaces of the regular kernel

\[
K_c
\]

and

\[
P\subseteq F.
\]

The canonical obstruction is

\[
\mathcal E_c=F/P.
\]

Use the ambient \(L^2(-c,c)\) metric and define the canonical orthogonal
representative

\[
\boxed{
E
=
F\cap P^\perp.
}
\]

Then

\[
\boxed{
F=P\oplus^\perp E,
}
\]

and \(E\) is canonically isometric to \(\mathcal E_c\).

Let

\[
\Pi_P,\Pi_E,\Pi_F
\]

denote the corresponding orthogonal projections.

---

# II. Persistent-valued corrections cannot work

## 2. Basic algebraic obstruction

Let

\[
T=T_{\ell,c}
\]

with

\[
0<\ell\le\log2.
\]

Suppose

\[
C:F\to P.
\]

If the corrected operator

\[
\widehat T=T-C
\]

satisfies

\[
\widehat T(F)\subseteq F,
\]

then for every \(u\in F\),

\[
Tu
=
\widehat Tu+Cu.
\]

Both terms on the right lie in \(F\).

Therefore

\[
\boxed{
T(F)\subseteq F.
}
\]

GERM-8 then forces

\[
F=\{0\}.
\]

Hence:

\[
\boxed{
\operatorname{Ran}C\subseteq P
\text{ and }
(T-C)F\subseteq F
\Longrightarrow
F=0.
}
\]

So a genuinely nonzero flat obstruction cannot be repaired by subtracting a
persistent-valued correction.

---

## 3. Stronger range statement

The same proof uses only

\[
\operatorname{Ran}C\subseteq F.
\]

Thus

\[
\boxed{
\operatorname{Ran}C\subseteq F
\text{ and }
(T-C)F\subseteq F
\Longrightarrow
F=0.
}
\]

Therefore any correction that restores \(F\)-invariance for a nonzero flat
space must itself have a component **outside** \(F\).

That outside component is forced to cancel the ejection

\[
(I-\Pi_F)Tu.
\]

So the phrase "persistent correction" from GERM-8 was too strong.

A nontrivial lift requires a boundary/ejection correction first; persistence
can only enter after that component has been cancelled.

---

# III. Mandatory ejection correction

## 4. The unique outside-\(F\) component

Suppose

\[
\widehat T=T-C
\]

satisfies

\[
\widehat T(F)\subseteq F.
\]

Apply

\[
I-\Pi_F.
\]

For \(u\in F\),

\[
0
=
(I-\Pi_F)\widehat Tu
=
(I-\Pi_F)Tu
-
(I-\Pi_F)Cu.
\]

Therefore necessarily

\[
\boxed{
(I-\Pi_F)Cu
=
(I-\Pi_F)Tu.
}
\]

So every admissible correction has the same outside-\(F\) component.

Define the canonical ejection defect

\[
\boxed{
C_{\rm out}
=
(I-\Pi_F)T|_F.
}
\]

Any corrected lift must contain \(C_{\rm out}\).

The remaining freedom is entirely \(F\)-valued.

---

# IV. Canonical block compression

## 5. A canonical corrected operator

There is a canonical way to obtain an operator preserving both stabilized
blocks.

Define

\[
\boxed{
\widehat T^{\rm can}
=
\Pi_P T\Pi_P
+
\Pi_E T\Pi_E
\quad
\text{on }F.
}
\]

Then

\[
\widehat T^{\rm can}(P)\subseteq P
\]

and

\[
\widehat T^{\rm can}(E)\subseteq E.
\]

Hence it induces the canonical quotient compression

\[
\boxed{
A_\ell
=
\Pi_E T_{\ell,c}|_E
:
E\to E.
}
\]

This exists without any invariance theorem.

---

## 6. Canonical correction formula

On \(F\),

\[
C^{\rm can}
=
T-\widehat T^{\rm can}.
\]

Using

\[
\Pi_F=\Pi_P+\Pi_E,
\]

we obtain

\[
\boxed{
C^{\rm can}
=
(I-\Pi_F)T
+
\Pi_P T\Pi_E
+
\Pi_E T\Pi_P.
}
\]

Thus the canonical correction has three pieces:

1. the mandatory ejection term
   \[
   (I-\Pi_F)T;
   \]
2. \(E\to P\) mixing;
3. \(P\to E\) mixing.

Only after removing all three does one get a block-preserving operator.

This is a canonical Hilbert-space construction, but it is not an arithmetic
theorem.

---

# V. Corrected-lift existence is otherwise tautological

## 7. Arbitrary quotient action can be manufactured

Let

\[
A:E\to E
\]

and

\[
B:P\to P
\]

be arbitrary linear maps.

Define

\[
L_{A,B}
=
B\Pi_P+A\Pi_E
:
F\to F.
\]

Set

\[
\boxed{
C_{A,B}
=
T|_F-L_{A,B}.
}
\]

Then

\[
T-C_{A,B}
=
L_{A,B},
\]

so

\[
(T-C_{A,B})(P)\subseteq P
\]

and

\[
(T-C_{A,B})(F)\subseteq F.
\]

The induced quotient action is exactly

\[
\boxed{
A.
}
\]

Therefore:

\[
\boxed{
\text{without a custody restriction on }C,
\text{ every quotient operator can be produced.}
}
\]

In particular, one can manufacture:

- zero quotient action;
- nilpotent quotient action;
- simple spectrum;
- repeated spectrum;
- any prescribed Jordan form.

So mere existence of a corrected lift contains no edge-rigidity information.

---

# VI. Compression does not preserve nilpotence or arithmetic spectrum

## 8. Finite-dimensional warning

Even if \(T\) is nilpotent, the orthogonal compression

\[
\Pi_E T|_E
\]

need not be nilpotent.

For example, on \(\mathbb C^2\), let

\[
T=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
\]

and let

\[
E=\operatorname{span}\{(1,1)\}.
\]

The compression of \(T\) to \(E\) is multiplication by

\[
\frac12.
\]

Thus a canonical compression can create nonzero spectrum from a nilpotent
ambient operator.

There is therefore no abstract spectral inheritance from the raw truncated
translation to \(A_\ell\).

---

# VII. Moment-intertwining defect

## 9. Separating moment chart

Let

\[
\mathcal M
\]

denote one of the finite archimedean moment charts from GERM-2 on a compact
source interval where it is injective on the relevant finite-dimensional
quotient representative \(E\).

For a whole-line translation by \(\ell\), the expected arithmetic action is

\[
D_\ell
=
\operatorname{diag}
\left(
e^{-(2m+1/2)\ell}
\right)_m.
\]

For a finite von-Mangoldt weighted family \(H\), use instead

\[
D_H
=
\operatorname{diag}
\left(
\alpha_m(H)
\right)_m.
\]

GERM-7 proved that exact invariance under such a diagonal action would force
the finite-dimensional source family to vanish.

---

## 10. Defect of the canonical compression

For the canonical quotient compression

\[
A_\ell=\Pi_E T_{\ell,c}|_E,
\]

define

\[
\boxed{
\mathfrak R_\ell
=
\mathcal M A_\ell
-
D_\ell\mathcal M.
}
\]

This is the **moment-intertwining defect**.

Likewise, for a weighted arithmetic compression \(A_H\),

\[
\boxed{
\mathfrak R_H
=
\mathcal M A_H
-
D_H\mathcal M.
}
\]

If

\[
\mathfrak R_H=0
\]

and \(\mathcal M\) is injective on \(E\), then \(E\) is a
finite-dimensional invariant moment family for the simple diagonal arithmetic
spectrum.

GERM-7 therefore gives

\[
\boxed{
\mathfrak R_H=0
\Longrightarrow
E=0
\Longrightarrow
\mathcal E_c=0.
}
\]

So vanishing of the moment-intertwining defect is a complete sufficient
closure criterion.

---

# VIII. Where the defect comes from

## 11. Decomposition

The defect has two conceptually distinct sources.

First, support truncation changes the raw translation law:

\[
T_{\ell,c}
\ne
\tau_\ell
\]

on the compact carrier.

GERM-7/8 identified this with:

- the boundary-strip commutator on the core zone;
- the shifted old exterior residual on the entry zone.

Second, the quotient compression applies

\[
\Pi_E,
\]

which removes both:

- components outside \(F\);
- persistent \(P\)-components.

Therefore schematically

\[
\boxed{
\mathfrak R_\ell
=
\text{support-boundary moment defect}
+
\text{projection/mixing moment defect}.
}
\]

The corrected-lift problem is precisely the problem of controlling this
operator.

---

# IX. Persistence does not make the defect moment-invisible

## 12. No automatic annihilation

A persistent vector

\[
p\in P
\]

has zero collar edge observation on a stabilized collar.

That does **not** imply that every interior archimedean moment of \(p\)
vanishes.

Indeed, GERM-3's one-sided restriction is injective on the full kernel
\(K_c\), including persistent modes.

So persistent directions generally carry nontrivial interior source data.

Therefore subtracting a persistent component can alter the moment chart:

\[
\boxed{
\mathcal M(p)
\text{ need not vanish for }p\in P.
}
\]

Hence quotienting by persistence does not automatically preserve the
arithmetic diagonal spectrum.

This is the critical custody distinction.

---

# X. Strong no-go for the proposed route

## 13. Exact conclusion

The GERM-8 target asked whether a nontrivial correction could:

1. preserve \(F\);
2. preserve \(P\);
3. retain the arithmetic moment spectrum.

The present pass shows:

- a \(P\)-valued correction cannot repair \(F\)-ejection;
- an arbitrary correction can force any quotient action and is therefore
  vacuous;
- the canonical Hilbert correction exists but does not inherit arithmetic
  spectrum;
- persistent components are not moment-invisible.

Thus

\[
\boxed{
\text{PERSISTENT-CORRECTION LIFT}
\text{ is not a self-closing mechanism.}
}
\]

The only mathematically meaningful remaining statement is an intertwining
theorem for the specific boundary/projection defect.

---

# XI. Result of this NF pass

The corrected-lift problem is now normalized.

There is a canonical quotient representative

\[
E=F_\infty\cap(P_c^+)^\perp
\]

and a canonical compressed translation

\[
\boxed{
A_\ell
=
\Pi_E T_{\ell,c}|_E.
}
\]

But:

\[
\boxed{
\text{corrected lift existence is automatic;}
}
\]

\[
\boxed{
\text{persistent-valued correction is impossible on a nonzero flat space;}
}
\]

and

\[
\boxed{
\text{arithmetic rigidity survives only if }
\mathfrak R_\ell
=
\mathcal M A_\ell-D_\ell\mathcal M
\text{ can be controlled.}
}
\]

Therefore the remaining obstruction has become one explicit finite-dimensional
operator defect.

---

# XII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-10 / MOMENT-INTERTWINING BOUNDARY COCYCLE}.
}
\]

The next pass should derive an explicit formula for

\[
\mathfrak R_\ell
\]

using:

1. the boundary-strip screw potential from GERM-8;
2. the shifted entry residual;
3. the canonical projection onto
   \[
   E=F_\infty\cap(P_c^+)^\perp;
   \]
4. the archimedean exponential moment coordinates from GERM-2.

The target is to determine whether \(\mathfrak R_\ell\) is:

- triangular in the prime-delay ordering;
- lower rank;
- a coboundary in the arithmetic diagonal algebra;
- or necessarily nonzero on every nonzero edge obstruction.

Only a nontrivial structural law for \(\mathfrak R_\ell\) can reactivate the
simple-spectrum rigidity theorem of GERM-7.

No such law is proved in this pass.

---

# XIII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified corrected-lift no-go / normalization residue.

No public promotion and no canonical cursor movement are asserted.
