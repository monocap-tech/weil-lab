# RPB108 RC256: retained-band positivity and physical-source inverse bound

Starting head: `01192e3c18e404601983bf5ce545c5438d02fe3e` (RC255).

RC256 uses additional structure of the same chosen rational augmented
operator. It preserves the original operator, augmentation coefficient,
kernel, sources, four-trial spaces, selected Z, and degree-256 residual
centers. No ideal-band operator is identified with the rational kernel.

RC112/RC115 give the full canonical lower form
`A_Q >= gamma I-p J_U*J_U`, while the actual rational augmentation is
`Hhat=A_Q+lambda Fhat*Fhat`, with lambda=5p/4. A certified canonical
operator error delta bounds Fhat-J_U. RC256 conservatively adds the
separate finite-kernel error again before forming delta^2, preserving all
comparison uncertainties.

For 0<tau<1/5, reverse Young gives

`||Fhat q||^2 >= (1-tau)||J_U q||^2-(1/tau-1)delta^2||q||_canonical^2`.

Consequently the same physical augmented form G=D N obeys

`G >= eta_tau L+beta_tau C_U`,

where `eta_tau=gamma-lambda(1/tau-1)delta^2` and
`beta_tau=lambda(1-tau)-p`. Both coefficients are strictly positive for
the selected parameters. C_U is the supported ideal Fourier-band form;
its comparison error has already been paid by reverse Young.

The canonical form L has Fourier weight log(e+|xi|), so this lower form
retains the explicit multiplier

`m_tau(xi)=eta_tau log(e+|xi|)+beta_tau 1_(|xi|<=U)`.

Inside the band it is at least eta_tau+beta_tau. Outside it is at least
eta_tau log(U). A rational lower bound for log(U) is obtained by power-of-two
range reduction and 100 positive atanh-series terms, with the remainder
also bounded. Thus G has a new global **physical L2** floor equal to the
smaller of these two multiplier bounds. This is not a new D-energy floor
for N or a positive floor for the original Weil form G0.

An exact finite search checks 1,000 rational tau values from 0.1 through
0.1999. It does not claim continuous optimality. Selected tau values and
physical floors are:

| Parity | Selected tau | Physical augmented form floor |
| --- | ---: | ---: |
| Even | 79/400 | 0.040950007779 |
| Odd | 987/5000 | 0.043281289774 |

For the actual residual e=N0 Pbase-N Z, its physical source
`g_e=D e=G0 Pbase-G Z` is in supported physical L2: polynomial inputs have
L2 endpoint logarithms, piecewise polynomial prime actions, and bounded
regular, pole, and augmentation actions. The inverse comparison gives

`e*D N^-1 e = g_e*G^-1 g_e <= ||g_e||_physical^2/c_physical`.

RC256 encloses the full physical source. The retained center coefficients
are multiplied by H(n)+s_mid, with both coefficient uncertainty and the
actual s interval paid. The physical endpoint remainder comes directly
from RC252's signed bracket and parity telescoping bound. The physical
prime remainder is the pinned complete-model norm remainder from RC250.
The augmentation remainder uses RC251's physical band-output bound times
lambda^2. These are physical bounds, not arbitrary D-energy tail bounds
rescaled by the first harmonic weight.

The three omitted physical components are combined in norm. Retained
and omitted model output blocks are orthogonal. The regular-kernel,
prime-arithmetic, pole-Taylor, and rational-augmentation global faults
are paid afterward in physical norm. Their source-side bounds are
recovered from the explicit RC248 formulas that divided physical squared
fault bounds by s_lower; this does not infer physical norm from a generic
D-norm error. The resulting complete physical source-energy upper bounds
are approximately 0.023814339432 even and 0.031638349372 odd.

| Source | Previous inverse upper | RC256 inverse upper | Reduction | RC256 signed gap interval |
| --- | ---: | ---: | ---: | --- |
| N0 P0 | 1.648943262 | 0.593215220 | 64.02% | [-0.504656024, 0.077109514] |
| N0 P1 | 2.384179020 | 0.745085472 | 68.75% | [-0.648002657, 0.083641806] |

Decimals are approximate; exact endpoints are in the certificate. The
inverse lower endpoints remain approximately 0.011449682251 and
0.013441009636. Positivity still requires an inverse upper below the
respective original source forms near 0.08856 and 0.09708; there is no
generic 0.5 threshold for these responses. Both signed intervals cross zero.

The retained multiplier also gives a stronger directional estimate. If
S bounds the full physical source norm squared and X bounds its full
Fourier energy outside U, with inside denominator I greater than outside
denominator O, then

`e*D N^-1 e <= S/I+X(1/O-1/I)`.

For tau=1/10 in both parities, the current S and variational center give
the following sufficient strict thresholds:

| Source | Required full physical residual-source Fourier energy outside U |
| --- | ---: |
| N0 P0 | < 0.002415315967 |
| N0 P1 | < 0.002345353098 |

These are conditional budgets, **not computed outside-energy bounds**.
They refer to the complete physical residual source and all its faults,
not omitted Legendre output energy. Meeting them would certify the two
source tests, not the complete rank-639 signed criterion.

Validation covers 203 inherited Git blob pins, the exact reverse-Young
slack identity, nonidentity-metric/noncommuting lower-form controls,
positive retained-band coefficients, rational logarithm bounds, full
physical-source error propagation, deterministic parameter selection,
exact conditional budget identities, and intersection with RC255.
Replay reverses parameter and exact energy-summation orders and requires
equality of the complete JSON certificate.

Run:
`python scripts/validate_rpb108_rc256_retained_band_inverse.py --output certificates/rpb108_rc256_retained_band_inverse.json`

Replay:
`python scripts/validate_rpb108_rc256_retained_band_inverse.py --output certificates/rpb108_rc256_retained_band_inverse.json --replay`

The full signed matrix has rank 639 (248 even, 391 odd) and remains
unevaluated. The original full auxiliary norm gate is open. The separate
canonical eight-source inverse width stays `485647/1000000`. Original N0,
augmented N, and canonical M remain distinct. Stage I, RH, F4, and Lean
remain open.

Next cursor RC257: certify the full physical residual source Fourier
energy outside U against the explicit two-band budget, or change the
response trial. Full signed positivity remains required.
