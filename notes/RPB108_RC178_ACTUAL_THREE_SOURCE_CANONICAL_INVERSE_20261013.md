# RC178: actual three-source canonical inverse, with explicit remaining residual

Parent: RC177, `bef9b6cb547a05c5d260a67e5474e6ad3371fefa`.

RC178 extends the actual canonical inverse response certificate to S=(P0,P2,f0). The best tested enclosure has relative width 0.997665 and does not pass the half-Gram width gate. The certificate is valid, but the richer source family exposes a residual that the current three-vector inverse trial space does not remove. An exact failure witness and a paid residual direction make the next obligation concrete.

## 1. Actual inverse target and two trials

The target is

\[
 \Sigma=(DS)^*L^{-1}(DS)=S^*DM^{-1}S,
 \quad M=D^{-1}L,\quad L=D+h+R-rI.
\]

RC121 supplies aI<=M<=2I in D energy, a=32125/230953. RC177 supplies the correlated G=S*DS, K=S*DMS and represented action Gram Qhat=V*DV, with full-column action error Gram E0. The nonzero P2/f0 source pairing 11/30 remains in every matrix calculation.

Two rational trials are evaluated:

\[
 Y_G=K_{mid}^{-1}G_{mid},\qquad
 Y_R=\widehat Q_{mid}^{-1}K_{mid}.
\]

Every entry is rounded to a 10^-30 rational grid. The midpoint matrices only choose a trial. No exact optimizer or invariant finite compression is inferred from them. Both trials are certified using independently accumulated, signed, full residual coefficients.

## 2. Full residual, including native analytic tails

The represented residual is Rhat=S-VY and the actual residual is R=S-MS Y. Finite coefficients are accumulated through O=4094, using the immutable RC177 action-carrier generator. Native w14 reconstruction must reproduce RC128's historical coefficient hash.

Above O the source S itself vanishes, and the action tails are

\[
 \eta_n,\quad\eta_n/(1-6/z_n),\quad
 \eta_n\sum_{k=0}^{14}\mu_k(\lambda/z_n)^k,
 \qquad z_n=n(n+1),\quad\lambda=977132.
\]

Let T be RC177's full eta D-energy tail upper, z_first=(O+2)(O+3),

\[
 \delta_2=6/(z_{first}-6),\qquad
 \delta_f=\sum_{k=1}^{14}\mu_k(\lambda/z_{first})^k,
 \qquad b=Y_{0,:}+Y_{1,:}+\mu_0Y_{2,:}.
\]

With t=1/1000, the entire residual-tail Gram is bounded above by

\[
 (1+t)T b^*b+
 2(1+1/t)T[\delta_2^2Y_{1,:}^*Y_{1,:}
                    +\delta_f^2Y_{2,:}^*Y_{2,:}].
\]

The common eta term and both native tail remainders are retained. Young's inequality pays their correlations; no orthogonality is assumed. The finite residual and this omitted tail have disjoint D support. They give nominal residual enclosures N_lower,N_upper.

The represented-to-actual residual error Gram is bounded by E=Y*E0Y. For positive tau and sigma in (0,1),

\[
 R^*DR\le(1+\tau)N_{upper}+(1+1/\tau)E,
\]

\[
 R^*DR\ge(1-\sigma)N_{lower}-(1/\sigma-1)E,
\]

whenever the latter lower matrix is PSD. Zero is always available as a lower bound. The finite candidate set is evaluated exactly; it is not claimed globally optimal.

## 3. Exact variational identity and inverse enclosure

For X=SY, the actual variational term is C=G Y+Y*G-Y*K Y. The identity

\[
 \Sigma=C+R^*DM^{-1}R
\]

is exact. Actual G,K uncertainty is paid using

\[
 C=G-(I-Y)^*G(I-Y)+Y^*(G-K)Y.
\]

Consequently the selected actual residual bounds R_lower,R_upper give

\[
 C_{lower}+\tfrac12R_{lower}\le\Sigma
 \le C_{upper}+a^{-1}R_{upper}.
\]

The certificate also checks that these bounds improve the full-space structural enclosure G/2<=Sigma<=G/a, using adverse actual Gram endpoints.

| Trial | Certified relative inverse width |
|---|---:|
| Galerkin | 1.154778 |
| Least residual, selected | 0.997665 |

For the selected trial, Sigma_upper-Sigma_lower <= 0.997665 G_lower is verified by exact rational PSD arithmetic. The next smaller millionth fails. The selected residual upper parameter is 1/100; the selected residual lower matrix is zero. The true inverse uncertainty is not claimed to be this large.

The selected inverse trial has canonical-energy error Gram at most R_upper/a and D-error Gram at most R_upper/a^2. Relative to the true image energy Sigma, its canonical norm error is below 0.588756. This is a warm-start certificate, not an executed Riesz iteration.

## 4. Exact gate witness and concrete next residual

The half-Gram gate matrix is

\[
 H=\tfrac12G_{lower}-(\Sigma_{upper}-\Sigma_{lower}).
\]

For the exact rational source coefficient vector

\[
 x=(-1/1200,-1/6,1)^T,
 \qquad Sx=f0-P2/6-P0/1200,
\]

the certificate computes x*Hx < -0.0069801204. This proves that the selected enclosure fails the half-Gram gate. It does not prove that another enclosure or trial cannot pass.

The represented focus residual is (S-VY)x. If n=x*N_lower x and e=x*E x, the actual residual satisfies

\[
 \|Rx\|_D\ge\sqrt n-\sqrt e.
\]

Exact outward square-root bounds give

\[
 \|Rx\|_D>0.0414247834,\qquad
 \frac{\|Rx\|_D^2}{\|Sx\|_D^2}>0.1223314401.
\]

The represented focus residual differs from the actual one by D norm below 0.000498715420. Thus the selected trial has a paid, substantial residual on this explicit source mixture. These are statements about this trial, not impossibility statements for richer trial spaces.

Next action: construct a finite approximation to (S-VY)x, pay its full input tail, and evaluate its actual canonical action with full output tails. That supplies an enrichment direction for the inverse trial space. The bounded canonical action M<=2I can transfer a paid input approximation error; it cannot substitute for evaluating the retained input's actual action.

## 5. Replay, custody, and remaining scope

All ten inputs are hashed and cross-linked. Generation and replay reverse native w14 reconstruction sums, inverse-trial order, finite residual sums, and the enclosure search order; the selected certificate must reproduce exactly. Historical checkpoints are additive and unchanged.

```bash
python scripts/validate_rpb108_rc178_three_source_canonical_inverse.py \
  --replay --output certificates/rpb108_rc178_three_source_canonical_inverse.json \
  certificates/rpb108_rc177_three_source_canonical_action_gram.json \
  certificates/rpb108_rc173_canonical_inverse_response.json \
  certificates/rpb108_rc176_f0_regular_output_carrier.json \
  certificates/rpb108_rc172_quadratic_regular_action.json \
  certificates/rpb108_rc171_regular_legendre_projection.json \
  certificates/rpb108_rc129_four_vector_joint_moment.json \
  certificates/rpb108_rc128_collective_second_response.json \
  certificates/rpb108_rc127_enriched_even_endpoint_action.json \
  certificates/rpb108_rc121_diagonal_metric_equivalence.json \
  certificates/rpb108_rc175_f0_regular_physical_source.json
```

RC173's two-source certificate and half-Gram pass remain intact. RC178 does not replace that result with the three-source gate failure. The new inverse enclosure covers all real and complex P0/P2/f0 mixtures, but the native seven-source frame and its full canonical inverse remain separate.

Stage I is open. The actual original augmentation adjoint range and required full matrix tolerance remain unidentified here; neither the original augmented Weil floor nor its auxiliary response bound is certified. No original positivity, whole-aperture original positivity, RH, F4, or Lean claim is made.
