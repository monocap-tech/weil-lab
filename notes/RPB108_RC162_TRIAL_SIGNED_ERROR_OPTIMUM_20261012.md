# RC162: sharp marginal trial-error bound and blend audit

Resume from RC161 (`f6d54d831136c0d6d110814d8a806250ded3e71b`) on `research/rpb108-route-consolidation`, aperture 11/10. Additive definitions appear in `docs/TERMINOLOGY_RPB108_RC162_MARGINAL_TRIAL_ERROR.md`.

The fixed inverse trial matrix Y and seven paid action error norms epsilon_i imply

\[\|e(Yc)\|_D\le\sum_i\epsilon_i|(Yc)_i|=\max_\sigma z_\sigma^Tc,\qquad z_\sigma=Y^T(\sigma_i\epsilon_i).\]

RC162 checks all 64 distinct signed rank-one controls after simultaneous reversal is factored out. The exact optimum of a uniform bound against the certified conditioned Gram lower G is max_sigma z_sigma^T G^-1 z_sigma, approximately **0.201374747623474**. Outward rounding gives **0.201375**, and all 64 matrices 0.201375 G-z_sigma z_sigma^T pass exact PSD checks. RC161's selected weighted error matrix had a certified uniform factor **0.204707**. Thus its uniform marginal-norm factor was already close to this optimum.

The maximizing rational coefficient vector c=G^-1 z is recorded. An artificial aligned family of column errors sigma_i epsilon_i times one real unit vector realizes the exact ratio. This proves sharpness for the marginal column-norm information and the fixed trial coefficients. The certificate does not assume that this artificial family is realized by the actual self-adjoint positive endpoint contraction, nor that it obeys all native source identities. It supplies no lower bound on actual error or true inverse uncertainty.

On that sharp control, the contributions to sum_i epsilon_i|(Yc)_i| are approximately:

| Action column | Share of this marginal norm-budget control |
| --- | ---: |
| z_b6-v10 | 42.44329% |
| psi0 | 27.90953% |
| t10 | 27.25942% |
| (v10+z_b6)/2 | 2.38336% |
| w14-alpha*psi0 | 0.00440% |
| P0 and f0 | negligible at displayed precision |

These shares are obtained from the certificate's exact maximizing coefficients and the paid predecessor norm bounds. They are not a decomposition of the actual errors.

The new uniform error matrix and RC161's weighted error matrix are blended with five rational weights, and each blend is tested with endpoint parameters 1, 2, and 4. The selected endpoint estimate remains the pure weighted bound with gamma=2. Its full relative endpoint width is unchanged at **0.666942**, and the combined variational lower remains PSD. Rerunning the tested inverse residual parameters retains RC161's sharper positive inverse enclosure at **0.536203**. The half-Gram inverse-width gate stays open.

This audit closes the sharp *uniform marginal-norm* optimization for the current fixed trial matrix, not every possible matrix-shaped estimate or use of native correlations. The tested blend family does not improve inverse precision. The next target is additional actual action information: improve the delta trial first, or certify native error correlations beyond the seven separate norm bounds; psi0 and t10 also carry substantial budget. Retain the completed direct pairing blocks and correlated source Gram certificates.

No Stage I closure, original Weil/augmented transport, whole-aperture positivity, F4, RH, or Lean closure is asserted.

## Reproduction

```bash
python scripts/validate_rpb108_rc162_trial_signed_error_optimum.py \
 --output certificates/rpb108_rc162_trial_signed_error_optimum.json \
 certificates/rpb108_rc161_combined_endpoint_functional.json \
 certificates/rpb108_rc160_correlated_variational_transport.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc159_correlated_source_gram_tail.json
```

The predecessor chain is hash-checked. Add `--replay` to reverse signed controls and tested parameter orders and check exact certificate equality. Historical files are unchanged.
