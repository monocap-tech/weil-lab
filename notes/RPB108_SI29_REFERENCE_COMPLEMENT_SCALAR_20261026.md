# Original SI29 reference inverse is scalar on the full J470 complement

**October 26, 2026. W-ODD-NEG remains OPEN.** This is a quantitative original-reference inverse compression and a scoped ceiling on its possible residual-weight improvement. It is not the actual Astar inverse, an evaluated energy Schur response, or a new signed positivity certificate.

## GitHub custody

Recover PR #335 at 0e3321350980247f8cba46cdbb45b717e49ad213, successful focused Actions 40417043904. Its full-trial preconditioner remains separate evidence. The canonical manifest still selects open W-ODD-NEG. This result reuses the earlier raw-feature physical Schur witness, not the normalized feature coordinates or an endpoint-aligned representative.

Primary input: successful native Actions 40385192745 at ab41a96861c9e5d0623807e40d53482985d143bc, artifact 12679609974. Archive SHA256 243d40e1fc7d7ce349a0c16c809f06eea0593cd91635d6966241e4f5f478cf33; JSON si29_full_J_L2_normalization.json SHA256 c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60. The workflow verifies original run/source/artifact/archive/JSON custody. Its new computation uses only the standard library and exact Fractions; no native solve or integration is repeated. This composition replay does not independently re-prove the native Gram enclosure.

## Original objects and quantitative result

Let P be the complete physical projection onto the ORIGINAL J470, Q=I-P, and F the ORIGINAL fourteen continuous SI29 mean/first-moment features. The pole s=sinh(x/2) belongs to J470, hence Qs=0. Write E=QF and retain the original positive diagonal weights Gamma. SI29/SM19 supplies the bounded original reference

    B14 = kappa I + F Gamma F* - 2 s s* >= kappa_star I,
    kappa=1/1000, kappa_star=33621/10^9.

This inherited reference coercivity is distinct from the sought full signed positivity.

The pinned native full-J PHYSICAL Schur S=F*QF encloses E*E. Exact dyadic midpoint/radius extraction gives

    ||E||^2 <= ||E||_HS^2 = tr S <= e2 < 10^-512.

The original weights have max gamma=8/25. A continuous mean has absolute integration weight 1 and a first moment has absolute weight 3/2. Consequently

    ||F Gamma||^2 <= ||F Gamma||_HS^2
       <= 2B sum_j gamma_j^2 amplitude_j^2
       = 818166899/1250000000,   B=11/10.

These are bounds on the actual continuous functions, not finite Simpson proxies. The script checks the feature definitions and weights against the pinned native input and composes the original fourteen physical Schur diagonal balls as exact rationals.

## Complete compressed inverse proof

Set V=B14-kappa I. The second resolvent identity is

    B14^-1 = kappa^-1 I - kappa^-2 V
                         + kappa^-2 V B14^-1 V.

All operators in this identity are bounded. This identity requires no order comparison of noncommuting inverse squares. Since Qs=0,

    QVQ = E Gamma E*,       VQ = F Gamma E*.

The final term is positive. Applying B14^-1 <= kappa_star^-1 I gives the ENTIRE compressed Loewner enclosure

    -kappa^-2 gamma_max e2 Q
       <= Q B14^-1 Q - kappa^-1 Q
       <= kappa^-2 kappa_star^-1 ||F Gamma||_HS^2 e2 Q.

The exact relative errors are therefore

    rho_minus = gamma_max e2/kappa,
    rho_plus  = (818166899/1250000000) e2/(kappa kappa_star).

Using the actual rational e2, the checker proves BOTH are strictly less than delta=10^-500. Thus

    (1-delta)/kappa Q <= Q B14^-1 Q <= (1+delta)/kappa Q.

Equivalently, for EVERY bounded residual synthesis R with J*R=0, including ALL 470 coefficient cross terms when R has 470 columns,

    (1-delta)/kappa R*R <= R*B14^-1 R <= (1+delta)/kappa R*R.

This is a full-family operator compression, not a set of scalar source tests. An exact coupled three-dimensional regression checks the pole sign, resolvent identity and two-dimensional complement cross terms; it also rejects extension outside J-perp. That algebra regression is not original-operator numerical evidence. The analytic proof above and inherited SI29/native input standing remain explicit and separate from CI.

## Computational consequence and scope

For an EXACT Galerkin residual R=J-Astar Z whose test space CONTAINS J, J*R=0. Its original MG07 DB=R*B14^-1 R can be bounded by 1000(1+10^-500)R*R without separately computing the fourteen-feature residual Gram or the pole Woodbury correction. Conversely this FIXED reference can reduce the 1000R*R charge by at most the relative factor 10^-500. Further feature/pole correction bookkeeping cannot yield a material residual-weight improvement on this residual family.

If the test space also contains all actual F, the already-known stronger identity DB=1000R*R holds EXACTLY. The new result covers every exactly J-orthogonal residual even without F-orthogonality. It does not quantify approximate orthogonality: a numerically small J*R must not be substituted for zero without a separate leakage bound.

This does not restart the already stopped fixed source-only Ritz/cap method. It resolves one reference-weight subproblem for applicable future complete residual tests. It does not show that SI29 is dispensable: its pole-conditioning certificate is used in the proof. It also does NOT bound how much an SI29-enriched trial may improve the ACTUAL Astar energy Schur response. A small physical feature residual can have a small energy Schur and small matched forcing whose ratio still matters; those actual energy objects remain uncomputed.

Complete original strong residual R*R, actual Astar projection and inverse, matched energy-Schur response, signed negative coupling, full original infinite-operator transfer and independent domain/analytic review remain OPEN. No negative action is transported under J additions. Even/CC27/Weil/RH remain OPEN. Draft/unmerged, stacked on PR #335.
