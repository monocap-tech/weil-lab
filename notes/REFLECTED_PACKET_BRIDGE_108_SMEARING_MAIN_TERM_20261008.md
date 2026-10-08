# RPB108 NF59: fixed-width prime-only smearing cannot stay positive globally

Date: 2026-10-08 UTC. Recovered head fba75ed4eda84f0c71286f314f85b0d29db0202a.
Definitions: [smearing main-term mismatch](../docs/TERMINOLOGY_RPB108_SMEARING_MAIN_TERM.md).

## Direct lower-bound attempt and outcome

For EVERY fixed nonzero width delta in the NF57 range, the prime-only smeared form is negative on smooth nonnegative physical packets in sufficiently large supported windows. Indeed its physical Rayleigh values tend to minus infinity along the family below.

This is unconditional using the classical prime number theorem. It does NOT construct a negative vector for the ORIGINAL Weil form and does not imply an off-line zeta zero. It rules out an all-window positive lower bound for this approximation with one fixed width. NF57 and NF58 remain valid at each fixed aperture with their stated error budgets. Adaptive widths are not ruled out.

## Imported arithmetic input and weighted consequence

Use only psi(X)=sum_(n<=X)Lambda(n)~X. A checked primary author-hosted source is K. Kedlaya, *Notes on analytic number theory*, [the prime number theorem](https://kskedlaya.org/ant/chap-pnt.html), together with [Chapter 8, Definition 8.1 and Theorem 8.7](https://kskedlaya.org/ant/chapter-8.html), which give the von Mangoldt formulation and an unconditional error bound stronger than needed. The half-weight convention at isolated endpoints does not affect the asymptotic; the discrete measure here retains full prime-power atoms.

For every fixed smooth compactly supported test phi on the logarithmic displacement line, the theorem implies

    exp(-R) sum_(n>=2) Lambda(n)/sqrt(n) phi(log n-2R)
       -> integral_R exp(u/2)phi(u)du.                       (1)

To check the weight and scale, put X=exp(2R) and t=n/X. The left side is the integral of t^(-1/2)phi(log t) against dpsi(Xt)/X. On the fixed compact t-support bounded away from zero, psi(Xt)/X converges uniformly to t. Integration by parts gives convergence against this smooth test to dt. Substitution t=exp(u) yields (1).

No shrinking-prime-interval theorem is imported: delta and phi are FIXED before R increases. No uniformity as delta varies with R follows from (1).

## Smooth actual physical packets

Choose a real nonnegative nonzero smooth psi supported in [-b,b]. Let

    h_R(x)=psi(x-R)+psi(x+R),
    a_R=R+b+delta,  R>b,
    J_psi=integral exp(u/2)C_psi(u)du
         =M_+(psi)M_-(psi)>0.

The two bumps have disjoint supports and mass 2||psi||_2². Their complete correlation is

    C_(h_R)(s)=2C_psi(s)+C_psi(s-2R)+C_psi(s+2R).

Every prime term whose smeared correlation is nonzero lies in the COMPLETE active dictionary at a_R. In particular, the cross term has log n<=2R+2b+delta<2a_R. Thus a missing outside threshold cannot cause the asymptotic below.

The original pole cross term is

    2exp(R)J_psi+O(exp(-R)).                                 (2)

Its self terms are fixed. The archimedean Euler difference kernel k(s)=exp(-s/2)/(1-exp(-2s)) makes its cross term O(exp(-R)); its self terms are fixed as well. These estimates follow directly from the unchanged actual physical dictionary on smooth supported packets.

For the averaged prime cross term, use

    phi_delta(u)=(1/(2delta))integral_(-delta)^delta C_psi(u+v)dv.

This is a fixed smooth compact test. Its weighted integral is

    integral exp(u/2)phi_delta(u)du
       =alpha_delta J_psi,
    alpha_delta=(1/(2delta))integral_(-delta)^delta exp(-v/2)dv
               =sinh(delta/2)/(delta/2)>1.                  (3)

Equation (1) and the original negative prime coefficient -2 show that this cross term is -2alpha_delta exp(R)J_psi+o(exp(R)). All averaged prime self terms remain fixed.

Consequently

    Q_(a_R,delta)(h_R)/exp(R)
       -> 2(1-alpha_delta)J_psi<0.                          (4)

Since physical mass is constant, its smeared physical Rayleigh quotient tends to minus infinity. This proves the failure of the proposed fixed-width all-window lower bound, rather than merely showing that an absolute estimate is inconclusive.

For comparison, the SAME argument with UNSMEARED actual primes has alpha=1 and gives Q_(a_R)(h_R)/exp(R)->0. That statement supplies no sign for the lower-order ORIGINAL value. The negative leading term in (4) is introduced by this approximation's mismatch.

## What a repair does and does not establish

Multiplying the ENTIRE original pole by alpha_delta cancels the leading mismatch in (4). This is exactly the exponential moment of the averaging kernel; both signed hyperbolic pole slots must be scaled. Then the pole-matched comparison form divided by exp(R) tends to zero on this family. No sign for its remaining value is inferred.

At fixed a its additional approximation error obeys

    |(alpha_delta-1)Pole_a(h)|
       <=(alpha_delta-1)4a exp(a)||h||_2².

Thus an NF58 eigenvector sign-transfer calculation for this MODIFIED form would have to add that explicit error to its prime-smearing budget. It cannot treat the scaled pole as the original actual source term. Nor does matching a main term prove whole-domain positivity.

Alternatively choose a width depending on aperture and prove a lower bound and transfer error at EACH aperture. The fixed-delta proof does not exclude this. It supplies no justified aperture-dependent width, lower margin, or uniform prime remainder estimate for that route.

This pass therefore narrows the next arithmetic task: a fixed-width prime-only global lower bound is impossible; any surviving smearing route must either control adaptive widths or explicitly correct the main-term mismatch and retain the correction cost. Further generic moment refinement cannot supply that lower bound.

## Validation and standing

Exact rational series controls check alpha_delta>1, its delta²/24 leading excess, the signs of the unmatched/matched coefficients, and the retained pole-error term. The prime-number-theorem limit and actual smooth-packet argument are analytic. No finite negative aperture or numerical physical witness is located, and no Lean certification is claimed.

NF55's original source-gain target remains open. Aperture-one, all original divisor/pole/threshold custody and concurrent fronts are preserved. No original negative vector, new positivity interval, global exclusion, RH, F4 or full transport claim.
