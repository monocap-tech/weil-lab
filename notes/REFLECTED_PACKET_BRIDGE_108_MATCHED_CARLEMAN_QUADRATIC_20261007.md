# RPB108: a lawful matched Carleman quadratic identity

Date: 2026-10-07 UTC. Recovered live head 99b8346b238abde76730d4fcdc5b86012fdb3e01.
Definitions: [matched quadratic identity](../docs/TERMINOLOGY_RPB108_MATCHED_CARLEMAN_QUADRATIC.md).
Category: critical derivative promotion / endpoint exclusion.
Publication recovery: GitHub writes recovered during this pass. The preceding absolute-collar result is now committed at 5efd53af7e3318d05f39218a6ff4dd9963d1e6b8, preserving the newer aperture head 200ba143265914d8fc6d03b81f14bc95a9232a20. This note is an analytic continuation with canonical cursor/source custody; no Lean certification is asserted.

## Exact result

For every actual h in K_a intersect Xcrit and sufficiently small delta>0,

    J_delta=(1/4)|C(delta)-M|^2
               -Re integral_0^delta (A_h(u)-A_h(0))
                                      conjugate(C'(u))du.       (1)

Here C is the full Carleman profile, M=2A_h(0) is its proved signed boundary limit, and J_delta uses the complete actual residual r=A_h-C/2. Both J_delta's underlying two-variable product and the drive-variation integral are absolutely integrable. This is a new lawful boundary calculation from the already assumed critical membership, not a new bound on the critical positive source moment or on h'.

Absolute inverse-moment convergence is not needed. In particular, the previously audited scalar inverse-moment observation is not made injective, and its older averaged quadratic formula is not imported without its own hypotheses. Equation (1) retains the full drive variation and the actual residual profile.

## 1. Absolute convergence before integration by parts

Fix a collar size delta0<exp(-4) on which the preceding absolute-collar estimate holds, and take 0<delta<=delta0. The pinned critical joint matching theorem gives the three finite Hardy budgets

    integral_0^delta0 |f(v)|^2 log(1/v)/v dv,
    integral_0^delta0 |r(u)|^2/[u log(1/u)]du,
    integral_0^delta0 |d(u)|^2/[u log(1/u)]du,

where d=A_h-A_h(0). Applying the same proved Schur kernel estimate, first with r and then with d, makes

    integral_0^delta integral_0^delta0
       (|r(u)|+|d(u)|)|f(v)|/(u+v)^2 dv du

finite. The weight constant remains 1+2 log 2; restricting u to the shorter collar only decreases the positive integrals.

For delta0<=v<=2a, the kernel is bounded by delta0^(-2), and f is L1 because it is supported L2. Each of r,d is L1 on (0,delta): Cauchy-Schwarz bounds that norm by its Hardy norm times sqrt(integral_0^delta u log(1/u)du). Thus the outer part is finite as well. These arguments justify the full absolute product defining J_delta and

    integral_0^delta |d(u) C'(u)|du<infinity.           (2)

They do not justify replacing r by A_h or by C/2 separately. The two Hardy budgets apply to the complete residual and the drive difference, respectively, not an arbitrary nonzero constant at the boundary.

## 2. Fixed-cutoff algebra followed by the signed limit

For every u>0, differentiation under the nonsingular Carleman integral is lawful and gives C'(u)=-integral f(v)/(u+v)^2 dv. On [epsilon,delta], ordinary calculus gives

    Re integral_epsilon^delta r(u)(-conjugate(C'(u)))du
       =(1/4)(|C(delta)|^2-|C(epsilon)|^2)
          -Re A0(conjugate(C(delta))-conjugate(C(epsilon)))
          -Re integral_epsilon^delta d(u) conjugate(C'(u))du.

The left side converges absolutely by section 1; the final integral does so by (2). The matching theorem supplies the ordinary, potentially conditionally obtained limit C(epsilon)->M=2A0. Taking the limit and completing the finite scalar square gives exactly (1):

    (1/4)(|C(delta)|^2-|M|^2)
       -(1/2)Re M(conjugate(C(delta))-conjugate(M))
        =(1/4)|C(delta)-M|^2.

Neither Re integral C conjugate(C') nor integral A0 conjugate(C') is asserted absolutely convergent down to zero. They are evaluated together through the fixed-cutoff identity and the independently proved ordinary boundary limit. Complex conjugations and the sign of the residual are retained.

## 3. Why this does not supply the missing native estimate

The exact native translation formula controls the triangular flux

    F_h(t)=Re integral_0^t r(u) conjugate(f(t-u))du,
    F_h(t)=-D_m(t)+(cosh(t/2)-1)Ppole(h).

J_delta instead integrates over 0<u<delta and 0<v<2a with weight (u+v)^(-2). Its domain contains a nontrivial region u+v>=delta. Thus one cannot apply the already proved upper bound F_h(t)<=O(t^2) to conclude J_delta<=0, discard the drive-variation term in (1), or deduce C(delta)=M. Even a bound on the signed triangular integral would not by itself establish the corresponding rectangular sign.

More fundamentally, (1) is a kinematic identity for any matched profiles with the three Hardy budgets. The earlier independently assigned constant-drive cusp has d=0 and J_delta=|C(delta)-M|^2/4; its native sign defect is separately audited. The refined comparison drive d(u)=-u^(1/4)log(1/u) also satisfies (1) with its nonzero drive correction, despite its physical derivative not being L2. Neither comparison has actual full-null/source custody.

The derivative gate therefore cannot be obtained by omitting the correction. A positive eigenmode, if it belongs to Xcrit and has the same matching, also permits this calculation after mass subtraction; the identity is not inherently exclusive to zero normalization. The available actual positive-eigenmode control still has its critical moment undecided.

## 4. What the external boundary literature supplies here

Theorem 1.1 of Hernandez-Santamaria, Lopez Rios and Saldana, arXiv:2401.18033v2 (3 July 2024), is read at https://arxiv.org/html/2401.18033v2 and https://arxiv.org/pdf/2401.18033. It supplies continuity and an inverse-square-root-log boundary upper bound for bounded weak solutions with bounded forcing. Its stated conclusion does not supply an L2 derivative or the homogeneous critical promotion theorem. The introduction also explains why the logarithmic operator has weak regularizing properties. No boundary-trace expansion or critical null-space classification is assumed from this result. This is a scope check of the already used external theorem, not a new external input or a claim that no stronger theorem exists elsewhere.

## Remaining theorem and standing

The exact remaining homogeneous obligation is h in actual K_a intersect Xcrit -> h' in global L2. The same physical h and its actual source/drive compatibility must supply that implication; a scalar square or the rectangular boundary formula alone cannot do so. Whole-contact-kernel critical membership is separately unproved. The alternative whole-contact-kernel finite-liminf order-3/2 signed trace remains a sufficient, unproved endpoint-exclusion target.

The accepted |beta_rho|<=3/8 input is retained. It bounds the transverse source remainder, not the drive correction in (1), the rectangular flux sign, or the missing whole-kernel critical moment. No new aperture is computed. Prescribed historical packet attachment, enlarged same-vector full-null transport, global unit domination, endpoint exclusion, Lean certification, RH, F4 and FULL TRANSPORT CLOSED are not claimed.

Validation is analytic for Schur/Tonelli absolute convergence, nonsingular differentiation, cutoff algebra and passage to the signed limit. Documentation and algebra checks have narrower scope. No numerical inverse, Lean build or axiom audit. The canonical cursor is updated additively after write recovery, preserving whole-domain positivity through 97/100 with Q>=9e-30 physical mass and Q>=4e-32 Elog; no aperture recomputation is made.

## Source custody

- CRITICAL_JOINT_MATCHING_20261007, blob 299cea4f1fe5b45b844c52a7912842f93d21dd9a at recovered live head: actual critical budgets and M=2A_h(0).
- EXACT_TRANSLATION_BOUNDARY_FLUX_20261005, blob 432ffd64d6460c65cee106f0b46afdb50d1ec28a: triangular native residual identity.
- SIGNED_CUTOFF_SOURCE_MOMENT_20261007, blob 52f34cc5c348c7ad5b00058c1208599f531bf4c7: endpoint target and whole-kernel quantifiers.
- CRITICAL_ABSOLUTE_COLLAR_20261007, blob 498a8ad4530bd2ed5c613746f4b1afc2780103a7 at commit 5efd53af7e3318d05f39218a6ff4dd9963d1e6b8: explicit Schur kernel bound and refined native-sign comparison. The original pre-publication local SHA256 is retained in the manifest as recovery history only; this published blob includes the newer aperture custody addendum.
