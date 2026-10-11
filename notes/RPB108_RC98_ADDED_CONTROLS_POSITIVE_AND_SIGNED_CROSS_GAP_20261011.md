# RPB108 RC98 — Added controls pass individually; signed cross remains open

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC97, commit `e38c6b64308065244777a817a10befd6aa37c980`.
Aperture B=1.10. Complete sufficient Riesz head rank 1250.

Both RC63 positive controls pass the original rank-1250-complement directional Schur test. Together with RC94/95, all six selected individual directions now have certified positive corrected value. Positivity of their entire six-dimensional span is not yet certified.

A robust three-mode completion test identifies the remaining gap. The inherited weak pair is positive, and the added control has a positive corrected diagonal, but a cross enclosure obtained from signed head entries and scalar PSD Cauchy bounds is too wide in both parities. This is a limitation of that rectangular enclosure, not an actual negative or null direction of the Weil operator.

No new source integration is performed. RC98 contracts existing source moments before taking bounds, subtracts the 64-mode physical source capture, and transports the remainder directly through the actual rank-1250 canonical complement. The inherited complement floor is applied at that same rank.

## Exact numerical result

Let v denote the added control of each parity. Let Q_lower be its actual original Weil lower and g its actual rank-1250 coupling covariance upper. With alpha=247/2500,

    T(v,v) >= Q_lower − g/alpha = d > 0.

| Quantity | Even control | Odd control |
| --- | ---: | ---: |
| Actual original Weil lower | 1.0169448481e-9 | 1.5469286059e-7 |
| Actual coupling squared upper g | 7.7175109795e-11 | 1.1250255198e-8 |
| Corrected diagonal lower d | 2.3582025505e-10 | 4.0823880851e-8 |
| Accepted source Young parameter | 1/8 | 19/64 |
| Robust box worst inverse penalty / d | 16.71647719 | 2780.16877343 |
| Directional Schur test | Pass | Pass |
| Entire three-mode robust completion | Not certified | Not certified |

The corrected values are bilinear values on the fixed rational RC63 inputs; they are not canonical Rayleigh floors. Displayed decimals do not decide acceptance. The exact rational margins and all four cross-box vertices are in the certificate.

The old four-dimensional corrected weak-span positivity is retained. RC98 does not increase the certified positive-subspace dimension to six. Positive values on six generators do not prove positivity on all their combinations. The RC96 nonpositive-index upper therefore remains 1246; no reduction to 1244 is asserted.

## 1. Tighten the added-control Riesz error before taking norms

Use the unchanged RC67 64-mode Riesz trial V for each native input. For the fixed control coefficient vector v, let z=C_native v be its Legendre target coefficients and let t be its physical trial norm squared.

Contract RC81's raw nominal Legendre residual entry intervals onto z first. If the resulting nominal residual energy is enclosed by center e and radius r, the actual physical Riesz error energy satisfies

    Ep <= rho² [(1+nu)(e+r) + (1+1/nu) delta_L² t],
    rho=252/257, nu=1/65536.

The actual canonical Riesz-error upper is Ep/rho. This is the matching operator-residual attachment, not a generic inverse-conditioning estimate. All interval contractions retain signed centers; the radius uses the absolute ordered coefficients for a common conservative replay enclosure.

The targeted physical error squared uppers are approximately 3.766831272e-13 and 2.486149677e-10. They suffice for the added-control diagonal sign test. No claim is made that these controls' source errors are negligible.

## 2. Capture the existing source through degree below 64

The nominal original source is F=q+K_nom V. RC68 provides its complete signed physical norm entries, and RC83 provides its pairings against all physical Legendre modes n<64.

Contract those entries onto the fixed control before bounding. Write u and r_u for its nominal source-norm center and radius, h_n and r_n for its pairing centers and radii, and m_n=R/(2n+1) for physical mass. Subtract the fixed polynomial

    p = sum_(n<64) (h_n/m_n) P_n.

Its residual obeys

    ||F−p||² <= u − sum h_n²/m_n
                + r_u + sum 2|h_n|r_n/m_n = w.

The residual is computed using fixed center coefficients, so the pairing error enters linearly through -2<F,p>. A quadratic r_n² term is not needed for this particular polynomial-subtraction identity. The calculation retains original-source cancellation before taking its residual upper.

The physical source subtraction has degree count 64. The canonical projection being bounded has rank 1250. These are different objects and are kept distinct.

## 3. Direct rank-1250 transport

Because i* p belongs to H1250,

    P_E1250 i* F = P_E1250 i* (F−p).

RC95's canonical-complement embedding/adjoint norm upper tau1250, approximately 0.45112852565, gives

    N = tau1250² w

for the nominal projected source squared norm. One need not transport first through H64, and no rank-64 Weil complement floor is assumed.

For the actual-source attachment, RC89 supplies projected archimedean, prime and pole physical-to-canonical bounds at its reference rank 38. Each transfer term contains one complement embedding factor, so it scales by tau1250/tau38. Write k for the sum of those scaled bounds divided by sqrt(rho). Then

    E = rho(1+nu) k² Ep
        + (1+1/nu) delta_K² tau1250² t.

The second term pays the nominal-source approximation on the actual trial. The first pays the actual Riesz error through the original remainder. For any positive rational parameter s,

    Gamma1250(v,v) <= (1+s)N + (1+1/s)E = g(s).

A fixed rational grid chooses a usable upper. It is not a necessity statement about the actual covariance. The certificate also records N+E+2 sqrt_floor(N E), a lower for this fixed scalar-Young enclosure family, without interpreting it as actual leakage.

The nominal and transfer squared uppers are approximately:

| Source contribution | Even | Odd |
| --- | ---: | ---: |
| N | 6.118593129e-11 | 6.614503769e-9 |
| E | 9.267707888e-13 | 6.116788173e-10 |

## 4. Update the actual original head diagonal

RC97 reconstructed the signed original trial head on the same matching 64-mode trials. RC98 retains its diagonal center and paid trial radius, and attaches the targeted control Riesz-error upper.

Let source norm upper s_v=sqrt(u+r_u)+delta_K sqrt(t), and kappa be RC66's full physical original remainder norm in that parity. The actual original head interval is bounded by

    Q_lower = center − trial_radius − 2 sqrt(Ep) s_v
                         − kappa Ep − Ep/rho,
    Q_upper = center + trial_radius + 2 sqrt(Ep) s_v
                         + kappa Ep.

The canonical error keeps the cancellation sign on the diagonal. Outward rational square roots and 1e-40 endpoint rounding pay every attachment. The resulting d=Q_lower−g/alpha is positive in both parities. This is a certificate for the complete actual original source and its actual rank-1250 coupling, not a reference source.

## 5. Retain the certified pair and test the added cross terms

Let L be the already-certified corrected weak-pair lower: RC95 even and RC94 odd. Let G be the corresponding actual coupling covariance upper. Then the actual corrected three-mode matrix has block form

    [[B,c],[c*,d_actual]], B>=L, d_actual>=d.

The original head cross entries Q(w_i,v) retain their signed RC97 intervals. Positivity of the actual coupling covariance gives

    |Gamma1250(w_i,v)|²
      <= Gamma1250(w_i,w_i) Gamma1250(v,v)
      <= G_ii g.

Hence the corrected cross c_i=Q(w_i,v)−Gamma1250(w_i,v)/alpha lies in the interval obtained by enlarging the signed head interval by sqrt(G_ii g)/alpha on both sides.

This yields a rectangle for the two cross coordinates. For any fixed c, the lower block completion is positive precisely when

    d − c* L^(-1) c > 0.

The inverse quadratic is convex in c, so its maximum on the rectangle occurs at a vertex. Exact evaluation of all four vertices proves whether this robust sufficient condition passes.

It fails in both parities. The worst box penalties are about 16.72 and 2780.17 times the positive added diagonal margins. An explicit rational witness (-L^(-1)c,1) has quadratic value d−c*L^(-1)c in each worst vertex matrix; replay checks that identity independently using the two-by-two adjugate inverse.

Crucially, these vertices are matrices allowed by the rectangular relaxation. Their cross coordinates need not be jointly realizable by a coupling covariance satisfying every known Loewner constraint, much less by the original arithmetic operator. Negative values in these enclosure matrices are not negative values of the original Weil form. RC98 certifies failure of this robust box test and nothing stronger.

## 6. Next estimate

The control diagonal is now sufficient. The missing estimate is the signed corrected interaction of each added control with its weak pair. Bounding two source cross terms separately by Cauchy throws away their relationship to the weak-block inverse, especially in the very thin odd corrected block.

A next certificate should target the mixed source covariance or the combined inverse-weighted cross response. A common signed physical residual Gram for the three inputs, with compatible actual-source errors and the rank-1250 projection, is one candidate. A direct matrix source-tail theorem is another. The existing four-input RC95 jump-profile construction cannot simply be extended by asserting that the extra controls share its certified derivative entries.

No dense 1250-feature Weil-head evaluation is required by this six-mode test. Complete low-mode coverage and the later corrected strong/cross theorem remain separate obligations.

## Verification

Inputs: RC97, RC63, RC67, RC59, RC68, RC81, RC83, RC89, RC95, RC94 and RC66. Byte SHA-256 digests and the matching source, trial, residual, pairing, norm and transport crosslinks are checked.

Generation contracts ordered entries; independent algebra replay contracts symmetric triangles and column-first trial products, checks the adjugate inverse, and rechecks every exact directional margin and cross-box vertex. It reproduces the JSON exactly. Existing source integration certificates are inherited, not reintegrated. No machine-float positivity decision or Lean formalization is claimed.

- `scripts/validate_rpb108_rc98_six_mode_schur_completion.py`
- `certificates/rpb108_rc98_six_mode_schur_completion.json`
- `notes/RPB108_RC98_ADDED_CONTROLS_POSITIVE_AND_SIGNED_CROSS_GAP_20261011.md`

Full positivity, RH and Global/F4 remain open. Only the designated RC branch receives additive files.
