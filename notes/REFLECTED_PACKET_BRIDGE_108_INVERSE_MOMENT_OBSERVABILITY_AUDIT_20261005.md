# RPB108: the averaged inverse moment is not an exclusion observation

Base: ef46f5691790d06d40cc521ca4434962f2f1643e.
Definitions: docs/TERMINOLOGY_RPB108_MOMENT_OBSERVABILITY_AUDIT.md.
Standing: explicit comparison construction and analytic applicability audit.

## Exact nonzero even control

Fix L=2a>0 and let z(v)=v(L-v). Define

    f_1(v)=z(v)[z(v)-L^2/6],  0<v<L,

and zero outside. Set h_1(x)=f_1(a-x). This is real and even. It vanishes at both endpoints, is polynomial on the interior and has zero extension in H1(R): its weak first derivative is the bounded polynomial derivative on the interval and zero outside, without endpoint delta terms because the function itself is continuous and zero there. Hence it belongs to the canonical logarithmic domain and satisfies the critical Fourier regularity conditions being investigated.

It is nonzero arbitrarily near both endpoints, so every left and right support collar has positive L2 mass. Nevertheless

    integral_0^L f_1(v)dv/v=0,
    ||f_1||_2^2=L^9/7560>0.

For L=2 the latter is 64/945. The averaged leading Carleman pairing from the preceding theorem therefore vanishes exactly, although the physical vector is nonzero. The profile changes sign: near each edge it is negative, and at the center it is positive.

This is not asserted to satisfy the actual weak-null equation. At a certified positive aperture it cannot do so. No actual negative/null vector, off-line zero or RH counterexample is constructed.

## An infinite independent comparison family

For every integer p>=1 put

    f_p(v)=z(v)^p [z(v)-c_p],
    c_p=L^2 p/[2(2p+1)].

The same reality, even parity, H1 membership and support-collar saturation hold. Its inverse moment vanishes because

    integral_0^L z(v)^(p+1)dv/v
      / integral_0^L z(v)^p dv/v
      =L^2 B(p+1,p+2)/B(p,p+1)
      =L^2 p/[2(2p+1)].

For integer p this ratio also follows by expanding the two polynomials and integrating monomials, so no special-function identity is needed. Distinct p give distinct highest degrees 2p+2 with nonzero leading coefficient. The family is therefore linearly independent. Every member has positive physical mass and zero averaged scalar moment.

Consequently no positive estimate |M(f)|^2>=c||f||_2^2, c>0, holds on the arbitrary supported carrier, its real even sector, or the explicit edge-saturated H1 comparison family. This failure concerns a single observation, not the full source/divisor analysis map.

## Actual route boundary

The preceding averaged singular-kernel identity remains valid under its stated gap or absolute inverse-moment integrability hypotheses. Its rank-one output cannot supply actual endpoint exclusion merely by requiring that scalar average vanish. Reflection parity and support saturation do not repair that loss of information, and stronger regularity by itself does not remove these comparison controls.

An actual-kernel-specific injectivity theorem could still work, because these profiles are not asserted to solve the actual interior mixed equation. It would first need to establish that the inverse moment exists for actual modes, then exploit the exact prime/pole or complete source observations to rule out nonzero actual modes in its scalar kernel. Both steps are additional obligations, not conclusions of the averaged identity.

The bounded nonnegative divergent-moment obstruction also remains valid in its extra sector; these sign-changing controls lie outside that sector and explain why it is not exhaustive after the even/odd reduction.

The next research step must use the full actual interior equation and independent arithmetic/source information, or an independent endpoint exclusion mechanism. Further algebraic refinement of the one averaged moment alone does not close the missing observability. Critical regularity is also not an endpoint-exclusion theorem by itself.

Numerical frontier remains 81/100. Global endpoint exclusion, retained selected-witness attachment, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms and CI unchanged.

## Verification boundary

Exact rational polynomial controls check inverse moments, positive L2 masses, parity and endpoint zeros for p=1 through 8 at three scales. A control equating zero moment to zero physical mass is rejected. The family-wide independence and H1 argument are analytic. The controls are not actual weak-null modes, and no test establishes actual-kernel injectivity.
