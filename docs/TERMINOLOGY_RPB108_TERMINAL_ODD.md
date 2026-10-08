# CC17 terminal odd terminology

All definitions refer to the original, unshifted Weil form at aperture
`a=21/20` and the physically orthonormal Legendre basis.

| Term | Meaning |
| --- | --- |
| `e111` | Original normalized odd Legendre coordinate of degree111. |
| `D_o` | Compression of the original odd form to the physical orthogonal complement of `e111`; this contains odd degrees1 through109 and the entire original odd F112 complement. CC16 certifies its positivity and coercivity. |
| Terminal scalar `sigma` | `inf Q(e111+v)` over the original form domain with `v` physically orthogonal to `e111`. This is the actual Schur scalar after eliminating `D_o`. |
| Finite native trial `q` | An exact rational combination of odd degrees1 through111 with degree111 coefficient exactly1. It is a concrete admissible upper-bound trial for `sigma`. |
| Trial mass `m` | The physical squared norm of `q`, the sum of its56 rational coefficients squared. |
| Residual source `r_s` | `P_D L(s q)`, where `L` is the original source operator, `P_D` removes only the degree111 coordinate, and `s=10^-14`. This retains the complete odd55 and original infinite complementary source. |
| Inverse-weighted reaction | `<r_s,D_o^-1 r_s>/s^2`. Computing its full value would evaluate the terminal scalar through the exact identity `sigma=Q(q)-<r_s,D_o^-1 r_s>/s^2`. |
| CC16 lower endpoint | The terminal interval pivot of CC16's sufficient complete no-lift lower matrix. Infimum monotonicity makes its lower endpoint a lower bound for the actual terminal scalar. It is inherited evidence, not a freshly replayed full source/Gram calculation. |
| Mass-normalized bracket | The scalar bracket divided by the fixed positive trial mass `m`. It preserves the scalar sign. It is not an estimate of the minimum spectral eigenvalue. |

A bracket crossing zero settles neither positivity nor contact. A negative
sufficient lower pivot certifies no actual negative direction. Positive
`sigma` would close this fixed aperture together with CC16's positive even
sector and positive odd compression; it would not establish reusable
continuation, non-stalling, RH/F4/full transport or Lean closure.
