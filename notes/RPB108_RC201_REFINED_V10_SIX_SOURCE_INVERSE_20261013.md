# RC201: attach RC200 and narrow the unchanged six-source inverse

Starting head:e8739e482f3b4f0dc6da2d1b7d353a226a550b34 (RC200). Aperture11/10, supported canonical M=D^-1 L, D-energy norm and response family P0,P2,f0,psi0,w14,v10 remain unchanged. Both source-Gram endpoints are reproduced exactly against RC199.

| Same-family precision measurement | RC199 | RC201 |
|---|---:|---:|
| Selected certified inverse width relative to G_lower | 4.039743 | 1.823489 |
| Width/half-Gram threshold ratio | 8.079486 | 3.646978 |
| Threshold minus width | -3.539743 | -1.323489 |
| Selected nominal residual squared-error upper | 0.323779 | 0.176780 |
| Selected adaptive action-error squared upper | 0.040835 | 0.001905 |
| Exact half-Gram acceptance | Failed | Failed |

Both Galerkin and least-residual trials produce valid six-source inverse enclosures. Galerkin gives width2.512125; the selected least-residual trial gives1.823489 using new refined lower and upper endpoints. Inherited RC199 endpoints remain valid alternatives. This is a same-family inverse-precision improvement, not merely substitution of a smaller action error.

## Full new carrier attachment

RC200's degree-65534 endpoint polynomial replaces RC197's small endpoint output. The centered omitted native input now begins32768 instead of514; the analytic output moments begin65536 instead of1538. The native source, negative-r correction beginning514 and regular degree-1536 polynomial remain unchanged. RC200's main certificate binds the materialized carrier's exact bytes and its complete action error.

All finite source/action mixed entries, nominal action-Gram rows, selected trial maps and trial residuals are rebuilt through65534. The new analytic output moments also replace the endpoint-output envelopes and leading eta terms in the infinite residual calculation. The source Gram is checked unchanged; the nominal action Gram is recomputed rather than asserted equal to RC199. The complete new canonical and represented-action Gram entry arrays are included for audit.

The seven-term residual-tail proof and response-adapted triangle proof from RC199 are retained with the refined carrier. The selected variational width decreases from1.449072 to0.335944. Selected action Young parameter1/300 and actual residual upper parameter1/10 give the new inverse enclosure. Every parameter is chosen only after exact PSD acceptance checks; the actual six-source response includes all complex mixtures and infinite tails.

## Exact failure probe and residual target

The selected gate matrix is not PSD, though its diagonal coordinate probes are nonnegative. A rational mixed source probe in response order is

(-3/1000, 3/250, -129/1000, 1, 109/250, -107/250).

Its gate quadratic is strictly negative by exact rational evaluation (approximately-6.562869280547499e-7). The probe was selected using a numerical eigendirection, but the negativity check uses only rational data. It witnesses failure of this enclosure, not impossibility of meeting the true inverse tolerance.

The nominal residual lower Gram and adaptive error upper give a positive actual trial-residual norm lower on this probe, above0.000371410 by rational square-root bounds. The same construction gives a lower above0.007756017 on the P0 coordinate. These are concrete nonzero residuals that can seed a subsequent finite enrichment; no new residual polynomial is certified in this pass.

Action-error accounting is now more balanced: approximately38.67% of the selected triangle factor is psi0,28.08% w14,28.55% v10 and4.71% f0. These shares describe a certified upper-bound factor, not actual errors or shares of inverse width. The nominal residual squared envelope0.176780 remains substantial, so further action accuracy alone is not promised to close the gate. The next priority is a paid residual-enrichment direction, with remaining action/regular payments kept visible.

## Verification and continuation

RC200 main/carrier, RC199 and the entire RC199 ancestry are SHA-256 bound. The unchanged source Gram and refined carrier attachment are checked. Replay reverses coefficient sums and trial/parameter search order and requires equality of the entire output certificate.

```
python scripts/validate_rpb108_rc201_refined_v10_six_source_inverse.py --output certificates/rpb108_rc201_refined_v10_six_source_inverse.json
python scripts/validate_rpb108_rc201_refined_v10_six_source_inverse.py --replay --output certificates/rpb108_rc201_refined_v10_six_source_inverse.json
```

The six-source inverse is certified but its half-Gram gate remains open. The accepted RC196 five-source result is intact. Native z_b6/t10 complete action coverage, original Stage I source-range and augmented acceptance obligations, original Weil positivity, RH,F4 and Lean closure remain open/unclaimed.

Next: construct and pay a finite approximation to an identified actual trial residual, certify its complete canonical action, and enrich the unchanged six-source inverse trial space before retesting acceptance.
