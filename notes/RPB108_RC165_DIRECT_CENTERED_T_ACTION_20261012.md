# RC165: direct centered t10 action trial

Resume from RC164 (`de4c7c60be8e12dda81711cea2522db7ac2c0d50`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are added in `docs/TERMINOLOGY_RPB108_RC165_DIRECT_CENTERED_T_ACTION.md`.

RC164 completed the changed delta pairing rebase and identified t10 as the largest contributor to the updated sharp marginal norm-budget control. RC137's t action norm bound, 2.618625774909e-4, contains a finite projection residual with squared energy 2.630432737047e-8. This is a bound on fitting the retained action back into the native seven-vector span. RC165 replaces that fitted action trial with direct action coefficients at the same source and output cutoffs.

The validator reconstructs the canonical source data through RC136, checks the RC135 finite response and collective source hashes, and retains all predecessor source checks. It evaluates C(t10[0..4094]) through even degree 8190 using directed intervals. It rounds those output centers on the established rational grid and pays every finite action radius in D energy.

For even n>=8192, the finite source action is exactly eta_n times an infinite positive moment series. RC165 retains 25 moment centers, pays their rounding, and bounds the complete remaining series by mu_25 rho^25/(1-rho), where rho=4094*4095/(8192*8193). The zero-degree source coefficient is included in mu_0. The eta tail energy comes from the paid RC131 output-tail bound.

Write t10=p+r. The new trial is Q_24(p)+r/2. Since 0<=C<=I on the paid carrier,

\[\|Ct10-q_{t,\mathrm{new}}\|_D\le\sqrt{R_{\rm finite}}+\sqrt{R_{\rm moment}}+\sqrt{R_{\rm geometric}}+\tfrac12\sqrt{R_{\rm omitted\ source}}.\]

The full omitted source energy is RC136's 5.377122193817e-9, including degrees 4096..16382 and the prescribed analytic tail. No mixed-error sign or cutoff commutation is assumed. The old native fit residual and fitted-trial tail belong to the old trial and are not reused in this new error budget.

The trial has two different tail transition degrees. Its direct Cp output becomes analytic at 8192, while the canonical t source retains finite centers through 16382. The certificate specifies both contributions and their scales separately, avoiding replacement of finite t coefficients by an earlier analytic approximation.

The new t norm and the paid RC163 delta norm are tested in all 64 signed marginal controls against the same RC159 conditioned source Gram lower and RC158 inverse-source coefficient matrix Y. This diagnostic concerns changed physical action trials. Its maximizing sign control need not be realized by the actual positive endpoint operator, and supplies no lower bound on actual error or true inverse uncertainty. It does not reuse the old native Ct pairings or certify a new inverse enclosure.

The complete new t action error bound is **3.666443165323e-5**, improving RC137's bound by **7.142142** in norm and **51.010192** in squared error. The finite rounding energy is at most **2.708798e-67**, and the output geometric remainder energy at most **6.124705e-45**. The centered omitted-source term dominates this upper bound.

All 64 signed controls pass exact rational PSD checks with the outward marginal factor **0.056779**, compared with the paid delta refinement's **0.113762**. This reduction is an error-only diagnostic for the changed physical action approximants, not an inverse-width improvement.

The next pass must pay q_t_new's source row and its mixed Gram entries with the other action trials, then rebuild the endpoint approximation and nominal residual using four native and three separate non-native action columns. The RC164 retained inverse width remains 0.536203 until that reassembly passes. Stage I, original Weil/augmented transport, whole-aperture positivity, F4, RH, and Lean closure remain open.

## Reproduction

```bash
python scripts/validate_rpb108_rc165_centered_t_action.py \
 --output certificates/rpb108_rc165_centered_t_action.json \
 certificates/rpb108_rc137_seven_input_covariance.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc163_centered_difference_tail_action.json \
 certificates/rpb108_rc155_seven_source_action_interface.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json \
 certificates/rpb108_rc164_difference_pairing_rebase.json
```

Implicit RC136 dependencies are located by exact checkpoint hashes. Add `--replay` to reverse source sums and signed controls and check exact JSON equality. Historical files are unchanged.
