# RPB108 — RC142: centered common-tail endpoint upper

Date: 2026-10-12 UTC. Aperture a=11/10. Branch `research/rpb108-route-consolidation`. Parent RC141, `cb519b03421a637b35f2191e98f85bcb58d73f70`.

The normalized full-carrier P_0 reference inverse response satisfies

\[
0.931329492307642\le\Sigma_{00}/G_{00}\le0.931329517490064.
\]

Its width is 2.5182422e-8, at least 1.368337 times narrower than RC141's width. The lower endpoint improves; the upper retains RC141's bound. No new vector is added to the seven-dimensional carrier.

## Centered tail interaction

Use RC135's exact source split u=u_f+u_tail, where the finite even degrees end at 8190 and the analytic tail starts at 8192. The D Gram is diagonal in these Legendre degrees, so

\[
\langle u,u_{tail}\rangle_D=\|u_{tail}\|_D^2.
\]

For the global positive contraction C, the centered operator has norm at most one half. Therefore

\[
\langle u,C u_{tail}\rangle_D
\le\frac12\|u_{tail}\|_D^2
+\frac12\|u\|_D\|u_{tail}\|_D.
\]

Every norm on the right receives its actual upper enclosure. This avoids a symmetric charge of the full uncentered contraction bound. RC135's t trial approximates C u_f with its entire finite-output rounding and omitted-output error paid. Consequently

\[
H(u,u)\le G(u,t)_{upper}
+\epsilon_{finite}\|u\|_{D,upper}
+\tfrac12 T_{upper}
+\tfrac12\sqrt{G(u,u)_{upper}T_{upper}}.
\]

The resulting endpoint upper is below 0.000439385140644243, reducing the old upper by more than 4.0302476401e-7. RC141's positive-tail endpoint lower is retained, and the intersection is checked nonempty. The infinite analytic tail is fully included through its certified energy, exact finite-tail orthogonality, and the global centered contraction.

## Response acceptance

All four rational trials accepted by RC139 are rechecked. For each, its positive c_u^2 H(u,u) energy contribution decreases by the endpoint upper improvement, so its variational lower increases by c_u^2 times that improvement. RC139's paid lower residual correction is also retained. The best resulting response lower is from the RC138 four-combination trial, showing why the maximizing trial can change after an energy enclosure improves. Division uses the actual G_00 upper and outward 10^-15 rounding. RC141's accepted upper response remains available independently.

The validator rebuilds the RC141 predecessor chain, checks five exact centered spectral controls including both endpoints, reverses inherited signed sums and candidate traversal in replay, and compares the entire rational certificate. This remains one scalar reference response. An explicit Stage I matrix response budget, a full inverse response matrix, and original Weil source transport remain to be established. Whole-aperture positivity, F4, RH and Lean remain open.

## Reproduction

```bash
python scripts/validate_rpb108_rc142_centered_common_tail.py \
 --output certificates/rpb108_rc142_centered_common_tail.json \
 certificates/rpb108_rc141_positive_common_tail.json \
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

Repeat with `--replay`. Only the three additive RC142 files are published.
