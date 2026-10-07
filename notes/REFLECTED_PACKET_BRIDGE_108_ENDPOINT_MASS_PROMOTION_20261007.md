# RPB108: an endpoint-average criterion closes derivative promotion

Date: 2026-10-07 UTC. Recovered live head 0a1d6cd0fdc0b7f7d18ab5d103e064ef57575fd6.
Definitions: [endpoint mass and exact native action](../docs/TERMINOLOGY_RPB108_ENDPOINT_MASS_PROMOTION.md).
Category: endpoint exclusion / local derivative promotion. Analytic, not Lean-certified; no new actual arithmetic bound.

## Result

For every actual h in K_a,

    B_h(epsilon)->0  iff  h is globally H1.             (1)

Under either condition its unchanged global distributional derivative belongs to the SAME K_a. The forward implication does not assume Xcrit, a critical source moment, a pointwise normalized boundary trace, or critical regularity of a forced inverse test.

Consequently, if the finite whole-contact trace B_K(epsilon) tends to zero, differentiation is an endomorphism of K and the existing Fourier-polynomial argument forces K=0. This supplies a LOCAL sufficient endpoint theorem replacing the global source-moment premise for this route. It does not prove that actual contact vectors meet the local condition.

On an actual kernel the criterion is equivalent to the previously closed Xcrit/H1 criterion. It is a different possible arithmetic input, not evidence that the missing endpoint estimate is already true. The exact full-native equation is indispensable in the forward proof.

## 1. Actual boundedness and boundary upper bounds before any critical premise

The pole-free killed-semigroup argument of CRITICAL_RECIPROCAL_PROMOTION applies to any canonical solution q_u=f with bounded f, including f=0. Its exact right-hand side for the pole-free operator is f-p_u, bounded because u is supported L2 and the pole is a finite smooth integral operator. Time-one Duhamel gives u bounded. No positivity-preserving semigroup for the FULL pole-added form is assumed.

Now every frozen prime translate of u is bounded. The difference between m0 and one half of the logarithmic Laplacian is a bounded local mass/convolution correction on fixed compact supports; the singular kernels differ by k_reg(s)=k(s)-1/(2s), bounded near zero. The finite translations and pole are bounded forcings. The established domain equivalence and the external Theorem 1.1 therefore give, at either edge,

    |u(edge-v)|<=C_u/sqrt(log(1/v)).                  (2)

The zero extension is continuous with zero endpoint values. This reasoning applies both to h in K and to the Fredholm inverse tests below. It requires no global maximum principle for the full native form. The cited external theorem proves an upper bound and continuity, NOT existence of a normalized boundary trace.

The exact exterior action retained in the prior boundary notes is

    q_u(a+t)=-(1/2) integral_0^(2a) u(a-v)/(t+v)dv+A_u(t),

where A_u is bounded for small t: pole and regular Euler terms are bounded, and every actual finite prime term evaluates bounded u. Threshold-equality translations remain in that list. Applying (2) gives

    |q_u(edge+t)|<=C_u(1+sqrt(log(1/t))).             (3)

Both statements hold without a critical Fourier-domain premise.

## 2. A vanishing endpoint average also improves the exterior residual

Write M_h(v)=integral_0^v |h(a-t)|dt. Cauchy-Schwarz and B_h->0 imply

    M_h(v)=o(v/sqrt(log(1/v))).                     (4)

We claim that the exact Carleman profile has absolute upper bound o(sqrt(log(1/t))). Fix small delta. Its outer part is bounded. Integrate the inner part by parts against M_h:

    integral_0^delta |h(a-v)|/(t+v)dv
       =M_h(delta)/(t+delta)
           +integral_0^delta M_h(v)/(t+v)^2 dv.

There is no term at v=0 since M_h(v)->0. Given eta>0, choose delta so that M_h(v)<=eta v/sqrt(log(1/v)) below delta. The part v<t is bounded by eta/(2sqrt(log(1/t))). The part t<v<delta is at most

    eta integral_t^delta dv/[v sqrt(log(1/v))]
       <=2 eta sqrt(log(1/t)).

Terms from fixed v>=delta are bounded and vanish after division by sqrt(log(1/t)). Sending eta to zero proves the claim. The bounded actual drive thus yields

    q_h(edge+t)=o(sqrt(log(1/t))).                  (5)

This is weaker than an ordinary zero boundary limit, but sufficient for the joint reciprocal estimate below. Neither (4) nor (5) follows from the automatic upper bound (2) alone.

## 3. Exact mixed nullity retains BOTH exterior pairings

Take f in C_c^infinity(I_a) physically orthogonal to the whole finite K_a. The Fredholm inverse supplies u in D_a solving q_u=f on I_a. Do not project a smooth f onto a rough kernel and then call the result smooth. Equations (2)-(3) apply to this u.

Let phi be a fixed even smooth compact mollifier of integral one, supported in [-1,1], and h_epsilon=phi_epsilon*h. The same exact multiplier, finite translations and Hermitian translation pole commute locally with convolution and differentiation. Global reciprocity on these supported vectors gives

    <q_(h_epsilon'),u>=<h_epsilon',q_u>.            (6)

This is full actual native reciprocity. Since q_h=0 on the interior, the left side is confined to the two interior epsilon strips. Since q_u=f only on the interior, the right side has an exterior term which MUST be kept.

For the left side, ||phi_epsilon'||_infinity<=C/epsilon^2, and (2) gives integral_strip |u|<=C_u epsilon/sqrt(L_epsilon). Thus its absolute value at each edge is bounded by

    C_u/[epsilon sqrt(L_epsilon)]
                   integral_0^epsilon |q_h(edge+t)|dt=o(1),

using (5) and integral_0^epsilon sqrt(log(1/t))dt
<=epsilon*(sqrt(L_epsilon)+1/(2sqrt(L_epsilon))).

For the exterior part of the right side,

    |h_epsilon'(edge+t)|<=C epsilon^(-2) M_h(epsilon),
    integral_0^epsilon |q_u(edge+t)|dt<=C_u epsilon sqrt(L_epsilon).

Their product is o(1) by (4). These two estimates improve the previous critical proof: the inverse test's boundary decay permits q_h=o(sqrt(log)), rather than requiring q_h->0. No exterior pairing is discarded before it is bounded.

For epsilon smaller than the fixed distance of supp f from the endpoints, the remaining interior pairing tends to -<h,f'>. Equation (6) therefore proves <h,f'>=0 for every such smooth f orthogonal to K.

## 4. Finite codimension and endpoint removal without Xcrit

The annihilator of these smooth orthogonal tests is precisely the finite span of the physical kernel basis. Density makes their r constraints independent. Elementary finite-codimension linear algebra therefore identifies h'=g on I_a for some g in K_a.

Because g is L2, h agrees on I_a with an absolutely continuous primitive of g plus a constant. Its already proved continuous representative has zero values at both endpoints. Hence that primitive has zero endpoint traces. The zero extension is H1 and its global derivative is exactly g; there are no endpoint delta terms. This step uses continuity and the primitive, not a critical negative-space endpoint-removal assumption.

Conversely, a zero-extended H1 vector has zero traces and |h(edge-v)|^2<=v||h'||_2^2. Thus B_h(epsilon)<=epsilon*L_epsilon*||h'||_2^2, tending to zero. This proves (1).

The same proof works for a fixed real physical eigenspace q_h=mu h by applying reciprocity to q-mu and using the shifted Fredholm inverse. Outside the support the residual is unchanged. Its derivative stays in that SAME eigenspace. Zero normalization is not by itself what yields (1).

## 5. The unresolved improvement is genuinely critical

The automatic bound (2) gives only B_h(epsilon)=O(1). It does not give B_h->0. For the inverse-square-root-log profile, on epsilon/2<v<epsilon the normalized squared mass is bounded below by

    L_epsilon/[2(L_epsilon+log 2)],

while its upper bound is one. The ACTUAL small-window nonnegative forced inverse from ACTUAL_ROUGH_FORCED_INVERSE has a lower bound by a positive multiple of this profile, so fails the vanishing endpoint condition. That inverse has q_u=f, not q_u=0; it is not a null counterexample.

For the already constructed actual rough positive eigenmode, the shifted version of (1) implies limsup B_h>0. There is no assertion of a pointwise normalized trace or a positive liminf for that mode. Therefore this local target also fails for the actual positive-mode control, just as the critical source target does.

For a nonzero hypothetical actual full K, B_K is automatically bounded, but cannot tend to zero: otherwise (1) puts every basis vector in H1, and differentiation on finite K contradicts compact-support Fourier-polynomial independence. Thus limsup B_K>0 conditionally. No nonzero actual K or finite contact is asserted to exist.

## Smallest remaining theorem for this route

Prove B_K(epsilon)->0 on every hypothetical nonnegative actual first-contact kernel, using the unshifted arithmetic full-native equation. This would immediately exclude contact by the proof above, without further aperture marching or a global positive-source moment estimate. A generic boundary upper theorem, compact negative observations, finite kernel, or exact mass-shifted contact does not supply it.

The failed implication is actual bounded forcing plus the optimal logarithmic boundary upper bound -> a vanishing normalized endpoint average. The actual forced inverse refutes it. The route now has a proved LOCAL derivative-promotion criterion and one remaining local endpoint estimate. It belongs to endpoint exclusion; retained attachment and same-vector enlarged/null transport are unchanged.

## Source custody and audit

Pinned repository sources at the recovered head:
- CRITICAL_RECIPROCAL_PROMOTION_20261007: 9983be22ab58e926b5e15127f8feaf53d43329e0.
- ACTUAL_ROUGH_FORCED_INVERSE_20261007: 525ced5f03a8fc5dee543ada83d74a5fed8d74b0.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.
- CRITICAL_JOINT_MATCHING_20261007: 299cea4f1fe5b45b844c52a7912842f93d21dd9a.
- FRACTIONAL_NULL_REGULARITY_20261005: f5dd2cfe71a99cd41fcfd21b01a62c2b17ce89ff.

External primary source re-read: Hernandez-Santamaria, Lopez Rios and Saldana, arXiv:2401.18033v2, 3 July 2024, https://arxiv.org/html/2401.18033v2, Theorem 1.1 and Theorem 1.2. Only the already accepted bounded-solution continuity/upper theorem is used in the new promotion proof. The existing forced-inverse lower control retains its separately audited barrier custody. Neither theorem is imported as a normalized boundary-trace existence theorem; Theorem 1.2 states liminf/two-sided bounds, not that limit. Search results are not taken as an exhaustive theorem catalogue.

Analytic audit: boundedness before boundary transfer; exact finite translations and pole; averaged absolute Carleman integration; smooth forcing orthogonal BEFORE inversion; both signed reciprocal exterior terms; finite-codimension identification; continuous primitive endpoint removal; correct shifted-control scope. Companion rational checks cover logarithmic-profile mass brackets, product constants and the H1 rate, not actual nulls or the analytic theorem. No Lean build/axiom audit. Accepted beta bound 3/8 preserved but is not used to replace the physical endpoint premise. Canonical cursor updated additively. Aperture lane and historical certificates preserved. No endpoint exclusion, retained attachment, enlarged actual-null transport, RH, F4 or FULL TRANSPORT CLOSED.
