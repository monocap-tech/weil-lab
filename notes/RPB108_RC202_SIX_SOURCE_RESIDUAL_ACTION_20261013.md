# RC202: a paid residual direction for the six-source inverse

Starting head:4b44c5fa403d50de6dab0b2c64d86e21bc8d6b4d (RC201). Definitions are in docs/TERMINOLOGY_RPB108_RC202_SIX_SOURCE_RESIDUAL_ACTION.md. Operator M=D^-1 L, aperture11/10, D norm and the six response sources remain unchanged.

RC202 constructs q202 and certifies its complete actual canonical action. It does not yet attach a new inverse trial or claim an improved inverse width.

## Input approximation and selection

Both RC201's exact mixed gate-failure probe and the P0 coordinate are tested at even input degrees256 and512. Selection minimizes the certified approximation error divided by a certified actual residual norm lower, not a numerical residual estimate.

| Focus | Cutoff256 relative error upper | Cutoff512 relative error upper |
|---|---:|---:|
| P0 coordinate | <0.316129 | <0.203464 |
| Mixed gate-failure probe | <0.434787 | <0.314576 |

The selected q202 is the P0-coordinate polynomial through512. Its actual residual norm lower exceeds0.0078084509. The actual residual-to-polynomial D error is below0.001588738, giving relative upper0.203463796. The local half-norm budget passes, with ratio below0.406928 and margin above0.296536 relative norm units. This is an input construction budget, not inverse acceptance.

The complete finite residual is reconstructed through65534 using RC200's attached v10 carrier and RC201's exact selected trial coefficients. The source-Gram lower is reproduced exactly. Retained coefficient rounding, omitted finite degrees514..65534, the complete analytic residual tail, and nominal-to-actual action uncertainty are all paid. On this selected probe, the direct triangle bound is sharper than the adaptive Gram bound; both are recorded and their minimum is used. Stored rational centers alone define the exact q202 polynomial.

## Complete canonical action

The signed endpoint action is enclosed through4094. Beyond that prefix,25 exact signed moments of the finite input are retained; the omitted geometric remainder has D norm below1.455e-50. Its normalized input lambda is512*513, and the first analytic even output degree is4096. The negative-r D-inverse correction is included through512.

The regular analytic-kernel construction uses kernel degree192, exact Legendre output through1536, and private600-digit directed interval helpers. The analytic kernel and infinite regular output remainders are paid. The resulting complete canonical q202 action error is below2.614712e-10 in D norm. Exact interval checks also put its actual canonical pairing strictly between a*norm_D(q202)^2 and2*norm_D(q202)^2 under RC121's full-domain metric bounds.

Transferring this carrier to the actual focus residual costs the separate input error: the complete Mr approximation error is below0.003177475. The tiny polynomial-action error must not be reported as an error on the actual residual itself.

## Verification and continuation

The main certificate SHA-256 binds RC201 and its entire input ancestry. Replay reverses focus order, reconstructed coefficient sums, endpoint output order, signed moment sums and regular construction order, and requires exact equality of the entire output certificate.

```
python scripts/validate_rpb108_rc202_six_source_residual_action.py --output certificates/rpb108_rc202_six_source_residual_action.json
python scripts/validate_rpb108_rc202_six_source_residual_action.py --replay --output certificates/rpb108_rc202_six_source_residual_action.json
```

Next: add q202 to the inverse trial space, certify its full source/canonical/action mixed rows and infinite tails, and retest the unchanged six-source response family. RC201's width1.823489 and ratio3.646978 remain the latest six-source inverse measurements. The RC196 accepted five-source result remains intact. Native z_b6/t10 complete action coverage, original Stage I source-range and augmented positivity, RH,F4 and Lean closure remain open/unclaimed.
