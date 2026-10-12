# RPB108 — RC136: seven-vector joint matrices and correlated endpoint row

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Parent RC135, 2c0bd82172f1266b4ebc3f2bf766d11377e5e7ff.

## Result

The full selected seven-vector family has a positive Gram lower with relative finite-prefix diagonal floor 10^-7. All 49 joint Gram and endpoint entries are enclosed, including infinite mixed tails and the new t_10 row.

The correlated new endpoint row additionally certifies

\[
\boxed{|H(w,t)-\alpha H(\psi,t)-G(z_b,t)|
<2.886555\times10^{-9}.}
\]

The common-source endpoint pairing H((v+z)/2,t) lies approximately between 0.000206420959767 and 0.000206797746394; the exact rational endpoints are in the certificate. Its constraint from the paid Cu-t action and the centered signed-difference constraint are retained jointly, rather than discarded in separate v/z row errors.

The numerical PSD tests for H_lower and G_lower-H_upper both remain false with the current conservative endpoint intervals. No tight inverse bound follows from those enclosures. The seven-input covariance, especially the new Ct action and analytic remainder, remains open.

## Definitions and selected family

Keep RC135's selected t_10, the collective finite-source trial at relative norm target 10^-12 with eleven internal output-tail features. The exact seven-vector family is

\[
U_7=(P_0,\psi_0,f_0,w_{14},v_{10},z_{b,6},t_{10}),
\qquad E_7=\operatorname{span}(U_7).
\]

Define u=(v+z)/2 and delta=z-v. The Gram is G_ij=<U_i,D U_j>, and the endpoint pairing matrix is H_ij=<U_i,D C U_j>. These unprojected joint matrices are distinct from the projected covariance R_E7(U_7).

RC135's independence proof and old-six covariance apply to exactly this selected span. This pass evaluates its full Gram and full endpoint matrix, with explicit signed endpoint correlations. It does not import old-six covariance as a complete seven-input bound.

## Full Gram and quantitative independence

The validator independently reconstructs the exact RC135 finite common source and t_10 polynomial, matching both hashes. It extends each old analytic coefficient family through even degree 16382 and evaluates all 49 finite-prefix Gram entries in directed arithmetic.

Above 16382, all seven tails share a positive leading eta_0 shape. Psi uses amplitude one; w uses its z_988-scaled positive moments; v and z use their z_4094-scaled moments; t uses its z_8190-scaled moments. For the recorded amplitudes A_i and paid tail energy T_new,

\[
\|U_{i,tail}\|_D^2\le t_i=T_{new}A_i^2,
\quad 0\le G_{ij,tail}\le\sqrt{t_it_j}.
\]

Every omitted mixed Gram term is paid. The entire tail Gram is PSD, so the full Gram has the finite-prefix Loewner lower. Its upper is the finite-prefix Loewner upper plus 7 diag(t_i). An exact rational PSD test certifies a positive relative diagonal floor under the finite-prefix lower. This provides a quantitative joint independence certificate, beyond RC135's dimension proof.

No polynomial trial is substituted for its source image, and no overlapping Gram support is discarded.

## Complete new endpoint row

The old six-input endpoint block is inherited from RC133. Positive finite endpoint sums evaluate every new t pairing through degree 4094. The omitted source energy explicitly includes all actual finite/analytic coefficients between degrees 4096 and 16382, together with the entire infinite tail above 16382.

If p_i and r_i bound retained and omitted D-energy, contraction gives the complete omitted pairing upper

\[
\sqrt{p_i r_t}+\sqrt{p_t r_i}+\sqrt{r_i r_t}.
\]

Positivity of the coefficient sums supplies a finite-prefix lower. This pays both mixed blocks and the tail-tail block, and is intersected with the global pairing upper sqrt(G_ii,upper G_tt,upper).

The exact CP_0 relation and the paid Cf_0-w and Cw-v action estimates tighten the P_0, f and w entries in the new row.

## Correlated endpoint identities

Three constraints are recorded before being used to tighten the scalar row intervals.

First, RC135's paid full action norm ||Cu-t||<=epsilon_u gives

\[
|H(u,t)-G_{tt}|\le\epsilon_u\sqrt{G_{tt,upper}}.
\]

This is a joint constraint on (H(v,t)+H(z,t))/2, not two independently inflated pairings.

Second, positive contraction gives ||C-I/2||<=1/2. Hence

\[
\left|H(\delta,t)-\frac12G(\delta,t)\right|
\le\frac12\sqrt{G_{\delta\delta,upper}G_{tt,upper}}.
\]

The signed difference Gram is enclosed from the actual new mixed Gram entries. The known full delta energy upper is retained. The common and difference constraints are intersected with the original finite-sum row intervals, then converted back to paired v and z entries.

Third, RC132's exact shared source identity and paid Cb-z_b error imply the unprojected action bound

\[
\|Cw-\alpha C\psi-z_b\|_D\le e_{shared},
\]

so

\[
|H(w,t)-\alpha H(\psi,t)-G(z_b,t)|
\le e_{shared}\sqrt{G_{tt,upper}}.
\]

The same norm bound used for RC132's projected residual relation is valid before projection: it came from the full Cb trial error plus the full higher analytic action norm. Projection is not reversed as an inference. This provides a tight shared analytic constraint between the new w and psi row entries.

All intersections are verified nonempty. The three signed constraints remain stored as certificate data alongside the scalar entry intervals; they are not lost when a conservative weighted Loewner enclosure is formed.

## Numerical enclosure tests and evidence boundary

The full endpoint matrix receives weighted entry-error Loewner enclosures. The numerical PSD test of H_lower and of G_lower-H_upper is reported separately from C's structurally inherited positivity/contraction. A broad interval failing those tests is insufficient for a tight inverse calculation, not evidence of an actual negative endpoint operator.

RC135's full old-six covariance in the same seven-dimensional projection span remains valid. The new vector's complete Ct_10 action and the complete seven-input covariance are still open. No six-input covariance is substituted for those missing data.

RC137 cursor: certify Ct_10 and the remaining analytic covariance in E_7, using the common/difference and shared-analytic identities when refining a conditioned Schur enclosure. The analytic input floor remains paid; high finite-source action accuracy is not full inverse accuracy.

RC130's normalized P_0 response interval [0.931327855055,0.931339797136] remains unchanged. No original Weil action, original positivity, whole-aperture extension, F4, RH or Lean result is claimed.

## Reproduction

```bash
python scripts/validate_rpb108_rc136_seven_vector_joint_matrices.py \
 --output certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc135_common_response_capture.json \
 certificates/rpb108_rc134_correlated_six_input_covariance.json \
 certificates/rpb108_rc133_six_vector_joint_matrices.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json
```

Repeat with --replay. Reverse reconstruction, Gram and endpoint summation order must reproduce the complete rational certificate. Historical validators are used for reconstruction without edits; only additive RC136 files are committed.
