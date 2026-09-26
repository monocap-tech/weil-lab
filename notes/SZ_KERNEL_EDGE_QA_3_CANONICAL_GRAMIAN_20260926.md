# SZ-KERNEL-EDGE-QA-3 — Canonical edge Gramian and determinant

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate canonical support:** SZ-EDGE-PACKAGE-RATIFICATION-20260926  
**Traversal target:** SZ-KERNEL-EDGE-QA / CANONICAL EDGE MATRIX  
**Public promotion:** forbidden

## 0. Objective

The ratified edge package proves that the finite-dimensional obstruction

\[
\mathcal E_c
=
F_\infty/P_c^+
\]

is detected by finitely many arbitrarily small edge samples, but the concrete
sample matrix depends on:

- a complement of \(P_c^+\);
- a basis;
- sample locations;
- the choice of \(+\) or \(-\) edge component.

This pass removes those choices.

The key observation is that the ratified variance identity already supplies a
canonical Hilbert-space observation map.  Its Gram operator is a basis-free
finite-dimensional edge matrix, and its determinant is the canonical average
of the squared determinants of all sampled edge matrices.

The pass does **not** prove

\[
\mathcal E_c=0.
\]

It instead converts the remaining obstruction into a canonical positive
superflat determinant.

---

# I. Stabilized collar and quotient observation

## 1. Choose only the canonical stabilization scale

The persistence spaces

\[
P_\varepsilon
=
\ker(G_{c+\varepsilon}J_\varepsilon)
\subset K_c
\]

stabilize for all sufficiently small \(\varepsilon>0\).

Fix

\[
0<\varepsilon_* 
\]

inside that stabilization regime, so that

\[
P_\varepsilon=P_c^+
\qquad
(0<\varepsilon\le\varepsilon_*).
\]

No basis, complement, or sample location is chosen.

---

## 2. Two-edge observation family

For \(u\in F_\infty\), define

\[
\Gamma_u(\delta)
=
\left(
F_u(c+\delta)-m_u(c+\delta),
F_u(-c-\delta)-m_u(c+\delta)
\right),
\qquad
0<\delta\le\varepsilon_*.
\]

Both \(F_u\) and \(m_u\) depend linearly on \(u\), so

\[
u\longmapsto\Gamma_u(\delta)
\]

is linear.

If

\[
p\in P_c^+,
\]

then \(p\in P_\varepsilon\) throughout the stabilized collar.  Hence its collar
residual vanishes and

\[
\boxed{
\Gamma_p(\delta)=0
\qquad
(0<\delta\le\varepsilon_*).
}
\]

Therefore the edge observation descends canonically to the quotient

\[
\mathcal E_c=F_\infty/P_c^+.
\]

Write

\[
\bar\Gamma_\delta:
\mathcal E_c\to\mathbb C^2,
\qquad
\bar\Gamma_\delta([u])=\Gamma_u(\delta).
\]

This is independent of the representative \(u\).

---

# II. Canonical observation operator

## 3. Integrated collar observation

For

\[
0<\varepsilon\le\varepsilon_*,
\]

let

\[
\mathcal H_\varepsilon
=
L^2((0,\varepsilon);\mathbb C^2)
\]

and define

\[
\boxed{
\mathcal O_\varepsilon:
\mathcal E_c\to\mathcal H_\varepsilon,
\qquad
(\mathcal O_\varepsilon[u])(\delta)
=
\bar\Gamma_\delta([u]).
}
\]

This map is canonical.

It requires no complement and no discrete sample selection.

---

## 4. Exact variance identity on the quotient

The ratified variance-growth identity gives

\[
\Delta_{c,c+\varepsilon}(u)^2
=
\int_0^\varepsilon
\|\Gamma_u(\delta)\|_{\mathbb C^2}^2\,d\delta.
\]

Therefore

\[
\boxed{
\|\mathcal O_\varepsilon[u]\|_{\mathcal H_\varepsilon}^2
=
\Delta_{c,c+\varepsilon}(u)^2.
}
\]

In particular, the collar defect norm is already the norm of a canonical
quotient observation.

---

## 5. Injectivity

Suppose

\[
\mathcal O_\varepsilon[u]=0.
\]

Then

\[
\Gamma_u(\delta)=0
\]

for almost every \(0<\delta<\varepsilon\).

The screw potential and moving mean are continuous in the collar variable, so
\(\Gamma_u\) is continuous.  Hence

\[
\Gamma_u(\delta)=0
\qquad
(0<\delta<\varepsilon).
\]

Thus

\[
\Delta_{c,c+\varepsilon}(u)=0,
\]

so

\[
u\in P_\varepsilon=P_c^+.
\]

Consequently

\[
[u]=0
\]

in \(\mathcal E_c\).

Hence

\[
\boxed{
\mathcal O_\varepsilon
\text{ is injective for every }
0<\varepsilon\le\varepsilon_*.
}
\]

This is the canonical version of finite collar-sample separation.

---

# III. Canonical edge Gramian

## 6. Quotient Hilbert metric

Because \(F_\infty\) and \(P_c^+\) are finite-dimensional subspaces of the
ambient \(L^2(-c,c)\) carrier, the quotient carries its canonical Hilbert
metric

\[
\|[u]\|_{\rm quot}
=
\inf_{p\in P_c^+}
\|u+p\|_{L^2(-c,c)}.
\]

Equivalently, it may be identified isometrically with the \(L^2\)-orthogonal
representative space

\[
F_\infty\cap(P_c^+)^\perp.
\]

This orthogonal representative is canonical once the ambient \(L^2\) metric
is fixed; no arbitrary complement is required.

---

## 7. Definition of the Gramian

Define

\[
\boxed{
A_c(\varepsilon)
=
\mathcal O_\varepsilon^*
\mathcal O_\varepsilon
:
\mathcal E_c\to\mathcal E_c.
}
\]

Equivalently, its Hermitian form is

\[
\boxed{
\langle A_c(\varepsilon)[u],[v]\rangle_{\rm quot}
=
\int_0^\varepsilon
\langle
\bar\Gamma_\delta([u]),
\bar\Gamma_\delta([v])
\rangle_{\mathbb C^2}
\,d\delta.
}
\]

This is the canonical edge Gramian.

It is:

- finite-dimensional;
- self-adjoint;
- positive;
- basis-free;
- complement-free;
- sample-free.

By injectivity of \(\mathcal O_\varepsilon\),

\[
\boxed{
A_c(\varepsilon)>0
\qquad
(0<\varepsilon\le\varepsilon_*),
}
\]

provided \(\mathcal E_c\ne0\).

Thus the abstract "canonical edge matrix" exists naturally as an operator,
rather than as an arbitrarily sampled matrix.

---

## 8. Rank-two growth law

In quadratic-form notation,

\[
A_c(\varepsilon)
=
\int_0^\varepsilon
\bar\Gamma_\delta^*\bar\Gamma_\delta\,d\delta.
\]

Therefore

\[
\boxed{
\frac d{d\varepsilon}A_c(\varepsilon)
=
\bar\Gamma_\varepsilon^*
\bar\Gamma_\varepsilon
}
\]

where the derivative is interpreted entrywise/formwise on the
finite-dimensional quotient.

Since

\[
\bar\Gamma_\varepsilon:
\mathcal E_c\to\mathbb C^2,
\]

we have

\[
\boxed{
\operatorname{rank}A_c'(\varepsilon)\le2.
}
\]

So the canonical edge detector is an integrated rank-two observation Gramian.

This is stronger structural information than an arbitrary invertible sampled
matrix.

---

# IV. Canonical determinant

## 9. Intrinsic determinant

Let

\[
d=\dim\mathcal E_c.
\]

If \(d>0\), define

\[
\boxed{
D_c(\varepsilon)
=
\det_{\mathcal E_c}A_c(\varepsilon),
}
\]

where the determinant is taken relative to the canonical quotient Hilbert
metric.

Equivalently, in any quotient-orthonormal basis
\(e_1,\ldots,e_d\),

\[
D_c(\varepsilon)
=
\det
\left[
\int_0^\varepsilon
\langle
\bar\Gamma_\delta(e_i),
\bar\Gamma_\delta(e_j)
\rangle_{\mathbb C^2}
\,d\delta
\right]_{i,j=1}^d.
\]

Changing the orthonormal basis conjugates the matrix unitarily and leaves the
determinant unchanged.

Since \(A_c(\varepsilon)>0\),

\[
\boxed{
D_c(\varepsilon)>0
\qquad
(0<\varepsilon\le\varepsilon_*)
}
\]

whenever \(d>0\).

---

# V. Continuous Cauchy-Binet formula

## 10. Edge samples as one observation space

Let

\[
X_\varepsilon
=
(0,\varepsilon)\times\{+,-\}
\]

with product measure

\[
d\mu=d\delta\times\text{counting measure}.
\]

For an orthonormal basis \(e_1,\ldots,e_d\) of \(\mathcal E_c\), define

\[
f_j(\delta,\sigma)
=
(\bar\Gamma_\delta(e_j))_\sigma.
\]

Then

\[
A_c(\varepsilon)_{ij}
=
\int_{X_\varepsilon}
f_i(x)\overline{f_j(x)}\,d\mu(x).
\]

The continuous Gram/Cauchy-Binet identity gives

\[
\boxed{
D_c(\varepsilon)
=
\frac1{d!}
\int_{X_\varepsilon^d}
\left|
\det
\bigl(
f_j(x_i)
\bigr)_{i,j=1}^d
\right|^2
\,d\mu(x_1)\cdots d\mu(x_d).
}
\]

Each determinant inside the integral is exactly a finite edge-sample matrix
determinant of the kind produced existentially in QA-2.

Therefore the earlier noncanonical finite matrices assemble into one canonical
quantity:

\[
\boxed{
\text{canonical determinant}
=
\text{average squared edge-sample volume}.
}
\]

This removes the sample-choice defect without discarding the finite-matrix
interpretation.

---

## 11. Equivalence with finite separation

The integrand is nonnegative.

Hence

\[
D_c(\varepsilon)>0
\]

if and only if the observation family spans the full dual of
\(\mathcal E_c\), equivalently if and only if some \(d\)-tuple of edge
observations has nonzero determinant.

Thus QA-2's existence theorem and positivity of the canonical Gram determinant
are two formulations of the same finite-dimensional fact.

The latter is basis-free and suitable for asymptotic analysis.

---

# VI. Superflatness becomes a canonical scalar obstruction

## 12. Operator superflatness

Every class in \(\mathcal E_c\) is represented by a vector in \(F_\infty\).

Hence for every \(N\),

\[
\Delta_{c,c+\varepsilon}(u)
=
o(\varepsilon^N).
\]

Take a fixed quotient-orthonormal basis
\(e_1,\ldots,e_d\).

For each basis vector,

\[
\langle A_c(\varepsilon)e_j,e_j\rangle
=
\Delta_{c,c+\varepsilon}(e_j)^2
=
o(\varepsilon^M)
\]

for every \(M\).

Since \(A_c(\varepsilon)\ge0\),

\[
\|A_c(\varepsilon)\|
\le
\operatorname{tr}A_c(\varepsilon)
=
\sum_{j=1}^d
\Delta_{c,c+\varepsilon}(e_j)^2.
\]

Therefore

\[
\boxed{
\|A_c(\varepsilon)\|
=
o(\varepsilon^M)
\qquad
\forall M.
}
\]

So the entire canonical Gramian is superflat, not merely each chosen vector.

---

## 13. Determinant superflatness

For \(d>0\),

\[
0<D_c(\varepsilon)
\le
\|A_c(\varepsilon)\|^d.
\]

Hence

\[
\boxed{
D_c(\varepsilon)
=
o(\varepsilon^M)
\qquad
\forall M.
}
\]

Thus a nonzero edge obstruction is equivalent to the existence of a canonical
scalar function satisfying the striking pair

\[
\boxed{
D_c(\varepsilon)>0
\quad
(\varepsilon>0),
}
\]

but

\[
\boxed{
D_c(\varepsilon)
\text{ is flat to every algebraic order at }0.
}
\]

This is the first canonical scalar packaging of the remaining edge defect.

---

# VII. What would now kill the obstruction

## 14. Analytic determinant criterion

If one could prove that

\[
D_c(\varepsilon)
\]

extends real-analytically to \(\varepsilon=0\), then its infinite-order
flatness would force

\[
D_c\equiv0
\]

near zero.

But positivity for every \(\varepsilon>0\) would then be impossible when
\(d>0\).

Therefore:

\[
\boxed{
D_c
\text{ real-analytic at }0
\Longrightarrow
\mathcal E_c=0.
}
\]

More generally, any quasi-analytic class for \(D_c\) at the edge would suffice.

This is now a scalar determinant-rigidity target rather than a
vector-by-vector endpoint regularity target.

---

# VIII. Localization of the remaining nonanalyticity

## 15. Screw-kernel decomposition of the observation

The ratified QA-1 formula expresses each scalar edge functional as

\[
\ell_{\delta,\sigma}(u)
=
\text{analytic bulk moment}
+
\sum_{x\in\Sigma_c}
\text{local Volterra/germ contribution at }x.
\]

Therefore every entry of the Gramian, and every sampled determinant in the
continuous Cauchy-Binet formula, is built from:

1. analytic bulk terms;
2. finitely many local germ terms at the arithmetic singular set
   \(\Sigma_c\).

Hence any failure of quasi-analyticity of the canonical determinant is
localized to the same finite singular package already isolated by QA-1.

No new whole-interval pathology is introduced by passing to the determinant.

---

# IX. Result of this NF pass

The arbitrary-matrix problem has a canonical resolution.

For each sufficiently small collar there is a canonical positive operator

\[
\boxed{
A_c(\varepsilon)
=
\mathcal O_\varepsilon^*\mathcal O_\varepsilon
}
\]

on

\[
\mathcal E_c=F_\infty/P_c^+,
\]

with exact quadratic form

\[
\boxed{
\langle A_c(\varepsilon)[u],[u]\rangle
=
\Delta_{c,c+\varepsilon}(u)^2.
}
\]

If \(\mathcal E_c\ne0\), then

\[
\boxed{
A_c(\varepsilon)>0,
\qquad
D_c(\varepsilon)=\det A_c(\varepsilon)>0,
}
\]

for every sufficiently small \(\varepsilon>0\), while simultaneously

\[
\boxed{
A_c(\varepsilon)
\text{ and }
D_c(\varepsilon)
\text{ are superflat at }0.
}
\]

Moreover,

\[
\boxed{
D_c(\varepsilon)
=
\frac1{d!}
\int
|\det(\text{finite edge sample matrix})|^2,
}
\]

so the previous existential edge matrices are precisely the finite minors
whose squared volume is canonically averaged by \(D_c\).

The canonicalization problem is therefore substantially closed.

What remains is not to choose a better matrix.

What remains is to rule out a positive infinitely-flat canonical determinant.

---

# X. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-DET-1 / CANONICAL GRAM DETERMINANT RIGIDITY}.
}
\]

The next pass should attack one of the equivalent goals:

1. prove \(D_c(\varepsilon)\) belongs to a quasi-analytic class at
   \(\varepsilon=0\);
2. prove a finite-order lower bound
   \[
   D_c(\varepsilon)\gtrsim \varepsilon^\alpha
   \]
   whenever \(d>0\);
3. extract a nonzero finite-order wedge coefficient from the local
   screw-kernel/prime-hinge decomposition;
4. use the first-kind interior equation to forbid a nonzero exterior-power
   observation from being infinitely flat.

Any of these would contradict the superflatness forced by
\(\mathcal E_c\subset F_\infty/P_c^+\) and therefore give

\[
\mathcal E_c=0.
\]

No such rigidity result is proved in this pass.

---

# XI. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This note is an unratified NF result beneath the ratified edge package.

No public promotion and no canonical cursor movement are asserted.
