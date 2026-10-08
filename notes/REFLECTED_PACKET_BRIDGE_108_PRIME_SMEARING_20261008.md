# RPB108 NF57: a uniform rough-domain prime approximation, with sharp logarithmic rate

Date: 2026-10-08 UTC. Recovered head bbb04c0d9811184f651095bcae360ba548f0e269.
Definitions: [canonical prime smearing](../docs/TERMINOLOGY_RPB108_PRIME_SMEARING.md).

## Actual estimate

For every fixed finite aperture, every original supported canonical h, and 0<delta<=exp(-4),

    |Q_a(h)-Q_(a,delta)(h)| <= [4 S_a/log(1/delta)] E_log(h).   (1)

No derivative, contact hypothesis or zero-specific regularity is required. The complete actual active prime dictionary, exact archimedean term and original pole are retained. This gives a lawful uniform approximation bound for the arithmetic remainder considered in NF56. It does NOT give a positivity bound for the approximating form.

At the ACTUAL one-prime aperture a=1/2, the canonical smearing error has order Theta(1/log(1/delta)) as delta decreases to zero. Smooth modulated supported tests prove the lower bound. Thus a uniform power-of-delta error rate is false for this approximation on the canonical domain.

## Fourier proof on the full carrier

Physical Plancherel gives C_h(s)=integral exp(2pi i xi s)|hhat(xi)|²dxi. Averaging the physical shift over [-delta,delta] multiplies this integral by sinc(2pi xi delta), with sinc(0)=1. Therefore

    |c_h(s)-average_u c_h(s+u)|
       <= integral [1-sinc(2pi xi delta)]|hhat(xi)|²dxi.       (2)

The bracket is nonnegative and at most min(2,(2pi xi delta)²/6). The quadratic bound follows directly by averaging 1-cos(2pi xi u) and using 1-cos v<=v²/2.

Put L=log(1/delta)>=4. For |xi|<=delta^(-1/2), the bracket divided by w(xi)=log(e+|xi|)>=1 is at most (32/3)delta, using pi<4. Since L exp(-L)<=4exp(-4)<1/4, this is less than 4/L. For |xi|>delta^(-1/2), w(xi)>L/2 and the quotient is at most 4/L. Consequently

    sup_xi [1-sinc(2pi xi delta)]/w(xi) <= 4/L.

This bounds (2) uniformly in the shift s. Multiply by the original prime coefficient 2Lambda(n)/sqrt(n) and sum ALL active prime powers to obtain (1). The common archimedean and pole terms cancel only in this error calculation; they remain in each form separately.

All integrals are absolutely defined for canonical h since physical mass is finite and the multiplier is bounded. No smooth-test approximation with an uncontrolled derivative constant is used. The forms are Hermitian, so the diagonal bound gives the same bound for their canonical self-adjoint Riesz operator difference. This is a canonical form norm, not the physical-L2 operator norm of translations.

## Sharpness using an actual active prime

At a=1/2, log 2<1<log 3, so the active dictionary contains only n=2. Let s=log 2 and c=log 2/sqrt(2). Choose a nonnegative smooth real bump psi, supported in (-1/2,1/2) and positive throughout that open interval. Then m=||psi||_2²>0 and C_psi(s)>0 because the shifted interiors overlap.

For each sufficiently small delta, set

    j_delta=ceiling(s/(2delta)), N_delta=j_delta/s,
    h_delta(x)=exp(2pi i N_delta x)psi(x).

These are smooth actual physical carrier vectors in the SAME aperture. N_delta*s is an integer, so c_(h_delta)(s)=C_psi(s). Meanwhile N_delta*delta -> 1/2. Substituting u=delta*t in the averaged correlation and using continuity of C_psi gives

    average_u c_(h_delta)(s+u)
       -> C_psi(s) (1/2) integral_(-1)^1 cos(pi t)dt = 0.

Hence the exact original-minus-smeared form difference tends to -2c C_psi(s), a nonzero constant. The established smooth modulation estimate gives

    E_log(h_delta)=m log N_delta+O_psi(1)
                 =m log(1/delta)+O_psi(1).

Thus the canonical error norm is at least

    [2c C_psi(s)/m+o(1)]/log(1/delta).

Together with (1), this proves the claimed sharp order for all sufficiently small delta, not just a selected sequence. The construction uses the actual prime term; no artificial divisor, contact or off-line zero is introduced. Pole and archimedean terms are identical in the two compared forms, so cannot cancel this approximation error.

## Concrete arithmetic budgets and transfer scope

Rational logarithm/square-root enclosures give S_1<6 for the dictionary 2,3,4,5,7, and S_(log(8)/2)<13/2 after including 8. For delta=2^(-k), k>=6, log 2>2/3 yields

    canonical error <36/k at a=1,
    canonical error <39/k at a=log(8)/2.                     (3)

These are uniform error budgets, not new positivity certificates or estimates of the original source gain. If a lower bound Q_(a,delta)>=gamma E_log is proved independently and 4S_a/log(1/delta)<gamma, then the ORIGINAL form has the positive lower bound gamma-4S_a/log(1/delta). The converse transfer from an original certificate to the smeared form obeys the same error subtraction.

For scale, preserving half of the current 2*10^(-34) aperture-one canonical margin using (3) alone requires k>3.6*10^(35). That is merely a sufficient bound from this method, not a necessary width for all possible proofs. The sharp logarithmic rate explains why treating this smearing as a rapidly accurate numerical approximation is unjustified. No new smeared-form sign computation is claimed.

The NF56 cancellation formula remains exact: only its finite atomic prime part is smeared here, and the growing continuum subtraction is unchanged. At a threshold, the original endpoint correlation is zero but its average can be nonzero. This error is INCLUDED in (1); no threshold atom is dropped, and no source-range interpretation is assigned to the smeared form.

For a positive physical level mu, compare Q_a-mu mass with Q_(a,delta)-mu mass. Their difference satisfies the same error bound, while the original mu residual remains. This result supplies neither original zero-nullity nor same-vector enlarged cancellation.

## Custody and validation

The companion script verifies the complete finite budgets, the one-prime support inequalities, the elementary constant comparison, and the error/margin arithmetic with exact rationals. The Fourier norm estimate and actual modulated lower-bound proof are analytic, not Lean certified. They are a new rough-domain approximation result; they do not prove the required sign estimate for Q_(a,delta), strict source gain at every aperture, global exclusion, RH, F4 or full transport. Aperture-one and concurrent fronts are preserved.
