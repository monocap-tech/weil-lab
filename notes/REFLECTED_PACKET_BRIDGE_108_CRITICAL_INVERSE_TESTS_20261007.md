# RPB108: critical inverse tests would promote the exact native derivative

Date: 2026-10-07 UTC. Recovered live head f0c609147d67201476eb1cc82c74e3c97585e336.
Definitions: [critical inverse tests](../docs/TERMINOLOGY_RPB108_CRITICAL_INVERSE_TESTS.md).
Category: endpoint exclusion / critical derivative promotion.
Conditional analytic implication; the critical inverse-test premise is unproved.

## Outcome

The critical distributional gate can be attacked through the actual Fredholm inverse without requiring a bounded support projection on a general critical space:

    critical inverse-test premise
        -> every supported Zcrit solution of the exact native equation
           is the same distribution as an element of K_a
        -> K_a intersect Xcrit has global derivative in L2.

This is a sufficient criterion, not an equivalence or a proved estimate on actual inverse tests. The existing Fredholm theorem supplies tests u in D_a; the missing part is their Xcrit regularity.

The proof avoids projecting an arbitrary critical distribution. It uses global multiplier duality and approximates an already exterior-supported critical-dual function by exterior tests. The whole-kernel order-one source bound is still independently required to turn this derivative gate into contact exclusion.

## 1. The correct critical weights

Use r=1+|xi| and w=log(e+|xi|). The spaces have squared Fourier weights

| Space | Weight | Role |
| --- | --- | --- |
| Xcrit | r w | inverse tests and critical physical vectors |
| Zcrit | w/r | critical derivative distributions |
| Ecrit | r/w | dual of Zcrit |
| Zlow | 1/(r w) | dual of Xcrit |

The actual multiplier satisfies |m_a(xi)|<=C_a w(xi), because the quarter-line symbol has logarithmic growth and the frozen prime sum is bounded. Consequently m_a(D):Zcrit->Zlow and m_a(D):Xcrit->Ecrit are bounded. Finite prime translations preserve all four spaces. Compactly localized smooth pole profiles belong to all the positive spaces.

Thus a critical distribution g can be tested against u in Xcrit in the differentiated equation, and the flipped pairing <g,m_a(D)u> is continuous in Ecrit. Neither pairing follows merely from u in all H^s, s<1/2.

## 2. Lawful inverse tests

Fix f in C_c^infinity(-a,a) with <f,k>_2=0 for every k in K_a. The actual self-adjoint I+compact form Fredholm theorem already gives u in D_a with

    Q_a(u,v)=<f,v>_2,  v in D_a.

Its uniqueness is only modulo K_a. Assume the critical inverse-test premise provides such a u in Xcrit. No coercive inverse of the singular whole form is taken.

Using f itself avoids subtracting Pi_K f from an arbitrary smooth function. That subtraction would introduce kernel regularity into the forcing at the critical threshold. Smooth functions satisfying the finitely many physical orthogonality constraints suffice for the distributional conclusion below.

## 3. Interior testing without critical projection

Let g be supported in [-a,a], belong to Zcrit, and solve m_a(D)g+p_g=0 on (-a,a). Then m_a(D)g belongs to Zlow. Choose a compact smooth cutoff equal to one on a neighborhood of [-a,a] to localize the pole term.

Every supported u in Xcrit can be approximated in Xcrit by C_c^infinity(-a,a). Explicitly shrink its support by a dilation with factor tending to one and then mollify within the support margin. Dilation is strongly continuous in this weighted Fourier norm: it is uniformly bounded for factors near one by comparability of r w at scaled frequencies, and continuity first holds on Schwartz functions, which are dense. Mollification converges by dominated Fourier convergence. These are approximating tests, not a change of the g being promoted.

The distributional interior equation and Zlow/Xcrit continuity therefore give

    <m_a(D)g,u>+<p_g,u>=0.

The frozen multiplier is real and the compact-distribution pole moments obey the same Hermitian rank-two identity as in subcritical promotion. Flipping the pairings yields

    <g,m_a(D)u+p_u>=0.

All pairings are localized where necessary; no globally growing exponential is assigned a Fourier Hilbert norm.

## 4. Removing the exterior term by its actual support

For the regular inverse test, q_u=m_a(D)u+p_u equals f on the interior by its form equation and compact interior testing. Let chi be compact smooth and equal to one near [-a,a], and set

    v=chi q_u-f.

Since u is in Xcrit, v belongs to Ecrit. It vanishes on (-a,a). Split v into its left and right exterior parts using a smooth partition whose transition lies strictly inside that interval. Multiplication by these smooth cutoffs preserves Ecrit; this follows from the polynomially moderate Fourier weight and the rapidly decaying convolution kernel.

Translate each part outward by a distance delta>0. Strong translation continuity in Ecrit brings these translated parts back to v as delta decreases to zero. Each translated part can be mollified within half its separation from [-a,a], giving smooth tests disjoint from the support of g. Their pairings with g are zero. Ecrit/Zcrit continuity then gives

    <g,v>=0.

This uses density for a function already supported on the exterior, not boundedness of multiplication by 1_[-a,a] on Ecrit. Combining with step 3 gives <g,f>=0 for every smooth f physically orthogonal to K_a.

## 5. Recovering the same L2 kernel distribution

Let e_1,...,e_d be a physical L2 orthonormal basis of K_a. The map from interior smooth functions to their d pairings with the e_j is surjective: otherwise a nonzero linear combination of the e_j would vanish as a distribution on the interior, hence vanish in L2, contradicting independence.

Choose interior smooth functions biorthogonal to these d functionals. An arbitrary interior smooth f can then be decomposed into a function annihilating K_a plus its finite biorthogonal correction. Step 4 shows that g on the interior is a fixed linear combination of e_j. This is a distributional identity and does not assume g has an L2 norm.

The difference is supported at the two endpoints and belongs to Zcrit, since L2 is contained in Zcrit. No nonzero finite-point-supported distribution belongs to Zcrit: even a delta has squared Fourier tail integral w/r, which diverges, and derivatives are worse; distinct endpoint phases cannot cancel their diagonal leading mean. Thus the difference is zero globally.

Therefore g is the same L2 distribution as an element of K_a. Apply this to g=h' for h in K_a intersect Xcrit. The already established exact differentiated multiplier/pole equation and support give the critical derivative promotion conclusion. If the entire K_a also has critical source moment finiteness, differentiation becomes an endomorphism and the existing finite-dimensional derivative-chain contradiction excludes it.

## 6. Why the existing estimates do not prove the premise

The subcritical inverse tests obey the earlier capped-weight argument for each fixed s<1/2. Its operator budgets grow like (1/2-s)^(-2) and its absorption threshold grows exponentially in that budget. Those estimates give no Xcrit limit.

The cutoff pole also demonstrates the exact dual threshold. For a smooth b with nonzero endpoint values, the zero extension P_a b has leading Fourier tail

    [b(-a)exp(2pi i a xi)-b(a)exp(-2pi i a xi)]/(2pi i xi).

Its Ecrit norm has a divergent diagonal contribution proportional to

    integral^R dxi/(xi log xi)=log log R+constant.

The cross phase is integrable by integration by parts, and the smoother remainder contributes a finite amount. Thus P_a b need not even belong to Ecrit, although it belongs to every H^s below one half and every finite logarithmic L2 order. In Xcrit the divergence is stronger. This is a cutoff-profile control, not an actual null or inverse test. It prevents obtaining the premise by assigning critical norms separately to the cutoff pole and commutator terms.

A further logarithmic loss changes this jump integral to integral dxi/(xi log^(1+delta)xi), which converges for delta>0, but the resulting weaker positive space is not the exact dual of Zcrit. No such loss repairs the pairing with the given critical derivative without an additional estimate. The combined native equation must supply the needed inverse-test regularity.

The accepted |beta_rho|<=3/8 source bound changes neither these weights nor the quarter-line/pole/cutoff geometry. The exact zero equation is essential in step 3. A positive eigenmode has a nonzero mass term there, so the argument cannot silently rename it as a native null solution. The existing positive-eigenmode controls have not established or refuted critical Xcrit regularity for these forced tests.

## Remaining theorem and standing

The sufficient new research target is: at an actual nonnegative window, every smooth interior forcing orthogonal to its full native kernel has some supported Fredholm solution in Xcrit. Proving this would close critical derivative promotion, without claiming a bounded general critical support projection or an injective scalar boundary observation.

That target remains unproved; its necessity is not asserted. The minimal gate remains K_a intersect Xcrit -> L2 derivative. Inverse-test regularity is a stronger sufficient route to investigate, not a claim that the minimal gate has been replaced by an equivalent one. No actual critical source trace bound is obtained, so endpoint exclusion is not closed even conditionally on this gate alone. The order-3/2 signed-trace alternative and its audited global strength remain unchanged.

The argument is an analytic conditional proof: critical dual weights, supported test approximation, exterior approximation, finite-codimension recovery and endpoint-defect removal are explicit. No new numerical estimate or Lean validation is claimed. Historical packet attachment and enlarged same-vector null transport are unchanged. The newer 97/100 method obstruction is preserved; certified whole-domain positivity remains 24/25. F4 and FULL TRANSPORT CLOSED remain unproved.

## Source custody

See the accompanying manifest for exact path/blob custody at the recovered head. Load-bearing sources are the critical derivative registry/audit, subcritical distributional promotion, logarithmic multiplier bootstrap, fractional forced-test regularity, the accepted external-strip audit and the signed-target strength audit.

- docs/TERMINOLOGY_RPB108_CRITICAL_DERIVATIVE_PROMOTION.md, blob 8db486559673d4f3b94448800e9d08fe41ea3633.
- docs/TERMINOLOGY_RPB108_SUBCRITICAL_DISTRIBUTIONAL_PROMOTION.md, blob 9774bce09e97c8b627371591cb971572f1a64aec.
- notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_DERIVATIVE_PROMOTION_20261007.md, blob 26627f85c34572a8197b32a1216382e8d02e07f5.
- notes/REFLECTED_PACKET_BRIDGE_108_SUBCRITICAL_DISTRIBUTIONAL_PROMOTION_20261007.md, blob 665a473edee975b2d346d0511a292e4a64cb56e8.
- notes/REFLECTED_PACKET_BRIDGE_108_LOGARITHMIC_BOOTSTRAP_20261005.md, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028.
- notes/REFLECTED_PACKET_BRIDGE_108_FRACTIONAL_NULL_REGULARITY_20261005.md, blob f5dd2cfe71a99cd41fcfd21b01a62c2b17ce89ff.
- notes/REFLECTED_PACKET_BRIDGE_108_EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007.md, blob c369d3760606d9e5b9ae0f4862156fd712e5be29.
- notes/REFLECTED_PACKET_BRIDGE_108_SIGNED_TARGET_GLOBAL_STRENGTH_20261007.md, blob 05366bb0939a5bec0962f1e53b0a81b623ecfc4e.
