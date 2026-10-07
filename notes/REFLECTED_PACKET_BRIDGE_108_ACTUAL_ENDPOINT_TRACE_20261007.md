# RPB108: actual averaged traces and a rank-one rough kernel quotient

Date: 2026-10-07 UTC. Recovered head 427493abacb293065fc7abd631b2e0afbd9d2740.
Definitions: [actual averaged endpoint traces](../docs/TERMINOLOGY_RPB108_ACTUAL_ENDPOINT_TRACE.md).
Category: global endpoint / actual boundary observation. Analytic, not Lean-certified.

## Result

At each fixed actual window, every h in the FULL mixed-null K has linear averaged traces kappa_R(h), kappa_L(h). They satisfy

    H_R(L)=kappa_R(h)/sqrt(L)+O_h(1/L),
    J_R(L)=2kappa_R(h)sqrt(L)+O_h(1),
    q_h(a+t)=-kappa_R(h)sqrt(log(1/t))+O_h(1).          (1)

Moreover the full rescaled physical profiles converge STRONGLY:

    sqrt(L_epsilon)h(a-epsilon t)->kappa_R(h)
                                      in L2(0,1).    (2)

Reflection supplies the left equations. Thus the normalized endpoint MASS actually has a limit, not just upper/lower bounds:

    B_h(epsilon)->|kappa_R(h)|^2+|kappa_L(h)|^2.       (3)

Reciprocity for TWO actual null vectors then yields

    kappa_R^*kappa_R=kappa_L^*kappa_L on K.            (4)

Consequently K_reg is the common zero-trace subspace. If K is nonzero, its rough quotient K/K_reg has dimension exactly ONE. The traces are not asserted to be injective on K itself or on the general physical carrier.

The remaining local endpoint theorem can now be stated without a subsequence: prove kappa_R vanishes on the WHOLE hypothetical nonnegative actual first-contact kernel. Equation (4) then kills the left trace too; (3) and the closed derivative-chain argument imply K=0. The actual arithmetic vanishing of this functional remains unproved. These are structural trace/quotient results, not contact exclusion or F4.

## 1. Exact strip matching makes the averaged trace exist

Write F_h(L)=h(a-exp(-L)). The canonical strip law proved in NF26 is

    J(L)=2L H(L)+r(L), |r(L)|<=C_h.

Here H(L)=integral_L^infinity exp(L-s)F_h(s)ds, and J'=F_h almost everywhere. The actual bounded continuous h makes these identities locally absolutely continuous. Differentiating ONLY the exact integral definitions gives H'=H-F_h; no derivative or limit of the bounded r is assumed.

Put V=J+H. Then V'=H and V=(2L+1)H+r. Therefore

    d/dL [V(L)/sqrt(2L+1)]
          =-r(L)/(2L+1)^(3/2).                      (5)

The right side is integrable at infinity. The bracket has a finite limit w, with error O_h(L^(-1/2)). Set kappa=w/sqrt(2). Solving the two algebraic equations yields H=kappa/sqrt(L)+O_h(1/L) and J=2kappa sqrt(L)+O_h(1). The exterior Carleman estimate from NF26 gives the last line of (1). Thus trace existence follows from the exact FULL equation's bounded strip remainder, not from a generic boundary theorem.

The trace is linear because each finite H is linear and its limit exists. The accepted boundary upper bound also bounds this functional on the finite physical kernel. No pointwise normalized interior trace is imported from an external theorem.

## 2. A second lawful null test controls the squared profile

Let g_epsilon=1_(a-epsilon,a)h, and h_out=h-g_epsilon. These are canonical tests: actual h has H^s regularity for every s<1/2, and sharp interval multiplication is bounded on each such H^s. The resulting positive fractional norm dominates the logarithmic domain norm. Hence full mixed nullity gives

    Q(g_epsilon)=-Q(h_out,g_epsilon).                (6)

For completeness, the needed lower bound is independent of any new aperture certificate. A function g supported in an interval of length epsilon satisfies |ghat(xi)|^2<=epsilon||g||_2^2 in the canonical unitary Fourier convention. Consequently its Fourier mass in |xi|<=R is at most 2R epsilon||g||_2^2. Layer-cake up to L_epsilon gives

    Elog(g)>=integral_0^(L_epsilon)
                           mass_(|xi|>exp(t))dt
             >=(L_epsilon-2)||g||_2^2.

The existing actual envelope m0>=log(e+|xi|)-C0 then gives the same lower bound with C0 added. For epsilon<log 2, every nonzero frozen prime shift has disjoint support from g itself, so its diagonal pairing is EXACTLY zero. The physical +2cosh pole has absolute norm bound 3epsilon on that short interval. Thus

    Q(g_epsilon)>=(L_epsilon-C)||g_epsilon||_2^2,     (7)

with fixed C. This is a structural short-strip bound, not a larger-aperture stress test.

Inside the strip, the archimedean cross action from h_out is

    -integral_epsilon^(2a) k(y-v)f_R(y)dy,
                                           0<v<epsilon.

Its leading signed forcing is -(1/2)J_R(epsilon). All remaining prime and pole cross terms are bounded, since h_out is bounded. The difference of the singular cross integral from (1/2)J has pointwise bound

    C_h[1+(1+|log(1-v/epsilon)|)/sqrt(L_epsilon)].

Indeed, on epsilon<y<2epsilon the logarithm at y=v is integrable, with h bounded by C_h/sqrt(L_epsilon-log 2). On 2epsilon<y<sqrt(epsilon), the difference 1/(y-v)-1/y is at most 2epsilon/y^2 and the boundary bound applies with L/2. Above sqrt(epsilon) use bounded h. The regular-kernel correction is bounded. Hence its L2 strip norm is at most C_h sqrt(epsilon).

Equation (6) therefore reads

    Q(g_epsilon)=(1/2)J_R(epsilon)
                   conjugate(integral_0^epsilon f_R(v)dv)
                    +E_epsilon,
    |E_epsilon|<=C_h sqrt(epsilon)||g_epsilon||_2.   (8)

If complex pairings are used, take real parts of the displayed equality. The fixed factors and signs retain the actual off-diagonal kernel; no absolute value is substituted into J.

The already proved boundary upper bound gives ||g_epsilon||_2<=C_h sqrt(epsilon/L). Inserting (1) into (8), then applying (7), proves

    limsup (L/epsilon)||g_epsilon||_2^2<=|kappa_R|^2.

Cauchy-Schwarz applied to its signed mean gives the reverse liminf, because sqrt(L)H(L)->kappa_R. Thus the normalized mass converges to |kappa_R|^2. Combining convergence of its mean and squared norm proves (2). The same estimates give squared L2 profile error O_h(L^(-1/2)); no pointwise convergence of h sqrt(log) is claimed. This completes (3).

## 3. Two actual null vectors force a balanced boundary Gram form

Take h,u in the same K and the fixed even compact mollifier phi from the prior reciprocal proofs, of integral one. Exact native reciprocity still gives

    <q_(h_epsilon'),u>=<h_epsilon',q_u>.             (9)

Both native actions vanish on the physical interior. The left pairing is confined to the two interior epsilon strips; the right to the exterior strips.

Equation (1) implies q_h(a+epsilon t)/sqrt(L_epsilon)->-kappa_R(h) in L2(0,1): the difference between sqrt(L+log(1/t))/sqrt(L) and one is dominated using the integrable logarithm in t, and the O_h(1) remainder is uniform for small arguments. Equation (2) supplies the interior physical profile. Convolution with the smooth phi' therefore gives, at the right edge,

    epsilon q_(h_epsilon')(a-epsilon s)/sqrt(L)
                    ->-kappa_R(h)phi(s),
    epsilon sqrt(L)h_epsilon'(a+epsilon t)
                    ->-kappa_R(h)phi(t).

These convergences are in L2 on the relevant unit strips. Since the even mollifier has integral 1/2 on (0,1), the right-edge contributions in (9) tend respectively to

    -(1/2)kappa_R(h)conj(kappa_R(u)),
    +(1/2)kappa_R(h)conj(kappa_R(u)).

At the left edge the derivative orientation reverses; the corresponding limits are +1/2 and -1/2 times the left trace product. Equality in (9) proves (4). BOTH exterior terms are essential. Zero physical endpoint values do not make these renormalized boundary products disappear.

The proof uses h,u both full-native nulls on the same window. It is not obtained from a retained selected witness, effective-background equation or a general carrier norm. The comparison mass-shifted eigenspace obeys the analogous identity for q-mu with unchanged exterior action.

## 4. What the rank-one observation does and does not imply

By (3) and the closed endpoint derivative criterion,

    K_reg=ker(kappa_R,kappa_L).

Equality of the rank-one Gram forms in (4) implies that either both functionals vanish or kappa_L=omega kappa_R for one fixed |omega|=1 on K. If both vanish, the whole K is H1 and its derivative endomorphism forces K=0. Therefore for a nonzero hypothetical K, the trace is nonzero and the regular subspace has codimension one. This proves the stated rough quotient dimension.

The actual native form is reflection invariant. Applying reflection to the proportionality twice shows omega^2=1, so omega=+1 or -1; the one-dimensional rough quotient has one definite reflection parity. This does not bound the TOTAL dimension of K or remove its possible regular derivative chains.

Most importantly, kappa_R(h)=0 for ONE actual h only implies that h is H1 and h' belongs to K. In a higher-dimensional kernel it need not imply h=0. The earlier noninjectivity audit of a single inverse-boundary moment on the general carrier is preserved. This new trace is a different, renormalized observation, with a proved kernel-specific quotient statement; no general scalar injectivity is asserted.

## Remaining endpoint theorem and controls

The local endpoint-exclusion gate is now kappa_R|_K=0 at every hypothetical nonnegative unshifted actual first contact. It is exactly the whole-kernel condition, not an existential vector with zero trace. Balance kills kappa_L, and (3) supplies the previously missing normalized-mass vanishing needed for the derivative-chain contradiction.

All trace-existence, mass-convergence and balance arguments extend to any fixed real physical eigenspace by using Q-mu mass. Its short-strip lower bound merely changes C in (7); the strip remainder in (5) stays bounded. The ACTUAL rough positive eigenmode consequently has nonzero trace and a positive normalized mass limit. The mass-shift first-contact control has the same property. Thus the exact trace architecture and nonnegative comparison contact do not prove trace vanishing. An unshifted arithmetic estimate is still required.

The profile c/sqrt(log(1/v)) has trace c and satisfies the leading strip equation; it remains a control for why the logarithmic boundary upper bound cannot make the trace zero. No nonzero actual null/contact is constructed. Accepted |beta|<=3/8 remains in force but does not alter this physical logarithmic singularity.

This pass closes actual averaged trace existence, strong scaled mass convergence, and a rank-one rough quotient. It does NOT close arithmetic trace vanishing, endpoint exclusion, historical retained attachment or same-vector enlarged/null transport. No aperture marching or replacement of the physical kernel by a selected packet.

## Source custody and validation

Pinned repository inputs at 427493abacb293065fc7abd631b2e0afbd9d2740:
- ENDPOINT_STRIP_MATCHING_20261007: 3ba5f3a36fde17ce90d58dfcede20b93b07778e8.
- ENDPOINT_MASS_PROMOTION_20261007: 6bae812597a46f52e110ecea4a150cfa7c369d80.
- FRACTIONAL_NULL_REGULARITY_20261005: f5dd2cfe71a99cd41fcfd21b01a62c2b17ce89ff.
- CRITICAL_RECIPROCAL_PROMOTION_20261007: 9983be22ab58e926b5e15127f8feaf53d43329e0.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.
- CRITICAL_MASS_SHIFT_CONTACT_20261007: 228069a79d0a987ef3651a926b0aaf797dd7541b.

No new external theorem imported. Existing versioned boundary upper theorem, semigroup transfer, Fourier convention, native envelope, and full mixed-domain custody are inherited explicitly. Analytic audit checks integrable bounded-remainder ODE without differentiating r; actual strip restriction domain; layer-cake coercivity; disjoint prime diagonal versus retained cross terms; correct positive pole norm; singular cross remainder in L2; mean/norm convergence; both reciprocal edge signs; quotient versus total-kernel distinction; and shifted controls. Companion rational/algebraic checks audit ODE integrating factors, coercivity mass budgets, balanced Gram signs and quotient controls, not actual zeros or the infinite-dimensional theorem. No Lean executable/build/axiom audit. Canonical cursor updated additively; historical certificates and concurrent aperture work preserved. No RH, F4 or FULL TRANSPORT CLOSED.
