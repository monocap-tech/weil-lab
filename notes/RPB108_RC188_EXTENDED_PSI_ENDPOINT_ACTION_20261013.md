# RC188: larger centered psi endpoint carrier with exact integer evaluation

Parent: RC187, `81a40cdaac1fec9398a553d74630ee4e356f7503`.

RC188 extends the finite input for the unchanged native psi0 from degree8190 to32766, and its finite endpoint output from16382 to65534. The complete centered Cpsi error bound improves by a factor greater than4.2023. Including the unchanged full regular-component bound gives a complete actual canonical psi action relative D norm error below0.022225398, down from0.065432142.

## Same-source accuracy comparison

| Certified error, unchanged psi0 and D norm | Previous upper | RC188 upper |
|---|---:|---:|
| Cpsi complete D norm error | 0.000017499518 | 0.000004164180 |
| Full canonical Mpsi D norm error | 0.000020194990 | 0.000006859651 |
| Full canonical Mpsi relative D norm error | 0.065432142 | 0.022225398 |

These are norm errors, not squared-error factors. No new local acceptance threshold is assigned to the full action. The five-source inverse has not yet been recomputed with the new carrier, so RC187's width2.576643 and its failed gate remain the latest inverse result.

## Finite input and exact kernel arithmetic

Write psi0=p_exact+t with p_exact on even degrees990..32766 and t on even degrees>=32768. Its finite coefficients are replaced by exact integer multiples of2^-42 to obtain p188. Every coefficient interval discrepancy is paid in D energy; the resulting quantization energy upper is below4.267e-25.

The even Legendre h-matrix has nonnegative entries. Off the diagonal,

\[
 h_{nm}=\frac{2n+1}{|n-m|(n+m+1)}.
\]

The diagonal is2H_(2n)-2H_n+1/(2n+1)-log2 and is enclosed by exact harmonic/log intervals. Each entry is replaced by its integer lower approximation on the2^-28 grid. The exact integer dot sum gives a lower enclosure of each h p188 coefficient. Adding the total finite input coefficient sum divided by2^28, together with the diagonal interval width, gives its upper enclosure. Dividing by the certified D_n interval then encloses Cp188.

No floating-point arithmetic is used in construction. To rule out integer overflow, the off-diagonal row sum is bounded by2H_N, N being the finite input coefficient count. Indeed h_nm<=2/|n-m|=1/|n/2-m/2|, and each side of an even row contributes at most H_N. The largest diagonal upper and largest integer input coefficient therefore bound every nonnegative dot sum. The resulting guard is below4.481e18, strictly below2^63. All products and partial sums are nonnegative and cannot exceed that guard. Numerators and denominator products used by integer division are separately bounded below2^63.

The output coefficients are stored at scale10^30. Kernel intervals, division intervals, and output-center rounding contribute a total finite output D energy upper below3.083e-19. The carrier has32768 even coefficients through65534, with exact integer-center custody and replay hashes.

## Complete analytic output and centered input tails

For n>65534, every retained input degree m is below n. With z_n=n(n+1), lambda=32766*32767, and eta_n=(2n+1)/(z_n D_n),

\[
 (Cp188)_n=\eta_n\sum_m\frac{(p188)_m}{1-z_m/z_n}.
\]

The carrier retains25 normalized moments and pays the entire positive geometric remainder with the26th moment. Exact integer moment numerators are accumulated before rational normalization. Moment-center rounding is also paid. The output ratio is below1/4, and the common eta tail has the established D energy bound B/[D_(65534),lower*(65533)*(65534)].

The trial for the entire Cpsi0 is

\[
 \widehat{Cpsi0}=Q188(p188)+\frac12t.
\]

Since0<=C<=I on the complete supported canonical carrier,

\[
 \|C(p_{exact}-p188)\|_D\le\|p_{exact}-p188\|_D,
 \qquad \|(C-I/2)t\|_D\le\frac12\|t\|_D.
\]

These pay both the finite-input discrepancy and the entire infinite input tail. No cutoff commutation or invariant finite subspace is asserted. Combining input quantization, finite output intervals, moment rounding, geometric output remainder, and centered input tail proves

\[
 \|Cpsi0-\widehat{Cpsi0}\|_D<4.164180\times10^{-6}.
\]

## Complete actual canonical action

The actual canonical action is Mpsi0=psi0+Cpsi0-rD^-1 psi0+D^-1 Rpsi0, r=789/125. The identity and negative-r terms are exact complete analytic source expressions. The regular term remains the previously paid zero trial on the whole output carrier, with RC181 error upper below2.695472e-6.

Thus the new complete action has

\[
 \|Mpsi0-\widehat{Mpsi0}\|_D<6.859651\times10^{-6},
 \qquad
 \frac{\|Mpsi0-\widehat{Mpsi0}\|_D}{\|psi0\|_D}<0.022225398.
\]

The materialized companion stores the complete finite-center array, normalized analytic output moments, centered-input cutoff, and source/dot-product hashes. Its exact file SHA256 is bound in the main certificate.

## Verification and next obligation

Five inputs are hashed: RC187, RC181, RC129, RC121, and RC154. Their inherited hashes are checked, including the original psi and endpoint ancestry. The full-domain endpoint form bound0<=h<=D is verified from RC121. Replay reverses input ordering, integer dot reductions, output ordering, and integer moment accumulation; both complete JSON artifacts must reproduce exactly.

Run:

```
python scripts/validate_rpb108_rc188_extended_psi_endpoint_action.py --output certificates/rpb108_rc188_extended_psi_endpoint_action.json --carrier-output certificates/rpb108_rc188_materialized_Cpsi_carrier.json
python scripts/validate_rpb108_rc188_extended_psi_endpoint_action.py --replay --output certificates/rpb108_rc188_extended_psi_endpoint_action.json --carrier-output certificates/rpb108_rc188_materialized_Cpsi_carrier.json
```

Next: attach this new carrier to the full mixed five-source calculations and retained q185 inverse trials, using RC187's correlated variational proof. The output support and analytic tail formulas have changed, so old residual or mixed-row matrices cannot simply be reused with a smaller error number. Further w14 action precision remains available as a separate refinement.

The native source frame and the accepted four-source result remain unchanged. Native v10,z_b6,t10 full action/inverse coverage remains open. The five-source inverse gate, original Stage I obligations, whole-aperture original Weil positivity, RH, F4, and Lean remain open/unclaimed.
