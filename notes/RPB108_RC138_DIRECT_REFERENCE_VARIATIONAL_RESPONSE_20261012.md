# RPB108 — RC138: direct reference variational response

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Parent RC137, 3fb7af434df933b3c2fae985b5787adf01072786.

## Result

The normalized P_0 reference inverse response now satisfies

\[
\boxed{0.931329471901\le\Sigma_{00}/G_{00}\le0.931329519543.}
\]

Its interval width is 4.7642e-8, more than 250.662881 times narrower than RC130's width 1.1942081e-5. Both endpoints improve the previous certificate. This is a new actual reference-response enclosure, not a numerical midpoint or an unaccepted Schur estimate.

The best accepted trial uses four source combinations within the existing seven-vector span. No new vector is added. The trial exploiting Ct is also tested but gives a broader interval because its endpoint energy and action error are still relatively loose.

| Trial combinations used | Certified normalized P_0 lower | Certified normalized P_0 upper |
|---|---:|---:|
| P_0, f, w-alpha*psi | 0.931328423159 | 0.931329784584 |
| Those three plus (v+z)/2 | **0.931329471901** | **0.931329519543** |
| Those four plus t_10 | 0.931329423807 | 0.931329538842 |

These are different candidates for one P_0 response, not disjoint covariance blocks or changes in the certified carrier dimension.

## Definitions and target

Keep RC136's seven-dimensional source carrier E with basis U=(P_0,psi_0,f_0,w_14,v_10,z_b,6,t_10), its actual Gram G and endpoint matrix H, and RC137's complete covariance and rounding audit. The global D-energy operator C is positive self-adjoint with 0<=C<=I. Define

\[
A=I+C,\qquad
\Sigma_{00}=\langle P_0,A^{-1}P_0\rangle_D,
\qquad G_{00}=\|P_0\|_D^2.
\]

The reference operator A has I<=A<=2I on the full carrier. The target here is the single normalized P_0 response, not an accurate inverse matrix for every source and not original Weil positivity.

Define the trial source frame

\[
S=(P_0,f_0,B,u,t),\qquad
B=w_{14}-\alpha\psi_0,\quad
u=\frac{v_{10}+z_{b,6}}2,\quad t=t_{10}.
\]

Here the symbol u (the averaged source) is distinct from the analytic output moments nu_k. The exact alpha is the rational coefficient defining the inherited shared-source identity.

## Canceling the leading unknown analytic action

The action frame has fully paid approximants:

\[
CP_0=aP_0+\psi_0+f_0,\qquad
Cf_0=w_{14}+e_f,
\]
\[
CB=z_{b,6}+e_B,\qquad
Cu=t_{10}+e_u,\qquad
Ct_{10}=y_t+e_t.
\]

The first row is exact up to the enclosed real scalar a; the norm of its scalar-center error is paid. The other four error norms are inherited from RC128, RC132, RC135 and RC137, respectively. They are full unprojected action errors, including every finite/analytic omission.

The B row follows from Cw-alpha*Cpsi=Cb+Ca_1 and the paid Cb-z_b trial. Therefore the leading Cpsi action cancels exactly in CB; a full independent Cpsi evaluation is not assumed or performed.

The rational source/action coefficient matrices are stored in the certificate. Their centers are used only to choose each trial, not to accept it as an exact inverse or Galerkin solution.

## Actual residual and endpoint energy acceptance

For a candidate y=sum_j c_j S_j, the nominal residual uses the recorded source and action approximant matrices K=S+T:

\[
r_{nom}=Kc-P_0.
\]

Its actual D norm is bounded by the full seven-vector Gram Loewner upper. The total true residual pays all action errors by the norm triangle:

\[
\|(I+C)y-P_0\|_D
\le\sqrt{r_{nom}^*G_Ur_{nom}}+\sum_j|c_j|\epsilon_j.
\]

Coefficients are exact rationals on a 10^-20 grid, and their actual retained residual is tested after rounding. A center-matrix inverse selects coefficients only; no uncertain Gram or endpoint matrix is inverted as an acceptance step.

Every endpoint pairing H(S_i,S_j) is initially enclosed by transforming RC136's actual entry intervals with signed rational arithmetic. Both action directions then supply additional valid enclosures

\[
|H(S_i,S_j)-G(T_i,S_j)|\le\epsilon_i\|S_j\|_D.
\]

Their intersections preserve the leading analytic cancellation. The exact CP_0 action and paid Cf_0/CB rows keep the large low-mode pairings tight, rather than multiplying the u action error by ||P_0|| or ||f_0|| unnecessarily. Every intersection is checked nonempty.

The true trial norm uses the Gram Loewner bounds, while the true endpoint energy uses the signed frame pairing intervals. The actual P_0-y pairing is also enclosed. Thus the complete variational functional has independently accepted lower and upper bounds; no endpoint tail is discarded.

## Global inverse certificate without a numerical uniform Schur gate

For any trial y, define

\[
L(y)=2\operatorname{Re}\langle P_0,y\rangle_D-\langle y,Ay\rangle_D,
\qquad r=Ay-P_0.
\]

The exact identity is

\[
\Sigma_{00}-L(y)=\langle r,A^{-1}r\rangle_D.
\]

Since I<=A<=2I,

\[
\frac12\|r\|_D^2\le\Sigma_{00}-L(y)\le\|r\|_D^2.
\]

The accepted enclosure is therefore

\[
L_{lower}\le\Sigma_{00}\le L_{upper}+\|r\|_{D,upper}^2.
\]

Division uses the actual positive G_00 bounds, with outward 10^-12 rounding. The final interval intersects all candidate trials and RC130's inherited interval. Its lower and upper both come from the four-combination candidate.

This bypasses the broad sufficient numerical Schur matrix test by validating the desired response directly in the full carrier. It does not ignore the complementary response: every action error in the actual residual is included, and the global inverse bound controls that residual. Twelve exact rational scalar controls include both spectral endpoints C=0,1, intermediate levels and signed trials; they verify the identity and factor-two residual bounds.

## Evidence boundary and RC139 cursor

The new enclosure is only for the normalized P_0 reference response. The existing seven-dimensional family, full covariance coverage and RC137 rounding repair remain intact. Full independent Cpsi action, a uniformly high-accuracy inverse matrix, original Weil source actions and original positivity are not certified by this step.

RC139 cursor: reduce the direct trial residual and tighten the common-source/t endpoint energy uncertainty. The fifth trial's larger certified interval identifies why adding an available trial coordinate need not improve a sufficient enclosure before its energy is tightened. Test the required reference-response tolerance explicitly; do not infer Stage I closure from a narrower interval alone.

Original Weil positivity, whole-aperture extension, F4, RH and Lean standing are unchanged. No completion tolerance is silently assumed from a single-action feature target such as 10^-24.

## Reproduction

```bash
python scripts/validate_rpb108_rc138_reference_variational_response.py \
 --output certificates/rpb108_rc138_reference_variational_response.json \
 certificates/rpb108_rc137_seven_input_covariance.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc135_common_response_capture.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc128_collective_second_response.json \
 certificates/rpb108_rc130_remaining_covariance.json
```

Repeat with --replay to reverse signed pairing/energy sums and compare the entire rational certificate. All predecessor byte hashes and the RC137 rounding audit are checked. Only additive RC138 validator, certificate and note files are committed.
