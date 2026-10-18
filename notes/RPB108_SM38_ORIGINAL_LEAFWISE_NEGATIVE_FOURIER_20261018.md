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
