# SM41 — Rigorous original positive digamma/log-frequency Fourier tails on the true odd supported source functions

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM40 draft PR #222 (final-head CI passed).**

## Decision: stop polishing the negative cap; measure the true original positive operator

SM36–SM40 reduced the actual original seven-prime negative-frequency upper cap, using 107 unchanged moment clusters / 890 genuine odd source Taylor columns and the whole infinite residual. SM40's strict real-frequency endpoint-curvature upper passes exact Fraction arithmetic, and on the same 25-source **NONCERTIFYING** physical odd Galerkin probe, cap/direct negative generalized maxima are now only ~1.04× apart. The **complete original odd signed positivity** still requires the true all-470 positive-operator inverse or full corrected Schur, not a selected Ritz test; the existing positive Fourier computations (SM36–SM40) omit an uncapped logarithmic archimedean tail.

**SM41 mathematical deliverable:** a valid analytic, quantitative, entire real-positive-high-frequency **original** digamma-plus-seven-prime \(A_o\) form and original strong-multiplier \(L^2\) tail for the **same genuine physically supported 25 original SI10 odd source generators**, plus a separate coarse all-470 valid source IBP tail and a direct low-frequency Gauss **diagnostic**. No claim that the low-band integration is yet rigorous, no full 470 original resolvent, no O1/O2/RH promotion.

## 1. Explicit **whole-real** logarithmic upper for the true original positive multiplier

The genuine original seven-prime signed real Fourier multiplier is
\[
m(\xi)=\mathcal A(\xi)-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\log p(n)}{\sqrt n}\cos(2\pi\xi\log n),
\quad
\mathcal A(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi.
\]
As in the original SI06/SM17 operator realization, \(A_o\) is the **true pole-free positive multiplier** \(a_o(\xi)=\max\{\kappa,m(\xi)\}\), \(\kappa=1/1000\). For every true real \(|\xi|\ge1\), the original arch has the *exact* convergent positive-term digamma expansion (put \(t=\pi|\xi|\), \(a=1/4\)):
\[
\mathcal A(\xi)
=\psi(a)-\log\pi+
\sum_{k=0}^\infty\frac{t^2}{(k+a)((k+a)^2+t^2)}.
\]
Here \(\psi(1/4)-\log\pi<0\). Split at \(N=\lceil t\rceil\). For \(k<N\), bound each summand by \(1/(k+a)\), obtaining
\[
\sum_{k<N}\frac{t^2}{(k+a)((k+a)^2+t^2)}
\le4+\log(4N+1).
\]
For \(k\ge N\), the summand is at most \(t^2/(k+a)^3\), and an integral bound gives the remainder
\[
\sum_{k\ge N}\frac{t^2}{(k+a)((k+a)^2+t^2)}
\le t^2\left(\frac1{(N+a)^3}+\frac1{2(N+a)^2}\right)
\le\frac1t+\frac12\le\frac32 .
\]
For \(|\xi|\ge1\) the exact rational SI06 \(\pi<4\) entails \(4N+1\le4(t+1)+1\le21|\xi|\). The rational strict proof \(e^4>21\) establishes \(\log 21<4\). Hence
\[
\mathcal A(\xi)\le\frac{19}{2}+\log|\xi|.
\]
SI06's **exact original all-seven-prime** rational amplitude certificate \(\mathrm{TWOC}<70751/10000\) gives
\[
\boxed{\quad 0<\kappa\le a_o(\xi)\le 17+\log|\xi|,\quad\forall\,|\xi|\ge1.\quad}
\]
This is a **true-original, whole-real, unbounded positive logarithmic tail**, not a false finite frequency cutoff. Its constant 17 is deliberately conservative. It is independently replayed using only SI06 exact rational \(\pi,\log2,\mathrm{TWOC}\) and the analytic digamma identity; no sampled digamma values support its mathematical validity.

## 2. Exact original physical source transforms pay the tail

Let \(B=11/10\), \(H_o=L^2([-B,B])_{\rm odd}\), and for genuine physically supported odd \(g\), \(T_g(\xi)=\int_{-B}^Bg(x)\sin(2\pi\xi x)\,dx\). Original even Fourier weight of real odd \(g\) gives
\[
\langle g,A_og\rangle_{\{|\xi|>\Lambda\}}
=2\int_\Lambda^\infty a_o(\xi)|T_g(\xi)|^2\,d\xi.
\]
The SM36–SM40 pilot uses **25 actual original SI10 physical odd source generators**, all drawn from \(g_c(x)=\sin(2\pi cx)\), \(h_c(x)=x\cos(2\pi cx)\), and the true odd pole \(s(x)=\sinh(x/2)\). For any original source frequency \(c\), take \(\Lambda\ge2c\) and \(\Lambda\ge1\). The genuine physically supported analytic sine transforms from SM38 satisfy uniform *rational source-specific* upper bounds
\[
\boxed{
|T_{g_c}(\xi)|\le\frac{1/2}{|\xi|},\qquad
|T_{h_c}(\xi)|\le\frac{7/10}{|\xi|},\qquad
|T_s(\xi)|\le\frac{2/5}{|\xi|}
\quad(|\xi|\ge\Lambda).
}
\]
Derivations: \(|\operatorname{sinc}u|\le1/(\pi|u|)\) and \(|\operatorname{sinc}'u|\le1/|u|+1/(\pi u^2)\). Since \(\xi-c\ge\xi/2\), \(\xi+c\ge\xi\), \(\pi>3\), and \(B=11/10\),
\[
\frac{3}{2\pi}<\frac12,\qquad
\frac{3B}{2\pi}+\frac5{4\pi^2|\xi|}
<\frac B2+\frac5{36}<\frac7{10}.
\]
For the pole, \(\sinh(B/2)<1,\cosh(B/2)<2\) follow from \(\log2>69/100>B/2\); its exact physically supported sine transform implies
\[
|T_s(\xi)|\le\frac1{3|\xi|}+\frac1{18\xi^2}<\frac{2/5}{|\xi|}.
\]
The condition \(\Lambda\ge 2c\) is checked against the **true rational maximum** of ALL 107 SI10 original cluster centers, not just an approximate selected source frequency. The initial certifying cutoffs are powers of two \(\Lambda=2048,4096,8192\).

For \(d=25\) source columns with exact coefficient-to-transform majorants \(u_j\in\{1/2,7/10,2/5\}\), put \(E=\sum_{j=1}^{25}u_j^2\). Then **for every real source coefficient vector \(z\in\mathbb R^{25}\)**,
\[
|T_{\sum z_jg_j}(\xi)|^2
\le\frac{E}{\xi^2}\|z\|_2^2.
\]
The original \(25\times25\) positive source-form high Fourier tail matrix \(T^A_\Lambda\) therefore satisfies the complete **Loewner upper**
\[
\boxed{
0\preceq T^A_\Lambda\preceq
\delta_A(\Lambda)I,\qquad
\delta_A(\Lambda)=\frac{2E}{\Lambda}
(18+\log\Lambda).
}
\]
The log is bounded **upward with SI06's exact rational** \(\log\Lambda\le q\operatorname{LN}[2]_{\rm up}\) when \(\Lambda=2^q\). This gives a true rational tail ceiling, not numeric quadrature convergence.

For the **whole-line strong original Fourier multiplier \(A_o\)**, the same argument with \(a_o^2\) gives an independently important **squared strong-residual high-frequency tail**:
\[
\boxed{
\left\|\mathbf1_{\{|\xi|>\Lambda\}}\,
a_o\widehat{\sum z_jg_j}\right\|_2^2
\le\delta_{A^2}(\Lambda)\|z\|_2^2,
\qquad
\delta_{A^2}(\Lambda)=
\frac{2E}{\Lambda}\left[(17+\log\Lambda)^2+
2(17+\log\Lambda)+2\right].
}
\]
This is **not** yet a full original strong residual \(R=J-A_*Z\): its positive-frequency low-band action, pole, full original 470-source resolvent and source stability remain to be checked. It does, however, remove the previously completely unpriced high-frequency positive-arch log tail **for any coefficient combination in the actual pilot source space**.

## 3. A valid but weak source-general 470-direction fallback

The original complete SI10 exceptional source basis has precisely **470** odd supported generators: 469 \(x^k\sin(2\pi c_jx)\) for even \(k\) or \(x^k\cos(2\pi c_jx)\) for odd \(k\), plus \(s(x)=\sinh(x/2)\). For any one of these original supported degree-\(k\) functions \(g\), a real-space integration by parts provides
\[
|T_g(\xi)|\le \frac{2(1+k)B^k+4\pi_{\rm up}c_jB^{k+1}}{6|\xi|}.
\]
The pole has the crude integration-by-parts upper \((2+2B)/(6|\xi|)\). Summing squared source-specific rational upper constants gives a **genuine source-general 470×470 high-frequency scalar Loewner tail**, but it is far more conservative than the resonant-frequency-separated \(25\)-source exact sine formula. The script computes its explicit rational coefficient; it is a **feasibility warning, not a usable sign certificate**. Full-470 success will likely require individual generalized \(k\)-th derivative sinc transforms and a matrix-weighted tail rather than this scalar IBP bound.

## 4. Practical numerical whole-positive low band, explicitly NOT yet certified

For the same 25 actual original source formulas, evaluate the genuine original \(a_o=\max(\kappa,m)\) source quadratic via source-analytic sine transforms and Gauss orders 8 and 16 over every unit frequency cell from **0 to \(\Lambda\)**, independently of FFT bins; compare both full \(25\times25\) matrices for numerical convergence. The original \(|\xi|>\Lambda\) tail is **rigorously bounded above by \(\delta_AI\)**, but the low band is currently floating Gauss with no interval quadrature remainder. Thus a full true original \(A_o\) matrix \([A_{\rm low},A_{\rm low}+\delta_AI]\) is **NOT YET CERTIFIED**, and neither is the pole-restored full original positive inverse.

This is an intermediate necessary construction toward an actually workable all-470 original pole-free \(A_o\), the true rank-one odd pole and a complete strong residual. Numerical selected-source Ritz/eigenvalue signs remain **NONCERTIFYING**, including if they appear favorable. No source direction is silently removed.

## 5. Acceptance, next frontier and custody

SM41's scoped acceptance is: prove original all-real \(\max(\kappa,m)\le17+\log|\xi|\), certify genuine original 25 supported source FORM and squared strong \(A_o\) high-frequency tail for every source combination with exact rational parameters at \(\Lambda=2048,4096,8192\), and compute the original all-470 IBP scalar source majorant as an explicit warning. Run actual **source-analytic original positive low-band Gauss8/16** on the same 25 source pilot, keeping its status numerical.

**SM42:** rigorously enclose the original positive **low-band** digamma/prime matrix and pole coupling, using all actual original supported physical odd sine source transforms and partitioning at non-smooth crossings of \(m=\kappa\). Then combine that independent exact low-band error with SM41's whole-real high tail into a true interval \(A_o\) source matrix. For full 470, derive higher-degree source-specific Fourier transform bounds and certified Gram basis transformations to replace the impractical scalar IBP tail; implement an original strong resolvent residual and entire 470-source generalized original \(51/56\) or exact corrected Schur gate. Canonical W-ODD-NEG O1/O2, even E1–E4, whole signed Weil, CC27 D-Riesz, RH all **OPEN**, independent full original Fourier/closed operator-domain audit required.

Replay: \`python3 scripts/validate_rpb108_sm41_original_positive_log_tail.py\`. Exact Fraction source high-tail bounds in the JSON are mathematically distinct from the **noncertifying numerical low-band Gauss matrices**.


## Focused engineering correction after the first run

The **first SM41 workflow run 39176160687 failed**, **not** because of the exact original analytic high-logarithmic positive Fourier tail. All three source-complete 25-direction exact rational high-tail bounds and the original all-470 elementary IBP bound computed and printed. The numerical original LOW band failed its intentional Gauss8/16 convergence gate: relative matrix Frobenius drift **0.02352266152534048** when applying each Gauss rule across entire **unit-width** frequency cells. This demonstrates why a high-frequency tail certificate cannot justify trusting a coarse low-band quadrature.

The first revision subdivided **each unit interval into four subcells**, reducing Gauss8/16 drift to 0.0010056123, narrowly above the strict 0.001 numerical acceptance. The final revision uses **eight subcells per unit frequency interval**, keeping the same strict 0.001 gate (not weakening it). It does not weaken the numerical gate or recast an untrusted low-band as a proof. Independently it uses the existing SI06 exact, much more economical outward rational upper \(\log2<347/500\) to prove \(\log\Lambda<q(347/500)\) for the power-of-two cutoffs. This avoids multi-hundred-digit 128-term fractions in source certificate records while preserving rigorous outward bounds.

### First run's exact high-tail figures, prior to the economical rational tightening

The actual 25 original supported odd pilot sources consist of **16 sine \(k=0\)**, **8 \(x\cos\), \(k=1\)** and **the original sinh pole**. Hence
\[
E=16(1/2)^2+8(7/10)^2+(2/5)^2
=\boxed{202/25=8.08}.
\]
The original TRUE rational maximum SI10 cluster center is \(113013/128=882.9140625\), so every cutoff \(\Lambda=2048,4096,8192\) lies beyond **twice every source center**.

| True original 25-source **high-frequency-only** operator scalar ceiling | 2048 | 4096 | 8192 |
| --- | ---: | ---: | ---: |
| Positive \(A_o\) source **FORM tail** \(\delta_A I\) | 0.2022 | 0.1038 | 0.0533 |
| Squared **strong \(A_o\) Fourier multiplier tail** \(\delta_{A^2}I\) | 5.189 | 2.737 | 1.441 |

These first-run decimals used the tighter exact 128-term SI06 rational log2 upper. The revised simpler strict outward bound \(\log2<347/500\) yields slightly **larger**, still rigorous tail ceilings. No high-tail number is a rigorous enclosure of the *low-frequency* source integral, the whole original \(A_*\) pole-conditioned resolvent, or entire 470 signed odd spectral sign.

The original naive all-470 supported-source derivative integration-by-parts scalar form high tail at 4096 was **approximately \(3.01\times10^6\)**. This valid but extremely loose number is decisive computational evidence that **we cannot scale the same scalar IBP technique from 25 to 470**. Full 470 requires analytic \emph{higher-degree polynomial-source Fourier transforms} and matrix-weighted tail bounds, not a blind larger source solve.

Full original W-ODD-NEG O1/O2, even E1–E4, whole Weil, CC27 and RH remain OPEN. A passing revised numerical Gauss check does NOT prove the original low-band matrix without rigorous quadrature-error enclosures.


## SM41 passing original positive source-tail and low-band diagnostic

**Focused GitHub Actions 39176458907 — PASSED** on the final script with original seven-prime rational bounds, true supported original 25 source transforms, all 470 original polynomial/pole directions in the conservative fallback, and improved original low-band eight-subcell quadrature.

The exact **25-source upper source-transform square sum** is \(E=202/25\). Using the economical exact upward bound \(\log2<347/500\), the rigorous original high Fourier tail Loewner/strong multiplier coefficient ceilings are:

| True original positive Fourier HIGH tail, all selected 25 source coefficients | \(\Lambda=2048\) | \(\Lambda=4096\) | \(\Lambda=8192\) |
|---|---:|---:|---:|
| Source-form \(0\preceq T^{A_o}_\Lambda\preceq\delta_A I_{25}\) | **0.20226828125** | **0.1038721875** | **0.0533051171875** |
| Squared strong multiplier \(\|\mathbf1_{\rm high} a_o\widehat g\|_2^2\le\delta_{A^2}\|z\|^2\) | **5.1928357465625** | **2.738692265** | **1.442383532890625** |

**These are true original high-tail analytic upper bounds (conditional on inherited full Fourier/domain identification), not actual strong Galerkin residuals or full source stiffness matrices.** The full original 470 polynomial/pole-source IBP scalar form-tail bound at 4096 is about **3,010,087.7**, proving how numerically ineffective the straightforward all-direction IBP scaling would be.

The first **NUMERICAL NONCERTIFYING** source-analytic positive low band calculations, now using **eight Gauss subcells per unit frequency**, give:

| Original positive \(A_o\) selected 25-source low-band diagnostics | Band 0–2048 | Band 0–4096 |
|---|---:|---:|
| Gauss8 vs Gauss16 full matrix relative Frobenius difference | **0.0001818606** | **0.0001818547** |
| Numerical Gauss16 source stiffness raw-basis smallest eigenvalue | 0.00737615 | 0.00738275 |
| Numerical Gauss16 source stiffness raw-basis largest eigenvalue | 5.13377 | 5.13400 |
| Numerical sampled pole-conditioned low-band raw-basis smallest eigenvalue | 0.00735898 | 0.00736539 |

The Gauss8/16 agreement is useful numerical evidence of *stability*, NOT a rigorous low-frequency integral enclosure: the original positive multiplier \(a_o=\max(\kappa,m)\) has non-smooth transitions at \(m=\kappa\), the digamma and cosine evaluations are float64, and neither an interval quadrature bound nor full original pole source Gram enclosure has passed.

**Next SM42:** rigorous low-band positive source matrix interval enclosure, including whole-real digamma/quadrature and all \(m=\kappa\) transitions, plus certified physical source Gram and true original pole-conditioned denominator. For all 470 original directions avoid the ~3-million norm scalar IBP bound with analytic higher-degree Fourier transforms / matrix-weighted tails and certified source preconditioning. Only after full original \(A_*\) inverse and strong residual may the 470×470 generalized \(51/56\) or exact corrected Schur original O1/O2 gate be evaluated. Even, Weil, CC27 and RH remain **OPEN**.
