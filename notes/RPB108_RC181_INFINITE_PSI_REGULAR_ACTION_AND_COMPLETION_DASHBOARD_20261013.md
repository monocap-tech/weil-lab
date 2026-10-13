# RC181: infinite psi regular action and formal completion contracts

Parent: RC180, `078dd1eff1b1f94291264a60fed97f05ff018039`.

RC181 adopts separate, scope-aware measurements of precision, coverage, and acceptance margin. It verifies RC180's canonical gate margin exactly and advances the native psi0 direction by bounding its entire regular action and attaching a paid complete canonical source form. A current dashboard is stored in `docs/RESEARCH_COMPLETION_DASHBOARD.md`; its exact structured data is embedded in the new certificate.

## 1. Actual infinite psi source and regular zero carrier

The native source psi0 has coefficients

\[
 \eta_n=\frac{2n+1}{n(n+1)(H_n+s)},\qquad n\ge990\text{ even},
\]

and no other coefficients. It is orthogonal to every polynomial of degree at most 988. No input truncation of psi0 is made in this checkpoint.

RC174 supplies the actual regular high-input-mode estimate

\[
 \|R(I-\Pi_N)\|_{physical}^2\le\phi_N^2
 =\min\{r^2,4B I_2(11/12)^{2(N+1)}+e_+^2/U^2\},
 \quad U=\frac{N+1}{6\pi_+B},\quad I_2=e_+\pi_+^2/3.
\]

Use N=988. Since the diagonal D eigenvalues on psi's support are at least D_first=H_990+s_lower,

\[
 \|\psi0\|_{physical}^2\le\Gamma_{\psi,upper}/D_{first}.
\]

Also D>=s_lower I. Consequently

\[
 \|D^{-1}R\psi0\|_D^2
 \le\frac{\phi_{988}^2\Gamma_{\psi,upper}}
              {s_{lower}D_{first}}.
\]

Thus zero is a valid whole-output regular trial with a paid error. Every output mode is included in the norm estimate; no finite output or low-mode self-adjointness assumption is needed.

The exact arithmetic gives

\[
 \|D^{-1}R\psi0\|_D<2.695472\times10^{-6},
\]

\[
 \frac{\|D^{-1}R\psi0\|_D}{\|\psi0\|_D}
 <0.008733378.
\]

The selected local component budget is 0.01 relative D norm, and its certified acceptance ratio is below 0.873338. This is a local regular-component construction contract, not the accuracy requirement for the complete canonical psi action or Stage I. The proof uses the entire actual infinite input source; no nonzero regular output coefficients are evaluated.

## 2. Complete canonical source-form attachment

RC154 already supplies a Cpsi trial:

\[
 Q(\psi[990..8190])+\tfrac12\psi[8192..\infty],
 \quad C=D^{-1}h.
\]

Its Q part has finite outputs through degree 16382 and 25 eta output moments above that cutoff. The historical coefficient digest and analytic moment data are inherited unchanged. The full error is below 0.000017499518.

The negative-r term is retained exactly as an analytic source:

\[
 (-rD^{-1}\psi)_n
 =-\frac{r(2n+1)}{n(n+1)(H_n+s)^2},\qquad n\ge990\text{ even}.
\]

For the actual canonical M=D^-1 L=I+C+D^-1 R-rD^-1, attach the source-form trial

\[
 \widehat M\psi=\psi+Q_{C\psi}-rD^{-1}\psi,
\]

using the paid regular zero carrier. The endpoint and regular errors may overlap, so their norm bounds add. The complete action source-form error is

\[
 \|M\psi-\widehat M\psi\|_D<0.000020194990,
 \qquad
 \frac{\|M\psi-\widehat M\psi\|_D}{\|\psi\|_D}<0.065432142.
\]

The full canonical error is not the smaller regular-component error. No required full canonical psi accuracy is selected here. The RC154 finite coefficients are not rematerialized in RC181; the existing generator, coefficient digest, and complete analytic data define the inherited source form. This attachment alone does not evaluate the four-source inverse response.

## 3. Correlated four-source action-error envelope

The evaluated source-map family now has the form S4=(P0,P2,f0,psi0). The new source's D support is disjoint from the old finite sources, while the existing nonzero P2/f0 overlap remains. Thus its source Gram is block diagonal between the three-source Gram and the scalar psi Gram, not diagonal within the old block.

For all four action errors epsilon_i, weights w_i=sqrt(G_ii,upper), the same weighted Cauchy envelope gives

\[
 E_{ii}=\epsilon_i w_i\sum_j\epsilon_j/w_j,
 \qquad\|(MS4-V)c\|_D^2\le c^*Ec.
\]

Exact PSD checks establish E-epsilon epsilon*>=0 and E<=0.004333 G4_lower. Diagonality permits application to coefficient absolute values; complex source mixtures are included. No error-vector orthogonality is asserted.

The corresponding relative action norm upper is below 0.065825527. This four-source factor is larger than RC177's three-source factor 0.000003 because the family changed and the endpoint psi error dominates. It is coverage progress, not a decreasing precision comparison on the same source map. The dashboard records both scopes and does not assign a closure threshold to the new four-source action envelope.

## 4. Exact inverse acceptance margin

RC180's response sources remain S=(P0,P2,f0), despite its richer trial space. Its certified width is beta=0.300941 and the existing local half-Gram threshold is b=1/2. Define

\[
 \rho_{gate}=\beta/b=0.601882,\qquad
 m_{gate}=b-\beta=0.199059.
\]

The validator directly checks

\[
 bG_{lower}-(\Sigma_{upper}-\Sigma_{lower})
 \succeq0.199059G_{lower}.
\]

This is a guaranteed canonical matrix gate margin, not an original Weil spectral floor. The ratio below one and the full named three-source coverage establish that contract. RC178's historical width 0.997665 had ratio 1.995330 on the same response family and failed that enclosure's gate; both rows remain visible.

The dashboard also records RC177's K width 0.011597, action-Gram Q width 0.010509, squared action-error factor 0.000003, and its norm conversion below 0.001732051. These are distinct measurements. The current source-map estimates do not claim a whole-domain approximation norm for M.

## 5. Coverage and Stage I are separate

The dashboard distinguishes full-domain canonical structural bounds, evaluated source-map action carriers, actual inverse response coverage, and the original augmentation source range. It keeps native P0,psi0,f0,w14,v10,z_b6,t10 separate from the auxiliary P2 response direction and q inverse trial vector.

Stage I's original augmented Weil floor and auxiliary response are unevaluated here. Its selected numerical matrix tolerance and certified acceptance margins remain unset. Its completion ratio is therefore null, not zero, one, or an estimated percentage. Full native seven-source inverse coverage would still require the original source-range identification and actual original target certificates before implying Stage I closure.

## 6. Replay and next cursor

All seven inputs are hashed and cross-linked. Replay reverses the exact harmonic sum and reproduces the full certificate, including the completion dashboard. The regular component contract, correlated source-map envelope, and inverse margin are checked with exact rational inequalities or PSD elimination.

```bash
python scripts/validate_rpb108_rc181_psi_action_completion_dashboard.py \
  --replay --output certificates/rpb108_rc181_psi_action_completion_dashboard.json \
  certificates/rpb108_rc180_residual_enriched_canonical_inverse.json \
  certificates/rpb108_rc177_three_source_canonical_action_gram.json \
  certificates/rpb108_rc174_regular_source_tail_compression.json \
  certificates/rpb108_rc170_poisson_regular_action.json \
  certificates/rpb108_rc129_four_vector_joint_moment.json \
  certificates/rpb108_rc154_centered_analytic_tail_action.json \
  certificates/rpb108_rc169_native_canonical_transport.json
```

Next: rematerialize the inherited Cpsi carrier for mixed inverse calculations as needed, then certify the actual P0/P2/f0/psi0 inverse response with paid correlated residuals. Keep the dashboard's precision, coverage, and acceptance fields separate. Stage I, original whole-aperture positivity, RH, F4, and Lean remain open/unclaimed.
