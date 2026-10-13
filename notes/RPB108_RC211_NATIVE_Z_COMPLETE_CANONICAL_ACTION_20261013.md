# RPB108 — RC211: complete native z_b6 canonical action

Parent RC210, commit a3e53797a478490f0d7f35966b9ba1e3f3f118a1. Aperture 11/10 and M=D^-1 L remain fixed. RC210's accepted six-source inverse width 0.436100 and margin +0.063900 are preserved. This checkpoint supplies a complete canonical action carrier and rigorous error for the previously uncovered native z_b6 source.

## Result

The unchanged native z_b6 now has a full canonical action trial with

    ||M z_b6 - represented_action||_D
      <= 0.0006006754718840694046875394914392715329,

and a certified relative error upper approximately **0.01916407161** (1.9165%) against its D-norm lower bound. A short safe displayed absolute bound is **0.000600676**.

| Paid component | D-norm error upper, rounded upward |
| --- | ---: |
| Complete endpoint action | 0.000384605 |
| Complete regular action | 0.000216072 |
| Complete canonical action | 0.000600676 |

The regular omitted-input error dominates its regular component. The endpoint error includes half of the entire omitted native input above degree 512. This is an initial complete carrier; no assertion is made that its accuracy suffices for the expanded inverse gate.

## Native identity and prefix custody

The source is exactly RC132's z_b6: a finite midpoint/floor polynomial through even degree 8190, followed by the selected order-6 analytic carrier. It is not replaced by C(w14-alpha psi0) or a newly rounded source. RC132's actual finite balanced input is g-alpha psi0 restricted to even degrees through 4094, retaining its actual s-dependent coefficient intervals.

The verifier reconstructs every balanced input interval, checks its full immutable SHA-256 against RC132, and then reproduces the exact historical directed midpoint/floor native z coefficients at every even degree 0..512. The source radius printed for these coefficients belongs to their generator; it does not redefine the native source as a varying interval vector. Both normal and reverse generator orders reproduce identical native centers.

RC136 supplies the unchanged full native z D-energy lower and upper. Subtracting a directed lower energy for the reproduced finite prefix from the full upper pays all omitted native source degrees, including the rest of the finite polynomial and its infinite analytic carrier. The historical seven-vector independence result is retained.

## Complete canonical carrier

The trial is

    native z
      + represented endpoint action of the finite native z prefix through 512
      + (1/2) omitted native z above 512
      - r D^-1 native z
      + represented D^-1 R(low native z prefix through 128),

with r=789/125. The finite endpoint output is materialized through even degree 4094. Above it, retain 25 exact signed moments of the degree-512 input and pay the full geometric remainder. Directed coefficient-rounding energy is included. Positivity/contraction 0<=C<=I on the whole D-domain pays the centered omitted-input error by half its D-norm. No cutoff commutation is assumed.

The negative-r multiplier is exact on every coefficient of the actual native source, including all finite and infinite omitted degrees. It is not truncated or assigned zero.

The regular part is explicitly projected from the degree-128 native input into the output polynomial through even degree 768. The inherited analytic Poisson/Beta/log-moment construction retains its kernel-series, parameter, coefficient-rounding and entire output-tail payments. RC174's high-input smoothing estimate at cutoff 128 pays the complete remaining native regular input. Its physical L2 energy is bounded using the full D-energy minus the finite-prefix lower, divided by the actual D-floor at the first omitted degree. No unconstructed input or output tail is silently discarded.

## Verification and evidence limits

Seven inherited certificate blobs and eleven helper blobs match the live repository tree. Normal verification and reversed-order replay pass and require an identical complete certificate. Replay reverses balanced source summation, endpoint output/summation order, exact moment summation and analytic regular-kernel accumulation. A mismatched input Git pin is rejected.

```bash
python scripts/validate_rpb108_rc211_native_z_canonical_action.py --output certificates/rpb108_rc211_native_z_canonical_action.json
python scripts/validate_rpb108_rc211_native_z_canonical_action.py --replay --output certificates/rpb108_rc211_native_z_canonical_action.json
```

This extends full canonical-action coverage to native z_b6. It does not yet attach its mixed action/residual rows or evaluate a new seven-response inverse enclosure. The existing six-response family includes auxiliary P2; it should not be confused with the seven-member native frame. Adding z to that response family is new coverage whose gate must be checked independently. Reference endpoint action/Gram certificates are not canonical inverse certificates.

## RC212 cursor

Construct the remaining native t10 complete canonical action, or attach z_b6's complete carrier and paid error to the enlarged mixed/action/residual matrices and test the expanded inverse. If refinement is required, increase the endpoint input/output and regular input degrees while retaining the full omitted-source payments. Never promote the preserved six-source gate to the enlarged family without its own enclosure.

Native t10 complete action, expanded inverse acceptance, odd-parity/source-range and original augmentation remain open. Stage I, original Weil positivity, RH, F4 and Lean closure are unclaimed. All historical files and other branch heads are preserved.
