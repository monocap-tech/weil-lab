# RC259 — coupled endpoint/prime/augmentation physical tail

Parent: `428b8ff70e918a7bdcdb6827d3d190f8cc4ffd60` (RC258).
Branch: `research/rpb108-route-consolidation`.

RC259 explicitly computes the physical band-output window from degree 257
through 512 for the same fixed exact Z. It combines endpoint, prime and
negative augmentation output on that window before taking squared norms.
This preserves cross terms lost when entire original and augmentation tails
were previously added in norm. The source polynomial used for the retained
Fourier calculation remains degree 256; no degree-512 Fourier calculation
of the complete residual polynomial is claimed.

| Certified upper bound | RC258 even | RC259 even | RC258 odd | RC259 odd |
| --- | ---: | ---: | ---: | ---: |
| Complete model physical energy beyond 256 | 0.011951734 | 0.010459339 | 0.013641108 | 0.011249287 |
| Actual full-source outside Fourier energy | 0.020907928 | 0.019096711 | 0.024547032 | 0.021487656 |
| Actual source inverse response | 0.529975291 | 0.485973828 | 0.608475141 | 0.537641806 |

Display decimals are rounded outward; exact rational bounds are stored in
the certificate. The updated signed-gap lower bounds remain negative,
approximately -0.397415 even and -0.440559 odd. The original source forms
are approximately 0.088559 and 0.097083, respectively: crossing 0.5 in the
even inverse upper is not this signed-gap criterion. It is also unrelated
to the separate eight-source canonical inverse width 0.485647.

The newly captured band-output physical energy is only about 6.68e-8 even
and 1.01e-7 odd. The C_U^2<=C_U beyond-512 allowance remains about 1.80e-5
and 1.87e-5. This allowance is not the actual omitted energy; it can include
the compressed projection defect. The improvement primarily comes from
retaining cancellation on the newly coupled output window, not from a
large reduction in the separate band-output tail allowance. Further cutoff
extension should not be assumed to remove that defect.

## Band window with an exact boundary identity

The new calculation returns intervals for <P_n,C_U Z> for matching parity
257 <= n <= 512. C_U is the ideal full-line Fourier-band projection compressed
to the physical support. The actual rational augmentation remains separate;
its inherited model-comparison fault is still paid in full.

All output degrees exceed the input degree 64. The off-diagonal spherical
Bessel Sturm--Liouville equation therefore gives a particularly economical
exact boundary formula. For lambda_n = n(n+1), let

    W_nd(t) = j_n'(t)j_d(t) - j_n(t)j_d'(t).
    (t^2 W_nd(t))' = (lambda_n-lambda_d)j_n(t)j_d(t).

Matching parity implies lim_(t->infinity) t^2 W_nd(t) = 0, from the common
leading sine/cosine phase and the O(t^-2) remainder in each spherical Bessel
function. Hence

    integral_z^infinity j_n(t)j_d(t) dt
      = -z^2 W_nd(z)/(lambda_n-lambda_d).

The full-band Legendre Gram is zero for n>64, so the desired compressed-band
Gram is minus its outside-frequency integral. The code pays the usual
Fourier parity signs and 4B/pi prefactor and combines all source modes before
squaring any physical source output.

Spherical inverse-power polynomials are generated and checked against
independent Legendre endpoint derivatives through degree 512. Exact symbolic
controls check j_n''+(2/z)j_n'+(1-lambda_n/z^2)j_n=0 on seven modes, including
512. For the actual endpoint values, j_0 and j_1 are enclosed directly and
all higher j_n and derivatives follow by outward interval recurrence, on
600-decimal grids in generation and 620-decimal grids in replay.

The phase uses 600-term Machin arctangent intervals, 450-decimal pi and
400-decimal reduced-argument grids, 220 sine/cosine Taylor terms in generation
and 240 in replay, and 800-decimal interval rounding. The original pinned pi
displacement and prefactor fault is still paid separately. Final Gram
intervals have 24-decimal outward endpoints. No improper oscillatory integral
is numerically sampled or truncated in this window calculation.

Three independently recomputed low-output controls per parity must intersect
the corresponding pinned RC251 intervals. The stored source Z, bandwidth U,
augmentation coefficient, sources and four trial vectors per parity are
unchanged.

## Complete omitted physical source

Let L_256 be RC251's lower bound on captured physical energy of C_U Z through
256. The new window contributes a further lower bound L_high, computed from
the interval minimum absolute Gram values squared divided by mass(n).
For the pinned band-form upper bound q_upper,

    ||(C_U Z)_(>512)||^2 <= q_upper - L_256 - L_high.

This uses C_U^2 <= C_U, not equality. The compression defect is retained in
the allowance; increasing output degree does not justify deleting it.

RC253's exact seven-boundary prime calculation is replayed through 512. Its
raw coefficient digest and remaining physical prime energy must match the
pinned certificate. Above degree 256 the original model consists only of
endpoint plus prime output: the regular model vanishes there, and identity
and pole model outputs have lower degree.

For each matching mode on the explicit window, form an interval for

    endpoint_n + prime_n - lambda*(C_U Z)_n.

All endpoint/prime/augmentation cross terms are retained before squaring.
Each per-mode physical energy is bounded using the interval's maximum
absolute value and the physical Legendre mass. Stored centers and radii
enclose these intervals; the energy bounds are evaluated on the underlying
intervals before the extra center/radius rounding.

Above 512 only, add the RC258 original-model and new augmentation bounds in
norm. Physical Legendre orthogonality then adds the squared explicit-window
norm to the remaining squared tail norm. Intersect this proposed tail with
RC258's valid complete model tail bound.

## Actual full-source Fourier and inverse bounds

The retained physical polynomial p is unchanged, with exact energy A and
pinned outside Fourier-energy upper Y from RC257. The omitted model q is
orthogonal to p. With its new squared norm bound R, RC258's checked regime
Y(A+R) <= A^2 gives

    ||P_out(p+q)||^2 <= (sqrt(Y)+sqrt((1-Y/A)R))^2.

Finite retained coefficient and actual-s uncertainty, plus all original
regular-kernel, prime-arithmetic, pole-Taylor and rational-augmentation
global faults, are paid after this model bound. The resulting actual full
source outside energy X and total physical energy S are intersected with
RC258. No physical omitted-output norm is identified with a Fourier tail.

For the same 1000 rational tau candidates with inside multiplier I greater
than outside multiplier O > 0, minimize

    S/I + X*(1/O - 1/I).

Add this correction to the inherited variational center upper bound,
intersect with RC258's inverse-response upper, and update the signed-gap
lower using the pinned original source form. M = D^-1 L is still the
canonical metric, N the actual positive augmented operator, and N0 the
original Weil operator. D's diagonal is harmonic H_n+s, not n(n+1).

## Reproduction and scope

Generation and exact replay verify 212 inherited blob pins. Replay uses the
longer phase Taylor expansion and finer Bessel recurrence grid, reverses
source-mode summation, exact prime-boundary contribution summation,
captured-energy and coupled-energy sums, pin order and tau candidates, then
requires exact certificate equality.

From repository root:

    python scripts/validate_rpb108_rc259_coupled_augmentation_tail.py --output certificates/rpb108_rc259_coupled_augmentation_tail.json
    python scripts/validate_rpb108_rc259_coupled_augmentation_tail.py --output certificates/rpb108_rc259_coupled_augmentation_tail.json --replay

This remains two source tests with four trials per parity. The full rank-639
signed response and full original auxiliary norm gate remain unevaluated.
The separate eight-source canonical inverse width remains 485647/1000000.
Stage I, RH, F4 and Lean remain open/false.

Next: control the compressed-band projection defect or the complete omitted
source's Fourier leakage directly, or change the response trial. No original
Weil positivity floor or Stage I closure follows from this validator passing.
