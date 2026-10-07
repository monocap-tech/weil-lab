# RPB108: an actual positive eigenmode defeats every supercritical signed trace bound

Date: 2026-10-07 UTC. Recovered live head a03073b422d8975a415565175e4b7b225c0e6925.
Definitions: [actual supercritical source control](../docs/TERMINOLOGY_RPB108_ACTUAL_SUPERCRITICAL_SOURCE_CONTROL.md).
Analytic actual-operator obstruction, not an eigenmode computation or endpoint closure.

## Actual result

At c=24/25, the existing actual whole-domain certificate and physical eigenvalue theorem give an attained positive lowest eigenvalue

    mu=lambda_ph(c)>=3e-29>0.

Its finite nonzero eigenspace contains a physical mass-one vector h outside global H1. For this SAME actual native eigenmode,

    sum_actual_copies |theta_q|^r |p_q(h)|^2=+infinity
    for every r>1,

and at every fixed 1<r<2,

    I_(epsilon,r)(h)->+infinity.

In particular the proposed order-3/2 signed cutoff upper estimate fails for an actual positive native eigenmode retaining every prime, pole and divisor observation. The accepted external quasi-RH strip |beta|<=3/8 applies to these same divisor observations. No abstract cusp or artificial source coordinate supplies this control.

This does not falsify an estimate confined to the exact actual zero kernel: the control solves q_h=mu h with mu>0. Its critical order-one source moment remains undecided.

## 1. Negative distributional promotion with a scalar eigenvalue

Fix finite a and real mu. Suppose supported g in Y_-sigma, 0<sigma<1/2, satisfies

    m_a(D)g+p_g=mu g on (-a,a).

Extend the read zero-promotion argument explicitly. The support-projected equation has no nonzero endpoint defect in H^(-sigma-delta), with sigma+delta<1/2. Its commutator identity is now

    m0(D)g=P T_a g-P p_g+[m0(D),P]g+mu g.

The additional term is bounded on Y_-sigma. Thus m_a(D)g remains in Y_-sigma, as in the zero proof.

The shifted logarithmic Riesz operator is A-mu J*J, self-adjoint I+compact; its kernel K_a^mu is finite-dimensional and its inverse is taken only on the kernel complement. The read shifted null bootstrap puts the kernel basis in every Y_t, t<1/2.

For a smooth interior forcing f, subtract its physical L2 projection onto K_a^mu. The shifted Fredholm inverse gives a supported canonical u with

    (Q_a-mu mass)(u,v)=<f-Pi_(K^mu)f,v>_2.

The forced capped absorption bound is the previous one with B_t replaced by B_t+|mu|. Choosing the high-frequency threshold using this finite enlarged budget still leaves absorption coefficient strictly below 1/2. Thus u and m_a(D)u belong to every required Y_t with sigma<t<1/2.

Testing g against u, the dual adjoint identity has the additional bounded symmetric term -mu<g,u>. It gives <g,f-Pi_(K^mu)f>=0. Endpoint removal then identifies g with the SAME global L2 eigenspace vector. Every step of promotion survives the shift; it does not require adding a mass observation to the divisor source carrier.

## 2. Supercritical regularity collapses to H1 on the actual eigenspace

For h in K_a^mu intersect H^alpha, 1/2<alpha<1, its global distributional derivative is supported, belongs to H^(alpha-1), and solves the differentiated eigen-equation. The pole moment signs and constant mass commute with differentiation. Shifted negative promotion puts h' in K_a^mu and L2. Therefore

    K_a^mu intersect H^alpha=K_a^mu intersect H1.

If the entire finite eigenspace lay in H1, differentiation would be its endomorphism, and arbitrarily long Fourier-polynomial independent derivative chains would contradict finite dimension. Hence some nonzero lowest actual eigenmode is outside H1; normalize its physical L2 norm to one. That vector fails H^alpha for every alpha>1/2.

The general actual positive source/Fourier equivalence applies to all canonical h, independently of nullity. For 1<r<2 a finite positive r-moment would put this h in H^(r/2), a contradiction. At r=2 the earlier derivative-log criterion also implies H1; for r>2, base source energy and monotonic comparison imply the order-two moment would be finite. This proves the displayed divergence at every r>1.

The shifted bootstrap still provides every source order below one, both positive and negative. These are actual observations of the eigenmode, not a comparison source augmented by a mass channel.

## 3. Signed cutoff divergence and leading weighted flux

The diagonal-subtracted source identity proved in the previous pass does not require eigenvalue zero:

    E_h(t)=D_m(t)-(cosh(t/2)-1)Ppole(h)+R_h(t).

Both derived subcritical source moments make the R_h integral against t^(-1-r) finite for every fixed r<2, by choosing r<1+2s. The native envelope supplies

    I_(epsilon,r)>=W_(epsilon,r)/2-L_(h,r).

The supercritical Fourier moment is infinite, so W_(epsilon,r)->+infinity and hence I_(epsilon,r)->+infinity.

There is also a sharper fixed-vector relative statement. The read rough-flux theorem gives D_mass(t)=o(D_w(t)) for every fixed non-H1 h. Since W_(epsilon,r) diverges, splitting its integral at any small fixed delta shows

    integral_epsilon^t0 D_mass(t)t^(-1-r)dt
            =o(W_(epsilon,r)).

Indeed on (0,delta) the ratio is at most any prescribed eta, while the integral on (delta,t0) is a fixed finite constant. Use the limits epsilon->0 then eta->0. The bounded archimedean correction and finite prime multiplier satisfy the same relative bound. The pole integral and transverse remainder are finite. Consequently

    I_(epsilon,r)/W_(epsilon,r)->1,
    B_(epsilon,r)^mu/W_(epsilon,r)->-1.

The second identity retains the genuine eigenmode exterior flux

    F_h^mu=-D_m+(cosh(t/2)-1)Ppole(h)+mu D_mass.

Thus the interior mass correction cannot cancel the leading weighted rough flux for this fixed physical mode. The same conclusions hold for the full fixed lowest-eigenspace trace, because at least one basis contribution is rough and the cutoff proof applies to the trace.

No aperture-uniform or moving-eigenvector limit is asserted. This is not a statement that the scalar mass term is irrelevant to deciding which vectors solve the exact zero equation.

## Failed implication and smallest remaining theorem

Category: endpoint exclusion.

Failed implication: full actual prime/pole/source custody + |beta|<=3/8 + a finite eigenspace + all subcritical source moments + signed cutoff identities -> bounded order-3/2 signed source trace for every actual eigenmode.

The actual positive eigenmode above disproves that generic claim. It improves the previous actual order-two control to EVERY supercritical source order and to the exact signed cutoff target. Its sole interior-normalization difference is mu>0.

The remaining theorem must be explicitly confined to a hypothetical nonnegative actual zero kernel: finite liminf of its full signed order-3/2 cutoff trace, or the equivalent weighted signed boundary lower estimate. Repeating an argument that is unchanged by adding -mu mass cannot establish that bound. No independent arithmetic estimate has been proved in this pass.

## Source custody and validation

Pinned reads at the recovered head:
- THREEBAND_POSITIVITY_096_20261007, blob 119a2a3198ea0df81486e9f0ba98795f72685c98: actual physical lower bound 3e-29 at 24/25.
- NATIVE_MASS_CONTACT_20261006, blob 65b45b856fdb33014f9dee0468d0cf75ff413539: attained actual physical eigenvalue, shifted promotion/bootstrap, finite eigenspace and derivative obstruction.
- SUBCRITICAL_DISTRIBUTIONAL_PROMOTION_20261007, blob 665a473edee975b2d346d0511a292e4a64cb56e8: negative Sobolev inverse-test proof.
- SIGNED_CUTOFF_SOURCE_MOMENT_20261007, blob 52f34cc5c348c7ad5b00058c1208599f531bf4c7: legal finite cutoff sums, remainder and native symbol comparison.
- LEADING_ROUGH_FLUX_20261006, blob 9982daabb0e22a666c13ef83b74bc21e235c0ef8: fixed-vector mass/log defect comparison.
- EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007: accepted external strip input, unchanged.
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006 and POSITIVE_SOURCE_HEIGHT_MOMENT_20261006: actual general source criteria.

Analytic validation explicitly tracks the added mu term through the distributional domain, Fredholm inverse, capped absorption, dual test and derivative equation. Existing signed-cutoff and source-flux algebra controls pass as regression only. No actual eigenvector coefficients, eigenvalue beyond the imported lower bound, or numerical divergence rate are computed. No Lean certification, new axiom audit or CI claim. No aperture calculation or historical packet work. Cursor updated additively; 24/25 whole-domain certificate preserved. Exact-zero endpoint exclusion, critical order-one promotion, F4 and FULL TRANSPORT CLOSED remain unproved.
