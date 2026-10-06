# RPB108: averaged singular channel and an inverse-moment obstruction

Base: 4078bf1ad97435e754b22d067b5c68a8ac5826be.
Definitions: docs/TERMINOLOGY_RPB108_AVERAGED_CARLEMAN.md.
Standing: analytic derivation with exact algebra controls; not Lean certified.

## Exact averaged leading-kernel identity

Let f in L2(0,L), extended by zero, and first assume f is supported in [epsilon,L] for epsilon>0. Let C_L f(u)=integral_0^L f(v)/(u+v)dv and

    S_f(t)=Re integral_0^t C_L f(u) conjugate(f(t-u))du.

Then

    integral_0^infinity S_f(t)dt/t^2
       =1/2 |integral_0^L f(v)dv/v|^2.                    (1)

To prove it, set w=t-u and apply Fubini. The kernel in the v,w pairing is

    K(w,v)=integral_0^infinity du/[(u+w)^2(u+v)].

Its real pairing is unchanged by replacing it with its symmetric part. Direct differentiation gives

    1/[(u+w)^2(u+v)]+1/[(u+v)^2(u+w)]
       =-d/du [1/((u+v)(u+w))].

Integration over u gives K(w,v)+K(v,w)=1/(vw), proving (1). Absolute Fubini follows by using |f| and the same nonnegative symmetric calculation: the absolute triple integral is at most 1/2 (integral |f(v)|dv/v)^2, finite under the support gap. More generally (1) holds whenever integral |f(v)|dv/v is finite. It is not imported unregularized for an actual edge-saturated h without that condition.

In the actual flux the coefficient is -1/2 S_f, so this leading contribution averages to -1/4 |M(f)|^2. The rank-one identity is a fact about the leading singular channel, not the full actual flux.

## Uniform tail bound localizes the identity

For fixed t0>0, the absolute tail satisfies

    |integral_t0^infinity S_f(t)dt/t^2|
       <=T_L,t0 ||f||_2^2,
    T_L,t0=pi sqrt(L)/(sqrt(3) t0^(3/2)).                 (2)

Indeed for each w>0 the squared L2 norm, as a function of u, of
1_{u+w>=t0}/(u+w)^2 equals 1/[3 max(w,t0)^3]. Cauchy-Schwarz in u, then ||f||_1<=sqrt(L)||f||_2 and the recovered Carleman bound ||C_L f||_2<=pi||f||_2, prove (2). This tail bound is uniform in a lower source cutoff epsilon. Thus the small-t average of an edge-truncated profile equals its squared inverse moment divided by two, up to a uniformly bounded tail.

## Actual bounded nonnegative sector: a conditional obstruction

Now suppose the actual full mixed weak-null profile f(v)=h(a-v) is real, nonnegative and bounded, with L=2a. These are extra hypotheses, not supplied by the parity reduction. Put U=||f||_infinity, H=||f||_2, and fix 0<t0<min(1,L). In the exact exterior dictionary write

    r_h(a+u)=-C_L f(u)/2+b_h(u),  0<u<t0.

The actual background b_h contains the pole, remainder kernel and all frozen prime translations, including threshold equality. It is bounded by a finite B. For example the recovered inequalities give |rho(s)|<=1 globally, and hence one may take

    B=[2sqrt(L)exp(a+t0/2)+sqrt(L)]H+(S_a/2)U.

The first term bounds the actual pole and remainder; the second retains every finite prime coefficient. No prime echo is discarded.

For 0<epsilon<t0 define M_epsilon=integral_epsilon^L f(v)dv/v and f_epsilon=1_[epsilon,L]f. Positivity of the Carleman kernel gives S_f>=S_fepsilon pointwise. The latter vanishes for t<epsilon because its testing profile does. Equations (1)-(2) therefore imply

    integral_epsilon^t0 S_f(t)dt/t^2
       >=M_epsilon^2/2-T_L,t0 H^2.

The actual background contribution, integrated over the same scales, has absolute value at most

    B integral_0^t0 f(w)/max(w,epsilon)dw
       <=B(U+M_epsilon).

The first inequality follows by swapping u,w with t=u+w and integrating t^(-2) from max(w,epsilon) to t0; the omitted -1/t0 term only decreases the bound. The interval w<epsilon contributes at most U. Consequently the exact actual flux obeys

    integral_epsilon^t0 F_h(t)dt/t^2
       <=-M_epsilon^2/4+(T_L,t0/2)H^2+B(U+M_epsilon).    (3)

If M_epsilon tends to infinity, the right side tends to minus infinity. The critical integral integral_0^t0 |F_h(t)|dt/t^2 is therefore infinite. Via the already proved translation criterion, the logarithmically strengthened H^(1/2) condition fails in this sector.

This is an obstruction to proving critical cancellation for a bounded nonnegative mode with divergent inverse moment. It does not exclude that mode: critical regularity is an investigative target, not a known compulsory property of an endpoint. Nor does it prove that an actual null mode has a divergent inverse moment. A sign-changing parity representative may have different cancellations and is outside this positivity argument.

## What this rules out procedurally

In this sector, merely bounding the prime/pole/remainder background cannot cancel the quadratic singular growth: its scale contribution is only linear in M_epsilon. A successful critical route would have to prove finite inverse moment, exploit sign changes outside this sector, or use another endpoint-exclusion mechanism. Compactness of the remainder and thin collars alone do not supply that information.

The exact leading-kernel identity (1) is unconditional under its stated integrability/gap conditions. The actual obstruction (3) is conditional on boundedness and nonnegativity of the actual profile. No actual-null existence, universal critical cancellation, endpoint exclusion, retained witness attachment, F4 or FULL TRANSPORT CLOSED is established. Numerical aperture remains 81/100. Lean, axioms and CI unchanged.

## Verification boundary

Pinned inputs: actual edge channels at this base, and inherited boundary scaling and translation-flux criteria. The reproducible controls verify the rational kernel symmetrization and quadratic-versus-linear comparison. They do not mechanically certify Fubini, Carleman boundedness, the actual sector hypotheses or an RH-facing exclusion theorem.
