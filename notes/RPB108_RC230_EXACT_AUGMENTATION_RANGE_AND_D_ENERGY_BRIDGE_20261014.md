# RPB108 — RC230: exact rational augmentation range and D-energy bridge

Date: 2026-10-14 UTC. Aperture B=11/10. Branch: research/rpb108-route-consolidation. Parent RC229: `83ac4f6b37176c9ecc3b9b3085e0294819a01368`.

RC230 fixes the augmentation to RC115's exact rational polynomial Fourier kernel. It proves its rank is exactly **639**, with 248 even and 391 odd channels, and identifies its entire adjoint range. It also derives a direct D-energy representation of the augmented inverse response. The original Weil actions and full auxiliary norm below one remain uncomputed. RC228's accepted eight-source canonical inverse width 0.485647 is preserved as a separate result.

The validator checks the exact positive leading coefficient of every retained frequency polynomial, fresh augmented spectral bounds, conditional exact-action inverse budgets, and noncommuting rational matrix controls. Its reversed-input replay reproduces the certificate exactly. The analytic range and form-domain arguments below are part of this milestone; the matrix controls do not prove an actual arithmetic operator action.

## Fixed operator and exact full range

Use RC115's rational pi_0, N=2400 and parity bandwidths U_e=64135627/1000000 and U_o=51359649/500000. Write Z=2 pi_0 B U. The physical finite-kernel operator is Fhat from supported physical L2 to parity frequency L2 on [-U,U]. Its canonical restriction is Xhat=Fhat i, where i is the canonical-to-physical inclusion. The chosen augmentation is, separately in each parity,

\[
 \widehat H=A_Q+\lambda\widehat X^*\widehat X,
 \qquad A_Q=I+i^*Ki.
\]

Here K is the actual bounded selfadjoint physical Weil remainder, including its original prime and signed pole contributions. This is the RC115 rational augmentation, distinct from RC114's exact-kernel augmentation.

The retained indices are 0,2,...,494 and 1,3,...,781. RC115's exact coefficient formula gives, after removal of the unit phase (-i)^j,

\[
 \widehat\psi_j(\tau)/(-i)^j
 =d_j\sum_{m=0}^{\lfloor(2400-j)/2\rfloor}
 \frac{(-1)^m(Z\tau/2)^{j+2m}}{m!(j+m)!},
 \quad d_0=1,\quad d_j=2\ (j>0).
\]

Its lowest nonzero monomial has degree j and coefficient d_j(Z/2)^j/j!>0. Restricting the coefficient matrix to the retained monomial degrees, in increasing order, produces a triangular square matrix with nonzero diagonal. Thus all retained frequency polynomials are linearly independent. Polynomial independence implies independence in the actual frequency L2 metric: a zero L2 polynomial vanishes identically. Their frequency Gram is therefore positive definite, without a computed numerical conditioning bound.

The validator generates all 639 diagonal coefficients by exact Fraction recurrence. It records bit lengths and a SHA256 of each coefficient, encoded as unsigned big-endian numerator and denominator with separate eight-byte lengths. It avoids enormous decimal conversions. These controls certify the diagonal formula and positivity; they do not numerically factor the full frequency Gram.

Let O map the finite native coefficient space to these frequency polynomials. O is injective, so O* is onto that finite coefficient space. Let R map coefficients to the actual canonical moment/Riesz representatives r_j, characterized by

\[
 \langle r_j,h\rangle_c=\int_{-B}^B T_j(x/B)(ih)(x)\,dx.
\]

The r_j are independent: if their linear combination vanishes, its polynomial moment functional vanishes on every interior smooth test, hence its polynomial is identically zero. This uses RC112's actual moment-functionals argument, rather than approximate polynomial Riesz images. With the usual conjugate-linear convention handled consistently, Xhat=O R*, and Xhat*=R O*. Consequently

\[
 \boxed{\operatorname{range}\widehat X^*=W_{639},
 \quad\operatorname{rank}\widehat X=639.}
\]

The physical adjoint range is exactly the corresponding Chebyshev polynomial span. Since D is diagonal in the Legendre basis and has strictly positive entries, D^-1 maps each complete retained parity polynomial space bijectively to itself. Therefore range(D^-1 Fhat*) is exactly that same parity polynomial space, with maximum degree 494 even and 781 odd and ranks 248 and 391.

This discharges RC229's exact source-range specification for the chosen rational augmentation. An exact factorization through only eight channels cannot exhaust it. It does not require 639 separate solves or a dense 639-square Gram: a matrix-free uniform bound or a reduced approximation with a rigorously paid discarded range remains possible. These ranks count source channels, not negative eigenvectors or newly discovered dangerous modes.

## Full-domain operator bridge

Let V be the shared canonical/D-energy form domain established by RC121. Its two equivalent inner products are the canonical form L and the physical diagonal form D=J+sI. Globally,

\[
 aD\preceq L\preceq2D,\qquad a=32125/230953.
\]

Define M as the bounded D-Riesz representative of L, and N as the bounded D-Riesz representative of the augmented physical form

\[
 G(u,v)=L(u,v)+\langle u,Kv\rangle_2
       +\lambda\langle\widehat Fu,\widehat Fv\rangle_{\rm freq}.
\]

Both added forms are bounded on V because the physical inclusion and Fhat are bounded. Thus on all V, M represents D^-1 L and N represents D^-1 G in the form sense. On polynomial cores where the physical actions exist in L2 these are the literal physical formulas. No global unbounded physical composition is silently assumed.

For all u,v in V, the definitions give

\[
 \langle u,Nv\rangle_D=G(u,v)
 =\langle u,\widehat Hv\rangle_c
 =\langle u,M\widehat Hv\rangle_D.
\]

Hence N=M Hhat as bounded maps on the common vector space. Canonical positivity of Hhat makes G positive, so N is selfadjoint positive in D energy, even though it need not be selfadjoint in the canonical metric. M and N need not commute.

For a physical source q, let R_q=D^-1 q, meaning the D-Riesz representative of its physical functional. The corresponding canonical adjoint is i*q=M^-1 R_q. This proves the cancellation identity

\[
 \boxed{\widehat H^{-1}\widehat X^*
       =N^{-1}D^{-1}\widehat F^*,\qquad
 \widehat{\mathcal B}
       =\lambda\widehat F N^{-1}D^{-1}\widehat F^*.}
\]

The direct augmented response can thus start from finite physical polynomial sources in D energy. A separately computed canonical Riesz image is not a prerequisite for this representation. The actual N action still needs the original K action and the rational augmentation action in addition to M. RC228's M inverse gate is not an N inverse gate.

## Fresh bounds and conditional inverse budgets

RC115 supplies eta I<=Hhat. For a fresh safe upper, let b_old be RC114's exact-kernel augmented upper. Since that old augmentation is positive, A_Q<=H_RC114<=b_old I. RC115's combined contour/Taylor/pi error delta bounds J_U-Xhat, giving

\[
 \|\widehat X\|_c\le\sqrt\rho+\delta,
 \quad \rho=252/257,
 \quad b_{\rm hat}=b_{\rm old}+\lambda(\sqrt\rho+\delta)^2.
\]

This deliberately conservative upper adds the new rational augmentation afresh. It never identifies the two different frequency-band operators or subtracts an upper error term from an inherited upper bound. Outward rational rounding yields

\[
 \boxed{\mu I\preceq N\preceq\nu I\text{ in D energy},
 \quad \mu\le a\eta,\quad\nu\ge2b_{\rm hat}.}
\]

The contour bound is a pointwise kernel/rectangle bound before canonical restriction, as is RC115's Taylor/pi kernel error. Applying the same Hilbert-Schmidt estimate to physical L2, and physical Plancherel for J_U, gives ||Fhat||_2<=1+delta. With s>=s_lower>0,

\[
 \|D^{-1}\widehat F^*\|_{{\rm freq}\to D}^2
 \le(1+\delta)^2/s_{\rm lower}=:r^2.
\]

All endpoints are rational outward bounds in the certificate. Approximate displayed values and conditional budgets are:

| Parity | mu lower | nu upper | Residual degree for correction <=10^-6 | Residual degree for correction <=10^-12 |
|---|---:|---:|---:|---:|
| Even | 0.00136934737 | 83.17753192 | 1419 | 2270 |
| Odd | 0.00130178337 | 77.12602135 | 1408 | 2248 |

These are sufficient budgets under **exact N actions**, not executed responses, optimal degrees or inexact-action certificates. Set c=(nu+mu)/(nu-mu), p_n(t)=T_n((nu+mu-2t)/(nu-mu))/T_n(c) and q_(n-1)(t)=(1-p_n(t))/t. Then ||p_n(N)||_D<=epsilon_n=1/T_n(c). Taking Y=q_(n-1)(N)D^-1 Fhat* gives e=p_n(N)D^-1 Fhat* and a response correction at most lambda epsilon_n^2 r^2/mu times the actual frequency identity.

The validator encloses T_n(c) by a positive recurrence for T_n and Delta_n=T_n-T_(n-1): Delta_(n+1)=Delta_n+2(c-1)T_n, T_(n+1)=T_n+Delta_(n+1). Directed rational rounding occurs at every step on a 10^-60 grid. Independent exact positive binomial sums check n<=24. Positivity avoids interval inflation from subtraction of correlated Chebyshev values. Existing RC114 and RC228 inverse budgets are not reused. The worse D-energy conditioning is an explicit tradeoff; no runtime improvement is claimed.

## Actual-metric residual identity and implementation contract

For any bounded trial Y from the full auxiliary space to V, let R=D^-1 Fhat*, e=R-NY and

\[
 C_Y=\widehat F Y+Y^*\widehat F^*-Y^*DN Y.
\]

Adjoints in these displayed physical pairings denote their associated forms; e*D e uses the D inner product and Bhat uses the actual frequency metric. Expanding the square gives

\[
 \boxed{\widehat{\mathcal B}
 =\lambda(C_Y+e^*DN^{-1}e),\qquad
 \nu^{-1}e^*De\preceq e^*DN^{-1}e
 \preceq\mu^{-1}e^*De.}
\]

The inverse residual correction is **added**. An upper bound on e*De supplies an upper response correction; it is not automatically a lower residual bound. A certified lower residual Gram, if available, supplies the corresponding lower correction.

Physical source rounding satisfies ||D^-1 delta_q||_D^2<=||delta_q||_2^2/s_lower. Actual N-action errors must pay M, D^-1 K and lambda D^-1 Fhat*Fhat errors, plus every source/trial truncation and rounding contribution in D energy. Triangle or correlated covariance bounds may combine them; orthogonality cannot be assumed. If exact-action polynomial budgets are implemented with inexact actions, the actual final residual must be bounded again including all propagated errors.

The validator's two-dimensional rational control uses noncommuting M and N and three distinct metrics. It checks N=M Hhat, the cancellation identity, equality of canonical and D response formulas, and the added residual correction exactly. Subtracting that correction fails the exact identity. This is a structural control, not an actual Weil arithmetic computation.

## Remaining work and replay

The full chosen range is now specified in both parities. Still open are actual original K and augmentation action contracts, actual full-range inverse residuals, numerical auxiliary conditioning or an equivalent uniform operator bound, and ||Bhat||<1 followed by Stage I assembly. No original positivity, Stage I, F4, Lean or RH closure is claimed.

Run from the repository root:

```bash
python scripts/validate_rpb108_rc230_augmentation_range_bridge.py --output certificates/rpb108_rc230_augmentation_range_bridge.json
python scripts/validate_rpb108_rc230_augmentation_range_bridge.py --output certificates/rpb108_rc230_augmentation_range_bridge.json --replay
```

Publication adds only this note, its validator and its certificate, with an expected-head non-force branch update. The remote comparison and tree readback must verify preservation of all existing blobs and absence of conflict markers in the new additions. This is not a claim to have scanned every existing repository file.
