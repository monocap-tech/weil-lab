# RPB108: exact translation boundary flux and a critical integrated condition

Status: local analytic continuation at d17a74065324575654cd53ea394957dfa4961ebb; not promoted or Lean certified.

## Definitions registered before use

Fix a>0 and an actual full mixed weak-null vector h in D_a. Extend h by zero. Let tau_t h(x)=h(x-t), P_a=1_[-a,a], H=||h||_2, w(xi)=log(e+|xi|), and m_a=m0-t_a be the actual frozen multiplier including the fixed right-limit prime set. L_h=m_a(D)h and r_h=L_h+p_h are the recovered core and full residual; r_h vanishes almost everywhere on (-a,a) and is locally L2. Write

    P0=2 Re(conjugate(M_-(h)) M_+(h)),
    D_m(t)=integral m_a(xi)(1-cos(2*pi*xi*t)) |Fourier(h)(xi)|^2 dxi,
    D_w(t)=integral w(xi)(1-cos(2*pi*xi*t)) |Fourier(h)(xi)|^2 dxi.

For 0<t<min(1,2a), define the real translation boundary flux

    F_h(t)=Re integral_a^(a+t) r_h(x) conjugate(h(x-t)) dx.

This sign convention is fixed: the flux is the residual paired with the translated source, not its negative. It is distinct from the moving-Gaussian collar action. The frozen whole-line pairing below does not assert a larger-window weak-null equation or identify it with a native form using newly activated primes.

## The support-projected translated test is lawful

The recovered logarithmic bootstrap gives h in X_1. Translations preserve X_1, and the recovered projection bound proves P_a tau_t h in X_1, hence in D_a. Full mixed nullity therefore kills the genuine action against conjugate(P_a tau_t h).

The recovered multiplier-domain theorem gives L_h in L2. The pole is bounded on every compact interval. Thus the action against any compactly supported L2 test is defined by ordinary L2 pairing, agrees with the form on D_a, and permits the exact decomposition of tau_t h into its interior and exterior portions. Only the right strip (a,a+t) remains. Consequently

    F_h(t)=Re A_a(h;conjugate(tau_t h)).                    (1)

No trace of h or r_h is taken. All identities are almost-everywhere or L2 identities.

## Exact spectral and pole identity

Fourier(tau_t h)=exp(-2*pi*i*xi*t) Fourier(h). Thus the real core pairing is integral m_a cos(2*pi*xi*t)|Fourier(h)|^2. Compact support also gives

    M_+(tau_t h)=exp(t/2) M_+(h),
    M_-(tau_t h)=exp(-t/2) M_-(h).

The real pole pairing is cosh(t/2) P0. The full null diagonal is integral m_a|Fourier(h)|^2+P0=0. Subtracting that diagonal from the translated pairing proves

    F_h(t)=-D_m(t)+(cosh(t/2)-1)P0.                       (2)

The sign in (2) is essential. It comes from cos-1, not 1-cos. The actual archimedean and prime multiplier are retained together in D_m; the actual Hermitian pole cross-moment is retained separately.

## A precise critical cancellation criterion

Use the recovered global envelope |m_a-w|<=C_a, with C_a>=0. Choose N=exp(2C_a+2), wN=log(e+N). For |xi|>=N, m_a>=w/2. For |xi|<N, m_a>=-C_a and 1-cos(2*pi*xi*t)<=2*pi^2*N^2*t^2. Hence

    D_m(t)>=D_w(t)/2-Zcore_a*t^2*H^2,
    Zcore_a=2*pi^2*N^2*(wN/2+C_a).

For 0<t<=1, cosh(t/2)-1<=t^2/4, and |P0|<=Ppole_a H^2 with Ppole_a=4a exp(a). Set Z_a=Zcore_a+Ppole_a/4. Equation (2) yields

    D_w(t)<=-2F_h(t)+2Z_a*t^2*H^2.                       (3)

Conversely |m_a|<=w+C_a<=(1+C_a)w gives

    |F_h(t)|<=(1+C_a)D_w(t)+(Ppole_a/4)t^2 H^2.           (4)

For any fixed t0 in (0,min(1,2a)), Tonelli and the elementary cosine integral imply

    integral_0^t0 D_w(t)/t^2 dt<infinity
       iff integral |xi| w(xi)|Fourier(h)(xi)|^2 dxi<infinity.  (5)

For completeness, the full half-line integral is integral_0^infinity (1-cos(2*pi*xi*t))/t^2 dt=pi^2|xi|. A proof uses integration by parts followed by the Abel-regularized Dirichlet integral. No exact constant is needed for (5): the substitution u=|xi|t gives an upper bound C|xi| by splitting at u=1 and a lower bound c|xi| at high frequencies by integrating over u in [1/4,1/2]. The bounded-frequency contribution is finite since h already has logarithmic energy.

Equations (3)-(5) show the following exact equivalence under the actual full mixed-null hypotheses:

    integral_0^t0 |F_h(t)|/t^2 dt<infinity
       iff integral |xi| w(xi)|Fourier(h)(xi)|^2 dxi<infinity.  (6)

The right side is a logarithmically strengthened zero-extension H^(1/2) condition. In particular, a genuine flux lower bound F_h(t)>=-C t^(1+epsilon)H^2 for some epsilon>0 would establish it. This sufficient condition is unproved. Its orientation is a lower bound on the signed translation flux, whereas the Gaussian route asks for an upper bound on a different signed action.

An upper bound F_h(t)<=O(t^2)H^2 is already immediate from (2)-(3), because D_w>=0. That one-sided estimate cannot be used as the missing cancellation: it allows an arbitrarily large negative flux. Likewise the recovered every-s bounds may give subcritical power control but do not establish the integral in (6).

## What changed and what remains

This gives an exact boundary identity for the same actual weak-null vector, without endpoint traces or an enlarged null window, and identifies a concrete integrated cancellation quantity for the critical regularity route. It does not prove that quantity finite, produce half-derivative regularity, exclude a finite endpoint, or establish the exponential Gaussian upper theorem. Even the critical regularity condition alone is not an RH conclusion.

The next substantive arithmetic task is to estimate the negative part of the explicit exterior strip pairing in (1), using the actual kernel, translated prime terms and pole. Squared collar mass or absolute Cauchy-Schwarz alone does not provide critical integrability. The separate retained selected-witness attachment remains open.

Numerical aperture remains 81/100. F4 and FULL TRANSPORT CLOSED remain open. No actual nonzero null vector existence, repository push, Lean change or CI result is asserted.

## Validation boundary

Inputs: recovered ENDPOINT_BOUNDARY_REGULARITY, LOGARITHMIC_BOOTSTRAP and FRACTIONAL_NULL_REGULARITY, plus their exact source dictionary. Pole phase orientation and the cos-minus-one algebra were checked separately. The exact integral and operator arguments are analytic, not mechanically certified. Algebra controls are not actual zeta modes.

## Repository custody addendum

This note was initially produced locally; its original status sentences above record that history. It is now included in the research-branch custody repair based on d17a74065324575654cd53ea394957dfa4961ebb. Repository custody supersedes the original unpromoted/local storage status only. The analytic derivation remains unverified in Lean and is not certified by the algebra controls. Definitions: docs/TERMINOLOGY_RPB108_BOUNDARY_CONTINUATION.md. Reproducible algebra controls: scripts/certify_native_boundary_continuation.py; certificate and repeat validation under notes/data/RPB108_BOUNDARY_CONTINUATION_*_20261005.json.
