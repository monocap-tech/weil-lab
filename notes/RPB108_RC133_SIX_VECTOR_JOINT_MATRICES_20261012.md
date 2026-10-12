# RPB108 — RC133: six-vector joint Gram and endpoint pairings

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Parent RC132, 80d46a2801c4e997945b636650549f43cc8cb149.

## Result

The selected union has **dimension six**, certified directly from its full finite-prefix Gram. The full Gram obeys

\[
\boxed{G\succeq 10^{-7}\operatorname{diag}(G_{prefix,ii,lower}).}
\]

All 36 joint Gram and endpoint pairing entries are enclosed, including infinite mixed tails. The positive Gram floor resolves RC132's previously open union dimension and supplies a quantitative independence bound.

The new endpoint self-pairing intervals are approximately [0.000439065886,0.000442702491] for v_10 and [0.000438892892,0.000441921829] for z_b,6 (these displayed decimals are descriptive, with exact rational endpoints in the certificate). The resulting endpoint Loewner lower fails its numerical PSD test, and G_lower-H_upper fails its numerical PSD test. Those failures indicate insufficient enclosure precision; they do not contradict C's established positivity/contraction. No tight inverse bound is inferred from these intervals.

## Scope and definitions

This pass evaluates the full joint D Gram and endpoint pairing matrices of the selected union family

\[
\mathcal U=(P_0,\psi_0,f_0,w_{14},v_{10},z_{b,6}),
\qquad E=\operatorname{span}\mathcal U.
\]

Here w_14 is RC128's exact collective Cf_0 trial, v_10 is RC131's selected collective Cg_hat trial, and z_b,6 is RC132's selected collective Cb trial (seven internal analytic features). The finite polynomials and rational moment centers defining these vectors are exact; the action errors relating each trial to its source image remain separate paid estimates.

Let D, C=D^-1 h, s, H_n and z_n retain their established meanings. For a finite family U, define G(U)_ij=<U_i,D U_j> and H(U)_ij=<U_i,h U_j>=<U_i,D C U_j>. These are unprojected joint matrices, distinct from the projected action covariance R_E(U).

## Full Gram and independence

The validator independently reconstructs the RC128 finite g_hat, RC132 balanced source b, and both new collective finite output polynomials. Their historical coefficient hashes must match exactly. It evaluates all six actual finite coefficient prefixes through even degree 8190, including the existing w_14 analytic tail within that prefix. No vector is replaced by its source image.

Above 8190, every analytic coefficient is nonnegative and dominated by A_i eta_0,n. The psi coefficient has amplitude one, w_14 uses its inherited lambda-scaled moments, and the new vectors use their Lambda-scaled moments. The complete tail energies satisfy

\[
\|U_{i,tail}\|_D^2\le t_i:=T A_i^2,
\]

where T is RC131's paid leading eta_0 D-energy upper. Tail Gram entries lie between zero and sqrt(t_i t_j). Thus every infinite mixed Gram term is enclosed.

For independence, it is stronger to retain the tail Gram as a PSD block rather than subtract entrywise tail uncertainty from the finite-prefix lower. Directed finite Gram entries yield a finite-prefix Loewner lower G_prefix,L. The full Gram satisfies

\[
G\succeq G_{prefix,L},
\qquad
G\preceq G_{prefix,U}+6\operatorname{diag}(t_i).
\]

An exact rational PSD test searches a positive relative diagonal floor beneath G_prefix,L. This directly tests joint independence of the two added classes modulo the old U; individual independence from U is not used as a substitute.

## All endpoint pairings, with finite and infinite omissions paid

The old four-input endpoint block is inherited from RC129. For every genuinely new pair, positive coefficient sums evaluate the endpoint prefix through even degree 4094 using

\[
h_{nm}=\begin{cases}
\dfrac{2B}{2n+1}\left(2H_{2n}-2H_n+\dfrac1{2n+1}-\log2\right),&n=m,\\
\dfrac{2B}{|z_n-z_m|},&n\ne m,
\end{cases}
\qquad B=11/10.
\]

All these scalar coefficients are nonnegative. Therefore the finite endpoint prefix is a lower for the full pairing. The omitted source energy includes the *evaluated* finite coefficients at even degrees 4096..8190 and the full analytic tail above 8190. Neither portion is assigned zero.

Writing p_i and r_i for prefix and omitted D-energy uppers, C's inherited positive contraction gives the complete omitted mixed upper

\[
|h(U_i,U_j)-h(U_{i,prefix},U_{j,prefix})|
\le\sqrt{p_i r_j}+\sqrt{p_j r_i}+\sqrt{r_i r_j}.
\]

It covers both asymmetric mixed blocks and the tail-tail block. A second upper sqrt(G_ii,upper G_jj,upper) is available by contraction. Historical action identities tighten new mixed pairs:

- CP_0=a P_0+psi_0+f_0 supplies the P_0 row exactly from the full Gram.
- RC128's paid Cf_0-w_14 norm error tightens the f_0 row.
- RC131's paid Cw_14-v_10 norm error tightens the w_14 row.

Every intersection is checked nonempty. Weighted interval radii produce full endpoint Loewner enclosures. Their numerical PSD/contraction tests are reported as explicit booleans; structural 0<=H<=G inherited from C is not mislabeled as a passed numerical enclosure test.

## Evidence boundary and next cursor

A full entrywise endpoint certificate can be valid while its Loewner interval is too broad for a tight inverse calculation. The finite endpoint prefix and paid omitted source energies are stored so that further refinement can target the actual enclosure uncertainty. Increasing the endpoint cutoff or certifying new-vector actions can tighten it.

RC132's shared old-input covariance estimates apply to this same selected union span. New-vector actions Cv_10 and Cz_b,6, the remaining Cpsi_0 action, and complete six-input projected covariance are not certified here. Those are required before a new covariance-based Schur inverse bound.

RC134 cursor: use the now explicit joint family and its conditioning certificate to tighten endpoint/action uncertainty, then certify the remaining analytic and new-vector covariance block. Preserve the exact CP_0 row and paid Cf_0 row; do not transfer a four-input covariance upper into a six-input inverse calculation.

RC130's normalized P_0 response interval [0.931327855055,0.931339797136] remains unchanged. No original Weil action, original positivity, whole-aperture extension, F4, RH or Lean advance is claimed.

## Reproduction

```bash
python scripts/validate_rpb108_rc133_six_vector_joint_matrices.py \
 --output certificates/rpb108_rc133_six_vector_joint_matrices.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json
```

Repeat with --replay to reverse reconstruction, Gram and endpoint summation order and compare the complete rational certificate. RC132's immutable validator is used only for source/polynomial reconstruction; no historical files are edited.
