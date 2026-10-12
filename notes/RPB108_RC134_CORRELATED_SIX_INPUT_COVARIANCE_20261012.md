# RPB108 — RC134: correlated full six-input covariance

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Parent RC133, 5356cac08f038d1198b8822002993a85ef6724e8.

## Result

The entire six-input projected covariance has a paid correlated Loewner upper. A finite-action distance certificate also proves genuine remaining leakage in the v_10 row:

\[
8.300730\times10^{-7}<R_{vv,E}<1.195479\times10^{-6},
\qquad
\boxed{R_{vv,E}/G_{vv}\ge0.000844756653.}
\]

Thus the selected six-vector family cannot meet a relative v-coordinate small-variance target below 0.000844756653. This is an actual residual lower after projection onto E, not merely a broad endpoint interval. It does not obstruct original Weil positivity or an inverse bound that can tolerate this residual.

The paid source difference satisfies ||z-v||_D^2<2.379447e-8, retaining a shared leading new-vector residual channel with a controlled correction. The full covariance upper preserves both that correlation and RC132's w-alpha*psi correlation for arbitrary signed/complex inputs.

The paid Cv trial upper improves the generic positive-contraction coordinate upper by over 205-fold. The numerical Schur lower test still fails with RC133's current endpoint intervals; no new inverse-response interval follows.

## Definitions and scope

Use RC133's exact six-vector family U=(P_0,psi_0,f_0,w_14,v_10,z_b,6) and E=span(U). The six-dimensional independence certificate is retained. Write v=v_10 and z=z_b,6.

For each source u in E define r_u=(I-Pi_E)Cu. The full projected covariance is R_E(U)_ij=<r_i,D r_j>. This pass certifies an upper for every six-input mixture, including actions on both newly added source vectors. It also tests a genuine v residual lower, and does not identify the full Cz or Cpsi actions with finite trials.

## Paid Cv action trial

The actual finite prefix of v through even degree 4094 is acted on by the exact endpoint coefficient formula, enclosing every even output through degree 8190. The collective vector v itself is not equated to its finite prefix.

A finite-prefix least-squares calculation selects a rational trial y=sum_i Y_i U_i. The coefficients Y are obtained from a center finite Gram, but their acceptance never relies on inversion of an uncertain Gram: the actual finite residual is independently enclosed coefficient by coefficient in directed arithmetic, and its D-energy upper E_fin is summed exactly upwards.

The entire action error obeys

\[
\|Cv-y\|_D\le
\sqrt{E_{fin}}+\sqrt{E_{trial,tail}}
+\sqrt{E_{output,tail}}+\sqrt{E_{input,omitted}}.
\]

The four terms pay the finite action/trial difference (including constant uncertainty), the trial's full infinite tail, the retained input prefix's full omitted output, and the action of the entire omitted input by contraction. No cross term or omitted source is dropped. All source/polynomial hashes and the RC133 finite Gram are independently reconstructed and matched.

For the trial tail, all infinite features have a common eta_0 factor. The exact signed polynomial in Lambda/z_n is combined across psi, w, v and z *before* absolute values are taken. This preserves known cancellation between overlapping source tails. Its scalar amplitude is bounded by sum_k |q_k| rho^k, and the full tail energy by T times its square.

Since y lies in E, the paid action error bounds ||r_v||_D. Independently, positive contraction implies ||r_u||_D^2<=||u||_D^2/4 for every u in E, by using u/2 as a projection trial. The accepted v upper is the smaller of these two valid bounds.

## Genuine remaining v leakage

For the action of the retained v input prefix, its output through 8190 has second-moment lower Q_L and six finite-family pairing intervals q_i. RC133's finite Gram Loewner lower G_prefix,L is positive definite. Therefore

\[
\operatorname{dist}_D(Cv_{prefix}|_{\le8190},U|_{\le8190})^2
\ge Q_L-\sup_{q\text{ in its intervals}}q^*G_{prefix,L}^{-1}q=:\ell.
\]

The supremum is paid by signed rational interval products, not by inverting an entrywise Gram interval. Restricting output cannot increase distance to the full family. The entire omitted input action changes the restricted distance by at most sqrt(E_input,omitted). Hence

\[
\|r_v\|_D\ge\max(0,\sqrt\ell-\sqrt{E_{input,omitted}}).
\]

Exact downward square-root acceptance subtracts the rational rounding allowance. A positive lower under this test certifies an actual remaining action direction even after the six-vector enrichment; it cannot be attributed solely to broad endpoint pairings.

## Correlated new-vector source difference

The exact finite centers of v and z give the source difference energy through 8190. Above that degree, their analytic moment coefficients are subtracted in their common eta_k basis before taking absolute values. Thus

\[
\|z-v\|_D^2\le d_{z-v},
\qquad
\|r_z-r_v\|_D^2\le d_{z-v}
\]

by contraction and projection contraction. This relation pays the full action difference without asserting that r_z=r_v or that Cz has been computed independently.

RC132's shared relation remains valid in the same E:

\[
\|r_w-\alpha r_\psi\|_D^2\le e_w^2,
\qquad\alpha=0.850307215745097778\ldots.
\]

Its psi upper, inherited f upper and exact P_0 zero row are retained.

## Full six-input Loewner upper

Choose the five residual generators

\[
q=(r_\psi,r_f,r_w-\alpha r_\psi,r_v,r_z-r_v)
\]

with squared norm uppers d=(p,d_f,e_w^2,d_v,d_{z-v}). The source residuals satisfy r_U=Aq, where A has rows

\[
(0,0,0,0,0),\ (1,0,0,0,0),\ (0,1,0,0,0),\
(\alpha,0,1,0,0),\ (0,0,0,1,0),\ (0,0,0,1,1).
\]

Cauchy-Schwarz for five generators yields the accepted full matrix bound

\[
\boxed{0\preceq R_E(U)\preceq A\,[5\operatorname{diag}(d)]\,A^*.}
\]

This is a conservative joint Loewner upper, not the exact covariance or a diagonal covariance assertion. Separate entrywise bounds retain sharper coordinate estimates. In particular,

\[
|R_{vz}-R_{vv}|\le\sqrt{d_vd_{z-v}},
\quad
|R_{zz}-R_{vv}|\le2\sqrt{d_vd_{z-v}}+d_{z-v}.
\]

Exact rational controls verify that opposite new-vector coefficients cancel the common r_v generator, and that w-alpha*psi cancels the leading shared analytic generator. These controls detect a loss of the known covariance correlations; they do not assume residual orthogonality.

## Evidence boundary and next cursor

The full six-input covariance upper is now paid, including every signed/complex source mixture. The v row also has a certified positive lower obstruction. The Cv approximation includes explicit omitted input/output errors; Cz and Cpsi are not evaluated independently.

The complementary Schur lower G_lower+H_lower-R_upper is checked as an exact rational PSD test. Its acceptance status is recorded separately from covariance acceptance. A failed Schur test with these sufficient enclosures does not imply failure of the actual compression or original Weil positivity.

RC135 cursor: capture the certified common new-vector residual/action in a collective response, preserving these signed differences when refining the endpoint Schur enclosure. If broad endpoint intervals dominate, refine them in a correlated basis instead of independently inflating the nearly coincident v,z rows. A new inverse-response interval requires a positive paid compression, not merely existence of this full covariance upper.

RC130's normalized P_0 response interval [0.931327855055,0.931339797136] remains unchanged. No original Weil action, original positivity, whole-aperture extension, F4, RH or Lean result is claimed.

## Reproduction

```bash
python scripts/validate_rpb108_rc134_correlated_six_input_covariance.py \
 --output certificates/rpb108_rc134_correlated_six_input_covariance.json \
 certificates/rpb108_rc133_six_vector_joint_matrices.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json
```

Repeat with --replay. Historical validators are used for reconstruction without editing their files. Replay reverses all finite sums and compares the full rational certificate, including the canonical coefficient hash.
