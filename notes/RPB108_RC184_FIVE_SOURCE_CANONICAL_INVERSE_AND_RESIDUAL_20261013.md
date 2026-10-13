# RC184: actual five-source inverse enclosure and an explicit remaining residual

Parent: RC183, `06bc8a80d99b03d953892ebc36db12f2b46c9fa1`.

RC184 extends the actual canonical inverse response enclosure to S=(P0,P2,f0,psi0,w14). The selected enclosure is valid for every real and complex mixture, but its width 5.513393 fails the local half-Gram gate. The new checkpoint records coverage without calling it precision acceptance. An exact gate witness and a paid nonzero trial residual identify the next enrichment direction.

## Complete native carriers and source geometry

The input w14 carrier's file SHA256 is checked against RC183. The materialized Cpsi carrier reproduces its historical metadata and analytic moment data. The original P0/P2/f0 action columns, exact finite residual direction q, psi action, and native w14 action are assembled with their actual D_n=H_n+s dependence.

Finite mixed source/action and represented action/action sums are accumulated through degree 16382. Above the historical cutoffs, all native analytic source and action coefficients are evaluated by their eta formulas. No finite compression is asserted invariant.

The source Gram includes all overlaps. The exact (P2,Df0)=11/30 pairing is retained. Available native P0/f0/psi0/w14 Gram rows from RC129 intersect the direct coefficient enclosures. The resulting Gram lower is positive.

The trial basis uses the five response directions themselves. The previous q direction is nearly dependent with native w14 at the level of the trial source Gram. Retaining both makes the raw interval congruences broad. Removing q changes the trial basis only; it does not remove a response source or mixed coupling, and it does not alter q's historical meaning.

Actual symmetric first moments are enclosed by intersecting both independent directional action estimates. The old four-source trial block supplies additional intersections. Every intersection is nonempty and the selected first-moment lower is PSD. The stronger adverse interval comparisons K_lower>=a G_upper and K_upper<=2 G_lower fail at this precision. They are recorded as failed checks, not as contradictions of the actual full-domain theorem aG<=K<=2G. Independent interval endpoints can be too broad to imply those stronger comparisons.

## All infinite source and action tails

Write z_n=n(n+1), eta_n=(2n+1)/(z_n D_n),

\[
 A_w(n)=\sum_{k=0}^{14}\mu_k(977132/z_n)^k.
\]

On n>16382, the source tails are eta_n for psi and eta_n A_w(n) for w14. The represented action tails are eta_n times

\[
 1,\quad(1-6/z_n)^{-1},\quad A_w(n),
 \quad\frac32+\sum_{k=0}^{24}\nu_k(\lambda_\psi/z_n)^k-r/D_n,
 \quad(3/2-r/D_n)A_w(n),
\]

in the response/trial order P0,P2,f0,psi0,w14. The finite q carrier is not part of the selected trial basis. Here lambda_psi=8190*8191.

The common eta energy is bounded by B/[D_O,lower (O-1)O], O=16382. Positive tail amplitudes give entrywise tail controls for the source, source/action, and represented action Gram matrices. Weighted Young bounds produce simultaneous Loewner enclosures; no rank-one matrix order is inferred from entrywise bounds.

For the full inverse residual, the native w14 source tail and f0 action tail share A_w(n). Their higher-moment error is combined before absolute values, with coefficient row e_w-Y_f. The varying negative-r factor is centered at r/(2D_O,lower) with its full radius paid.

Let delta_f bound A_w(n)-mu_0, A_w,upper bound A_w(n), and c_w=3/2-r/(2D_O,lower). Then

\[
 |(3/2-r/D_n)A_w(n)-c_w\mu_0|
 \le |c_w|\delta_f+A_{w,upper}r/(2D_{O,lower}).
\]

Together with the P2 and psi remainders, this gives four paid variable residual terms. Cauchy-Schwarz bounds their sum, then Young's inequality pays their coupling with the shared leading eta term. The whole source/action tail remains in the certificate.

## Actual inverse response and selection

The canonical action is M=D^-1 L, L=D+h+R-rI, with aI<=M<=2I and a=32125/230953. The actual target is Sigma=S*D M^-1 S.

Both Galerkin and least-residual midpoint matrices select rational inverse trials. Actual finite residuals are independently accumulated. The whole residual tail is added on disjoint D support, and the full column errors are transformed by the trial coefficient matrix. The weighted Cauchy error envelope includes every real and complex source mixture; no mixed error is declared orthogonal.

The exact variational identity gives residual-based response bounds. Separately, the global structural bounds give G_lower/2 and G_upper/a. The validator tests complete lower/upper combinations from these valid bounds and chooses a certified width. It never performs entrywise matrix optimization. The selected enclosure uses the residual lower and residual upper.

| Five-source trial | Certified relative inverse width | Half-Gram gate |
|---|---:|---|
| Galerkin | 6.588115 | Failed |
| Least residual, selected | 5.513393 | Failed |

The selected local acceptance ratio is 5.513393/(1/2)=11.026786. The guaranteed margin bound from that width is 1/2-5.513393=-5.013393, so it supplies no positive acceptance margin. The actual selected gate failure is also witnessed directly below. These numbers describe the selected enclosure, not a lower bound on true inverse uncertainty.

The selected nominal residual relative Gram upper is 0.162203. Its selected canonical vector-error upper relative to true image energy is 1.442941; that bound is not a contraction certificate. The positive source Gram, full residual bounds, and actual inverse enclosure are nevertheless certified.

## Exact witness and focused next action

The rational source coefficient vector

\[
 x=(-1/120,3/50,-14/25,-26/25,1)^T
\]

represents

\[
 w14-\frac{26}{25}\psi0-\frac{14}{25}f0
      +\frac3{50}P2-\frac1{120}P0.
\]

For the selected gate matrix H=G_lower/2-(Sigma_upper-Sigma_lower), exact arithmetic gives

\[
 x^*Hx<-0.0012566546.
\]

This proves that the selected enclosure fails the gate.

Let Rhat=S-VY and R=S-MS Y. From its full nominal residual Gram lower N_lower and transformed action-error Gram upper E,

\[
 \|Rx\|_D\ge\sqrt{x^*N_{lower}x}-\sqrt{x^*Ex}.
\]

Outward exact square-root bounds certify

\[
 \|Rx\|_D>0.0033582849.
\]

This is a nonzero residual of the selected trial, not an impossibility result for richer trials. It provides a concrete source for the next finite approximation, action evaluation, and inverse enrichment pass.

## Replay, dashboard, and remaining scope

All eighteen inputs are hashed and cross-linked. Replay reverses finite mixed sums, residual sums, trial order, and the finite parameter search. The entire certificate must reproduce exactly. The materialized w14 carrier's bytes are checked against its bound file hash.

Run `scripts/validate_rpb108_rc184_five_source_canonical_inverse.py --replay --output certificates/rpb108_rc184_five_source_canonical_inverse.json` with these files in order: RC183 main action certificate, RC183 materialized w14 carrier, RC182 main inverse certificate, RC182 materialized Cpsi carrier, RC181, RC180, RC179, RC178, RC177, RC176, RC172, RC171, RC129, RC128, RC127, RC121, RC175, RC154.

The dashboard keeps RC182's accepted four-source gate and adds the failed five-source enclosure as a distinct scope. It marks w14 inverse coverage enclosed while precision acceptance remains open. No aggregate completion percentage is assigned.

Next: construct a paid finite approximation of (S-VY)x, evaluate its actual canonical action with all input/output tails, and enrich the five-source inverse trial space. Native v10,z_b6,t10 action/inverse coverage remains subsequent work. Stage I original targets, original whole-aperture positivity, RH, F4, and Lean remain open/unclaimed.
