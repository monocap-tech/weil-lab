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


## First SM39 fully scoped exact-rational outcome — real breakthrough in cap efficiency

The initial focused GitHub Actions run **39173765061 PASSED** on the original SI10/SM37 **3892 rational signed-real frequency subcells**, original complete seven-prime SI06 signed midpoint bounds, rational SI07 left-endpoint digamma arch, all 107 original cluster moment covariances, **all 890 exact rational SPD LDL pivots**, and the full original 24-bit Taylor-infinite residual.

| Whole-original signed-negative cap quantity | SM37 | SM39 | Improvement |
| --- | ---: | ---: | ---: |
| **Original complete signed envelope mass** | 27.227999359375 | **18.73146440625** | **−8.496534953125 (−31.205%)** |
| True entire Taylor error residual η | 2.181335594123035e−10 | **1.500646797442107e−10** | **−31.205%** |
| Strictly improved signed-real subcells | — | **2728 of 3892** | Original certified genuine real intervals |
| Physical sine-Taylor source columns | 890 | **890 unchanged** | No dropped source directions |
| Entire rational covariance LDL pivots | 890 | **890 strict positive** | Every original cross paid |

The original full-negative **operator-level** enclosure strengthens:
\[
0\preceq K_{\neg,o}
\preceq\widehat K_{\rm SM39}
\preceq\widehat K_{\rm SM37}
\preceq\widehat K_{\rm SM10}.
\]
SM39's strict full signed cap weight reduction is a rational operator-certificate outcome (conditional on inherited true original Fourier/domain premises), not a sampled eigenvalue. Following this first PASS, the validator was strengthened to require **exact Fraction**:
\[
\boxed{
T_{39}<\frac{7}{10}T_{37},\qquad
T_{37}-T_{39}>8,\qquad
\#\{\text{strictly improved true subcells}\}>2700.
}
\]
Those are **new final-head** checks whose separate CI rerun must be verified.

### SAME original 25-source selected trial — spectacular spectral response

| Generalized spectral maximum, same selected approximate original 25-source \(A_*\)-Galerkin solve | Grid 4096, pad×4 | Grid 8192, pad×8 |
| --- | ---: | ---: |
| **SM38 direct source-analytic leafwise original true-formula Kneg** | 0.964650 | 0.972929 |
| SM37 old original certified signed-envelope-only | 9.817182 | 9.975612 |
| **NEW SM39 original certified signed-envelope-only** | **1.109610** | **1.125944** |
| SM37 old full 890-source covariance/Young cap | 9.826764 | 9.985352 |
| **NEW SM39 full 890-source covariance/Young cap** | **1.110693** | **1.127044** |
| True **sufficient 470-source** acceptance \(\theta=51/56\) | 0.910714 | 0.910714 |

The SM39 full 890-source cap selected-source generalized maximum is **88.70% lower** than SM37 in the SAME sampled trial. This is a much larger source-weighted gain than its 31.2% global mass reduction, emphasizing the value of **original-frequency-specific** rigorous arch estimates.

The SM39 trial cap is now only about **1.151×** (4096) / **1.158×** (8192) the SAME SM38 leafwise direct selected-source negative response, rather than SM37's ≈10.2×. The **remaining discrepancy is a practical local certificate target**, not a proof that the whole odd operator has crossed its critical generalized spectral gate. Both the selected direct \(\sim0.965–0.973\) and its new conservative cap \(1.11–1.13\) remain ABOVE the sufficient threshold \(51/56\sim0.911\). The SM34 gate itself is sufficient, not necessary; failure does **not** establish original Wodd negativity.

The sampled new moment cap minus envelope-only matrix had a small negative minimal eigenvalue \(-3.70\times10^{-6}\) at grid4096 and \(-2.16\times10^{-7}\) at grid8192. This is a **numerical physical-grid quadrature discrepancy**, consistent with SM38; the strict true original rational pointwise cap / whole-form Loewner order was proved independently under inherited premises. **Do not promote these sampled eigenvalues to certified original spectrum**.

### SM40 now has a better-informed target

Further improvement should attack the residual **~15–16% original cap-to-direct selected-source inflation** by refining the **SI06 original seven-prime derivative allowance 69** to rigorous *local* derivatives on each original rational signed subcell, with exact log/π/√n sin/cos ranges and complete real interval coverage. That may improve the full accepted negative cap without modifying the original 890 sine-Taylor source factoring. In parallel, certify the original positive archimedean logarithmic high-frequency tail and actual all-470 source pole-conditioned \(A_*\) inverse strong residual. No substitute 25-source Ritz sample may close complete O1/O2, even E1–E4, whole signed Weil, CC27 or RH.

**Run status:** first genuine-source exact-rational cap and sample benchmark CI 39173765061 PASSED. Post-run strengthened exact-source and scoped numerical thresholds **require an independent final-head CI replay**, which must be reported accurately.
