# SM35 — Exact original 470-source resolvent certification by full Galerkin residual matrices

**October 18, 2026 · Canonical W-ODD-NEG · stacked on SM34 draft PR #215 (focused CI PASSED).**

**New result.** SM34's true original odd complete-operator sufficient acceptance
\[
\mathsf N=J^*A_*^{-1}K_-A_*^{-1}J\preceq\theta\mathsf G,\qquad
\mathsf G=J^*A_*^{-1}J,\quad \theta=\frac{51}{56},
\]
on *all* original exceptional source coefficients admits an exact, **inversion-free resolvent residual enclosure**. Instead of asserting entries of the full original \(A_*^{-1}\), one can certify a finite Galerkin solve \(Z\) against the unmodified original \(A_*=A_o-2|s\rangle\langle s|\), retaining the complete original positive archimedean continuum, then pay the entire source residual with explicit original \(\kappa_* >0\). The result is a **fully coupled matrix Loewner sufficient gate**, not componentwise Ritz or finite window positivity. It has **not yet been evaluated on the actual original 470-source Galerkin stiffness, residual, or negative-frequency physical Gram**, so complete W-ODD-NEG O1/O2, even E1–E4, whole signed Weil, native CC27 D-Riesz and RH stay **OPEN**. Independent original Fourier/form-domain analytic audit remains necessary.

## 1. An actual **470-dimensional**, linearly independent exceptional physical basis

SI10/SM32 original b9 protected cover consists of 107 **distinct positive-frequency cluster centers** \(c_j>0\), nonoverlapping in frequency, with 469 total original Taylor orders \(p_j\), and original odd-pole vector \(s(x)=\sinh(x/2)\). The true physical odd generators on the actual support \(I=[-B,B]\), \(B=11/10\), are
\[
w_{jk}(x)=
\begin{cases}
x^k\sin(2\pi c_jx), & k\text{ even},\\
x^k\cos(2\pi c_jx), & k\text{ odd},
\end{cases}
\quad 0\le k<p_j,
\qquad s(x)=\sinh(x/2).
\]
SI10 gives \(\sum p_j=469\), including 260 sine-type and 209 cosine-type functions; **the exact dimension is 470**, not merely \(\le470\).

**Analytic independence proof.** Suppose a real linear combination vanishes almost everywhere on \((-B,B)\). It is real analytic and hence vanishes identically on the whole real line and by entire continuation. Expand each sine/cosine into \(e^{\pm2\pi ic_jz}\) times its polynomial coefficient and \(s\) into \((e^{z/2}-e^{-z/2})/2\). The exponential frequencies \(\{\pm2\pi ic_j\}\cup\{\pm1/2\}\) are pairwise distinct, as the actual cluster centers are distinct and positive. Uniqueness of exponential polynomials therefore forces each polynomial coefficient and the coefficient of \(s\) to vanish; in each frequency cluster the distinct monomials \(x^k\) force all 469 original source coefficients to vanish. Thus the true physical inclusion \(J:\mathbb R^{470}\hookrightarrow H_o\) is injective, with \(\mathsf H=J^*J\succ0\). This is a rank result, **not a lower bound** on the smallest eigenvalue of that possibly ill-conditioned Gram.

These compactly supported analytic-on-the-interior generators, including \(s\), have zero-extension Fourier transform \(O(1/|\xi|)\). The original high-frequency positive multiplier grows at most logarithmically, hence each lies in \(\operatorname{Dom}A_*\) by square-integrability of \((\log(2+|\xi|)/|\xi|)^2\). This permits the simplest trial space \(V\supset J\mathbb R^{470}\) for the strong-residual construction below; a smoother expanded trial space may be numerically preferable.

## 2. Exact entire 470-source resolvent identities, no guessed inverse entries

Take **any finite-dimensional real trial space** \(V\subset\operatorname{Dom}A_*\) containing the original \(J\mathbb R^{470}\), and let \(Z:\mathbb R^{470}\to V\) be its **full original \(A_*\)-Galerkin Riesz solve**
\[
V^*(J-A_*Z)=0.
\]
The full original positive pole-conditioned operator \(A_*\succeq\kappa_*I\) is strictly selfadjoint, with \(\kappa_*=33621/10^9\) from SI29, so this finite energy Galerkin solution exists and is unique. Introduce the **actual, complete source residual**
\[
R:=J-A_*Z
\]
(not the 890-source negative moment truncation residual). The entire original exact resolvent response is \(E=A_*^{-1}J=Z+A_*^{-1}R\). Because the Galerkin orthogonality gives \(Z^*R=0\), the TRUE ORIGINAL finite positive-resolvent Gram has the **exact matrix identity**
\[
\boxed{
\mathsf G:=J^*A_*^{-1}J
=Z^*A_*Z+R^*A_*^{-1}R.
}
\]
Thus, on the **entire** original 470-dimensional coefficient space,
\[
\boxed{
\mathsf G_0:=Z^*A_*Z
\preceq\mathsf G
\preceq\mathsf G_0+\kappa_*^{-1}\mathsf E,
\qquad \mathsf E:=R^*R.
}
\]
As \(V\) contains \(J\mathbb R^{470}\), \(\mathsf G_0\succ0\). All are **complete 470×470 coupled matrices**, not selected entries. The residual \(\mathsf E\) includes the actual full original positive-frequency and archimedean action \(A_*Z\); no positive window can be substituted for it.

## 3. Rigorous complete original negative response enclosure without \(A_*^{-1}\)

Let \(K_-\) be the **genuine entire** original seven-prime signed-negative odd operator (positive semidefinite). SI10/SM33's all-real 973 negative-frequency leaves give its **original full Hilbert-space bound**
\[
0\preceq K_-\preceq H_- I,\qquad H_-=2BM,\quad M=37.59565259375\ldots<38.
\]
For \(\mathsf N:=J^*A_*^{-1}K_-A_*^{-1}J=E^*K_-E\), set the actual trial negative matrix
\(\mathsf N_0:=Z^*K_-Z\succeq0\). The operator-valued weighted Young inequality, valid for **every** \(t>0\), yields
\[
\begin{aligned}
\mathsf N
&=(Z+A_*^{-1}R)^*K_-(Z+A_*^{-1}R)\\
&\preceq(1+t)\mathsf N_0+
 (1+t^{-1})R^*A_*^{-1}K_-A_*^{-1}R\\
&\preceq\boxed{
 (1+t)\mathsf N_0+
 (1+t^{-1})\,\frac{H_-}{\kappa_*^2}\,\mathsf E.}
\end{aligned}
\]
Again **every mixed source coefficient, high original resolvent response, whole-seven-prime negative real frequency and true original odd pole within \(A_*\)** are accounted for. The cross is bounded as a complete quadratic matrix, not silently discarded.

The actual full-frequency \(\mathsf N_0\) can if desired be **rigorously upper-enclosed without a new full-negative integral** using SM10:
\[
K_-\preceq U D U^*+\eta I
\quad\Longrightarrow\quad
\boxed{
\mathsf N_0\preceq\widehat{\mathsf N}_0:=
Z^*U D U^*Z+\eta Z^*Z,
}
\]
with all **890 original negative Taylor columns, all 107 original exact SPD moment blocks, all physical cross and complete \(\eta\) infinite residual**. This is a one-sided original operator inequality, not a claim that the cap is sharp enough to pass.

## 4. New fully coupled **measurable finite acceptance gate**

SM34 showed that the entire original odd spectral sign is nonnegative if
\(\mathsf N\preceq\theta\mathsf G\) on all \(470\) original sources, with \(\theta=51/56\); SM33's true original infinite complement correction is already priced by this margin.

The identities above yield the following **sufficient, complete-operator, residual-aware, finite matrix gate**:
\[
\boxed{
(1+t)\widehat{\mathsf N}_0+
 (1+t^{-1})\frac{H_-}{\kappa_*^2}\,\mathsf E
\preceq\frac{51}{56}\mathsf G_0
\qquad\text{on all }470\text{ original source coordinates},
}
\]
for **some certified rational \(t>0\)**. Here every matrix term has an unambiguous original physical definition; \(A_*Z\), \(Z^*A_*Z\), \(Z^*UDU^*Z\), \(Z^*Z\) and \(R^*R\) are measurable through their entire true original signed source integrals. The source-trial \(\mathsf G_0\) and \(\widehat{\mathsf N}_0\) can be assembled via **certified original 470-source Galerkin stiffness**, true physical positive pole-conditioned inverse solve and complete 890 negative moments. An exact/outward-rational **FULL 470×470 Loewner or generalized eigenvalue test**, not diagonal Gershgorin without full offdiagonal, is required.

If this gate passes, the original complete \(W_o\succeq0\) follows (under inherited original closed form/transfer premises). Failure is **inconclusive**: more accurate \(Z\), less conservative \(K_-\) bounds, a better \(t\), or exact finite energy-dual Schur may still succeed. This is a measurable constructive alternative to directly computing true \(\mathsf G,\mathsf N\), **not** a second proof of odd positivity.

**Precision reality:** with full-original scalar norm \(H_-=2BM=82.7104\ldots\) and \(\kappa_*=0.000033621\), the cheap \(t=1\) gate has residual coefficient \(2H_-/\kappa_*^2\) of order \(1.46\times10^{11}\). For instance, under the strong trial bound \(\widehat{\mathsf N}_0\preceq\theta\mathsf G_0/4\), it suffices additionally that
\[
\boxed{
\mathsf E\preceq\frac{\theta\kappa_*^2}{4H_-}\,\mathsf G_0
}
\]
with the rational coefficient approximately \(3.11\times10^{-12}\). **This is a conditional tolerance, not an achieved original residual.** It warns that naive scalar \(\kappa_*\) conditioning may render brute-force Galerkin impractical; sharper **weighted** residual response (e.g. negative-frequency-resolved) or direct corrected Schur might be needed.

## 5. What is actually proved and what SM36 must do

SM35's source-geometry replay checks the **exact** original 107 frequency clusters, 469 Taylor degrees and one pole generator, including positive and pairwise distinct original centers; the mathematical exponential-polynomial uniqueness gives full **470-dimensional** linear independence. Its exact rational finite test verifies the **whole-matrix** Galerkin identities and PSD enclosure, including a nonzero residual for which the gate passes and a near-defect where diagonal-only or small finite Ritz positivity does **not** certify the true full operator. It checks the above extreme original conditioning tolerance using actual original \(\kappa_*\), SI10 full negative mass and SM34 \(\theta\), not guessed parameters. All original operator sign flags stay OPEN.

**SM36 next acceptance:** construct and rigorously *evaluate* the true original \(V^*A_*V\) source stiffness and 470×470 Galerkin matrix, including the archimedean/logarithmic frequency tail and negative odd pole, plus a strict original full residual \(R^*R\) and full SM10 890-column source cap \(Z^*UDU^*Z+\eta Z^*Z\). Then certify the entire residual-aware 470D matrix Loewner gate (or use tighter resolvent-weighted residual), not its partial windows or a toy demonstration. The earlier PS36 even/odd original complete-operator acceptance remains invariant. Full W-ODD-NEG O1/O2, original even E1–E4, whole signed Weil, native CC27 D-Riesz and RH remain **OPEN**. Independent analytical audit of source independence and original Hilbert/operator domain is required.

Replay: \`python3 scripts/validate_rpb108_sm35_full_original_resolvent_galerkin_enclosure.py\`.
