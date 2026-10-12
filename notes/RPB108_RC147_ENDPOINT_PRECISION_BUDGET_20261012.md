# RC147: the coupled endpoint precision budget

RC146's narrow five-source coordinate improved the reference response enclosure at aperture 11/10, but its uniform relative width is still 2.051566. RC147 attributes the narrow coordinate's interval width using exact rational coefficients and the inherited endpoint and D Gram intervals. It changes no action data or earlier certificate.

## Exact attribution

The fifth source coordinate is the RC145 rational witness. Apply its coefficients to the five action-trial frame vectors first, obtaining a single rational frame vector h. The signed variational expression is evaluated as S*Y+Y*S-Y*Y-h*Hh. For each uncertain matrix entry, its absolute signed coefficient times the certified interval width gives an exact contribution. The certificate recomputes this sum and checks it against RC146's stored fifth diagonal entry interval, up to outward rounding.

| Narrow-direction width charge | Approximate value |
| --- | ---: |
| D Gram entries together | 0.000000000741352 |
| Endpoint entries together | 0.000001764590435 |
| Of which t10 diagonal (4,4) | 0.000001198857236 |
| Of which common/t10 pair (3,4), both orders | 0.000000379974747 |
| Of which common diagonal (3,3) | 0.000000180916746 |
| Extra entry-to-Loewner conversion | 0.000000054879246 |
| Paid residual | 0.000000174508692 |

The t10 diagonal and common/t10 mixed endpoint entries account for most of the direct signed interval width. The D Gram interval and matrix conversion are much smaller here. These numbers are outward summaries of exact rational calculations, not sampled operator values.

## Conditional necessary target

The source energy upper is 0.000000976467677, so its half-Gram threshold is at most 0.000000488233839. If the t10 diagonal interval were reduced all the way to zero while every other *direct signed-entry* and paid residual charge remained at its present value, the witness width would still exceed 0.000000740983242. Its excess above the half-Gram threshold is greater than 0.000000252749404. Under that fixed-charge scenario, the common/t10 mixed entry charge must also shrink by **more than 66.5174%** for this witness to reach the half-Gram gate. The Loewner conversion would impose an additional charge, so this is a necessary diagnostic, not a sufficient route to a five-source matrix certificate.

The inference concerns this independent entry-interval enclosure. It is not a lower bound on uncertainty of the true reference response. A correlated combined endpoint energy for h could avoid paying the t10 and mixed intervals separately. That is the next mathematical target.

## Reproduction and boundary

```bash
python scripts/validate_rpb108_rc147_endpoint_budget.py \
 --output certificates/rpb108_rc147_endpoint_budget.json \
 certificates/rpb108_rc146_narrow_coordinate.json \
 certificates/rpb108_rc145_fifth_source_conditioning.json \
 certificates/rpb108_rc144_conditioned_joint_response.json \
 certificates/rpb108_rc143_joint_variational_matrix.json \
 certificates/rpb108_rc142_centered_common_tail.json \
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

`--replay` reverses the summations, rebuilds RC146 and its ancestors, and compares the generated certificate exactly. No original Weil action, whole-aperture positivity, F4, RH, or Lean closure follows.
