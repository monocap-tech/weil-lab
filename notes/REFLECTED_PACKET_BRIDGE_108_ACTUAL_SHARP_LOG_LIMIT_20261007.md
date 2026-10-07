# RPB108: the actual null equation supplies the missing signed Tauberian bound

Date: 2026-10-07 UTC. Recovered live head 87b5e7574e3d6519cb6b94ec4da2ddc0c15fb999.
Definitions: [actual sharp logarithmic limit](../docs/TERMINOLOGY_RPB108_ACTUAL_SHARP_LOG_LIMIT.md).
Category: endpoint exclusion / actual weak critical source tail. Analytic, not Lean-certified.

## Result

Every h in a fixed actual full-native kernel satisfies the stronger borderline UNSIGNED estimate

    V_h(T)=sum_(|theta_q|>T)(|p_q(h)|^2+|n_q(h)|^2)<=C_h/T.

It follows that, for every sufficiently large T,

    |A_(1/T)(h)-S_h(T)|<=2C_h,
    S_h(T)/log T -> (2/pi)|kappa_R(h)|^2.

The whole physical kernel trace has the corresponding limit (2/pi)Lambda_K. Thus a single unbounded height subsequence with bounded-above sharp signed trace, or more generally with nonpositive normalized liminf, now suffices to exclude actual contact. Producing such an ACTUAL arithmetic subsequence remains unproved.

This closes the Tauberian transfer gate for the actual kernel. It does not prove the needed sign bound. The previous general warning about sharp subsequences remains valid on its stated carrier; its paired-atom control does not satisfy the newly derived O(1/T) unsigned tail. No historical wording is rewritten.

## 1. Exact null correlation bounds the canonical translation defect

The preceding actual slope theorem proved

    -Re Q(h,tau_t h)=|kappa_R(h)|^2 t+o_h(t), t down to 0,

by the exact interior zero equation and strong rescaled endpoint traces. The native convolution/pole identity is

    Q(h)-Re Q(h,tau_t h)
       =D_m(t;h)-(cosh(t/2)-1)Ppole(h).

For actual Q(h)=0, the pole term is O_h(t^2), and therefore D_m(t;h)=O_h(t). The already established symbol/core envelope gives

    D_m(t;h)>=D_w(t;h)/2-Zcore t^2 ||h||_2^2.

Consequently D_w(t;h)=O_h(t). The finite low-frequency negative core is charged to t^2; no positivity of m0 at every frequency is assumed. This is a stronger endpoint translation estimate than merely having every subcritical Sobolev norm. It is not Xcrit: integrating O(t)/t^2 still permits logarithmic divergence.

## 2. Actual bounded sampling and pair translation give U_h(t)=O(t)

Choose one fixed b>a and t0<min(1,b-a). Both h and tau_t h lie in D_b. The complete analysis is bounded there, say ||Gamma v||<=L_b||v||_D. Only the existing UPPER sampling bound is used, not an inverse onto arbitrary coefficient packets. Source normalization is support independent.

On each actual pair, with gamma_q=(p_q,n_q), the exact law is

    gamma_q(tau_t h)=exp(i theta_q t) H_(beta_q t) gamma_q(h),
    H_x=[[cosh x,sinh x],[sinh x,cosh x]].

The accepted |beta|<=B=3/8 gives ||H_(beta t)-I||<=Bt exp(Bt). Subtract the phase-only difference from the actual pair difference, then use the triangle and squared-norm bounds in the COMPLETE positive source metric:

    2U_h(t)<=2||Gamma(tau_t h-h)||^2
               +2B^2 t^2 exp(2Bt)||Gamma h||^2
             <=4L_b^2 D_w(t;h)+2B^2 t^2 exp(2Bt)||Gamma h||^2.

Thus U_h(t)<=C t for 0<t<t0. Both actual channels are retained. This estimate cannot be obtained by compactness of a selected negative operator alone, and introduces no auxiliary rows or carrier changes. The translated physical vector changes only as a lawful test at b; h is never assumed null there.

## 3. An elementary averaging bound yields the unsigned O(1/T) tail

For T>=1/t0, Tonelli applies to the nonnegative source series:

    T integral_0^(1/T) U_h(t)dt
       =sum_q [1-sin(theta_q/T)/(theta_q/T)]v_q(h)
       <=C/(2T).

At theta=0 the bracket is defined by its zero limit. For |x|>=1 it is at least 1/24. Indeed for |x|>=2 use |sin x|<=1. For 1<=x<=2, write the bracket as integral_0^1(1-cos(xs))ds and restrict to 0<s<1/x. The elementary bound 1-cos u>=u^2/4 on [0,1] gives 1/(12x)>=1/24. Evenness covers negative x.

Therefore V_h(T)<=12C/T for large T. Enlarge the constant to cover the finite initial interval using ||Gamma h||^2; then V_h(T)<=C_h/T for every T>0. Local zero counting retains finite heads, but no copy independence is inferred.

Summing over a physical orthonormal basis gives a basis-independent whole-kernel unsigned tail V_K(T)<=C_K/T. Its constant is finite; no optimized number or larger-aperture certificate is required.

## 4. Bounded Abel-minus-sharp error without a signed Tauberian assumption

For tau=1/T, alpha_tau(u)=(1-exp(-tau u))/tau satisfies

    0<=u-alpha_(1/T)(u)<=u^2/(2T),
    0<=alpha_(1/T)(u)<=T.

Let d_q=|p_q|^2-|n_q|^2, so |d_q|<=v_q. Split at |theta|=T. Absolute summation is legal and gives

    |A_(1/T)-S(T)|
       <=[1/(2T)] sum_(|theta|<=T) theta^2 v_q+T V_h(T).

The unsigned layer-cake identity proves

    sum_q min(theta_q^2,T^2)v_q
       =integral_0^T 2u V_h(u)du<=2C_h T.

The head second moment is no larger. Hence the difference is at most 2C_h, uniformly in T. This is the missing absolute error estimate: signed oscillations are controlled by the derived UNSIGNED tail, not by an unproved sign of the graph projector commutator.

The preceding actual Abel/log limit now passes directly to the sharp head:

    S_K(T)/log T -> (2/pi)Lambda_K.

No general signed Tauberian theorem is imported, and no unregularized divergent moments are subtracted. The formula also identifies a sharper actual source-tail bound; it does not say that the unsigned critical height moment is finite.

## 5. Why the earlier subsequence control does not apply

The preserved abstract paired-atom control has positive squared mass (9/4)j4^(-j) at height 4^j, negative squared mass (9/8)j4^(-j) at height 2*4^j, and a negative mass at zero. Its sharp head returns to zero repeatedly despite a divergent Abel defect. At T_j=4^j/2, however,

    T_j V(T_j)>=(9/8)j -> infinity.

It lacks the O(1/T) unsigned bound and cannot refute the new ACTUAL implication. The old general-carrier warning remains correct. This additive refinement identifies the extra hypothesis that actual full-nullity now provides.

Conversely, O(1/T) unsigned tails and neutral unweighted norms still do not force a nonpositive logarithmic coefficient. For a simple separate coefficient control take theta_j=2^j, positive squared masses 2^(-j), and negative squared mass one at theta=0. Both base norms are one. Its unsigned tail is <=2/T and its sharp head is floor(log T/log 2), with positive logarithmic coefficient. This is not an actual divisor or physical-null model; it guards against turning the new tail theorem into a sign theorem.

The previous coherent compact-good-row physical control also has positive logarithmic slopes; its artificial rows are not the actual dictionary. No control is renamed as an actual zero kernel.

## 6. Actual positive-eigenvalue control and exact remaining obligation

The pinned fixed physical eigenspace q_h=mu h obeys the same result. The preceding slope note explicitly proved D_mass=o(t) and D_m=|kappa_R|^2t+o(t), using its exact eigen equation and a low/high frequency split. Bounded complete sampling then supplies U=O(t), V=O(1/T), and the bounded Abel-minus-sharp error exactly as above.

The ACTUAL rough positive eigenmode therefore has

    S_h(T)/log T -> (2/pi)|kappa_R(h)|^2>0.

This strengthens the old limsup statement and shows that no shift-invariant tail argument proves the new sign target. The actual zero-contact theorem still must use the zero interior residual; the positive mode has mu<h,v> instead of zero.

For hypothetical nonzero actual K, Lambda_K>0 by the closed trace/derivative obstruction. The smallest sufficient arithmetic theorem on this sharp route is now

    liminf_(T to infinity) S_K(T)/log T<=0,

or any construction of an unbounded height sequence with that upper property. A bounded-above subsequence is enough. The theorem does not require a uniform bound at all large heights, but it DOES require actual source/zero arithmetic; no such sequence or bound is proved here. With the derived limit, producing it is equivalent to whole-contact trace vanishing.

Endpoint exclusion, retained historical attachment, same-vector enlarged full-null transport and F4 remain open. No aperture marching; certified 49/50 is preserved. Publication recovers newer concurrent head 1abf19e7abe8e85c7b899503bac6eaaa43239231 with complete 99/100 native/source custody; its full matched Gram and corrected coupling sign remain pending. The newer cursor is preserved rather than reset to the initial head.

## Validation and source custody

Six pinned repository inputs in the manifest retain the actual correlation, symbol envelope, complete sampling/pair law, averaged traces, positive-eigenvalue control and previous physical obstruction. The companion checks the rational cosine lower margin, independent atomic layer-cake identities, weak-tail/error budgets, and rejection of the old paired-atom control's O(1/T) premise. Those finite checks are not an analytic proof, actual arithmetic certificate, Lean build or axiom audit. No new external theorem is imported. Historical claims remain immutable; this is an additive actual-kernel refinement.

All six source blobs were verified at the live recovered head. The local positive-source-height mirror had an extra terminal newline; retrieval-only normalization restores the verified source bytes. No historical source is edited in the repository by this publication.
