# NF — Whole-frequency original Knegative operator norm from SI06

**October 23, 2026. Canonical W-ODD-NEG remains OPEN.** This is a structural scalar-norm improvement on the original whole operator, conditional on the SI06 Fourier/physical realization and domain assumptions, not a signed positivity proof.

## Exact all-frequency multiplier inequality

The actual original seven-prime-power signed Fourier multiplier is
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
 -2\sum_{n\in\{2,3,4,5,7,8,9\}}
             \frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n).
\]
SI06's digamma positive-term identity yields the archimedean lower \(-C\) everywhere on the real frequency line, since all y-dependent summands are nonnegative. Its exact rational bound is
\[
 C=\frac{29}{50}+\frac{11}{7}
       +3\frac{347}{500}+\frac{573}{500}
   =\frac{4707}{875}.
\]
For all seven original prime powers (including 4, 8 and 9), the complete prime contribution is at least \(-T\), where SI06 proves
\[
 T=\sum_{n\in\{2,3,4,5,7,8,9\}}
             2\frac{\Lambda(n)}{\sqrt n}
 \le \mathrm{TWOC}<\frac{70751}{10000}
\]
using exact outward coefficients. Therefore for every real \(\xi\),
\[
 m(\xi)>-C-\frac{70751}{10000},\qquad
 0\le(\kappa-m(\xi))_+<
 \boxed{H_\infty=\kappa+C+\frac{70751}{10000}
 =\frac{871887}{70000}\approx12.4555285714}
\]
with \(\kappa=1/1000\). Restriction from all-frequency Fourier space to the original zero-extended physical odd interval is isometric; it cannot increase the nonnegative multiplier's operator norm. Consequently the **entire original** negative-frequency operator satisfies
\[
 \boxed{0\preceq K_-\preceq H_\infty I.}
\]
This is *much stronger* than the corrected SM33 original mass-based upper 82.77732945625 and the certified SM40 integrated-envelope mass-norm upper 36.899564590625. No finite-frequency sampling or b9/b24 source truncation is involved.

## Fully coupled MG07 impact

The MG07 noncommutative original inverse-residual inequality
\[
R^*A_\star^{-1}K_-A_\star^{-1}R
 \preceq\frac{H_-}{\kappa_\star}R^*B_{14}^{-1}R
\]
uses the valid spectral comparison \(A_\star^{-2}\preceq\kappa_\star^{-1} A_\star^{-1}\preceq\kappa_\star^{-1}B_{14}^{-1}\), NOT a spurious \(A_\star^{-2}\preceq B_{14}^{-2}\).

Thus the same conditional complete 470-source MG07 criterion can use
\[
 (1+t)N_{0,\mathrm{cap}}
 +(1+t^{-1})\frac{H_\infty}{\kappa_\star}
           R^*B_{14}^{-1}R\preceq\theta G_0.
\]
At \(t=1\), the original reference-weighted residual coefficient improves from approximately 4,924,144.4 using the **repaired** SM33 mass to approximately 740,937.4, a reduction by factor \(\sim6.6458\). This improves a bound, not a constructed inverse response. The tightened SM34 scalar theta may also be used after its own corrected exact cluster audit.

Similarly, if the same original b9 physical exceptional complement leakage satisfies \(QK_-Q\preceq\varepsilon I\), the negative-only mixed squared norm satisfies
\[
 \|QK_-P\|^2\le H_\infty\varepsilon.
\]
For the separately audited conditional corrected \(\bar\varepsilon=1062977491599207/16000000000000000000\), this is below \(0.000827497\), and its old-complement \(\mu=17/25000\) negative-only Schur payment is below \(1.216907\). The full signed mixed \(C_+-C_-\) remains necessary in the old physical split; this is not a shortcut to positivity.

The companion exact script is scripts/validate_rpb108_mg07_global_negative_sup.py. It checks SI06's ORIGINAL arch constant and seven-power TWOC upper using rational arithmetic. It does not establish the inherited full physical Fourier/domain correspondence, a true 470x470 source Gram, its residual, exact signed Schur, even sector, CC27 or RH.
