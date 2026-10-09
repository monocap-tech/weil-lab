# RPB108 — DNE34 terminology: coherent projected source block

Definitions are additive. DNE29's tested source credit, DNE31's frozen remainder and DNE32/DNE33's certificates remain unchanged.

**Coherent frozen remainder block X_[0,m):** the first m exact columns of DNE32's native-normalized packet X=hatY U. Each original source is approximated once at the same regular order, coefficient grid and translation cells. Every diagonal and mixed Gram entry uses these same source approximations and the same retained projection coordinates.

**Complete projected source block Gamma_m:** the m-by-m matrix <P_F112 L_original X_i,P_F112 L_original X_j>. Complete means every component of each source norm and pairing, including the unmeasured high tail. A proper principal block does not cover all 52 remainder columns in that parity.

**Exact signed Kronecker convolution:** polynomial coefficients on a common integer grid are packed into an integer with radix 2^b, multiplied exactly, and unpacked using centered digits. The explicit coefficient bound min(lengths) max|a_i| max|b_j|<2^(b-1) prevents carries from obscuring any coefficient. This changes the arithmetic implementation, not the polynomial or source model.

**Complete retained projection subtraction:** Gamma_N,ij=<s_N,i,s_N,j>-sum_(n<112)<s_N,i,e_n><s_N,j,e_n>, with all 56 same-parity retained coordinates. Mixed entries retain their signs. The independent validator reconstructs this identity from stored rational whole-source and coordinate intervals.

**Mixed original-source error payment:** if e_i bounds the physical L2 source error and R_i bounds the projected approximate-source norm, each Gram interval is enlarged by e_i R_j+e_j R_i+e_i e_j. Polynomial coefficient rounding and the original analytic source remainder are both included in e_i.

**Half-credit budget:** Gamma_m<=(c/2)C_m, where C_m=Q(X_[0,m),X_[0,m)) and c is the inherited tested source credit. It is a convenient sufficient allocation, not the actual high inverse response.

**Paid reallocation:** replace c/2 by a certified rational r while using the actual paid native dual border epsilon. The DNE25 sufficient criterion remains r+kappa epsilon<c. Failure of the half-credit matrix budget alone does not disprove this more general criterion.

**Full-credit obstruction witness:** an exact nonzero rational vector v with v*(c C_m-Gamma_m)v<0. It rules out every proportional source budget r<=c on this fixed block, and therefore this particular tested/remainder scalar-credit criterion. It is not a negative vector of the original Weil form or a disproof of whole-aperture positivity.

**Certified source-budget congruence:** a rational upper-triangular invertible U_b for which U_b*(r C_m-Gamma_m)U_b has strictly positive paid Gershgorin row margins. Decimal or floating-point arithmetic may choose r and U_b; only outward intervals and rational validation establish the comparison.

**All-high prefix extension:** the four tested directions plus a certified first n remainder columns in each parity, together with every original vector in F112. The retained projection has rank 4+n. Passing the source-budget congruence and the paid native border gives a positive original Schur form on this entire subspace.

**Frozen scalar-credit route obstruction:** the full-credit witness is embedded by zeros in the full 52-column remainder packet. Since the sufficient criterion demands r+kappa epsilon<c, it cannot hold for that frozen packet. An invertible change of remainder coordinates transforms source and native matrices by the same congruence and does not remove the witness.

**Standalone remainder source-floor control:** a positive congruence for kappa C_8-Gamma_8. It proves positivity of those remainder directions after adjoining all original high vectors, separately from the tested span. It does not pay the mixed terms needed to unite the two positive subspaces.

**Joint signed source target:** kappa Q_(T4 union X)-Gamma_(T4 union X), including the actual mixed source entries. This avoids replacing the remainder source by a separate budget below c. The original high floor may still suffice; failure of the scalar-credit allocation does not make an actual inverse evaluation inevitable.
