# NF523 — Original endpoint logarithmic carrier: sharp regularity, operator-graph approximation, and the 242-moment image obstruction

**November 14, 2026 PT. Original NF494 exact-rational local source check PASS; independent reverse-Horner/source check and six-direction rational moment-correction control PASS.** This is a **source-image / graph-domain mathematical increment**, not a new finite physical NO-GO, Weil sign certificate, or proof/counterexample to RH. It is stacked on NF522 draft PR #551; no merge to main; dedicated GitHub CI not accepted.

## What the older branches actually established

NF522 locally certified three **specific finite-selected physical NF404 sufficiency failures** on H4094, H4095 and their union. None proves the presence, absence, or sign of an *admissible* infinite-dimensional Weil quadratic form. The earlier October actual-source graph Lean sources already distinguish these objects:

- `WeilDefect/Arithmetic/ActualZetaSourceGraph.lean`: closed **two-source coordinate graph** with actual divisor multiplicities; Green lifts enter it.
- `WeilDefect/Arithmetic/ActualZetaGreenPacketDensity.lean`: finite actual Green packets are dense **in the closed Green-lift subspace**, NOT proved dense in the entire actual source graph. Its orthogonal-packet criterion does not prove the full complement zero.
- `WeilDefect/Arithmetic/ActualZetaHilbertSourceGraph.lean`: source operator is bounded on the constructed **Hilbert graph**, explicitly not a physical Weil-operator identification.
- `WeilDefect/Morphology/NeutralLogSourceDomainRealization.lean`: lawful source-domain realization is conditional on a domain attachment carrying support/log energy. It does not manufacture the attachment for a selected physical vector.
- `WeilDefect/Morphology/NeutralSourceOperatorDomain.lean`: the *actual* operator-domain spectral-product criterion is stronger than finite one-logarithm **form** energy. Exact spectral-product membership and the required interior source cancellation are separate premises.

NF498 already showed the genuine terminal logarithmic carrier is in supported physical L² but is not H¹ and cannot simply be declared a 243rd analytic selected generator. NF523 resolves its **sharp fractional regularity** and the *natural Fourier-multiplier operator-domain* question, while keeping the actual divisor source-image and exact test-identification problems OPEN.

## 1. The unchanged original arithmetic-source terminal logarithm

Fix the authentic old J8 right endpoint B=11/10 and terminal collar δ=1/500. NF492/NF494 source-certified the complete original W decomposition with the same original U(B-d):

\[
W(B-d)=H(d)+U(B) C_8+\frac{U(B-d)}2\log\frac Bd,
\quad0<d<\delta.
\]

Define the *same NF498 candidate* on the entire original physical carrier I=[−B,B]:

\[
\boxed{\ell_U(x)=\operatorname{sgn}(x)\mathbf1_{\{B-\delta<|x|<B\}}
\frac{U(|x|)}2\log\frac B{B-|x|}.}
\]

This is a **diagnostic original-source-built vector**. Neither the original test-image equation nor the full divisor graph membership has been established simply by writing it down.

The actual **full 400 U-source coefficient** SHA256 is `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`; it pins original NF407 and NF406 sources and the holomorphic radius 1/25. In exact rational arithmetic, including **all 400 outward coefficients** and the original analytic Cauchy tail with M=10^400, we certified

\[
\boxed{U(B)<-10^{-11},\quad
\sup_{0\le d\le\delta}|U(B-d)|<2\cdot10^{-7},\quad
\sup_{0\le d\le\delta}|U'(B-d)|<7\cdot10^{-4}.}
\]

Actual source outward absolute-sum envelopes are about `1.9659655557684862e-7` and `6.957098822919963e-4`; the nonzero signed endpoint value is ~`−1.16798644909683007032e−11`. The higher-jet function and derivative tails were separately paid:

\[
T_0=10^{400}\frac{(1/20)^{400}}{1-1/20}<5\cdot10^{-121},\qquad
T_1=25\cdot10^{400}(1/20)^{399}
\left(\frac{400}{1-1/20}+\frac{1/20}{(1-1/20)^2}\right)<10^{-114}.
\]

The U-function tail reproduces the **actual archived NF494 analytic Cauchy tail exactly**; the derivative bound is its same holomorphic Cauchy majorant differentiated. The derivative input is a property of this original source, not of a freely introduced model function. A second exact rational implementation recomputed both bounds using reverse Horner + dual-number derivative recurrence rather than the first forward coefficient sums.

## 2. New SHARP original-source fractional regularity threshold

Write \(L(d)=\log(B/d)\). On the positive collar, \(\ell_U(B-d)=c(d)L(d)\), \(c(d)=U(B-d)/2\). The exact source bounds above imply \(|c|\le M_0=2\cdot10^{-7}\), \(|c'|\le M_1=7\cdot10^{-4}\) (the factor 1/2 is deliberately discarded for a simple rigorous overcharge).

For \(0<s<1\), use the homogeneous Gagliardo seminorm on the whole line

\[
[f]^2_{H^s(\mathbb R)}=\iint_{\mathbb R^2}
\frac{|f(x)-f(y)|^2}{|x-y|^{1+2s}}\,dx\,dy.
\]

For \(0<e<d<\delta\), the exact logarithmic difference identity and the original source derivative bound give

\[
|c(d)L(d)-c(e)L(e)|
\le M_0\log(d/e)+M_1(d-e)L(e).
\]

The inner logarithmic kernel separates by \(e=td\):

\[
\int_0^\delta\int_0^d
\frac{\log^2(d/e)}{(d-e)^{1+2s}}\,de\,dd
=\frac{\delta^{1-2s}}{1-2s}
\int_0^1\frac{\log^2(1/t)}{(1-t)^{1+2s}}\,dt.
\]

This is finite for **every** \(s<1/2\): near t=0 the log² is integrable, while near t=1 the numerator is O((1−t)²). The cross-support terms at both collar boundaries are also finite exactly when \(\int_0^\delta d^{-2s}L(d)^2\,dd<\infty\), i.e. \(s<1/2\). The source-Lipschitz part is integrable for these s. The odd reflected two-collar function obeys the same conclusion by the fractional norm triangle inequality.

**NEW true original-source theorem:**

\[
\boxed{\ell_U\in H^s(\mathbb R)\quad\text{for every }0\le s<1/2.}
\]

A *quantitative independent of untrusted floating point* control is given at s=1/4. Direct rational integration and splitting at t=1/2 give

\[
\int_0^1\frac{\log^2(1/t)}{(1-t)^{3/2}}dt<7,
\quad6<\log(550)<7,
\quad\sqrt\delta<1/20.
\]

The exact one-collar seminorm is bounded by

\[
[\ell_{U,+}]_{H^{1/4}}^2
<1512M_0^2\sqrt\delta+174M_1^2\delta^{5/2},
\]

and using odd reflection and triangle inequality plus exact log² L² integration, the original **two-collar** a priori **Gagliardo** energy satisfies

\[
\boxed{\|\ell_U\|_2^2+[\ell_U]_{H^{1/4}}^2<10^{-10}.}
\]

This is the unnormalized Gagliardo definition above, not a claim that every convention for the Fourier H^{1/4} norm has the same numeric constant. Source-native exact Fraction acceptance verifies all the explicit inequalities. Actual sharper NF493 \(L^2\) norm exists separately; the displayed upper here is intentionally conservative.

**The threshold 1/2 is sharp.** By the original nonzero U(B) and the independently paid derivative bound, for every 0<d<10^{-9} we have \(|U(B-d)|>9\cdot10^{-12}\). In the H^{1/2} seminorm, use cross-boundary pairs x=B−d and y>B, where the zero extension of \(\ell_U\) vanishes:

\[
[\ell_U]^2_{H^{1/2}}
\ge\int_0^{10^{-9}}\frac{|\ell_U(B-d)|^2}{d}\,dd
\ge (4\cdot10^{-12})^2\int_0^{10^{-9}}
\frac{\log^2(B/d)}d\,dd=\infty.
\]

Hence

\[
\boxed{\ell_U\notin H^{1/2}(\mathbb R),\qquad
\ell_U\notin H^s\text{ for }s\ge1/2.}
\]

This strengthens NF498's previously known ``not H¹'' and identifies the exact Sobolev threshold. The original source indicator at the **inner** collar boundary is also included in the s<1/2 proof; no hidden smooth endpoint condition was assumed.

## 3. The natural Weil Fourier-operator domain is NOT the same as the smooth test image

The previously retained original finite-window symbol bounds have at most logarithmic Fourier growth:

\[
|m_B(\xi)|\le C_B[1+\log(e+|\xi|)]
\]

for a finite C_B (the same prime/pole/archimedean source, not a new symbol). Since for each fixed p>0,

\[
[1+\log(e+|\xi|)]^p\le C_{p,s}(1+\xi^2)^{s/2}
\quad\text{when }s>0,
\]

our source-certified \(H^{1/4}\) membership implies **all finite logarithmic spectral moments** of the actual \(\ell_U\) are finite. In particular, the stronger **actual Fourier multiplier operator-domain condition** holds:

\[
\boxed{m_B(\xi)\widehat{\ell_U}(\xi)\in L^2(\mathbb R).}
\]

This is an **operator-domain regularity conclusion under the already retained logarithmic upper symbol bound**, not membership in an actual full-divisor graph or proof of the equality of a signed Weil source quadratic. It also does not imply \(\ell_U\in C_c^\infty(-B,B)\), which is false, or membership in any fixed strict supported aperture c<B, which is false because \(U(B)\ne0\) and the support reaches \(\pm B\).

There is nevertheless a precise **positive approximation result**. First dilate \(\ell_U\) slightly inward so its support lies in [−B/(1+ε),B/(1+ε)]. Convolve with an even C_c^∞ mollifier of radius smaller than the remaining strict aperture gap. These are **odd, smooth, strictly interior supported physical test functions** \(g_ε\in C_c^\infty(-B,B)\), and dilation/mollifier continuity on H^{1/4} gives

\[
g_ε\to\ell_U\text{ in }H^{1/4},\qquad
\|m_B(D)(g_ε-\ell_U)\|_{L^2}\to0.
\]

**NEW**: the original endpoint singularity is NOT an obstruction to inclusion in the **closure of smooth strict-interior tests in the natural multiplier-operator graph norm**. It IS an obstruction to identifying the raw endpoint vector with a single smooth test, or with any fixed strict c<B physical support object. The actual two-source **ℓ² divisor graph** is a different topology and does not follow from this conclusion.

## 4. Preserve all 242 original selected moments while smoothing

Let \(J=(j_0,\ldots,j_{241})\) be **exactly** the original NF505 full-carrier physical selected generators with the sinh pole. The NF522 full-carrier original Gram certificate gives linear independence of these real-analytic functions. Choose any fixed even nonnegative \(\chi\in C_c^\infty((-B,B))\) which is strictly positive on a nonempty interval (for example a smooth bump in (−B/2,B/2)). The **genuine original 242×242 weighted moment matrix**

\[
M_{ij}=\int_{-B}^B \chi(x)j_i(x)j_j(x)\,dx
\]

is mathematically **strictly positive definite**, because any real-analytic combination which vanishes on an interval must vanish everywhere, contradicting the already source-certified full raw Gram. No matrix condition number or numerical inversion needs to be asserted for this *existence* statement.

Let \(h_j=\chi j_j\in C_c^\infty(-B,B)\). For each strict smooth approximant \(g_n\) above, define the original 242-vector of moment errors

\[
d_i^{(n)}=\langle j_i,\ell_U-g_n\rangle_{L^2(I)}.
\]

It tends to zero by physical L² convergence. Set \(c^{(n)}=M^{-1}d^{(n)}\) **mathematically**, and

\[
\boxed{\phi_n=g_n+\sum_{j=0}^{241}c_j^{(n)}h_j.}
\]

Then each \(\phi_n\) is **odd, strictly interior, smooth** (choose even χ and odd original j_i), and has the **exact same complete original 242 selected moments as \(\ell_U\)**:

\[
\boxed{\forall i=0,\ldots,241,\quad
\langle j_i,\phi_n\rangle_I=\langle j_i,\ell_U\rangle_I.}
\]

Since M is fixed and invertible, c^{(n)}→0; finite h_j have finite H^{1/4} and operator graph norm. Thus \(\phi_n\to\ell_U\) in **H^{1/4} and natural Weil multiplier graph norm** while preserving all **242 original finite selected moments EXACTLY**, not merely asymptotically. The independent exact Fraction verifier tests the same algebra with six odd polynomial control generators and a closed-form logarithmic target, **not** by claiming an already computed original 242D weighted χ Gram.

This resolves **physical smooth approximation and finite moment preservation** without inventing a new source or modifying the original J242 projector. It does **NOT** prove the exact source-graph ℓ² samples of \(\phi_n\) converge, or that any \(\phi_n\) represents an admissible full Weil **source-image** satisfying all prime/pole/zero conditions.

## 5. Sharp non-transfer theorem: even ALL 242 moments plus full L² norm cannot decide source-form membership

Let \(X=L^2([-B,B])\) (zero extended), \(F=\operatorname{span}\{j_0,\ldots,j_{241}\}\), and

\[
\mathcal H_{\log}=\big\{f\in X:\int(1+\log(e+|\xi|))|\widehat f(\xi)|^2d\xi<\infty\big\}.
\]

Every original \(j_i\) zero-extended to the full line belongs to \(\mathcal H_{\log}\): it is piecewise C¹ with finite jumps, has Fourier decay O(|ξ|^{-1}), and hence has finite logarithmic energy. \(\mathcal H_{\log}\) is a proper dense linear subspace of X. Indeed if \(\mathcal H_{\log}=X\), the closed graph theorem applied to the closed logarithm-weighted Fourier operator would make that operator bounded on X. But modulations of a fixed nonzero \(\psi\in C_c^\infty(-B,B)\), \(\psi(x)e^{2\pi iNx}\), have fixed L² norm and unbounded logarithmic Fourier energy as N→∞; contradiction.

Choose \(u\in X\setminus\mathcal H_{\log}\). Then \(z=u-P_Fu\) is orthogonal to **all 242 actual original selected generators** and remains outside \(\mathcal H_{\log}\), since \(P_Fu\in F\subset\mathcal H_{\log}\). The original \(\ell_U\) is in \(\mathcal H_{\log}\), but not in F (nonzero endpoint logarithm versus bounded analytic F), so \(r=\ell_U-P_F\ell_U\ne0\). Scale z so \(\|z\|_2=\|r\|_2\), and put \(h=P_F\ell_U+z\). Then

\[
\boxed{\langle j_i,h\rangle_I=\langle j_i,\ell_U\rangle_I\ \forall i,
\qquad \|h\|_2=\|\ell_U\|_2,}
\]

**but** \(h\notin\mathcal H_{\log}\), while \(\ell_U\in\mathcal H_{\log}\). This is an exact original **finite observation non-identifiability theorem**, not a fabricated zeta/RH counterexample. Even every original selected physical moment AND the full physical L² scalar cannot determine whether a vector is in the required logarithmic form domain. More numerical precision in only those finite observations can never resolve the image/domain question.

The theorem does **not** assert that h matches every local NF522 support-energy observation, or that h is a genuine Weil test. It proves only the stated observation limitation.

## 6. Precise source-image obligations left open

The existing actual-zero Green packet results establish closure in the Green-lift subspace and its packet orthogonality test, **not** equality with the entire two-source graph. NF523 now distinguishes:

| Obligation | NF523 result |
| --- | --- |
| Original NF494 U(B) nonzero; full collar U and U' control | **SOURCE-EXACT Fraction PASS** |
| Original ℓ_U in supported L² | Retained NF498/NF493 |
| Sharp ℓ_U H^s threshold | **s<1/2 YES; s≥1/2 NO** |
| ℓ_U in natural log-growth multiplier **operator** domain | **YES from retained symbol upper bound** |
| Approximation by odd strict-interior C_c∞ tests in operator graph norm | **YES, analytic proof** |
| Exact preservation of all 242 original selected moments under smooth approximation | **YES, analytic positive χ-weighted Gram construction** |
| Finite 242 moments + L² norm decide graph domain membership | **PROVABLY NO** |
| ℓ_U itself is a smooth test or belongs to fixed strict c<B | **NO** |
| ℓ_U belongs to actual **two-source divisor ℓ²** graph | OPEN |
| Those smooth approximants satisfy full genuine Weil **source-image** identity with controlled two-source graph norm | OPEN |
| Green packet closed span equals entire actual source graph | OPEN |
| Original signed Weil form, W-ODD-NEG, RH | OPEN |

**NF524:** To progress toward RH instead of repeating finite physical projections, test **actual** source-coordinate analysis of the explicit moment-matched smooth approximants \(\phi_n\): do BOTH positive and negative divisor sample ℓ² norms stay uniformly controlled and Cauchy in the **real source graph norm**, with the unchanged multiplicities and source normalization? Identify the exact Green-closed-span orthogonal obstruction using the already existing packet criterion; do not assume its complement vanishes. Independently check the actual compact-test Weil multiplier/source diagonal identity on the same \(\phi_n\). Only such graph-norm convergence and same-source form identification permit transfer from this physical operator-domain result to the original actual Weil source problem. No RH claim.