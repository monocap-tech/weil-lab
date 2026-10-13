# RC190: endpoint and regular refinements of the complete native w14 action

Parent: RC189, `88de98936b811f072ed76f7f9dae54948b0b8f4c`.

RC190 tightens both nontrivial components of the unchanged native w14 canonical action. Its complete action-error norm upper decreases from0.000125385655 to0.000016950765, a same-source bound improvement greater than7.397. The new endpoint and regular carriers are materialized with all infinite input and output tails paid. No new inverse width is evaluated in this checkpoint.

## Same-source precision comparison

| Certified D norm error, unchanged w14 | RC183 upper | RC190 upper |
|---|---:|---:|
| Complete centered Cw14 endpoint action | 0.000067061959 | 0.000003543481 |
| Complete D^-1 Rw14 regular action | 0.000058323696 | 0.000013407284 |
| Complete canonical Mw14 action | 0.000125385655 | 0.000016950765 |
| Complete canonical relative D norm error | 0.001619393 | 0.000218925 |

These are norm bounds, not squared-error factors or intrinsic actual-error ratios. The endpoint bound decreases by a factor greater than18.925. The total comparison includes the retained finite negative-r correction error. The complete-action contract has no selected local threshold; RC183's accepted local regular-component budget remains preserved by the improved regular error.

## Extended centered endpoint carrier

The native source remains g on even degrees0..4094 and eta_n A_w(n) on even degrees>=4096, with A_w(n) its unchanged fifteen-moment polynomial at native scale977132. All its coefficients are nonnegative.

The finite endpoint input is extended through32766, including the analytic native source prefix above4094. Its coefficients are approximated by exact integer multiples of2^-32. Every native coefficient interval discrepancy is paid in D energy. The endpoint output has32768 even finite coefficients through65534, with centers stored at scale10^30.

The Legendre h-matrix entries are evaluated by exact integer lower kernels at scale2^28. Kernel intervals, D division, and output-center rounding are paid as in RC188. Positivity and the row-sum majorant consisting of the largest diagonal plus2H_N prove that every integer product and partial reduction fits int64. The endpoint calculation uses no floating-point arithmetic.

Above65534, the finite input produces eta_n times25 retained normalized moments at scale32766*32767. This output moment scale is distinct from the native w14 scale977132. The next positive moment pays the complete geometric output remainder, and moment-center rounding is also included.

Let t be the actual native source tail above32766. Since A_w(n) decreases there, its complete D energy is bounded by the common eta tail bound times A_w(32768)^2. The centered trial is

\[
 \widehat{Cw14}=Q190(p190)+\frac12t.
\]

The finite input quantization error is paid using ||C||_D<=1. The entire omitted input is paid using ||(C-I/2)t||_D<=||t||_D/2. No cutoff commutation or finite support invariance is assumed. These payments, together with complete finite/analytic output errors, prove the endpoint norm error upper0.000003543481.

## Larger regular input and complete regular output

The regular input is the exact native g prefix through degree512, extended from256. It is distinct from the quantized endpoint polynomial. Subtracting its certified prefix D energy lower from the whole native D energy upper pays every remaining finite g coefficient and the entire analytic native tail.

RC174's high-mode smoothing estimate, in the same form used by RC183, bounds the omitted input's complete regular action. For the input degree M=512, its paid squared factor is

\[
 \phi_M^2\le\min\left\{r^2,
 4B I_2(11/12)^{2(M+1)}+\frac{e^2}{U_M^2}\right\},
 \qquad U_M=\frac{M+1}{6\pi B}.
\]

Its D inverse action error upper is the square root of phi_M^2 times the omitted D energy divided by s_lower D_(M+2),lower. This includes all input modes, not only those materialized in the endpoint calculation.

The exact finite regular input is evaluated by the inherited analytic kernel/Beta/log-moment method with kernel degree192. The regular output is extended to1536. Every parameter interval, kernel remainder, polynomial/log coefficient rounding term, finite projection interval, and infinite endpoint-log output tail is paid. The full regular error is below0.000013407284.

Degree512 has larger intermediate monomial coefficients than the historical degree256 calculation. Private600-digit directed Decimal contexts and600-digit upward rational square-root bounds avoid excessive rounding payments in these intermediate quantities. These are rigorous interval bounds, not sampling estimates. Historical helper modules and old checkpoints are unchanged. The chosen interval and root precisions are recorded in the certificate.

## Complete canonical action and custody

The represented action is the exact native identity term plus the new centered Cw14 carrier, RC183's retained finite negative-r correction and exact analytic negative-r tail, and the new degree-1536 regular polynomial. Their three complete error payments give

\[
 \|Mw14-\widehat{Mw14}\|_D<1.6950765\times10^{-5},
 \qquad
 \frac{\|Mw14-\widehat{Mw14}\|_D}{\|w14\|_D}<0.000218925.
\]

The companion stores the endpoint finite-center array, normalized output moments, centered native-input cutoff, and the new regular output polynomial. It binds the unchanged native source and retained correction carrier by hash. Its exact file SHA256 is recorded in the main certificate.

Seven inputs are hashed: RC189, RC183 main and materialized native carrier, RC129, RC121, RC170, and RC174. Parent ancestry, native carrier bytes, and regular compression/kernel dependencies are checked. The full-domain endpoint form bound0<=h<=D is checked explicitly.

Run:

```
python scripts/validate_rpb108_rc190_extended_w14_endpoint_action.py --output certificates/rpb108_rc190_extended_w14_endpoint_action.json --carrier-output certificates/rpb108_rc190_materialized_Cw14_carrier.json
python scripts/validate_rpb108_rc190_extended_w14_endpoint_action.py --replay --output certificates/rpb108_rc190_extended_w14_endpoint_action.json --carrier-output certificates/rpb108_rc190_materialized_Cw14_carrier.json
```

Replay reverses endpoint input/output order, exact integer sums, analytic moment sums, and regular kernel summation. Both entire artifacts must reproduce exactly.

Next: attach the refined w14 endpoint and regular carriers to the full mixed five-source calculation, retain the refined psi0 carrier, and re-evaluate the canonical inverse with correlated variational bounds. Old mixed or residual matrices cannot merely be reused with the smaller error number: the represented w14 action and its analytic output tail have changed.

RC189's width1.654087 remains the latest evaluated inverse result, and its gate remains failed. The accepted four-source result and native seven-source frame remain intact. Native v10,z_b6,t10 coverage, original Stage I targets, whole-aperture original Weil positivity, RH, F4, and Lean remain open/unclaimed.
