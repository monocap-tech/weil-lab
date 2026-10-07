# RPB108: a positive Abel interface to the actual sharp first-height sums

Date: 2026-10-07 UTC. Recovered live head 5d2f3b839cf200700720f6eca0b1c443826ef06d.
Definitions: [Abel defect and sharp divisor-height registry](../docs/TERMINOLOGY_RPB108_ABEL_SHARP_HEIGHT.md).
Category: endpoint exclusion / actual arithmetic target reduction. No independent arithmetic bound or Lean certification.

## Result

For the whole hypothetical nonnegative ACTUAL full-native contact kernel K_a, the following uniform one-sided bound suffices to exclude contact:

    sup_(T>=T1) sum_(|theta_q|<=T) |theta_q|
                   sum_basis (|p_q(h_j)|^2-|n_q(h_j)|^2) < infinity.   (1)

This is a finite-height target on the prescribed complete divisor observations. There is no auxiliary mass carrier, height-weighted absolute tail premise, or same-vector enlarged-null substitution.

A positive Abel averaging identity converts (1) into the already sufficient critical signed estimate. The identity and conversion are proved here; the ACTUAL bound in (1) is NOT obtained. Thus this is a usable arithmetic interface, not progress on the missing arithmetic inequality itself.

An abstract normalized two-channel control has every subcritical moment, infinitely many sharp heads equal to zero, but Abel critical defect tending to +infinity. Consequently a bounded SUBSEQUENCE of sharp first-height heads cannot replace the uniform upper bound. This is not an actual zero-source or null example.

## 1. Legal Abel sums and the positive sharp-head identity

Fix supported canonical h. Base actual source sampling gives sum_q |d_q(h)|<=||P h||^2+||N h||^2=:V_h<infinity. Since 0<=alpha_tau(u)<=1/tau, A_tau(h) is absolutely defined for each tau>0. Sharp S_h(T) is finite since u<=T in its sum; no critical moment is assumed.

The formula k_tau(T)=integral_0^1 exp(-tau T v)dv proves it is decreasing, starts at 1 and tends to zero. Differentiation gives the nonnegative omega_tau above and integral_0^infinity omega_tau(T)dT=1. Moreover

    integral_u^infinity omega_tau(T)dT=k_tau(u).

Tonelli applied separately to the positive and negative channels yields

    A_tau(h)=integral_0^infinity omega_tau(T) S_h(T)dT.       (2)

The absolute interchange is justified by

    sum_q |u_q d_q| integral_(u_q)^infinity omega_tau(T)dT
          =sum_q alpha_tau(u_q)|d_q|<=V_h/tau.

Coordinates at u=0 contribute zero to both sides. No unregularized infinite first moments are subtracted. Formula (2) remains valid for the finite kernel trace and does not rely on ordering multiplicity copies.

If S_h(T)<=M for all T, (2) gives A_tau(h)<=M for all tau. A bound only above T1 extends to all T with max(M,T1 V_h). There is no need for a lower bound on S_h. Positivity of omega_tau is precisely why a ONE-SIDED uniform sharp bound works.

## 2. Exact translation representation and native comparison

For tau>0 and real theta,

    alpha_tau(|theta|)=(2/pi) integral_0^infinity
                       (1-cos(theta t))/(t^2+tau^2)dt.      (3)

A direct proof integrates exp(i theta z)/(z^2+tau^2) over an upper half-plane semicircle for theta>0. Its only pole is i tau, with residue exp(-theta tau)/(2 i tau); the arc tends to zero. Evenness gives the cosine half-integral pi exp(-tau |theta|)/(2 tau). Subtract it from the elementary theta=0 half-integral pi/(2 tau). This proves (3), including theta=0, without importing a new theorem.

At fixed tau, the integrals of the absolute source sum are bounded by V_h/tau, so (3) gives the lawful complete-source identity

    A_tau(h)=(2/pi) integral_0^infinity E_h(t)/(t^2+tau^2)dt. (4)

For t>=t0, |E_h(t)|<=2V_h, making that part bounded uniformly by 4V_h/(pi t0). E_h is defined there by the ordinate cosine sum. We do NOT extend the small-collar actual null-flux identity to all translations or grow the physical support without custody.

On (0,t0) use the EXACT previously established full-source/native identity

    E_h=D_m-(cosh(t/2)-1)Ppole(h)+R_h.

For actual zero-null h, both subcritical half-height source moments are already derived. The accepted B=3/8 strip and s=1/4 give integral_0^t0 |R_h(t)|dt/t^2<infinity. The pole correction is O(t^2). Since 1/(t^2+tau^2)<=1/t^2, these terms have a tau-independent absolute budget. The actual native symbol envelope therefore yields a finite L_h such that

    A_tau(h)>=W_tau(h)/2-L_h,
    |A_tau(h)|<=(1+C_a)W_tau(h)+L_h.                       (5)

W_tau increases as tau decreases. By monotone convergence its limit is (2/pi) times the critical D_w integral, finite exactly when h is in Xcrit. Consequently

    liminf_(tau down to 0) A_tau(h)<infinity iff h in Xcrit; (6)
    h not in Xcrit -> A_tau(h)->+infinity.

This is a regularized actual-source criterion. It does not prove its premise on a zero kernel. The same comparison applies to the pinned actual positive eigenmode because its shifted subcritical moments and diagonal-subtracted source identity are already certified analytically.

## 3. Whole-kernel exclusion and actual positive-mode control

Sum (2),(5) over a physical orthonormal basis of finite K_a. The traces are basis independent. The constants are finite sums; W_tau^K is nonnegative and monotone. Bound (1) forces A_tau^K uniformly bounded above, hence every basis vector in Xcrit. The analytically closed critical reciprocal promotion puts the WHOLE K_a in H1, with differentiation preserving K_a. The finite-dimensional derivative-chain contradiction then gives K_a=0.

Conversely, any hypothetical nonzero actual contact kernel would have A_tau^K->+infinity. Equation (2) implies

    limsup_(T to infinity) S_K(T)=+infinity.                (7)

Indeed S_K is bounded on each finite height interval; a finite upper bound at large heights would contradict Abel divergence. Nothing here proves S_K(T)->+infinity or excludes dips.

For the pinned unchanged rough positive actual eigenmode at 24/25, the same reasoning proves A_tau(h)->+infinity and limsup S_h(T)=+infinity. Thus (1) cannot be deduced for all actual eigenspaces from shift-stable regularity, source sampling and the transverse strip. This actual control does not solve q_h=0 and is not a counterexample to the proposed actual CONTACT bound.

## 4. Why a bounded sharp subsequence is not enough

This separate abstract coefficient control uses beta=0 everywhere and theta>0. At theta=4^j, j>=1, assign positive squared coefficient (9/4)j 4^(-j). At theta=2*4^j assign negative squared coefficient (9/8)j 4^(-j). Add a negative squared coefficient 1/2 at theta=0.

Since sum j 4^(-j)=4/9, the complete positive and negative squared norms are each one. Every source order r<1 is finite on both channels by the geometric series sum j 4^(-(1-r)j); finite logarithmic orders are also summable. The sharp first-height head rises to (9/4)j at the positive atom, then returns to ZERO at the following negative atom. Hence S>=0, liminf_(T->infinity) S(T)=0 and sup S=infinity.

Its Abel signed defect is the positive sum

    A_tau=(9/4) sum_(j>=1) j [k(tau 4^j)-k(2 tau 4^j)],
    k(x)=(1-exp(-x))/x=integral_0^1 exp(-x v)dv.

Choose j with x=tau 4^j in [1,4] for small tau. On v in [1/4,1/2], x v lies in [1/4,2], so

    k(x)-k(2x)>=exp(-2)(1-exp(-1/4))/4>=1/160.

Here exp(2)<8 and exp(1/4)>=5/4 justify the rational lower bound. Thus A_tau>=(9/640)j and tends to +infinity as tau decreases to zero. Legal Abel sums are finite for each tau by the base norms. A bounded sharp subsequence therefore does NOT force bounded Abel defect even with neutral norms, the strip, all subcritical moments and all logarithmic moments.

This control has no actual-divisor sampling, physical compact-support or full-native null custody. It rejects only the attempted weakening of the arithmetic interface. It does not show such sharp dips occur for an actual contact vector.

## Remaining theorem, source custody and validation

Category: endpoint exclusion. The smallest theorem for THIS finite-height route is the uniform ONE-SIDED upper bound (1) for every hypothetical nonnegative actual zero-contact kernel. A direct finite-liminf Abel bound also suffices by (6); it remains equivalent to the existing critical moment gate. A proof must use actual fixed-divisor zero normalization, not the added mass carrier in the preceding comparison audit. No such bound is supplied by ordinary quadratic-tail localization without a critical height rate.

Pinned sources at recovered head:
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.
- SIGNED_CUTOFF_SOURCE_MOMENT_20261007: 52f34cc5c348c7ad5b00058c1208599f531bf4c7.
- EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007: c369d3760606d9e5b9ae0f4862156fd712e5be29.
- POSITIVE_SOURCE_HEIGHT_MOMENT_20261006: 7997a0a3ccb0666d117f696dd208b743255b7ac5.
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006: 955ff7b4bd0d7f58221c300a962a803824232fd6.
- SIGNED_CUTOFF_SOURCE_MOMENT terminology: c427714cd49636daa3f3ce1622a759c8af3b1728.

Analytic validation: absolute finite-tau Fubini, nonnegative Abel density and its total mass, exact cosine transform, separation of the large-translation source tail from the local native identity, uniform remainder budgets, monotone unsigned defect, whole-kernel quantifier, and abstract subsequence-control divergence. The rational companion checks norm normalization, 64 paired sharp returns and growing peaks, and the exponential ceiling/lower constant. It is an abstract regression control, not actual zeta data or a proof of an arithmetic bound. Source observability and external boundary/strip dependencies remain those of the pinned notes. No new external input, Lean build, axiom audit or CI claim.

Definitions and canonical cursor updated additively; historical wording and concurrent aperture work preserved. Whole-domain positivity remains certified through 973/1000. No aperture marching, retained packet substitution, same-vector enlarged actual-null transport, endpoint exclusion, RH, F4 or FULL TRANSPORT CLOSED.
