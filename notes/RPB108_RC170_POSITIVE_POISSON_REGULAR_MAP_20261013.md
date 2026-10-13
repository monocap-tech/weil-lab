# RPB108 — RC170: positive Poisson regular map and constant-source action

Aperture 11/10. Parent RC169: `2af9c9b490a9863e1389d60c95a291f826146469`.
Only `research/rpb108-route-consolidation` is written; prior checkpoints and Lean remain unchanged.

RC170 constructs a finite represented action for the actual bounded regular metric multiplier. It certifies its error uniformly over the full supported physical source space, and evaluates its constant-source action with paid whole-interval error. This advances the operator construction required by RC169 without substituting the reference inverse for the canonical or augmented inverse.

The quadrature uses 4,096 positive Poisson terms. Its physical L2 operator error is below 0.0002; its physical Linfinity operator error is below 0.00025. Exact rational endpoints and the sharper D-energy transfer bounds are recorded in the certificate. The operator representation is a deterministic rational-node generator, not a sampled fit.

## Positive integral representation

With the inherited Fourier convention exp(-2 pi i x xi), the ambient Poisson semigroup P_t has multiplier exp(-t abs(xi)) and kernel

\[
k_t(x-y)=\frac{2t}{t^2+4\pi^2(x-y)^2}.
\]

The scalar Laplace identity, obtained by differentiating in the positive numerator parameter and integrating back from zero, is

\[
\log(1+e/|\xi|)=\int_0^\infty\frac{1-e^{-et}}{t}e^{-t|\xi|}\,dt.
\]

After restriction to supported inputs and outputs, it gives

\[
R=\int_0^\infty (1-e^{-et})\,\chi P_t\chi\,\frac{dt}{t}.
\]

Positive quadratic forms and Tonelli identify this integral with the actual regular multiplier. The estimates below also prove operator-norm convergence on the supported physical space. No claim of a bounded ambient multiplier at frequency zero is used.

## Complete quadrature payment

Set t0=10^-6, rho=(257/256)^2 and N=4096. The cells have logarithmic length Delta=log rho and exact midpoint t_j=t0 rho^j (257/256). After u=log t, composite midpoint quadrature approximates the finite integral by Delta sum_j (1-exp(-e t_j)) chi P_t_j chi.

For the small tail, 1-exp(-et)<=et and ||P_t||_2<=1, so its norm is at most e t0. For the large tail, k_t<=2/t, hence the supported kernel has row and column integrals at most 4B/t. Schur's bound gives norm at most 4B/t, and integration pays 4B/t_N. The same estimates hold on supported Linfinity. Both tails are retained in the error budget.

For the finite-integral L2 midpoint error, its ambient multiplier as a function of u is f(u,xi)=exp(-t abs(xi))-exp(-t(abs(xi)+e)). Each term's second u derivative is (z^2-z)exp(-z). Its absolute value is at most one: for z<=1 use z exp(-z)<=1/e<1/2; for z>=1 use z^2 exp(-z)<=4/e^2<1. Thus ||f''||_2<=2, and total midpoint error is at most N Delta^3/12.

For Linfinity, put w=t^2/(t^2+4 pi^2(x-y)^2). Direct differentiation gives partial_u k_t=(1-2w)k_t and partial_u^2 k_t=(1-8w+8w^2)k_t. Both factors have absolute value at most one on [0,1], so the derivative operators have Linfinity norm at most one. The weight a(t)=1-exp(-et) has |a'|<=1/2, |a''|<=1 and 0<=a<=1. Product differentiation bounds the second derivative of a(t)P_t by three. The corresponding midpoint error is at most N Delta^3/8.

The validator encloses e by a positive factorial series and Delta by a positive atanh series. Directed 70-digit sums, followed by rational outward rounding, enclose every node. Each positive weight coefficient is enclosed using a positive exponential Taylor series at argument divided by 128, its explicit geometric remainder, seven repeated squarings and inversion. Beyond argument 100, exp(-x)<=2^-100 is paid. The approximate coefficient and node are rational centers.

For a node uncertainty d_t, the weight changes by at most e d_t. The Poisson operator changes in both norms by at most d_t/t_lower, since its logarithmic first derivative has norm at most one. Coefficient-radius and step-radius errors are added as well. The certificate stores a SHA-256 digest of all rational node/coefficient pairs and the generator parameters. All terms are positive, selfadjoint and reflection preserving.

## Constant physical source

For P0=1 on [-B,B], exact spatial integration gives

\[
(P_tP_0)(x)=\frac{\arctan(2\pi(B-x)/t)+\arctan(2\pi(B+x)/t)}{\pi}.
\]

The resulting finite arctangent sum represents Rhat P0 throughout the interval. RC170 evaluates it at 0, B/2 and B using directed arctangent series and a Machin pi enclosure. Alternating-series remainders are included. Each recorded true-action interval adds the full Linfinity operator error; the displayed sample checks do not replace the whole-interval theorem.

The full physical action error satisfies ||(R-Rhat)P0||_2 <= sqrt(2B) epsilon_2. The represented action is a physical L2 source. It is an explicit finite function representation, not yet a polynomial/analytic-tail coordinate vector for the endpoint carrier.

## Correlated D-energy transfer and remaining work

RC121 supplies D>=s_lower I. For any supported physical source map Q, let E=D^-1(R-Rhat)Q. Then

\[
E^*DE\preceq\frac{\epsilon_2^2}{s_{lower}}Q^*Q.
\]

For a D-energy input family, Q^*Q<=s_lower^-1 Q^*D Q, giving a full correlated D-action error upper epsilon_2^2/s_lower^2 times its D Gram. Equivalently, the D-energy operator norm error is at most epsilon_2/s_lower. This is uniform over source mixtures, including complex inputs. It does not assume action errors are orthogonal or discard mixed rows. Subtracting the exact -r D^-1 term does not change the error of the regular component D^-1(R-rI).

The next obligation is to realize D^-1 of this represented regular source in the finite/analytic endpoint carrier, and extend evaluated output coefficients to the required physical source family. Subsequent endpoint actions must pay representation errors. A full canonical Riesz iteration, requested final tolerance and posterior correlated residual certificate remain open. The original augmentation source range has not been identified with the seven native reference vectors.

No original Weil action or augmented inverse response is evaluated. The signed original response below one remains the original positivity criterion. Stage I, whole-aperture positivity, Global/F4, RH and Lean closure remain unclaimed.

## Reproduction

Run `python scripts/validate_rpb108_rc170_poisson_regular_action.py --output certificates/rpb108_rc170_poisson_regular_action.json certificates/rpb108_rc169_native_canonical_transport.json certificates/rpb108_rc121_diagonal_metric_equivalence.json`. Repeat with `--replay` to reverse the entire finite Poisson sum and compare the complete rational certificate. The validator checks the historical hash link, exact positive-series scalar enclosures and every recorded error budget. The supported operator and midpoint proofs are supplied above.
