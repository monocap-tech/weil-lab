# RPB108 RC252: signed endpoint moments and parity tail

Starting head: `efc004271794aa8a893b3ced386adab079d01b9d` (RC251).

RC252 sharpens the endpoint part of the existing degree-256 coupled
residual certificate. Sources, four-trial spaces, selected coefficients,
retained residual centers, prime tails, augmentation tails, and all
global model faults are preserved. The residual remains
`N0(Pbase-Z)-lambda D^-1 Fhat*Fhat Z`.

For the exact combined original-action input with Legendre coefficients
a_d, every endpoint output degree n above the input degree satisfies

`h_n=(2n+1) sum_d a_d/[n(n+1)-d(d+1)]`.

Set x=n(n+1), t_d=d(d+1), and M_k=sum_d a_d t_d^k. An exact finite
geometric expansion gives

`x sum_d a_d/(x-t_d) = sum_(k=0)^3 M_k/x^k + R(x)`.

For x>=x_first>max t_d, the remainder has absolute upper bound
`sum_d |a_d| t_d^4/[x_first^4(1-max(t_d)/x_first)]`.
Signed input moments are formed before bounding. Positive and negative
moments yield a uniform interval for the combined bracket on the entire
tail; its lower endpoint is positive in both parity cases. This is a
statement about the endpoint model coefficients, not Weil positivity.

The squared D-energy weight simplifies using

`(2n+1)/[n^2(n+1)^2] = 1/n^2-1/(n+1)^2 = f(n)`.

The positive sequence f decreases. The sum over both parities telescopes
to 1/first^2, and the alternating sum is at most f(first). Therefore the
same-parity sum is at most `(1/first^2+f(first))/2`. Together with the
uniform bracket bound and the first omitted harmonic weight, this gives
a rigorous endpoint tail bound over infinitely many degrees.

RC252 also sums the exact combined endpoint outputs of the relevant
parity from degree 257/258 through 1023/1024, paying outward rounding on
each squared energy. The remaining tail uses the signed-moment and parity
bound at degree 1025/1026. Each explicit coefficient is checked against
the independent rational-denominator expression above; its logarithm
uncertainty is exactly zero. The better of the direct uniform and explicit
plus remaining bounds is accepted and intersected with the previous bound.

| Source | Endpoint squared D-tail before | Endpoint squared D-tail after | Reduction |
| --- | ---: | ---: | ---: |
| N0 P0 residual input | 0.000010560545 | 0.000001010642 | 90.43% |
| N0 P1 residual input | 0.000011285370 | 0.000000953473 | 91.55% |

The refined endpoint norm is combined with the unchanged prime remainder,
then with the unchanged augmentation remainder. Finite output rounding
is orthogonal to omitted output degrees. Original global faults and the
rational augmentation discrepancy remain paid in norm. The same positive
augmented inverse identities propagate the result.

| Source | RC251 inverse upper | RC252 inverse upper | Reduction | RC252 signed gap interval |
| --- | ---: | ---: | ---: | --- |
| N0 P0 | 3.999083723 | 3.760538040 | 5.97% | [-3.671978844, 0.077120767] |
| N0 P1 | 5.522428343 | 5.216778132 | 5.53% | [-5.119695317, 0.083675302] |

Decimals are approximate. The certificate stores exact rational bounds.
Complete residual squared D-error bounds are approximately 0.001294629153
and 0.001548454267. The odd actual residual squared D-energy lower bound
improves to approximately 0.000012931482; the even lower bound is zero.
The prior inverse lower endpoints remain approximately 0.011438429 and
0.013407514. Neither signed interval certifies positivity or negativity.

Validation covers 191 inherited Git blob pins, a polynomial proof of the
finite geometric identity for all actual input degrees, the positive
finite-difference numerator `6n^2+12n+4`, exact telescoping controls,
explicit endpoint coefficient replay, signed bracket bounds, and unchanged
residual-center energy evaluation. Replay reverses input traversal and
exact energy-summation order and requires equality of the entire JSON.

Run:
`python scripts/validate_rpb108_rc252_signed_endpoint_tail.py --output certificates/rpb108_rc252_signed_endpoint_tail.json`

Replay:
`python scripts/validate_rpb108_rc252_signed_endpoint_tail.py --output certificates/rpb108_rc252_signed_endpoint_tail.json --replay`

The rank-639 signed response criterion (248 even, 391 odd) remains
unevaluated. The original full auxiliary norm gate is open. The separate
canonical eight-source inverse width stays `485647/1000000`. Original N0,
augmented N, and canonical inverse M remain distinct. Stage I, RH, F4,
and Lean remain open.

Next cursor RC253: sharpen the remaining prime or band omitted output,
or strengthen the residual inverse estimate, while retaining the full
signed positivity requirement.
