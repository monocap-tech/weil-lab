# RPB108: finite actual selection realizes the effective positive synthesis

Base: research e9ac044dec970e2ef032ac1d99b5ee2c2e04bc02.
Definitions: docs/TERMINOLOGY_RPB108_FINITE_SELECTION_REALIZATION.md.

## Result

Fix an actual window a where the full native form is nonnegative. Let H=D_a, A its bounded logarithmic Riesz operator, and K=ker A. The complete normalized actual positive and negative analyses are denoted P_0 and N_0, so
\[
A=P_0^*P_0-N_0^*N_0.
\tag{1}
\]
The established actual positive-carrier theorem makes P_0:H->H_+=Ran P_0 a bounded isomorphism onto a closed range.

There exists a finite selection s of actual negative divisor coordinates such that R=Pi_s N_0 is injective on K. For any such selection the effective background covariance
\[
G_s=A+R^*R=P_0^*P_0-B^*B,\qquad B=(I-\Pi_s)N_0
\tag{2}
\]
is strictly coercive. The actual WD-T10 effective positive synthesis S:H_+->H is then a bounded isomorphism. The selected compensator is concretely
\[
C=-S^{-1}R^*,\qquad N_s=R^*=-SC,
\tag{3}
\]
and
\[
SS^*=G_s,\qquad SS^*-N_sN_s^*=A,\qquad \|C\|\le1.
\tag{4}
\]
No abstract synthesis-identification or Douglas-range premise is supplied: the maps are constructed from the attached actual full analyses.

For every h in K, put u=-Rh and a_+=S^*h. Then
\[
Cu=a_+=S^*h,\qquad C^*Cu=u,\qquad
(SS^*-N_sN_s^*)h=0.
\tag{5}
\]
If h!=0 then u!=0. These are the same-vector unitGain, physicalAdjoint, and physicalNull equations used by WD-T38.

This constructs an actual realization from an actual nonnegative-window kernel, if that kernel is nonzero. It does not recover a historical retained k, prove an actual endpoint exists, identify the historical fixed packet with s, or instantiate the entire WD-T38 morphology.

## Finite actual coordinates separate the kernel

The actual operator A=I+compact has finite-dimensional kernel. On K, (1) gives
\[
\|N_0k\|=\|P_0k\|\ge\eta_a\|k\|,
\tag{6}
\]
where eta_a>0 is the previously derived fixed-window positive-analysis lower bound. Thus the complete actual negative analysis is injective on K.

Finite coordinate projections converge strongly to the identity on the actual divisor-copy l2 space. Restricted to N_0(K), a finite-dimensional space, this convergence is uniform on the unit sphere. Choose finite s so that
\[
\|(I-\Pi_s)N_0|_K\|<\eta_a/2.
\]
Then ||Rk||>=eta_a||k||/2. This proves existence of a lawful finite selection, rather than adding kernel-observability as an unexplained hypothesis.

Equal-ordinate multiplicity copies retain their actual energy weights but do not create independent rows. Selection must have actual analysis rank at least dim K on K; cardinality alone is insufficient. No numerical basis or explicit list of actual selected ordinates has been obtained.

For a prescribed historical selection, injectivity of R|K is an independent obligation. The existential finite selection is not silently substituted for that packet.

## Exact coercivity criterion and estimate

Since A>=0,
\[
\ker G_s=\ker A\cap\ker R.
\tag{7}
\]
Indeed <h,G_s h>=<h,A h>+||Rh||^2; vanishing implies both A h=0 and Rh=0. G_s is I+compact because A is and R has finite rank. Therefore G_s is coercive exactly when R|K is injective.

For a quantitative fixed-window estimate, suppose K!=0. Write h=k+v with v perpendicular to K. Nonnegativity and Fredholm structure give
\[
\langle v,Av\rangle\ge\delta\|v\|^2,\quad\delta>0.
\]
Let gamma>0 satisfy ||Rk||>=gamma||k|| on K, and M=||R||. Then
\[
\|h\|\le
\frac{1+M/\gamma}{\sqrt\delta}\sqrt{\langle h,Ah\rangle}
+\frac1\gamma\|Rh\|.
\]
Cauchy-Schwarz yields
\[
\langle h,G_s h\rangle\ge c_s\|h\|^2,\quad
c_s=\left[\frac{(1+M/\gamma)^2}{\delta}+\gamma^{-2}\right]^{-1}>0.
\tag{8}
\]
These constants are derived on H, not on unrestricted physical L2. If K=0, A itself is coercive; the empty selection suffices and has no nonzero unit-gain vector.

## Constructing the actual WD-T10 maps on the positive carrier

Define T_B=B P_0^{-1}:H_+->background coefficients. Actual full nonnegativity gives
\[
\|Bh\|\le\|N_0h\|\le\|P_0h\|,
\]
so T_B is a contraction. Let
\[
X_B=-T_B^*,\quad
E=I_{H_+}-X_BX_B^*=I_{H_+}-T_B^*T_B.
\]
Then B^*=-P_0^*X_B. The square-root synthesis is exactly the WD-T10 construction:
\[
S=P_0^*E^{1/2}.
\tag{9}
\]
The existing residual-budget theorem gives
\[
SS^*=P_0^*E P_0
=P_0^*P_0-B^*B=G_s.
\tag{10}
\]
Every adjoint uses the logarithmic Hilbert space H and actual coefficient Hilbert norms. No unbounded physical L2 operator is inferred.

Coercivity (8) also gives E coercive. For z=P_0h,
\[
\langle z,Ez\rangle=\langle h,G_s h\rangle
\ge\frac{c_s}{\|P_0\|^2}\|z\|^2.
\]
Thus E^{1/2} is boundedly invertible. P_0 is a bounded isomorphism onto H_+, hence P_0^* is a bounded isomorphism from H_+ to H. Equation (9) proves S is invertible, not merely surjective. Formula (3) now constructs the unique compensator with the actual selected synthesis N_s=R^*.

The positive coefficient space is the actual closed positive-analysis range H_+, not the raw Green synthesis quotient. The physical vector is the unchanged h in H, and its physical L2 realization is the already attached inclusion J_a h. This construction does not place h in the H1 raw Green synthesis range.

## Contractivity and exact endpoint coefficient custody

Using (3)-(4),
\[
A=S(I-CC^*)S^*.
\tag{11}
\]
Because S is invertible and A>=0, I-CC^*>=0, so ||C||<=1. This is a derived actual selected compensator contraction at the named nonnegative window.

For h in K, A h=0 and (2) imply R^*Rh=G_s h=SS^*h. Consequently
\[
C(-Rh)=S^{-1}R^*Rh=S^*h.
\]
Also C^*=-R(S^{-1})^*, giving
\[
C^*C(-Rh)=-R(S^{-1})^*S^*h=-Rh.
\]
This proves (5), including both signs. Since R|K is injective, h!=0 gives u=-Rh!=0 and a_+=S^*h!=0. Unit gain gives ||a_+||=||u||. Scaling h by 1/(sqrt(2)||u||) makes the coefficient pair (a_+,u) have direct-sum norm one and each squared norm one half, as in the attained-neutral output.

Conversely, a nonzero u satisfying C^*Cu=u determines
\[
h=(S^*)^{-1}Cu.
\]
Then Rh=-u and (11) gives A h=0. Thus the unit-gain space ker(I-C^*C) and K are isomorphic, with h->-Rh and the displayed inverse. This derives the endpoint coefficient dictionary; it is not the selection of a critical subsequence.

Importantly, such an h is null for the full defect A, while
\[
G_s h=R^*Rh,\qquad Q_{{\rm bg},s}(h)=\|Rh\|^2>0.
\]
It is not weak-null for the effective-background form G_s. The earlier finite-selected forcing obstruction concerns G_s-nullity and is consistent with this full-native realization. Subtracting the selected covariance after background elimination is essential.

## What the certified short windows imply

Where actual A is strictly positive, every finite selection yields coercive G_s and the construction still works, but it has no nonzero unit-gain vector. If A>=delta I, then (11) gives
\[
I-CC^*\ge\frac{\delta}{\|S\|^2}I,\qquad
\|C\|^2\le1-\frac{\delta}{\|S\|^2}<1.
\]
Thus the certified positivity range through 81/100 cannot provide an attained-neutral WD-T38 instance through these actual maps. No actual null vector is constructed there.

For a hypothetical nonnegative endpoint with kernel, finite selection gives the realization above. It does not provide a uniform selection, constants across windows, the historical fixed-packet monotone carrier A(t), a critical sequence, or enlarged same-vector null transport. Those must not be inferred from a fixed-window construction.

## Retained attachment standing

The pinned source scan recovered the generic retained equations and no concrete actual-zeta constructor application. This pass supplies a lawful actual effective-positive realization at a nonnegative window, and an exact finite-selection criterion for its bounded inverse. It supplies no identification of the pre-existing retained P,C,k with these maps and vectors.

The next attachment issue is precise: recover the historical physical realization and fixed selection, prove its agreement with the actual full analyses and this background reduction, and prove selection injectivity on the relevant kernel if an inverse is needed. Alternatively an independently constructed actual first-contact kernel can use this realization, with its own sequence and selection custody. Neither option creates enlarged central cancellation.

Once a full actual null vector is attached, the L2 domain-promotion and derivative constraints already apply. No new H1 regularity follows from S^{-1}; it is a bounded inverse on D_a.

## Validation

Analytic proof from actual full-domain sampling, the positive closed-range isomorphism, nonnegative Fredholm structure, finite coordinate approximation on a finite-dimensional subspace, and the existing WD-T10 square-root covariance identity. The coercivity estimate, both compensator signs, all adjoint equations, and both directions of the kernel/unit-gain dictionary are explicit.

Primary repository sources read at the base commit:
- POSITIVE_CARRIER_EQUIVALENCE_20261004.
- RETAINED_UNIT_GAIN_CUSTODY_20261004 and RETAINED_SOURCE_RECOVERY_20261003.
- ACTUAL_SELECTED_BACKGROUND_20261004 and FINITE_SELECTED_FORCING_OBSTRUCTION_20261004.
- WeilDefect/Screening/ResidualBudget.lean and CarrierFactorization.lean.
- WeilDefect/Morphology/Neutral.lean.

This pass is not Lean certified. No Lean or workflow edits, new CI result, actual endpoint existence, historical retained attachment, selected packet identification, global positivity or RH conclusion. Historical notes unchanged. F4 and FULL TRANSPORT CLOSED remain open.
