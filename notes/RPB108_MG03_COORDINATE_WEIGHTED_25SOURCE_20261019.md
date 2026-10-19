# MG03 — Complete 25-source weighted-error and weak-direction method gate

**October 19, 2026.** Stacks on the passing MG02 (#246) and SM62 (#245). Actual full W-ODD-NEG, even, Weil, CC27 and RH remain OPEN.

## Motivation

MG02 exact-rational Actions 39312736956 PASSED: 296 of 338 real cells selected a whole-operator Young bound, recovering a 23-complement lower TRACE amount +0.2082176910, but both MG02 and SM62 have 22 negative pivots in the 23D coordinate-complement lower reference. This confirms that reducing aggregate scalar error is not sufficient by itself to close the signed Schur.

SM63 is separately exploring a direct physical three-source strict positivity certificate. MG03 is NOT a duplicate of that original signed-domain test; it instead asks whether uncertainty in the **whole 25-source mean-vector enclosure** can be redistributed in a way that improves the weak complement or designated g1/pole directions.

## Exact weighted whole-operator inequality

On each of the same 338 original real sign-positive disjoint source-frequency intervals used by SM62, let \(u=v+e\in\mathbb R^{25}\) be the actual Fourier mean, with exact-rational enclosures \(|e_i|\le r_i\). In the original physical supported-source representation, its positive contribution has weight
\(\gamma=2|I|(m_{I,\mathrm{lo}}-\kappa)>0\).

The rank-one difference \(D=uu^\top-vv^\top\) has entrywise bound
\[
 |D_{ij}|\le d_{ij}:=|v_i|r_j+|v_j|r_i+r_ir_j.
\]
For **any positive rational weighting vector** \(w=(w_i)>0\), the complete symmetric form bound is
\[
|z^\top Dz|
\le\sum_{ij}d_{ij}|z_i z_j|
\le\sum_i z_i^2 \sum_j d_{ij}\frac{w_j}{w_i}.
\]
Thus the actual original whole-source rank-one covariance obeys
\[
\boxed{\gamma uu^\top\succeq
\gamma vv^\top-
\operatorname{diag}\left(
  \left\lceil\gamma\sum_j d_{ij}w_j/w_i\right\rceil
\right) .}
\]
This **dominates all off-diagonal uncertainty in full 25D operator order**; it does not assert componentwise scalar positivity and does not drop source crosses.

For efficient exact-rational arithmetic let \(R_w=\sum_j r_j w_j\) and \(A_w=\sum_j |v_j|w_j\).
Then each diagonal fee is \(\gamma[(|v_i|+r_i)R_w+r_i A_w]/w_i\), rounded upward independently.

## Competing certificates and acceptance

MG03 evaluates complete rank-one lower matrices for each identical original signed-positive cell using MG02's scalar/Young selection and seven separately valid Gershgorin weight choices: uniform, amplitude, inverse-amplitude, complement focus, positive-two-plane focus, g1 focus, and pole24 focus.

Three independent policies choose the certificate maximizing the exact **one-cell** contribution to the 23-coordinate lower trace, the g1 source-1 signed lower diagonal, or the physical sinh-pole source-24 lower diagonal. Each chosen candidate is a valid full 25D Loewner lower, regardless of selection criterion; sums retain entire physical source cross.

Complete rational signed lower matrices are independently assembled and outward-rounded at 96, 192, 288 and 338 original disjoint windows. Every resulting 25D and 23D lower-reference inertia is computed with exact-rational 1x1/2x2 congruence. Record direction-specific trace/diagonal improvement and whether **lower-reference inertia changes**; do not infer anything about the actual negative index from negative lower pivots.

The 973 original negative Fourier leaves, original baseline 49 positive windows, original pole penalty and all 625 verified SM58 matrix entries are replayed unchanged.

**Decision:**
- If the weak-complement negative lower-reference inertia decreases, the weighted method has a viable structural lead, not an odd-sector proof.
- If only trace/diagonal improvements occur with unchanged inertia, classify as another METHOD LIMIT and prioritize direct signed integration on residual weak directions or a new positive-energy inverse/Schur method.
- If no adaptive directional improvement occurs, reject the diagonal Gershgorin weighting strategy in favor of a matrix-correlated error enclosure.

No 470-source Astar inverse, infinite orthogonal remainder, even operator, Weil or RH theorem is promoted. Independent audit of the original signed Fourier multiplier, supported source transformations and operator domain remains required.

Run: python scripts/validate_rpb108_mg03_coordinate_weighted_25source.py.
