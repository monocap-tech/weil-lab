# RPB108 RC73 — actual projected signed-pole transfer

RC73 certifies a projected source-transfer estimate for the actual rank-38 native Riesz head. It uses the signed pole operator's rank-two range to remove almost all of its contribution to the transfer allowance. The actual projected residual upper factor for the existing 22 source inputs improves from RC72's 4235/512 to 4961/1024, approximately 4.8447265625. This is a further 29/70, approximately 41.4286%, tightening of the certified upper.

The source inputs remain degrees 0 through 21. The projection head remains degrees 0 through 37. The complete 38-input source covariance and enlarged Weil floor remain open.

## Signed pole range and actual projection

On the physical interval [-B,B], B=11/10, the signed pole operator has parity ranges

\[
g_0(x)=\cosh(x/2),\qquad g_1(x)=\sinh(x/2),
\]

and acts as +2 g_0 tensor g_0 in the even block and -2 g_1 tensor g_1 in the odd block. The signs and complete original source convention are unchanged.

Let i be the physical embedding and Pi38 the actual canonical orthogonal projection. For every physical polynomial p of degree at most 37, i*p is in the actual native Riesz head. Therefore (I-Pi38)i*p=0 exactly. This uses the actual Riesz identity and polynomial target span, not nominal trial coefficients.

Take t=x/B and b=B/2=11/20. The even Taylor polynomial through degree 36 approximates cosh(bt); the odd Taylor polynomial through degree 37 approximates sinh(bt). Both map exactly into the actual head.

For a pole input u, the subtraction coefficient 2<g_p,u>_phys can be unknown. Its existence is sufficient for the orthogonal-projection estimate; the actual projection coefficients need not be evaluated.

## Exact Taylor remainder and operator bound

For parity p in {0,1}, the first omitted Taylor degree is n_p=38+p. All omitted coefficients are positive in absolute value and their successive ratios decrease. Set

\[
r_p=\frac{b^2}{(n_p+1)(n_p+2)},\qquad
\tau_p=\frac{b^{n_p}}{n_p!\,(1-r_p)}.
\]

For |t|<=1, the uniform range remainder is at most tau_p. With R=2B=11/5 and the existing physical range squared-norm upper N_p from RC42, define

\[
\beta_p\ge2\sqrt{R N_p}\,\tau_p.
\]

Exact rational square-root ceilings and outward rounding are paid. Then

\[
\|(I-\Pi_{38})i^*K_{\mathrm{pole}}u\|_{\mathrm{can}}
\le\sqrt{\rho}\,\beta_p\|u\|_{\mathrm{phys}},
\qquad\rho=252/257.
\]

This follows by subtracting the Taylor polynomial from g_p, applying Cauchy-Schwarz to <g_p,u>, and applying the physical embedding adjoint norm bound. It is an actual projected operator estimate.

| Parity | Uniform range remainder upper | Projected pole norm upper divided by sqrt(rho) |
|---|---:|---:|
| Even | approximately 2.60223164e-55 | approximately 1.20474326e-54 |
| Odd | approximately 3.66977913e-57 | approximately 5.28460649e-57 |

The exact fractions, Taylor coefficient lists, range norms, and root ceilings are stored in the certificate. The full pole operator is not small; its output range is approximated inside the head with a small remainder. No pole sign is replaced with positivity, and no pole head contribution is removed from the Weil form.

## Projected complete source transfer

Let e=iR22-V64 be the physical Riesz error for the existing 22 inputs. The full physical error Gram upper E_phys remains RC67's unchanged correlated enclosure. RC68's nominal operator approximation error delta and trial physical Gram T also remain unchanged.

The archimedean remainder retains its full physical norm bound 643/100. The paired-prime operator retains its full physical norm bound k_prime. After the actual rank-38 projection, the combined norm bound divided by sqrt(rho) becomes

\[
k_{p,\mathrm{proj}}=643/100+k_{\mathrm{prime}}+\beta_p,
\]

instead of adding the full signed-pole norm 2 N_p. With nu=1/65536, the projected canonical transfer Gram upper is

\[
E_{\mathrm{proj}}=\rho\big((1+\nu)D_kE_{\mathrm{phys}}D_k
 +(1+1/\nu)\delta^2T\big),
\]

with paid outward rounding. D_k contains the parity-dependent projected norm bounds. This matrix encloses the error only after projection; it is not a new upper for the full physical source error.

Exact PSD checks prove E_proj is Loewner smaller than rho times RC68's full physical transfer allowance. Thus the current calculation changes the allowance that caused RC72's fixed-allowance barrier. It does not contradict that barrier.

## Actual residual upper

Use RC71's unchanged paid rank-38 nominal physical polynomial residual covariance W. A second Young inequality gives

\[
\Gamma_{38}^{(22\text{ inputs})}
\le(1+t)\rho W+(1+1/t)E_{\mathrm{proj}}.
\]

The validator first retains RC72's Young parameters and proves a whole-matrix Loewner improvement over RC72's upper. It then selects parameters from an explicit rational grid and verifies every candidate against RC67's actual 22-input canonical Gram lower bound. Final outward rounding is paid and checked again.

| Parity | Selected Young parameter | Certified actual residual relative upper |
|---|---:|---:|
| Even | 2 | 4961/1024 |
| Odd | 9/4 | 305/64 |

Consequently

\[
\Gamma_{38}^{(22\text{ inputs})}\le(4961/1024)M_{22}.
\]

The optimized upper is certified through scalar parity comparisons. Whole-matrix dominance is claimed for the version with unchanged Young parameters, not assumed for every reoptimized candidate.

## Independent replay

Replay bounds the omitted range series using 20 explicit terms plus a separate geometric tail, independently of generation's one-step geometric majorant. It checks exact root conditions, parity and Taylor degree, reconstructs physical trial masses by direct weighted sums, and transports the Riesz error through diagonal congruence. Final Gram comparisons and the unchanged-parameter matrix improvement are checked after inverse Chebyshev-to-Legendre congruences. The resulting certificate is reproduced exactly.

The analytic range-subtraction argument is recorded above; no new Lean formalization is asserted.

## Remaining boundary and next obligation

The scalar Schur budget remains unproved. Even with projected pole transfer, the Legendre-degree-20 input makes every positive Young majorant retaining the new combined allowance have a relative factor at least approximately 0.1354028443, about 7.92546e9 times the inherited ceiling. This is again a barrier for those upper majorants, not a lower bound on actual error or leakage.

The next projected-transfer components to sharpen are the compressed archimedean multiplier and the paired-prime translation operator. RC73 supplies one concrete projection-sensitive mechanism; simply repeating full operator-norm transport for those components retains a large allowance. Improved Riesz/source error enclosures remain another possible route.

No actual source-budget failure at rank 38, negative Weil direction, enlarged positive Weil floor, complement floor at rank 38, complete 38-input source covariance, full 1250 projection, new aperture positivity, RH, or F4 conclusion follows. The inherited 1250-complement floor is not attached to the rank-38 complement. Historical milestone artifacts remain unchanged.
