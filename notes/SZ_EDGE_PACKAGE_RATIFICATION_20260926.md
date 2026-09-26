# SZ-EDGE-PACKAGE-RATIFICATION-20260926 — Ratification of the audited edge package

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Operation:** audit ratification only; no new traversal  
**Canonical theorem head before/after:** SZ-CROSS-COLLAR-3  
**Canonical supporting head before:** SZ-POST3-RATIFICATION-20260926  
**Canonical supporting head after:** SZ-EDGE-PACKAGE-RATIFICATION-20260926  
**Audit record:** SZ-EDGE-PACKAGE-AUDIT-20260926  
**Audit commit:** 7347a91ba0644ed565f22cd8ec1730ae0683ed5e  
**Public promotion:** forbidden

## 0. Scope

This record ratifies the edge/quasi-analyticity package that was deliberately
excluded from SZ-POST3-RATIFICATION-20260926 and subsequently passed the
dedicated adversarial audit SZ-EDGE-PACKAGE-AUDIT-20260926.

The source package is:

- SZ-KERNEL-EDGE-PROP-0;
- SZ-KERNEL-EDGE-QA-1;
- SZ-KERNEL-EDGE-QA-2.

The source gate required by QA-1 is supplied by the already-ratified

\[
\text{SZ-SUZUKI-ARCHIMEDEAN-ANALYTICITY-PIN}.
\]

This pass incorporates the two audit corrections:

- **E1:** mean analyticity is made explicit in the analytic-gap argument;
- **E2:** local restriction injectivity is strengthened from sufficiently small
  \(r\) to every \(r>0\).

This is a supporting-package ratification.  It does not move the theorem
cursor, does not prove endpoint quasi-analyticity, and does not prove

\[
\mathcal E_c=0.
\]

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

---

# I. EDGE-PROP structural package

## A1. Finite prime-delay geometry — RATIFIED AUXILIARY

For the right exterior point

\[
x=c+\delta,
\]

a translated arithmetic sample

\[
u(c+\delta-\log n)
\]

can be nonzero only when

\[
\delta<\log n<2c+\delta.
\]

For a sufficiently small fixed collar, every already-active prime power
\(\log n<2c\) samples a fixed compact subinterval of \((-c,c)\), while no
prime power with \(\log n>2c\) enters except for the possible exact threshold

\[
\log n_0=2c.
\]

At that threshold,

\[
u(c+\delta-\log n_0)=u(-c+\delta),
\]

so a unique arithmetic hinge can directly couple the two endpoint germs.

The left-edge statement is obtained by symmetry.

**Ratified scope:** finite delay geometry and the exact-threshold coupling
statement.

---

## A2. Zero-eigenvalue nonbootstrap — RATIFIED SCOPE STATEMENT

Suzuki's regularity statement

\[
G_a u\in H^1(-a,a)
\]

does not imply

\[
\ker G_a\subset H^1(-a,a).
\]

For a nonzero eigenvalue,

\[
G_a u=\lambda u,\qquad \lambda\ne0,
\]

one may infer

\[
u=\lambda^{-1}G_a u\in H^1.
\]

At zero eigenvalue, however,

\[
G_a u=0
\]

contains no inverse relation recovering regularity of \(u\) from the smoothed
output.

Hence

\[
\boxed{
G_a:L^2\to H^1
\;\not\Rightarrow\;
\ker G_a\subset H^1
}
\]

without additional structure.

This is a no-bootstrap statement only.  It does not assert that the actual
Weil kernel contains rough vectors.

---

## A3. Smooth-kernel countermodel — VALIDATED AUXILIARY EXAMPLE

The generic smooth compact-kernel construction in EDGE-PROP is accepted as a
valid counterexample to the inference that a smooth integral kernel must have a
regular zero eigenspace.

This example is **non-load-bearing**.  It may be cited to block the invalid
bootstrap in A2, but no later edge theorem depends on its particular
construction.

---

## A4. UCP/Hopf comparisons — CONTEXTUAL ONLY

The comparisons with logarithmic-Laplacian unique continuation and Hopf-type
boundary theory remain motivation and literature context.

They are not canonical theorem dependencies.

In particular, this ratification does not promote any broad negative theorem
claiming that all UCP or Hopf mechanisms are incapable of resolving the edge
problem.

---

# II. QA-1 — first-difference and singular-site localization

## B1. Exact first-difference transform — RATIFIED

Let

\[
f_+(s)=u(c-s),\qquad 0<s<2c.
\]

Using continuity of the screw potential and the endpoint constant law,

\[
\boxed{
F_u(c+\delta)-C_u
=
\int_0^{2c}
[g(s+\delta)-g(s)]f_+(s)\,ds.
}
\]

The left-edge formula follows from evenness of \(g\).

No differentiation of the collar residual is used.

---

## B2. Prime-hinge Volterra decomposition — RATIFIED

For one active hinge

\[
\ell=\log n,\qquad 0<\ell<2c,
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

The first term is analytic and linear in \(\delta\).  The second is the local
Volterra germ

\[
\boxed{
\frac{\Lambda(n)}{\sqrt n}
\int_0^\delta
(\delta-t)f(\ell-t)\,dt.
}
\]

At \(\ell=2c\), this becomes the opposite-endpoint germ.

Thus all nonanalytic small-collar arithmetic dependence is localized to
finitely many local source germs.

---

## B3. Archimedean analytic-gap input — RATIFIED

By SZ-SUZUKI-ARCHIMEDEAN-ANALYTICITY-PIN, the non-prime component
\(a_\infty\) is real analytic on \((0,\infty)\).

Consequently, if the source vanishes on neighborhoods of the relevant endpoint
and arithmetic hinge sites, the archimedean first-difference term is analytic
in \(\delta\), all local Volterra hinge terms vanish for sufficiently small
\(\delta\), and the remaining prime-tail terms are analytic linear moments.

---

## B4. Finite singular-site set — RATIFIED

Define

\[
\boxed{
\Sigma_c
=
\{\pm c\}
\cup
\left\{
c-\log n,\,
-c+\log n:
\Lambda(n)\ne0,\;
0<\log n<2c
\right\}.
}
\]

At an exact threshold, the opposite endpoint is already represented by
\(\pm c\).

For fixed \(c\), the set \(\Sigma_c\) is finite.

Every possible nonanalytic small-collar contribution is generated by the local
\(L^2\) germ of \(u\) at a point of \(\Sigma_c\).

---

## B5. Mean-analyticity correction E1 — RATIFIED EXPLICITLY

Let the exterior residuals relative to the old constant be

\[
r_+(\delta)=F_u(c+\delta)-C_u,
\]

\[
r_-(\delta)=F_u(-c-\delta)-C_u.
\]

If \(r_+\) and \(r_-\) are real analytic near zero, then

\[
\boxed{
m(c+\delta)-C_u
=
\frac{
\int_0^\delta r_+(s)\,ds
+
\int_0^\delta r_-(s)\,ds
}{
2(c+\delta)
}.
}
\]

Since \(c>0\), the denominator is nonzero near \(\delta=0\).  Therefore

\[
m(c+\delta)-C_u
\]

is real analytic near zero.

Hence the mean-corrected edge germs

\[
R_+(\delta)=F_u(c+\delta)-m(c+\delta),
\]

\[
R_-(\delta)=F_u(-c-\delta)-m(c+\delta)
\]

are real analytic whenever the analytic-gap hypothesis holds.

This is the explicit intermediate lemma omitted from the original QA-1 note.

---

## B6. Analytic gap plus superflatness implies persistence — RATIFIED

The ratified variance identity gives

\[
\Delta(c+\varepsilon)^2
=
\int_0^\varepsilon
\left(
|R_+(s)|^2+|R_-(s)|^2
\right)\,ds.
\]

Under the analytic-gap hypothesis, \(R_\pm\) are real-analytic germs.

If either has first nonzero Taylor order \(k<\infty\), then the nonnegative
integrand has leading order \(s^{2k}\), and therefore

\[
\Delta(c+\varepsilon)^2
\asymp
\varepsilon^{2k+1}.
\]

Thus

\[
\Delta(c+\varepsilon)=o(\varepsilon^N)
\qquad
\forall N
\]

forces both analytic germs to vanish identically on a strict collar.

Therefore

\[
\boxed{
\text{analytic gap around }\Sigma_c
+
\text{superflat collar residual}
\Longrightarrow
\text{persistence}.
}
\]

No cancellation loophole exists because the variance integrand is a sum of
nonnegative squared moduli.

---

## B7. Contrapositive singular-site localization — RATIFIED

If a regular kernel mode is superflat but nonpersistent, then it cannot vanish
on neighborhoods of every point of \(\Sigma_c\).

Equivalently, there exists

\[
x_0\in\Sigma_c
\]

such that the mode is nonzero on every relative neighborhood of \(x_0\) in
the essential-support sense.

Thus every flat-but-leaking mode is forced to remain locally nontrivial at
least one of finitely many arithmetic singular sites.

This is localization, not yet elimination.

---

# III. QA-2 — finite local detectability

## C0. Canonical quotient versus chosen complement — RATIFIED DISTINCTION

The stabilized obstruction is the canonical finite-dimensional quotient

\[
\boxed{
\mathcal E_c=F_\infty/P_c^+.
}
\]

For concrete linear-algebraic arguments one may choose a complement

\[
F_\infty=P_c^+\oplus E_c.
\]

The space \(E_c\) is a representative of the quotient, not a canonical
subspace.

This distinction is load-bearing for what follows:

- finite-dimensionality of the obstruction is canonical;
- existence of separating local data is canonical up to choice;
- a particular complement, basis, sample family, and matrix are not canonical.

---

## C1. Local restriction injectivity — RATIFIED WITH E2 STRENGTHENING

For \(r>0\), let

\[
U_r
=
(-c,c)
\cap
\bigcup_{x\in\Sigma_c}(x-r,x+r).
\]

For any chosen complement \(E_c\), define

\[
R_r:E_c\to L^2(U_r).
\]

Then

\[
\boxed{
R_r\text{ is injective for every }r>0.
}
\]

Indeed, if \(R_r u=0\), then \(u\) vanishes on a relative open neighborhood of
every point of \(\Sigma_c\).  Since every \(u\in E_c\) is superflat, QA-1
implies persistence.  But

\[
E_c\cap P_c^+=\{0\},
\]

so \(u=0\).

This strengthens the original QA-2 statement from "for sufficiently small
\(r\)" to "for every \(r>0\)."

---

## C2. Fixed-radius local mass bound — RATIFIED

For every fixed \(r>0\), finite dimensionality and injectivity imply the
existence of

\[
\eta_r>0
\]

such that

\[
\boxed{
\|u\|_{L^2(U_r)}
\ge
\eta_r\|u\|_2
\qquad
(u\in E_c).
}
\]

No uniform positive lower bound on \(\eta_r\) as \(r\downarrow0\) is asserted.

---

## C3. Finite local-moment separation — RATIFIED

For every \(r>0\), the finite-dimensional space \(R_r(E_c)\subset L^2(U_r)\)
is separated by finitely many continuous \(L^2(U_r)\) dual functionals.

Hence one may choose finitely many test functions supported in \(U_r\) whose
moment map is injective on \(E_c\).

Since \(r>0\) is arbitrary, the obstruction is detectable by finitely many
local \(L^2\) moments supported arbitrarily close to \(\Sigma_c\).

No pointwise trace or positive Sobolev regularity is required.

---

## C4. Arbitrarily small collar-sample separation — RATIFIED

For \(u\in E_c\), define

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

for every \(0<\delta<\varepsilon\), then the variance-growth identity gives

\[
\Delta_{c,c+\delta}(u)=0
\]

through that collar, so \(u\in P_c^+\).

Since

\[
E_c\cap P_c^+=\{0\},
\]

the family of arbitrarily small edge evaluations separates \(E_c\).

If

\[
d=\dim E_c,
\]

finite dimensionality reduces the separating family to at most \(d\) scalar
linear functionals.

---

## C5. Finite edge matrix — RATIFIED AS EXISTENCE ONLY

Choose:

1. a complement \(E_c\);
2. a basis \(e_1,\dots,e_d\) of \(E_c\);
3. \(d\) separating scalar local/collar functionals
   \(\lambda_1,\dots,\lambda_d\).

Then the matrix

\[
\mathsf E_c
=
\bigl(\lambda_i(e_j)\bigr)_{1\le i,j\le d}
\]

is invertible:

\[
\boxed{
\det\mathsf E_c\ne0.
}
\]

This is an existence certificate for a nonzero finite-dimensional edge
obstruction.

The following are **not** ratified:

- a canonical complement \(E_c\);
- a canonical basis;
- canonical sample locations;
- canonical local moments;
- a canonical matrix \(\mathsf E_c\);
- a determinant asymptotic;
- an arithmetic determinant formula;
- a quantitative lower bound uniform as samples approach the edge.

The entries of an existence matrix may be superpolynomially small.

---

# IV. Explicit exclusions

## D1. UCP/Hopf literature comparisons

Context only.  They do not enter the dependency graph of B1–C5.

## D2. Superflat Stieltjes construction

The illustrative construction in SZ-MV-ROUGH-ENDPOINT-0 remains
non-load-bearing and unratified.

No theorem in this ratification cites it as a premise.

## D3. Endpoint elimination

This pass does not prove

\[
\boxed{
\mathcal E_c=0.
}
\]

It therefore does not prove kernel endpoint quasi-analyticity.

## D4. Public promotion

No public repository change is authorized by this ratification.

---

# V. Canonical consequence

After this pass, the post-SZ-3 bridge supports the following canonical
reduction.

The stabilized regular obstruction is

\[
\boxed{
\mathcal E_c=F_\infty/P_c^+,
}
\]

a possible nonzero finite-dimensional space.

If this quotient is nonzero, then after choosing any complement representative
\(E_c\):

1. every nonzero vector is locally nontrivial at the finite singular set
   \(\Sigma_c\);
2. restriction to every neighborhood \(U_r\) is injective;
3. finitely many \(L^2\) moments supported arbitrarily close to \(\Sigma_c\)
   separate the obstruction;
4. finitely many arbitrarily small collar evaluations separate it;
5. an invertible finite edge matrix exists.

Thus the edge package does not eliminate the obstruction.  It converts the
remaining infinite-dimensional-looking endpoint problem into a
finite-dimensional, arbitrarily local detection problem.

The canonical content is the finite obstruction and its finite local
detectability.

The presently noncanonical content is the particular detector realization.

---

# VI. Next traversal target

With EDGE-PROP / QA-1 / QA-2 now ratified, the next genuinely new traversal
target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-QA / CANONICAL EDGE MATRIX}.
}
\]

The target is not to prove once more that some invertible finite detector
matrix exists.

The target is to obtain a detector with enough canonical structure—through
screw-kernel moments, arithmetic hinge data, zero-side data, or an equivalent
intrinsic construction—that its rank or determinant can be controlled without
arbitrary choices.

A successful closure would need to bridge the gap

\[
\text{finite local detectability}
\quad\Longrightarrow\quad
\text{canonical obstruction test},
\]

and only then can one attempt to force

\[
\mathcal E_c=0.
\]

---

# VII. Canonical status

The theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

The edge package is now canonical supporting structure beneath that head.

The current obstruction remains

\[
\boxed{
\mathcal E_c=F_\infty/P_c^+.
}
\]

No traversal movement beyond the ratification boundary is asserted in this
record.
