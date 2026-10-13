# RC180: residual enrichment closes the three-source canonical half-Gram gate

Parent: RC179, `341d73b6367e52dadaa485fae68734be4b58c134`.

RC178's actual canonical inverse enclosure on S=(P0,P2,f0) had relative width 0.997665 and failed the half-Gram gate. RC179 constructed the exact finite polynomial q approximating its focus residual and evaluated the complete actual canonical action on q. RC180 adds q to the inverse trial basis, pays its mixed Gram rows and all correlated residual errors, and closes the original three-source gate with relative inverse width 0.300941.

The response sources remain S=(P0,P2,f0). The trial basis alone becomes T=(P0,P2,f0,q). The native seven-source frame retains its historical definition.

## 1. Actual target and independent enriched trial basis

The target is

\[
 \Sigma=(DS)^*L^{-1}(DS)=S^*DM^{-1}S,
 \quad M=D^{-1}L,\quad L=D+h+R-rI.
\]

RC121 gives aI<=M<=2I in D energy, a=32125/230953. The exact source overlap (P2,Df0)=11/30 remains in all matrices.

The four-by-four source Gram G_T=T* D T is evaluated from actual finite source coefficients and the inherited original three-source block. The q coefficients are exact rational centers from RC179. The positive Loewner lower for G_T proves q is independent of the previous trial basis. No approximate orthogonality is used.

The canonical first moment K_T=T* D M T is evaluated by intersecting both directional action pairings. For each mixed entry,

\[
 (T_i,DV_j)\pm\sqrt{(G_T)_{ii}}\epsilon_j,
 \qquad
 (T_j,DV_i)\pm\sqrt{(G_T)_{jj}}\epsilon_i
\]

both enclose the same self-adjoint entry. All intersections are nonempty. The historical RC177 block and RC179 q diagonal give additional controls. The adverse endpoints verify a G_T<=K_T<=2G_T.

The represented action Gram Qhat_T=V* D V is also evaluated in full. Above degree 4094, the first three represented action columns retain their native analytic tails; the represented q action is exactly zero there. The actual q action's omitted tail is already paid by RC179's full column error. This distinction prevents counting a finite carrier as an invariant compression.

## 2. Correlated action error and trial selection

Let e_i=M T_i-V_i and w_i=sqrt((G_T)_{ii,upper}). With all four inherited full-column errors epsilon_i, the diagonal matrix

\[
 E_{0,ii}=\epsilon_i w_i\sum_j\epsilon_j/w_j
\]

bounds the error of every real or complex trial mixture. The exact check E0-epsilon epsilon*>=0 is included; applying it to coefficient absolute values proves the full mixture bound. No mixed error is discarded.

Two rational four-by-three matrices are selected and independently certified:

\[
 Y_G=(K_T)_{mid}^{-1}(G_T)_{mid}J,
\]

\[
 Y_R=(\widehat Q_T)_{mid}^{-1}(V^*DS)_{mid},
 \qquad J=\begin{pmatrix}I_3\\0\end{pmatrix}.
\]

Every coefficient is rounded to a 10^-30 rational grid. The second trial uses directly evaluated represented-action/source pairings. Midpoint matrices only choose trials; their actual inverse residuals are accumulated independently.

Because q is an exact chosen polynomial, the error of approximating RC178's focus residual is not charged again to Mq. The full action error on that exact q, less than 0.000043651799, is included in E0. The focus approximation's role was to select a useful direction, not to redefine it as an uncertain vector.

## 3. Full residual and rectangular variational identity

For X=T Y, the actual residual is R=S-M T Y; its represented counterpart is S-VY. The finite residual Gram is accumulated through degree O=4094 using directed signed coefficient products. Above O, S vanishes and the represented q action vanishes. The remaining residual tail is

\[
 -\eta_n\left[Y_{0,:}+
       \frac{Y_{1,:}}{1-6/z_n}
       +\sum_{k=0}^{14}\mu_k(\lambda/z_n)^kY_{2,:}\right],
 \quad z_n=n(n+1),\quad\lambda=977132.
\]

RC178's common eta term and both tail-remainder bounds remain valid for the rectangular Y. They supply a PSD upper for the entire infinite tail. This is added to the finite prefix on disjoint D supports, producing nominal residual bounds N_lower,N_upper.

The actual residual's correlated error Gram is bounded by E=Y*E0Y. Young bounds give

\[
 R^*DR\le(1+\tau)N_{upper}+(1+1/\tau)E,
\]

and a nonnegative lower, whenever valid, from (1-sigma)N_lower-(1/sigma-1)E; zero is always available. All listed rational parameter candidates are tested. No global optimality is claimed.

The exact response identity is

\[
 \Sigma=C+R^*DM^{-1}R,
\]

with

\[
 C=(T^*DS)^*Y+Y^*(T^*DS)-Y^*K_TY
   =G_S-(J-Y)^*G_T(J-Y)+Y^*(G_T-K_T)Y.
\]

The second expression pays actual source and first-moment uncertainty through Loewner congruences. It remains valid when Y is four-by-three. From M^-1 between I/2 and I/a,

\[
 C_{lower}+R_{lower}/2\le\Sigma
 \le C_{upper}+R_{upper}/a.
\]

Both trials also improve the full-space structural enclosure G_S/2<=Sigma<=G_S/a, with adverse actual Gram endpoints.

## 4. Certified gate closure

| Inverse trial | Certified relative width | Half-Gram gate |
|---|---:|---|
| RC178, three-vector least-residual trial | 0.997665 | Failed |
| RC180, enriched Galerkin trial | 0.326463 | Passed |
| RC180, enriched least-residual trial, selected | 0.300941 | Passed |

The selected actual enclosure satisfies

\[
 \Sigma_{upper}-\Sigma_{lower}
 \le0.300941\,(G_S)_{lower}
 \le\tfrac12(G_S)_{lower}.
\]

The width comparison and the half-Gram gate matrix are checked by exact rational PSD elimination. The next smaller millionth fails for the selected width enclosure. This is a bound on the certified enclosure, not a lower bound on true inverse uncertainty.

The selected nominal residual relative Gram upper is 0.017679. Its selected actual residual upper uses tau=1/10; its selected actual residual lower is zero. The transformed full action error is retained.

The inverse trial's canonical-energy error Gram is at most R_upper/a, and its D-error Gram at most R_upper/a^2. Relative to the true image energy Sigma, its canonical norm error is below 0.223665. The true image energy is bounded below by the certified response lower; no Euclidean coefficient norm substitutes for it.

This is an actual inverse-response and warm-start certificate. It does not execute a Riesz iteration or prove a full seven-source inverse bound.

## 5. Replay and remaining obligations

All eleven inputs are hashed and cross-linked. Native w14 reconstruction retains its historical coefficient hash. Generation/replay reverse that reconstruction, the full finite Gram/residual sums, trial order, and enclosure search order. They must produce identical complete certificate JSON.

```bash
python scripts/validate_rpb108_rc180_residual_enriched_canonical_inverse.py \
  --replay --output certificates/rpb108_rc180_residual_enriched_canonical_inverse.json \
  certificates/rpb108_rc179_focus_residual_canonical_action.json \
  certificates/rpb108_rc178_three_source_canonical_inverse.json \
  certificates/rpb108_rc177_three_source_canonical_action_gram.json \
  certificates/rpb108_rc176_f0_regular_output_carrier.json \
  certificates/rpb108_rc172_quadratic_regular_action.json \
  certificates/rpb108_rc171_regular_legendre_projection.json \
  certificates/rpb108_rc129_four_vector_joint_moment.json \
  certificates/rpb108_rc128_collective_second_response.json \
  certificates/rpb108_rc127_enriched_even_endpoint_action.json \
  certificates/rpb108_rc121_diagonal_metric_equivalence.json \
  certificates/rpb108_rc175_f0_regular_physical_source.json
```

Historical RC178's gate failure remains immutable, and RC173's earlier two-source pass remains intact. The new result closes the canonical inverse enclosure gate on the original P0/P2/f0 response family with an enriched trial space.

Next: extend the actual canonical action and inverse response coverage toward the remaining native seven-source directions. Preserve the distinction between canonical conditioning and Stage I's original Weil targets. The original augmentation adjoint range, full required matrix tolerance, actual augmented Weil floor and auxiliary response bound are not certified here. Stage I, original whole-aperture positivity, RH, F4, and Lean remain open/unclaimed.
