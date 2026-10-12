# RPB108 — RC140: paid residual endpoint probe

Date: 2026-10-12 UTC. Aperture a=11/10. Branch `research/rpb108-route-consolidation`. Parent RC139, `53906860e45d605a7d17710b602c3e63831e2cf3`.

The normalized full-carrier reference response has the certified enclosure

\[
0.931329483032\le\Sigma_{00}/G_{00}\le0.931329517596497.
\]

The upper endpoint decreases by 1.0503e-11 from RC139; the width is 3.4564497e-8, versus 3.4575e-8. This is a small but strict improvement. The lower endpoint and seven-vector carrier are unchanged.

## Endpoint energy of the true residual

For RC139's upper-optimized rational trial, let `r_0=(S+T)c-P_0` be its nominal residual and `r=(I+C)y-P_0` its actual residual. The full D-norm action error is paid by `||r-r_0||_D<=e`. Choose the fixed rational probe `s=P_0-(5.711278414)f_0`. The actual seven-vector endpoint intervals bound `H(r_0,s)` and `H(s,s)`. Since `0<=C<=I`, `||Cs||_D^2<=H(s,s)`. Thus

\[
H(r,s)\ge H(r_0,s)_{lower}-e\sqrt{H(s,s)_{upper}}
>8.2674891759\mathbin{\cdot}10^{-6}.
\]

Cauchy in the positive `C` form gives

\[
H(r,r)\ge\frac{H(r,s)^2}{H(s,s)}
>1.6525002877\mathbin{\cdot}10^{-10}.
\]

For every spectral value `0<=lambda<=1`,

\[
\frac1{1+\lambda}\le1-\frac\lambda2,
\qquad
1-\frac\lambda2-\frac1{1+\lambda}
=\frac{\lambda(1-\lambda)}{2(1+\lambda)}\ge0.
\]

Consequently, the upper residual correction in the exact variational identity is at most `||r||_D^2-H(r,r)/2`, sharpening RC139's `||r||_D^2` bound. All products, square roots, signed endpoint sums and divisions are enclosed by rational outward rounding. The probe coefficient was chosen numerically but is checked as a fixed rational; it is not an acceptance premise. The validator rebuilds RC139 and its predecessor chain, checks five exact scalar spectral controls, and replays all signed sums in reverse order.

This endpoint probe only improves one scalar reference response. Its small gain also quantifies that the current action and endpoint uncertainty limits this route. It does not meet an asserted Stage I matrix tolerance, evaluate original Weil actions, or prove original positivity. Whole-aperture extension, F4, RH and Lean remain open. RC141 should refine common-source/t endpoint energy directly and pin down the required matrix response tolerance before transport to original sources.

## Reproduction

```bash
python scripts/validate_rpb108_rc140_residual_endpoint_probe.py \
  --output certificates/rpb108_rc140_residual_endpoint_probe.json \
  certificates/rpb108_rc139_two_sided_variational_response.json \
  certificates/rpb108_rc138_reference_variational_response.json \
  certificates/rpb108_rc137_seven_input_covariance.json \
  certificates/rpb108_rc136_seven_vector_joint_matrices.json \
  certificates/rpb108_rc135_common_response_capture.json \
  certificates/rpb108_rc132_balanced_action_shared_covariance.json \
  certificates/rpb108_rc128_collective_second_response.json \
  certificates/rpb108_rc130_remaining_covariance.json
```

Repeat with `--replay` for full certificate equality. Historical files remain untouched.
