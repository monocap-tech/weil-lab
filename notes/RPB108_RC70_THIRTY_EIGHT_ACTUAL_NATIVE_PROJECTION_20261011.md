# RPB108 RC70 — actual 38-feature native projection

RC70 constructs a certified interface for the actual consecutive native head of 38 features (degrees 0 through 37), using the already certified 64-mode canonical trial metric of RC67. RC69 proved that fewer than 38 consecutive features cannot meet the inherited scalar source-budget ceiling. RC70 supplies the first larger projection interface at that necessary count; it does not establish that 38 features suffice.

The certificate contains the physical native Gram and its exact rational inverse, a Ritz lower enclosure for the actual canonical native Gram, its physical embedding upper enclosure, inverse envelopes, 64-mode rational trial coefficients, and conservative whole-map canonical and physical Riesz error bounds. All acceptance checks use exact rational arithmetic.

## Actual Gram and inverse

Let C be the exact Chebyshev-to-Legendre conversion for 38 native targets, D the diagonal physical Legendre mass, and X the physical pairings between the 64 trial polynomials and those targets. RC67 supplies

\[
G_{\mathrm{nom}}-\delta D_{64}\le G_{\mathrm{actual}}
\le G_{\mathrm{nom}}+\delta D_{64},\qquad
\delta=1849\cdot10^{-30}.
\]

With P=C^*D_{38}C, variational Ritz and the global physical embedding give

\[
M_{\mathrm{lo}}\le X^*(G_{\mathrm{nom}}+\delta D_{64})^{-1}X
\le M_{38}\le\rho P,\qquad\rho=252/257.
\]

The exact Ritz matrix is rounded with diagonal row-sum allowances. An exact parity-block PSD bisection with ten steps finds a positive rational alpha satisfying M_lo >= alpha P. This is a certified lower factor, not a claimed optimum. The actual inverse therefore satisfies

\[
\rho^{-1}P^{-1}\le M_{38}^{-1}\le\alpha^{-1}P^{-1}.
\]

The certified factor is alpha=3843/16448 (approximately 0.23364543). The physical-Gram-preconditioned condition number is at most rho/alpha=256/61 (approximately 4.19672). The positive lower bound proves linear independence and actual projection rank 38. These are canonical Gram conditioning statements; they are not Weil positivity floors.

## Trials and whole-map error

The trial columns are the exact nominal solve rounded to denominator 10^40. Their first 22 columns equal RC67's enriched native trial coefficients exactly. The separate sharp correlated 22-column error bound from RC67 remains available through the hashed input certificate.

For trial coefficient matrix V, let J=X^*V and T=V^*D_64 V. The identity

\[
\operatorname{Gram}_{\mathrm{can}}(R_{38}-V)
=M_{38}-J-J^*+V^*G_{\mathrm{actual}}V
\]

provides the conservative full 38-column upper enclosure by replacing M_38 and G_actual with their certified upper bounds and paying outward rounding. Multiplication by rho gives a physical error Gram upper. This initial full-head error bound need not match the sharper old 22-column bound on its principal block.

## Nested actual projection and extension

The first 22 physical targets are unchanged. Thus the actual canonical subspaces are nested, and

\[
\Pi_{38}\Pi_{22}=\Pi_{22}\Pi_{38}=\Pi_{22}.
\]

Their difference is an orthogonal projection of rank 16. For any fixed source map S on a fixed input space, Pythagoras gives

\[
S^*(I-\Pi_{22})S-S^*(I-\Pi_{38})S
=S^*(\Pi_{38}-\Pi_{22})S\ge0.
\]

This proves monotonicity for the same source inputs. It does not convert RC68's 22-input covariance into a 38-input covariance, nor does it quantify the reduction.

The validator also constructs the exact physical extension Schur complement P_ext=P_bb-P_ba P_aa^-1 P_ab, where a denotes features 0 through 21 and b denotes 22 through 37. Minimizing the full quadratic Gram inequalities over the first block gives

\[
\alpha P_{\mathrm{ext}}\le
M_{\mathrm{ext}}:=M_{bb}-M_{ba}M_{aa}^{-1}M_{ab}
\le\rho P_{\mathrm{ext}}.
\]

M_ext is the actual canonical Gram of (I-Pi22)R_b. Its inverse envelopes are stored. These attach the next source-pairing computation to an actual 16-dimensional canonical projection increment rather than a nominal trial projector.

## Independent replay and boundaries

Replay reconstructs the physical Gram directly from Chebyshev monomial integrals and independently recovers each conversion coefficient by Legendre orthogonality. It verifies the trial solve by multiplication, reconstructs Ritz through the variational quadratic Z^*G_up Z, checks the physical inverse through triangular conversion, and reconstructs the extension Schur complement from residual physical polynomials. The certificate is reproduced exactly.

RC70 does not evaluate the actual canonical inverse entries or actual projection coefficients exactly. It encloses the actual inverse and characterizes Pi38=R38 M38^-1 R38^*. It certifies no 38-input original source covariance, source-budget success, 38-feature Weil floor, or 38-complement floor. RC63's weak-head-floor ceiling continues to constrain any larger head containing those directions. No full 1250 projection, aperture positivity extension, RH, or F4 conclusion follows.

The next concrete interface task is to attach source pairings to the new projection increment, keeping source-input scope explicit. Enlarging the head alone provides no numerical promise of meeting the inherited scalar budget.

Added artifacts are the RC70 validator, JSON certificate, and this report. Historical milestone files remain unchanged.
