# RC193: refine the complete regular action on unchanged native f0

Starting checkpoint: RC192, commit 0318b854a18957aea75b5443b407e1aab9416b22.

At aperture B=11/10, the source, supported canonical operator M=D^-1 L, and D-energy norm remain unchanged. Native f0 is finite through even degree 988. This pass extends its regular input from degree 172 to 512 and regular output from 512 to 1536.

| Same-source absolute D-norm bound | RC176 | RC193 |
|---|---:|---:|
| Complete D^-1 Rf0 carrier error | 0.00009988108808718027 | 0.000009048437853031322 |
| Complete canonical action error | 0.00009988108808718048 | 0.000009048437853031544 |

These decimal summaries come from exact rational certificate uppers. The complete action bound improves by more than 11.038 times. No full-action acceptance tolerance is selected and no new inverse width is evaluated.

## Input and output payments

The input coefficients are eta_n=(2n+1)/(n(n+1) D_n), D_n=s+H_n. The RC129 interval for s gives directed coefficient intervals; rational centers are rounded on a 10^80 grid. Their physical L2 error energy is paid separately. Every omitted input degree 514..988 is included in an exact rational physical-energy upper. No input coefficient beyond 988 exists in the native definition.

RC174's high-mode smoothing estimate gives phi_M^2 = min(r^2, 4B I2 (11/12)^(2(M+1)) + e_upper^2 / band^2), with I2>=e*pi^2/3, band=(M+1)/(6*pi_upper*B), and r=789/125. Since D>=s_lower I, the input-tail contribution to the D^-1 output D-norm is bounded by sqrt(phi_M^2 E_tail)/sqrt(s_lower). This contribution is below 0.000009047501832913119 and dominates the new bound. The coefficient-center contribution uses the physical R bound r and is paid separately.

The finite polynomial action uses RC179's analytic kernel/Beta/log projection method with kernel degree 192 and output degree 1536. Degree 512 requires private directed 600-digit interval helpers and a 600-digit square-root grid, as in RC190. Historical helpers and certificates are unchanged. Kernel parameter uncertainty, analytic kernel truncation, coefficient rounding, retained output coefficient intervals, and the complete omitted logarithmic output tail are all paid. The polynomial source basis ends at power 705, so its polynomial part has no omitted coefficients beyond 1536.

The retained nonregular payment is RC176's complete-action upper minus its regular upper. RC176 constructs its complete upper by adding nonregular payments then rounding upwards, so this difference remains an upper bound for the retained payments. Native w14 and the negative-r correction remain the historical representation; RC193 changes only the regular polynomial.

## Verification and custody

Six input certificates are bound by SHA-256. RC176's direct kernel, compression and joint-source ancestry is checked, as is the full-domain endpoint form bound from RC121. Remote RC192 input/helper Git blobs were compared with the local bytes before publication. Replay reverses input summation and analytic kernel convolution order and requires exact equality of the entire output certificate.

```
python scripts/validate_rpb108_rc193_extended_f0_regular_action.py --output certificates/rpb108_rc193_extended_f0_regular_action.json
python scripts/validate_rpb108_rc193_extended_f0_regular_action.py --replay --output certificates/rpb108_rc193_extended_f0_regular_action.json
```

The existing workspace draft certificate passed exact replay. The dashboard records this as same-source action precision. RC191's inverse width 1.254303 and acceptance ratio 2.508606 remain current, with the gate open. Native v10, z_b6, t10 coverage, original Stage I targets, whole-aperture original Weil positivity, RH, F4, and Lean closure remain open/unclaimed.

Next: retain q185's analytic endpoint-output tail, then rebuild complete mixed rows and the same five-source inverse using RC192 and RC193. The new action error cannot simply be substituted into old mixed matrices.
