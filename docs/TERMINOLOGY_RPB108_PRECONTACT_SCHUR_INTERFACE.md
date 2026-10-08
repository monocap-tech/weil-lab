# PS2 localized Schur interface

Additive definitions; PS1 and historical terminology remain unchanged.

- **Finite physical block V:** the 112 physical orthonormal polynomial vectors of the aperture-one certificate, pulled to the fixed mass carrier. This is a computational restriction, not an identified near-null spectral projection.
- **Complement W:** its physical orthogonal complement intersected with the canonical form domain. Orthogonality is physical, not the canonical Riesz inner product.
- **Block data:** F_a is the finite native restriction; B_a:V->W is its physical mixed-source residual; C_a is the physical self-adjoint complement operator associated to the restricted form. These block letters do not replace PS1's full canonical A(a).
- **Comparison Schur matrix:** G_a=F_a-c_a^(-1)B_a*B_a when C_a>=c_a I in physical mass. It bounds the exact Schur complement below; it is not generally equal to F_a-B_a*C_a^(-1)B_a.
- **Complement-sensitive coupling:** B_a*C_a^(-1)B_a. Changes in this operator can be smaller than changes in the scalar majorant c_a^(-1)B_a*B_a, but need their own proof.
- **Margin barrier:** a rigorously excluded candidate lower margin for the conservative finite comparison matrix, not an upper bound for the actual physical lowest eigenvalue or a negative actual Weil vector.

PS2 preserves the physical mass operator and the entire actual normalized source system. It adds no source-row deletion, actual contact claim or Lean theorem.
