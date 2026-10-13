# RC200: refine the dominant native v10 endpoint action

Starting head:8651cd0a903e9773a8b139951a2db0d622ba2d8e (RC199). Aperture11/10, supported canonical M=D^-1 L, native v10 and D-energy norm remain unchanged.

| Same-source complete D-norm bound | RC197 | RC200 |
|---|---:|---:|
| Endpoint C v10 action error | 0.0004204240791785482 | <0.000003252791 |
| Complete canonical Mv10 action error | 0.0004349625030493767 | <0.000017791215 |
| Complete relative canonical norm error | 0.01387585109749939 | <0.000567563 |

The endpoint bound improves by more than129 times and the complete canonical bound by more than24.44 times. These decimal values summarize exact rational certificate uppers. No full-action tolerance is selected. The unchanged regular payment1.4538423870828507e-5 now dominates the complete bound.

## Larger input and complete output

RC197 evaluated C on a degree-512 input, with output1536 and a centered native input tail. RC200 extends the input to32766 and output to65534. The source remains RC131's order10 v10: exact rational prefix through8190 plus11 analytic native moments from8192 onward. RC197's full source-prefix digest and its materialized predecessor are SHA-256 bound.

The finite endpoint input uses positive integer centers on scale2^32. Its full D-energy quantization error is bounded. The endpoint kernel uses scale2^28 integer floors; the complete row rounding and diagonal parameter interval errors enclose every output coefficient. Output centers use scale1e30. Nonnegative entries and the row-sum bound max(alpha)*Q*(max(diagonal)+2H_count) establish that every product, partial sum and reduction fits signed64-bit arithmetic. Kernel numerator and denominator products are independently checked. No floating-point endpoint arithmetic is used.

All omitted native input coefficients are paid by the analytic source envelope at32768 and the common eta-tail D-energy estimate. The full-domain0<=C<=I bound gives a centered input-tail payment of half that source-tail norm. Its energy upper is4.2255016896292654e-11. No cutoff commutation is assumed.

The exact positive finite-input moments determine the output beyond65534. Orders0..24 are retained, with their1e-40 center errors paid; the order25 geometric remainder is bounded over every omitted output degree. Input quantization, finite action intervals, output moment rounding, output remainder and the centered native input tail are all included in the complete endpoint norm upper.

## Canonical attachment and verification

The represented canonical action is native v10 + new RC200 endpoint carrier + retained RC197 finite/exact-tail negative-r correction + retained RC197 regular carrier. The regular and negative-r certificates are unchanged. The source and operator have not been redefined to obtain the improvement.

Five inputs are SHA-256 bound: RC199, RC197, RC183 materialized native source, RC129 and RC121. A separate materialized endpoint carrier contains the finite coefficient array, analytic output moments, centered input cutoff and input/dot-product digests. Its exact SHA-256 is bound by the main certificate. Replay reverses integer input/output order and moment sums and must reproduce both entire artifacts.

```
python scripts/validate_rpb108_rc200_extended_v10_endpoint_action.py --output certificates/rpb108_rc200_extended_v10_endpoint_action.json --carrier-output certificates/rpb108_rc200_materialized_Cv10_carrier.json
python scripts/validate_rpb108_rc200_extended_v10_endpoint_action.py --replay --output certificates/rpb108_rc200_extended_v10_endpoint_action.json --carrier-output certificates/rpb108_rc200_materialized_Cv10_carrier.json
```

No inverse response is evaluated. RC199's six-source width4.039743 and ratio8.079486 remain current, with acceptance open. RC196's accepted five-source result remains intact. Stage I, native z_b6/t10 action coverage, original Weil positivity, RH,F4 and Lean closure remain open/unclaimed.

Next: rebuild all six-source mixed rows and residual matrices with the larger v10 endpoint carrier, then retest the same inverse gate. The represented action has changed; substituting the smaller error into old mixed matrices is not sufficient. The unchanged regular payment or nominal residual may require a subsequent refinement.
