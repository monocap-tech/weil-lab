# SZ-ZERO-SIDE-NORMALIZATION-0 — Zero-side normalization ledger

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** AUDIT NORMALIZATION / OPEN-BRIDGE SUPPORT  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Purpose:** discharge audit item C1 before ratifying the Suzuki channel bridge  
**Traversal movement:** none

## 0. Scope

This note fixes the exact normalization used by the post-SZ-3 zero-side
channel bridge.

It does not add a new mathematical theorem.

It records:

1. the additive Fourier-transform convention;
2. Bombieri ordinate coordinates;
3. multiplicity handling;
4. the normalized conjugate-pair transform used in Hilbert norm identities;
5. the distinction between that unitary transform and the existing Lean
   algebraic pair equivalence;
6. the corresponding selected/background coefficient spaces.

The purpose is to remove the last normalization ambiguity from
SZ-PRECOND-FORM-BRIDGE-2 and SZ-CHANNEL-CUSTODY-FORMDOMAIN-0.

---

## 1. Additive Fourier convention

For a compactly supported physical test function \(f\), use

\[
\boxed{
\widehat f(z)
:=
\int_{\mathbb R}
f(x)e^{izx}\,dx.
}
\]

For support in \([-a,a]\),

\[
\widehat f(z)
=
\int_{-a}^{a}
f(x)e^{izx}\,dx.
\]

This is the convention used in Suzuki's screw-function framework; in
particular Suzuki writes transforms with \(e^{izt}\) and uses the corresponding
\(1/(2\pi)\) Plancherel normalization.

Accordingly,

\[
\boxed{
\|f\|_2^2
=
\frac1{2\pi}
\int_{\mathbb R}
|\widehat f(t)|^2\,dt.
}
\]

This is also the convention compatible with the Horizon-1 compact-window
formula

\[
Q_c(f)
=
2|\widehat f(i/2)|^2
+
\frac1{2\pi}
\int_{\mathbb R}
|\widehat f(t)|^2\Psi_c(t)\,dt.
\]

No \(2\pi\) is placed in the exponential.

---

## 2. Compatibility with Suzuki's derivative coordinate

On the regular carrier let

\[
D=i\,\frac{d}{dx}
\]

and

\[
u=Dv=iv',
\qquad
v\in H_0^1(-a,a).
\]

Since

\[
v(\pm a)=0,
\]

integration by parts gives

\[
\begin{aligned}
\int_{-a}^{a}
u(x)e^{i\gamma x}\,dx
&=
i\int_{-a}^{a}
v'(x)e^{i\gamma x}\,dx\\
&=
\gamma
\int_{-a}^{a}
v(x)e^{i\gamma x}\,dx.
\end{aligned}
\]

Therefore

\[
\boxed{
\widehat v(\gamma)
=
\frac1{\gamma}
\int_{-a}^{a}
u(x)e^{i\gamma x}\,dx.
}
\]

Thus the scalar \(c_{\rm FT}\) left implicit in
SZ-PRECOND-FORM-BRIDGE-2 is

\[
\boxed{
c_{\rm FT}=1
}
\]

under the project convention above.

The finitely many low ordinates are treated separately when the
\(1/|\gamma|\) Bessel estimate is used.

---

## 3. Bombieri ordinate coordinate

Write a nontrivial zero as

\[
\rho
=
\frac12+i\gamma.
\]

Thus

\[
\boxed{
\gamma
=
-i\left(\rho-\frac12\right).
}
\]

If an off-critical zero is written

\[
\rho
=
\frac12-\delta+iT,
\]

then

\[
\gamma
=
T+i\delta.
\]

Its reflection across the critical line corresponds to

\[
\bar\gamma
=
T-i\delta.
\]

Hence one nonreal Bombieri ordinate pair is

\[
\boxed{
\gamma=T+i\delta,
\qquad
\bar\gamma=T-i\delta.
}
\]

This is the convention used throughout H1-P2.

---

## 4. Raw zero-side analysis coordinate

First work on the zero multiset: one raw coordinate is retained for every zero
occurrence.

For one occurrence of ordinate \(\gamma\), define

\[
z_\gamma(f)
:=
\widehat f(\gamma).
\]

If a distinct ordinate \(\gamma\) has multiplicity

\[
m_\gamma,
\]

then before quotienting the raw multiplicity block contains \(m_\gamma\)
copies of the same analysis coordinate

\[
\widehat f(\gamma).
\]

The zero-sum subspace in that multiplicity block is synthesis-null and is
quotiented exactly as in WD-T23 / ZW1-T4.

---

## 5. Normalized distinct-ordinate coordinate after the multiplicity quotient

Let

\[
e_{\gamma,1},\ldots,e_{\gamma,m_\gamma}
\]

be the orthonormal raw occurrence basis at one repeated ordinate.

The normalized surviving diagonal vector is

\[
\widetilde e_\gamma
=
\frac1{\sqrt{m_\gamma}}
\sum_{j=1}^{m_\gamma}
e_{\gamma,j}.
\]

The analysis coordinate along this normalized survivor is

\[
\boxed{
w_\gamma(f)
=
\sqrt{m_\gamma}\,
\widehat f(\gamma).
}
\]

Thus

\[
|w_\gamma(f)|^2
=
m_\gamma
|\widehat f(\gamma)|^2.
\]

This is the Hilbert normalization compatible with counting zeros with
multiplicity while quotienting the \(m_\gamma-1\) null directions.

Hence there are two distinct statements:

\[
\boxed{
\text{multiplicity changes the weight of the surviving coordinate},
}
\]

but

\[
\boxed{
\text{multiplicity does not create additional independent channels}.
}
\]

These are exactly compatible with EXT-2B / WD-T23.

---

## 6. Multiplicity symmetry inside a conjugate pair

For the zeta divisor, the functional-equation/conjugation symmetry preserves
multiplicity.

Therefore, for a nonreal Bombieri pair,

\[
m_\gamma=m_{\bar\gamma}.
\]

Write their normalized distinct-ordinate coordinates as

\[
w_\gamma,
\qquad
w_{\bar\gamma}.
\]

All pair norm identities below are applied to these multiplicity-weighted
coordinates.

---

## 7. Analytic Hilbert pair transform

For one nonreal pair, define the **normalized analytic pair coordinates**

\[
\boxed{
p
=
\frac{w_\gamma+w_{\bar\gamma}}{\sqrt2},
\qquad
n
=
\frac{w_\gamma-w_{\bar\gamma}}{\sqrt2}.
}
\]

Equivalently,

\[
\begin{pmatrix}
p\\
n
\end{pmatrix}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
\begin{pmatrix}
w_\gamma\\
w_{\bar\gamma}
\end{pmatrix}.
\]

This matrix is unitary and self-inverse.

Therefore

\[
\boxed{
|w_\gamma|^2+|w_{\bar\gamma}|^2
=
|p|^2+|n|^2.
}
\]

The pair fundamental symmetry is diagonalized as

\[
\boxed{
Jp=p,
\qquad
Jn=-n.
}
\]

The Hermitian pair contribution is

\[
w_\gamma\overline{w_{\bar\gamma}}
+
w_{\bar\gamma}\overline{w_\gamma}
=
\boxed{
|p|^2-|n|^2.
}
\]

This is the pair normalization used in every channel norm-square formula.

---

## 8. Critical-line coordinate

If \(\gamma\) is real in Bombieri ordinate coordinates, then

\[
\gamma=\bar\gamma.
\]

After multiplicity quotienting there is one normalized active coordinate

\[
w_\gamma
=
\sqrt{m_\gamma}\widehat f(\gamma),
\]

and it contributes

\[
\boxed{
|w_\gamma|^2
}
\]

to the positive zero-side sector.

There is no corresponding negative pair coordinate.

---

## 9. Full normalized zero-side coefficient spaces

After multiplicity-null quotienting and the unitary pair transform, define

\[
K_+
=
K_{\rm crit}
\oplus
K_{{\rm off},+},
\]

\[
K_-
=
K_{{\rm off},-}.
\]

The normalized zero-side analysis map is

\[
\mathcal Z_a f
=
\bigl(
\mathcal Z_{+,a}f,\,
\mathcal Z_{-,a}f
\bigr).
\]

For a finite selected packet \(\Pi\),

\[
K_-
=
M_\Pi
\oplus
B_\Pi
\]

orthogonally.

Thus

\[
\mathcal Z_{-,a}
=
\mathcal Z_{M,a}
\oplus
\mathcal Z_{B,a}.
\]

The corresponding quadratic decomposition is

\[
\boxed{
Q_W(f)
=
\|\mathcal Z_{+,a}f\|^2
-
\|\mathcal Z_{M,a}f\|^2
-
\|\mathcal Z_{B,a}f\|^2,
}
\]

in the project zero-side normalization.

If an external presentation of the Weil form differs by one common positive
scalar \(c_W\), all three channel maps are simultaneously replaced by

\[
\sqrt{c_W}\,\mathcal Z_{+,a},
\qquad
\sqrt{c_W}\,\mathcal Z_{M,a},
\qquad
\sqrt{c_W}\,\mathcal Z_{B,a}.
\]

No sign, range, Douglas-budget, or ownership statement depends on that common
positive rescaling.

---

## 10. Important distinction from the current Lean pair equivalence

The current Lean file

\[
\texttt{WeilDefect/PairGeometry.lean}
\]

defines

\[
\texttt{pairPos}=(1,1),
\qquad
\texttt{pairNeg}=(1,-1),
\]

and the algebraic equivalence

\[
(a,b)
\longmapsto
a\,\texttt{pairPos}
+
b\,\texttt{pairNeg}.
\]

Thus its raw coordinates are

\[
(a+b,\ a-b),
\]

with inverse

\[
\left(
\frac{z_1+z_2}{2},
\frac{z_1-z_2}{2}
\right).
\]

This is an exact algebraic diagonalization of the swap involution, but it is
**not** the unitary analytic pair transform of Section 7.

Therefore:

\[
\boxed{
\texttt{pairEigenEquiv}
\text{ certifies eigenspace algebra, not Hilbert normalization.}
}
\]

Downstream norm-square identities must use the normalized analytic pair
coordinates

\[
\frac1{\sqrt2}(w_\gamma\pm w_{\bar\gamma}),
\]

not the raw Lean coefficients without the corresponding scale conversion.

No existing WD-T20 theorem is invalidated by this distinction.

---

## 11. Raw residue normalization

For a normalized negative pair coordinate

\[
n=\alpha,
\]

undoing the unitary transform gives the raw distinct-ordinate residues

\[
\boxed{
\left(
\frac{\alpha}{\sqrt2},
-\frac{\alpha}{\sqrt2}
\right).
}
\]

Therefore

\[
\sum_{\text{pair}}v_j=0.
\]

This agrees with the H1-P2 prose formulation of ZW1-T7.

The Lean helper

\[
\texttt{rawResiduesOfNegativePairs}
\]

uses the unnormalized algebraic pair

\[
(\alpha,-\alpha).
\]

That is sufficient for the certified zero-moment and nonvanishing statements,
because both are homogeneous.

It should not be used without rescaling for analytic norm identities.

---

## 12. Support naturality under the normalized convention

If \(E_{c,b}\) is zero extension and \(f\) is supported in \([-c,c]\), then

\[
\widehat{E_{c,b}f}(\gamma)
=
\widehat f(\gamma).
\]

The multiplicities \(m_\gamma\) and the unitary pair transform are independent
of the support radius.

Therefore

\[
\boxed{
\mathcal Z_{M,b}(E_{c,b}f)
=
\mathcal Z_{M,c}(f)
}
\]

for every fixed selected packet \(\Pi\).

Hence the raw selected-coordinate naturality proved in
SZ-CROSS-COLLAR-4R remains exact under the normalized Hilbert convention.

---

## 13. Consequence for the regular Suzuki bridge

On the regular carrier,

\[
u=Dv,
\]

and Suzuki gives

\[
Q_W(v_1,v_2)
=
\langle G_a u_1,u_2\rangle.
\]

With the normalization ledger above, the zero-side identity becomes

\[
\boxed{
\langle G_au_1,u_2\rangle
=
\langle
\mathcal A_{+,a}u_1,
\mathcal A_{+,a}u_2
\rangle
-
\langle
\mathcal A_{M,a}u_1,
\mathcal A_{M,a}u_2
\rangle
-
\langle
\mathcal A_{B,a}u_1,
\mathcal A_{B,a}u_2
\rangle,
}
\]

where

\[
\mathcal A_{\bullet,a}
=
\mathcal Z_{\bullet,a}D^{-1}.
\]

Thus the normalization ambiguity identified by the audit is removed.

---

## 14. Consequence for LOG-BESSEL

The LOG-BESSEL estimate should be read with multiplicity included:

\[
\boxed{
\sum_{\gamma\ {\rm distinct}}
m_\gamma
|\widehat f(\gamma)|^2
\lesssim_a
\int_{\mathbb R}
\log(e+|t|)
|\widehat f(t)|^2\,dt.
}
\]

Equivalently,

\[
\boxed{
\|\mathcal Z_af\|_{\ell^2}^2
\lesssim_a
\|f\|_{\log}^2.
}
\]

This follows from the same unit-shell proof because the external zero-count
input already counts zeros with multiplicity.

So multiplicity requires no new estimate.

---

## 15. Audit determination

Audit item C1 is discharged as a normalization ledger:

\[
\boxed{
\text{Fourier sign/scale fixed;}
}
\]

\[
\boxed{
\text{multiplicity quotient and }\sqrt m\text{ weighting fixed;}
}
\]

\[
\boxed{
\text{analytic pair transform fixed as unitary }1/\sqrt2;
}
\]

\[
\boxed{
\text{Lean algebraic pair map explicitly separated from analytic
normalization.}
}
\]

No theorem cursor moves as a result.

The Suzuki channel bridge may now cite this ledger instead of the phrase
“up to fixed Fourier normalization.”

---

## 16. Remaining audit obligations

After C1, the principal normalization obligations from the post-SZ-3 audit
are:

- C2 — parity/reality-sector scope of same-source surjectivity;
- C3 — compact-collar uniformity lemma for \(\sigma_b\) and \(G_b\);
- C4 — keep the superflat Stieltjes example non-load-bearing unless fully
  source-pinned/proved;
- C5 — exact source pin for real-analyticity of Suzuki's non-prime
  archimedean screw component on \((0,\infty)\).

**No canonical cursor movement is asserted by this audit-normalization pass.**
