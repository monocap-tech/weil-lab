# RPB108: absolute critical collar pairing and the native-sign control

Date: 2026-10-07 UTC. Recovered live head 99b8346b238abde76730d4fcdc5b86012fdb3e01.
Definitions: [critical absolute collar product](../docs/TERMINOLOGY_RPB108_CRITICAL_ABSOLUTE_COLLAR.md).
Category: critical derivative promotion / endpoint exclusion.

## Result and its exact strength

For every actual h in K_a intersect Xcrit, and sufficiently small t0,

    integral_0^t0 integral_0^t
      |r_h(a+u) conjugate(h(a-(t-u)))|du dt/t^2
       <=(1+2 log 2) H_r H_f < infinity.                 (1)

The entire residual r_h=A_h-(1/2)Cf is retained before taking absolute value. No separate prime/pole/Carleman absolute budgets are asserted. Reflection gives the left endpoint version.

This closes absolute integrability of the physical collar product under the already assumed critical membership. It strengthens the integrability of the real integrated flux, which was already equivalent to critical membership by the exact native identity. It does NOT prove that membership, a new positive-source moment, or an L2 derivative. The estimate is a consequence, not a new arithmetic input.

The previous constant-drive cusp is excluded by a necessary native flux sign. A modified comparison drive obeys that sign and all the boundary-profile budgets used in (1), while still failing derivative regularity and the order-3/2 flux integral. It is explicitly not an actual native drive or null solution. Thus adding the available one-sided native sign to the profile estimates does not close the gate.

## 1. The two actual Hardy budgets fit the same positive kernel

The pinned joint matching theorem proves

    H_f^2=integral_0^delta |f(v)|^2 L(v)/v dv<infinity,
    H_r^2=integral_0^delta |r(u)|^2/[u L(u)]du<infinity,

where L(x)=log(1/x). The second estimate uses the exact zero interior residual; generic continuity alone does not give it.

By Tonelli, the left side of (1) is

    integral_(u>0,v>0,u+v<t0) |r(u) f(v)|/(u+v)^2 du dv.

Enlarge this triangle to (0,delta)^2. Write

    R(u)=|r(u)|/sqrt(u L(u)),
    V(v)=|f(v)|sqrt(L(v)/v).

Their L2 norms are H_r and H_f. The resulting positive kernel is

    K(u,v)=sqrt(u v)/(u+v)^2 sqrt(L(u)/L(v)).

For u,v<delta<exp(-4),

    sqrt(L(u)/L(v))<=1+|log(u/v)|.

If u>=v, the left side is <=1. If u<v, its square is 1+log(v/u)/L(v), and L(v)>4, so the displayed bound follows. The same bound applies after interchanging u,v.

Use Schur weight p(u)=u^(-1/2). The row and column integrals of the symmetric majorant, divided by their respective p, are bounded by

    C=integral_0^infinity [1+|log x|]/(1+x)^2 dx
     =1+2 log 2.

Indeed the row substitution is v=u x and the column substitution is u=v x; enlarging their finite domains to the positive half-line only increases the bounds. Splitting at one and substituting x->1/x shows the two log integrals equal; integration by parts gives each log integral log 2. Weighted Cauchy-Schwarz, or the positive-kernel Schur test first on truncated intervals followed by monotone convergence, proves operator norm <=C. This proves (1).

No pointwise bound on r, absolute inverse-moment convergence, or critical support-projection bound is used. The estimate controls the product with the complete residual even when neither separated profile has an admissible absolute budget.

## 2. Native sign audits the old comparison rather than proving promotion

The exact full-null translation identity remains

    F_h(t)=-D_m(t)+(cosh(t/2)-1)Ppole(h),
    D_m(t)>=D_w(t)/2-Zcore t^2 ||h||_2^2.

It implies F_h(t)<=Z t^2 ||h||_2^2, with Z finite at the fixed aperture. No lower bound on F_h is obtained from this statement.

For the previous comparison f(v)=v^alpha chi(v), alpha=1/4, choose nonnegative smooth chi supported strictly below 2a and equal to one near zero. Let M=integral f(v)/v dv. With independent drive A^cmp_0=M/2,

    r^cmp_0(u)=(M-Cf(u))/2
             =(u/2) integral f(v)/[v(u+v)]dv,
    r^cmp_0(u)/u^alpha -> c_alpha
       =(1/2) integral_0^infinity y^(alpha-1)/(1+y)dy>0.

Scaling v=u y and domination by y^(alpha-1)/(1+y) prove the limit. Hence its real flux has the asymptotic

    F^cmp_0(t)~c_alpha B(alpha+1,alpha+1)t^(2alpha+1)>0.

Since 2alpha+1=3/2<2, this comparison violates the necessary native upper bound F<=O(t^2). It remains a valid counterexample to profile matching alone, exactly as previously stated; it was never an actual native null solution. This additional audit prevents it being used as a control satisfying all native necessary conditions.

## 3. A refined comparison keeps the necessary sign but still has no derivative

On a sufficiently short collar instead assign the independent continuous drive

    A^cmp_-(u)=M/2-u^alpha log(1/u),  alpha=1/4.

It can be extended continuously away from the collar. It has the same limiting value M/2, and its difference from that value is O(1/log(1/u)), indeed smaller than every inverse logarithmic power. Its residual is

    r^cmp_-(u)=r^cmp_0(u)-u^alpha log(1/u).

Both Hardy budgets are finite: near zero their respective integrands are bounded by constants times v^(2alpha-1)log(1/v) and u^(2alpha-1)log(1/u). The drive difference has the required squared norm with weight 1/[u log(1/u)]. The ordinary signed inverse moment and Carleman limit both equal M. The physical cusp is in Xcrit, is continuous with zero endpoint value, is smooth on every strictly interior compact set, and satisfies the previously available logarithmic boundary upper estimate. Nonetheless its physical derivative is not L2, since integral_0 v^(2alpha-2)dv diverges.

For t small enough f(t-u)=(t-u)^alpha. Substituting u=t x gives

    F^cmp_-(t)
       =-B(alpha+1,alpha+1)t^(2alpha+1)log(1/t)
          +O(t^(2alpha+1)).                             (2)

The integral containing log(1/x) is finite, and the r^cmp_0 term is O(t^(2alpha+1)); these justify the remainder. Thus the flux is negative for all sufficiently small t, and satisfies the necessary native upper sign bound. Equation (1) still applies to these comparison budgets.

At the critical weight t^(-2), its absolute flux integral is finite. At the order-3/2 weight t^(-5/2), (2) instead gives a negative signed integral with leading growth

    -(1/2)B(5/4,5/4) log^2(1/epsilon)+O(log(1/epsilon))

as epsilon decreases to zero; the absolute integral diverges as well. The exponent and sign are exact, not an inferred actual source moment.

This comparison retains the full-profile matching, the proved weighted budgets, the drive modulus, the necessary one-sided native flux sign and the absence of an endpoint delta. It discards the actual interior equation, the actual prime/pole/regular-Euler definition of A_h, and the full exact source/symbol identity. It is therefore NOT a counterexample to K_a intersect Xcrit -> H1. No assertion that its independently assigned drive can be realized arithmetically is made.

## 4. The unresolved step is still a homogeneous theorem

Failed implication: critical physical/residual Hardy budgets + matched ordinary boundary limit + continuous drive with the proved modulus + necessary native flux sign -> L2 derivative or order-3/2 integrated flux. The refined comparison rejects this implication. The original constant-drive control alone did not test the added native sign.

The smallest remaining homogeneous gate is unchanged:

    h in actual K_a intersect Xcrit -> h' in global L2.

Its proof must use the actual interior/source compatibility beyond the boundary properties audited here. Supported-L2 null-domain promotion then puts that same derivative in D_a and K_a. Whole-contact-kernel critical membership is an additional, still unproved hypothesis needed to iterate and contradict finite dimension. Alternatively, the already isolated finite-liminf order-3/2 signed trace on the whole contact kernel bypasses the critical gate, but is also unproved.

The external |beta_rho|<=3/8 theorem remains an accepted pinned input. It controls the integrable transverse source remainder; it neither supplies H_f independently of critical membership nor changes the t^(-2) threshold of (1). Positive-eigenmode controls retain their original scope: the actual rough forced inverse fails critical membership; the actual rough positive eigenmode fails supercritical moments, with its critical moment undecided. A hypothetical critical positive eigenmode can satisfy the same exterior Hardy reasoning after mass subtraction. This pass supplies no estimate separating every such mode by zero normalization alone.

Category: endpoint exclusion / critical derivative promotion, not retained attachment or null transport. The physical vector has not been dilated, enlarged or replaced. No historical packet identification, same-vector enlarged full-nullity, global domination, RH, F4 or FULL TRANSPORT CLOSED claim.

## Custody and validation

Pinned at the recovered live head:

- CRITICAL_JOINT_MATCHING_20261007, blob 299cea4f1fe5b45b844c52a7912842f93d21dd9a: both Hardy budgets and signed boundary matching.
- EXACT_TRANSLATION_BOUNDARY_FLUX_20261005, blob 432ffd64d6460c65cee106f0b46afdb50d1ec28a: native sign and critical flux/source equivalence.
- SIGNED_CUTOFF_SOURCE_MOMENT_20261007, blob 52f34cc5c348c7ad5b00058c1208599f531bf4c7: supercritical trace and promotion implications.
- EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007, blob c369d3760606d9e5b9ae0f4862156fd712e5be29: accepted external strip input and source remainder.

Proof validation is analytic: Tonelli, the explicit Schur rows/columns, comparison scaling and cutoff divergence. Documentation/source checks validate scope and custody only. No numerical inverse, new external theorem, Lean build, axiom audit or arithmetic certificate is claimed. Historical wording and certificates remain intact. The certified 24/25 whole-domain frontier and newer 97/100 aperture milestone are preserved.

## Publication recovery addendum

GitHub writes recovered after the original pass. The live branch advanced to 200ba143265914d8fc6d03b81f14bc95a9232a20, which certifies whole-domain positivity through 97/100 with Q>=9e-30 physical mass and Q>=4e-32 Elog. This publication preserves that newer cursor and all aperture files. The recovered research head and historical frontier statements above record the original pass; no reset or aperture recomputation is made.
