# RPB108: fractional actual source moments locate the remaining tail gap

Date: 2026-10-06 (America/Los_Angeles). Live source 36258194fa49539ae6d73e2af2a83ae08e4eb5a7.
Definitions: [fractional positive-source moment registry](../docs/TERMINOLOGY_RPB108_FRACTIONAL_POSITIVE_SOURCE_MOMENTS.md).
Analytic source/Fourier equivalence and actual eigenmode control. The newer certified 24/25 aperture frontier is reused.

## Exact fractional comparison

For 0<s<1 and h in D_c,
\[
\boxed{M_{+,s}(h)<\infty\quad\Longleftrightarrow\quad V_s(h)<\infty.}
\tag{1}
\]
Moreover, after adding ||h||_log^2, the two quantities are comparable by finite fixed-support constants. Only the positive source moment is required; the base negative l2 norm is already controlled by logarithmic sampling.

This supplies the actual source version of the Fourier fractional regularity criterion. At s=1/2 it identifies the critical first-height positive moment with logarithmically strengthened H^(1/2). At s=1 the separately proved derivative difference-quotient theorem applies; the integral proof below must not be used there because its error budget ceases to be integrable.

## Translation proof and bounded strip error

Choose b>c and 0<t0<min(1,b-c). Both h and tau_t h belong to D_b for 0<t<t0. Keep the exact actual pair translation formula from the preceding height-moment theorem:
p(tau_t h)=exp(i theta t)(cosh(beta t)p+sinh(beta t)n), |beta|<=1/2.
Thus
\[
P_0(\tau_t h-h)=(e^{i\theta t}-1)p+r_t,
\qquad \|r_t\|_{\ell^2}\le C t(\|p\|+\|n\|).
\tag{2}
\]
Here the cosh-minus-one term is O(t^2), the sinh term O(t), and the phase has modulus one. All actual copies and source weights are unchanged.

The two squared-norm inequalities ||x+y||^2<=2||x||^2+2||y||^2 and ||x||^2<=2||x+y||^2+2||y||^2 show that the weighted integrals of the first term and the full observation in (2) differ in finiteness only by the remainder budget
\[
\int_0^{t_0} t^2 t^{-1-2s}\,dt
=\frac{t_0^{2-2s}}{2-2s}<\infty.
\tag{3}
\]
Bounded sampling and the positive observability lower bound at b compare the full observation with ||tau_t h-h||_log in both directions. This comparison uses actual physical translated tests, not arbitrary coefficient sequences.

For a real frequency lambda, substitution u=|lambda|t gives
\[
\int_0^{t_0}|e^{i\lambda t}-1|^2t^{-1-2s}dt
\asymp_s |\lambda|^{2s}
\quad(|\lambda|\ge1/t_0).
\tag{4}
\]
The full u integral is finite by the quadratic bound near zero and boundedness at infinity; a fixed subinterval with nonzero phase defect gives the lower bound. Low frequencies contribute at most a finite constant times the base l2 energy. Tonelli therefore converts the first observation integral into M_plus,s, modulo that base term.

On the physical side Plancherel gives
||tau_t h-h||_log^2=integral w(xi)|exp(-2pi i xi t)-1|^2|hhat|^2.
The same (4) and Tonelli convert its integral into V_s, again modulo base logarithmic energy. This proves (1) and the norm comparison. No support enlargement null equation, endpoint trace or derivative is assumed.

The same argument with the negative pair translation formula and bounded N0 also makes the negative height moment finite whenever (1) is finite. Positive observability is what makes the positive moment alone sufficient.

## What actual null bootstrap already supplies

For any 0<s<1/2 choose s<alpha<1/2. The existing actual full-null bootstrap gives h in H^alpha globally. Since |xi|^(2s)w(xi)<=C_(s,alpha)(1+|xi|)^(2alpha),
V_s(h)<infinity and hence M_plus,s(h)<infinity.

The bounds are uniform over a physical unit sphere in a finite kernel by choosing a finite basis, or directly from the existing fixed-window estimates. Therefore, for the full positive trace tail,
\[
E_{+,K}(T)=o(T^{-2s})\qquad(0<s<1/2).
\tag{5}
\]
Indeed T^(2s)E_plus,K(T) is bounded by the discarded weighted trace tail, which tends to zero. Thus actual source energy tails decay as o(T^(-1+epsilon)) for every 0<epsilon<1. These are genuine conditional actual-kernel estimates, stronger than merely tail->0, but below the first-height critical threshold.

| Source height order | Physical criterion | Current input |
| --- | --- | --- |
| 0<r<1 | Logarithmic fractional H^(r/2) | Follows from existing actual null bootstrap |
| r=1 | Logarithmically strengthened global H^(1/2) | Open; equivalent to critical integrated flux |
| 1<r<2 | Stronger fractional regularity | Not supplied by current bootstrap |
| r=2 | Derivative-log membership; on full-null vectors, global H1 | Full-kernel finiteness would exclude contact; unproved |

At r=1, the exact boundary-flux theorem gives
\[
M_{+,1/2}(h)<\infty
\iff\int_0^{t_0}|F_h(t)|t^{-2}dt<\infty
\tag{6}
\]
for actual full-null h. This follows by combining (1) with that theorem's Fourier criterion integral |xi|w|hhat|^2<infinity. No rank-one inverse-boundary injectivity is used.

The first-height moment by itself does not close the derivative-chain contradiction: it is below H1. The order-two target is exactly the preceding full-kernel endpoint criterion, requiring integral 2T E_plus,K(T)dT<infinity. Estimate (5) does not provide it.

## Actual positive eigenmode rejects a generic order-two estimate

The established actual native eigenmode control at c=47/50 supplies a real physical mass-one lowest eigenvector h outside H1, with mu=lambda_ph(c)>0. It retains all actual primes, pole and complete actual P0,N0 analyses. Its deviation from a native null vector is exactly the interior equation q_h=mu h.

The general derivative criterion from the preceding pass gives
\[
\boxed{\sum_q\theta_q^2|p_q(h)|^2=+\infty.}
\tag{7}
\]
This is now an **actual positive-source coefficient** control, not merely the geometric abstract sequence. The shifted bootstrap also gives every subcritical moment in (1), and ordinary source localization holds, yet the order-two moment is infinite. The full physical orthonormal lowest-eigenspace trace has the same infinite order-two moment because its regularity ceiling supplies a rough basis contribution.

Consequently no order-two positive-source moment theorem for every actual lowest eigenmode can follow from the current shift-stable prime/pole, log bootstrap, source boundedness and unweighted localization package. A candidate estimate must use the exact zero interior normalization to constrain the admissible vectors.

This does **not** show the order-one critical moment of that actual eigenmode diverges; non-H1 alone does not decide it. No actual source moment is numerically computed, and no actual nonzero zero-null vector or negative trial is constructed.

## Controls and smallest remaining theorem

The abstract geometric coefficient controls distinguish all subcritical moments from the critical moment: theta_j=2^(m j), p_j=2^(-m j/2), with even m. At s=(m-1)/(2m) the moment terms are 2^(-j), whereas at s=1/2 each term is one. Base energy and every finite logarithmic order are summable. These are coefficient controls, not actual divisor observations or compactly supported physical functions.

Category: endpoint exclusion. The concrete remaining theorem is still a sufficiently integrable actual positive order-two trace tail for the whole hypothetical zero kernel. A critical order-one estimate would close a regularity rung but requires a further lawful argument to reach exclusion. No missing bound is assumed.

Pinned source custody and repeated rational error-budget/rate controls: notes/data/RPB108_FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006.json. Fractional integral comparisons, source lower bounds and actual eigenmode existence are analytic applications of read results; controls do not certify those analytic statements. Existing source-count and critical-zero-density dependencies remain explicit through the cited records. No new external result, Lean file/build, axiom audit or CI claim. The entire newer 24/25 whole-domain certificate is preserved; no aperture calculations occur. Historical retained attachment, same-vector enlarged cancellation, F4 and FULL TRANSPORT CLOSED remain open.
