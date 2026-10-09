# CC57: form convergence does not certify the physical residual estimator

Read [terminology](../docs/TERMINOLOGY_RPB108_RESIDUAL_GRAPH_GAP_CC57.md) first. This is an exact abstract inference control for the proposed NF20/NF21 estimator, not a counterexample to the original Weil arithmetic.

## Result and native scope

NF20 establishes form density and qualitative convergence of the true eliminated response on the finite retained carrier. Its physical-source representation also makes the finite polynomial residual estimator well-defined. These facts alone do not guarantee that the estimator becomes small when native trial spaces are enlarged. Coercivity, compact resolvent, a physical L2 source, nested form-dense trial spaces in Dom(C), and a positive complete Schur complement all hold in the following example, while the physical residual diverges. Native Legendre graph instability is neither asserted nor proved.

The actual NF21 two-mode residual Gram remains unevaluated at source branch head 44b22630d0211b5204284407fe16e45a24151843. Evaluating that Gram remains a valid finite test and can succeed without proving convergence of the whole trial sequence. CC56's qualitative full-source injection remains intact.

## Exact infinite control

On the physical Hilbert space direct sum of two-dimensional blocks with basis e_j,f_j, let

    C_j = [[j, j^3], [j^3, 2j^5]],  g_j=(j^-2,0),  j>=1.

Use the selfadjoint direct-sum operator domain. C_j>(j/3)I since its shifted first diagonal is 2j/3 and its shifted determinant is j^6/3-2j^2/9 >= j^2/9>0. Therefore C>1/3>207/1000 and has compact resolvent. The source is physical: ||g||²=sum j^-4<4/3. Its inverse is

    W_j=(2j^-3,-j^-5),  C_j W_j=g_j,
    G=<g,C^-1g>=2 sum j^-5<5/2.

W belongs to Dom(C). With retained scalar A=3, the full Schur complement A-G>1/2, so the complete block form is positive.

Take H_m=span{e_j:j<=m}+span{f_j:j<=floor(m/2)} and k=floor(m/2). These spaces are nested, lie in Dom(C), and their union is even graph dense, by direct-sum truncation. The exact form Galerkin projection equals W_j for j<=k, (j^-3,0) for k<j<=m, and zero otherwise. For each pending block,

    W_j-Y_{m,j}=(j^-3,-j^-5),
    C_j(W_j-Y_{m,j})=(0,-1).

Consequently

    T_m=sum_{k<j<=m} j^-5 + 2 sum_{j>m} j^-5 < 1/(2k^4)  (k>=1),
    P_m=(m-k)+sum_{j>m} j^-4.

Thus T_m tends to zero, G_m increases to G, but P_m tends to infinity. For every m>=1, P_m>1>(207/1000)*3 >= (207/1000)(A-G_m). The sufficient physical residual gate fails at every stage despite strict complete positivity. The valid estimate T_m<=P_m/kappa remains valid; it simply provides no useful upper bound here.

## Genuine crossing and positive-level controls

Keeping the same high operator, source and trial spaces, replace A by G+epsilon. The complete Schur complement is exactly epsilon. At epsilon=0 the actual model null is (1,-W), in the block operator domain. Positive, zero and negative epsilon give a genuine crossing. The validator checks the finite exact counterparts for 1,2,8,32 blocks at epsilon=1/100,0,-1/100: twelve controls.

For a genuine positive eigenlevel use C=[[1,1],[1,2]], g=(1,0), w_mu=(C-mu I)^-1g and A_mu=mu+<g,w_mu>. The original 3 by 3 block Q has eigenvector h=(1,-w_mu) with Qh=mu h. For mu=10^-40,1/100,1/20 the shifted high block remains above kappa=207/1000, and Q-mu I is positive semidefinite by its exact zero Schur complement. Thus mu is a positive ground eigenlevel and Q(h)=mu||h||²>0. Shifting the retained diagonal alone misses the null because A_mu-mu-<g,C^-1g>>0. All three levels are checked rationally.

These controls prevent confusion between residual convergence, complete positivity, an original null, and a positive-level shifted null. They are not actual native Weil crossings.

## What is now required

For a fixed original finite polynomial source, physical L2 representability puts W in Dom(C_F). Form convergence alone still cannot control ||C_F(W-Y_m)||. One sufficient route is graph density of the actual trial union and a uniform graph-norm bound on its C_F-form projections. For v in an earlier trial space, Pi_m v=v; approximating W in graph norm then gives

    ||W-Pi_m W||_graph <= (1+sup_m||Pi_m||_graph)||W-v||_graph ->0.

Alternatively, directly enclose the finite residual Gram or estimate the residual in the C_F-dual norm. Spectral trial projections commuting with C_F also give physical residual convergence, but no identification with the native Legendre trial spaces is supplied. None of these qualitative routes gives a computable rate or constants uniform over aperture caps or critical defects without further arithmetic estimates.

The immediate native sufficient estimate remains P_2 < (207/1000)(A-G_2), with all original prime, archimedean and pole contributions and interval errors paid. A sharper source-aligned C_F-dual estimate can replace it. The minimal exact positivity gate is T_rest < A-G_2; a margin theta A requires T_rest <= A-G_2-theta A. The physical Gram gate is a sufficient majorant, not an equivalent requirement or a lower frame assertion.

No all-cap defect-relative lower frame, quantitative leakage theorem, original critical-space alignment, target 53/50 complete positivity, actual contact exclusion, RH/F4 or Lean theorem is certified. The established whole-aperture positivity anchor remains 21/20. No paused endpoint-regularity or prime-smearing route is restarted.

## Validation

[Exact validator](../scripts/validate_native_residual_graph_gap_cc57.py) and [output](data/RPB108_RESIDUAL_GRAPH_GAP_CC57_VALIDATION_20261009.json): 64 rational block identities/coercivity checks, ten trial-stage checks, twelve finite genuine crossing controls and three positive eigenlevel controls pass. Infinite convergence/divergence follows from the displayed summation bounds; finite tests do not substitute for that proof. [Custody](data/RPB108_RESIDUAL_GRAPH_GAP_CC57_CUSTODY_20261009.json) records the parent and artifact hashes.
