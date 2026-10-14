# RC258 — coupled physical tail and orthogonal Fourier enclosure

Parent: `a20af51b6db12c82cf5e9bde3d524f10fb13de77` (RC257).
Branch: `research/rpb108-route-consolidation`.

RC258 improves both source inverse-response upper bounds by coupling the
original endpoint/prime output before measuring its physical energy, and by
using physical orthogonality in the Fourier-tail estimate. The two sources,
four trials per parity, fixed trial Z, degree-256 retained polynomial, and
actual rational augmentation are unchanged. No signed gap is closed.

| Certified upper bound | RC257 even | RC258 even | RC257 odd | RC258 odd |
| --- | ---: | ---: | ---: | ---: |
| Actual full-source outside Fourier energy | 0.023814340 | 0.020907928 | 0.027474918 | 0.024547032 |
| Actual source inverse response | 0.593215220 | 0.529975291 | 0.670898393 | 0.608475141 |

Decimals are outward display values; the certificate contains exact rational
bounds. Both actual inverse upper bounds improve. Neither Fourier allowance
meets its recomputed sufficient strict two-band budget. This does not prove
that either actual source violates that budget.

## Coupled physical output beyond degree 256

The physical residual source remains g_e = D e = G0 Pbase - G Z, where
e = N0 Pbase - N Z. The D diagonal is H_n+s with harmonic H_n. The actual
augmented N is separate from the canonical metric M = D^-1 L.

RC250 proves that the regular model output is exactly zero above degree 256;
the pole model has degree at most 40, and the identity input degree is at most
64. Original model output above 256 is therefore just endpoint plus prime.

For 257 through 512, RC253 stores each coupled output's bound explicitly as
mass(n)*(endpoint_n+prime_n)^2/(H_n+s_lower), rounded upward. Multiplication
by the same positive H_n+s_lower gives a valid physical numerator bound.
This uses that explicit coefficient formula; it is not a generic comparison
of arbitrary D and physical norms. The n(n+1) in the separate boundary
resolvent is not substituted for the harmonic D diagonal.

Beyond 512, RC252's signed endpoint bracket and parity telescoping weight
give the physical endpoint bound 2B*bracket_upper^2*weight_sum_upper. RC253
already certifies the prime physical energy beyond 512. The triangle
inequality combines only that remaining block. Orthogonality adds this
block's squared norm to the explicit 257-through-512 block. The result is
intersected with the inherited original physical bound.

The rational augmentation's omitted model output is then added in norm.
The complete model physical tail energy R decreases from approximately
0.0123795804 to 0.0119517338 even, and from 0.0141288254 to 0.0136411078 odd.
All regular-kernel, prime-arithmetic, pole-Taylor, finite-coefficient,
actual-s and rational-augmentation errors remain paid.

## Orthogonality-constrained Fourier bound

Let p be RC257's complete retained physical polynomial, q the omitted model
output, and P the full-line orthogonal Fourier projection outside U. Write

    ||p||^2 = A,  <p,q> = 0,  ||q||^2 <= R,
    ||P p||^2 <= Y < A.

The orthogonality is physical Legendre orthogonality between degrees at most
256 and degrees above 256. It does not identify Legendre output tails with
Fourier tails. RC257's pinned Fourier calculation supplies A and Y with all
retained mode cross terms already included.

For any unit vector w in the outside Fourier subspace, set
t = |<w,p>|/sqrt(A). Then t <= sqrt(Y/A), and orthogonality implies

    |<w,p+q>| <= sqrt(A)t + sqrt(R)sqrt(1-t^2).

If Y(A+R) <= A^2, this scalar function increases throughout the allowed
t interval. Hence

    ||P(p+q)||^2 <= (sqrt(Y) + sqrt((1-Y/A)R))^2.

The validator checks this nonsaturated condition in both actual parities.
Its general helper falls back to A+R when the condition fails. This is
stronger than the unstructured triangle expression
(sqrt(Y)+sqrt(R))^2. A sharp rational two-dimensional projection control
checks normalization; an aligned counterexample checks that dropping the
orthogonality assumption would invalidate the bound.

The retained finite uncertainty and all global faults are subsequently paid
in norm. Thus the final X bounds the outside Fourier energy of the actual
full physical residual source. The actual total source energy S is also
recomputed using orthogonality of retained and omitted physical blocks.
Both S and X are intersected with the inherited bounds.

For RC256's retained lower form G >= eta_tau L + beta_tau C_U, let
I = eta_tau+beta_tau and O = eta_tau log(U)_lower. When I>O>0,

    <e,N^-1 e>_D <= S/I + X(1/O - 1/I).

The same 1000 rational tau candidates are searched; no continuous optimum is
claimed. The least certified correction yields the inverse-response upper,
which is intersected with RC257. Signed-gap lower bounds are updated using
the pinned original source form lower bounds. The sufficient outside budget
is recomputed with the smaller total physical source bound S.

## Validation and remaining obligations

Generation and exact replay verify all 209 inherited blob pins. Replay
reverses the explicit physical energy sum, tau-search candidates and pin
order, and requires exact certificate equality. RC257's expensive Fourier
integrals are reused from its pinned certificate; this pass does not claim
to regenerate them.

From repository root:

    python scripts/validate_rpb108_rc258_orthogonal_physical_tail.py --output certificates/rpb108_rc258_orthogonal_physical_tail.json
    python scripts/validate_rpb108_rc258_orthogonal_physical_tail.py --output certificates/rpb108_rc258_orthogonal_physical_tail.json --replay

The full rank-639 signed response and original full auxiliary norm gate are
unevaluated. The separate eight-source canonical inverse width remains
485647/1000000. Stage I, RH, F4 and Lean remain open/false. The original Weil
operator has not acquired a positive floor from these augmented estimates.

Next: RC259 should materialize augmentation output beyond degree 256 or
control complete omitted-source Fourier leakage directly. Closure of these
two source tests would still leave the full signed criterion to certify.
