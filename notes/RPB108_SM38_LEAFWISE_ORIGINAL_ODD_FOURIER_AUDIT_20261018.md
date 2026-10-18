# SM38 — Leafwise original odd Fourier response: FFT resolution versus signed envelopes and Taylor moments

October 18, 2026. Canonical W-ODD-NEG. Stacked on SM37 PR #218 (final-head focused CI passed).

## 1. Actual original supported odd physical Fourier transform

The SM36/37 25-source numerical pilot compared a sparse frequency-bin FFT estimate of the original negative multiplier against a rigorously enveloped 107-block / 890-column original cap. The ≈9.9× discrepancy may include undersampled negative-frequency integrals: original FFT frequency spacing was 0.113636 (padding ×4) or 0.056818 (×8), against original signed-negative leaves width 0.015625 and refined SM37 subcells width 0.00390625.

For the true original physical odd carrier H_o=L²([-B,B])_odd, B=11/10, the physically supported sine Fourier transform is
\[
T_f(\xi)=\int_{-B}^{B}f(x)\sin(2\pi \xi x)\,dx.
\]
Original full signed-negative odd quadratic:
\[
\langle f,K_{\neg,o}f\rangle
=2\int_0^\infty(\kappa-m(\xi))_+ |T_f(\xi)|^2d\xi.
\]
The inherited SI10 real-frequency signed-negative support consists of all 973 original leaves; SM37 subdivides them into 3892 whole-real signed-envelope subcells. No true negative source lies outside those leaves under inherited exact original sign premises.

The pilot's 25 genuine original odd physical source functions have degrees 0 and 1 plus pole s=sinh(x/2). For any positive original source center c and S(u)=sin(pi u)/(pi u), source transforms are ANALYTIC:
\[
T_{\sin(2\pi cx)}(\xi)=B[S(2B(c-\xi))-S(2B(c+\xi))],
\]
\[
T_{x\cos(2\pi cx)}(\xi)
=\frac{B^2}{\pi}[S'(2B(c-\xi))-S'(2B(c+\xi))].
\]
For the actual original odd pole, a=1/2 and b=2pi xi:
\[
T_s(\xi)=
\frac{2[a\cosh(aB)\sin(bB)-b\sinh(aB)\cos(bB)]}{a^2+b^2}.
\]
These are exact formulas for the genuine ORIGINAL supported source functions, not disjoint frequency source approximations. The implementation uses a stable Taylor series for S' near zero and checks against independent 32768-grid spatial source quadrature. Evaluation of trigonometric/digamma functions is floating point, NOT rigorous interval arithmetic.

## 2. True three-way diagnostic with the SAME positive trial

Keep the actual same selected 25-source SM36 original sampled pole-conditioned positive Galerkin trial Z and G0=Z* Astar_sample Z (not certified true original Astar inverse, because original unbounded positive digamma log Fourier tail is not enclosed). At EVERY one of the genuine 3892 signed negative subcells, apply independent Gauss-Legendre frequency integration at orders 4,8,16 of the COMPLETE coupled physical 25×25 matrix.

Compute the three true-formula negative quadratic matrices on identical Gauss nodes:
\[
N_{\rm direct}=2\int_{\cup J}(\kappa-m(\xi))_+ T(\xi)T(\xi)^T d\xi,
\]
\[
N_{\rm env37}=2\int_{\cup J}w_{\rm SM37}(\xi)T(\xi)T(\xi)^Td\xi,
\]
\[
N_{\rm env10}=2\int_{\cup J}w_{\rm SM10}(\xi)T(\xi)T(\xi)^Td\xi.
\]
Here T(xi) is the whole real physical source Fourier vector after multiplication by the SAME Z coefficient matrix. The m(xi) is the **original seven-prime real digamma multiplier**, and the whole-real signed-envelope weights come from the existing exact-rational original certificates. No positive/source cross is silently dropped. The original frequency integral is physically supported, not a Fourier-sampled disjoint-band surrogate.

Compare full generalized spectral maxima of:
(1) old sparse frequency-bin FFT direct negative,
(2) new leafwise source-analytic direct negative,
(3) actual original SM37 signed-envelope-only negative,
(4) original SM10 parent signed-envelope-only negative,
(5) actual original SM37 107-block/890-column moment/Young cap and
(6) old original SM10 moment cap, all against the SAME sampled G0.

That decomposes **FFT frequency sampling**, **multiplier envelope conservatism**, and **Taylor/Young/physical covariance inflation**. Report full 25×25 numerical Loewner diagnostics in addition to eigenvalues; do not infer mathematical PSD from their float signs. Independent Gauss orders identify convergence but are NOT error certification.

There are only 3892×16=62272 signed frequency points at the densest level and 25 source Fourier vectors; the calculation is practical without assembling all 470 positive resolvent columns.

## 3. Acceptance, noncertification, and next direction

SM38's mathematical advance is the exact source-supported transform formulas and a reproducible direct-original-leaf numerical workflow. All eigenvalues, Gauss quadrature values and FFT source positive stiffness remain exploratory **NONCERTIFYING** because original digamma/prime values, quadrature errors, real source Gram, true positive logarithmic archimedean Fourier tail and strong full original resolvent residual are not interval-enclosed. The existing exact original SI06/SM10/SM37 negative-operator envelope upper bounds are inherited, not supplanted by float Gauss nodes. A large difference may also indicate source Taylor implementation or physical-grid aliasing; fail closed and investigate.

SM39: follow the *measured* dominant discrepancy. If FFT sampling dominates, use leafwise source-analytic negative quadrature rather than frequency-bin FFT. If envelope dominates, improve the original signed multiplier all-real envelopes selectively. If Taylor/Young/moment cap dominates, build a physically weighted direct negative Fourier operator/complete interval Gauss cap, tighten Young remainder or isolate source covariance errors. Independently certify the full original positive digamma log-frequency tail and entire 470-source Astar inverse strong residual before PS36 whole original O1/O2 acceptance.

Whole original odd W-ODD-NEG O1/O2, even E1–E4, signed Weil positivity, native CC27 D-Riesz and RH remain OPEN. Independent signed Fourier/form-domain analytic audit also required.

Replay: python3 scripts/sm38_leafwise_original_odd_fourier_audit.py


## 5. First actual full negative leafwise run: causal decomposition is decisive

**First focused GitHub Actions run 39172268117 PASSED** with the real original 25-source selected support, all 973 original seven-prime negative leaves / 3892 signed subcells, true source-analytic supported Fourier amplitudes, all 107 original negative moment blocks/890 source columns, and independent 4/8/16 Gauss frequency quadrature (still FLOAT / NONCERTIFYING). It compared all matrices against the exact SAME sampled original pole-conditioned positive trial.

**Generalized maximum in each same 25-source trial:**

| Numerically evaluated negative-frequency quadratic | Physical 4096, FFT pad×4 | Physical 8192, FFT pad×8 |
|---|---:|---:|
| Previous **sparse-FFT direct original** signed-negative K | 0.997101 | 0.999835 |
| NEW **leafwise analytic-source direct original** signed-negative K (Gauss16) | **0.964650** | **0.972929** |
| NEW original SM37 signed-envelope-only full physical frequency integral | **9.817182** | **9.975612** |
| Old original SM10 signed-envelope-only full physical frequency integral | 10.677776 | 10.853260 |
| New original SM37 full 890-column Taylor/Young source cap | **9.826764** | **9.985352** |
| Old original SM10 full moment source cap | 10.688198 | 10.863858 |
| SM34 sufficient WHOLE ORIGINAL source threshold | 0.910714 | 0.910714 |

**Where the remaining inflation lives (same physical matrix/source trial):**

- **FFT sampling:** sparse FFT overestimated the leafwise direct generalized maximum by only **3.36%** (pad×4) / **2.77%** (pad×8). Thus the previous FFT was imperfect, but **not the primary source** of the near-10× cap excess.
- **Real-frequency signed negative ENVELOPE:** the certified SM37 envelope-only response had a sampled generalized maximum **10.177×** (pad×4) / **10.253×** (pad×8) the leafwise true-formula original signed-negative response. This is the **dominant measured bottleneck**.
- **Taylor/moment/Young synthesis:** the exact-formula 107-block/890-column source cap exceeded the corresponding envelope-only sampled generalized maximum by just **1.000976×** (pad×4) / **1.000976×** (pad×8), practically all of which is consistent with the mandatory Young factor \(1+\tau=1+1/1024\).
- **Actual signed negative weight integrated mass** from numerical leafwise Gauss16: **16.016884** (full reflected signed axis); SM37 certified envelope full mass **27.227999** and SM10 original full envelope mass **37.626059**. Global mass comparison alone cannot explain spectral 10× inflation; source-frequency leverage is essential.
- **Frequency Gauss stability:** direct leafwise generalized max at 4096 grid: order4 \(0.964653974\), order8 \(0.964647176\), order16 \(0.964650176\); at 8192 grid: \(0.972933367\), \(0.972924904\), \(0.972928650\). This is a useful numerical convergence test but **NOT** an interval Gauss error bound.
- **Numerical Loewner residual caution:** new cap minus envelope-only sampled matrix shows a small negative eigenvalue \(-1.04\times10^{-5}\) at 4096 physical grid and \(-4.90\times10^{-7}\) at 8192; this is consistent with spatial physical-overlap discretization/aliasing rather than a rigorous failure of the independently certified SM37 cap. Do **NOT** use these float matrices to prove a true Loewner inequality.

**Outcome:** SM38 measured the remaining computational inefficiency and found it **principally in the conservative ORIGINAL signed seven-prime multiplier ENVELOPE**, not in the 890-column moment/Taylor machinery. Broad improvements to the latter are a poor next allocation. Increasing Fourier FFT zero-padding alone likewise would not resolve the main excess.

### New, precisely targeted mathematical SM39 direction

The current SM37 real-cell envelope uses \(\operatorname{arch}_{\rm SI07}(\lfloor a\rfloor)\), held constant across each integer interval \([j,j+1]\), PLUS a 69-derivative prime correction. The archive source implementation writes the arch lower explicitly as a sum of positive increasing rational terms and a logarithmic tail lower:
\[
\mathcal A_{\rm lo}(t)=
\sum_{k=0}^{63}
\frac{(Yt)^2}{(k+1/4)((k+1/4)^2+(Yt)^2)}
+\frac12\log_{\rm lo}\!\left(1+\left(\frac{Yt}{64+1/4}\right)^2\right)-C_{\rm up},
\quad Y=333/106<\pi.
\]
Because the physical arch \(\Re\psi(1/4+i\pi t)-\log\pi\) is increasing for \(t\ge0\) by its convergent positive term expansion, **a rational subcell-left endpoint** \(t=a\), instead of its integer floor \(j=\lfloor a\rfloor\), is a valid target for a tighter ORIGINAL whole-real lower (provided the inherited SI07 exact log-rational bound and monotonicity are audited). This addresses the main source of *global envelope slack* without increasing the original negative Taylor rank.

**SM39 acceptance proposal:** implement and certify this original **left-endpoint archimedean lower** at each true signed source subcell, with the same original SI06 exact all-seven-prime midpoint lower and derivative, take its minimum with the SM37 certified old subcell weight, and repeat the exact **107-block/890-pivot** SPD full-operator cap check. Then rerun the SAME 25-source analytic negative Fourier integral and envelope-only response; focus additional refinement on subcells with largest eigenvector-weighted response. No original full O1/O2, even E1–E4, Weil, CC27/RH proof promotion.
