# EF41 — Four authentic SI10 even frequency jets, signed physical Schur projection

**2026-10-31, original W-EVEN-FORM OPEN.** Parent EF40 [draft PR #448](https://github.com/monocap-tech/weil-lab/pull/448), last source/governance [Actions #41265978041](https://github.com/monocap-tech/weil-lab/actions/runs/41265978041) SUCCESS, parent head cea3c626b6e7f5a62e18f44e6df2cdb06bb936d0. EF39's full original seven-prime/pole + first 40 signed quarter-digamma cutoff physical response and complete arch Gram retained, with the entire infinite arch remainder paid. This pass tests source-valid higher jets rather than increasing independent unprojected upper bounds.

## Original-object source inventory and four authentic even rows

The original SI10 first center is c0=37/64, with protected Taylor order **p0=15**. In the ORIGINAL physical interval I=[-11/10,11/10], the first four real-even Fourier source jets are (up to harmless overall signs)

v0(x)=cos(omega x), v1(x)=x sin(omega x), v2(x)=x²cos(omega x), v3(x)=x³sin(omega x),
with omega=2*pi*c0.

The actual derivatives of exp(2*pi*i*c0*x) bring phase signs, but these four exact directions lie in the unchanged SI10 protected exceptional V469. They are not new assumed constraints or merely approximate surrogate trial functions. All 469 original source directions remain defined: only FOUR are tested here.

Define original source-specific signed physical H40=z+h40. The TRUE z includes all seven signed prime-power translations n=2,3,4,5,7,8,9 with weights w_n=ln(prime(n))/sqrt(n), the authentic original physical source cutoff on I and the original genuine positive even cosh pole 2u cosh(x/2) where u=<cosh(x/2),v0>. The TRUE h40 uses the first 40 physical original half-integer quarter-digamma Laplace cutoff modes after subtracting the exact protected constant arch row a_arch(c0)v0. EF39 separately proved the entire omitted m>=40 arch tail has L2 norm <57/500+1/10000.

## Complete original signed source integrals, no floating Gram inverse

The actual physical source Gram is G_ij=<v_i,v_j> on I, i,j=0,...,3. For every i,j, x^(i+j) times the product of the appropriate sin/cos is reduced algebraically to integrals of x^n, x^n cos(2omega x), x^n sin(2omega x). Their antiderivatives are evaluated using the finite exact polynomial-exponential identity

int x^n exp(zx) dx = exp(zx) sum_{r=0}^n (-1)^r [n!/(n-r)!] x^(n-r)/z^(r+1), z != 0,

with z=i*2omega, and the zero-frequency polynomial integral as needed.

The true signed source response column b_j=<H40,v_j> uses the same exact primitive on the EIGHT positive-half original cutoff cells for the arithmetic terms, the two z=+/-1/2+i*omega physical cosh-pole terms, and the first 40 actual z=+/-lambda_m+i*omega arch modes. At arch endpoints the exponential is evaluated directly as exp[-lambda_m(B-/+x)] so it remains physical and bounded; native SI06/EF24/EF29 source pi/log/sqrt/trig/exp interval arithmetic gives fully outward fixed integer endpoints at 10^340 scale.

No fitted floating quadrature is used in the certificate, and all original prime n4,n8,n9, positive even pole, finite arch mode cross and full EF39 40x40 signed arch Gram remain in the original response.

## Four-row exact Schur/pivot certificate

Starting with EF39's complete signed finite-source squared norm ||H40||², the native script performs FOUR successive exact interval Schur updates:

q_k = G_(kk) conditioned on previous k source rows >0,
beta_k = <H40,v_k> conditioned on previous source rows,
D_k = D_(k-1) - beta_k²/q_k,
D_(-1)=||H40||².

The complete source-native verified original interval centers (displayed rounded for readability) are:

| # genuine rows projected | pivot q_k | positive gain beta_k²/q_k | remaining physical squared norm D_k |
|---|---:|---:|---:|
| 1 (v0) | 1.2363494115 | 0.41780698674 | 0.06232001255 |
| 2 (v1) | 0.28829890668 | 0.005257751141 | 0.057062261409 |
| 3 (v2) | 0.16703295695 | 0.001651701716 | 0.055410559694 |
| 4 (v3) | 0.027484393523 | 0.008649828192 | **0.046760731501** |

Exact source assertions certify q2>1/7, q3>1/40, D_2<56/1000 and **D_3<47/1000**; every positive pivot and residual has strict 340-digit outward interval bounds, and the first two reproduce the previous EF39/EF40 genuine source values. The fourth pivot is markedly smaller than the first three, hence Gram conditioning is an explicit forward obligation, not dismissed by the positivity of one finite Gram.

The actual four source pairings (native original signed physical) are
b0 ≈ 0.71871790166,
b1 ≈ 0.061903423020,
b2 ≈ 0.37351172841,
b3 ≈ 0.094784201688.

## Entire infinite arch tail and inherited original cofinite energy bound

Let V4 be the genuine span of these FOUR source rows. Because V4 is a subspace of the authentic protected SI10 V469, the cofinite F=V469^perp is contained in V4^perp. Orthogonal projection is a contraction, so

||P_F g_e|| <= ||H40 - P_V4 H40|| + ||h_tail||.

The TRUE first-source arch constant row is already in V4 and hence in V469. The native strict source bound D_3<47/1000 gives sqrt(D_3)<217/1000 since 47/1000<(217/1000)^2. Together with the original certified infinite tail,

||P_F g_e|| <217/1000+57/500+1/10000
= 3311/10000 < **1/3**.

The inherited original SI10 full signed even cofinite energy floor is mu>17/25000. Consequently the complete first-source cofinite energy-dual response and the EF34 unseen residual obey

**0<eta <= ||P_F g_e||²/mu < (1/3)^2/(17/25000)=25000/153 ≈163.39869.**

The lower eta>0 inherits EF34's conditional source-shell jump/pseudolocality/form-core premise. The upper inherits the independent original EF26/EF29 source physical quarter-digamma identity and strong domain; native arithmetic alone is not an independently audited Fourier/form-domain proof.

This improves EF40 eta<3240/17≈190.588 by about 14.3%. The remaining upper is still far above EF33's restricted original two-vector Schur positive lower S2>1/500=0.002. No complete first-source full-cofinite Schur sign, original 469D exceptional Schur PSD, even positivity, odd positivity, whole Weil form or RH result is certified.

## Next EF42 and custody

The first cluster has 15 genuine even protected Taylor jets; four are now explicitly measured, **11 remain in that cluster** and **465 original protected even source directions in total remain unprojected**. EF42 should inspect the actual fifth and sixth source jets with full signed original physical cross and verified Gram pivot conditioning. An additional small positive pivot alone is not a meaningful advance: evaluate its net reduction in the entire signed response, while continuing to pay the arch infinite tail, and STOP a method if the accumulated conditioning budget no longer permits a certified projection.

Native script: `scripts/validate_rpb108_ef41_original_even_four_jet_projection.py`; workflow: `.github/workflows/ef41-original-even-four-jet-source.yml`; status: provisional pending independent original analytic domain and Fourier/source audit. No historical overwrite, no main merge.
