# RPB108 RC248: direct coupled residual certificates

Starting head: `8b2e080af767cde8ce0f8d1d094493e927ff383b` (RC247).

RC248 certifies the selected RC247 four-trial residual directly as
`e = N0(Pbase - Z) - lambda D^-1 Fhat*Fhat Z = N0 Pbase - N Z`.
The sources remain `N0 P0` and `N0 P1`; the trial spaces remain
`[P0,P2,P4,R0]` and `[P1,P3,P5,R1]`. No original/augmented operator
commutation or original inverse is assumed.

The exact rational polynomial `Pbase-Z` is acted on as one input. The
regular kernel, all seven prime pairs and fifteen support segments, signed
poles, and endpoint action retain input cross terms. Output coefficients
are retained through degree 128. The endpoint, regular, and prime omitted
outputs and kernel, prime arithmetic, and pole Taylor faults are paid.
Prime parameter rounding is included in the 16-digit model fault.

The aggregate band action is likewise materialized on the exact polynomial
`Z`. Its input pairing is intersected with an independent full Fourier
inside/outside energy partition. The positive contraction inequality
`C^2 <= C` bounds omitted output using that pairing minus captured output
energy. The physical/rational augmentation comparison is paid separately.
Finite and omitted output degrees are orthogonal; global model faults are
then combined by the norm triangle inequality. Separate source and trial
action errors are not added for this direct residual.

The direct residual energy enclosure yields variational inverse-response
and signed-gap intervals using the pinned positive augmented bounds.
These are intersected with RC247, preserving its stronger lower endpoints.
All displayed decimal values below are approximate; the certificate stores
exact rational endpoints.

| Source | RC247 inverse upper | RC248 inverse upper | Reduction | RC248 inverse lower | Signed gap interval |
| --- | ---: | ---: | ---: | ---: | --- |
| N0 P0 | 5.415606202 | 4.493986789 | 17.02% | 0.011438429 | [-4.405427593, 0.077120767] |
| N0 P1 | 7.063101490 | 6.339861093 | 10.24% | 0.013407514 | [-6.242778277, 0.083675302] |

Complete direct residual squared D-error bounds are approximately
0.002220472350 (even) and 0.002849195031 (odd). Actual residual squared
D-energy upper bounds are approximately 0.006137850664 and 0.008234781300.
The certified residual energy lower bounds are zero. Neither signed gap
has a certified positive lower endpoint or negative upper endpoint.

Validation: 179 inherited Git blob pins; exact input mass replay; parity
zeros; complete input/output and model controls; an exact nonidentity
metric, noncommuting two-dimensional residual identity control. Replay
reverses exact summation order and uses the inherited higher-order band
and Fourier partition replay before requiring equality of the entire JSON.

Run:
`python scripts/validate_rpb108_rc248_direct_coupled_residual.py --output certificates/rpb108_rc248_direct_coupled_residual.json`

Replay:
`python scripts/validate_rpb108_rc248_direct_coupled_residual.py --output certificates/rpb108_rc248_direct_coupled_residual.json --replay`

The full signed response criterion has rank 639 (248 even, 391 odd) and
remains unevaluated. The original full auxiliary norm gate is open. The
canonical eight-source inverse width remains `485647/1000000`, a separate
quantity. Stage I, RH, F4, and Lean remain open.

Next cursor RC249: refine direct output tails or strengthen residual
inverse estimates, while retaining the full signed positivity requirement.
