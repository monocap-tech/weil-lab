# RPB108: a polynomial Gaussian action moment is exactly derivative energy

Date: 2026-10-06 (America/Los_Angeles). Source `565bc84b6502545d672d5977946030a8f7941397`.
Definitions: [Gaussian action moment](../docs/TERMINOLOGY_RPB108_GAUSSIAN_ACTION_MOMENT.md).
Global/F4 lane; no aperture computation.

## Actual action criterion

Fix a>0 and a complex supported logarithmic vector h. Use the unchanged project Gaussian K_n, beta_n(xi)=exp(-(2pi xi-n)^2/n), and the genuine full frozen action. Set
\[
a_n(h)=\Re\mathcal A_a(h;\overline{K_n*h}),\qquad
v_n=\frac{n^{3/2}}{\log(e+n)},\qquad
S_+(h)=\sum_{n=2}^{\infty}v_n(a_n(h))_+.
\]
Then
\[
\boxed{S_+(h)<\infty
\quad\Longleftrightarrow\quad
\int_{\xi>0}\xi^2|\widehat h(\xi)|^2d\xi<\infty.}
\tag{1}
\]
In particular, with physical reflection Jh(x)=h(-x),
\[
\boxed{h\in H^1(\mathbb R)
\quad\Longleftrightarrow\quad
S_+(h)+S_+(Jh)<\infty.}
\tag{2}
\]
For real h, Fourier conjugate symmetry makes the two derivative tails equal, so S_+(h)<infinity alone is equivalent to global H1.

These are analytic actual-action equivalences. They need neither endpoint nullity nor enlarged cancellation. They are not a proof that the moment is finite for an actual null vector.

At any hypothetical nonnegative null window the full native kernel is finite-dimensional and has a real basis. Proving finiteness of this action moment for each vector in that basis would put the entire kernel in H1. Automatic derivative promotion and Fourier-polynomial independence would then exclude the kernel. This is a polynomial summability endpoint target, distinct from historical F4's exponential-weight conclusion.

## Lower Gaussian overlap recovers derivative energy

The retained actual lower estimate, including the true signed pole contribution, gives
\[
a_n(h)\ge(\log n-C'_a)M_n(h)
-D_a(1+\log n)e^{-n/4}\|h\|_2^2,
\qquad
M_n=\int\beta_n|\widehat h|^2.
\]
Choose a fixed N0 so that log n-C'_a>=log(e+n)/2 for n>=N0. The weighted error is summable. Therefore finite S_+(h) implies
\[
\sum_{n\ge N0}n^{3/2}M_n(h)<\infty.
\tag{3}
\]
Indeed the lower estimate bounds half of each n^(3/2) M_n by v_n(a_n)_+ plus the summable error.

Write x=2pi xi. For x sufficiently large, restrict the sum in (3) to integers satisfying |n-x|<=sqrt(x)/2. Such n are at least x/2 and at least N0. There are at least sqrt(x)/2 of them. On this set
\[
\frac{(x-n)^2}{n}\le\frac12,\quad
\beta_n\ge\frac12,\quad
n^{3/2}\ge\frac{x^{3/2}}4.
\]
Here e^(1/2)<2 follows directly from the exponential series or e<4. Hence
\[
\sum_{n\ge N0}n^{3/2}e^{-(x-n)^2/n}\ge x^2/16.
\tag{4}
\]
Tonelli applied to (3)-(4) proves the positive-frequency derivative integral finite. Its bounded-frequency part is finite by physical L2 membership.

The extra sqrt(x) in (4) is why the action weight has power 3/2 rather than power 2: adjacent Gaussian windows overlap on about sqrt(x) integer centers. No single-frequency lower mass bound is assumed.

## Upper overlap proves the converse with the same weight

Define
\[
W(x)=\sum_{n=2}^{\infty}
\frac{n^{3/2}}{\log(e+n)}e^{-(x-n)^2/n}.
\]
There is an absolute finite C such that
\[
W(x)\le C\frac{(1+x)^2}{\log(e+x)}\quad(x\ge0),
\qquad W(x)\le C e^{-2|x|}\quad(x<0).
\tag{5}
\]
For x>=4, split the sum into n<x/2, x/2<=n<=2x and n>2x. In the central part the coefficient is at most C x^(3/2)/log(e+x), and the exponent is at most exp(-(n-x)^2/(2x)). The elementary Gaussian lattice sum is bounded by C sqrt(x): separate the nearest lattice points and compare the decreasing tails with the Gaussian integral. This gives the central bound in (5).

For n<x/2, the exponent is at most e^{-x/2}; at most x terms with coefficient at most C x^(3/2) give C x^(5/2)e^{-x/2}, which is bounded by the right side of (5). For n>2x, the exponent is at most e^{-n/4}; its polynomially weighted sum is uniformly finite, again bounded by that right side. For x in [0,4], the same exponential tail bounds the sum uniformly. If x<0,
\[
(x-n)^2/n=n+2|x|+x^2/n\ge n+2|x|,
\]
which proves the negative-tail bound.

The exact action dictionary is
\[
\mathcal A_a(h;\overline{K_n*h})
=\int m_a(\xi)\beta_n(\xi)|\widehat h(\xi)|^2d\xi
+\operatorname{pole}_n(h).
\]
The retained envelope |m_a|<=w+C_a and exact pole bound
\[
|\operatorname{pole}_n(h)|
\le4ae^a e^{-n+1/(4n)}\|h\|_2^2
\]
keep the actual prime and pole terms. Summing absolute values, Tonelli and (5) give
\[
\sum_{n=2}^{\infty}v_n
|\mathcal A_a(h;\overline{K_n*h})|
\le C_a^*\left(\|h\|_2^2+
\int_{\xi>0}\xi^2|\widehat h(\xi)|^2d\xi\right).
\tag{6}
\]
On positive frequencies w(xi) times W(2pi xi) is at most C(1+xi^2); on negative frequencies it is bounded because of the exponential in (5). The pole errors sum. Thus finite one-sided derivative energy proves S_+(h) finite. This completes (1). Reflection gives (2), since Fourier(Jh)(xi)=Fourier(h)(-xi).

The action is evaluated on a whole-line Schwartz Gaussian convolution. It is not a supported endpoint-domain test, and the endpoint null equation is never used to declare it zero.

## Signed partial sums and the arithmetic target

The same retained lower estimate implies
\[
\sum_{n=2}^{\infty}v_n(a_n(h))_-<\infty,
\tag{7}
\]
because the coefficient of M_n is nonnegative eventually and the finitely many earlier actions are finite. Therefore S_+(h)<infinity is equivalent to finite liminf of the signed weighted partial sums
\[
\liminf_{N\to\infty}\sum_{n=2}^N v_n a_n(h)<\infty.
\tag{8}
\]
There is no cancellation loophole: the negative-part budget in (7) is finite. If the positive-part budget diverges, the signed sums tend to positive infinity. Bounds at a sequence of truncation indices would suffice for (8).

The actual form has real coefficients: its multiplier is real and even, paired prime translations preserve reality, and the pole kernel is real. Hence its full kernel is invariant under complex conjugation. Taking real and imaginary parts identifies it with the complexification of its real fixed subspace. A real basis of that subspace is also a complex basis of K.

A sufficient global arithmetic theorem is thus (8) for every vector of a real basis of K at every hypothetical nonnegative actual contact. By (1), each such vector is H1; all of K is H1, and the existing finite-dimensional derivative contradiction excludes contact. The real basis may depend on the window. No common aperture selection or uniform numerical constant is needed for this implication. At a nonnegative window the universal basiswise moment theorem is itself equivalent to kernel exclusion, with the reverse direction vacuous. The polynomial criterion is a new observation formulation, not evidence that the actual arithmetic bound is automatic or easier to prove.

Equivalently one may require (2) basiswise without making a real basis choice. Reflection in (2) changes the physical vector; for a real vector no physical reflection is needed because the Fourier energy is already symmetric. Neither device is same-vector enlarged/null transport.

## A concrete polynomial sufficient bound, and its scope

For any delta>0 an eventual bound
\[
(a_n(h))_+\le C_h n^{-5/2}
(\log(e+n))^{-\delta}
\tag{9}
\]
implies the moment finite, because the weighted terms are bounded by
\[
\frac{C_h}{n(\log(e+n))^{1+\delta}},
\]
a summable series. Any exponent strictly greater than 5/2 also suffices. The bare n^(-5/2) control does not suffice for the implication, since its weighted series has divergent 1/(n log(e+n)) scale.

The aggregate target (8) is weaker than imposing a particular bound such as (9). H1 implies the aggregate bound by (6), but need not impose the stated pointwise decay profile. The available actual R^(-1+o(1)) action estimate supplies neither (8) nor (9). Improving constants in that existing bound would not close the exponent/summability gap.

For a one-dimensional kernel, one real full-null vector meeting (8) would already contradict derivative promotion. For higher nullity, one regular vector need not suffice; the real-basis or entire-kernel quantifier is essential. In fact at a nonzero contact at least one vector of every real kernel basis has infinite S_+, by the strict regularity flag. This is a conditional divergence statement, not actual contact existence.

The earlier one-sided logarithmic Gaussian mass budget rejects sufficiently fast decay for any individual nonzero compact vector. The present polynomial criterion uses finite nullity and derivative promotion on the entire kernel instead. It does not improve that general logarithmic-budget theorem or prove historical F4 exponential Fourier weight.

## Remaining implication, custody and standing

The exact missing implication is actual endpoint mixed nullity -> basiswise signed weighted Gaussian action summability (8). The lower estimate, real symmetry and frame comparison establish what such summability would buy; they do not establish it. This belongs to endpoint exclusion. Prescribed retained packet identity and actual full-null attachment retain their independent gates.

The physical h is unchanged in each action sequence. The moving convolution is a test vector, not a new null vector. No dilation, enlarged central cancellation, selected-background nullity or single inverse-boundary-moment injectivity is used.

Pinned sources and repeated rational Gaussian-overlap/rate controls are in notes/data/RPB108_GAUSSIAN_ACTION_MOMENT_20261006.json. The lattice summation and actual Fourier/action arguments are analytic proofs, not certified by sampled controls or Lean. No Lean/compiler/workflow changes or new axiom audit. Historical wording is preserved. Certified whole-domain aperture 93/100 and concurrent larger-aperture work remain untouched. F4 and FULL TRANSPORT CLOSED remain open.
