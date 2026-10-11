# RPB108 RC102 — Six-response completion and the norm-transport boundary

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC101, commit `95ee5095e97e81e85a2df0f78f2652d08ea1ef6f`.
Aperture B=1.10. Actual sufficient canonical Riesz head H has rank 1250.

RC102 advances the remaining-head interface after the complete six-mode corrected certificate. It derives a common upper for the original strong responses from existing signed physical source data, then proves that transporting the Schur correction by the available operator norm cannot pass the resulting sufficient completion test, for any positive Young parameter. The failure is quantified for the current upper-enclosure architecture. It is not a negative direction of the original Weil operator, and does not rule out a different completion theorem or stronger estimates.

The next missing quantity is a common Gram bound for six combined corrected responses. A theorem on the remaining strong block is a separate obligation. The 1244 remaining coordinates do not thereby require dense pairwise evaluation.

## The actual object to complete

Let A_Q be the original canonical Weil operator. Write E=H orthogonal complement and let P_H,P_E be the actual canonical projections. The accepted floor is A_Q|E >= alpha I with alpha=247/2500. Define

    A_H=P_H A_Q P_H,
    B=P_H A_Q P_E,
    Gamma_H=B B*,
    T_alpha=A_H-Gamma_H/alpha.

T_alpha is a sufficient lower for the exact effective head A_H-B(A_Q|E)^(-1)B*. It is the lower used by RC100/101; replacing the complement resolvent by its scalar floor remains a sufficient strategy, not a logical requirement for all proofs.

Let W denote the six certified canonical vectors, represented by three vectors in each parity, and S=H orthogonal W. In each parity RC100/101 certify

    W* T_alpha W >= L > 0.

Suppose a structural theorem supplies D=T_alpha|S >= beta I for some beta>0. Define the three-input cross-response Gram in each parity

    U_actual = Gram(P_S T_alpha W).

For any common upper U >= U_actual, the condition

    beta L-U > 0

proves T_alpha>0 by matrix Schur completion. Together with the accepted E floor it proves positivity of the full original form at this aperture. This is the RC96 completion criterion applied to the now-certified six-dimensional span. It needs three correlated responses per parity and a strong-block theorem; it does not require all 1244 strong-basis cross rows.

The exact response capture identity is

    U_actual = W* T_alpha^2 W - B_W M_W^(-1) B_W,
    B_W=W* T_alpha W,    M_W=W*W.

Here B_W and M_W are the actual form compression and canonical metric, respectively. Their certified lower matrices cannot simply be squared in place of the actual compression. RC102 checks an explicit matrix-order counterexample: with L_0=diag(2,1) and B_0=[[3,1],[1,2]], B_0>=L_0>0, but B_0^2-L_0^2=[[6,5],[5,4]] has value -6 on (5,-6). This is an abstract algebraic control, not an arithmetic counterexample.

## A rigorous original-response upper without metric inversion

The original response alone is P_S A_Q W, rather than the corrected response P_S T_alpha W. RC102 supplies a common Gram upper for the former using RC68's signed source Gram and RC83's source/polynomial pairings.

For the three physical native target polynomials q_j, W_j=i* q_j. Let F_nom,j=q_j+K_nom V_j be the original nominal physical source on the matching unchanged RC67 Riesz trials. Set

    P_q = Gram(q),
    H_c = center of <q,F_nom>,
    Z = P_q^(-1) H_c.

P_q is a physical target Gram, not the actual canonical metric M_W. Its inverse is used only for a chosen physical least-squares subtraction. Because i* qZ=WZ and P_S W=0,

    P_S A_Q W = P_S i*(F_actual-qZ).

Thus any fixed subtraction Z is legitimate without reconstructing the unknown canonical projection onto W. The least-squares choice minimizes the nominal centered physical residual, but interval uncertainty is paid separately.

Let U_c,U_r be the contracted signed RC68 source Gram center/radius and H_r the contracted RC83 pairing radius. The nominal residual center is

    R_c = U_c-H_c* Z,

and a valid entry radius is

    R_r,ij = U_r,ij
             + sum_k [|Z_ki| H_r,kj + H_r,ki |Z_kj|].

Replay verifies this through the expanded identity U_c-H_c*Z-Z*H_c+Z*P_q Z. Weighted row inflation with scales (10000,100,1) in the even block and (8000,100,1) in the odd block produces a physical Gram upper R_upper. Outward Loewner rounding to a 10^-40 grid is paid by diagonal row allowances.

For the actual physical source error, use the already-certified three-input physical Riesz error Ep from RC100/101, the trial physical Gram T_trial, the complete physical remainder norm kappa from RC66, and RC68's approximation error delta_K. With nu=1/65536,

    E_phys = (1+nu) kappa^2 Ep
             +(1+1/nu) delta_K^2 T_trial.

This is also rounded upward in Loewner order. The global physical embedding bound rho=252/257 and a common Young inequality give

    Gram(P_S A_Q W) <= UA = 2 rho (R_upper+E_phys).

All signed contractions are performed before matrix inflation. There are no new integrations and no reconstruction of a strong canonical basis. The fixed polynomial subtraction kills only W; it is not confused with the separate projection onto E used for the RC101 source coupling certificate.

## Why the generic correction transport fails

The identity part of A_Q has no H/E cross term. Therefore B=P_H i* K i P_E. With the global embedding factor rho, the rank-1250 complement embedding norm tau1250 from RC95 and the complete parity-specific physical K norm kappa from RC66,

    ||B||^2 <= g = rho tau1250^2 kappa^2.

Since Gamma_H=B B* is positive and Gamma_H<=g I,

    Gamma_H^2 <= g Gamma_H.

RC100/101's common source upper G bounds Gamma_W=W*Gamma_H W. Orthogonal projection then gives

    Gram(P_S Gamma_H W) <= g Gamma_W <= g G.

Consequently the following is a valid sufficient upper for the corrected strong response for every t>0:

    U_norm(t) = (1+t) UA + (1+1/t) V,
    V = g G/alpha^2.

This retains each input Gram's mixed entries, but loses correlations between the original and correction response terms. Those correlations are different from the head/leakage alignment already certified at RC101.

There is an upper limit on a feasible strong floor for this route. Because T_alpha<=A_H and ||A_Q||<=1+rho kappa,

    D<=beta_max I,    beta_max=1+rho kappa.

If D>=beta I on the nonzero remaining strong space, necessarily beta<=beta_max. This statement needs no assumption that D is positive.

For every t>0, U_norm(t)>=V. RC102 proves V_ii>beta_max L_ii on all three axes in each parity. Hence beta L-U_norm(t) has a strictly negative coordinate quadratic whenever beta<=beta_max. No positive Young parameter can make this current norm-transport upper pass the completion criterion, even if the entire original-response UA term were hypothetically removed.

Approximate displays of certified quantities:

| Parity | g | beta_max | Largest axis V_ii/L_ii | Ratio to beta_max |
| --- | ---: | ---: | ---: | ---: |
| Even | 47.35436413 | 16.10474592 | 1130.783531, weak_0 axis | 70.21430431 |
| Odd | 24.16596524 | 11.79034903 | 173.1359913, weak_1 axis | 14.68455182 |

An independent trace obstruction is also certified:

    trace(L_even^(-1) V_even) >= 2695.8896404516,
    trace(L_odd^(-1) V_odd) >= 372.3128381057.

These exceed 3 beta_max in their respective blocks, so V cannot be bounded by beta_max L. Lower scalar budgets and negative-margin upper enclosures are rounded outward with exact rational inequalities. The table is display only; acceptance and rejection use exact Fractions.

This establishes a boundary of this particular upper-enclosure architecture with the inherited g and G. It does not prove that actual corrected cross leakage is large, that a stronger g or G is impossible, or that the full original form is nonpositive. In particular, treating a lower bound on U_norm as a lower bound on U_actual would be invalid.

## What additional structure can replace the norm transport

The combined corrected response has the exact identity

    P_S T_alpha W
      = P_S A_Q(W-alpha^(-1)P_E A_Q W).

Its common Gram retains both the signed cross correlation of the original and correction responses and the projection onto S. Bounding the two terms separately and optimizing a Young parameter cannot recover those lost correlations.

One sufficient next target is a rigorous upper U_joint for these six combined responses with beta L-U_joint>0, together with an independent positive strong-block floor beta. Equivalent source-resolved bounds on P_S Gamma_H W and its mixed Gram with P_S A_Q W can serve the same purpose. The present weak source covariance G records only the first projected response P_E A_Q W, and does not provide that mixed information.

An abstract near-sharp control explains the loss in the generic positive-covariance step. For t=1/1000 let v=(2t/(1+t^2),(1-t^2)/(1+t^2)) and Gamma=v v*. It is an exact rank-one positive contraction with Gamma^2=Gamma. For W=e_0, its strong response squared is gamma(1-gamma), where gamma=Gamma_00, whereas the norm envelope g gamma is gamma with g=1. Their ratio exceeds 0.99999. Generic contraction and small weak compression alone therefore allow essentially the whole norm envelope. This is not the original operator and does not impose its joint arithmetic source constraints; those additional correlations are precisely a possible route to a stronger theorem.

This combined-response route is one sufficient strategy. A tighter complement resolvent, spectral exclusion, direct arithmetic factorization or first-contact exclusion may replace it. RC102 does not make a separate 1.10 certificate logically mandatory for Global/F4.

## Verification and scope

The ten direct inputs are RC101, RC100, RC95, RC63, RC67, RC59, RC68, RC83, RC66 and RC96. Their byte digests and predecessor/source/trial crosslinks are checked. The full six-mode certificate, original common G, corrected L and parity orthogonality are retained exactly; the nonpositive spectral-dimension upper remains 1244.

Generation uses exact inverses and centered least-squares identities. Independent replay uses explicit three-dimensional adjugate inverses, reordered signed contractions and expanded residual Grams. It recomputes all exact budgets and requires equality with the saved certificate. Positive correlated 3+1 Schur controls, a boundary null control with a nonidentity illustrative canonical metric, the squared-order counterexample and the near-sharp positive-contraction control are checked independently. All illustrative controls are labeled abstract, not original arithmetic certificates.

The original strong-response and generic corrected-response Gram uppers are certified. A sufficient corrected cross budget, the strong block, complete weak-mode coverage, full-head positivity, whole-aperture positivity, Global/F4 and RH remain uncertified. This is an internal rational certificate with analytic operator lemmas, not a Lean formalization.

- `scripts/validate_rpb108_rc102_six_response_completion_boundary.py`
- `certificates/rpb108_rc102_six_response_completion_boundary.json`
- `notes/RPB108_RC102_SIX_RESPONSE_COMPLETION_AND_NORM_TRANSPORT_BOUNDARY_20261011.md`
