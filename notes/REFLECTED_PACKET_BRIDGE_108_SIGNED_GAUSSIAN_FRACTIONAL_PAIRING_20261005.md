# RPB108: signed Gaussian upper bound from two fractional factors

Status: local analytic continuation, not promoted or Lean verified.
Source snapshot: d17a74065324575654cd53ea394957dfa4961ebb.

## Definitions registered before use

Fix an aperture a>0 and an actual full mixed weak-null vector h in D_a, extended by zero. Let H=||h||_2, r(xi)=1+|xi|, beta_R(xi)=exp(-(2*pi*xi-R)^2/R), x_R=1+R/(4*pi), and g_R=K_R*h with the unchanged project Gaussian. L_h is the frozen multiplier core (m0(D)-T_a)h; it excludes the exponentially growing physical pole. A_R is the genuine full action A_a(h;conjugate(g_R)). C_R is the compact collar action for fixed cutoffs in the recovered far-field note. None of these definitions asserts that h is nonzero or exists.

Use the recovered fractional-null constants C_s and G_s, so for each 0<s<1/2:

    ||h||_(Y_s)<=C_s H,  ||L_h||_(Y_s)<=G_s H.

The recovered boundary-domain theorem gives ||L_h||_2<=B_a H, B_a=4+S_a+4a exp(a). Put Ppole_a=4a exp(a). These bounds include the full frozen prime set and actual pole moments.

## A direct bound for the genuine signed action

Split frequencies into J_R={|2*pi*xi-R|<=R/2} and its complement. On J_R, r>=x_R, so weighted Cauchy-Schwarz gives

    |integral_(J_R) beta_R Fourier(L_h) conjugate(Fourier(h))|
       <=x_R^(-2s) G_s C_s H^2.

On the complement beta_R<=exp(-R/4). Ordinary Cauchy-Schwarz gives a bound B_a exp(-R/4) H^2. This split avoids multiplying the off-band error by the large fractional constants.

The recovered exact Gaussian pole identity separately bounds the pole action by Ppole_a exp(-R+1/(4R)) H^2. Therefore, for R>=1,

    |A_R| <=[G_s C_s x_R^(-2s)
              +B_a exp(-R/4)
              +Ppole_a exp(-R+1/(4R))] H^2.                 (1)

This is an absolute bound, hence also a real-part upper bound. It concerns the genuine whole-line test; no endpoint-domain membership of g_R is asserted. The improvement over the earlier L2 bound B_a H sqrt(M_R) comes from retaining both weighted factors.

## Explicit approach to exponent one

Use the recovered optimization constants c_a,g_a,E_a,K_a with K_a=2E_a+3. For d=1-2s,

    C_s<=c_a exp(E_a/d^2),
    G_s<=g_a exp((E_a+1)/d^2),
    G_s C_s<=g_a c_a exp(K_a/d^2).

For log x_R>=8K_a choose d=(K_a/log x_R)^(1/3). The recovered balance identity yields

    |A_R| <=[g_a c_a x_R^(-1)
               exp(2 K_a^(1/3)(log x_R)^(2/3))
              +B_a exp(-R/4)
              +Ppole_a exp(-R+1/(4R))] H^2.                (2)

Thus the genuine signed interaction has an explicit R^(-1+o(1)) upper bound at fixed a, conditional on full mixed weak-nullity. It is not an exponential bound.

## Transfer to the genuine fixed collar

The recovered same-vector identity is A_R=C_R+F_R, and

    |F_R|<=Cfar_a,b R^(3/2) exp(-R b^2/64) Elog(h)

for a fixed positive exterior separation b and fixed admissible cutoffs. The recovered logarithmic multiplier envelope |m_a-w|<=C_a and multiplier-domain bound give

    Elog(h)<=||w Fourier(h)||_2 H<=(B_a+C_a)H^2.

Consequently (1) and (2) are also bounds for |C_R| after adding

    Cfar_a,b (B_a+C_a) R^(3/2) exp(-R b^2/64) H^2.

No cutoff derivative uniformity as b tends to zero is claimed.

## Boundary of the result

This derives a signed-action upper bound, not signed cancellation. The correction factor grows and does not give exact O(1/R), H^(1/2), a boundary trace, or exponential Fourier mass decay. The polynomial/subpolynomial upper bound is compatible with the recovered collar coercivity lower bound and does not contradict nonzero compact support. It neither excludes a first positivity endpoint nor identifies a retained selected witness with an actual full weak-null vector.

The independent next issue remains an endpoint-specific constraint that supplies cancellation or another exclusion mechanism. Numerical aperture stays 81/100. F4 and FULL TRANSPORT CLOSED remain open. No repository push, Lean mutation or CI run is made by this local continuation.

## Source custody and verification

Inputs are the recovered FRACTIONAL_NULL_REGULARITY, FRACTIONAL_OPTIMIZATION, ENDPOINT_BOUNDARY_REGULARITY, ACTUAL_MOVING_GAUSSIAN_COERCIVITY and GAUSSIAN_FAR_FIELD_BOUNDARY_COLLAR notes at the pinned snapshot. The fractional optimization certificate was reproduced byte for byte in the recovery turn. The new derivation uses weighted Cauchy-Schwarz, the exact frequency split, the recovered pole identity and the already checked optimization balance. It is an analytic derivation; the source certificate does not mechanically certify this theorem.

## Repository custody addendum

This note was initially produced locally; its original status sentences above record that history. It is now included in the research-branch custody repair based on d17a74065324575654cd53ea394957dfa4961ebb. Repository custody supersedes the original unpromoted/local storage status only. The analytic derivation remains unverified in Lean and is not certified by the algebra controls. Definitions: docs/TERMINOLOGY_RPB108_BOUNDARY_CONTINUATION.md. Reproducible algebra controls: scripts/certify_native_boundary_continuation.py; certificate and repeat validation under notes/data/RPB108_BOUNDARY_CONTINUATION_*_20261005.json.
