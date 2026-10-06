# RPB108: one-sided Gaussian mass budget and a weaker endpoint exclusion criterion

Date: 2026-10-06 (America/Los_Angeles).
Source base: 4d65dd0898806f31f0389fd6542cbbc525d01334.
Definitions: docs/TERMINOLOGY_RPB108_ONE_SIDED_GAUSSIAN_BUDGET.md.
Lane: GLOBAL ENDPOINT / RETAINED ATTACHMENT -> F4.
Standing: new analytic theorem and exact algebra controls; not Lean certified.

## Result

Every nonzero compactly supported complex L2 vector satisfies
\[
\boxed{\quad
 \sum_{n=1}^\infty
 \frac{\log(\|h\|_2^2/M_n(h))}{1+n^2}<\infty .
 \quad}
\tag{1}
\]
Only the existing positive-frequency moving Gaussians, at the integer parameters R=n, are used. No second Fourier tail, reflection parity, H1 regularity, nonnegative source, or actual null equation is required.

Consequently an eventual one-sided bound
\[
M_n(h)\le C\|h\|_2^2 e^{-\omega(n)},\qquad
\sum_n\frac{\omega(n)}{1+n^2}=\infty
\tag{2}
\]
forces h=0. In particular both exponential decay and the weaker decay
\[
M_n(h)\le C\|h\|_2^2\exp[-n/\log(e+n)]
\tag{3}
\]
are impossible for a nonzero compactly supported vector.

Combining this with the retained actual Gaussian lower estimate gives a smaller sufficient endpoint input:
\[
\boxed{\quad
\Re\mathcal A_a(h;\overline{g_n})
 \le C_{a,h}\|h\|_2^2\exp[-n/\log(e+n)]
 \quad\hbox{for every sufficiently large integer }n.
\quad}
\tag{4}
\]
For an actual full-native null h, (4) would exclude h directly. This bound is not proved here. Constants and the eventual threshold may depend on h; no uniform condition number or packet selection is needed for this implication.

This closes the analytic implication from (4) to zero, not global endpoint exclusion or the historical Lean F-4 package.

## A bounded analytic function supplies the logarithmic budget

Suppose supp h is contained in [-a,a], a>0, and H=||h||_2>0. Compact support makes h L1, so
\[
F(z)=\int_{-a}^a h(x)e^{-2\pi i xz}\,dx
\]
is entire and |F(t)|<=sqrt(2a)H on the real axis. Fourier injectivity makes F nonzero.

The function
\[
f(z)=e^{-2\pi i az}F(z)
 =\int_{-a}^a h(x)e^{-2\pi i(x+a)z}\,dx
\]
is bounded analytic on the lower half-plane: x+a>=0 and Im z<0 make the integrand's exponential modulus at most one. Put B=max(1,sqrt(2a))H, so |f|<=B and B>=H.

Choose z0=x0-iy0 with y0>0 and f(z0)!=0. Map the disk conformally to the lower half-plane with its center sent to z0. If g is the resulting bounded analytic disk function, Jensen's formula at radius r<1 gives
\[
\frac1{2\pi}\int_0^{2\pi}
 \log\frac{B}{|g(re^{i\theta})|}\,d\theta
 \le\log\frac{B}{|g(0)|}.
\tag{5}
\]
Zeros on a circle are harmless integrable logarithmic singularities; use nearby radii if needed. The integrand is nonnegative. Fatou's lemma and continuity of the entire boundary F, except at the single boundary point mapping to infinity, therefore give
\[
\int_{\mathbb R}
 \log\frac B{|F(t)|}
 \frac{y0\,dt}{\pi[(t-x0)^2+y0^2]}<\infty .
\tag{6}
\]
The Poisson weight in (6) is bounded below by a positive constant times (1+t^2)^{-1}: its ratio to that weight is a positive continuous rational function with a positive limit at both infinities. Hence
\[
\int_{\mathbb R}\frac{\log(B/|F(t)|)}{1+t^2}\,dt<\infty.
\tag{7}
\]
This proof is elementary bounded analytic/Jensen/Fatou reasoning. No unproved quasianalytic or strip-holomorphy premise has been imported.

## Integer Gaussian windows turn that integral into (1)

Let I_n=[n/(2pi),(n+1)/(2pi)], of common length ell=1/(2pi). On I_n,
\[
(2\pi t-n)^2/n\le1/n\le1,
\]
so beta_n>=e^{-1} and
\[
m_n:=\int_{I_n}|F(t)|^2dt\le e M_n.
\tag{8}
\]
Each m_n and M_n is positive: an entire nonzero F cannot vanish on an interval. Jensen's inequality for the concave real logarithm gives
\[
\frac1\ell\int_{I_n}\log\frac B{|F(t)|}\,dt
 \ge\frac12\log\frac{\ell B^2}{m_n}
 \ge\frac12\log\frac{H^2}{M_n}
       -\frac12\log(2\pi e).
\tag{9}
\]
B>=H justifies the last step. Truncated logarithms or the integrability supplied by (7) justify the inequality at isolated zeros.

On I_n, 1+t^2<=C0(1+n^2) for one absolute C0. For example C0=3 suffices since 2pi>1 and (n+1)^2<=2(1+n^2). Multiplying (9) by ell/(1+n^2), summing the disjoint intervals, and applying (7) proves (1); the constant term sums because sum(1+n^2)^{-1}<infinity.

Notice that (1) is a weighted logarithmic budget, not a uniform lower mass bound at individual n. It permits small selected windows, long finite runs of small mass, and all the certified polynomial upper bounds.

## Decay exclusion and the nearly exponential profile

If (2) holds, then
\[
\log(H^2/M_n)\ge\omega(n)-\log C
\]
eventually. The finite sum of the constant correction cannot cancel a divergent omega budget, contradicting (1).

For omega(n)=n/log(e+n), divergence can be checked without asymptotic notation. For k>=1 and 2^k<=n<2^{k+1},
\[
e+n\le2^{k+3},\qquad
\frac{n}{1+n^2}\ge\frac1{2n}\ge2^{-k-2}.
\]
Since log 2<1, summing the 2^k indices gives
\[
\sum_{n=2^k}^{2^{k+1}-1}
 \frac{n}{(1+n^2)\log(e+n)}
 \ge\frac1{4(k+3)}.
\tag{10}
\]
The harmonic sum in k diverges, proving (3) impossible.

By contrast, polynomial mass suppression gives omega(n)=p log n and a finite budget. Dyadic blocks are bounded above by a constant times (k+2)/2^k, whose sum converges. Thus the current R^{-1+o(1)} estimates do not approach this criterion merely by improving their polynomial exponent.

## Actual signed action: the exact remaining endpoint theorem

The retained ACTUAL_MOVING_GAUSSIAN_COERCIVITY lower estimate, valid also at c=a, gives
\[
(\log n-C'_a)M_n
 \le\Re\mathcal A_a(h;\overline{g_n})
   +D_{a,a}(1+\log n)e^{-n/4}H^2.
\tag{11}
\]
Assume (4). For all sufficiently large n, log n-C'_a>=1 and log(e+n)>=8, so omega(n)<=n/8. Consequently
\[
(1+\log n)e^{-n/4}
 \le C_1 e^{-\omega(n)}
\]
for an absolute finite eventual C1: after factoring e^{-omega}, the remaining expression is at most (1+log n)e^{-n/8}, bounded on n>=1. Substitution in (11) yields (3), with an adjusted finite constant. The mass budget therefore forces h=0.

Only an upper bound on the real part is used; absolute action smallness is stronger than needed. The entire Gaussian has whole-line support, so this action is not killed by endpoint test-domain nullity. The prime/pole terms and the same physical h remain exactly those of the genuine full frozen action.

This implication works for every compact supported logarithmic h obeying (4), whether or not Q_a is nonnegative. For the global lane it is enough to prove (4) for full-null vectors at nonnegative windows. The previous contact dichotomy then gives all-window unit domination.

The criterion is independently unproved actual information. At a fixed a, a universal (4) for K_a is equivalent to K_a={0}, with the reverse direction vacuous. It must not be advertised as an automatic weaker arithmetic theorem merely because its numerical decay is weaker than exponential.

## Boundary and regularity attack disposition

Recovered signed action already satisfies the analytic R^{-1+o(1)} bound in SIGNED_GAUSSIAN_FRACTIONAL_PAIRING_20261005. It does not satisfy (4), and the logarithmic budget gives no contradiction with that result. Translation flux supplies a critical half-derivative criterion, not the nearly exponential action bound.

The previous entry audit mentioned H^{1+epsilon} as a sufficient regularity route. The stronger L2_NULL_DOMAIN_PROMOTION theorem already shows that K_a subset global H1 suffices: an L2 derivative automatically promotes back into D_a and K_a, making differentiation an endomorphism of the finite kernel. For an individual vector the sharper obstruction is K_a intersect H^r={0}, r=dim K_a. This is an additive clarification; no H1 conclusion is newly derived.

The failed implications remain precise:
- polynomial/subpolynomial action upper bound -> divergent Gaussian logarithmic decay budget: FALSE, by convergence of the polynomial budget;
- endpoint mixed nullity -> (4): NOT PROVED; the Gaussian is not an endpoint supported test;
- a scalar inverse moment zero -> (4) or h=0: INVALID on the general carrier, as the retained polynomial controls show;
- full-null supported L2 -> enlarged same-vector nullity: obstructed by the retained translation theorem.

The remaining theorem belongs to endpoint exclusion, not retained packet attachment or null transport. No historical packet is replaced. No dilation or enlarged cancellation is used.

## Validation and custody

Analytic checks: Fourier sign and lower-half-plane shift, disk Jensen orientation, nonnegative Fatou integrand, Poisson weight comparison, the exact beta_n interval, both logarithm normalizations, and the harmonic divergence all appear explicitly. The associated exact-rational control verifies the Gaussian exponent ceiling and dyadic comparison constants, and distinguishes the summable polynomial control from the divergent profile. It does not certify complex analysis or actual-zeta estimates.

Primary repository sources read at the base:
- GLOBAL_F4_ENTRY_AUDIT_20261006;
- ACTUAL_MOVING_GAUSSIAN_COERCIVITY_20261004;
- SIGNED_GAUSSIAN_FRACTIONAL_PAIRING_20261005;
- FRACTIONAL_NULL_REGULARITY_20261005;
- EXACT_TRANSLATION_BOUNDARY_FLUX_20261005;
- INVERSE_MOMENT_OBSERVABILITY_AUDIT_20261005;
- L2_NULL_DOMAIN_PROMOTION_20261006.

No Lean module, workflow or historical note changes. No new Lean build/axiom audit or arithmetic estimate is claimed. F4, historical retained attachment, global endpoint exclusion and FULL TRANSPORT CLOSED remain open.

New global-lane cursor: derive or refute the genuine actual endpoint real-action bound (4), or prove global H1 membership of the nonnegative kernel. The implication from either criterion to endpoint exclusion is now shorter; another fixed-aperture decimal is not required by this pass.
