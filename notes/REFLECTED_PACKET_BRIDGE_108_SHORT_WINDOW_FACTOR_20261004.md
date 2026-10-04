# RPB108: short-window contraction and carrier recovery

Base: research 432982ba05056a53bc0e36bbd3ad00673094a74f.

## Independent external input and exact scope

Xuefeng Zhu, arXiv:2608.24827v2, Corollary 6.3, states Q(h)>=delta||h||_2^2 for arbitrary complex h supported in [-0.8,0.8], delta=8.9e-18. The form is the Weil autocorrelation form, including the Hermitian cross-pole term. The paper describes a computational certificate; we have read its theorem and normalization, but have not independently rerun that certificate or imported it into Lean.

Primary source: https://arxiv.org/pdf/2608.24827v2, Section 6, Corollary 6.3 and Lemma 6.1. Only this bounded range is used. No larger-window exploratory computation is promoted to a theorem.

## Application on the actual Green graph closure

Fix 0<a<=0.8. Let D_G be the actual Green graph closure in the complete Hilbert source graph. Write P,N for normalized full positive/negative analysis, N_s for selected negative analysis, B_s for its complement, k for the logarithmic coordinate and h=neutralLogPhysical(k) for the supported physical vector.

The certified source/native equality on D_G identifies
\[
Q_{\rm source}(w)=\|Pw\|^2-\|Nw\|^2=Q(h).
\]
Normalization is the one in ActualZetaSelectedBackground.lean: the extra 1/sqrt(2) removes the unnormalized source difference's factor two. Fourier variable t=2pi xi converts the multiplier integral to (1/2pi)int Psi(t)|F_h(t)|^2 dt. The pole is 2Re(conjugate(F_h(i/2))F_h(-i/2)); it is not a positive single square on arbitrary complex vectors. This agrees with the paper's complex/parity form.

For finite Green packets the physical vector is H1 and the identity is already certified. For general D_G limits, the native form is continuous in logarithmic norm, physical L2 reconstruction is continuous, and the full source coordinates converge in the graph topology. Thus the inequality extends from finite Green packets. Finite raw truncations approximate general Green lifts by continuity of the certified synthesis/lift; no density in the entire source graph is invoked.

The external lower bound gives
\[
Q_{\rm source}(w)\ge\delta\|h\|_2^2\ge0.
\]
The exact selected split gives
\[
Q_{B,s}(w)=Q_{\rm source}(w)+\|N_sw\|^2\ge0.
\]
Consequently
\[
\boxed{\|B_sw\|\le\|Pw\|,\qquad \ker P\subseteq\ker B_s.}
\]
Indeed the stronger full-negative estimate ||Nw||<=||Pw|| holds. The induced map T_0(Pw)=B_sw is therefore a contraction and extends uniquely to closure(P(D_G)). This is the actual WD-T10 norm estimate on D_G in this bounded range, using independent external positivity rather than assuming background positivity.

## Graph custody recovered by the positive norm

Let K=neutralActualZetaNativeLogError(a)+neutralPhysicalPoleEnergyConstant(a), the certified nonnegative mass-error coefficient in the Green-closure Garding theorem. That theorem says
\[
\|k\|_{\log}^2\le Q_{\rm source}(w)+K\|h\|_2^2.
\]
Strict positivity gives ||h||_2^2<=Q_source/delta. Since Q_source<=||Pw||^2,
\[
\|k\|_{\log}^2\le(1+K/\delta)\|Pw\|^2.
\]
The actual Hilbert source graph stores unnormalized source coordinates sqrt(2)P and sqrt(2)N. Its norm obeys
\[
\|w\|_{\rm graph}^2
 =\|k\|_{\log}^2+2\|Pw\|^2+2\|Nw\|^2
 \le(5+K/\delta)\|Pw\|^2.
\]
The reverse continuity is automatic from coordinate projection.

D_G is a closed linear subspace of the complete source graph. Hence P(D_G) is closed: a Cauchy sequence of positive coordinates is graph-Cauchy by this estimate, and its graph limit remains in D_G. P is injective because P=0 forces h=0, and weighted physical reconstruction is injective. Thus the positive-energy completion is canonically boundedly equivalent to this same Green graph carrier, preserving both source coordinates and physical logarithmic custody. The contraction B_s P^{-1} is already defined on the closed positive range.

This statement does not establish equivalence with the raw lp2/ker G inherited norm. That quotient may have a different synthesis-range topology; the estimate controls graph vectors by positive observations, not minimum raw coefficients.

## Neutral realization is excluded in this range

For nonzero w in D_G, h is nonzero: the graph dictionary and injective weighted reconstruction force w=0 whenever h=0. Therefore Q_source(w)>0.

If an actual full source operator null equation holds on w, its diagonal is zero, contradicting the strict bound. The same applies to the effective background operator null equation. An actual WD-T38 null witness whose attached quadratic is Q_source cannot be a nonzero vector in this short-window carrier.

The algebraic existence of a contractive background factor does not create attained unit gain or a physical null witness. Choosing a<=0.8 to obtain the factor therefore cannot supply a fresh neutral realization. Larger/enlarged windows and retained membership/source identification remain independent.

## Standing

This is a bounded-window analytic closure of the WD-T10 factor/carrier interface, conditional only on accepting the explicitly cited external theorem. It is not a general-window proof, a Lean certification, or FULL TRANSPORT CLOSED.

No Lean source/workflow changed. Latest certified Lean head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775; those checks do not certify the imported positivity result.

No actual off-line zero existence, full graph density, simplicity, spectral operator-domain membership or retained source/null attachment is assumed.

## Cursor/residue

At 432982b, Zhu arXiv:2608.24827v2 Corollary 6.3 supplies external analytic strict Weil positivity delta=8.9e-18 for arbitrary complex supported vectors in [-0.8,0.8]. On the actual Green graph closure for 0<a<=0.8, certified source/native equality gives Q_source>=delta||h||^2 and Q_background>=Q_source, hence WD-T10 unit domination and its induced contraction. Combining the certified Garding estimate E_log<=Q_source+K||h||^2 yields graph norm <=sqrt(5+K/delta)||P|| for the unnormalized source graph; the positive range is closed and positive completion recovers the same Green graph carrier. This does not identify the inherited raw lp2 quotient norm or claim full graph density. Strict positivity excludes a nonzero actual source-null WD-T38 realization in these windows. External theorem/certificate not reproduced or Lean-imported; deductions analytic. General/enlarged windows above0.8, retained same-vector source/null attachment and enlarged strict-persistence cancellation remain open. Do not choose a small window to manufacture neutral unit gain. FULL TRANSPORT CLOSED is not globally certified; SOURCE is off the critical path.
