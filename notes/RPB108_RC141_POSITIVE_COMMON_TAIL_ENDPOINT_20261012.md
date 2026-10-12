# RPB108 — RC141: positive common tail sharpens the endpoint energy

Date: 2026-10-12 UTC. Aperture a=11/10. Branch `research/rpb108-route-consolidation`. Parent RC140, `4b849bc814baeda48aa67db1f925a2a7e643a396`.

The certified normalized full-carrier `P_0` reference inverse response is now

\[
0.931329483032\le\Sigma_{00}/G_{00}\le0.931329517490064.
\]

The upper endpoint improves by 1.06433e-10 over RC140 and the interval width becomes 3.4458064e-8. The seven-vector carrier and the lower response endpoint are unchanged. The improvement is modest, but it comes from an actual endpoint sign rather than a narrower numerical optimizer tolerance.

## The source sign

RC135 defines `u=(v_10+z_b,6)/2 = u_f+u_tail`, with finite even degrees at most 8190 and analytic even degrees from 8192 onward. Its reconstructed finite source coefficients are all strictly positive; its eleven exact analytic moment coefficients are also strictly positive. The analytic basis coefficient has positive factors `(2n+1)/((H_n+s)z_n)` and positive powers of the positive cutoff ratio, so every analytic coefficient is positive.

For distinct even degrees, the actual endpoint kernel has off-diagonal entry

\[
h_{nm}=\frac{2a}{|n(n+1)-m(m+1)|}>0.
\]

All finite versus analytic cross terms in `H(u_f,u_tail)` therefore have positive sign. Moreover `H(u_tail,u_tail)>=0` since `C` is positive. Consequently `H(u,u_tail)>=0`. The validator checks representative exact rational cross entries and checks every recorded analytic moment sign; RC135's finite positivity assertion and source hash are inherited through its byte-identical input certificate.

The RC135 trial `t_10` approximates `C u_f` in the full D norm with finite action error below 1.356825e-14. Thus

\[
H(u,u)=\langle u,t_{10}\rangle_D+
\langle u,C u_{tail}\rangle_D+
\langle u,C u_f-t_{10}\rangle_D
\ge\langle u,t_{10}\rangle_D-\|u\|_D\epsilon_{finite}.
\]

RC136's actual seven-vector Gram entries and the paid finite error give a new lower bound for `H(u,u)`. Intersecting it with RC138's signed endpoint interval raises its lower endpoint by more than 5.6209941668e-9. The old upper endpoint remains in force. The `u` coefficient of RC139's upper-optimized rational trial is nonzero; increasing this positive diagonal endpoint contribution tightens its variational upper response. RC140's independently paid residual endpoint correction is retained. All response divisions and the final upper endpoint are rounded outward at 10^-15.

This only sharpens a scalar reference response. It does not establish a Stage I matrix response tolerance, certify original Weil actions, or prove original positivity. Whole-aperture extension, F4, RH and Lean remain open. The next useful endpoint task is a direct upper bound on the common tail interaction or sharper `t` endpoint rows, followed by a concrete matrix tolerance and original-source transport audit.

## Reproduction

```bash
python scripts/validate_rpb108_rc141_positive_common_tail.py \
  --output certificates/rpb108_rc141_positive_common_tail.json \
  certificates/rpb108_rc140_residual_endpoint_probe.json \
  certificates/rpb108_rc139_two_sided_variational_response.json \
  certificates/rpb108_rc138_reference_variational_response.json \
  certificates/rpb108_rc137_seven_input_covariance.json \
  certificates/rpb108_rc136_seven_vector_joint_matrices.json \
  certificates/rpb108_rc135_common_response_capture.json \
  certificates/rpb108_rc132_balanced_action_shared_covariance.json \
  certificates/rpb108_rc128_collective_second_response.json \
  certificates/rpb108_rc130_remaining_covariance.json
```

Repeat with `--replay` to reverse inherited signed accumulation and compare the complete rational certificate. Historical certificates and notes remain unchanged.
