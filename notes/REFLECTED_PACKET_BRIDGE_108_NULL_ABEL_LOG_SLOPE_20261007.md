# RPB108: exact null correlation fixes the Abel logarithmic slope

Date: 2026-10-07 UTC. Recovered live head ceb1c43f24a22d66d8bf7c409f6c08b79e2fd99e.
Definitions: [null Abel logarithmic slope](../docs/TERMINOLOGY_RPB108_NULL_ABEL_LOG_SLOPE.md).
Category: endpoint exclusion / sharper actual arithmetic target. Analytic, not Lean-certified.

## Result

The exact FULL-native null equation and established averaged endpoint traces give, for h,u in the SAME actual kernel,

    Q(h,tau_t u)/t -> -kappa_R(h) conjugate(kappa_R(u)), t down to 0.

The translated vector is a lawful test in a fixed enlarged support. It is not assumed to be null there. Actual divisor pair translation then gives

    E_h(t)/t -> |kappa_R(h)|^2,
    A_tau(h)/log(1/tau) -> (2/pi)|kappa_R(h)|^2.

The critical translation-cutoff quantity likewise satisfies I_(epsilon,1)(h)/log(1/epsilon)->|kappa_R(h)|^2, with its historical normalization unchanged.

Thus the logarithmically normalized whole-kernel Abel form has exactly the rank-one boundary Gram limit, and

    A_tau^K/log(1/tau) -> (2/pi) Lambda_K.

A nonzero hypothetical kernel has Lambda_K>0 by the proved regularity/derivative obstruction. Consequently it suffices to prove the weaker actual arithmetic estimate

    liminf_(tau down to 0) A_tau^K/log(1/tau)<=0.

A uniform one-sided SUBLOGARITHMIC sharp-head upper bound implies that estimate. Neither arithmetic bound is established here. This improves the target from bounded Abel/sharp sums to their leading logarithmic coefficient; it does not exclude actual contact.

## 1. Exterior overlap and full mixed-null custody

Fix t0>0 small and a larger finite b with a+t0<b. The actual global form/action pairing on compact supported canonical vectors is compatible with support restriction. For t in (0,t0), h and tau_t u belong to D_b. On the ORIGINAL interior, q_h=0. Since tau_t u has no support left of -a, the whole pairing reduces to one right exterior strip:

    Q(h,tau_t u)=integral_0^t q_h(a+v) conjugate(u(a-(t-v)))dv.

The established exterior action is locally integrable and has logarithmic growth. The physical vector u is bounded; the displayed pairing is absolutely defined. To identify it with the canonical form, approximate the translated vector by convolution in D_b. The convolutions are uniformly physically bounded and converge pointwise because u is continuous; q_h is integrable on their common compact support. Form convergence and dominated convergence agree. No unproved enlarged nullity is used.

Let L=log(1/t). The pinned trace theorem gives in L2(0,1)

    q_h(a+t s)/sqrt(L) -> -kappa_R(h),
    sqrt(L)u(a-t(1-s)) -> kappa_R(u).

For the first limit use q_h(a+v)=-kappa_R(h)sqrt(log(1/v))+O(1); the logarithm in s is integrable. For the second use the proved STRONG rescaled physical trace, with the measure-preserving reflection s->1-s. Cauchy-Schwarz passes to the product integral and proves the correlation limit. No pointwise normalized physical trace is required.

The convergence is uniform on bounded sets of finite K by expansion in a fixed basis. For left translations reflection gives the left boundary Gram; the proved balanced Gram makes its coefficient equal to the right coefficient. This remains a full-native kernel-specific statement.

## 2. Actual complete pair translation retains only a lower-order transverse error

The complete actual source identity already proved in the signed-cutoff note is

    Q(h)-Re Q(h,tau_t h)=E_h(t)-R_h(t).

Actual Q(h)=0, so E_h(t)=-Re C_t(h,h)+R_h(t). For the accepted B=3/8 and any derived subcritical source moment 0<s<1/2,

    |R_h(t)|<=exp(Bt)[B^2 V_h t^2/2
                 +2B t^(1+2s) sqrt(M_(+,s) M_(-,s))].

In particular R_h(t)=o(t), and the correlation limit proves E_h(t)/t=|kappa_R(h)|^2+o(1). The sharper transverse bound is retained, but bounded beta would already make the error lower order. This is not a new critical positive-source moment estimate: the nonzero boundary coefficient survives the joint cancellation.

One can also prove R=o(t) directly from base l2 sampling and dominated convergence of the sine cross term. The displayed derived-moment estimate is kept for explicit custody. No auxiliary rows, finite packet substitution or generic regularity argument replaces the complete actual pair law.

## 3. Legal Abel integration and the exact logarithmic coefficient

For each tau>0 the established absolutely convergent representation is

    A_tau(h)=(2/pi) integral_0^infinity E_h(t)/(t^2+tau^2)dt.

The part t>=t0 is uniformly bounded, since |E_h(t)|<=2V_h. Write c_h=|kappa_R(h)|^2. The leading local term integrates exactly:

    integral_0^t0 c_h t/(t^2+tau^2)dt
       =(c_h/2) log((t0^2+tau^2)/tau^2)
       =c_h log(1/tau)+O(1).

For every eta>0, E_h(t)-c_h t has absolute value at most eta t below a sufficiently small fixed delta. Its integral there is at most eta log(1/tau)+O_eta(1); the remaining fixed interval has a tau-independent bound. Divide by log(1/tau), then send eta to zero. This proves the coefficient without a Tauberian theorem or an interchange of divergent signed moments.

Polarization gives the Hermitian Abel form limit (2/pi) kappa_R^*kappa_R on K. In particular its whole physical trace is (2/pi)Lambda_K, independent of basis. This scalar is positive whenever K is nonzero. The rough quotient is rank one; total dimension may exceed one. Regular kernel vectors can have bounded individual Abel forms even when this whole trace diverges logarithmically.

The identical local error argument, now integrating E_h(t)/t^2 from epsilon to t0, gives I_(epsilon,1)(h)/log(1/epsilon)->c_h and the whole trace limit Lambda_K. This is a second exact critical interface, not a subtraction of divergent positive/negative moments. A nonpositive liminf of that normalized whole trace also suffices for exclusion.

## 4. A weaker sharp-height sufficient target

Use the lawful positive averaging identity

    A_tau^K=integral_0^infinity omega_tau(T) S_K(T)dT,
    omega_tau(T)=tau omega_1(tau T),
    omega_1(x)=[1-(1+x)exp(-x)]/x^2.

This is a probability density. Its representation omega_1(x)=integral_0^1 v exp(-xv)dv gives omega_1<=1/2 and omega_1<=1/x^2. Hence integral omega_1(x)log(e+x)dx is finite (the elementary bound 5 suffices). For 0<tau<=1,

    integral omega_tau(T)log(e+T)dT<=log(1/tau)+5.

Suppose the actual sharp head has limsup S_K(T)/log(e+T)<=0. For every eta>0 there is finite M_eta such that S_K(T)<=eta log(e+T)+M_eta for all T. Finite-height boundedness supplies the constant on the initial interval. Positive averaging gives

    A_tau^K<=eta(log(1/tau)+5)+M_eta.

Thus limsup A_tau^K/log(1/tau)<=0. The exact positive coefficient for a nonzero K contradicts this. This is a strictly weaker sufficient hypothesis than the older uniform upper bound. It still requires an ACTUAL arithmetic estimate, not merely ordinary tail convergence.

A sharp SUBSEQUENCE with S_K(T_n)/log T_n small does not suffice. The earlier abstract paired-atom control has sharp heads returning to zero at every negative atom, yet at tau=4^(-n) it has A_tau>=(9/640)n. Since log 4<2, its normalized Abel liminf along those scales is at least 9/1280. This is a coefficient control, not actual divisor data or a native-null example. No sharp asymptotic S_K(T)/log T is inferred from the signed Abel limit.

## 5. Same-vector enlarged-null failure and an explicit negative trial

For a kernel vector with nonzero trace, actual translation invariance of the global native convolution form gives Q(tau_t h)=Q(h)=0. Therefore the physical trial h+tau_t h, supported in the enlarged window, satisfies

    Q(h+tau_t h)=-2|kappa_R(h)|^2 t+o(t)<0

for all sufficiently small positive t. This constructs a local actual negative trial CONDITIONALLY on hypothetical contact, without a new aperture certificate. Every strict larger window contains such a trial.

The retained physical h itself is unchanged and still has zero diagonal energy by support restriction. It has nonzero enlarged mixed pairing with tau_t h. Its complete actual coefficients remain the same on enlargement; the test coefficients change through the exact actual pair law. Thus diagonal zero is not same-vector enlarged full-null transport. The new trial changes the physical vector by adding a translate; no dilation or historical selected witness is used.

## 6. Positive-eigenvalue control still fails the new target

The exact coefficient is not exclusive to zero eigenvalue. On a fixed actual physical eigenspace q_h=mu h, the exterior overlap contributes the same -|kappa_R|^2 t+o(t), while diagonal subtraction leaves

    Q(h)-Re Q(h,tau_t h)=mu D_mass(t)+|kappa_R|^2 t+o(t),
    D_mass(t)=||h||^2-Re<h,tau_t h>.

Here D_mass=o(t), proved without assuming H1. Let D_m be the native symbol cosine defect and D_w its log-weighted positive counterpart. The retained symbol lower envelope gives D_w<=D_m+C D_mass. Split Fourier space at |xi|=t^(-alpha), 0<alpha<1/2. Below the split the cosine estimate gives O(t^(2-2alpha))||h||^2=o(t). Above it, w>=alpha log(1/t), so

    D_mass<=D_w/[alpha log(1/t)]+o(t)
           <=D_m/[alpha log(1/t)-C]+o(t).

The pole defect is O(t^2), hence D_m=mu D_mass+|kappa_R|^2 t+o(t). Insert this into the previous bound and absorb the fixed mu term for sufficiently small t. It follows that D_mass=o(t), and the actual pair error is still o(t). The SAME E/t and Abel/log coefficient follow.

The pinned actual rough positive eigenmode has nonzero trace and therefore a strictly positive Abel logarithmic slope. It fails the new sublogarithmic target, as required of a genuine zero-specific arithmetic criterion. It is not actual zero-nullity. This checks that the improvement did not quietly import a shift-invariant regularity bound that the control refutes.

A generic cusp/control vector has no exact interior zero equation, so its native correlation cannot be reduced to the single exterior strip in section 1. No kernel trace or actual null law is assigned to such a vector from regularity alone.

## Remaining theorem and validation

The smallest arithmetic obligation on THIS improved route is the one-sided nonpositive liminf of the whole-contact Abel logarithmic slope. The sublogarithmic sharp-head upper bound is a sufficient finite-height interface. Equivalently, the exact slope formula identifies the missing quantity with Lambda_K; its vanishing is still unproved. This is endpoint exclusion, not retained packet attachment.

The companion check verifies finite sharp returns and peaks, independent rational exponential enclosures for the Abel lower coefficient, and positive local-remainder integral budgets. These are scoped controls, not an analytic or Lean certification. Four repository source pins are recorded in the manifest. No new external theorem, local Lean build or axiom audit is claimed.

All four pins were verified at the live recovered commit. The local signed-cutoff mirror had an extra terminal newline; retrieval-only normalization to the verified source bytes restores its recorded blob hash. No historical repository source is edited or included as a new blob by this pass.

Pinned sources at the recovered head:

- notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_ENDPOINT_TRACE_20261007.md, blob 1996d3fb3358965c5468481c31252f3dda440e69.
- notes/REFLECTED_PACKET_BRIDGE_108_ABEL_SHARP_HEIGHT_20261007.md, blob a51b2becce5c0ffaa394f4b7d29f6aa136473687.
- notes/REFLECTED_PACKET_BRIDGE_108_SIGNED_CUTOFF_SOURCE_MOMENT_20261007.md, blob 52f34cc5c348c7ad5b00058c1208599f531bf4c7.
- notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_EIGENMODE_TARGET_20261007.md, blob 3354b89638b643d5b21c4c428f069f738ccf59f5.

At initial recovery the certified frontier was 973/1000. Publication recovers the newer concurrent head 8b2d7c69d3c7a5ea55009a3a118d8a0a873c126b: its full 112-source Gram/sign certificate advances whole-domain positivity to 49/50, with Q>=1e-30 physical mass and Q>=8e-33 Elog. This is reused aperture-lane evidence, not a new estimate in this global pass. Its read note notes/REFLECTED_PACKET_BRIDGE_108_PRIME7_GRAM112_098_20261007.md has blob 8874d390525a85d863bbe7563839b21b886304c9. All newer custody and historical wording are preserved. No aperture marching, actual kernel existence, arithmetic sublogarithmic bound, retained attachment, RH, F4 or FULL TRANSPORT CLOSED is claimed.
