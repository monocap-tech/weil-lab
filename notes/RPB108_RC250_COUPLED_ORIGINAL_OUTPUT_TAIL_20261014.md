# RPB108 RC250: coupled original output tails

Starting head: `c518f086e9a5f30c745e6212f3801073b5980022` (RC249).

RC250 improves the complete direct residual certificates from RC248
without changing their retained centers or trial coefficients. For each
selected exact polynomial Z, the residual remains
`e=N0(Pbase-Z)-lambda D^-1 Fhat*Fhat Z`.
The sources remain N0 P0 and N0 P1, with four trials per parity.
RC249's stronger accepted endpoints are included by intersection.

The dominant original-action error came from omitted prime output.
RC250 extends the exact Legendre projections of the full seven-pair,
fifteen-segment prime model from degree 128 through degree 256. The input
polynomial, chosen rational prime parameters, full prime output norm,
segment digest, and all parameter-rounding controls match RC248 exactly.
Every retained original coefficient and radius through degree 128 is
reconstructed and compared with RC248's stored values.
The prime arithmetic error is also exactly replayed.

For each same-parity degree 129 through 256, the endpoint, prime, and
regular model outputs are added with their signs **before squaring**.
Their weighted energy uses `mass(n)/(H(n)+s_lower)`. This retains all
cross terms within the explicit output block. The regular model has
exactly zero output beyond 256. The remaining endpoint and prime tails
are bounded in norm, using the first omitted harmonic weight for prime
output. The explicit block and the beyond-256 block are orthogonal, so
their squared bounds are added.

The inherited augmentation omitted-output norm is recovered from
RC248's stored bound `(old_original_tail_norm+augmentation_tail_norm)^2`:
an upward square root minus its exact stored original tail norm remains
an upper bound for that augmentation norm. No new band action is assumed.
Finite coefficient rounding, all original model faults, and the full
rational augmentation comparison remain paid. The sharper original tail
is then propagated through the same direct residual inverse identities.

| Source | Previous inverse upper | RC250 inverse upper | Reduction | RC250 signed gap interval |
| --- | ---: | ---: | ---: | --- |
| N0 P0 | 4.493986789 | 4.281277614 | 4.73% | [-4.192718418, 0.077120767] |
| N0 P1 | 6.339354546 | 6.050710991 | 4.55% | [-5.953628176, 0.083675302] |

Decimal values are approximate; exact rational endpoints are in the
certificate. The inverse lower endpoints remain approximately
0.011438429 and 0.013407514.

| Bound | Even | Odd |
| --- | ---: | ---: |
| Previous separate original omitted squared D-norm | 0.000797222727 | 0.001034866345 |
| Coupled original omitted squared D-norm | 0.000694513041 | 0.000904270662 |
| Previous complete residual squared D-error | 0.002220472350 | 0.002849195031 |
| RC250 complete residual squared D-error | 0.002046691141 | 0.002629598031 |

Validation covers 185 inherited Git blob pins, exact prime model and
retained-coefficient replay, full cross-prime terms, all fifteen segment
norm controls, parity zeros, monotone harmonic tail weights, and signed
component cross terms with orthogonal output blocks. The extended prime
projection cutoff is restored after each call. Replay reverses exact
prime-segment and tail-energy summation orders and requires equality of
the entire certificate JSON.

Run:
`python scripts/validate_rpb108_rc250_coupled_original_output_tail.py --output certificates/rpb108_rc250_coupled_original_output_tail.json`

Replay:
`python scripts/validate_rpb108_rc250_coupled_original_output_tail.py --output certificates/rpb108_rc250_coupled_original_output_tail.json --replay`

Neither signed interval certifies positivity or negativity. The full
signed response matrix of rank 639 (248 even, 391 odd) remains unevaluated.
The original full auxiliary norm gate remains open. The separate canonical
eight-source inverse width remains `485647/1000000`. Original N0,
augmented N, and canonical inverse M remain distinct. Stage I, RH, F4,
and Lean remain open.

Next cursor RC251: materialize further coupled residual output or
strengthen residual inverse coercivity, while retaining the full signed
positivity requirement.
