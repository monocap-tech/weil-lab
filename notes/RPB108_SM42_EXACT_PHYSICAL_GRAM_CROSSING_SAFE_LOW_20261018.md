# SM42 — Actual ORIGINAL selected odd physical Gram and crossing-safe positive low-band gate

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM41 PR #223 (final head focused CI PASSED).**

SM41 proved an actual original odd-source positive **HIGH** frequency digamma/seven-prime log-multiplier tail, but only **numerically** approximated the \(25\times25\) source-positive **LOW** band. A 0.0182% Gauss8/16 difference is **not** an outward integration error. SM42 therefore addresses the missing exact *physical Gram*, actual odd pole/source matrix, and an honest whole-real \(m=\kappa\)-crossing-safe low-band analytic envelope, without promoting unverified Gaussian quadrature.

### 1. Exact full original supported source Gram (25×25, not a toy)

The original SI10 selected physically supported odd generators \(g_i\) are 16 \(\sin(2\pi c_jx)\), eight \(x\cos(2\pi c_jx)\), and the true \(\sinh(x/2)\), all zero-extended from \(I=[-11/10,11/10]\). Original exact cluster centers \(c_j=(a_j+b_j)/2\) are rational and unchanged.

Define for rational \(q\),
\[
F_0(q)=\int_{-B}^B\cos(2\pi qx)dx,\qquad
F_1(q)=\int_{-B}^Bx\sin(2\pi qx)dx,\qquad
F_2(q)=\int_{-B}^Bx^2\cos(2\pi qx)dx.
\]
For \(w=2\pi q\), exact elementary antiderivatives are
\[
F_0(q)=2\sin(wB)/w,\qquad
F_1(q)=2[\sin(wB)-Bw\cos(wB)]/w^2,
\]
\[
F_2(q)=2[B^2\sin(wB)/w+2B\cos(wB)/w^2-2\sin(wB)/w^3],
\]
with removable \(q=0\) values \(2B,0,2B^3/3\). Sin-sin Gram uses \([F_0(c_i-c_j)-F_0(c_i+c_j)]/2\), \(x\cos\)-\(x\cos\) uses \([F_2(c_i-c_j)+F_2(c_i+c_j)]/2\), mixed sin and \(x\cos\) uses \([F_1(c_{\sin}+c_{x\cos})+F_1(c_{\sin}-c_{x\cos})]/2\), retaining EVERY cross.

For true original pole \(s=\sinh(x/2)\) the sin-source cross is
\[
\int_{-B}^B s(x)\sin(wx)dx
=\frac{2[\frac12\cosh(B/2)\sin(wB)-w\sinh(B/2)\cos(wB)]}{\frac14+w^2}
\]
and its derivative in \(w\) equals the \(x\cos\) source cross. The pole-pole entry is exactly
\[
\boxed{\langle s,s\rangle=\sinh(B)-B}.
\]

The validator bounds \(\pi\) by SI06 exact rational PI, reduces every original source phase \(\pi\)-periodically by an exact nearest-integer rational period, evaluates sine/cos Taylor through degree 35/34 with exact rational remainder and outward \(10^{-12}\), and independently encloses \(\sinh(B/2),\cosh(B/2),\sinh(B)\) by monotone rational Taylor with provable positive tail. It produces **the entire original physical 25×25 interval matrix** \(H\).

To rigorously prove this true original matrix is positive definite, a floating Cholesky is used **only to propose** a rational preconditioning matrix \(Q\). Every source interval entry is rounded to exact integer denominator; the full \(25\times25\) rational congruence \(Q^THQ\) is checked by a strict **exact Fraction Gershgorin bound paying the entire interval-entry error**. No floating eigenvalue is accepted as an original proof, and no physically supported generator is discarded. This does NOT certify full 470-source Gram.

### 2. Exact original low-band operator sandwich and crossing-safe smoothing

The true positive original multiplier is \(a_o(\xi)=\max(\kappa,m(\xi))\), \(\kappa=1/1000\), with genuine unbounded digamma+all seven original signed prime powers. At crossings \(m(\xi)=\kappa\) this has a kink. Define an analytic smoothing for any positive rational \(\varepsilon\):
\[
a_\varepsilon(\xi)=\kappa+
\frac{(m(\xi)-\kappa)+
\sqrt{(m(\xi)-\kappa)^2+\varepsilon^2}}2.
\]
The pointwise identity
\[
0\le\sqrt{x^2+\varepsilon^2}-|x|\le\varepsilon
\]
proves the TRUE original complete operator form comparison
\[
\boxed{
0\preceq A_\varepsilon-A_o\preceq\frac{\varepsilon}{2}H
}
\]
on the whole genuine physical source space. At \(\varepsilon=2^{-20}\), the coefficient \(\varepsilon/2=2^{-21}<10^{-6}\) is **exact rational**. This removes the *logical requirement to isolate every m=κ root* before bounding the regularized positive source integral, but the latter still needs rigorous quadrature/error.

A second, conservative **whole-original positive LOW-band Loewner** result holds independently of numerical Gauss. For \(0\le|\xi|\le\Lambda=4096\), arch monotonicity plus SM41's high original positive upper yields \( \kappa\le a_o(\xi)\le17+\log\Lambda\). With physical source Gram \(H\), band-frequency Gram \(H_{\le\Lambda}\), and the genuine original selected-source high-frequency unweighted Parseval bound \(H_{>\Lambda}\preceq(2E/\Lambda)I_{25}\) (SM41 \(E=202/25\)):
\[
\boxed{
\kappa\left(H-\frac{2E}{\Lambda}I_{25}\right)
\preceq A_{o,\le\Lambda}
\preceq(17+\log\Lambda)H.
}
\]
The positive-form HIGH tail is separately certified by SM41 \(\delta_A(4096)=0.1038721875 I_{25}\), so this is a valid albeit very **loose** complete original 25-source positivity-form bracket. It is NOT a numerical quadrature enclosure of SM41's sampled Gauss stiffness \(G\), not a certified Astar inverse, and it cannot close the spectral sign.

### 3. Actual acceptance / remaining mathematics

Scoped SM42 verification requires full 25×25 original physical source Gram/pole entries enclosed in rational intervals, **strict whole-matrix exact positive definiteness** after rational preconditioning, correct crossing-safe analytic smoothing/error \(\varepsilon/2\), and the broad original low-frequency multiplier Loewner. None of these findings is a proof of **entire signed original odd** \(W_o=A_o-2|s\rangle\langle s|-K_{\neg,o}\).

SM43 should build a **useful sharp outward low-band source-analytic digamma/seven-prime quadrature** on the now-certified physical source coordinates. It may use the regularized \(a_\varepsilon\) to avoid explicitly isolating all crossings, provided derivative/interval quadrature of that smooth weight is rigorously paid, including SI06 coefficient and source trigonometric errors. Combine exact low with SM41 positive high tail, certify true positive \(A_*\) rank-one update and 25-source strong residual, then derive full 470-degree original source-specific transformed Fourier tail and preconditioned complete source test. Do not mistake 25-source Gram or coarse low band for a full original odd O1/O2, original even E1-E4, Weil positivity, CC27 D-Riesz or RH proof. All OPEN.

Replay \`python3 scripts/validate_rpb108_sm42_original_physical_gram_and_low_gate.py\`, which writes an exact rational certificate JSON in \`artifacts/sm42_exact_original_25_source_gram_and_low_gate.json\`. Independent original zero-extension/Fourier-domain analytic audit remains a separate acceptance condition.


## Verified first original-source physical Gram run

**Focused GitHub Actions run 39177662612 completed SUCCESS.** The actual true original SI10 selected physical Gram source set consists of 25 distinct generators, including the full odd pole and 24 original non-pole sin/xcos directions. The whole original **25×25 Gram** entry enclosures were generated by rational \(\pi\), period-reduced sine/cos Taylor, hyperbolic Taylor, and exact rational integral formulas; strict positive definiteness was verified on **the complete coupled matrix** (no diagonal-only inference) via a numerically proposed but rationally rounded source congruence followed by exact Fraction interval-error Gershgorin.

The minimum **preconditioned matrix** Gershgorin diagonal-minus-row-sum margin after paying every original interval entry error is **0.9999926719198836**. This is a lower bound for \(Q^{T}HQ\) in those rational preconditioned coordinates, **not** a claim that the raw true source \(H\) has minimum eigenvalue 0.99999 or that the weighted original \(A_o\) or \(A_*\) is uniformly coercive. The pole-pole entry is the actual exact \(\sinh(11/10)-11/10\), enclosed in the artifact by two explicit rational fractions.

A complete unconditional true-original **coarse** positive source lower/upper holds at \(\Lambda=4096\):
\[
\boxed{
\frac1{1000}\left(H-\frac{101}{25600}I_{25}\right)
\preceq A_{o,\mathrm{low}}
\preceq\left(17+\frac{1041}{125}\right)H.
}
\]
Here \(\frac{101}{25600}=\frac{2E}{4096}\) with actual original selected \(E=202/25\), and the \(\log\Lambda\) upper is the exact rational SI06 outward \(1041/125\). This is a true low-frequency original *operator* sandwich with no numerical quadrature, but it is intentionally **much wider than the actual original sampled source stiffness**, so it is not sufficient for source-resolvent inversion, a useful \(51/56\) cap comparison, or original W-ODD-NEG closure.

The exact softplus smoothing at \(\epsilon=2^{-20}\) has full-original crossing error bounded in Loewner order by
\[
\boxed{0\preceq A_\epsilon-A_o\preceq \frac1{2097152}H.}
\]
This mathematical replacement does not require isolated individual crossings \(m(\xi)=\kappa\), but the smooth weighted low-band still needs rigorous outward quadrature.

**SM43 real next calculation:** tighten the low source-form matrix, retaining this certified true physical Gram and optional softplus crossing fee, with a reproducible *validated numerical quadrature error budget*. The original 25 source \(A_o\) positive *high* form tail from SM41 at 4096 remains \(0.1038721875 I_{25}\); do not confuse it with the unweighted high \(L^2\) fee \(101/25600 I_{25}\) used in the coarse lower. Full original 470 source Gram/conditioning and actual pole-conditioned inverse/strong residual remain OPEN. Complete original odd/even Weil/RH not proved by this CI.
