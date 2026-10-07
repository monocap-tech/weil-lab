# RPB108: the global pole budget cannot be inserted into the local edge estimate

Date: 2026-10-07 UTC. Recovered 617480dc67ee6840abed3c33a1f262d0ab8f226b.
Definitions: [combined right-edge drive](../docs/TERMINOLOGY_RPB108_COMBINED_RIGHT_EDGE_DRIVE.md).
Category: endpoint exclusion. Audit of the principal archimedean boundary route.

## Exact combined physical formula

Take h in the actual full-native K_a and retain the right-limit frozen prime set. Set f(v)=h(a-v). For 0<u<t0<log 2 the read full exterior formula gives

    r_h(a+u)=-integral_0^(2a) K_E(u+v)f(v)dv
             -sum_(log n<=2a) Lambda(n)/sqrt(n) h(a+u-log n)
             +p_h(a+u).

Every positive shift h(a+u+log n) is outside the support and vanishes. Threshold equalities in the negative shifts remain included. Expanding the Euler kernel at zero gives

    K_E(s)=1/(2s)+1/4+O(s).

Thus k_reg is bounded on [0,2a+t0], and the exact residual can be written

    r_h(a+u)=-(1/2)integral_0^(2a) f(v)/(u+v)dv+A_h(u).

This is a decomposition of the actual combined residual; no cancellation or estimate for A_h is assumed. The resulting full flux is

    F_h(t)=-(1/2)Re integral_0^t integral_0^(2a)
                      f(v) conjugate(f(t-u))/(u+v) dv du
           +Re integral_0^t A_h(u) conjugate(f(t-u))du.

The smallest missing lower estimate must control this combined expression on the exact zero kernel. A single averaged inverse moment is not substituted for the Carleman profile.

## Local pole and global pole are different quantities

In the exact full-null translation identity the global correction is

    (cosh(t/2)-1)Ppole(h)=O(t^2).

This follows by subtracting the full diagonal pole pairing from the full translated pole pairing, including its interior portion. It is not the local exterior pole pairing F_pole^edge(t). Full-nullity cancels the entire interior native action, not its pole summand separately.

Likewise boundedness of a finite prime multiplier in the global cosine defect is not a bound of the same order for its individual physical collar pairing. A proof splitting the right-edge formula and assigning the global O(t^2) pole budget to F_pole^edge drops the interior cancellation.

## Supported physical control for the false substitution

Choose a nonnegative cutoff chi(v), equal to one near v=0 and zero before a fixed delta<2a, and let

    h(a-v)=v^(1/4)chi(v),  0<v<2a,
    h=0 outside [-a,a].

This is a legitimate canonical logarithmic vector and is globally H^beta for beta<3/4, by the edge-difference estimate already audited in the critical cusp note. It is NOT assigned an actual null or eigen-equation.

Its two actual pole moments are positive, hence p_h(a)>0. Smoothness of the pole profile gives, for sufficiently small t,

    F_pole^edge(t)
      =p_h(a) integral_0^t (t-u)^(1/4)du+O(t^(9/4))
      =(4/5)p_h(a)t^(5/4)+O(t^(9/4)).

Therefore its isolated local pole term has infinite integral against t^(-5/2), while the global diagonal-subtracted pole correction has a finite integral against that same weight. This supplies a physical counterexample to the substitution, not a zero-null counterexample.

## Bounds actually available for the separate physical terms

For an actual null vector, subcritical H^s concentration gives

    ||f||_(L2(0,t))<=C_s t^s ||h||_2,  0<s<1/2.

The pole and bounded archimedean remainder therefore have local flux bounds of order t^(1/2+s), using the L1 edge bound sqrt(t)||f||_(L2(0,t)). Each actual prime profile on its translated interval has an L2 concentration bound of order t^s, including a possible opposite-endpoint profile at threshold equality. Cauchy-Schwarz gives a local prime flux budget of order t^(2s).

Neither exponent reaches 3/2; even the smooth-drive exponent is below one. This describes the insufficiency of these separate absolute budgets, not an assertion that actual combined cancellation fails.

The accepted |beta|<=3/8 input does not alter K_E, its 1/(2s) singularity, the prime profiles or p_h's exponent 1/2. Its source-side transverse remainder remains integrable as previously proved. It cannot justify the physical local/global pole substitution.

## Failed implication and remaining theorem

Failed implication: global pole translation correction O(t^2) + bounded global prime multiplier -> critically or order-3/2 integrable individual physical collar contributions. The supported cusp explicitly rejects the pole part.

The exact-zero equation still might impose a joint restriction on A_h and the Carleman edge profile. What is needed is the previously isolated signed weighted lower bound for the entire F_h, summed on the full hypothetical contact kernel. No new bound for that combined expression has been obtained.

The result closes this estimate audit only. It does not reopen the earlier inverse-moment injectivity route, infer a boundary trace for a general native null vector, or assert that the combined edge drive vanishes.

## Source custody and validation

- L2_NULL_DOMAIN_PROMOTION_20261006, blob b8ef9607e6823444a887ac71d8ec08bc21242510: exact actual exterior Euler/prime formula and pole.
- EXACT_TRANSLATION_BOUNDARY_FLUX_20261005, blob 432ffd64d6460c65cee106f0b46afdb50d1ec28a: global pole subtraction and full-null interior cancellation.
- FRACTIONAL_NULL_REGULARITY_20261005, blob f5dd2cfe71a99cd41fcfd21b01a62c2b17ce89ff: physical source and residual concentration.
- CRITICAL_DERIVATIVE_PROMOTION_20261007, blob 26627f85c34572a8197b32a1216382e8d02e07f5: supported cusp regularity.
- PROJECTED_FRACTIONAL_NULL_TEST_20261007 and SIGNED_CUTOFF_SOURCE_MOMENT_20261007: surviving complete boundary target.

Validation is analytic: endpoint substitution, Euler Taylor coefficient 1/4, supported prime shifts, pole cusp integral 4t^(5/4)/5 and weighted divergence are explicit. Existing cusp and signed-cutoff rational controls pass as regression only. No computed actual null/eigenmode, new numerical certificate, Lean build, axiom audit or CI claim. Cursor updated additively, 24/25 certification preserved. No aperture marching or historical packet work. Actual endpoint exclusion, critical promotion, F4 and FULL TRANSPORT CLOSED remain unproved.
