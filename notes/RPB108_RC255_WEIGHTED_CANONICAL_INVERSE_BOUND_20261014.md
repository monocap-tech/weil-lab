# RPB108 RC255: weighted inverse comparison and orthogonal model outputs

Starting head: `6b615e60439ee3c03a7277e0bc9f0a675bae3f00` (RC254).

RC255 improves the actual augmented inverse-response upper bounds while
keeping the same sources, four-trial spaces, selected exact Z, and
degree-256 residual centers. It combines an orthogonal model-output
upper bound with a valid comparison through the canonical metric.
Original N0, augmented N, and canonical metric M remain distinct.
No commutation or operator identification is assumed.

First, the retained model output plus its finite coefficient uncertainty
is orthogonal to the omitted model output. If nh bounds the retained
center energy, f bounds finite rounding energy, and t bounds omitted
model energy, the complete model energy is at most

`(sqrt_up(nh)+sqrt_up(f))^2+t`.

The original global model faults and rational augmentation discrepancy
can occupy both output blocks. They are added afterward in norm. This
improves the full residual squared D-energy upper bounds to approximately
0.002515174007 (even) and 0.003377311945 (odd), preserving all uncertainties.
The stronger lower bounds from RC254 remain in force.

For the inverse comparison, write M=D^-1 L for the actual canonical
metric's D-Riesz operator. The pinned canonical augmentation floor gives
`N >= eta M` in D energy. The actual canonical embedding gives
`L >= rho^-1 I_physical`, with rho=252/257. Also

`L=D+h-r I+R >= D-r I`, with r=789/125,

because h and the supported Fourier operator R with multiplier
log(1+e/|xi|) are positive. Convex combination gives the diagonal lower
form

`W_theta=(1-theta)D+[theta/rho-(1-theta)r]I_physical`.

For positive W_theta, inverse order in the common D metric yields

`N^-1 <= eta^-1 M^-1 <= eta^-1(D^-1 W_theta)^-1`.

This is an operator inequality, not replacement of N by M. Its proof
uses positivity and inverse order, and applies on the entire common form
domain. A nonidentity-metric, noncommuting rational control checks the
inverse order by congruence.

Put A=1-theta and C=theta/rho-A r. A relative global lower metric bound
is `beta=min(A,A+C/s_lower)>0`. On omitted degrees starting at n_first,
one may use `beta_tail=min(A,A+C/(H(n_first)+s_lower))`. The retained
center energy in this inverse metric uses the weights
`mass(n) d^2/(A d+C)`, where d=H(n)+s. The maximum over the actual s
interval occurs at an endpoint: this function has second derivative
`2 C^2/(A d+C)^3>=0`.

Finite rounding and global faults are paid with beta; the omitted model
energy uses beta_tail. Retained and omitted outputs remain orthogonal
in this diagonal weight. Every energy summand is rounded outward.
The validator searches 236 rational theta values from 0.715 through
0.950 in steps of 0.001. This is a finite certified search, not a claim
of continuous optimality. The selected weights are 371/500 (even) and
189/250 (odd).

| Source | Previous inverse upper | RC255 inverse upper | Reduction | RC255 signed gap interval |
| --- | ---: | ---: | ---: | --- |
| N0 P0 | 3.653532573 | 1.648943262 | 54.87% | [-1.560384066, 0.077109514] |
| N0 P1 | 5.085598109 | 2.384179020 | 53.12% | [-2.287096204, 0.083641806] |

Decimals are approximate; exact rational bounds are in the certificate.
The inverse lower endpoints remain approximately 0.011449682251 and
0.013441009636. Neither signed interval certifies positivity or negativity.

RC255 also identifies a limit of the canonical comparison. Since M<=2I
in D energy, M^-1>=I/2. For the same fixed Z and eta, any upper formula
obtained purely through eta^-1 M^-1 therefore has floor

`C_lower+residual_energy_lower/(2 eta)`.

This floor is approximately 0.073513194484 (even) and 0.104499488791
(odd). The odd floor exceeds the original source form upper bound,
approximately 0.097082815754. Thus even a perfect canonical inverse solve
cannot close this fixed odd source test through this comparison alone.
The even case is not excluded by this floor. These are limitations of
the comparison formula, not lower bounds on the true N inverse response
or negative original Weil witnesses. Changing Z or using stronger
information about N is outside this obstruction.

Validation covers 200 inherited Git blob pins, the full-domain canonical
metric and embedding constants, noncommuting inverse-order controls,
orthogonal weighted output blocks, positive diagonal weights, outward
arithmetic, deterministic finite-search selection, and intersection with
RC254. Replay reverses weight and exact energy-summation orders and
requires equality of the entire JSON certificate.

Run:
`python scripts/validate_rpb108_rc255_weighted_canonical_inverse_bound.py --output certificates/rpb108_rc255_weighted_canonical_inverse_bound.json`

Replay:
`python scripts/validate_rpb108_rc255_weighted_canonical_inverse_bound.py --output certificates/rpb108_rc255_weighted_canonical_inverse_bound.json --replay`

The rank-639 signed response matrix (248 even, 391 odd) remains unevaluated.
The original full auxiliary norm gate is open. The separate canonical
eight-source inverse width stays `485647/1000000`. Stage I, RH, F4, and
Lean remain open.

Next cursor RC256: obtain N-specific residual inverse control or change
the actual response trial. The fixed odd source cannot close using only
eta^-1 M^-1 domination.
