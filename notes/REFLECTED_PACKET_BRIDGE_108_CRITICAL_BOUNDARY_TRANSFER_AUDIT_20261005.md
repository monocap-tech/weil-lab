# RPB108: critical boundary transfer audit

Status: local continuation and applicability audit; no endpoint exclusion, repository promotion, or Lean certification.
Pinned repository source: d17a74065324575654cd53ea394957dfa4961ebb.

## Definitions before use

The critical exterior Hardy integral of a vector supported in [-a,a] is

    J_a(h)=integral_(-a)^a |h(x)|^2 [1/(a-x)+1/(a+x)] dx.

The logarithmic boundary profile is b(t)=1/sqrt(log(1/t)) for 0<t<1/10. This is a comparison profile, not an asserted asymptotic of an actual zeta weak-null vector. The zero-extension critical seminorm is the Gagliardo integral integral_R integral_R |h(x)-h(y)|^2/|x-y|^2 dx dy, equivalent up to a positive normalization constant to the homogeneous H^(1/2) Fourier seminorm.

## A necessary condition for the proposed half derivative

For x in (-a,a), direct integration gives

    integral_(R minus [-a,a]) 1/|x-y|^2 dy
       =1/(a-x)+1/(a+x).

Since h is zero on the exterior, the two orientations of the cross-boundary part of its Gagliardo integral are exactly 2 J_a(h). Tonelli applies to the nonnegative integrand even if the integral is infinite. Thus a zero-extended h in H^(1/2)(R) necessarily has J_a(h)<infinity. This is only a necessary condition; the interior-interior seminorm must also be finite.

The recovered every-s theorem with s<1/2 does not assert this critical condition. Its constants diverge near s=1/2, so neither monotone convergence nor taking a limit in the family of bounds supplies it. The recovered R^(-1+o(1)) bounds likewise do not prove the missing boundary integral.

## Primary comparison evidence

Source: V. Hernandez-Santamaria, L. F. Lopez Rios, A. Saldana, Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian, arXiv:2401.18033v2, July 3 2024, https://arxiv.org/pdf/2401.18033 . Read Theorems 1.1 and 1.2 in the introduction, pages 2-3 of the PDF.

Theorem 1.1 bounds bounded weak Dirichlet solutions with bounded forcing by a constant times the square root of ell(distance), where ell(t)=1/abs(log(min(t,0.1))). Theorem 1.2 gives two-sided comparable decay for the torsion solution in a sufficiently small ball, including one-dimensional intervals. These theorems concern the logarithmic Laplacian with symbol 2 log|xi| and their stated domain and solution hypotheses.

In dimension one, the lower torsion estimate implies failure of the critical exterior Hardy condition, since

    integral_0^epsilon b(t)^2/t dt
       =integral_(log(1/epsilon))^infinity du/u=infinity.

Therefore a zero-order logarithmic Dirichlet equation with smooth bounded forcing does not generically yield zero-extension H^(1/2). This comparison does not contradict the repository's subcritical H^s results and does not prove that any actual zeta mode fails H^(1/2).

## Why this theorem cannot be imported into the actual null problem

The actual interior identity is

    P_a m0(D)h=P_a T_a h-P_a p_h,
    m0(xi)=Re psi(1/4+i*pi*xi)-log(pi).

The paper uses a different exact multiplier. Our existing symbol envelope is not a theorem transferring boundary asymptotics under that difference. Moreover the actual translated forcing T_a h is initially L2, and the recovered fractional results give H^s only for s<1/2, not L-infinity. The pole is smooth but this does not make the full right-hand side bounded. Positivity and comparison principles for the published problem are also not proved for the full actual prime-and-pole form. No Hopf lemma or nonzero boundary coefficient may be transferred without these missing inputs.

## Consequence for the cursor

The preceding local two-factor Gaussian argument remains valid as an analytic consequence of the pinned fractional bounds: it bounds the genuine signed action and fixed collar by R^(-1+o(1)) plus exponential errors. It does not control J_a(h), eliminate the logarithmic comparison profile, or produce exponential signed cancellation.

The next substantive boundary task is to derive an actual boundary relation from the exact quarter-line multiplier, translated prime terms, pole, and full mixed-null equation, and identify which actual term would force additional cancellation. An H^(1/2) target must be supported by a proof of the Hardy condition and the interior seminorm; it is not a compulsory intermediate step for an independent exclusion route.

Numerical aperture remains 81/100. Retained selected-witness attachment, global endpoint exclusion, F4, and FULL TRANSPORT CLOSED remain open. This audit establishes a transfer boundary, not a new RH-facing exclusion theorem. No claim of existence of a nonzero actual null vector is made.

## Verification

The Hardy identity is direct one-dimensional integration; divergence follows by u=log(1/t). The comparison theorem was checked in the primary PDF. Applicability to the actual operator was explicitly withheld. No numerical test certifies those universal mathematical claims.

## Repository custody addendum

This note was initially produced locally; its original status sentences above record that history. It is now included in the research-branch custody repair based on d17a74065324575654cd53ea394957dfa4961ebb. Repository custody supersedes the original unpromoted/local storage status only. The analytic derivation remains unverified in Lean and is not certified by the algebra controls. Definitions: docs/TERMINOLOGY_RPB108_BOUNDARY_CONTINUATION.md. Reproducible algebra controls: scripts/certify_native_boundary_continuation.py; certificate and repeat validation under notes/data/RPB108_BOUNDARY_CONTINUATION_*_20261005.json.
