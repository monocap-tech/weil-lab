# RPB108: a one-sided signed source cutoff criterion for contact exclusion

Date: 2026-10-07 UTC. Recovered live head bd7a46764b5da37cb5b174ddf83961d27ad4e459.
Definitions: [signed cutoff source moment registry](../docs/TERMINOLOGY_RPB108_SIGNED_CUTOFF_SOURCE_MOMENT.md).
Analytic sufficient criterion, not an actual arithmetic estimate.

## Exact outcome

At a hypothetical actual full-native null window, for every fixed 1<r<2,

    liminf_(epsilon down to 0) I_(epsilon,r)^K < infinity -> K_a={0}.

Thus a one-sided bounded subsequence of finite signed actual source sums suffices; no absolute positive moment estimate or critical derivative-promotion theorem has to be supplied separately. The unsigned regularity is recovered from the actual native symbol envelope, then the newer negative-distributional promotion closes the derivative argument.

For a nonzero hypothetical kernel the converse obstruction is exact:

    I_(epsilon,r)^K -> +infinity for every 1<r<2.

This does not prove the finite-liminf premise. It expresses a smaller arithmetic target using actual signed source data, and identifies why a mere norm balance or a phase rearrangement is insufficient.

## 1. Stronger joint remainder from both derived subcritical moments

Use the read exact source identity F_h=-E_h+R_h for h in K_a and B=3/8. The preceding pass bounded the sinh cross term with only a positive fractional moment. The negative fractional moment is also already derived from the actual source translation theorem: for every 0<s<1/2,

    M_(+,s)=sum |theta|^(2s)|p|^2 < infinity,
    M_(-,s)=sum |theta|^(2s)|n|^2 < infinity.

These are consequences of actual null regularity and complete source sampling, not new assumptions. Since 0<2s<1, |sin(theta t)|<=|theta t|^(2s). Distribute one factor |theta|^s onto each coefficient and use Cauchy-Schwarz:

    sum |sin(theta t)| |p||n|
       <= t^(2s) sqrt(M_(+,s) M_(-,s)).

Consequently, with V=||p||^2+||n||^2,

    |R_h(t)| <= exp(Bt)[B^2 V t^2/2
                   +2B t^(1+2s) sqrt(M_(+,s) M_(-,s))].

For any fixed 0<r<2 choose 0<s<1/2 with r<1+2s. Then

    integral_0^t0 |R_h(t)| t^(-1-r) dt
      <= exp(Bt0)[B^2 V t0^(2-r)/(2(2-r))
           +2B sqrt(M_(+,s) M_(-,s)) t0^(1+2s-r)/(1+2s-r)]
      < infinity.

Both denominators are strictly positive. Example: r=3/2 and s=3/8 leave the cross-integral margin 1/4. The stricter transverse bound improves constants but the argument also works at B=1/2.

## 2. Native envelope recovers an unsigned Fourier moment

Let W_(epsilon,r)=integral_epsilon^t0 D_w(t) t^(-1-r) dt, with the unchanged nonnegative Fourier cosine defect D_w. The exact native flux identity and logarithmic symbol envelope give

    D_m(t)>=D_w(t)/2-Zcore t^2 ||h||_2^2,
    |D_m(t)|<=(1+C_a)D_w(t),
    |(cosh(t/2)-1)Ppole(h)|<=t^2 |Ppole(h)|/4.

Since E_h=D_m-(cosh(t/2)-1)Ppole(h)+R_h, there is a finite fixed-vector L_(h,r) such that for every 0<epsilon<t0,

    I_(epsilon,r)(h) >= W_(epsilon,r)(h)/2-L_(h,r),
    |I_(epsilon,r)(h)| <= (1+C_a)W_(epsilon,r)(h)+L_(h,r).

The first inequality also shows the negative part of E_h is integrable against t^(-1-r). Consequently its signed improper integral has an extended limit in the finite reals or +infinity; cancellation cannot create bounded oscillating subsequences hiding an infinite positive part.

By Tonelli and substitution u=|xi|t,

    sup_epsilon W_(epsilon,r)<infinity
       iff integral |xi|^r w(xi)|hhat(xi)|^2 dxi < infinity.

The high-frequency lower bound uses a fixed u interval where 1-cos(2pi u)>0; the low-frequency part is controlled by the base logarithmic energy. No limiting difference of two infinite source moments is taken.

Together these show finite liminf I_(epsilon,r) is equivalent to the unsigned Fourier r-moment and the actual positive source r-moment on K_a. If that moment is infinite, the lower bound forces I_(epsilon,r)->+infinity.

## 3. Legal source sums and whole-kernel quantifier

For every fixed epsilon>0,

    0<=J_(epsilon,r)(theta)<=2(epsilon^(-r)-t0^(-r))/r.

Thus both positive and negative sums defining I_(epsilon,r) are finite by unweighted complete source l2 norms. Fubini on the bounded epsilon interval gives exactly

    I_(epsilon,r)(h)=integral_epsilon^t0 E_h(t) t^(-1-r) dt.

No height truncation error or unproved weighted tail is hidden. It is NOT legitimate to replace the limit by an unregularized subtraction sum |theta|^r|p|^2 minus sum |theta|^r|n|^2 when either diverges.

Take a physical L2 orthonormal basis of finite K_a and sum the lower inequality. The constants and subcritical remainder norms are finite basiswise. W^K is nonnegative and monotone as epsilon decreases. A finite liminf of I^K forces every basis vector to have the Fourier r-moment, hence to be in global H^(r/2).

For r>1 the newer promotion theorem places each such vector in global H1. The entire K_a is then differentiation invariant, and Fourier-polynomial independence contradicts finite dimension unless K_a=0. Conversely a nonzero K_a contains a non-H1 vector; on actual K_a it fails every H^alpha with alpha>1/2, so at least one basis contribution has infinite W. The trace lower bound gives the displayed +infinity conclusion.

At r=1 the Fourier conclusion is Xcrit, and critical derivative promotion remains an additional unproved gate. Nothing here takes r down to one.

## 4. Audit of exact zero normalization

The signed source-to-symbol relation itself is kinematic, not zero-specific. For any actual supported h with the derived subcritical moments, the complete source identity at matching enlarged support gives

    Q(h)-Re Q(h,tau_t h)
       =D_m(t)-(cosh(t/2)-1)Ppole(h)
       =E_h(t)-R_h(t).

It follows by subtracting the diagonal from the translated pairing even when Q(h) is nonzero. For an actual positive eigenmode q_h=mu h, the genuine exterior flux has the additional mu D_mass(t), which is removed by that diagonal subtraction. Therefore the same symbol comparison for E_h holds. The zero equation is required to identify F_h as the null exterior pairing, to place h in K_a, and for the contact contradiction; it does not automatically bound I.

A compact cusp is not an actual eigenmode or null solution. The existing positive native eigenmode control retains actual source custody but has nonzero mu. Its order-one source moment remains undecided. These controls cannot be renamed as actual zero-null counterexamples, and the narrower beta strip alone does not distinguish them.

Failed implication: exact source/form dictionary + |beta|<=3/8 + subcritical source moments + subtraction of the diagonal -> finite liminf signed cutoff trace on a zero kernel. The first three ingredients only prove the comparison above. A new bound must use the admissible exact-zero kernel to constrain the signed sum.

## Smallest next theorem and standing

Category: endpoint exclusion. A concrete next target is

    for every hypothetical nonnegative actual contact kernel,
    liminf_(epsilon down to 0) sum_basis sum_actual_copies
      J_(epsilon,3/2)(theta_q)(|p_q(h_j)|^2-|n_q(h_j)|^2)
    is finite.

A basiswise finite-liminf version also suffices, even on different sequences, because each W is monotone. This is actual arithmetic/source cancellation, not ordinary l2 localization or another conditional carrier realization.

Validation is analytic for the infinite-source Cauchy bound, epsilon-Fubini, the native symbol inequalities and finite-kernel promotion. Rational exponent/denominator controls and fixed-epsilon signed-sum comparisons are regression controls, not proofs of the missing bound. The external theorem remains the pinned accepted input from the previous pass, without a local dependency rebuild. No Lean build or axiom/CI claim. No aperture marching, prescribed packet substitution or same-vector enlarged cancellation. Canonical cursor and source custody updated additively; 24/25 certificate preserved. Global endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain unproved.
