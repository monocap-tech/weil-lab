# RPB108 — RC172: quadratic regular action and two-source canonical interface

Aperture 11/10. Parent RC171: `413d3701d582271bd3e318790b1be58e985f8047`.
Only `research/rpb108-route-consolidation` is written. Historical checkpoints, the seven-source reference frame and Lean remain unchanged.

RC172 extends the represented regular carrier from P0 to P2, pays every omitted degree, and assembles the full canonical metric and action-error interface on span{P0,P2}. An independent cross-column self-adjoint identity checks the new action against RC171. P2 is a polynomial-source test of the general construction, not asserted coverage of the full original augmentation source family.

| Certified component | Outward upper |
|---|---:|
| P0 canonical action D-error norm, retained RC171 | 0.000179349 |
| P2 projected regular action D-error norm | 0.000055995 |
| P2 full omitted D-action energy | 2.595645e-7 |
| P2 complete canonical action D-error norm | 0.000512543 |
| Two-source action error squared relative to source D Gram | 2.252322e-7 |

The P2 tail bound dominates its final norm error. Additional arithmetic precision alone would not materially reduce this accepted bound. The actual canonical Gram entry intervals are G00 in [2.3935975964,2.3943217866], G02 in [0.0862301935,0.0865540612], and G22 in [0.5782506369,0.5783954750]. These displayed endpoints are outward; exact acceptance uses the full rational entry and Loewner matrices.

## Polynomial Poisson action

Write u=x/B, h=t/(2 pi_kernel B), c=1/h, and F(u)=[atan(c(1-u))+atan(c(1+u))]/pi_kernel. Direct integration of the physical Poisson kernel against P2(v) gives

\[
(P_tP_2)(u)=[P_2(u)-3h^2/2]F(u)
 +\frac{3uh}{2\pi_{kernel}}
 \log\frac{(1-u)^2+h^2}{(1+u)^2+h^2}
 +\frac{3h}{\pi_{kernel}}.
\]

This follows by writing v=u+w and P2(v)=P2(u)+3uw+3w^2/2. The three integrals are the constant arctangent profile, the logarithmic difference, and 2 minus h times the arctangent sum. All constants, including the physical Fourier scaling, are retained.

RC171's elementary complex moments Q_n(1+i h) compute the coefficients of F. If ell is the logarithmic ratio in the displayed formula, its odd Legendre coefficients are ell_n=4 Re(Q_(n+1)-Q_(n-1)). Differentiation gives ell'=-2 Re[(z-u)^-1+(z+u)^-1]; integration by parts against the Legendre antiderivative proves this formula. Multiplication by u or u^2 uses the exact Legendre recurrence, with all incoming neighboring coefficients retained. The validator therefore needs moments through Q259 to pay every output through even degree 256.

For c<1/4, the far kernel is expanded directly:

\[
\frac{h}{\pi_{kernel}[(u-v)^2+h^2]}
 =\frac c{\pi_{kernel}}\sum_{k=0}^{31}(-c^2)^k(u-v)^{2k}
 +\text{paid remainder}.
\]

The input moments are integral v^j P2(v)=3/(j+3)-1/(j+1) for even j and zero for odd j. The remainder applied to P2 is uniformly bounded by (2c)^65/pi_kernel, since |P2|<=1 and |u-v|<=2. Each term is rounded outward before aggregation to keep the rational denominator finite without losing the infinite error payment.

The same method is constructive for any finite polynomial source: its finitely many monomial moments replace these P2 moments, and polynomial division in the Cauchy integral gives the near-node logarithmic/arctangent profile. RC172 evaluates P2; it does not claim arithmetic realization of every high-degree required source. That execution and its conditioning costs remain a separate obligation.

## Actual P2 regular tail

Let k be RC171's positive even regular kernel, with ||k||_2^2=2I2, |k'(d)|<=2e/d and I2=e pi^2/3. The supported regular operator norm is at most r=789/125: the exact certificate checks 4B I2<r^2, using the inherited supported-input Hilbert–Schmidt estimate.

For q=P2(x/B), ||q'||_2^2=6/B and q''=3/B^2. Distributional differentiation of its zero extension retains both endpoint values q(-B)=q(B)=1 and both endpoint derivatives -3/B and 3/B. Thus, for f=Rq,

\[
f'=Rq'+k(x+B)-k(B-x),
\]

\[
f''=Rq''-\frac3B[k(x+B)+k(B-x)]
       +k'(x+B)+k'(B-x).
\]

The kernel difference has norm at most sqrt(2I2); the sum has norm at most 2sqrt(I2). It follows that

\[
\|f'\|_2\le r\sqrt{6/B}+\sqrt{2I_2}=:K_1,
\]

\[
\|Af\|_2\le2BK_1+3r\sqrt{2B}+6B\sqrt{I_2}+4eB\sqrt{2B}=:K_2,
\quad A=-\partial_x[(B^2-x^2)\partial_x].
\]

The endpoint flux vanishes by the same logarithmic kernel bound as RC171. The actual coefficients satisfy sum_n [n(n+1)]^2 m_n |f_n|^2<=K2^2. Evenness and monotonicity of D_n give the entire omitted D^-1 energy after degree 256 bounded by K2^2/[ (258*259)^2 (H258+s_lower)]. This concerns the actual action, not just the Poisson approximation.

The retained error pays RC170's full physical operator error on the norm sqrt(2B/5) input, kernel-pi replacement, the far-node remainder, all directed coefficient intervals and the actual D-constant enclosure. Retained and omitted D supports are orthogonal, so their squared errors are added. The explicit certificate stores every coefficient and the full norm bounds.

## Exact endpoint tail and canonical action

The full endpoint formula gives

\[
CP_2=\frac1{6s}P_0
 +\frac{41/30-\log2}{s+3/2}P_2+\xi_2,
\]

where xi2 has the coefficients specified in the terminology registry at every even n>=4. This is an exact retained analytic tail, not an omitted-output approximation. It belongs to D energy by its convergent coefficient-square sum. Subtracting r D^-1 P2 and adding the new regular polynomial supplies a finite-plus-analytic trial for D^-1 L P2, with the two finite endpoint coefficients' uncertainty paid. The previous P0 action remains unchanged.

## Correlated canonical interface

The same symmetric Poisson approximation is evaluated in two different source columns. Self-adjointness gives (Rhat P2)_0=(Rhat P0)_2/5. RC172 requires the two independently computed rational intervals to intersect before accepting the mixed regular entry. The near-node integral is symmetric, and the far polynomial is the same even polynomial in u-v in both columns, so the identity applies to the represented approximation as well.

For the actual canonical Gram, the endpoint mixed entry is 2B/6; the regular mixed entry is 2B times this intersected zeroth coefficient. The diagonal P2 entry retains D, endpoint, -r mass and the actual regular diagonal. RC170's operator error and all far/phase terms are paid in both mixed and diagonal bounds. The P0 diagonal uses RC171's actual canonical interval. Full entry intervals are converted to a weighted Loewner enclosure. Exact rational PSD checks accept its gap and its lower relative to the inherited physical embedding floor on this two-source span. This is not a new full-space or original Weil floor.

If e0,e2 are the full D-action norm error uppers for the two columns, then every real or complex coefficient mixture has error Gram bounded by 2 diag(e0^2,e2^2). This pays the unknown mixed error by norm Cauchy–Schwarz. The certificate tests its exact relative bound against the actual diagonal D Gram lower. No mixed action-error orthogonality or sign is assumed.

Remaining work is the required finite physical source family and the succeeding endpoint/regular actions needed by a correlated canonical inverse correction. The native seven-source reference certificate is preserved. This pass does not execute a canonical Riesz iteration, identify the original augmentation source range, evaluate original Weil or augmented actions, or close Stage I, whole-aperture positivity, Global/F4, RH or Lean.

## Reproduction

Run `scripts/validate_rpb108_rc172_quadratic_regular_action.py --output certificates/rpb108_rc172_quadratic_regular_action.json` with RC171, RC170, RC169, RC121 and RC129 certificate paths in that order. Repeat with `--replay` to reverse all Poisson nodes and far-moment sums and compare the complete rational certificate. The additive validator reconstructs the historical node generator and projection helpers, verifies exact hash and source-digest links, and independently checks the mixed cross-column intersection, full tails and two-source PSD bounds.
