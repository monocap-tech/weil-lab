# RC155: complete seven-source action-error interface

Resume from RC154 (`b94120e31a5bdff45abbb5c512d0c0ca355267e4`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are entered additively in `docs/TERMINOLOGY_RPB108_RC155_SEVEN_ACTION_INTERFACE.md`.

RC154 passed the two complementary action-error gate. RC155 assembles those two paid trials with the five existing RC138 trial actions in RC150's full-rank source frame

\[(P0,f0,w14-\alpha\psi0,(v10+z_{b,6})/2,t10,\psi0,z_{b,6}-v10).\]

The exact frame inverse and predecessor hashes are checked. The actual D Gram lower is transported from RC136 by congruence. A generic sevenfold diagonal Young budget fails the half-Gram gate, but that budget loses useful source geometry.

For real source coefficients c, the column error bounds give

\[\|\mathcal E c\|_D\le\sum_i\epsilon_i|c_i|=\max_\sigma v_\sigma^Tc.\]

There are 64 distinct signed rank-one controls after fixing the first sign positive; simultaneous reversal leaves the squared functional unchanged. RC155 computes each exact rational v_sigma^T G^-1 v_sigma and directly verifies every resulting PSD matrix beta G-v_sigma v_sigma^T. The exact worst factor is approximately 0.485069463653292. Outward rounding certifies

\[\boxed{\|\mathcal E c\|_D^2\le0.485070\,c^*Gc<\tfrac12c^*Gc.}\]

The worst sign representative is (1,1,-1,1,-1,-1,-1). This is a control for the column-error envelope, not evidence that the actual errors attain those signs or magnitudes. Realness of the actual operator and trials extends the quadratic inequality to complex coefficients by separate real/imaginary estimates. No complex-phase sign enumeration, error orthogonality, or cutoff commutation is assumed.

The full-frame inequality also transports back to the native seven-vector carrier. All 49 mutual error-pairing absolute bounds and all 49 action-error/source pairing absolute bounds are paid. Transforming RC136's source endpoint intervals and adding these latter errors encloses all 49 paid trial-source pairings Q_ij=<q_i,s_j>. These new Q intervals are obtained from inherited endpoint data; no new direct finite/analytic trial pairing evaluation is claimed, and Q is not incorrectly symmetrized.

This closes a complete seven-source action-approximation gate. It does not assemble the seven-source inverse-response matrix or certify that matrix's width. The five-source RC149 response certificate and its width remain the separate previously paid result. Stage I tolerance, original Weil/augmented action transport, whole-aperture positivity, F4, RH, and Lean closure remain open.

Next: evaluate sharper trial-source and trial-trial pairings from the explicit finite and analytic coefficients. Use those pairings and the paid joint error map to assemble the seven-source variational inverse enclosure, then certify its matrix width separately against an explicit Stage I tolerance.

## Reproduction

```bash
python scripts/validate_rpb108_rc155_seven_source_action_interface.py \
 --output certificates/rpb108_rc155_seven_source_action_interface.json \
 certificates/rpb108_rc150_source_coverage.json \
 certificates/rpb108_rc138_reference_variational_response.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc154_centered_analytic_tail_action.json \
 certificates/rpb108_rc153_correlated_difference_action.json
```

Add `--replay` to reverse control and pairing summation order and check exact certificate equality. Historical checkpoint files are unchanged.
