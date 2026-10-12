# RC156 terminology additions

These entries are additive; historical terminology remains unchanged.

**Complementary trial-source block Q.** Sources are ordered (psi0,delta), delta=z_b6-v10; trials are ordered (q_psi,q_delta), as defined by RC154 and RC153. Q_ij=<q_i,s_j>_D. It is generally not symmetric. RC156 evaluates its four entries directly from the reconstructed rational finite coefficients and prescribed analytic tails, rather than transporting an inherited endpoint interval.

**Complementary trial Gram R.** R_ij=<q_i,q_j>_D for those same two full-carrier trial vectors. R is symmetric. Its finite prefix includes q_psi's midpoint input-tail contribution at even degrees 8192 through 16382. Its remaining infinite tail starts at even degree 16384; q_delta has no coefficients there.

**Signed polynomial pairing-tail budget.** Beyond degree 16382, every nonzero source or trial tail in this block has the common coefficient eta_n=(2n+1)/(n(n+1)D_n), multiplied by a prescribed polynomial in inverse n(n+1). Multiply the two signed polynomials first, then bound positive and negative coefficient terms with the certified total eta D-energy. This bounds the entire infinite pairing tail without discarding the signed delta coefficients.

**Paid symmetric endpoint intersection.** If ||Cs_i-q_i||_D<=epsilon_i, then H_ij=<Cs_i,s_j>_D lies within epsilon_i||s_j||_D of Q_ij, and within epsilon_j||s_i||_D of Q_ji. Intersect both directed intervals with inherited H intervals. The resulting H block is symmetric even though Q need not be.
