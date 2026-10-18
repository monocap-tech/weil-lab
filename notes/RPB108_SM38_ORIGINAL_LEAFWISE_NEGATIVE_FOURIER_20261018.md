# SM38 — Original odd negative-frequency leafwise Fourier quadrature and attribution of remaining cap inflation

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM37 draft PR #218 (exact original complete negative cap final-head CI PASS).**

## Mathematical distinction: what is certified vs newly explored

SM37 **rigorously** improved the complete original seven-prime negative-frequency operator upper by refining all 973 original potentially negative real-frequency leaves into 3,892 exact-rational signed subcells, keeping the same 107 clusters, all 890 original sine-Taylor physical source columns and entire infinite Taylor residual. All 890 strict rational LDL checks passed. The true operator inequality remains
\[
0\preceq K_{\neg,o}\preceq\widehat K_{\rm SM37}
\preceq\widehat K_{\rm SM10}.
\]
SM37's matched 25-source FLOAT pilot found max generalized Ritz for new cap \(\approx9.827\)–\(9.985\), vs a coarse-FFT direct signed-negative response \(\approx0.997\)–\(1.000\). **Neither number is a rigorous operator spectral estimate.**

SM38 does **not** turn that selected Ritz block into whole-odd positivity. It replaces the unreliable FFT **negative-frequency integration reference** by **direct Gauss-Legendre integration over the entire original signed-negative real-leaf support** using *analytically evaluated true physically supported Fourier sine transforms*, with independent quadrature order checks. All new quadrature and eigenvalues are **NUMERICAL / NONCERTIFYING**. The original bounded-negative cap remains valid by inheritance; positive original digamma arch full logarithmic tail, original 470-source resolvent, genuine strong residual, and complete \(W_o\succeq0\) remain OPEN.

## 1. Exact continuous physical Fourier amplitudes for the selected ORIGINAL source functions

For the original odd physical Hilbert space \(I=[-B,B]\), \(B=11/10\), and frequency \(\xi\ge0\), define
\[
\mathcal F_s[f](\xi)=\int_{-B}^{B}f(x)\sin(2\pi\xi x)\,dx,
\qquad
\langle f,K_{\neg,o}g\rangle
=2\int_0^\infty (\kappa-m(\xi))_+\,
\mathcal F_s[f](\xi)\mathcal F_s[g](\xi)\,d\xi.
\]
Because each original selected \(f\) is odd, its ordinary zero-extended Fourier transform at \(\xi\) is \(-i\mathcal F_s[f](\xi)\); the factor **2** accounts for positive and negative frequencies. This is the same original physical normalization as the SM10 signed sine-Taylor source cap.

The SM36/SM37 fixed 25-source pilot contains **actual original SI10 exceptional generators** of degrees 0 and 1:
\[
f_{c,0}(x)=\sin(2\pi c x),\qquad
f_{c,1}(x)=x\cos(2\pi c x),
\]
for genuine seven-prime signed source cluster centers \(c\), plus the ORIGINAL odd pole vector \(s(x)=\sinh(x/2)\).

Use the exact entire real physical sine product
\[
S(t):=\frac{\sin(2\pi Bt)}{2\pi t}
=B\,\operatorname{sinc}(2Bt).
\]
Then for every original physical frequency \(\xi\), without frequency discretization,
\[
\boxed{
\begin{aligned}
\mathcal F_s[f_{c,0}](\xi)&=S(c-\xi)-S(c+\xi),\\
\mathcal F_s[f_{c,1}](\xi)&=\frac{S'(c-\xi)-S'(c+\xi)}{2\pi},\\
\mathcal F_s[s](\xi)&=
\frac{2\left[
\frac12\cosh(B/2)\sin(2\pi B\xi)
-2\pi\xi\sinh(B/2)\cos(2\pi B\xi)
\right]}{\frac14+(2\pi\xi)^2}.
\end{aligned}}
\]
The derivative uses its correct odd Taylor series near resonance to avoid subtractive cancellation. The script independently cross-checks these original exact-formula expressions against **SciPy oscillatory-weight physical quadrature** at low, intermediate and remote original frequencies; this is a consistency check and not an outward interval proof.

For the **same** selected-source trial coefficients \(Z\) (obtained from the SM36 sampled positive-pole-conditioned Galerkin solve), all 25×25 couplings are computed by a single matrix multiplication at quadrature nodes:
\[
N_{\rm leafwise}^{(q)}
=2\sum_{\ell\in\mathrm{SI10}\ 973\ \mathrm{leaves}}
\sum_{r=1}^q \omega_{\ell,r}
(\kappa-m(\xi_{\ell,r}))_+
\,\bigl(\mathcal F_sV(\xi_{\ell,r})Z\bigr)^*
\bigl(\mathcal F_sV(\xi_{\ell,r})Z\bigr).
\]
This **numerical** original integral never relies on FFT frequency bins. The original seven-prime m is evaluated at actual Gauss nodes. Its negative spectrum is inherited supported only on the SI10 unresolved leaves; this truncation concerns **negative frequencies alone**, not the positive arch tail.

## 2. Three-way *matched* signed negative/cap attribution on unchanged actual source trial

In addition to direct original signed-negative \((\kappa-m)_+\), compute its matrix response on the **same exact-formula physical sine amplitudes** with:
1. The full original **SM10 old whole-leaf envelope** \(w_{\rm old}(\xi)=\kappa+h_\ell\) constant on each original leaf.
2. The proven **SM37 new whole-real 3,892-subcell envelope** \(w_{\rm new}(\xi)\le w_{\rm old}(\xi)\) pointwise.
3. The physical-source **SM37 full 890-column Taylor/Young/eta upper cap**, evaluated using the *same* positive trial coefficients.

Thus the numerical same-trial spectral ladder separately tests:
\[
N_{\rm direct\ leafwise}
\preceq N_{\rm envelope\ new}
\preceq N_{\rm envelope\ old},
\quad
N_{\rm envelope\ new}
\preceq\widehat N_{\rm 890\ Taylor+Young+\eta}.
\]
The underlying **operator** envelope inequalities are rigorously inherited from SI06/SM10/SM37; the newly computed numerical matrix comparisons are **diagnostic**, and any substantial contradiction indicates an implementation/normalization problem requiring investigation.

This separation identifies whether the remaining ≈9.9× cap inflation arises mainly from:
- a coarse FFT direct reference (SM36/SM37 frequency steps 0.114 and 0.057, much wider than SI10 leaf 1/64=0.015625 or SM37 cell 1/256=0.00390625);
- conservatism of the genuinely original whole-real signed negative envelope **at the weighted physical response level**;
- additional original Taylor/moment covariance + Young/infinite-error cap inflation above that envelope.

The test reports generalized maxima from the same trial \(G_0=Z^*A_*^{\rm sampled}Z\). It cross-checks direct numerical quadrature orders 8, 16 and 32 **on every one of the 973 original leaves**, and same-order Gauss over all 3,892 refined cells for the new envelope. It also varies physical FFT grid \(4096,8192\) and zero padding 4×, 8× **for the positive trial only**. This is substantially less expensive than a 470-source entire inverse yet provides an actionable numerical diagnosis.

## 3. Explicit non-promotion and actionable next gate

A PASS in SM38 means the original-source closed-form amplitude is implemented correctly against independent numerical physical integration, and the complete negative 973-leaf quadrature / original 3,892-cell envelope comparisons were executed and consistent. **Convergence of two finite Gauss orders or a passing numerical Loewner comparison does not supply outward interval error bounds.** No numerical negative generalized eigenvalue here can establish an original negative odd mode; the positive pole-conditioned source resolvent is still an incompletely resolved 25-source sampled Fourier trial with a missing rigorous unbounded high-frequency arch tail and original strong residual. The full original **470×470** spectral sign has not been tested.

**SM39 next:** use the SM38 attribution results to choose either (a) a new tighter original all-real signed multiplier envelope weighted by the true physical source response (if envelope dominates), (b) a improved original frequency-local Taylor/Young comparison (if moment cap dominates), or (c) rigorously enclosed independent real-frequency quadrature (if FFT undersampling dominates). Then independently certify the **positive** original digamma full logarithmic Fourier tail and the actual original full strong \(A_o/A_*\) resolvent residual before any complete 470-source spectral acceptance. Preserve W-ODD-NEG O1/O2, even E1–E4, whole signed Weil, CC27/RH **OPEN**.

Replay: \`python3 scripts/sm38_original_negative_leafwise_quadrature.py\`; workflow uploads \`artifacts/sm38_original_negative_leafwise_pilot.json\` as **NONCERTIFYING** numerical evidence.


## 4. Actual focused initial numerical findings — the dominant source of inflation identified

The first SM38 run exposed a **failure of independent high-frequency QUADPACK oscillatory integration** (max-subdivision and roundoff flag). This was correctly treated as an inconclusive independent numeric check, NOT a failed analytic source formula. Replacing that particular cross-check with independent high-density physical-space composite Simpson integration (131073 physical nodes) fixed the numerical validation. The second run **39170637129 PASSED** on the 25 genuine original supported source pilot and all three matched settings.

Every reported eigenvalue below is **NUMERICAL, noncertifying**; SI06/SM37's underlying original real-frequency upper envelope and original exact rational 890-moment cap remain the separate rigorous statements.

| Same original 25-source Galerkin trial | 4096 physical, padding×4 | 8192 physical, padding×4 | 8192 physical, padding×8 |
|---|---:|---:|---:|
| Old **coarse FFT** sampled genuine signed negative generalized max | 0.997100712 | 0.997100617 | 0.999835397 |
| **NEW original negative physical sine Fourier direct 973-leaf Gauss32** max | **0.964651302** | **0.964651410** | **0.972929928** |
| Original old SM10 signed multiplier envelope on exact physical Fourier amplitudes | 10.677776197 | 10.677768979 | 10.853260397 |
| Original new SM37 signed multiplier envelope on exact physical Fourier amplitudes | **9.817182283** | **9.817173075** | **9.975611617** |
| Full original SM37 890-column Taylor/Young/η cap (sampled physical overlaps) | **9.826764138** | **9.826758843** | **9.985352056** |
| SM37 envelope / direct original negative leafwise | **10.1769×** | **10.1769×** | **10.2532×** |
| Original Taylor cap / its OWN original envelope | **1.000976×** | **1.000976×** | **1.000976×** |

The original full true-formula negative integrated mass at Gauss32 is **16.0168938464** (compared with SI10/SM10 original envelope cap mass 37.62605884375 and SM37 **refined** envelope cap mass 27.227999359375). **Mass ratios are not generalized eigenvalue ratios**; the physical source Fourier response weights each frequency very unevenly.

Direct negative leafwise Gauss16→Gauss32 generalized maximum changed only by **\(4.1\)–\(4.3\times10^{-6}\)**; this checks numerical stability but is **NOT** an outward truncation error certificate.

### Important causal ranking on the SAME 25-source pilot

1. **Genuine ORIGINAL multiplier envelope dominates remaining cap conservatism:** the SM37 weighted original upper envelope's largest generalized Ritz is ~10.18–10.25× the leafwise direct original signed multiplier integral. This holds even with the *same analytic physical-source Fourier transforms*. The gap cannot be primarily ascribed to Taylor/Young.
2. **Original Taylor/Young/η cap contributes only about \(0.0976\%\)** above its *own* genuine multiplier envelope (ratio ~1.000976), close to the inherited Young \(1+\tau=1+1/1024\). Thus changing source Taylor order, globally tiny η or its whole-series moment assembly first would miss the dominant bottleneck in this pilot.
3. **Coarse FFT was indeed biased, but secondary:** the FFT direct negative generalized max was about 2.8–3.4% above the independently leafwise-integrated true-formula one. The true-formula negative frequency support is narrower than the original FFT bins, but that explains only a small part of the apparent >10× gap.
4. The positive-pole-conditioned original **trial** \(Z\) still uses the FFT stiffness without an original logarithmic arch tail/residual certificate. Both the direct leafwise ~0.965–0.973 and refined-envelope ~9.82–9.98 are numerical tests on **25 selected original directions only**, not generalized eigenvalues of the real entire 470 source original \(A_*^{-1}\). The direct leafwise trial also lies above the *sufficient* full-operator threshold \(51/56\approx0.9107\), which **does not** prove original odd indefiniteness.

### Concrete SM39 computation prioritized by the evidence

The new SM38 source revision also computes a **frequency-leverage map** along the **largest generalized eigenvector of the refined envelope** on the same 25-source Galerkin basis:
\[
\Delta_j(v)=2\int_{J_j}
[w_{\rm SM37}(\xi)-(\kappa-m(\xi))_+]\,
|\langle Zv,\sin(2\pi\xi x)\rangle|^2\,d\xi.
\]
For every one of the 107 original clusters, numerically evaluate \(\Delta_j(v)\) across all four-way refined cells and sort the clusters by *actual original signed-envelope excess weighted by the problematic physical response*. This directly identifies the few frequency clusters to attack with tighter certified **whole-real pointwise signed multiplier enclosures**, rather than another indiscriminate 3892→15568 uniform subdivision.

The leverage map is also **NUMERICAL ONLY** (neither a true 470D eigenvector nor an outward interval bound). Its focused final-head run will record the exact top cluster locations and concentration. If the gap is not concentrated, a new operator inequality sharper than piecewise \(\kappa-m\) upper may be needed, including a safe signed cancellations scheme at the complete matrix level.

The mandatory independent certification of the ORIGINAL **positive archimedean digamma logarithmic high-frequency Fourier tail**, complete physical 470-source positive resolvent and strong Galerkin residual remains essential before whole W-ODD-NEG O1/O2 acceptance. No even, Weil, CC27/RH promotion follows.


## 5. Final-head SAME-TRIAL frequency leverage map — the SM39 target is exceptionally concentrated

The updated **final-head focused SM38 Actions run 39171010719 PASSED**, including the complete 107-cluster same-trial frequency-leverage calculation (same 8,192 physical/8× FFT-padded **sampled positive trial**, selected genuine SI10 25-source basis, original physical analytic sine amplitudes and original Gauss32 signed-negative frequency support). Its **noncertifying** dominant-envelope generalized eigenvalue is \(9.9756116173\ldots\), and the *true-formula direct negative integral on that SAME envelope eigenvector* is \(0.9607943044\ldots\). The original refined signed-envelope excess on the eigenvector is \(\Delta=9.0148173129\ldots\).

Numerically, that surplus is **not spread across the original 107 signed-negative frequency clusters**:

| True original negative-frequency cluster | Original frequency interval | Envelope-minus-actual physical energy on same sampled eigenvector | Fraction of total excess |
|---|---|---:|---:|
| **0** | **[0, 1.15625]** | **8.9766991713** | **99.57716%** |
| 1 | [1.265625, 2.03125] | 0.0368036556 | 0.40826% |
| 2 | [2.453125, 3.171875] | 0.0010351280 | 0.01148% |
| All remaining 104 original clusters combined | Rest of original real negative support | approximately 0.00027936 | approximately 0.00310% |

The first cluster alone comprises **296 of the 3,892 refined original whole-real subcells** and contributes \(9.8926931245\ldots\) of the total \(9.9756116173\ldots\) original refined envelope energy on the worst numerical mode, while the corresponding true-formula signed-negative original Fourier energy from this cluster is only \(0.9159939532\ldots\).

**This is the concrete SM39 frontier: tighten the original zero-to-1.15625 real-frequency ARCHIMEDEAN lower bound, not the Taylor approximation or the remote prime source bands.** In SI07,
\[
\mathrm{arch\_lower\_cell}(j)
= \sum_{k=0}^{63}\frac{y_j^2}
{(k+1/4)((k+1/4)^2+y_j^2)}
+\tfrac12\log_{\rm lower}\bigl(1+(y_j/(64+1/4))^2\bigr)-C_{\rm upper},
\quad y_j=\mathrm{YFAC}\cdot j,
\]
and this same integer-endpoint lower is used for EVERY \(\xi\in[j,j+1]\), including nearly the whole dominant original cluster inside \([0,1]\). Each rational summand and the logarithmic tail lower are increasing with \(y\ge0\); consequently the **same SI07 exact rational expression evaluated at the actual SUBCELL LEFT ENDPOINT** \(a\) yields an improved, valid original whole-real arch lower for every \(\xi\ge a\), without changing the multiplier or truncating its original Fourier domain:
\[
\boxed{\mathrm{arch}_{\rm original}(\xi)
\ge \mathrm{arch}_{\rm lower}(a)
\quad(\xi\in[a,b],\ a\ge0).}
\]
This is an analytically grounded **SM39 development proposal**, not yet a newly CI-verified operator bound. SM39 should implement \(\mathrm{arch}_{\rm lower}(a)\) using the inherited SI07 *outward-rational* \(64\)-term tail and integer-to-rational monotonicity proof, retaining the SI06 complete **seven-prime** phase interval and its 69 derivative payment on every subcell. The first pass should target **cluster 0** while leaving all other SM37 original intervals unchanged, then recompute the **same original 107 exact full covariance blocks/890 original source columns and true global 24-bit \(\eta\)**, verify \(K_-\preceq\widehat K_{\rm SM39}\preceq\widehat K_{\rm SM37}\) on the entire original odd carrier, and rerun the matched 25-source physical envelope generalized upper. A larger improvement on the first cluster would confirm the practical benefit before extending this rational arch procedure to other 106 clusters.

**Mandatory caution:** all cluster leverage values and physical eigenvectors above are numerical 25-source pilot data and are NOT global eigenvalues, lower/upper certified 470D generalized source spectra, or complete original signed odd positivity. The original SI07 signed real-frequency mathematical arch monotonicity, SI06 prime intervals, SM37 exact upper, and complete original \(A_o\) logarithmic high-frequency tail/strong physical Galerkin residual must undergo independent mathematical audit. W-ODD-NEG O1/O2, even E1–E4, Weil, CC27/RH all **OPEN**.
