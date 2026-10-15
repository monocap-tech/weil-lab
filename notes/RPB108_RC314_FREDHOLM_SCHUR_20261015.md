# RC314 — Fredholm localization and a residual-corrected rank-301 signed Schur contract

**Parent:** RC313 merged at \`f89fef4ae8a53c37015d9efc0ecc8ad5a05cd643\`.  
**Starting mathematical input:** RC313 identifies the complete bounded \(D\)-Riesz representative of the pinned original CC27 signed Weil form on its supported polynomial core.  
**Status:** the form's nonpositive spectral directions are **finite-dimensional**, but their absence is *not* certified. Stage I, signed inverse, F4 and RH remain OPEN.

## 1. Why boundedness is not the same as a positive lower spectral bound

RC313 discharged the remaining prime/pole source-identification gap, so the operator to study is no longer merely a conditional proxy. With the physical Legendre harmonic metric

\[
D_sP_n=(H_n+s)P_n,\qquad s>3,
\]

write the original form on the \(D\)-normalized Hilbert representation as

\[
\boxed{N_0=I+A+K},
\quad
A=D_s^{-1/2}hD_s^{-1/2}\succeq0,
\quad
K=D_s^{-1/2}(P-K_{\rm reg}+K_{\rm pole}-rI)D_s^{-1/2},
\]

where \(h(t)=-\tfrac12\log(1-t^2)\ge0\), \(r=789/125\), and \(P\) is the **signed** seven-prime physical source.

RC309–311 bound the endpoint term as a \(D\)-form operator, so \(A\) is **bounded and positive**. RC307, RC308 and RC313 bound the other physical source components, so \(S=P-K_{\rm reg}+K_{\rm pole}-rI\) is a bounded selfadjoint operator on physical \(L^2\).

Because \(H_n+s\to\infty\),

\[
D_s^{-1/2}\colon L^2\to L^2
\]

is **compact** in the physically orthonormalized Legendre basis. Consequently \(K=D_s^{-1/2}SD_s^{-1/2}\) is compact and selfadjoint. The previously certified complete \(D\)-action is therefore a bounded selfadjoint positive operator \(I+A\) plus a compact signed perturbation.

**Weyl's essential-spectrum theorem gives**

\[
\boxed{\sigma_{\rm ess}(N_0)\subset[1,\infty).}
\]

The original operator is selfadjoint Fredholm with index zero. Its nonpositive spectrum consists of finitely many isolated eigenvalues of finite multiplicity (or none). This is a structural spectral result, **not positivity**: finite negative eigenvalues or a zero mode can still exist.

## 2. How many directions can possibly be nonpositive?

A crude new decomposition uses the tighter original prime physical \(L^2\) norm from RC313, the regular-kernel norm from RC308, the strictly positive even pole, and the strictly *negative* odd pole.

For even inputs the lower perturbation constant may omit the positive even pole:

\[
\lambda_{\rm even}=r+\|P\|+\|K_{\rm reg}\|.
\]

For odd inputs, charge the actual negative pole eigenvalue:

\[
\lambda_{\rm odd}=\lambda_{\rm even}+2(\sinh B-B).
\]

Since \(h\ge0\), in the high parity subspace beginning at source degree \(m\),

\[
\langle q,N_0q\rangle_D
\ge\left(1-\frac{\lambda_{\rm parity}}{H_m+s_{\rm lower}}\right)
\|q\|_D^2.
\]

RC314 calculates the first admissible cutoffs using *outward-rounded* harmonic sums; it keeps the signed pole contribution rather than paying the large positive even-pole eigenvalue as a negative fault.

These new standalone norm estimates are intentionally conservative. The **stronger** RC283 global form lower estimates already established positive high complements after:

- even degree 232, excluding only the first **116 even** basis modes;
- odd degree 371, excluding only the first **185 odd** basis modes.

The exact RC283 positive high-complement floors are rechecked against their canonical pinned source data. Since any nonpositive subspace must inject into the 116+185-dimensional low projection, the original form's total nonpositive Morse index satisfies

\[
\boxed{\operatorname{dim}E_{(-\infty,0]}(N_0)\le301}.
\]

This index bound is **not** an assertion that all 301 eigenvalues are nonpositive. It only locates where a potentially negative direction could be encoded, including arbitrary mixing with its (positive) high-mode response.

For computation, the buffered **rank 317** reference remains more attractive: its certified high-complement \(D\)-coercivity floor is much stronger than the minimally positive rank-301 floor. The minimum rank sharpens the theoretical dimension count, but sacrifices inverse conditioning. Do not silently substitute one reference's inverse for the other.

## 3. Exact finite Feshbach/Schur reduction and the sign of the correction

Let \(P\) project onto the first 116 even plus 185 odd \(D\)-orthogonal modes, and \(Q=I-P\). Write

\[
N_0=\begin{pmatrix}B&T^\ast\\T&C\end{pmatrix},
\qquad C=QN_0Q\succeq\mu I,\quad\mu>0.
\]

Since the complement is positive, positivity of the **entire original Weil form** is equivalent to positivity of the 301-dimensional Schur operator

\[
S_{301}=B-T^\ast C^{-1}T.
\]

For any explicitly constructed approximate high response \(Y\colon P\mathcal H_D\to Q\mathcal H_D\), define the actual signed residual

\[
R=T-CY.
\]

The following is an **exact operator identity**, not a heuristic norm estimate:

\[
\boxed{
S_{301}=B-T^\ast Y-Y^\ast T+Y^\ast CY
           -R^\ast C^{-1}R.}
\]

The residual correction is SUBTRACTED. Since \(C\succeq\mu I\),

\[
S_{301}\succeq
B-T^\ast Y-Y^\ast T+Y^\ast CY
-\frac1\mu R^\ast R.
\]

**An executable sufficient acceptance test** is positivity of the latter explicitly computable finite block, after all native operator, tail, interval, approximation and residual errors have been paid in the \(D\)-metric. The converse is not asserted for an approximate \(Y\). The script independently checks the exact identity and Loewner correction on a non-diagonal rational block system with nonzero residual, preventing a wrong-sign implementation.

No actual 301-dimensional response \(Y\), principal Schur block or signed residual matrix is computed in this checkpoint; consequently **the positivity test remains unpassed**. This is not interchangeable with the earlier RC292 rank-317 conditional *auxiliary source* test, though both are exact Schur reductions.

## 4. Numerical conditioning and an important upper-bound caveat

RC313's new all-component norm bound is **not necessarily sharper** than the better global reference upper from RC292. RC314 explicitly compares them and retains the smaller previous upper for Chebyshev planning, instead of pretending the stronger source identification automatically improves every operator-norm estimate.

The RC283 floors confirm the tradeoff between the rank-301 theoretical index localization and the rank-317 buffered inverse construction. Future numerical work should use whichever one minimizes the full certified residual cost, with exact reference custody preserved.

## 5. RC315 — actual signed positivity calculation

The next genuine advancement is a **new source-action computation**, not another abstract identity: construct \(Y\) for the buffered 317 or minimum 301 original high-complement Schur block; certify the full original \(C Y\) and \(T\) actions; compute their signed cross correlations and the complete residual Gram; prove or obstruct the strict Schur lower inequality.

Only a *positive paid finite Schur witness* would imply full original Weil positivity. The essential-spectrum theorem and index bound do not establish Stage I, F4 or RH, nor do they independently transport positivity across every proposed zero divisor/null carrier.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc314_fredholm_schur.py --output certificates/rpb108_rc314_fredholm_schur.json
python scripts/validate_rpb108_rc314_fredholm_schur.py --output certificates/rpb108_rc314_fredholm_schur.json --replay
\`\`\`

This checkpoint depends on the pinned CC27/RC313 source-identification theorem, RC283 global lower forms, and standard Weyl compact-perturbation and Schur complement theorems. Exact GitHub Actions replay verifies the rational certificate and all source pins, not an independently peer-reviewed RH proof.
