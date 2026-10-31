# EF29 — Authentic 471-entry original signed mixed-response vector, modulo one protected SI10 row

**2026-10-31, canonical W-EVEN-FORM OPEN.** Parent clean [EF28 draft PR #419](https://github.com/monocap-tech/weil-lab/pull/419), source [Actions #41231918205](https://github.com/monocap-tech/weil-lab/actions/runs/41231918205) **SUCCESS**. The original EF28 physical Gram dI and exact 470×471 source-and-pole-neutral kernel EXIST, but no original numerical signed mixed vector or source moment rank/residual existed before this pass.

## 1. Calculate the ORIGINAL mixed vector only modulo an actual protected source row

Native source e(x)=1_I cos(2πc0x), c0=37/64, I=[-B,B], B=11/10. Original physical even pole cosh(x/2), 107 protected SI10 frequencies and 469 Taylor source functions unchanged. EF28 fixes 471 true C5 even-bell pairs:

  phi_j(x)=[b_r(x-j/512)+b_r(x+j/512)]/2,
  b_r(t)=cos^6(pi*t/(2r))1_(|t|<r),
  r=1/8192, j=1,..,471.

Let the actual 470×471 moment matrix be Htilde with **all original 469 SI10 rows and actual pole row**. The first protected SI10 k=0 row is

  h0_j=<cos(2πc0x),phi_j>=bhat_r(c0)*cos(2πc0*j/512),

where the closed true bell Fourier bhat_r is known exactly from EF21's sine/rational identity.

The true signed mixed original vector is g_j=q0(e,phi_j), with q0 the **entire original seven-prime plus digamma Fourier form**. For the digamma term a_arch(xi)=Re psi(1/4+iπxi)-lnπ, write its scalar value at the protected original c0 as a_arch(c0). The exact Fourier/physical cutoff computation gives

  g_arch = a_arch(c0)*h0 + g_arch,cut.

Therefore the **source-projected equivalent vector**

  gtilde = g_prime + g_arch,cut

obeys

  g - gtilde = a_arch(c0)*h0 in range(Htilde^T),

hence **P_ker Htilde gtilde = P_ker Htilde g** and their Euclidean residual δ is literally the same. This is not numerically *estimating* away the original arch source piece; the first protected row exactly removes it under the source-orthogonality constraint. It also removes an otherwise distracting singular-frequency contribution before numerical evaluation.

The nontrivial original quantitative gate still requires computing/enclosing the ACTUAL Htilde row entries and δ. This pass builds only the original signed vector **modulo a proven row-equivalence**, not a fabricated numeric Schur correction.

## 2. Original seven prime/power mixed entries become FULL-bell cosine formulas

The authentic source arithmetic Fourier multiplier is -2∑_(n=2,3,4,5,7,8,9) w_n cos(2πxi ln n), w_n=(ln p)/sqrt(n) with the authentic original prime p underlying each n. Its physical form gives

  g_prime,j = -2∑_n w_n ∫phi_j(x)e(x+ln n)dx.

For each n and every positive/negative EF28 bell center, the exact SI06 rational ln(n) intervals separate the physical cutoff B-ln(n) from the entire bell support by a STRICT margin. This is checked for ALL 7×471×2=6,594 original source/bell combinations. No cutoff partially intersects any bell. For a wholly present bell, the full original cosine integral is bhat_r(c0)*cos[ω(ln n±j/512)]/2, with ω=2πc0. Therefore

  g_prime,j = -∑_n w_n bhat_r(c0) [
    1_{positive bell inside} cos(ω(ln n+j/512))
   +1_{negative bell inside} cos(ω(ln n-j/512)) ].

Expected EXACT native counts of wholly included positive/negative bells, respectively:

| original n | + centers | - centers |
| ---: | ---: | ---: |
| 2 | 208 | 471 |
| 3 | 0 | 471 |
| 4 | 0 | 325 |
| 5 | 0 | 211 |
| 7 | 0 | 38 |
| 8 | 0 | 0 |
| 9 | 0 | 0 |

Thus the complete **original n8,n9 mixed channels vanish on all 471 basis functions**, while n2,n3,n4,n5,n7 are retained with genuine signed weights. The exact cutoff positions guarantee ZERO partially clipped bell integrals in the arithmetic gradient on this grid, not an invalid wholesale dropping of original terms.

The true original finite first-source **arithmetic diagonal A_prime=q_prime(e,e)** is ALSO calculated by an exact physical overlap formula, for all seven n:

  A_prime=-2∑_n w_n [ (2B-ln n)cos(ω ln n)/2
                             +sin(ω(2B-ln n))/(2ω)].

Here even n9 contributes: ln9<2B, so the diagonal still receives all original seven terms even though its mixed contribution on EF28's compact grid is zero. This scope distinction is essential.

The script computes an honest outward interval for original A_prime. It does **not** compute the separate arch diagonal A_arch and therefore does not determine the original full A or corrected Schur sign.

## 3. Original arch cutoff vector is an exponentially convergent native Laplace series

From EF26's exact original quarter-digamma translation identity, after removing the protected cosine row as above,

  g_arch,cut,j = 2 Re[e^(iωB) ∑_(m≥0)
    e^(-λ_m B)J_r(λ_m)cosh(λ_m*j/512)/(λ_m-iω)],

with λ_m=2m+1/2 and the same physical cosine-six bell Laplace transform

  J_r(λ)=45sinh(λr)/[2λ∏_(k=1)^3((λr/π)^2+k²)]>0.

No 469-factor FIR Λ appears, because the EF28 test is not FIR-filtered. Every term uses the actual original digamma kernel and the same true I cutoff. The series is evaluated with 100 terms m=0..99 in the native EF24/EF26 directed-outward 10^340 integer interval arithmetic. It uses exact SI06 arctan/log rational bounds, genuine original weights, direct trig recurrences and factored positive exponentials. Original n=2..9 cutoff indicators are exact Fraction decisions; real arch vector values are signed intervals, not a sampled frequency proxy.

**Uniform rigorous tail:** Every original j satisfies

  B-j/512-r >17/100.

The absolute mth series term is bounded by

  (5r/4)exp[-λ_m(B-j/512-r)]/λ_m.

For omitted m≥100, λ_m≥401/2 and λ_m*(17/100)>34; the finite exact rational exponential partial sum proves exp(34)>10^14. Also 1/(1-exp(-2*17/100))<4. Therefore for EACH of all 471 original coordinates

  |∑_(m≥100) true term_m| <
    (5r/4)*10^-14 * 4/(401/2)
    < 10^-19.

This is a **uniform absolute** enclosure, not a heuristic asymptotic decay. The script attaches ±10^-19 outward to each of the 471 calculated arch coordinates. Consequently the true source-reduced mixed vector is enclosed at all 471 coordinates with a global l2 tail <sqrt(471)*10^-19<22*10^-19, independent of Htilde's condition number. This does NOT pay error in an attempted numerical kernel projection; that separately requires an actual rank/singular-gap certificate.

## 4. Original k=0 source-grid alias audit

For the exact rational SI10 frequency centers c_i and c_j, sampled original zero-order cosine source rows on the uniform j/512 grid are proportional if c_i-c_j or c_i+c_j is an integer multiple of 512, even though their bell Fourier factors differ by an overall positive scalar. The native script scans every distinct frequency pair with exact Fraction arithmetic and reports any genuine alias. Such an alias certifies a precise row dependence among zero-order source rows, but does not by itself determine the rank of all polynomial-source rows or the complete Htilde.

This explicitly distinguishes the **physical Gram condition 1** proved by EF28 from the unrelated, possibly very poor conditioning of the original oscillatory source moment matrix.

## 5. Acceptance and stopping condition

EF29's source verifier exports a machine-readable JSON artifact containing all 471 outward intervals for gtilde, g_prime and g_arch,cut, the original protected h0 row, genuine A_prime interval, exact cutoff counts and alias evidence. The artifact belongs to native Actions, and may not be described as verified until source/manifest CI succeeds.

EF29 **does not construct or numerically invert Htilde**, claim a nonzero lower on δ, compute the original full A_arch, claim original S_even negativity, or close any whole Weil/RH obligation. Any future lower on δ must preserve the real source row-space and singular/rank uncertainty; no float rank cutoff is admissible.

**EF30 next:** build a certified matrix-vector residual interface using the same original moment rows and exported gtilde. Prefer a rank-revealing interval-validated row/nullspace witness, adaptive row scaling and a rigorous matrix backward-error budget. Independently enclose A_arch if the source residual appears near the negative-direction threshold. If the 471-grid's source matrix cannot be sufficiently separated from numerical singularity, report that finite-grid METHOD STOP and revise the basis, without reviving the universal 469-fold FIR.

All prior original files preserved. No main merge. W-EVEN-FORM, odd, whole Weil and RH OPEN.
