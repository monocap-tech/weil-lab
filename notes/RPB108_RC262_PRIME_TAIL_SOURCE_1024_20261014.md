# RC262 — prime output through 2048 and physical source through 1024

Parent: `a2fe7d7ca0653d2c3e17c2bc2efe7d771814c8de` (RC261).
Branch: `research/rpb108-route-consolidation`.

RC262 extends the original prime model's certified output to degree 2048,
assembles the complete retained physical residual through degree 1024, and
evaluates its full Fourier quadratic form. Both source inverse upper bounds
improve. The sources, four trials per parity, fixed exact Z, and chosen actual
rational augmentation are unchanged. Neither signed gap nor Stage I closes.

| Actual full-source upper bound | RC261 even | RC262 even | RC261 odd | RC262 odd |
| --- | ---: | ---: | ---: | ---: |
| Outside Fourier energy | 0.007689894 | 0.006810417 | 0.007229871 | 0.005740809 |
| Original-action inverse response | 0.208890536 | 0.187684022 | 0.206396443 | 0.171214893 |

Decimals are rounded outward for display. Exact rational bounds are stored
in the certificate. Signed-gap lower bounds improve to approximately
-0.099125 even and -0.074133 odd, and remain below zero. The original source
forms are approximately 0.088559 and 0.097083. An inverse upper bound above
these values does not prove a negative actual signed gap.

The new prime physical tail bounds beyond degree 2048 are 0.000328730 even
and 0.000335903 odd. The previous prime bounds were about 0.001543459 and
0.001293386 beyond degree 512. These tail quantities have different output
cutoffs; the comparable complete-source bounds are in the table above.

## Interval prime boundary projections

The same exact rational chosen prime coefficients and translations reconstruct
all fourteen translated terms and fifteen physical polynomial segments for
Q = Pbase-Z. Their complete segment digest and full physical norm must match
RC250. Every boundary jump polynomial is reconstructed exactly from its
Legendre coefficients. Reflection supplies the negative boundaries from
the seven positive ones, at matching parity.

For the jump polynomial u at a positive boundary b, write

    v_n(t) = sum_d u_d P_d(t)/(n(n+1)-d(d+1)).

The Legendre Sturm--Liouville identity gives its boundary contribution

    (1-b^2)*(v_n'(b)P_n(b)-v_n(b)P_n'(b)).

Summing all positive jumps and multiplying by 2n+1 gives the exact prime
Legendre output coefficient at matching parity. All prime and input-mode
cross terms remain included before any physical energy is computed.

High Legendre values are propagated by outward interval recurrence through
2048, on 1500-decimal grids in generation and 1540-decimal grids in replay.
Only two high-precision recurrence states are needed at once. Stored boundary
values and jump-resolvent factors use 120-decimal intervals, 140 in replay.
The final prime coefficients have 60-decimal outward endpoints. Every stored
Legendre interval must have width below 1e-110 and every final prime interval
below 1e-50. These are checked interval widths, not sampling assumptions.

Exact low Legendre polynomial evaluations check the recurrence at each
boundary. Three additional prime-output controls per parity, all through
degree 512, must intersect intervals independently reconstructed from RC259's
complete physical source, endpoint and band-output enclosures. No low-output
coefficient or prime parameter is silently replaced.

## Infinite original-output remainder

For each newly projected prime mode, the minimum absolute interval value
gives a physical energy lower bound mass(n)*minabs(coefficient)^2. Orthogonality
therefore gives

    prime_tail_above_2048
      <= pinned_prime_tail_above_512
         - captured_prime_energy_513_through_2048_lower.

All captures are rounded downward; the remaining bound is rounded upward
and checked positive. This subtraction uses the same model, full physical
norm and coefficient normalization as RC253. It does not convert a D-norm
error to a physical norm.

RC252's signed endpoint bracket is evaluated at first omitted matching
degree 2050 even or 2049 odd. Its direct physical bound is

    2B * bracket_upper^2 * parity_telescoping_weight_sum_upper.

Above 2048 only, combine the endpoint and prime physical bounds in norm.
For degrees 1025 through 2048, combine the signed endpoint coefficient and
prime interval before squaring and sum their physical energies. Orthogonality
then adds this explicit block to the remaining squared norm above 2048.
The regular model is zero above degree 256; identity and pole model outputs
also have lower degree. Thus this is the entire original-model tail above
1024. All original approximation faults remain paid globally.

RC260's compression-defect-free analytic ideal-band output tail above 1024
is multiplied by lambda^2 and combined in norm with that original tail.
The complete model physical-source tail above 1024 is bounded by
0.000764558 even and 0.000622447 odd. No remaining infinite output is dropped.

## Complete retained source through 1024

The exact retained physical centers through 512 are reused from RC261. For
each new mode 513 through 1024, form an interval for

    endpoint_n + prime_n - lambda*(C_U Z)_n,

using the new prime interval and RC260's pinned band Gram. Its center and
radius are stored explicitly. The new per-mode physical coefficient errors
are added orthogonally to the inherited retained uncertainty. The totals
are below 2.830e-41 even and 1.598e-41 odd.

All retained coefficient and actual-s uncertainty, regular-kernel error,
prime-arithmetic error, pole-Taylor error and actual rational-augmentation
comparison faults remain paid. The ideal C_U does not replace the actual
rational augmentation.

The actual source is still g_e = D e = G0 Pbase-G Z, with
e = N0 Pbase-N Z. N is the actual chosen positive augmentation of N0; it is
separate from the canonical metric M=D^-1 L. D's diagonal is harmonic H_n+s.
The n(n+1) parameters appear only in the separate Sturm--Liouville identities.
Degree 1024 is an output cutoff, not an increased response trial count.

## Degree-1024 Fourier quadratic form

RC261's stable calculation is extended to all retained degree pairs. For
n != d of matching parity, use the off-diagonal spherical-Bessel boundary
identity. For the diagonal integrals J_n = integral_z^infinity j_n(t)^2 dt,
use

    (2n+3)J_(n+1) = (2n+1)J_n + z*(j_n(z)^2+j_(n+1)(z)^2).

The base J_0 = 1/(2z)-Re(I_2)/2 uses 500 integration-by-parts terms in
generation and 520 in replay. Initial endpoint values and derivatives use
RC260's high-precision routine through 1024. Endpoint, diagonal and streaming
quadratic accumulator intervals use 120-decimal outward grids in generation,
140 in replay. Streaming bounds the working arithmetic size while preserving
every diagonal and off-diagonal term.

The degree-512 principal block is accumulated separately and must intersect
RC261's pinned Fourier certificate. Source-mode order and every streaming
term order reverse during replay. The original pinned pi displacement and
prefactor error is again paid globally using the squared sum of absolute
retained physical source coefficients. Final energies use 24-decimal outward
endpoints. Both retained Fourier energies are strictly between zero and the
exact physical polynomial energies.

## Actual source and inverse response

With retained polynomial physical energy A, outside upper Y, and complete
model tail R above 1024, RC258's checked regime Y(A+R)<=A^2 gives

    ||P_out(p+q_model)||^2
      <= (sqrt(Y)+sqrt((1-Y/A)R))^2.

The finite retained uncertainty and unchanged global physical faults are
subsequently paid in norm. Actual full-source total energy S and outside
energy X are intersected with RC261. Reverse-triangle lower bounds are also
intersected with the prior bounds. The validator checks
0 <= X_lower <= X_upper <= S.

For the same 1000 rational tau candidates with I>O>0, minimize

    <e,N^-1 e>_D <= S/I + X_upper*(1/O-1/I).

Add the correction to the unchanged variational center upper, intersect
with RC261's inverse upper, and update the signed-gap lower using the pinned
original source form. All reported improvements concern the same actual
operator, domain and two sources. No positive floor for the original Weil
operator is inferred from the augmented estimates.

## Validation and remaining obligations

Generation and exact replay verify 221 inherited blob pins. Replay uses
finer prime-boundary and Fourier grids, RC260's longer endpoint Taylor
construction, the longer base integral expansion, reversed boundary/source
and energy sums, reversed tau candidates and pin order, and requires exact
certificate equality. The reused earlier prime and source certificates
remain pinned; they are not claimed to be regenerated in full.

From repository root:

    python scripts/validate_rpb108_rc262_prime_tail_source_1024.py --output certificates/rpb108_rc262_prime_tail_source_1024.json
    python scripts/validate_rpb108_rc262_prime_tail_source_1024.py --output certificates/rpb108_rc262_prime_tail_source_1024.json --replay

The full rank-639 signed response and original full auxiliary norm gate
remain unevaluated. The separate eight-source canonical inverse width stays
485647/1000000. Stage I, RH, F4 and Lean remain open/false.

Next: sharpen the retained-source inverse frequency multiplier or change
the response trial. The remaining prime output is explicitly bounded;
further cutoff extension alone is not asserted to close the signed gaps.
