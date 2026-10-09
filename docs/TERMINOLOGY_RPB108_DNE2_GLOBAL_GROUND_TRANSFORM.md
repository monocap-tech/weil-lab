# RPB108 DNE2 — Positivity-improving and global ground-state semigroup transform

**Parent status:** DNE1 at `ab7b6d0d1e12ee6b9d2152d7a4f71b25122d7886`. DNE2 is the next independent numbered investigation. CC44–CC45 and NF15 remain read-only external dependencies.

**Pole-free operator** H_a: complete original native archimedean-plus-prime form (all prime powers and both orientations), subtracting ONLY both signed Hermitian pole cross terms. Its lower-bounded supported physical operator has compact resolvent. CC43 gives a simple real nonnegative even ground state phi_a, normalized by ||phi_a||_2=1, with eigenvalue lambda_0(a).

**Strict essential positivity:** phi_a(x)>0 for Lebesgue almost every x in (-a,a). This is weaker than a pointwise/Hopf lower bound, but sufficient to define division by phi_a almost everywhere.

**Ground-state unitary:** U_a u=phi_a u, a unitary map from L2((-a,a), phi_a^2 dx) onto physical L2(-a,a).

**Global transformed form:** E_phi(u,v)=H_a(U_a u,U_a v)-lambda_0(a)<U_a u,U_a v>, on the complete closed domain {u:phi_a u in D_a}. It is the closed nonnegative form associated with U_a^{-1}(H_a-lambda_0)U_a.

**Doob semigroup:** S_t=e^{lambda_0 t}U_a^{-1}e^{-t H_a}U_a. Symmetric, strongly continuous, positivity preserving/improving and conservative: S_t 1=1. Therefore E_phi is a Markov (Dirichlet) form on the weighted L2 space.

**Product-core identity:** The DNE1 exact original weighted jump formula holds for u bounded smooth Lipschitz. DNE2's global semigroup transform does NOT, by itself, prove that this product core is a form core or that the same displayed integral equals E_phi(u) for every transformed eigenvector. An asserted extension of the full explicit integral remains separately conditional.

**Odd parity transfer:** Since phi_a is even, U_a preserves even/odd parity. Odd transformed h satisfy weighted mean zero automatically, and a higher pole-free odd zero mode (if it exists) corresponds to a transformed eigenfunction of energy -lambda_0(a), not to ground energy zero.

**Control:** Connected finite attractive graphs admit the same Markov transfer and can still have higher original zero modes. Positivity improving is not an RH-specific obstruction.
