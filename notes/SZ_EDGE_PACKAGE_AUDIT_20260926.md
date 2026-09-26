# SZ-EDGE-PACKAGE-AUDIT-20260926 — Adversarial audit of the excluded edge package

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Operation:** adversarial audit only; no new traversal  
**Canonical theorem head:** SZ-CROSS-COLLAR-3  
**Canonical supporting head:** SZ-POST3-RATIFICATION-20260926  
**Public promotion:** forbidden

## 0. Scope

This audit reviews the three edge notes deliberately excluded from the
post-SZ-3 ratification:

- SZ-KERNEL-EDGE-PROP-0;
- SZ-KERNEL-EDGE-QA-1;
- SZ-KERNEL-EDGE-QA-2.

The source gate needed by QA-1 has now been closed by

\[
\text{SZ-SUZUKI-ARCHIMEDEAN-ANALYTICITY-PIN}.
\]

The purpose of this audit is to decide whether the edge package is
mathematically fit for a later ratification pass and to isolate any corrections
required first.

No theorem cursor is moved here.

---

# I. SZ-KERNEL-EDGE-PROP-0

## 1. Finite prime-delay geometry — PASSES

For the right exterior point

\[
x=c+\delta,
\]

the translated source sample

\[
u(c+\delta-\log n)
\]

can be nonzero only when

\[
\delta<\log n<2c+\delta.
\]

For a sufficiently small fixed collar:

- every already-active prime power with
  \[
  \log n<2c
  \]
  samples a fixed compact subinterval strictly inside \((-c,c)\);

- no prime power with \(\log n>2c\) enters, except the possible exact
  threshold
  \[
  \log n_0=2c;
  \]

- the threshold is unique because it corresponds to one natural number
  \(n_0=e^{2c}\).

At threshold,

\[
u(c+\delta-\log n_0)
=
u(-c+\delta),
\]

so exactly one arithmetic hinge directly couples the two endpoint germs.

The left-edge statement is the mirror image.

**Disposition:** RATIFIABLE AUXILIARY.

---

## 2. Zero-eigenvalue nonbootstrap — PASSES

Suzuki §2.1 explicitly states

\[
G_a u\in H^1(-a,a)
\qquad
(u\in L_0^2(-a,a)).
\]

For a nonzero eigenvalue,

\[
G_au=\lambda u,
\qquad
\lambda\ne0,
\]

this gives

\[
u=\lambda^{-1}G_au\in H^1.
\]

At zero eigenvalue,

\[
G_au=0,
\]

there is no inverse relation from the smoothed output back to \(u\).

Therefore the inference

\[
G_a:L^2\to H^1
\quad\Longrightarrow\quad
\ker G_a\subset H^1
\]

is invalid without additional structure.

This is a scope/no-bootstrap statement, not a claim that the actual Weil
kernel necessarily contains rough vectors.

Suzuki also explicitly identifies the relevant equations as Fredholm
integral equations of the first kind.

**Disposition:** RATIFIABLE SCOPE / NO-GO STATEMENT.

---

## 3. Generic smooth-kernel countermodel — PASSES AS AUXILIARY EXAMPLE

The construction with an arbitrary unit vector

\[
u_0\in L^2(-c,c)
\]

can be made rigorous:

1. \(C^\infty(-c,c)\cap u_0^\perp\) is dense in \(u_0^\perp\);
2. Gram-Schmidt gives an orthonormal basis
   \[
   (e_j)
   \]
   of \(u_0^\perp\) consisting of smooth functions;
3. choose \(\lambda_j>0\) decreasing sufficiently rapidly so that every
   differentiated kernel series
   \[
   \sum_j
   \lambda_j
   e_j^{(r)}(x)
   \overline{e_j^{(s)}(y)}
   \]
   converges uniformly;
4. then
   \[
   K(x,y)
   =
   \sum_j
   \lambda_j e_j(x)\overline{e_j(y)}
   \]
   is \(C^\infty\), self-adjoint, compact, and its operator has
   \[
   \ker T=\mathbb C u_0.
   \]

Hence smoothness of a compact integral kernel does not, by itself, regularize
its zero eigenspace.

**Disposition:** RATIFIABLE AUXILIARY EXAMPLE.

---

## 4. Logarithmic-Laplacian UCP comparison — CONTEXTUAL ONLY

The edge note correctly distinguishes open-set unique continuation from the
required implication

\[
\text{infinite-order edge flatness}
\Longrightarrow
\text{open-collar vanishing}.
\]

Ordinary open-set UCP cannot supply that implication, because a flat-but-
leaking mode has no exterior open set on which the residual vanishes.

The full Weil edge system also includes finite translations rather than merely
a multiplication potential.

**Disposition:** RETAIN AS CONTEXT / MOTIVATION, NOT AS A LOAD-BEARING
PROJECT THEOREM.

No later edge proof depends on a negative theorem about all possible UCP
methods.

---

# II. SZ-KERNEL-EDGE-QA-1

## 5. Exact first-difference transform — PASSES

For

\[
f_+(s)=u(c-s),
\qquad
0<s<2c,
\]

continuity of the screw potential and the endpoint constant law give

\[
\boxed{
F_u(c+\delta)-C_u
=
\int_0^{2c}
[g(s+\delta)-g(s)]f_+(s)\,ds.
}
\]

The left-edge formula follows identically from evenness of \(g\).

No differentiation of the collar residual is used.

**Disposition:** RATIFIABLE.

---

## 6. Prime-hinge Volterra decomposition — PASSES

For one hinge

\[
\ell=\log n,
\qquad
0<\ell<2c,
\]

the exact first-difference contribution is

\[
\boxed{
\frac{\Lambda(n)}{\sqrt n}
\left[
\delta\int_\ell^{2c}f(s)\,ds
+
\int_{\ell-\delta}^{\ell}
(s+\delta-\ell)f(s)\,ds
\right].
}
\]

The first term is analytic and linear in \(\delta\).

The second is the local Volterra germ

\[
\boxed{
\frac{\Lambda(n)}{\sqrt n}
\int_0^\delta
(\delta-t)f(\ell-t)\,dt.
}
\]

At

\[
\ell=2c
\]

the same formula becomes the opposite-endpoint germ.

**Disposition:** RATIFIABLE.

---

## 7. Archimedean analytic-gap input — PASSES AFTER C5

The new C5 source pin proves that the non-prime component

\[
a_\infty
\]

is real analytic on \((0,\infty)\).

Therefore, if \(f\) vanishes on a neighborhood of \(s=0\), its
archimedean first-difference transform is analytic in \(\delta\) near zero.

If \(f\) also vanishes near every active prime hinge, all local Volterra hinge
terms vanish for sufficiently small \(\delta\).

The remaining hinge contributions are linear analytic tail moments.

Hence the edge transform is analytic.

**Disposition:** RATIFIABLE.

---

## 8. Finite singular-site set — PASSES

The only source locations capable of generating nonanalytic small-collar
behavior are

\[
\boxed{
\Sigma_c
=
\{\pm c\}
\cup
\{
c-\log n,\,
-c+\log n:
\Lambda(n)\ne0,\ 0<\log n<2c
\}.
}
\]

At an exact threshold, the opposite endpoint is already represented by
\(\pm c\).

The set is finite at fixed support.

**Disposition:** RATIFIABLE.

---

## 9. Analytic-gap plus superflatness implies persistence — PASSES WITH ONE EXPLICIT MEAN LEMMA

The existing QA-1 argument is correct, but one intermediate step should be
made explicit before ratification.

Assume the two exterior residuals relative to the old constant,

\[
r_+(\delta)
=
F_u(c+\delta)-C_u,
\]

\[
r_-(\delta)
=
F_u(-c-\delta)-C_u,
\]

are real analytic near zero.

Then

\[
m(c+\delta)-C_u
=
\frac{
\int_0^\delta r_+(s)\,ds
+
\int_0^\delta r_-(s)\,ds
}{
2(c+\delta)
}.
\]

Therefore

\[
\boxed{
m(c+\delta)-C_u
\text{ is real analytic near }0.
}
\]

Hence

\[
R_+(\delta)
=
F_u(c+\delta)-m(c+\delta),
\]

and

\[
R_-(\delta)
=
F_u(-c-\delta)-m(c+\delta)
\]

are real-analytic germs.

The ratified variance identity gives

\[
\Delta(c+\varepsilon)^2
=
\int_0^\varepsilon
\left(
|R_+(s)|^2+|R_-(s)|^2
\right)ds.
\]

If either germ has finite first nonzero Taylor order \(k\), the nonnegative
integrand has leading order \(s^{2k}\), so

\[
\Delta(c+\varepsilon)^2
\asymp
\varepsilon^{2k+1}.
\]

Thus

\[
\Delta(c+\varepsilon)
=
o(\varepsilon^N)
\quad
\forall N
\]

forces both analytic germs to vanish identically near zero.

Consequently

\[
\boxed{
\Delta(c+\varepsilon)=0
}
\]

on a strict collar.

There is no cancellation issue because the variance integrand is a sum of
nonnegative squared moduli.

**Disposition:** RATIFIABLE AFTER ADDING THIS MEAN-ANALYTICITY LINE TO THE
RATIFICATION RECORD.  No mathematical change to QA-1 is required.

---

## 10. Contrapositive singular-site localization — PASSES

Because \(\Sigma_c\) is finite, failure of the analytic-gap hypothesis is
equivalent to the existence of at least one

\[
x_0\in\Sigma_c
\]

such that \(u\) is nonzero on every neighborhood of \(x_0\) in the
essential-support sense.

Therefore every superflat leaking kernel mode must be locally nontrivial at
one of finitely many arithmetic singular sites.

**Disposition:** RATIFIABLE.

---

# III. SZ-KERNEL-EDGE-QA-2

## 11. Local restriction separation — PASSES, AND CAN BE STRENGTHENED

Choose

\[
F_\infty
=
P_c^+\oplus E_c.
\]

Every \(u\in E_c\) is superflat and no nonzero \(u\in E_c\) is persistent.

QA-1 implies that if \(u\in E_c\) vanishes on a neighborhood of every point
of \(\Sigma_c\), then \(u\) is persistent, hence \(u=0\).

Therefore, for

\[
U_r
=
(-c,c)
\cap
\bigcup_{x\in\Sigma_c}(x-r,x+r),
\]

the restriction map

\[
R_r:E_c\to L^2(U_r)
\]

is actually injective for **every**

\[
r>0,
\]

not merely for sufficiently small \(r\).

Indeed,

\[
R_ru=0
\]

already means that \(u\) vanishes on an open neighborhood of every singular
site.

Thus the existing QA-2 statement is correct but weaker than necessary.

**Disposition:** RATIFIABLE WITH OPTIONAL STRENGTHENING.

---

## 12. Fixed-radius local mass bound — PASSES

For every fixed \(r>0\), finite dimensionality plus injectivity gives

\[
\boxed{
\|u\|_{L^2(U_r)}
\ge
\eta_r\|u\|_2
\qquad
(u\in E_c)
}
\]

for some \(\eta_r>0\).

No uniform control of \(\eta_r\) as \(r\downarrow0\) follows.

**Disposition:** RATIFIABLE.

---

## 13. Finite local-moment separation — PASSES

Since \(R_r(E_c)\) is finite-dimensional and \(R_r\) is injective, finitely
many \(L^2(U_r)\) dual functionals separate the space.

Thus there exist local test functions supported arbitrarily close to
\(\Sigma_c\) such that the associated moment map is injective on \(E_c\).

This is ordinary finite-dimensional duality and requires no pointwise trace.

**Disposition:** RATIFIABLE.

---

## 14. Collar-evaluation separation — PASSES USING THE VARIANCE IDENTITY

Define

\[
\Gamma_u(\delta)
=
\left(
F_u(c+\delta)-m_u(c+\delta),
F_u(-c-\delta)-m_u(c+\delta)
\right).
\]

If

\[
\Gamma_u(\delta)=0
\]

for every

\[
0<\delta<\varepsilon,
\]

then the variance-growth identity gives

\[
\frac d{db}\Delta_{c,b}(u)^2=0
\]

throughout that collar.

Since

\[
\Delta_{c,c}(u)=0,
\]

we obtain

\[
\Delta_{c,c+\delta}(u)=0
\]

for all \(\delta<\varepsilon\), so \(u\in P_c^+\).

Therefore the family of arbitrarily small scalar edge evaluations separates
\(E_c\).

Finite dimensionality then reduces this to at most

\[
d=\dim E_c
\]

scalar evaluations.

**Disposition:** RATIFIABLE.

---

## 15. Finite edge matrix — PASSES AS EXISTENCE, NOT CANONICALITY

After choosing a basis of \(E_c\) and a finite separating family of collar
evaluations, the resulting matrix is invertible.

This is an existence certificate.

It is **not** canonical:

- the basis is arbitrary;
- the sample locations are arbitrary;
- the matrix entries may be superpolynomially small;
- no determinant asymptotic or arithmetic formula is presently available.

**Disposition:** RATIFIABLE AS AN EXISTENCE LEMMA ONLY.

---

# IV. Audit corrections and boundaries

## 16. Correction E1 — make mean analyticity explicit

Before ratifying QA-1, record

\[
m(c+\delta)-C_u
=
\frac{
\int_0^\delta r_+(s)\,ds
+
\int_0^\delta r_-(s)\,ds
}{
2(c+\delta)
}.
\]

This closes the only omitted intermediate analytic step in the
analytic-gap proof.

---

## 17. Correction E2 — strengthen QA-2 restriction injectivity

Replace

\[
R_r\text{ injective for sufficiently small }r
\]

by the cleaner consequence

\[
\boxed{
R_r\text{ is injective for every }r>0.
}
\]

The weaker existing statement is not false; this is an editorial
strengthening.

---

## 18. Do not ratify contextual UCP/Hopf claims as theorem dependencies

The comparisons to logarithmic-Laplacian UCP and Hopf-type boundary theory
remain useful motivation.

They are not required for QA-1 or QA-2 and should not enter their dependency
graph.

This avoids turning “current literature does not immediately provide the
needed theorem” into an unnecessarily strong mathematical no-go claim.

---

## 19. Superflat Stieltjes example remains outside the package

The edge audit does not need the illustrative conformal/Stieltjes example in
SZ-MV-ROUGH-ENDPOINT-0.

Therefore C4 remains non-load-bearing exactly as decided in the post-SZ-3
ratification.

No edge theorem should cite that example as a premise.

---

# V. Audit determination

The edge package contains **no fatal mathematical defect**.

The audit-safe disposition is:

\[
\boxed{
\begin{array}{c|c}
\text{component} & \text{audit disposition}\\
\hline
\text{EDGE-PROP finite delay geometry} & \text{RATIFIABLE AUXILIARY}\\
\text{EDGE-PROP zero-eigenvalue nonbootstrap} & \text{RATIFIABLE SCOPE}\\
\text{generic smooth-kernel countermodel} & \text{RATIFIABLE EXAMPLE}\\
\text{UCP/Hopf discussion} & \text{CONTEXTUAL ONLY}\\
\text{QA-1 first-difference transform} & \text{RATIFIABLE}\\
\text{QA-1 finite singular-site localization} & \text{RATIFIABLE}\\
\text{QA-1 analytic-gap rigidity} & \text{RATIFIABLE after E1}\\
\text{QA-2 local moment separation} & \text{RATIFIABLE}\\
\text{QA-2 collar-sample separation} & \text{RATIFIABLE}\\
\text{QA-2 edge matrix} & \text{RATIFIABLE AS EXISTENCE ONLY}
\end{array}
}
\]

The package still does **not** prove

\[
\mathcal E_c=0.
\]

Instead it canonically reduces any nonzero edge defect to finite local data
near

\[
\Sigma_c
\]

and proves that a hypothetical obstruction has a finite, arbitrarily local
linear-algebraic certificate.

---

# VI. Recommended next action

A dedicated **edge-package ratification pass** is now justified.

That pass should:

1. include E1 explicitly;
2. adopt the E2 strengthened restriction statement;
3. ratify only the structural EDGE-PROP pieces;
4. keep UCP/Hopf discussion contextual;
5. ratify QA-1 and QA-2;
6. leave the theorem cursor at SZ-CROSS-COLLAR-3;
7. declare the next genuinely new target to be

\[
\boxed{
\text{SZ-KERNEL-EDGE-QA / CANONICAL EDGE MATRIX}.
}
\]

No traversal movement is authorized by this audit.
