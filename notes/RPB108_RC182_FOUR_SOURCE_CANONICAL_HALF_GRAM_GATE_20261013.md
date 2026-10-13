# RC182: materialized psi carrier closes the four-source canonical gate

Parent: RC181, `68d742a940ed624c7004dc7b39e99a5ed3e67e58`.

RC182 materializes RC154's complete Cpsi carrier and extends the actual canonical inverse response to S=(P0,P2,f0,psi0). Both tested five-direction trial families pass the local half-Gram gate. The selected width is 0.450753, its acceptance ratio is 0.901506, and its guaranteed gate margin is 0.049247 times the source Gram lower. This is a coverage expansion, not a decreasing-width comparison against the previous three-source family.

## Historical carrier reproduced

The inherited endpoint trial is Q(psi[990..8190])+(1/2)psi[8192..infinity]. Its finite output coefficients are reconstructed through degree 16382 with the original 70-digit directed generator. Every center/radius pair is included in the historical coefficient digest; the digest reproduces RC154 exactly. All 26 moment intervals also reproduce exactly: orders 0..24 are retained, and order 25 controls the geometric remainder. The inherited whole Cpsi action error reproduces as well.

The companion `rpb108_rc182_materialized_Cpsi_carrier.json` stores 8192 finite coefficient centers, in even-degree order from 0 through 16382, and the full analytic moment data. The half-input-tail term remains an exact analytic source. RC181's bounded regular zero carrier and its full error remain unchanged.

For the actual supported canonical M=D^-1 L, L=D+h+R-rI, the represented psi action is

\[
 V_\psi=\psi+Q_{C\psi}-rD^{-1}\psi.
\]

The negative-r coefficients use the actual D_n=H_n+s, not a substituted scalar. The full endpoint-plus-regular error is inherited from RC181. Materialization makes the coefficients usable for signed mixed Gram and inverse residual calculations; it does not lower that inherited action error.

## Four response sources and five trial directions

The response sources are S=(P0,P2,f0,psi0). The trial basis is T=(P0,P2,f0,q,psi0), with exact finite q from RC179. The inverse coefficient matrix is five-by-four. The native seven-source frame is unchanged.

The D support of psi begins at degree 990, above every finite source in the old trial family. Thus its source Gram is an exact scalar block added to the previous Gram. The P2/f0 overlap remains in the previous block. Positive source Gram lowers certify all source and trial vectors are independent; they are not treated as Euclidean coordinates.

All finite represented action/source and action/action pairings are evaluated through degree 16382. Beyond the old cutoff 4094, the previous P0/P2/f0 action columns are evaluated from their exact native eta tail formulas. The represented q action is finite through 4094. The actual q output tail remains in its paid action error.

Self-adjointness intersects both independently paid directional first-moment rows. The old four-direction canonical entries supply additional intersections. Every intersection is nonempty. The adverse matrix endpoints verify a G_T<=K_T<=2G_T, a=32125/230953.

## Entire infinite tail and the varying negative-r term

Above O=16382, let eta_n=(2n+1)/(n(n+1)D_n), z_n=n(n+1), and lambda_psi=8190*8191. The represented action coefficients are eta_n times

\[
 1,\quad(1-6/z_n)^{-1},\quad
 \sum_{k=0}^{14}\mu_k(977132/z_n)^k,\quad0,
 \quad\frac32+\sum_{k=0}^{24}\nu_k(\lambda_\psi/z_n)^k-r/D_n.
\]

The source psi itself contributes eta_n to the fourth response residual. All of these terms are retained in the common-tail calculation.

The eta D-energy tail is bounded by

\[
 T_\eta\le\frac{B}{D_{O,lower}(O-1)O}.
\]

The first-moment source/action tail entries and represented action-Gram tail entries have nonnegative coefficients and are bounded entrywise by their positive amplitude products times T_eta. Weighted Young bounds convert complete entry intervals into simultaneous Loewner bounds. No rank-one upper is inferred merely from entrywise bounds.

For inverse residual tails, the diagonal factor r/D_n varies over the infinite tail. Since 0<=r/D_n<=r/D_O,lower, its midpoint r/(2D_O,lower) has radius r/(2D_O,lower). This radius is paid together with the higher psi moment terms. Define

\[
 \delta_2=6/(z_{first}-6),\quad
 \delta_f=\sum_{k=1}^{14}\mu_k(977132/z_{first})^k,
\]

\[
 \delta_\psi=\sum_{k=1}^{24}\nu_k(\lambda_\psi/z_{first})^k
                      +r/(2D_{O,lower}).
\]

The common residual coefficient is

\[
 b=e_{\psi,response}^T-Y_{0,:}-Y_{1,:}-\mu_0Y_{2,:}
       -(3/2+\nu_0-r/(2D_{O,lower}))Y_{4,:}.
\]

With t=1/2, the whole tail Gram is bounded above by

\[
 (1+t)T_\eta b^*b+
 3(1+1/t)T_\eta[\delta_2^2Y_{1,:}^*Y_{1,:}
  +\delta_f^2Y_{2,:}^*Y_{2,:}+\delta_\psi^2Y_{4,:}^*Y_{4,:}].
\]

The three variable remainders are paid by Cauchy-Schwarz, then mixed with the common tail by Young's inequality. Freezing r/D_n without its radius would omit a genuine tail contribution; the certificate does not do that.

## Actual inverse enclosure

Both Galerkin and least-residual midpoint matrices select rational trials only. Actual finite inverse residuals S-VY are accumulated independently. Their full tail is added on disjoint D support. The five-column action errors are bounded for all real and complex mixtures by a diagonal weighted Cauchy envelope; the transformed error is Y*E0Y. No mixed error orthogonality is assumed.

The rectangular variational identity is unchanged:

\[
 \Sigma=S^*DM^{-1}S=C+R^*DM^{-1}R,
\]

\[
 C=G_S-(J-Y)^*G_T(J-Y)+Y^*(G_T-K_T)Y,
 \quad J\text{ embeds response indices }0,1,2,4.
\]

The source/first-moment uncertainty is paid by adverse Loewner congruences. Residual Young bounds and I/2<=M^-1<=I/a give the actual inverse enclosure.

| Trial on the four-source response family | Certified width | Half-Gram gate |
|---|---:|---|
| Galerkin | 0.484866 | Passed |
| Least residual, selected | 0.450753 | Passed |

The selected upper residual parameter is 1/3 and the selected residual lower is zero. Both trials improve the full-space structural inverse bounds.

The exact PSD width check gives

\[
 \Sigma_{upper}-\Sigma_{lower}\preceq0.450753G_{lower},
\]

\[
 \tfrac12G_{lower}-(\Sigma_{upper}-\Sigma_{lower})
 \succeq0.049247G_{lower}.
\]

The local acceptance ratio is 0.450753/(1/2)=0.901506<1. The selected canonical warm-start norm upper is below 0.547610 relative to the true image energy. This is a separate measurement with no warm-start threshold selected here. It is not an executed Riesz iteration.

## Replay, dashboard, and next obligation

All seventeen inputs are hashed and cross-linked. Replay reverses Cpsi reconstruction, native carrier recovery, finite Gram/residual sums, trial order, and the residual-parameter search. Both the main certificate and materialized carrier must reproduce exactly.

Invoke `scripts/validate_rpb108_rc182_four_source_canonical_inverse.py` with `--replay`, the main certificate as `--output`, the materialized carrier as `--carrier-output`, and these certificate checkpoints in order: RC181, RC180, RC179, RC178, RC177, RC176, RC172, RC171, RC129, RC128, RC127, RC121, RC175, RC154, RC130, RC151, RC153. All input basenames are recorded in the surrounding repository and their bytes are bound by the certificate hashes.

The current completion dashboard now records this four-source gate separately from RC180's three-source gate. The width increased because the response family changed; coverage grew. The even-sector inverse now includes the native P0,f0,psi0 and auxiliary P2. No odd-sector or original augmentation source-range coverage is supplied by this result.

Next: extend actual canonical action and inverse coverage toward w14,v10,z_b6,t10. The full native seven-source inverse, Stage I original augmented floor/auxiliary response, original whole-aperture positivity, RH, F4, and Lean remain open/unclaimed.
