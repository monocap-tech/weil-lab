# RPB108 RC254: projected residual lower bounds and inverse-gate audit

Starting head: `0b32221fc4a32a11ec5de1304cf0ac24c3230878` (RC253).

RC254 separates the retained residual output from its omitted model tail
when computing a lower energy bound. This both improves the response
lower bounds and proves that continued tail refinement alone cannot close
the current fixed-trial, global-coercivity formulas for these two sources.
It does not prove an obstruction for the actual operator or the full
four-trial spaces.

The exact residual remains `e=N0 Pbase-N Z`, with the selected Z fixed.
Let P be the D-orthogonal Legendre output projection through degree 256.
RC251 supplies a retained center ehat and its finite coefficient-rounding
bound. The omitted model output has exactly zero projection under P.
The original global model faults and rational-augmentation comparison
fault can project into the retained block; their complete norm bounds
are still paid, without any independence or orthogonality assumption.

Thus, with delta_P equal to the finite rounding norm plus those global
fault norms,

`||e||_D^2 >= ||P e||_D^2 >= max(0, ||ehat||_(D,lower)-delta_P)^2`.

The omitted model tail cannot cancel the retained output. Earlier lower
bounds subtracted its norm together with all other errors, losing this
orthogonality. The upper residual bounds and complete error bounds from
RC253 remain unchanged.

| Source | Previous residual squared D-energy lower | RC254 lower |
| --- | ---: | ---: |
| N0 P0 | 0.000000513396 | 0.001222386904 |
| N0 P1 | 0.000021531205 | 0.001705026191 |

The pinned positive augmented upper operator bound nu gives
`T >= C_lower + residual_lower/nu`, where
`T=(N0 Pbase)*D N^-1(N0 Pbase)` and
`C=2 Re(Z*D N0 Pbase)-Z*D N Z`.

| Source | RC254 inverse interval | RC254 signed gap interval |
| --- | --- | --- |
| N0 P0 | [0.011449682251, 3.653532573170] | [-3.564973377141, 0.077109513778] |
| N0 P1 | [0.013441009636, 5.085598108536] | [-4.988515292782, 0.083641806118] |

All decimals are approximate; the certificate stores rational endpoints.
Neither signed interval establishes positivity or negativity.

For the same exact Z, every certified full residual energy upper rbar
must be at least the new actual residual lower r_lower, and every valid
upper variational center must be at least C_lower. Therefore every bound
of the current form `C_upper+rbar/mu`, using the unchanged global mu,
has floor `C_lower+r_lower/mu`.

| Source | Global mu | Floor of inverse UPPER formula | Original source form upper |
| --- | ---: | ---: | ---: |
| N0 P0 | 0.001369347373 | 0.904106954265 | 0.088559196029 |
| N0 P1 | 0.001301783373 | 1.323168991015 | 0.097082815754 |

The corresponding signed-gap LOWER formula ceilings are negative,
approximately -0.815547758236 and -1.226086175261. This obstruction covers
any improved residual norm upper bound for this fixed actual Z and mu,
including arbitrarily sharp tail calculations. It is a limitation of
the specified upper/lower certification formulas. It is **not a lower
bound on the true inverse response**, a negative Weil witness, or a
uniform obstruction for all coefficients in the four-trial spaces.

The next target can be expressed as a residual-specific inverse inequality

`e*D N^-1 e <= ||e||_D^2/kappa`.

No such improved kappa is certified here. It need not be a global lower
bound for N. For this fixed trial, the retained residual lower bounds give
a necessary strict kappa floor even with better norm enclosures. The
current residual upper bounds and source-form intervals also give a
sufficient strict threshold, conditional on proving the inverse inequality.

| Source | Necessary kappa floor | Sufficient kappa threshold with current enclosures | Sufficient/current mu |
| --- | ---: | ---: | ---: |
| N0 P0 | 0.015848253371 | 0.064858068896 | 47.36 |
| N0 P1 | 0.020376606679 | 0.079550801721 | 61.11 |

Strictly exceeding the sufficient thresholds with a valid inverse bound
would certify these two source tests. It would not evaluate or close the
full signed matrix criterion. Another route is to change the actual
response trial, including different coefficients in the existing spaces.

Validation covers 197 inherited Git blob pins, unchanged selected trial
coefficients and degree-256 centers, a nonidentity-metric projection
control with arbitrary omitted-output amplitudes and signed global
faults, the distinction between a coarse upper formula and a true inverse
lower bound, positive interval intersections, and the exact conditional
budget identities. Replay reverses exact summation order and requires
equality of the entire JSON certificate.

Run:
`python scripts/validate_rpb108_rc254_projected_residual_gate_audit.py --output certificates/rpb108_rc254_projected_residual_gate_audit.json`

Replay:
`python scripts/validate_rpb108_rc254_projected_residual_gate_audit.py --output certificates/rpb108_rc254_projected_residual_gate_audit.json --replay`

The rank-639 signed response matrix (248 even, 391 odd) remains
unevaluated. The original full auxiliary norm gate is open. The separate
canonical eight-source inverse width stays `485647/1000000`. Original N0,
augmented N, and canonical inverse M remain distinct. Stage I, RH, F4,
and Lean remain open.

Next cursor RC255: strengthen the residual-specific inverse estimate or
change the actual response trial. Further tail refinement alone cannot
close the fixed-trial, current-mu source tests.
