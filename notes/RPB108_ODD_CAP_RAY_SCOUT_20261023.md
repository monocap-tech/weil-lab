# NF — Original 25-source pilot: smallest cap-only stopping ray

**October 23, 2026. Active W-ODD-NEG OPEN. This is strictly a numerical feasibility investigation, not a certificate.**

**October 23 correction:** The original SM10 cap (25-source sampled generalized maximum up to 10.863858) was superseded in the same original 890-column geometry by the exact certified SM37/SM39/SM40 caps. The last SM40 sampled maximum was ~1.003132 at 4096×4 and ~1.012044 at 8192×8, still above theta=51/56~0.910714. SM40 lowers the inherited 107-block cap while retaining all exact physical source columns and infinite Taylor remainder. This scout now targets **SM40**, not obsolete SM10. A failure witness against SM10 alone does not stop the best available negative-cap method.


## Historical evidence to exploit

The successful SM36 original-source numerical pilot (PR #217, GitHub Actions run 39167260822) sampled the genuine 107-block/890-column SM10 negative cap on 25 actual original odd polynomial and sinh sources. Its three original grid configurations returned maximum generalized cap/Ritz ratios 10.688198, 10.688195 and 10.863858, while its sampled direct negative-energy ratios were 0.997101, 0.997101 and 0.999835. The whole odd sufficient threshold is 51/56 = 0.9107142857142857. These are float, not outward-rational enclosures.

If Jp denotes the 25 actual physical original source functions, Ap=Jp*Astar Jp, Cp=Jp*Kcap Jp, Hp=Jp*Jp, the exact Galerkin change of coordinates Zp=Jp Ap^-1 Hp is invertible. Thus the generalized cap ratio on Zp equals that on Jp by exact congruence. The SM36 pilot therefore points to a potential **fixed-890-cap source Ritz method obstruction** before any expensive inverse-residual calculation, but proves none.

## Stronger branch: a direct-negative obstruction

The earlier SM38/SM40 source-analytic **sampled direct** negative-frequency generalized maximum was about 0.965–0.973, while SM40's sampled 890-cap maximum was 1.003–1.012, both above theta=51/56≈0.910714. A rigorous rational vector \(v\) with
\[
 v^*K_Jv>(51/56)\,v^*A_Jv,\qquad
 K_J:=J^*K_-J
\]
would rule out the **entire theta-based sufficient inequality on the canonical V=ran(J) Ritz space**, even with a zero-overestimate perfect negative cap; it would not rule out a better leakage ratio/threshold, enriched Ritz spaces, or true signed \(A_\star-K_-\succeq0\). Since theta is strictly below 1, a direct ratio between theta and 1 is completely compatible with a positive original signed operator. This is a *method-specific* obstruction only.

The updated scout checks individual, paired and triple selected original physical source combinations against both **SM40 cap** and **sampled direct Kneg**, with separately rationalized candidates and repeated-grid ratios. If a stable direct candidate appears, the harder rigorous enclosure requires original all-frequency \(A_\star\) action **upper** and ORIGINAL complete signed negative-frequency \(K_-\) action **lower** on that specific same rational source \(Jv\). SM40 provides a **negative upper**, not that necessary lower. A sampled direct Fourier value, however consistent between grids, is NOT an exact lower bound.

## Rational physical-ray discovery

The script scripts/scout_rpb108_w_odd_neg_cap_ray.py computes a full matched sampled raw 25-by-25 Ap and Cp, including the original seven-prime multiplier sampled to the FFT Nyquist, full SI29-style pole-corrected source stiffness, all 107 SM10 cap blocks and 890 polynomial columns, plus the cap infinite remainder eta. It progressively tests single original physical generators, two-generator spans and three-generator spans (then a full pilot eigenvector), always converting coefficients to genuine integers and recording the **exact rational** cluster center and polynomial degree.

The same rational integer vector is then replayed on 4096x4, 8192x4 and 8192x8 grids, and compared with the sampled direct-negative cap. In particular the script records any minimum-support ray with sampled cap/A ratio above theta+0.1 on every tested grid. Outputs go to artifacts/w_odd_neg_cap_ray_scout.json and CI log.

The computation is **NOT proof**: FFT aliasing, finite truncation, pole integral quadrature, digamma/trigonometric rounding, physical source integrals, floating Hankel moments and correlation errors are uncontrolled. No exact original 470-source \(A_J,C_J\) is being certified or promoted.

The **next proof** (if a clear candidate emerges) is to certify the SAME rational original physical f=Jv with a rigorous complete-frequency **upper** for its positive-pole Astar action and a rigorous same-original-890-cap **lower** for its cap energy:
\[
 \frac{51}{56}\langle f,A_\star f\rangle
  -\langle f,K_{\mathrm{cap}}f\rangle\le0.
\]
That would reject only the exact fixed original V=ran(J)/890-cap Ritz construction, *not* the true signed odd operator, an enriched Galerkin trial or a sharper alternative cap. Without this enclosure the original theorem remains OPEN.

**Custody:** a separate explicitly noncertifying workflow runs the scout on PR changes. This result stays outside any proof acceptance promotion.
