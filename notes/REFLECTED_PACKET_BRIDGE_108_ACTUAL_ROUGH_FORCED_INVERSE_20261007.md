# RPB108: an actual smooth-forcing inverse fails the critical premise

Date: 2026-10-07 UTC. Recovered live head 0da9145912cfd3f008cac490b35d0456fe1f0a27.
Definitions: [actual rough forced inverse](../docs/TERMINOLOGY_RPB108_ACTUAL_ROUGH_FORCED_INVERSE.md).
Category: critical derivative promotion / endpoint exclusion.
Analytic actual control, using an external logarithmic-Laplacian barrier theorem. No Lean certification.

## Result and exact scope

At a sufficiently small actual window with Q_a strictly positive and K_a={0}, take any nonzero nonnegative f in C_c^infinity(-a,a). The unique actual canonical solution

    Q_a(u,v)=<f,v>_2, v in D_a,

is nonnegative, bounded and continuous after zero extension. At either physical endpoint it has a lower bound

    u(a-t)>=c/sqrt(log(1/t)), 0<t<t1,

for constants c,t1>0 depending on the forcing and window. Thus its zero extension is not H^(1/2), and in particular u is not Xcrit. The full actual positive source moment of order one is infinite by the established source/Fourier equivalence.

This control includes the actual quarter-line symbol, the exact pole and complete actual source dictionary. The prime set is genuinely empty at this window. No artificial mass shift or invented source row is used. The equation is q_u=f, not q_u=0.

Consequently the previous critical inverse-test premise is FALSE as a proposed assertion at every nonnegative actual window: here the kernel is zero, so every smooth forcing meets its orthogonality condition and there is no kernel correction capable of improving u. The preceding conditional implication remains valid. A version restricted to a hypothetical nonnegative first contact is not refuted by this control and remains unproved. The original critical zero-kernel derivative gate is not refuted: it is vacuous at the present coercive window.

## 1. Exact combined kernel, including the pole

Let m00=m0(0). The recovered Euler energy identity is

    E0(h)=m00 ||h||_2^2+integral_0^infinity k(s)||tau_s h-h||_2^2 ds.

For 2a<log 2 there are no frozen prime translations. The actual pole is

    p_h(x)=integral_Omega 2cosh((x-y)/2)h(y)dy.

Separate the exterior part of the Euler integral and combine the interior pole with its interaction kernel. This gives the exact native form

    Q_a(h)=integral_Omega V_a(x)|h(x)|^2 dx
        +(1/2)integral_(Omega times Omega)
                     J(x,y)|h(x)-h(y)|^2 dx dy,

where J and V_a are defined in the registry. The half factor counts ordered pairs once. This is the actual full form, not the pole-free comparison form.

Choose any a>0 satisfying

    a<=1/32,
    a<=(1/4)exp(-2(|m00|+2)).

For 0<s<=1, 1-exp(-2s)<=2s and exp(-1/2)>1/2, so k(s)>1/(4s). At 0<s<=2a<=1/16, k(s)>4 while 2cosh(s/2)<3. Hence J(x,y)>1 for distinct x,y in Omega.

Both exterior rays include distances s>=2a. Therefore

    V_a(x)>=m00+2 integral_(2a)^1 k(s)ds
           >m00+(1/2)log(1/(2a))
           >2.

The omitted pole integral is positive. Thus Q_a>=2||h||_2^2. The logarithmic Garding envelope upgrades this to canonical-domain coercivity: Elog(h)<=Q_a(h)+C_a||h||_2^2<=(1+C_a/2)Q_a(h), after enlarging C_a to be nonnegative. The actual Fredholm kernel is zero.

These inequalities construct a small-window control. They do not advance the aperture frontier, optimize its complement or replace any existing certificate.

## 2. Existence, sign and boundedness of the actual inverse

Coercivity supplies the unique u in D_a for the specified f. The form in section 1 is real, so u is real. The native energy domain is stable under absolute value and Lipschitz truncation: the positive Euler difference energy contracts under those operations and the physical mass remains finite.

Test with the negative part. The J interaction and V terms have the maximum-principle sign, while the forcing is nonnegative, so u>=0. For the upper bound, the constant zero-extension 1_Omega belongs to D_a and its interior action is V_a. Comparison with (||f||_infinity/2)1_Omega gives

    0<=u<=||f||_infinity/2.

The same negative-part test gives a local comparison principle on any subinterval: if a form-domain function is nonnegative off that subinterval within Omega and has nonnegative weak action there, its negative part vanishes. No maximum principle for arbitrary apertures is asserted.

## 3. Transfer to the external logarithmic operator

Set k_reg(s)=k(s)-1/(2s), bounded on [0,1], with value 1/4 at zero. On this window all distances between support points are below one. The physical representation of the angular-symbol logarithmic Laplacian gives, on Omega,

    m0(D)u=(1/2)L_Delta u+c0 u
                     -integral_Omega k_reg(|x-y|)u(y)dy,

    c0=m00-rho_1/2
             +2 integral_0^1 k_reg(s)ds
             +2 integral_1^infinity k(s)ds.

Here rho_1 is the mass constant in the external logarithmic-Laplacian representation. Both integrals defining c0 are finite. The native pole is another bounded integral operator on bounded supported functions. Consequently the exact equation q_u=f gives L_Delta u a bounded right-hand side on Omega.

The external paper establishes continuity through the boundary for bounded zero-exterior weak solutions with bounded forcing (Theorem 1.1), and supplies a positive small-interval torsion barrier comparable to the inverse square root of the boundary logarithm (Theorems 1.2 and 5.2). Its normalization matches the factor 1/2 above. We use those results as external analytic inputs, not as Lean-certified repository facts.

The native and external form domains on a fixed bounded interval agree: their local positive difference kernels have the same logarithmic singularity, and the remaining form terms are bounded by physical mass. Thus Theorem 1.1 applies and u is continuous globally with zero boundary values. Since f is nonzero, u is nonzero; continuity and nonnegativity give a compact interior interval W on which u>=eta>0.

The external generalization to all zero-order kernels is not assumed. The bounded difference just proved and the actual local comparison principle provide the transfer below.

## 4. An actual edge comparison, rather than a borrowed Hopf lemma

Choose a sufficiently short right edge interval I=(a-delta,a), disjoint from W, whose length meets the external torsion theorem's smallness condition. Let beta be its positive logarithmic-Laplacian torsion function, extended by zero. It belongs to the native form domain, is bounded and satisfies

    L_Delta beta=1 on I,
    beta(a-t)>=c_beta/sqrt(log(1/t))

for sufficiently small positive t. By section 3 and the bounded pole, the actual native weak action q_beta is bounded above on I by some finite M>=0.

For x in I, the exact combined action on 1_W is

    q_(1_W)(x)=-integral_W J(x,y)dy<=-|W|.

Put lambda=(M+1)/|W| and b=beta+lambda 1_W. Then q_b<=-1 on I. Choose a positive epsilon with epsilon lambda<=eta. Off I within Omega, beta=0 and u>=epsilon lambda 1_W. On I, q_u=f>=0 and therefore q_(u-epsilon b)>=0. The actual local comparison principle yields

    u>=epsilon beta on I.

Reflection gives the other endpoint, choosing its own disjoint interior patch. This proves the stated logarithmic lower boundary bound for the ACTUAL forced inverse. The indicator patch is a lawful logarithmic test; no derivative trace or critical norm of u was assumed.

## 5. Critical divergence

For a zero-exterior H^(1/2) vector, the physical Gagliardo seminorm includes the exterior cross term and hence requires

    integral_0^t1 |u(a-t)|^2/t dt<infinity.

The lower bound instead gives

    integral_0^t1 |u(a-t)|^2/t dt
       >=c^2 integral_0^t1 dt/[t log(1/t)]
       =infinity.

Thus u fails H^(1/2), not merely the stronger logarithmic Xcrit norm. The actual positive source order-one moment is therefore infinite. No signed null trace is assigned to this non-null vector.

An estimate that places all smooth-forcing native inverse tests in Xcrit cannot hold even at these strictly positive actual windows. Finite kernel, exact actual arithmetic custody and a sharper transverse strip do not repair this forced-boundary obstruction.

## Failed implication and remaining theorem

Failed implication, now with an actual control:

    nonnegative actual form + Fredholm inverse + smooth compact
    forcing orthogonal to K_a -> inverse solution in Xcrit.

The control has K_a=0 and a unique solution, so neither changing inverse representatives nor finite kernel subtraction rescues it. This is stronger than the preceding isolated cutoff-profile control.

The smallest original obligation remains exact zero-kernel critical promotion K_a intersect Xcrit -> L2 derivative. That theorem concerns a critical homogeneous solution, whereas this forcing control is neither homogeneous nor critical. It does not disprove the gate.

A contact-only critical inverse-test premise would be an additional theorem with narrower quantifiers; no argument currently supplies it. This pass does not silently adopt it. A different duality argument might use tests outside Xcrit together with a proved zero-specific boundary pairing; that joint pairing is also unproved. The order-3/2 signed contact trace remains an alternative unresolved arithmetic target. Neither route is made true by repeated reformulation.

Validation is analytic: exact native pole combination, coercivity, truncation comparison, bounded operator transfer, edge barrier and critical divergence are explicit. External theorem applicability is checked above. There is no computed inverse/eigenvector, new aperture sign, Lean build or axiom audit. Accepted |beta_rho|<=3/8 remains in force but is not used to overcome this physical boundary geometry. Actual endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain unproved. Newer 96-moment preflight at 97/100 is preserved; certified whole-domain frontier remains 24/25.

## Source custody

External primary input: Hernandez-Santamaria, Lopez Rios and Saldana, Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian, arXiv:2401.18033v2 (3 July 2024), https://arxiv.org/pdf/2401.18033v2, DOI 10.3934/dcds.2024084. Read 2026-10-07: physical normalization (1.2), domain/form (1.15)-(1.17), Theorem 1.1, Theorems 1.2/5.2. No downloaded-PDF hash or formalization is claimed. The transfer proof is repository analysis, not a statement quoted from that paper.

Pinned repository sources are listed in the accompanying manifest.

- notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_INVERSE_TESTS_20261007.md, blob 0a5acc72749e39a54e92cbdc8c16337e81e36702.
- docs/TERMINOLOGY_RPB108_CRITICAL_INVERSE_TESTS.md, blob c3f80846c112325c2407215f0f9761c3dedd7ba6.
- notes/REFLECTED_PACKET_BRIDGE_108_ARCHIMEDEAN_CONTACT_CONTROL_20261006.md, blob cef50e5e46a7ddc6218f33042e720a0c12da58b4.
- notes/REFLECTED_PACKET_BRIDGE_108_LOGARITHMIC_BOOTSTRAP_20261005.md, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028.
- notes/REFLECTED_PACKET_BRIDGE_108_FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006.md, blob 955ff7b4bd0d7f58221c300a962a803824232fd6.
