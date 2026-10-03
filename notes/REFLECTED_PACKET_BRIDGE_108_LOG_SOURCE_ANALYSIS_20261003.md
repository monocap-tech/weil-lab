# RPB-108 — actual-zeta analysis on the logarithmic form carrier
Date: 2026-10-03
Parent: a5fecc6c41bb6ce6ce9eb5e4a00f87eda886f986

## Scope

This pass gives a written construction in actual zeta coordinates of a bounded source analysis on the canonical logarithmic form space. It does not add an assumed source-identity field. It is not Lean-certified and does not yet identify the current WD-T38 instance with this model.

Terminology:
- Logarithmic carrier H_log(a): physical L2 functions supported in [-a,a], with squared norm integral w(xi)|Fourier f(xi)|², where w(xi)=log(e+|xi|). Its topology is this energy norm, not the inherited ordinary-L2 subtype norm.
- Raw multiplicity-normalized analysis E: angular Fourier evaluations at zeta ordinates, weighted by square roots of multiplicities and then unitarily diagonalized across conjugate pairs.
- Selected analysis E_Pi: every positive channel together with the fixed selected negative channels. Unselected negative channels are denoted E_B.
- Coefficient closure: the closure of the analysis image in the coefficient Hilbert norm. Equality to the current retained coefficient closure requires an exact coordinate dictionary.

No H_0^1 or spectral-product L2 premise is used.

## 1. Hilbert domain, smooth core, compact physical embedding

H_log(a) is complete: Fourier multiplication by sqrt(w) identifies it with the subspace of weighted L2 whose inverse Fourier transform has the required support. A weighted-L2 Cauchy sequence converges in ordinary L2 because w>=1; support is closed under L2 convergence. The weighted limit and ordinary Fourier limit agree, proving completeness. The integral of w times the conjugate Fourier product is its inner product.

Compact smooth functions in (-a,a) are a form core. For a>0, first dilate a supported f slightly inward, then convolve with a compact smooth approximate identity smaller than the resulting margin. Dilations near one are uniformly bounded and strongly continuous in weighted L2: w(xi/rho) is uniformly comparable with w(xi), and the claim follows first for continuous compact frequency functions, then by density. Mollification converges by dominated convergence of its Fourier multiplier against the genuine weighted energy. Thus these approximants converge in the same form norm, with support strictly inside the window. The a=0 supported space is zero.

The embedding into physical L2 is compact. For a bounded form-norm family,
integral_{|xi|>R}|Fourier f|² <= C/log(e+R).
This uniform tail estimate and Plancherel give uniform translation continuity; physical supports lie in one compact interval. The L2 compactness criterion applies.

## 2. Actual-zeta upper sampling bound

Use angular frequency F(z)=integral f(x) exp(i z x) dx and w_ang(t)=log(e+|t|). Angular and mathlib energies are comparable by t=2pi xi; no new source normalization constant is hidden.

Actual nontrivial ordinates gamma have |Im gamma|<1/2. The retained unit-height zero count, including multiplicity and the reflected negative heights, gives at most C log(e+|t|) centers in any fixed-length horizontal interval.

For the entire F, the submean inequality gives
|F(gamma)|² <= (1/pi) integral_{disk(gamma,1)} |F(z)|² dA(z).
Summing with multiplicity and applying the overlap bound yields
sum_gamma m_gamma |F(gamma)|²
 <= C integral_{-3/2}^{3/2} integral_R w_ang(t)|F(t+i s)|² dt ds.

For |s|<=3/2, F(t+i s) is the Fourier transform of exp(-s x)f(x). Choose one compact smooth cutoff chi equal to one on [-a,a], and put M_s(x)=chi(x)exp(-s x).

Multiplication by M_s is uniformly bounded in the logarithmic norm. Indeed,
w_ang(t)<=w_ang(v)+w_ang(t-v)<=2w_ang(v)w_ang(t-v).
The Fourier convolution identity and Young's inequality therefore bound the weighted L2 norm by
sqrt(2) * norm(sqrt(w_ang) Fourier(M_s))_L1 * norm(sqrt(w_ang) F)_L2.
The first factor is uniformly bounded on the compact s interval by uniform Schwartz bounds on M_s. Integrating the strip estimate proves

sum_gamma m_gamma |F(gamma)|² <= C_a norm(f)_Hlog².

This proof applies to the actual divisor, including arbitrarily many off-critical pairs. It uses upper zero counting, not RH, a lower frame assumption, or spectral operator membership.

Consequently E and E_Pi are bounded complex-linear analysis maps. Pair diagonalization is unitary, so their coefficient norms are bounded by the same sampling sum.

## 3. Source diagonal and same-domain mixed identity

On the compact smooth core, the retained complex explicit formula identifies the signed multiplicity-normalized zero diagonal with the multiplier-plus-Hermitian-pole diagonal. The general pole is 2 Re(conj(M-) M+), not a nonnegative real-even pole.

The arithmetic form is continuous in the logarithmic norm: the retained symbol is bounded in absolute value by a constant times w, and the two pole moments are bounded by fixed-support L2. The zero diagonal is continuous by §2.

Both therefore extend to the same complete H_log(a) domain and agree there. Complex polarization gives the same-domain mixed equality. In normalized mathlib coordinates this is the concrete sourceDomainQuadratic diagonal and its multiplier-plus-pole sesquilinear form, with the already reconciled cutoff convention.

This is a written actual-model construction of the source identity, not a formal attachment to WD-T38's independent source parameters.

For the selected analysis specifically,
Q_Pi(f)=norm(E_+ f)²-norm(E_Pi,- f)²
       =Q_full(f)+norm(E_B f)².
The selected diagonal is not silently equated with the full Weil diagonal.

Taking Hilbert adjoints of the bounded actual analysis maps constructs concrete synthesis operators on H_log(a). Their bounded defect represents the signed form in that form-space inner product. This does not assert a bounded full Weil operator on ordinary physical L2.

## 4. Closed range and actual physical recovery from coefficient closure

The actual full form satisfies a Garding estimate from the logarithmic symbol and bounded signed pole:
norm(f)_Hlog² <= C_a (Q_full(f)+K_a norm(f)_L2²).
Since Q_full<=Q_Pi<=norm(E_Pi f)², it follows that
norm(f)_Hlog² <= C'_a (norm(E_Pi f)²+norm(f)_L2²).

E_Pi is injective because it retains all critical-line positive coordinates. If they vanish, the entire F vanishes at every simple critical-line ordinate. The retained Conrey input gives a number of distinct such ordinates comparable to T log T, whereas a nonzero compact-support Fourier transform of exponential type has at most O(T) zeros by Jensen. Thus F=0 and f=0.

The injectivity fact and compact physical embedding remove the L2 remainder. If no lower bound existed, choose norm(f_n)_Hlog=1 with E_Pi f_n->0. A weakly convergent subsequence in H_log converges strongly in physical L2. Its limit has zero analysis, hence is zero. The Garding estimate then forces norm(f_n)_Hlog->0, a contradiction.

Therefore E_Pi is bounded below and has closed range. In particular each vector in closure Ran E_Pi has a unique actual supported finite-log-energy physical preimage. This proves a qualitative bound for this specified actual logarithmic model; it is not an ordinary native H^{-1} lower frame bound, a special-packet quantitative transversality floor, or Gaussian coercivity.

## 5. Precise attachment boundary

If the retained coefficient closure is exactly the closure in these multiplicity-normalized coordinates, §4 recovers the actual physical vector from its coefficient datum. This equality still needs verification against the retained Bombieri/Green weights and effective-positive/background map. Nonzero coordinate scalings preserve injectivity but do not automatically preserve the coefficient norm, unit gain, or neutral Krein quadratic.

RPB-24 supplies a Green congruence in its stated model. On that model's exact raw coordinate convention, native analysis has image E_Pi(H_0^1); the form-core density and §2 imply the same closed coefficient closure as E_Pi(H_log). This explains how a coefficient-closure reconstruction can avoid assuming a native adjoint-range witness. It does not assert that the present independently parameterized WD-T38 H,P,C,k or chosen physical h already satisfy this coordinate dictionary.

There is also a lawful route to transporting an existing signed compensator, once the exact coordinate dictionary is proved. The native identity N=-PC is equivalent to E_Pi,- f=-C* E_+ f on its Green image H_0^1. Boundedness of both analyses and core density extend that SAME coefficient identity to H_log. Taking adjoints gives N_log=-P_log C. The positive synthesis kernels coincide because both are orthogonal complements of the same closed positive-analysis range, so reducedness is preserved. Thus transport need not choose a new compensator or assume a new unit-gain law. This argument requires the exact coefficient identity, not arbitrary coordinate reweighting.

The construction does not prove enlarged nullity from a scalar neutral diagonal. A same-domain mixed null law and the actual fixed-vector persistence transport are still required. Once actual central cancellation is attached, immediately consume the certified inner-collar/boundary-removal theorem.

Spectral L2 does not follow from membership in this H_log space and is neither assumed nor needed for this source construction.

## Primary inputs checked

- Titchmarsh unit-height zero count, already pinned as EXT-3.
- Retained EXT-4 admissible-test explicit formula and complex parity extension:
  https://arxiv.org/html/2608.24827v2, §2 equation (7), §6.1 Lemma 6.1.
- Retained EXT-5 symbol asymptotic.
- Conrey, J. reine angew. Math. 399 (1989), Theorem 1, printed p.4; simple critical-line count together with the zero-count asymptotic printed p.3:
  https://aimath.org/~kaur/publications/24.pdf.

Submean, weighted convolution, compactness, and core-extension arguments above are this pass's written deductions. No external sampling lower bound or RH positivity is imported.

## Standing

Written actual-zeta source-model construction: upper sampling bound, same-domain diagonal/mixed extension, and qualitative closed-range reconstruction. NOT LEAN-CERTIFIED.

Identification with the current WD-T38 coefficient metric/source vector: OPEN.
Actual enlarged central cancellation: OPEN.
Spectral L2 of the current carrier: unproved and unassumed.
Regularity and boundary removal from actual central cancellation: already Lean-certified.
Thresholds CLOSED; F-4 NOT STARTED; WD-T40/RH unchanged.

Documentation-only promotion. Code/manifests/workflow and historical notes remain unchanged. Next concrete check: the exact multiplicity/Green coefficient dictionary, followed by formalization of the upper sampling bound and the canonical-domain reconstruction; do not add an assumed identification field.
