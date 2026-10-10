# RPB108 RC27 — positive compact metric remainder

Date: 2026-10-10. Branch: research/rpb108-route-consolidation.
Recovered parent: 5deae6c3de0801752a937b617478ca8164bb91e5 (RC26).
This is an additive analytic result. No other branch is changed.

## Result

The actual RC25 compact metric operator K_B is positive semidefinite.
Its exact whole-line quadratic multiplier is

    m(xi) = log(1 + e/|xi|), xi != 0.

The logarithmic singularity at frequency zero is integrable. This is
a quadratic identity for zero-extended supported physical vectors,
not a claim that whole-line convolution is bounded on all L2.

Consequently the unevaluated compact matrix can no longer contribute
a negative direction to the physical trial metric. This supplies a
one-sided enclosure without evaluating its entries. It does not
provide the small errors needed for a Riesz solve.

## Direct proof and normalization

For t>0 set C_t(r)=2/(t^2+4 pi^2 r^2).
Elementary integration of the two exponential half-lines gives

    integral_R exp(-t|xi|) exp(2 pi i r xi) dxi
      = 2t/(t^2+4 pi^2 r^2).

Thus C_t has Fourier multiplier exp(-t|xi|)/t and is positive
semidefinite. RC25's exact kernel is

    k(r)=integral_0^infinity (1-exp(-e t)) C_t(r) dt.

For f in L2([-B,B]), extend f by zero. The spatial interchange is
absolutely justified: the integral with |f(x)f(y)| equals the
k-kernel quadratic integral on |f|, which is finite by RC25's
Hilbert--Schmidt bound (or its integrable Schur bound). For each fixed
t the C_t convolution is bounded and Plancherel applies. After that,
the frequency/time integrand is nonnegative, so Tonelli gives

    <f,K_B f>
      = integral_R |fhat(xi)|^2
          integral_0^infinity
           (exp(-|xi|t)-exp(-(|xi|+e)t))/t dt dxi.

For u>0, rewrite the inner difference divided by t as
integral_0^e exp(-(u+s)t) ds. Tonelli then evaluates its t integral as
integral_0^e 1/(u+s) ds = log(1+e/u).
This proves the stated identity and positivity with the RC24 Fourier
factor retained. No numerical quadrature or external special-function
formula enters this proof.

The frequency integral is finite: supported L2 functions are L1, so
their Fourier transforms are bounded near zero, where log(1+e/u) is
integrable. For |xi|>=1 the multiplier is bounded, and Plancherel
controls the remaining integral.

In fact <f,K_B f> > 0 for every nonzero supported f, because m>0
almost everywhere. This strict positivity is NOT a uniform positive
floor: K_B is compact on an infinite-dimensional interval L2 space.

## Physical trial matrix enclosure

Retain RC26's D,S,W and scalar endpoints c_lower,c_upper. Let
L=S+W+c_lower D, U=S+W+c_upper D, and let G be the COMPLETE
physical polynomial trial metric. RC25's norm <24 gives

    0 <= K_trial <= 24 D,
    L <= G <= U+24 D.

The inequalities are in the physical polynomial coefficient metric;
D is essential because these trial polynomials are not orthonormal.
Additionally G>=D follows directly from the canonical Fourier weight
log(e+|xi|)>=1. Both lower bounds are valid simultaneously; no matrix
entrywise maximum is implied.

The enclosure L<=G is new relative to RC26's L+K<=G. It remains
coarse: L_00=(11/5)(1+c_lower)<0. Hence positivity of K alone does
not make L a positive lower certificate or certify a useful inverse.
There is no computed eight-mode complete matrix here.

## Computational next step and evidence boundary

The positive mixture supplies a way to approximate K from below:
restrict the t integral to [delta,T], with 0<delta<T. The resulting
operator is positive semidefinite and is <=K_B. That truncation statement
is exact; discretizing this integral still requires a certified matrix
quadrature error, and removing both tails requires quantitative errors.
A naive sampled positive matrix is not automatically a lower enclosure.

This pass changes the immediate kernel task from sign discovery to
accurate enclosure. Actual compact entries, a certified Galerkin solve,
whole weak Riesz residuals, and native head/source checks remain open.

Validation: analytic proof above, with explicit Fubini/Tonelli,
Fourier normalization, zero-frequency integrability and coefficient
metric audit. No new executable exact-check count is claimed.
RC25/RC26 numerical check counts are inherited reports, not rerun here.

No original Weil positivity extension, RH/F4 closure, or Lean theorem
is claimed. The existing a=1.06 certificate remains the anchor.
