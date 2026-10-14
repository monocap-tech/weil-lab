# RC260 — direct band tail separated from the compression defect

Parent: `7c6d3cc1405caae7b822a0ea86e190998b31d812` (RC259).
Branch: `research/rpb108-route-consolidation`.

RC260 certifies that nearly all of the previous ideal-band output-tail
allowance was the compressed projection defect, rather than actual high
Legendre output. A direct infinite-tail bound replaces that allowance in
the physical residual estimate. Both source inverse-response upper bounds
improve substantially. Neither source signed gap nor Stage I is closed.

| Certified upper bound | RC259 even | RC260 even | RC259 odd | RC260 odd |
| --- | ---: | ---: | ---: | ---: |
| Ideal-band physical output beyond 512 | 1.797507e-5 | 2.013063e-34 | 1.872504e-5 | 1.312857e-8 |
| Complete model physical source output beyond 256 | 0.010459339 | 0.002957181 | 0.011249287 | 0.003535880 |
| Actual full-source outside Fourier energy | 0.019096711 | 0.008968308 | 0.021487656 | 0.010564676 |
| Actual source inverse response | 0.485973828 | 0.239383795 | 0.537641806 | 0.282920050 |

Display values are outward rounded; the certificate stores exact rational
enclosures. Signed-gap lower bounds improve to approximately -0.150825 even
and -0.185838 odd, and remain below zero. The relevant original source forms
are approximately 0.088559 and 0.097083. These are two source tests, distinct
from the full rank-639 signed response and from the separate eight-source
canonical inverse width 0.485647.

## Why the previous estimate included a different quantity

Let C = J_U^* J_U denote the ideal full-line Fourier-band projection compressed
to the physical interval [-B,B]. It is a positive contraction. For the same
fixed exact Z, put

    q = <Z,CZ> = ||P_band F Z||^2,
    D_comp = q - ||CZ||^2 = <Z,(C-C^2)Z>.

The old estimate used

    ||(CZ)_(>N)||^2 <= q_upper - captured_energy_lower_through_N.

Its right-hand side can pay both the actual tail and D_comp. Since C^2 need
not equal C after physical compression, increasing N alone need not remove
this allowance. RC260 does not discard D_comp or identify C with a projection.
It bounds the actual tail directly and separately encloses D_comp.

Equivalently, D_comp is the physical energy outside [-B,B] of the full-line
band-filtered Z. It is not the high Legendre-output energy inside that
interval, and it is not the source's outside-frequency energy.

The resulting positive defect intervals are tightly centered near
1.7975067103e-5 even and 1.8711902257e-5 odd. They concern the ideal compressed
band operator only. The actual rational augmentation is unchanged, and all
of its inherited model-comparison faults remain paid.

## Explicit band output through degree 1024

RC259's off-diagonal spherical-Bessel Sturm--Liouville boundary identity is
used for output degrees 513 through 1024. Every output degree exceeds the
input degree 64. Matching parity eliminates the infinite endpoint Wronskian,
and the full-band Legendre Gram is zero off diagonal. Thus each compressed
band Gram is a finite sum of endpoint Bessel values and derivatives; no
improper oscillatory quadrature is needed.

The phase uses Machin's identity with 600 alternating terms per arctangent,
explicit next-term remainders, and an outward 750-decimal pi interval. This
interval must lie inside the original pinned pi interval. Reduced arguments
use 700-decimal grids. Generation uses 420 sine/cosine Taylor terms, replay
440, with 1200-decimal interval arithmetic. Spherical-Bessel values and
derivatives are propagated through 1024 on 1200-decimal grids in generation,
1240 in replay. All intermediate rounding is outward. The original pinned
pi lower-limit and prefactor error is still paid separately.

The degree-511 odd and degree-512 even outputs are independently recomputed
and must intersect RC259's pinned intervals. New Gram intervals are stored
with 24-decimal outward endpoints. RC251's degree-0-through-256 intervals
and RC259's degree-257-through-512 intervals are reused unchanged.

## Infinite tail from the Poisson representation

Rodrigues' formula and integration by parts give, for real t,

    j_n(t) = t^n/(2^(n+1) n!)
             * integral_-1^1 exp(i t x)(1-x^2)^n dx.

The exact beta integral is

    integral_-1^1 (1-x^2)^n dx
      = 2^(2n+1) (n!)^2/(2n+1)!.

Consequently, without a positive exponential factor,

    |j_n(t)| <= |t|^n/(2n+1)!!.

Exact rational controls check the integral normalization through n=8. The
general bound follows from the nonnegative integrand weight and |exp(itx)|=1.

With the unitary Fourier convention exp(-2 pi i xi x),

    F(P_n)(xi) = 2B (-i)^n j_n(2 pi B xi),
    mass(n) = 2B/(2n+1).

Cauchy--Schwarz against F Z on [-U,U], followed by exact integration of
xi^(2n), therefore gives

    |<P_n,CZ>|^2/mass(n)
      <= q_upper * 4 B U * z_max^(2n)/((2n+1)!!)^2,

where z_max = 2 pi_upper B U. The factor 2n+1 cancels with the frequency-power
integral denominator. This uses the pinned band energy q_upper, not the
physical energy of the entire Z input and not an augmented-operator norm.

For the first omitted matching-parity degree f = 1026 even or 1025 odd, set

    a_f = z_max^(2f)/((2f+1)!!)^2,
    r_f = z_max^4/((2f+3)^2 (2f+5)^2).

The ratio of successive matching-parity terms decreases and r_f < 1, which
the validator checks exactly. The complete physical output beyond 1024 is
bounded by

    q_upper * 4 B U * a_f/(1-r_f).

This is a bound on the actual ideal-band output tail and contains no
compression-defect allowance. All infinitely many remaining modes are paid.

## Separating the defect and updating the actual source

For each explicit Gram interval, minimum and maximum absolute values yield
lower and upper physical mode energies. Sum these through 1024, and add the
analytic remainder only to the upper endpoint, to enclose ||CZ||^2. Intersect
the new beyond-512 tail bound with RC259's previous valid upper bound.

Using the pinned interval [q_lower,q_upper], the defect satisfies

    max(0,q_lower - ||CZ||^2_upper) <= D_comp
    D_comp <= q_upper - ||CZ||^2_lower.

Both lower endpoints are strictly positive. No inference about positivity
of the original Weil operator follows from this ideal-band defect.

RC259's complete endpoint/prime/augmentation source energy on degrees 257
through 512 is reused. Above 512, combine the RC258 original physical tail
with lambda times the square root of the new direct band tail. Add that
squared tail to the explicit source window using Legendre orthogonality.
Intersect with RC259 to obtain the new complete model tail R beyond 256.

The retained physical source polynomial remains degree 256, with exact
energy A and outside Fourier-energy upper Y from RC257. RC258's orthogonality
bound, in its checked regime Y(A+R)<=A^2, gives

    ||P_out(p+q_model)||^2 <= (sqrt(Y)+sqrt((1-Y/A)R))^2.

Here q_model is the omitted physical source, not the band quadratic form q.
All finite retained-coefficient/actual-s uncertainty and all global
regular-kernel, prime-arithmetic, pole-Taylor and rational-augmentation faults
are subsequently paid in norm. New actual total source energy S and outside
Fourier energy X are intersected with RC259.

For the same 1000 rational tau values, minimize the retained two-band bound

    <e,N^-1 e>_D <= S/I + X*(1/O - 1/I),  I>O>0.

The variational center, source, four trials per parity, actual rational N,
bandwidths and augmentation coefficients are unchanged. Inverse and signed
gap enclosures are intersected with RC259. The canonical metric remains
M=D^-1 L, distinct from N and original N0. D has harmonic diagonal H_n+s;
n(n+1) belongs only to the separate Sturm--Liouville identities.

## Reproduction and remaining work

Generation and exact replay verify 215 inherited blob pins. Replay uses the
longer Taylor expansion and finer Bessel interval grids, reverses source-mode
and physical-energy sums, pin order and tau candidates, and requires exact
certificate equality. Reused earlier certificates are pinned; this pass
does not claim to regenerate their expensive Fourier or prime calculations.

From repository root:

    python scripts/validate_rpb108_rc260_projection_defect_free_tail.py --output certificates/rpb108_rc260_projection_defect_free_tail.json
    python scripts/validate_rpb108_rc260_projection_defect_free_tail.py --output certificates/rpb108_rc260_projection_defect_free_tail.json --replay

The full rank-639 signed response and original full auxiliary norm gate are
unevaluated. The separate finite eight-source canonical inverse width stays
485647/1000000. Stage I, RH, F4 and Lean remain open/false.

Next: use the already materialized physical residual through degree 512 in
the Fourier/residual inverse calculation, or control the remaining original
prime output directly. Closure of the two source tests would still leave
the full signed criterion to certify.
