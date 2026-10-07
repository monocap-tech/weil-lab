# RPB108: unavoidable mixed logarithmic compensation in every bounded kernel gauge

2026-10-07. Recovered head c665b9d4bc55fed84ed4c2a2b38daf5fe9072d90. Definitions: [mixed height compensation](../docs/TERMINOLOGY_RPB108_MIXED_HEIGHT_COMPENSATION.md). Conditional on a hypothetical nonzero actual nonnegative contact kernel. Analytic, not Lean-certified.

## Result

The explicit actual-row interpolation does not separate the signed height problem into an innocuous finite correction and an energy part. For smooth compact v, put k=C_X v and e=R_X v. Then

    B_T(k,k)/log T -> eta |kappa_R(k)|^2,
    B_T(e,e)/log T -> eta |kappa_R(k)|^2,
    B_T(k,e)/log T -> -eta |kappa_R(k)|^2,       eta=2/pi. (1)

Whenever k has nonzero trace, BOTH diagonal contributions diverge positively and their mixed term cancels them in v=k+e. Such smooth v exist. The energy representative can therefore have a logarithmic source head even though its original input is smooth. Native orthogonality does not remove this mixed term.

More generally, no bounded projection onto the nonzero actual kernel can send every smooth compact input into its H1 part. Rough representatives are unavoidable in any continuous complementary gauge. These are source/regularity facts, not a new arithmetic exclusion estimate. The actual positive-eigenmode control has the same height compensation, with its unshifted mass residual retained.

## 1. Polarize the established actual kernel limit

The pinned ACTUAL_SHARP_LOG_LIMIT theorem gives S_h(T)/log T -> eta|kappa_R(h)|^2 for every h in K. Apply the complex polarization identity within finite-dimensional K. With the registered linear-first convention,

    B_T(h,k)/log T -> eta kappa_R(h) overline(kappa_R(k)). (2)

This uses only finite heads and four actual kernel vectors at a time. No weighted infinite source moment is assumed. All original actual zero-pair and multiplicity weights remain present.

## 2. A smooth core test has a finite absolute mixed first-height pairing

For v smooth and compactly supported in the open window, both v and its global derivative v' are canonical. The pinned actual derivative coupling gives p(v')=-i theta p(v)-beta n(v) and n(v')=-i theta n(v)-beta p(v). Their complete base source norms are finite, and beta is bounded. Hence both theta p(v) and theta n(v) are square summable, so

    sum_q theta_q^2 (|p_q(v)|^2+|n_q(v)|^2)<infinity.

The complete base source norm of every canonical h is finite. Cauchy-Schwarz therefore gives

    sum_q |theta_q| (|p_q(h)p_q(v)|+|n_q(h)n_q(v)|)<infinity.

Thus B_T(h,v) has a finite limit, and B_T(h,v)/log T ->0. The same is true for B_T(v,w) for any two smooth core tests. This step uses the original normalized actual source dictionary; arbitrary growing coordinate renormalizations are not introduced.

## 3. Exact mixed compensation after the actual-row split

The NF48 lift has k=C_X v in K and e=v-k. Sesquilinearity and (2) give, for every h in K,

    B_T(h,e)/log T -> -eta kappa_R(h) overline(kappa_R(k)). (3)

Expanding B_T(e,e)=B_T(v,v)-B_T(v,k)-B_T(k,v)+B_T(k,k) proves (1). On the space K plus the smooth core, the averaged endpoint trace is defined by linearity, with the smooth contribution zero. Thus kappa_R(e)=-kappa_R(k); no pointwise asymptotic or eigen equation for e is asserted.

The unweighted full-null equation still gives Q(h,e)=0 against all canonical e. Equations (1)-(3) show that this exact equation does NOT imply a bounded or sublogarithmic height-weighted mixed head. This is an actual conditional source theorem, not an artificial freely assigned packet control.

In particular, the finite correction C_X v is finite-dimensional in PHYSICAL space but has infinitely many original source observations. Its first-height contribution is order log T when its trace is nonzero. This does not contradict historical O(1) effects of deleting a fixed finite set of source coordinates. A finite-dimensional physical correction and a finite set of source coordinates are different operations.

## 4. Smooth row-cardinal tests and the complete finite block limit

The r distinct real evaluations v->F_v(x_i) map the smooth compact core onto C^r. Indeed, a linear dependence annihilating every test would make a finite sum of distinct exponentials identically zero on the open physical interval; differentiating at an interior point gives the invertible Vandermonde system. Nonzero coordinate normalizations are divided out as in NF48. Choose smooth v_i with F_vi(x_j)=delta_ij. Then C_X v_i=H_i and set e_i=v_i-H_i.

Let a_i=kappa_R(H_i), a nonzero vector by the terminal readout and the fact that {H_i} spans K. In the ordered family (H_1,...,H_r,e_1,...,e_r), the entire matrix of finite heads satisfies

    (B_T)/log T -> eta [[A,-A],[-A,A]],
    A_ij=a_i overline(a_j).                         (4)

This matrix has rank one and is positive semidefinite; its one nonzero eigenvalue is 2 eta sum_i |a_i|^2. Each original smooth vector v_i=H_i+e_i lies in its null directions. These claims concern the LIMIT of the signed finite-head matrix, not the sign of every finite head.

The family is physically independent. A relation would put a smooth core combination in K, whereas K intersect H^r={0} by the derivative-chain theorem; the smooth row-cardinal tests themselves are independent. At unshifted contact the native Gram has zero kernel blocks and energy block Q(v_i,v_j), which is strictly positive definite: a zero-energy smooth combination would be a nonzero member of K intersect H^r. Thus the height limit has nonzero mixed blocks even though the native Gram has none.

No actual x_i, v_i, matrix conditioning or numerical packet is computed here. The finite cardinal construction is non-effective and uses the already proved distinct-row existence. Equation (4) is exact analytic asymptotic custody, not a discretized actual source calculation.

## 5. No bounded kernel projection preserves core H1 regularity

Let P:D_a->K be any bounded projection onto K. Suppose P(v) were globally H1 for every smooth compact v. Then P(v) belongs to the proper closed subspace F_1=K intersect H1, whose dimension is r-1. Smooth compact tests are dense in D_a. Continuity of P and closedness of the finite-dimensional F_1 imply P(D_a) is contained in F_1. But P(D_a)=K, a contradiction.

Therefore some smooth v has k=P(v) outside H1 and nonzero terminal trace. For that input (1)-(3) apply with e=(I-P)v, because the argument needs only k in K, not the particular actual-row projection. This includes the physical orthogonal projection P_K from NF46. The projection and its complement remain bounded in the canonical logarithmic domain. No assertion that their restriction is bounded in the stronger global H1 norm is licensed.

The regularity obstruction follows from the actual kernel flag and core density. It does not establish that the actual kernel exists; if contact were excluded, the obstruction would disappear.

## 6. Shifted control and remaining arithmetic gate

Repeat the argument in the lowest positive actual eigenspace K^mu with Q_mu=Q-mu mass. Its established sharp limit and derivative flag give the same (1)-(4) and no regularity-preserving projection. The full original source equation on every pair of vectors in the family is

    <Gamma(f),J Gamma(g)>=Q_mu(f,g)+mu<f,g>_L2.

Its kernel/representative mixed block need not vanish in the ORIGINAL form: it is mu<H_i^mu,e_j^mu>_L2. Only the Q_mu mixed block is zero. The finite mass residual does not change the first-height logarithmic limits, and is not discarded from source custody.

The explicit interpolation lift is therefore useful for reconstruction but cannot by itself produce a height-weighted orthogonal splitting or regularize every input representative. The compensation is forced even for smooth inputs. No nonpositive sharp/log subsequence on the actual unshifted kernel is obtained. Signed arithmetic exclusion, endpoint exclusion, F4, full transport and Lean closure remain open. Whole-domain aperture-one positivity is preserved.

## Validation and provenance

Finite exact algebra checks validate the polarized rank-one block, cancellation on smooth sum directions, positive nonzero eigenvalue, and preservation of the shifted mass blocks. They do not compute actual zeros or certify analytic asymptotics, core density, derivative membership, or regularity. Those arguments above use pinned ACTUAL_ROW_INTERPOLATION, ACTUAL_SHARP_LOG_LIMIT, KERNEL_DERIVATIVE_CHAIN, CRITICAL_EIGENMODE_TARGET and POSITIVE_SOURCE_HEIGHT_MOMENT (complete actual source derivative custody); no new external theorem is imported. Definitions and cursor are additive, with historical certificates unchanged.
