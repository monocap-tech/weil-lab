# RPB108 RC47 — correlated native Riesz error transport

2026-10-10. Parent RC46: `db68e8fb87875baf6191dd60f914951a88008ab3`.
Only `research/rpb108-route-consolidation` is written.

## Result

RC38's complete mixed physical residual Gram now supplies refined native
Riesz error bounds, both as a whole 8-by-8 Loewner enclosure and as
feature-specific norm allowances. They tighten the actual canonical Gram
attachment and all three original Weil components without changing the
32-mode trials or dropping any prime power or signed pole.

Every same-parity upper-triangular entry of the complete actual original
low-eight head has an interval width **more than 11/4 times smaller** than
RC46's width. The minimum improvement is 2.7507683886...; diagonal
improvements range from 2.7507... to 5.4665.... Opposite-parity entries
remain exactly zero. Generation and rational replay pass.

All eight diagonal intervals still contain zero. No original head floor,
whole-aperture positivity, mixed original-source covariance, or full
1250-feature construction is certified. This is an actual precision
improvement using existing mixed-error information, not a positivity claim.

## Definitions and custody

Use B=11/10, the inherited canonical logarithmic Hilbert carrier D,
physical inclusion i:D->L2(-B,B), and ||i||^2<=rho=252/257. Native
features q_j are the first eight Chebyshev polynomials. R denotes the
actual native Riesz map and V the emitted rounded 32-by-8 trial map from
RC39. Let E_R=R-V, P the physical native Gram, and T=V^*V in physical L2.

RC38 constructed the physical residual d_j=q_j-L_w V_j, satisfying

    E_R=i^*d,
    ||E_R a||_D^2<=rho ||d a||_2^2,
    ||i E_R a||_2^2<=rho^2 ||d a||_2^2.

Here L_w V is the original logarithmic-metric source of the supported
polynomial trial, including its endpoint logarithms. These identities
are inherited from the weak source/Riesz framework; boundedness of L_w
on all physical L2 is neither needed nor asserted.

The certificate pins the byte hashes of the published RC38 metric and
residual certificates, RC39 native attachment, RC42 poles, RC43 primes,
and RC46 archimedean attachment. The script checks their cross-hashes and
reconstructs T from V and the physical Legendre masses. Historical
certificates remain unchanged. RC39's historical feature count 8600 is
not reinstated: RC44's reduced sufficient count remains 1250.

## Correlated physical residual bounds

Let C be the exact Chebyshev-to-Legendre conversion. RC38's nominal
Legendre residual Gram center is Q, with rounding error at most eta D_8,
where D_8 is the physical Legendre mass matrix and

    eta=8 max_entry_halfwidth / min_target_mass.

Thus the nominal native residual Gram is bounded above by

    Q_up=C^*(Q+eta D_8)C.

This congruence retains all native correlations. RC46 instead used the
single collective inequality d^*d<=beta_physical P for every entry.
RC38's source approximation error obeys
||(d-d_nom)a||_2<=delta ||V a||_2. RC47 rounds that inherited delta
upward at denominator 10^20; the increment is proved smaller than 10^-20.

Young's inequality with parameter 1/32 gives the whole-map bound

    d^*d <= B_res=(33/32)Q_up+33 delta^2 T,
    E_R^*E_R <=rho B_res,
    (i E_R)^*(i E_R) <=rho^2 B_res.

These are complete matrix bounds for all eight-feature combinations.
They do not assert that B_res dominates the old bound more tightly in
every direction: both valid bounds remain available. In particular, the
new source-Gram enclosure is the Riesz approximation residual, not the
mixed original Weil source covariance.

For each column, Minkowski yields the sharper allowance

    b_j=(sqrt((Q_up)_jj)+delta sqrt(T_jj))^2,
    e_can,j=sqrt(rho b_j),
    e_phys,j=rho sqrt(b_j),
    v_j=sqrt(T_jj).

The validator rounds square roots upward with exact integer square roots
at denominator 10^18. It proves b_j<beta_physical P_jj for every feature.
The new physical residual squared allowances are approximately

    [0.0001804463, 0.0001438287, 0.0001257483, 0.00009496175,
     0.00008396797, 0.00006707853, 0.00006421275, 0.00005497794].

These are rigorous upper bounds in the certificate; the displayed
decimals are descriptive. Correlations are used before extracting the
diagonal allowances, so native conversion does not lose them to an
entrywise triangle bound.

## Refined actual canonical Gram attachment

Let H=V^*Ghat_32 V be the nominal canonical trial Gram and let
J_ij=<q_i,V_j>_physical. All entries of J are evaluated exactly from C,
the Legendre masses, and the emitted V. Riesz duality gives

    M=R^*R=J+J^*-H_actual+E_R^*E_R.

If E_metric is RC38's mass-relative metric error, then
|(H_actual-H)_ij|<=E_metric sqrt(T_ii T_jj). On the diagonal the
nonnegative error-Gram contribution lies between zero and rho b_i;
off-diagonal its magnitude is at most e_can,i e_can,j. These give new
actual M entry enclosures. The script intersects them with the previous
RC39 intervals. This preserves both certificates and explicitly uses
the nonnegative diagonal structure rather than centering an error Gram
as though it were an arbitrary signed matrix.

## Original-component transport

For any bounded physical self-adjoint remainder K, replacing both trial
arguments by the actual native representatives costs at most

    ||K|| [e_phys,i v_j+e_phys,j v_i+e_phys,i e_phys,j].

The archimedean remainder uses RC46's physical bound ||a_arch-w||<8
and its previously certified trial-remainder intervals. Add the refined
actual canonical M interval to recover the actual original archimedean
head. Its endpoint logarithms and degree-192 regular-kernel error below
10^-23 remain paid exactly as in RC46.

The prime head uses the same formula with RC43's paired-chain physical
operator bound and complete trial head. All seven active powers
2,3,4,5,7,8,9 and both translation orientations remain present.

The signed pole head uses the refined physical error directly in its
cosh/sinh moment intervals, with the parity-specific norm bounds from
RC42. Products are enclosed with their original positive-even and
negative-odd signs; diagonal squares are treated as squares. Both poles
remain attached. Each new component interval is intersected with its
historical interval, and the final component sum is intersected with
RC46's complete original interval.

This calculation retains correlated approximation errors in native
coordinates. It does not evaluate archimedean/prime/pole cross-covariances
or claim cancellation between unknown component errors.

## Complete original diagonal intervals

The following endpoints are rounded further outward for display. Exact
rational endpoints for all 36 upper-triangular entries are in the certificate.

| Feature | Refined actual original Weil diagonal | Width improvement |
|---:|---:|---:|
| 0 | [-0.581285, 0.658717] | >4.23x |
| 1 | [-0.177235, 0.255704] | >2.75x |
| 2 | [-0.262170, 0.314328] | >3.47x |
| 3 | [-0.179581, 0.234421] | >4.09x |
| 4 | [-0.165926, 0.221351] | >4.38x |
| 5 | [-0.142148, 0.175611] | >4.92x |
| 6 | [-0.094062, 0.209873] | >5.04x |
| 7 | [-0.075995, 0.191099] | >5.46x |

Intervals crossing zero do not prove negative directions. Nor do their
positive midpoints establish positivity. The required original matrix
floor remains unresolved; sharper Riesz precision and source-specific
transport are still needed. RC44's complement floor and RC45's full-head
conditioning statement are unchanged.

## Validation and next obligations

Generation uses exact rational arithmetic throughout, including upward
square roots and all intersections. Replay independently converts the
mixed Gram through scalar double sums and verifies the column norm
allowances by squared rational inequalities, without irrational arithmetic.
It checks the whole-map matrices by exact rational PSD checks and
recomputes all transport, historical intersections, and width ratios.

    python scripts/validate_rpb108_rc47_correlated_native_transport.py
    python scripts/validate_rpb108_rc47_correlated_native_transport.py --replay certificates/rpb108_rc47_correlated_native_transport.json

Both pass. The analytic weak-source identities and Cauchy/Young
inequalities above supply the meaning of these rational checks; this
is not a Lean formalization.

The remaining target is the original head floor together with the
complete mixed source residual. Full 1250-feature native entries,
validated precise solves, and the full canonical projection remain
uncomputed. No new aperture positivity, RH/F4, or Lean closure is claimed.
