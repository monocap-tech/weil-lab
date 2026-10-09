# RPB108 DNE2 — Global Doob transform for the actual pole-free Weil operator

Date: 2026-10-08 America/Los_Angeles. Independent DNE parent `ab7b6d0d1e12ee6b9d2152d7a4f71b25122d7886` (DNE1). [Terminology](../docs/TERMINOLOGY_RPB108_DNE2_GLOBAL_GROUND_TRANSFORM.md). **Classification: analytic full-domain ground-state semigroup theorem, positivity-a.e. consequence, domain-transfer boundary, strict spectral-gap countercontrol. No actual null exclusion, new whole-aperture positivity or RH/F4/Lean certificate.**

## 1. Original pole-free form and the needed positivity

H_a is the EXACT original archimedean digamma plus all prime-power translations (both orientations), with ONLY the two original signed Hermitian pole cross terms removed. CC43 identifies its symmetric off-diagonal continuous kernel as

    -j(x-y), j(d)=exp(-|d|/2)/(1-exp(-2|d|))>0 (d != 0),

and the discrete off-diagonal atoms `-c_n`, `c_n=Lambda(n)/sqrt(n)>0`, at `+/-log n`. Local diagonal renormalizations remain. The form has compact resolvent and a simple nonnegative even ground eigenfunction phi_a of unit physical norm and ground eigenvalue lambda_0 (CC41, CC43). The inherited absolute-value comparison

    H_a(|f|,|f|) <= H_a(f,f)

holds on its closed supported logarithmic domain D_a, so the selfadjoint semigroup e^{-tH_a} preserves positivity (first Beurling-Deny criterion).

### Irreducibility is forced by the actual positive continuous jump kernel

If this semigroup were reducible, there would be a measurable E subset (-a,a) with both E and E^c of positive measure such that the ideal L2(E) reduces the semigroup. The standard form characterization of reducibility makes 1_E f and 1_Ec f members of D_a for every f in D_a and forces

    H_a(1_E f, 1_Ec f)=0.                           (1)

Choose f=eta in D_a, with eta(x)>0 for every |x|<a: for example eta(x)=exp(-1/(a²-x²)) on |x|<a and zero elsewhere. This globally smooth, compactly supported function vanishes to infinite order at the endpoints and belongs to the supported form domain by interior-cutoff approximation. It is NOT an element of C_c^infty(-a,a) in the usual support-away-from-boundary sense. Both projections are nonzero and disjoint. For these disjoint nonnegative supported form vectors, the local diagonal part contributes zero; the full native off-diagonal terms give a nonpositive mixed pairing, and the continuous term is strictly negative:

    H_a(eta 1_E, eta 1_Ec)
      = - int_E int_Ec j(x-y)eta(x)eta(y)dxdy
        - sum_(log n <= 2a) c_n [both directed cross shifts] < 0.  (2)

The mixed form is finite by form continuity. For the strict sign, select separated positive-measure portions of E and E^c: any two distinct Lebesgue density points admit separated small neighborhoods of positive intersection, where j is bounded strictly positive. No assumption of regular boundaries of E is made. This contradicts (1). Therefore the semigroup is irreducible.

For selfadjoint lower-bounded forms, irreducibility plus positivity preservation implies positivity improvement for every t>0 (standard semigroup theorem). Because

    e^{-tH_a}phi_a=e^{-lambda_0 t}phi_a

and phi_a is nonzero and nonnegative, positivity improvement yields

    phi_a(x)>0  for Lebesgue-almost every x in (-a,a).     (3)

This is a genuinely stronger regularity/positivity conclusion than CC43's nonnegativity; it does NOT assert a pointwise lower bound, essential boundedness, Hopf boundary asymptotic, or phi_a^{-1} local boundedness.

External transfer checks: Arendt et al., *Strict Positivity for the Principal Eigenfunction of Elliptic Operators*, 2020, https://www.degruyterbrill.com/document/doi/10.1515/ans-2020-2091/html (abstract irreducibility/positivity-improving equivalence); Frank--Lenz--Wingert, *Intrinsic metrics for non-local symmetric Dirichlet forms*, 2014, https://arxiv.org/abs/1012.5050 (ground transforms for nonlocal forms). The facts applied here concern the closed supported native form, not an unrestricted logarithmic Fourier multiplier on zero-extended vectors.

## 2. Exact global weighted semigroup without quotient-regularity assumptions

Put mu_a(dx)=phi_a(x)^2 dx. Since phi_a>0 a.e., multiplication

    U_a : L2((-a,a),mu_a) -> L2(-a,a), u -> phi_a u

is unitary onto the ENTIRE physical Hilbert space, not merely the span of smooth products. Define, by unitary conjugation,

    S_t=e^{lambda_0 t} U_a^{-1}e^{-tH_a}U_a.     (4)

It is strongly continuous, selfadjoint, positivity preserving and improving on weighted L2(mu_a); and

    S_t 1=e^{lambda_0 t}U_a^{-1}e^{-tH_a}phi_a=1.

As a positive unital contraction, S_t preserves [0,1] pointwise a.e.; it is a symmetric Markov semigroup. Its complete closed Dirichlet form is

    E_phi(u,v)=H_a(phi_a u,phi_a v)
                         -lambda_0 <phi_a u,phi_a v>,
    Dom E_phi={u:phi_a u in D_a}.               (5)

Thus the **ABSTRACT ground-state transform and its entire form domain are established** without a bounded ground state, inverse ground state, boundary trace or smooth eigenfunction.

DNE1's explicit weighted jump formula (continuous j(x-y)phi_a(x)phi_a(y) differences and each original prime conductance) is already valid on bounded smooth Lipschitz multipliers, as recorded. Formula (5) does NOT alone establish that this special product class is a form CORE of E_phi, or that the displayed explicit jump integrals equal E_phi on every rough transformed higher eigenfunction. Positivity-a.e. eliminates the pure measurability objection to division; a full explicit integral-domain identification still needs separate regularity/closure verification. In particular, do not directly substitute an arbitrary ratio h/phi_a into DNE1's pointwise displayed kernel identity.

The nonlocal form literature supplies possible transfer machinery, but its precise quasi-continuity, measure-potential and core hypotheses have not yet all been checked for this native supported logarithmic/pole-free operator. Pure log(|xi|) eigenfunction theorems do not automatically transfer to the actual log(e+|xi|) carrier or bounded-but-nonlocal prime-shift perturbation. A directly relevant primary paper on the precise supported carrier is `Spectral properties of the logarithmic Laplacian`, https://link.springer.com/article/10.1007/s13324-021-00527-y (its logarithmic form uses log(e+|xi|)); it does not certify an actual zeta ground-state boundary profile.

## 3. Full spectral reformulation and odd parity

Reflection commutes with H_a and phi_a is even, hence U_a preserves parity. If h is a higher odd H_a eigenfunction at eigenvalue 0 (the DNE moment-zero obstruction), then u=U_a^{-1}h is a valid odd vector in Dom E_phi and

    E_phi(u,u)= -lambda_0 ||u||²_(mu_a).          (6)

The corresponding globally defined Markov generator `G_phi=U_a^{-1}(H_a-lambda_0)U_a` is nonnegative, has simple eigenvalue 0 at constant 1, and has a non-ground eigenvalue `-lambda_0` precisely when H_a has a zero eigenvalue. The odd case is automatically weighted-orthogonal to constants by reflection. The even zero-moment case imposes BOTH weighted orthogonality to constants and its original cosh moment-zero condition.

This identifies the exact gap obstruction WITHOUT any source-shell inverse. To exclude an odd zero moment, one must certify

    inf spectrum(G_phi|odd) > -lambda_0,        (7)

or an equivalent strict full-domain jump-conductance inequality. Merely having a positivity-improving Markov semigroup only yields `inf spectrum(G_phi|odd)>0`, **not** the stronger bound (7). DNE1's conditional explicit odd reflection floor Gamma_odd is one sufficient candidate if its kernel representation extends and the floor is evaluated. The same caution applies to the even sector, which has the additional moment constraint.

## 4. Strict connected-graph countercontrol

Take a three-site symmetric attractive complete graph with
phi=(1,2,1), J_01=J_12=1/2, J_02=1/4, all positive. Define a symmetric matrix L with off-diagonal L_ij=-J_ij and diagonal L_ii=sum_(j!=i) J_ij phi_j/phi_i. Then L phi=0, and

    L = [[5/4,-1/2,-1/4],
         [-1/2,1/2,-1/2],
         [-1/4,-1/2,5/4]].

The weighted transform by phi is a conservative, irreducible Markov generator with jump rates q_ij=J_ij phi_j/phi_i and invariant/reversible site weights phi_i²=(1,4,1). L has eigenvalues (0,3/2,3/2). Choosing H=L-(3/2)I creates ground eigenvalue -3/2 and BOTH higher even and odd eigenvalue ZERO, with a strictly positive nonconstant ground state and every off-diagonal strictly negative. The odd vector (1,0,-1) is an exact H-null. Thus even full-domain positive-ground semigroup transfer, fully connected native-like jumps, strict positivity of the ground state, and parity preservation cannot by themselves exclude higher nulls. This is an operator/control countermodel, NOT the exact original zeta form nor a counterexample to RH.

The independent rational control validator verifies the graph identities. It is not a substitute for any real Weil ground eigenvector or prime coefficient calculation. Full DNE contact exclusion requires new zeta-specific arithmetic beyond the Markov property.

## 5. Next DNE frontier and proof status

**New proved analytic facts:** irreducibility of the native pole-free semigroup from its strictly attractive continuous off-diagonal kernel, positivity-improving semigroup, phi_a>0 a.e., globally defined unitary/closed Markov ground-state transform on the COMPLETE supported form domain.

**Not proved:** phi in L-infinity or locally uniformly positive, the explicit weighted-jump formula extended to all quotient eigenfunctions, actual evaluation of a strict Gamma_odd>-lambda_0 or even constrained gap, any exclusion of higher moment-zero original nulls, moment-carrying even/odd contact exclusion, all-cap original positivity, RH/F4/transport/Lean.

**DNE3:** Verify the exact Beurling-Deny jump-measure/domain identification for the globally transformed form, including prime translation atoms, and determine whether a lower gap stronger than -lambda_0 can be certified with the ACTUAL ground function (not a freely chosen positive bump). If no strict arithmetic surplus emerges, classify the obstruction without manufacturing a theorem.

Read-only concurrency: Coupled CC45 `9c95fc2fb3c1027ea8734ca433306c9456ed4fc2` at start of investigation; independent Aperture NF15 has certified a finite native E80 sign at a=53/50, but the full E112 mixed Schur remains open. Neither external branch is modified.
