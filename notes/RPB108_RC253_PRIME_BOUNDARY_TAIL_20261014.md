# RPB108 RC253: exact prime boundary projections through degree 512

Starting head: `a69d9769095b75a0ede918ecbf9266c8ba3cf741` (RC252).

RC253 introduces a boundary formula for high-degree Legendre projections
of the same rational prime model used in RC248/RC250. It extends that
model's projections through degree 512, preserving all seven prime pairs,
fifteen support segments, input cross terms, and cross-prime terms.
The original prime parameter uncertainties remain paid by the unchanged
global arithmetic fault. No new prime approximation is substituted.

Let `L u=-((1-t^2)u')'`. For a polynomial segment
`u=sum_(d=0)^64 u_d P_d` and n>64, define

`v_n=sum_d u_d P_d/[n(n+1)-d(d+1)]`.

The Legendre identity `L P_d=d(d+1)P_d` gives
`(n(n+1)-L)v_n=u`. Green's identity then gives

`integral_l^r u P_n = [(1-t^2)(v_n' P_n-v_n P_n')]_l^r`.

Segment contributions combine into jumps at the interior boundaries;
the exterior endpoints contribute zero. Exact parity reduces fourteen
interior boundaries to seven positive boundaries. Each jump polynomial
is reconstructed from its Legendre coefficients. Values and derivatives
are evaluated by rational Legendre recurrence. Degrees through 64 use
direct polynomial integration, avoiding singular resolvent denominators.

The complete segment-polynomial digest and full physical prime model
norm match RC250. The raw coefficient digest through degree 256 matches
RC250 exactly, checking every old coefficient, including the boundary
formula beyond the input degree. A new digest records all coefficients
through degree 512. The global prime norm minus captured output energy
bounds the physical remainder; the first omitted harmonic weight converts
it to squared D-energy.

For degrees 257 through 512, the endpoint and prime outputs are combined
with their signs before squaring. The other original polynomial model
outputs vanish beyond 256, as certified by RC250. Endpoint output beyond
512 uses RC252's signed-moment/parity bound, intersected with its explicit
endpoint-energy sum through 1024 plus its remaining bound. The endpoint
and prime remainder norms are combined after 512. This output block is
orthogonal to the explicit block. The better original tail is propagated
through the unchanged degree-256 residual center, augmentation tail, and
all global original/rational-augmentation model faults.

| Source | Original squared D-tail before | Original squared D-tail after |
| --- | ---: | ---: |
| N0 P0 residual input | 0.000317985489 | 0.000282313904 |
| N0 P1 residual input | 0.000362982331 | 0.000324286594 |

| Source | RC252 inverse upper | RC253 inverse upper | Reduction | RC253 signed gap interval |
| --- | ---: | ---: | ---: | --- |
| N0 P0 | 3.760538040 | 3.653532573 | 2.85% | [-3.564973377, 0.077120767] |
| N0 P1 | 5.216778132 | 5.085598109 | 2.51% | [-4.988515293, 0.083675241] |

Decimals are approximate. The certificate stores rational endpoints.
The even inverse lower endpoint remains approximately 0.011438428829;
the odd lower endpoint improves to approximately 0.013407574593.
Complete residual squared D-error bounds are approximately 0.001221572904
and 0.001467370142. Both actual residual squared D-energy lower bounds
are now positive: approximately 0.000000513396 and 0.000021531205.
Residual nonvanishing does not prove a negative signed gap or obstruct a
successful inverse estimate. Both signed intervals still cross zero.

Validation covers 194 inherited Git blob pins, exact polynomial
Sturm-Liouville controls, direct Green-boundary integration controls,
jump-polynomial reconstruction, low boundary value/derivative controls,
the full old coefficient digest, the unchanged segment/norm controls,
and nonnegative physical prime remainder. Replay reverses boundary and
exact output-energy summation orders and requires complete JSON equality.

Run:
`python scripts/validate_rpb108_rc253_prime_boundary_tail.py --output certificates/rpb108_rc253_prime_boundary_tail.json`

Replay:
`python scripts/validate_rpb108_rc253_prime_boundary_tail.py --output certificates/rpb108_rc253_prime_boundary_tail.json --replay`

The sources and four-trial spaces are unchanged. The rank-639 signed
response matrix (248 even, 391 odd) remains unevaluated, and the original
full auxiliary norm gate is open. The separate canonical eight-source
inverse width stays `485647/1000000`. Original N0, augmented N, and
canonical inverse M remain distinct. Stage I, RH, F4, and Lean remain open.

Next cursor RC254: exploit the boundary interface for further prime tails,
or improve the band remainder and residual inverse estimates, while
retaining the full signed positivity requirement.
