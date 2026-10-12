# RC162 terminology additions

Definitions are additive; historical terminology remains unchanged.

**Conditioned-trial marginal norm bound.** The seven paid action columns have D-norm error bounds epsilon_i. For fixed inverse trial coefficients Y and conditioned source coefficients c, the error norm is at most sum_i epsilon_i |(Yc)_i|. RC162 bounds this functional uniformly against the same certified conditioned source Gram lower G.

**Transformed signed control.** For a real sign vector sigma, z_sigma=Y^T(sigma_i epsilon_i). The rank-one matrix z_sigma z_sigma^T must be dominated by beta G to certify the uniform marginal norm bound. Simultaneous sign reversal preserves this matrix, leaving 64 controls.

**Sharp marginal model control.** The maximizing signed functional has coefficients c=G^-1 z. A family of artificial error columns sigma_i epsilon_i times one real unit vector realizes the maximum ratio. This checks the information content of the marginal norm bounds, not compatibility with the actual endpoint operator, its self-adjointness, or all native arithmetic identities.

**Blended trial-error bound.** Convex combinations of the sharp uniform error matrix and the paid weighted-column error matrix remain valid error uppers. RC162 tests their matrix geometry in the combined endpoint functional rather than treating an improved scalar action bound as inverse closure.
