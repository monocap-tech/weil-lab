# RC196: close the five-source canonical half-Gram gate

Starting head:6d435ace9ae49dec6acd6b6c963f567ac4c6fd92 (RC195). The aperture11/10, supported canonical M=D^-1 L, D-energy norm, five response sources P0,P2,f0,psi0,w14 and six represented trial directions remain unchanged.

| Same-family inverse measurement | RC195 | RC196 |
|---|---:|---:|
| Certified inverse enclosure width relative to G_lower | 0.571911 | 0.307029 |
| Width/half-Gram threshold ratio | 1.143822 | 0.614058 |
| Guaranteed half-Gram margin | No positive guarantee | 0.192971 G_lower |
| Exact half-Gram acceptance | Failed | Passed |

The selected enriched enclosure satisfies gap<=0.307029 G_lower by exact rational PSD verification. Hence (1/2)G_lower-gap>=0.192971 G_lower. The source lower Gram is positive definite from the inherited source certificate; this is a positive guaranteed local acceptance margin. The baseline retains the inherited0.571911 width and fails. The smaller accepted source-family results remain intact.

## Bound refinement without new actions

RC195 showed that the omitted-tail variational payment was small compared with the action-uncertainty payment. RC196 retains all complete RC195 source/trial Grams, mixed cross entries, nominal residuals and infinite-tail payments, bound by the exact input hash. No source, trial vector, action carrier or nominal residual is changed. RC192–194 actions and signed q185 tail remain attached through RC195.

Let Y_k be row k of the selected six-direction trial map and epsilon_k the full absolute D-norm error upper on its represented canonical action. For every complex five-source mixture x,

||sum_k error_k (Y_k x)||_D <= sum_k epsilon_k |Y_k x|.

For arbitrary positive rational t_k, Cauchy–Schwarz bounds its square by

(sum_k epsilon_k/t_k) sum_k epsilon_k t_k |Y_k x|^2.

Thus E=(sum epsilon_k/t_k) sum epsilon_k t_k Y_k*Y_k is a complete response action-error Gram upper. This does not assume any cancellation, independence or alignment among the actual action errors. The validator independently checks that diag[(sum epsilon/t) epsilon_k t_k]-epsilon epsilon* is PSD before transporting the bound through Y.

The selected weights are t_k=1/sqrtup(Y_k G_lower^-1 Y_k*), with t_k=1 for zero rows. The weights adapt the triangle proof to the actual response coordinates. They approximate the minimizer of the trace surrogate; this is a selection heuristic and not an unproved assertion of optimality. Every chosen rational weight is valid independently of that heuristic.

For the enriched trial, E<=0.000493 G_lower is certified by exact PSD checks. The corresponding variational response width decreases from0.281851 to0.109100. Selected variational action parameter1/400 and tail parameter1/3, followed by the actual residual upper parameter1/10, give the new inverse enclosure. The selected residual lower parameter iszero. Both endpoints are new refined endpoints; acceptance does not rely on claiming an exact inverse or zero error.

## Verification and coverage

The validator hashes RC195, RC121 and RC184, verifies their ancestry, and retains RC195's full-domain/tail contracts. Exact parameter searches include adapted, raw-trial and response-column triangle bounds, plus inherited/structural inverse endpoint alternatives. Forward generation and reversed trial/parameter-order replay must reproduce the entire certificate.

```
python scripts/validate_rpb108_rc196_adaptive_action_error_inverse.py --output certificates/rpb108_rc196_adaptive_action_error_inverse.json
python scripts/validate_rpb108_rc196_adaptive_action_error_inverse.py --replay --output certificates/rpb108_rc196_adaptive_action_error_inverse.json
```

This closes the named five-source canonical inverse contract only. The family contains four native directions plus auxiliary P2; q185 is an inverse trial direction. Native v10,z_b6,t10 canonical action and inverse coverage remain open. Full native-frame inverse coverage would still not alone prove the original Stage I augmented Weil floor or signed auxiliary response; their actual source-range attachment and acceptance remain open.

Stage I's ratio stays undefined. Original Weil positivity, RH,F4 and Lean closure are not claimed. Next: extend complete canonical action coverage to v10, retaining its signed mixed couplings with the accepted family, then test the expanded inverse family.
