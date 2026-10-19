# SM58 — Original complete 25-source coupled negative-frequency Fourier upper

**October 19, 2026 · original W-ODD-NEG OPEN · stacked on SM57 draft PR #240.**

## Motivation and exact acceptance obligation

The earlier verified SM51–SM56 results provide positivity on a genuinely physical two-source trial span and progressively better signed lower matrices on a physical three-source span. They **do not** certify the complete original odd negative index or its orthogonal remainder. SM57 started the missing 25-dimensional carrier step, using SI10's exhaustive 973 whole-real negative-frequency leaves and SM43 full real-frequency source amplitudes. Its first Actions 39273770072 stopped at a one-sided/two-sided leaf-width assertion (now corrected); its succeeding full-25-source verification must pass independently. The SM57 negative UPPER is a sourcewise Cauchy **diagonal**, correct but likely excessively expensive because it discards all Fourier correlations.

SM58 builds a **complete 25×25 source-coupled original negative UPPER** using the exact original SI10 16 sine, eight \(x\cos\), and genuine sinh-pole physically supported odd input functions, not just the three sources with the better SM56 signed bound.

## A complete, correctly directed Fourier covariance UPPER

For any original whole-real dyadic negative-cover leaf \(I=[a,b]\) from SI10, take its certified original multiplier upper \(0\le(\kappa-m(\xi))_+\le h_I+\kappa\), valid **at every real frequency** \(\xi\in I\), and round that scalar *upward* before use. Original SI10 certifies there are precisely 973 leaves/107 connected clusters covering all possible negative weight; outside them the multiplier is zero, including the sign-safe high-frequency region.

For all 25 original supported source transforms \(T_i(\xi)\), at \(c=(a+b)/2\), \(r=(b-a)/2\), reconstruct original SM42 analytic Fourier intervals, original SM46 exact first/second frequency derivative intervals, genuine sinh-pole Fourier formulas, and rigorous original supported third-spatial-moment bounds. Let \(v_i,d_i\) be rational midpoints with outward errors \(e_i^{(0)},e_i^{(1)}\) and original global/local curvature \(K_i\). For every real \(\xi\in I\),
\[
T_i(\xi)=v_i+d_i(\xi-c)+\rho_i(\xi),
\qquad |\rho_i(\xi)|\le R_i:=e_i^{(0)}+e_i^{(1)}r+K_ir^2/2.
\]
Every \(R_i\) is rounded upward. Set
\[
V^2:=\sum_{i=0}^{24}(v_i^2+r^2d_i^2/3),\quad
R^2:=\sum_{i=0}^{24}R_i^2,\quad
\epsilon_I:=\operatorname{ceil}_{10^{-9}}\bigl(2\sqrt{V^2R^2}+R^2\bigr).
\]
By the symmetric-interval identity \(\int_I(\xi-c)d\xi=0\), the true complete 25×25 Fourier covariance obeys, **in Loewner order for every original mixed-source coefficient vector**,
\[
\int_I T(\xi)T(\xi)^\top\,d\xi
\preceq |I|\bigl(vv^\top+(r^2/3)dd^\top+\epsilon_I I_{25}\bigr).
\]
The Cauchy estimate on the remainder justifies the *matrix*, not merely its diagonal entries. Thus
\[
\boxed{
K_{\rm neg,25}\preceq U_{58}:=
2\sum_{I\in\mathrm{SI10}_{973}}
 |I|\widehat{(h_I+\kappa)}
 \left(v_Iv_I^\top+\tfrac{r_I^2}{3}d_Id_I^\top+\epsilon_I I_{25}\right).
}
\tag{SM58-U}
\]
All 625 physical cross entries, including the true sinh pole input, are retained. Exact rational matrix entries are summed before any export; the final rounded 25×25 UPPER has its full max-row-sum export error added on the diagonal.

## Comparison to SM57 and signed 25×25 inertia

The inherited SM57 diagonal \(D_{57}\) is a second **independent complete true UPPER** on exactly the same entire negative source operator. Do not assume \(U_{58}\preceq D_{57}\), which need not hold; neither entrywise nor trace comparisons prove that. Every convex mixture \(U_t=(1-t)U_{58}+tD_{57}\), \(t\in\{0,1/4,1/2,3/4,1\}\), is nevertheless a rigorously valid whole-negative-frequency UPPER.

Recompute SM47/SM49's complete 25×25 original signed-positive LOW lower and the **actual SM42 physical sinh exceptional pole rank-one UPPER**. For each \(t\), form
\[
L_t:=L_{\rm pos,25}-U_t-U_{\rm pole,25}\preceq
W_{\rm odd}|_{\operatorname{span}\{g_0,\dots,g_{24}\}}.
\]
A compact outward rational lower is obtained only after paying the full source matrix max-row-sum error. Exact rational 1×1/2×2 symmetric congruence classifies the **inertia of this lower** for each \(t\). Among five fully certified alternatives, select the smallest number of negative lower-matrix pivots (and then higher trace as a tie-break). This strategy selection uses exact arithmetic and does not compromise validity of the selected lower matrix.

Loewner inertia monotonicity implies only
\[
n_-\!\left(W_{\rm odd}|_{25\mathrm{\ sources}}\right)
\le n_-(L_t).
\]
An indefinite \(L_t\) proves **no actual negative witness** and may give only a vacuous index ceiling of 25. It is essential not to confuse a finite 25-source test, even if positive, with the complete 470-source operator, the original source-eliminated odd orthogonal remainder, odd O1/O2, even sector, signed Weil, CC27 or RH. These remain **OPEN**. Independent mathematical verification of the inherited Fourier/form-domain and full SI10 negative-frequency-support premises is separate from Actions.

## Verification

Focused new SM58 Actions must recheck all original 973 negative support cells, all 25 physical Fourier source analytic derivatives, entire 25×25 Cauchy-Loewner upper and outward export fee, 25×25 signed lower and pole upper, convex alternatives and exact symmetric rational inertia, plus governance fail-closed. **No passing SM58 source or spectral result is claimed before the focused Actions succeeds.** SM57's corrected whole-source verification is also a separate dependency.

If this 25-source coupled upper is still too weak, the next mathematical pressure points are sharper *signed-weight* interpolation on the entire negative cover and block/Schur bounds that exploit original physical source correlations, together with a genuine estimate on the infinite-dimensional orthogonal remainder. This cannot be finished by extrapolating a 3D positivity certificate.
