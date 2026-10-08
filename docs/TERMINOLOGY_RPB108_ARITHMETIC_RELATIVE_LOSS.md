# CC4 exact original Schur relative loss

Definitions precede load-bearing use. CC1–CC3 and historical terminology remain unchanged.

- Original nested carrier: D_a is the supported canonical logarithmic domain on [-a,a]. For s<=t, D_s is a closed subspace of D_t; Q is the same unshifted original form restricted to these domains.
- Protected nested Schur chart: a fixed finite physical subspace E contained in D_s, a fixed physical orthonormal basis of E, and F_a=D_a intersect E^perp_mass. The original restriction C_a=Q|F_a must have a uniform positive canonical lower bound on the chart.
- Completed graph: W_a x=x-T_a x, with T_a x in F_a solving Q(T_a x,z)=Q(x,z). It is the actual minimizer among vectors with physical E coefficient x, not an original homogeneous eigenmode.
- Exact Schur block: S_a=W_a^* Q W_a, in the SAME fixed E coefficient basis throughout the chart. It is not the scalar inverse-estimator matrix or a trial restriction.
- Shell reaction: L_st=S_s-S_t=H_st^* D_st^(-1) H_st>=0, obtained by eliminating the additional complement directions. D_st denotes the completed shell form, not an aperture derivative.
- Relative reaction: R_st=S_s^(-1/2)L_st S_s^(-1/2), defined while S_s>0. Its eigenvalues lie in [0,1) when S_t>0.
- Exact accumulated relative loss: Lambda(s,t)=log(det S_s/det S_t)=-log det(I-R_st). It is nonnegative and exactly additive across partitions of one protected fixed-coordinate chart.
- Worst-direction step loss: ell(s,t)=-log lambda_min(S_s^(-1/2)S_t S_s^(-1/2)). It obeys Lambda/d<=ell<=Lambda, d=dim E, but is not itself asserted additive.
- Arithmetic nondivergence estimate: an INDEPENDENT finite upper bound for Lambda up to each finite endpoint, together with continued complement protection. CC4 derives the exact loss identity and contact dichotomy; it does not prove this missing estimate for the actual Weil arithmetic.
