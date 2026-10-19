# MG05 — Directional source-error fees on the same direct signed fourth-source operator

**October 19, 2026 · Method Gate. W-ODD-NEG, even, Weil, CC27 and RH OPEN.**

## Decision and rationale

SM63 passing Actions 39314851844 established strict original signed positivity on physical sources (g1,g2,g17), hence actual 25-source restricted negative index at most 22 under inherited original Fourier/domain premises. MG02 and MG03 independently reduced errors in the global 23-coordinate reference without improving its 22 negative lower-reference pivots.

SM64 independently computes direct signed positivity on (g1,g2,g17,g22). MG05 is an alternative **complete 4D error enclosure on exactly the same signed form and sources**. SM64 pays a scalar Fourier-cell remainder. MG05 compares that baseline with complete-matrix coordinate-specific bounds, retaining all original offdiagonal source interactions. No SM63 positivity block is illicitly spliced into the 4D lower.

## Full matrix source-error inequality

On a source-frequency cell, write actual physical Fourier vector T(xi) = z(xi)+e(xi), with certified |e_i(xi)| <= r_i and |z_i(xi)| <= a_i for all four original physical source coordinates. Its rank-one error satisfies

  |T_i T_j - z_i z_j| <= d_ij = a_i r_j + a_j r_i + r_i r_j.

Put R=sum_j r_j, A=sum_j a_j, and d_i=(a_i+r_i)R+r_i A. For every real vector h,

  |h^T(TT^T-zz^T)h|
    <= sum_ij d_ij |h_i h_j|
    <= sum_i d_i h_i^2,

using 2|h_i h_j| <= h_i^2+h_j^2. Hence the complete operator-order enclosure is

  -diag(d_i) <= TT^T - zz^T <= diag(d_i).

For positive Jensen cells, z is the exact-rational physical Fourier midpoint source vector and r is the complete analytic **source mean** error. For the signed-negative core and exterior cells, z(xi)=v+derivative*(xi-mid), with a_i=|v_i|+|derivative_i|halfwidth and r the analytic pointwise affine remainder. Both original signed-frequency cases pay absolute nonnegative uncertainty weights. All cross covariance, original signed multiplier and the sinh pole remain.

## Four exact same-integral policies

MG05 constructs FOUR original rational 4x4 signed Loewner lower matrices:

1. scalar: original SM64 uniform full-source error on every signed-frequency cell;
2. trace: select the valid anisotropic row-sum fee when its full four-source trace cost is smaller;
3. fourth: select it when the g22-coordinate fee is smaller;
4. parent3: select it when the total g1,g2,g17 anchor-coordinate fee is smaller.

Each independent policy is a full valid Loewner inequality even when the selection criterion uses only one coordinate. All original 768 signed [13,16] core cells, 973 seven-prime signed-negative leaves / 3892 exterior subcells, old 17+32 and new 96+242 positive bands, genuine exceptional odd pole, and all 16 source cross entries remain unchanged. Each policy's matrix is symmetrically rounded outward. Exact Sylvester minors are computed on the SAME complete 4x4 matrix.

The only strict fourth-source acceptance is four positive rational leading principal minors of one complete certified matrix. If one policy succeeds, the actual supported 25D negative index ceiling is <=21 (not complete odd positivity). If none succeeds, retain independent SM63 actual index<=22. No negative lower pivot is a negative witness for the true original signed form.

## Verification custody

The focused test checks all original source/digamma/seven-prime signed cells, source Fourier identities, strict physical four-source Gram SPD, pole payment, all policy lower matrices, exact four leading principal minors, and no higher theorem promotion. The scalar policy must reproduce SM64's original certified baseline formula; comparison to SM64's final Actions artifact is a further independent audit requirement before accepting a new mathematical claim.

The original 470-source Astar inverse, complete infinite-dimensional odd residual, even-sector, whole Weil positivity, CC27 and RH remain OPEN; original Fourier/form-domain premises still need independent analytic audit.

Reproduce with python scripts/validate_rpb108_mg05_anisotropic_direct_four_source.py.
