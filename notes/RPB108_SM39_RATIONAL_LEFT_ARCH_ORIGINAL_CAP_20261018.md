# SM39 — Original seven-prime signed multiplier: rational LEFT-endpoint arch bound with full moment-cap custody

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM38 draft PR #220 (final-head focused CI PASS).**

## Motivation: SM38 identified the *source* of the numerical inflation

SM38 integrated the actual original supported odd 25-source sine Fourier transform on every one of the **3892 original SI10/SM37 signed-negative frequency subcells**, applying Gauss 4/8/16 to the original seven-prime signed multiplier. SAME 25-source selected and uncertaified sampled positive \(A_*\) trial gave direct negative generalized maxima **0.964650/0.972929**, yet the certified SM37 real-frequency signed-envelope-only generalized maxima were **9.817182/9.975612**, ≈**10.2× larger**. Original SM37 107-block/890-column moment cap increased those envelope maxima by only \(\sim1/1024\). Thus the mathematically useful next adjustment is to tighten the **whole-real original signed multiplier envelope**, retaining the well-performing Taylor/moment source factorization.

**SM39 result to certify:** improve the original SI07 archimedean interval lower at each **rational frequency subcell's actual left endpoint**, rather than keeping the lower frozen at the parent unit interval's integer floor.

## 1. Whole-original seven-prime signed real-frequency lower

The actual original Fourier signed multiplier is
\[
m(\xi)=\Re\psi(\tfrac14+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\log p(n)}{\sqrt n}\cos(2\pi\xi\log n).
\]
On \(\xi\ge0\), the true archimedean term \(\mathcal A(\xi):=\Re\psi(1/4+i\pi\xi)-\log\pi\) is **strictly increasing** away from zero. Indeed, the convergent digamma identity, with \(a=1/4\), gives
\[
\mathcal A(\xi)=\psi(a)-\log\pi+
\sum_{k=0}^\infty\frac{(\pi\xi)^2}{(k+a)((k+a)^2+(\pi\xi)^2)},
\]
and every individual term is nondecreasing as \(\xi\) grows; the derivative is positive for \(\xi>0\).

The already accepted SI07 exact rational lower \(\operatorname{arch}_{\rm SI07}(j)\) was initially evaluated at **integer** \(j=\lfloor \xi\rfloor\), using the valid conservative \(\underline\pi=333/106\), 64 positive rational digamma terms, a monotone integral tail lower (the inherited exact \(\log_{\rm lo}\)), and the unchanged SI06 upper on \(\psi(1/4)-\log\pi\). All parts are valid for **any nonnegative rational frequency** \(a\), so define:
\[
\begin{aligned}
y&=\underline\pi a,\quad a_0=\tfrac14,\quad K=64,\\
\boxed{
\operatorname{arch}_{\rm lo}(a)
=\sum_{k=0}^{63}
\frac{y^2}{(k+a_0)((k+a_0)^2+y^2)}
+\frac12\log_{\rm lo}\!\left(1+
\frac{y^2}{(K+a_0)^2}\right)
-C_{\rm up}.}
\end{aligned}
\]
In particular, if a genuine original signed-negative frequency subcell is \([a,b]\subset[j,j+1]\),
\[
\operatorname{arch}_{\rm lo}(a)\ge
\operatorname{arch}_{\rm lo}(j),\qquad
\mathcal A(\xi)\ge\operatorname{arch}_{\rm lo}(a)
\quad\text{for every actual real }\xi\in[a,b].
\]

For the exact original seven-prime component, keep the **existing SI06 full original prime midpoint interval** and whole-cell derivative 69. For all true real \(\xi\in[a,b]\),
\[
\boxed{
m(\xi)\ge
L_{[a,b]}=
\operatorname{arch}_{\rm lo}(a)
+\operatorname{prime}_{\rm SI06,lo}((a+b)/2)
-\frac{69}{2}(b-a).
}
\]
No raw float sample can replace this inequality. The original SI06 high-frequency positive signed region \(|\xi|\ge896\) and every other SI10 certified-positive region are inherited unchanged.

## 2. Preserve original full signed source and exact whole-operator upper order

Start from **all the original SM37 3892 certified signed subcells**, with their already certified original positive step weights \(w_{37}\). On each original \([a,b]\), set:
\[
w_{39}=\min\!\left\{
w_{37},\;
\max\!\left(10^{-6},
10^{-6}\big\lceil10^6(\kappa-L_{[a,b]})_+\big\rceil
\right)\right\},\qquad \kappa=\tfrac1{1000}.
\]
Because both \(w_{37}\) and the second independently certified outward rational step dominate **the entire true original \((\kappa-m(\xi))_+\)** on \([a,b]\), the minimum does too. Strict \(w_{39}\ge10^{-6}>0\) preserves all true 107 moment covariance blocks SPD.

The exact signed-frequency reflected mass is computed across **the same 973 leaves/3892 subcells**. SAME 107 original true cluster boundaries/centers and 890 sine-Taylor physical source generators are used, with the full 24-bit residual \(\eta_{39}\) recalculated from the new weight mass. The script computes all 107 full rational covariance Hankel moments, pays **all 890 exact strict LDL pivots**, and establishes the full quadratic-form Loewner chain
\[
\boxed{
0\preceq K_{\neg,o}
\preceq\widehat K_{\rm SM39}
\preceq\widehat K_{\rm SM37}
\preceq\widehat K_{\rm SM10}.
}
\]
In particular this is a *full original negative-frequency operator bound under inherited Fourier identification*, not merely reduced source diagonal arithmetic. It **does not** establish the sign of the **complete original signed odd Weil operator** \(W_o=A_*-K_{\neg,o}\).

## 3. Matched pilot: what it measures and what it cannot

SM39 rebuilds the SAME original SM36/SM38 genuine 25 supported odd physical source trial, with the same sampled positive/pole-conditioned \(A_*\) coefficients \(Z\) (still **NOT certified**: full positive digamma/log-frequency tail and strong residual are missing). For physical grids \(4096\)/\(8192\) with independent FFT positive quadrature padding, compare:
- SM37 original signed-envelope-only 25×25 source Fourier Gauss matrix;
- NEW SM39 signed-envelope-only 25×25 matrix at exactly the **same** 3892 original subcells, with analytic supported sine transforms and Gauss16;
- Original SM37 890-source 107-block Taylor/Young covariance cap on the same \(Z\);
- NEW SM39 complete 890-source cap on the same \(Z\).

These float64 source generalized eigenvalues are **engineering diagnostics only**. Any improvement is descriptive; a failure to close the SM34 \(51/56\) sufficient gate, or a sampled value exceeding one, does **not** prove a true negative original eigenvalue. A tiny negative sampled cap-minus-envelope Loewner residual is likewise not a genuine counterexample to the exact original operator envelope proof; physical source quadrature and roundoff remain.

## 4. Next frontier is determined by measured effectiveness

If exact SM39 rational signed mass and physical source-weighted 25×25 envelope improve decisively, continue sharpening the most influential **source-weighted original negative subcells**, preferably with exact local prime derivative bounds rather than further uniform subdivision. If integer-floor-to-left arch barely helps, identify the **dominant inherited whole-real signed-multiplier slack**, especially the global SI06 **69** derivative paid across EVERY subcell even when the actual local signed-prime slope is small. A narrow exact seven-prime *per-subcell derivative* interval would then be the appropriate SM40 input.

Independently, the real original positive \(A_o\) digamma logarithmic high-frequency tail, full 470-source \(A_*^{-1}\) strong residual and complete original generalized \(51/56\) test remain completely **OPEN**.

**Custody:** no original W-ODD-NEG O1/O2 sign certificate, original even E1–E4 positivity, whole Weil positivity, native CC27 D-Riesz or RH promotion. Exact rational interval tests still require independent original Fourier/closed-form-domain analysis.

Replay: \`python3 scripts/validate_rpb108_sm39_rational_left_arch_cap.py\`; output in \`artifacts/sm39_original_rational_left_arch_cap.json\` keeps source-certified rational values separate from **NONCERTIFYING** sampled pilot Ritz.
