# RC163: sharper full delta action trial

Resume from RC162 (`e96b53e7f35cda26f436b626d559dd85167d7c57`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are added in `docs/TERMINOLOGY_RPB108_RC163_CENTERED_DIFFERENCE_TRIAL.md`.

RC162 identified delta as the largest contributor to the sharp marginal norm-budget control. RC163 changes that physical action trial, keeping the canonical source delta=z_b6-v10 unchanged. It reconstructs the RC153 finite delta and action centers, verifies both predecessor output hashes, and verifies the RC153 action-center hash and error budget.

Write delta=p+t at degree 4094. Instead of omitting Ct, use t/2. The paid positive self-adjoint endpoint contraction gives

\[C\delta-[Q_{24}(p)+t/2]=(Cp-Q_{24}(p))+(C-I/2)t,\qquad \|(C-I/2)t\|_D\le\tfrac12\|t\|_D.\]

The midpoint constant is uniformly sharp at the scalar spectral endpoints 0 and 1. This is a norm bound, with no mixed-error sign or cutoff commutation assumption. The omitted t includes the rational finite coefficients from degree 4096 through 8190 and the full prescribed analytic source tail.

RC153 also omitted the infinite action output of p beyond 8190. RC163 captures that output using 25 eta moments. Because every retained delta coefficient is negative, the corresponding positive mu_k moments pay the geometric remainder through mu_25 rho^25/(1-rho), where rho=4094*4095/(8192*8193). Moment centers and their radii are exact rational controls. The certificate stores the combined analytic trial polynomial and hashes the corrected finite trial centers. It pays finite output rounding, moment rounding, the infinite geometric remainder, and the centered full omitted-source energy separately.

For the resulting physical inverse trials with the same RC158 coefficients Y, RC163 recomputes all 64 signed marginal error controls against the RC159 conditioned source Gram lower. This error-only diagnostic does not substitute the new error norm into old trial pairings or certify a new inverse enclosure. The prior reference inverse enclosure, of width 0.536203, remains the available enclosure.

The resulting full delta action error bound is **4.947728908995e-6**, compared with RC153's **1.301646658673e-5**: a **2.630796** norm improvement and **6.921089** squared-error improvement. Centering the omitted input alone would give **8.068737677735e-6**. Capturing the output tail removes most of the remaining budget; its squared geometric remainder is bounded by **1.137497e-45**. These are certified upper bounds, not measurements of actual error.

All 64 signed controls for the changed physical inverse trials pass exact rational PSD checks with the outward marginal factor **0.113762**, compared with RC162's **0.201375**. This sharp scalar diagnostic uses the same source Gram lower and coefficient matrix, while the physical action trial vectors have changed.

The next pass must enclose the changed delta trial-source row and trial Gram cross/diagonal terms, then rebuild the nominal residual and combined endpoint functional. The exact rebase identities appear in the terminology file and certificate. Stage I, original Weil/augmented transport, whole-aperture positivity, F4, RH, and Lean closure remain open.

## Reproduction

```bash
python scripts/validate_rpb108_rc163_centered_difference_tail_action.py \
 --output certificates/rpb108_rc163_centered_difference_tail_action.json \
 certificates/rpb108_rc153_correlated_difference_action.json \
 certificates/rpb108_rc155_seven_source_action_interface.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json \
 certificates/rpb108_rc162_trial_signed_error_optimum.json
```

The six RC153 dependencies are hash-checked and loaded alongside the named inputs. Add `--replay` to reverse coefficient sums and signed controls and check exact JSON equality. Historical files are unchanged.
