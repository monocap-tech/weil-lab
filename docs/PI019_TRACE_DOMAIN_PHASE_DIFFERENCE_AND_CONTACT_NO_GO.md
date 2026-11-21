# PI019 — Re-read Masullo's actual trace domain; phase-opposed diagonals expose the contact-free comparison

**PI### Potential Interface, ANALYTIC-ONLY.** Stacked on \`research/pi018-analytic-contact-anchor-and-diagonal-obstruction\`, retaining PI001–PI018 original source claims and the NF/IV/CP separation. No new PR, Lean theorem, Actions workflow, or expensive numerical job. Canonical registry: issue #792. NF numerical compiler recovery remains active; IV/CP/PI analytic-first.

**Status:** direct inspection of Masullo's primary manuscript, printed pp. 459–461 and 519–520 (PDF indices 458–460, 518–519), identifies a previously overstated source-domain obstruction. Exact mathematical two-test phase contrast and linear-algebraic contact no-go derived; exact Gaussian-rational regression source committed. **No genuine independent diagonal operator normalization or RH/GRH/whole-Weil positivity has been proved.** Do not promote the manuscript's claimed theorem to independent formal certification.

Source read: Alessandro Maria Masullo, *The Music of the Primes* (November 2026 manuscript), https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf . Original IV024 compatibility context: \`docs/IV024_PHASE_IV_ORIGINAL_PRIME_GRAPH_AND_CERTIFICATION_CUSTODY.md\`, IV branch \`research/iv024-original-prime-graph-ci-custody\`, source Git blob \`96533ff010a498922532cc743b973551cf2f61c1\`; CP015 context: \`docs/CP015_UNCONDITIONAL_SOURCE_WITNESS_SEAM_AND_NO_ZERO.md\`, CP branch \`research/cp015-unconditional-source-seam-witnesses\`, blob \`3578a27071612863f36e992ef784309dcb31cac1\`. Both CP015 zero-source bridge and outstanding original Weil compiler objects remain *candidates*, not accepted results.

## 1. Primary-source correction: the operators are NOT simply undefined at the diagonal

The exact printed statements distinguish three DIFFERENT claims.

**Masullo Theorem 10.4.2.1, printed p.459, equations (10.4.2.3)–(10.4.2.5).** It asserts nuclearity of the relevant truncated spectral and geometric operators \`P^spec_a∘A(φ)\`, \`P^geom_{ρ,a}∘A(φ)\`, and \`P^spec_{ρ,a}∘A(φ)\`, **for any** \`φ∈D(C_F)\` given its cutoff and Sobolev hypotheses. It gives the identity
\[
\operatorname{Tr}(M_\rho A(\varphi))=
\operatorname{Tr}(P^{\rm geom}_{\rho,a}A(\varphi))+
\operatorname{Tr}(P^{\rm spec}_{\rho,a}A(\varphi)).
\]
This does NOT mean an unrenormalized \(\rho\to1\) *global geometric trace* has a finite limit at φ(1)≠0. But it refutes the oversimplification that the cutoff nuclear operators do not exist there.

**Masullo Remark 10.4.2.3, printed p.460, equation (10.4.2.10).** The source explicitly singles out the *subtracted-cutoff trace*
\[
R_\Lambda(\varphi):=
2\log\Lambda\,\bar\mu_1(C_F^1)\varphi(1)
-\operatorname{Tr}(P^{\rm geom}_{\rho,a}A(\varphi))
\tag{PI019-renorm}
\]
and says its convergence to a finite limit follows from the spectral trace statements. **This is a source-proposed renormalization mechanism on tests not required to vanish at the identity**. It is not yet a proved identification with the PI018 *archimedean-only* Gamma distribution: \(R_\Lambda\) includes global spectral/pole/prime contributions as specified by the actual source decomposition. The cutoff scheme \(\rho,\Lambda,\varepsilon\), Haar normalization and other local terms must be matched before extracting an archimedean contact constant.

**Masullo Theorem 12.5.1.1, printed pp.519–520.** The *main explicit trace formula* assumes \(\varphi(C_F^1)=0\). The surrounding introduction says \(\varphi(1)=0\); the displayed theorem imposes vanishing on the norm-one subgroup, a potentially stronger statement for a general nonradial idele test. We must preserve this precise distinction. On a norm-only pullback
\[
\varphi_h(g)=h(\log|g|_F)
\]
(with appropriate test-space regularity and support), the restriction to \(C_F^1\) is **identically \(h(0)\)**. Thus, on this specified radial family, the two vanishing criteria agree and the theorem applies to h(0)=0. An autocorrelation h_{s,s}(0)=||s||²>0 violates the main theorem's hypothesis, although relevant truncated operators may still be nuclear by 10.4.2.1.

**Corrected PI question:** not "Does Masullo's operator exist at the diagonal?" but "Does the *independently normalized finite-part trace* obtained from (10.4.2.10), after authentic pole/prime/archimedean decomposition and cutoff identification, agree on diagonal norm-only tests with the original Weil Gamma distribution of PI018?" That is presently OPEN.

**Parameter warning:** Masullo's \(a=1/2\) in the spectral projector and PI018's physical compensation exponent \(3/2\) are DIFFERENT parameters in unrelated constructions; matching their letters or numerical values has no mathematical basis.

## 2. Two legitimate smooth autocorrelations with equal contact but opposite phase

Take \(a=\log9\). Let \(\phi\in C_c^\infty(\mathbb R;\mathbb R_{\ge0})\) be nonzero, supported in a sufficiently small interval of length \(d<a/2\). Put
\[
\psi(x)=\phi(x-a),\qquad
s_\beta(x)=\frac{\phi(x)+\beta\psi(x)}{\sqrt2},
\quad\beta\in\{1,-1,i,-i\}.
\]
The two spatial bumps have disjoint supports and equal \(L^2\) mass \(J=||\phi||_2^2>0\), so every sβ has the same physical support and \(||s_\beta||_2^2=J\).

Define \(C(u)=\int \phi(x)\phi(x-u)dx\). It is real, even, nonnegative, smooth, compactly supported in \((-d,d)\). Use the **actual Weil-Lab correlation orientation**
\[
h_{s,t}(u)=\int t(x)\overline{s(x-u)}\,dx.
\]
For \(h_\beta:=h_{s_\beta,s_\beta}\), a direct four-term expansion gives the EXACT identity
\[
\boxed{
h_\beta(u)=C(u)+\tfrac{\overline\beta}{2}C(u+a)
                   +\tfrac{\beta}{2}C(u-a).}
\tag{PI019-corr}
\]
Since \(d<a\), all hβ have \(h_\beta(0)=J\). They are genuinely smooth compact complex autocorrelations, not the nonsmooth PI018 compensation anchor. They contain phase information that a support-overlap graph and an \(L^2\) mass cannot store.

For opposite real phases,
\[
\boxed{
D_{\rm even}(u):=h_{1}(u)-h_{-1}(u)
=C(u+a)+C(u-a),\qquad D_{\rm even}(0)=0.}
\tag{PI019-even}
\]
For opposite imaginary phases,
\[
\boxed{
D_{\rm odd}(u):=h_{i}(u)-h_{-i}(u)
=i[C(u-a)-C(u+a)],\qquad D_{\rm odd}(0)=0.}
\tag{PI019-odd}
\]

**Key point:** neither individual radial lift \(\varphi_{h_{\pm1}}\) meets the vanishing condition of Masullo 12.5.1.1. Their **difference** \(\varphi_{D_{\rm even}}\), however, is smooth compact, is supported off the norm-one fiber, and vanishes on **all** \(C_F^1\) when lifted through the norm in the \(F=\mathbb Q\) radial setting. It is therefore a natural genuine *admissible-difference* test of the source theorem, conditional only on verifying the exact lifted support/measure dictionary. Likewise for \(D_{\rm odd}\).

The full Masullo 12.5.1.1 formula is **global** (two pole Mellin evaluations, archimedean places, all nonarchimedean places, zeros). Its application to these differences must compare ALL places; one cannot relabel its full trace as an isolated Gamma component.

## 3. Nonzero contact-free archimedean phase separation

PI018 fixes the original Gamma distribution for smooth compact h:
\[
A(h)=-(\gamma+\log\pi)h(0)
-\int(h(u)-h(0)e^{-3|u|/2})K(u)du,
\quad K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}.
\]
On contact-zero D, this is simply \(A(D)=-\int D K\).

Since K is even, put
\[
I_a:=\int_{\mathbb R}C(v)K(v+a)\,dv.
\]
For φ≥0, \(C\ge0\) and \(C\not\equiv0\); K is positive on the compact support shifted by a, so \(I_a>0\). Consequently
\[
\boxed{A(h_1)-A(h_{-1})=A(D_{\rm even})=-2I_a<0,}
\tag{PI019-real-phase}
\]
while
\[
\boxed{A(h_i)-A(h_{-i})=A(D_{\rm odd})=0.}
\tag{PI019-imag-phase}
\]
These equalities are EXACT. No unknown diagonal constant remains, because hβ(0) cancels in the differences.

If supp C⊂[-d,d] with \(0<d<a\), K is strictly decreasing on the positive axis and \(M=\int\phi>0\) gives a rigorous positive interval
\[
\boxed{
2K(a+d)M^2\le -A(D_{\rm even})\le 2K(a-d)M^2.}
\tag{PI019-bound}
\]
At the actual n=9 offset, \(K(\log9)=27/80\); it is a *local physical-kernel value*, not a universal spectral positivity margin. Thus the phase contrast can be bounded with no diagonal spectral extension at all.

**Important:** the original prime n=9 functional also depends on the translated cross-correlations (e.g. \(h_\beta(a)=\beta J/2\), \(h_\beta(-a)=\overline\beta J/2\), with the stated narrow support). The original signed prime and pole contributions MUST be carried separately in any whole-Weil or Masullo spectral comparison. The source IV024 graph correctly detects potential \(\pm\log9\) edges but does not determine their phase-dependent amplitudes.

## 4. Exact affine-extension/no-go theorem, and what it can actually tell us

Let E denote a complex vector space of **smooth compact norm-only tests** containing the hβ above, and let \(e_0:E\to\mathbb C\), \(e_0(h)=h(0)\), be the nonzero evaluation functional. The admissible zero-contact subspace is \(E_0=\ker e_0\).

**Elementary extension lemma.** If two complex-linear functionals \(L_1,L_2:E\to\mathbb C\) agree on all of E0, then there is a **unique** \(c\in\mathbb C\) such that
\[
\boxed{L_1(h)-L_2(h)=c\,h(0)\quad\text{for all }h\in E.}
\tag{PI019-affine}
\]
Proof: choose any smooth compact \(\chi\in E\) with \(\chi(0)=1\), decompose \(h=[h-h(0)\chi]+h(0)\chi\), and use equality on E0. The coefficient is the difference on χ. This shows the one-dimensional ambiguity of extending a linear functional from admissible tests; it does NOT assert Masullo's limit is already continuous/defined on all E.

For two diagonal autocorrelations h1,h2 with nonzero contact, suppose an **independently defined** spectral functional T_spec (or accurately isolated arch component after separately paid pole/prime channels) is available on them and compare it against original Weil Gamma A. Define
\[
d_j=\frac{T_{\rm spec}(h_j)-A(h_j)}{h_j(0)}.
\]
If \(d_1\neq d_2\), **no** constant \(c\) makes \(T_{\rm spec}=A+c\,e_0\) on both tests. If \(h_1(0)=h_2(0)=J\), an equivalent contact-independent falsifier is
\[
\boxed{
T_{\rm spec}(h_1)-T_{\rm spec}(h_2)
\ \stackrel{?}{=}\
A(h_1)-A(h_2).}
\tag{PI019-two-test}
\]
For phase-opposed real tests the right side is **exactly −2I_a**.

**Logical limitation:** if the independent T_spec is already a linear extension agreeing with A on **all of E0**, then (PI019-affine) FORCES \(d_1=d_2\); two-test differences cannot determine the remaining scalar c. A phase-difference mismatch would instead expose failure of the proposed source dictionary or linear restriction already on E0, not merely a wrong diagonal normalization. Determining c then requires ONE genuinely independent diagonal normalization, for example from a justified finite-part trace of Masullo's actual cutoff operators with a specified cutoff/Haar convention. Neither identifying two formal operator expressions nor testing only h(0)=0 can supply it.

**Infinite-dimensional rank warning:** the evaluation quotient \(E/E_0\) has complex dimension one, but on an underlying infinite-dimensional Hilbert test space the induced sesquilinear contact correction \(c\,\langle t,s\rangle\) corresponds to \(cI\), not generally a rank-one **operator**. Calling it rank-one would conflate the codimension-one missing test direction with the rank of a Hilbert-space operator.

## 5. What the manuscript's renormalized cutoff suggests, but does NOT yet establish

Masullo's displayed finite-cutoff subtraction (10.4.2.10) is a concrete possible source of the missing normalization. However it is NOT enough to compare the numerical constants
\(-\gamma-\log\pi\) (PI018 physical anchor) and \(2\log\Lambda\) (Masullo cutoff).

Even when \(\bar\mu_1(C_F^1)=1\), the divergent scales need an independently specified dictionary:
\[
H_N=\log N+\gamma+o(1),\qquad
2\log\Lambda=\log(\Lambda^2).
\]
Replacing \(N\) by \(\lfloor b\Lambda^2\rfloor\) changes the finite asymptotic difference by \(\log b\). Thus the scalar finite part is sensitive to cutoff/anchor choices. Similarly changing \(\Lambda\mapsto c\Lambda\) shifts the displayed subtraction by \(2\log c\,\bar\mu_1(C_F^1)\varphi(1)\). This does NOT by itself give the variation of the full cutoff trace, which must be computed rather than guessed.

**Necessary missing hypotheses for a valid diagonal comparison:**
(i) a genuine fixed local-to-idelic logarithmic norm/test lift including Haar factors;
(ii) the source operator trace and pole/prime arch partition with signs paid;
(iii) a specified cutoff scheme and proof that the corrected limits exist on diagonal tests and are linear;
(iv) a scheme conversion or invariance law establishing the finite-part normalization;
(v) a comparison on at least one actual diagonal h with \(h(0)>0\) after the contact-free phase test.

Neither \(\eta_{3/2}\) (physical compensator) nor \(a=1/2\) (Masullo spectral projection) is an independently justified substitute for such a cutoff conversion.

## 6. Cross-branch compatibility and the information each source lacks

**IV024 / IV030.** IV024's authentic exact arithmetic overlap graph detects just the two old–old n=9 directed edges; it is invariant under phase and physically support-label permutations. PI019's four autocorrelations have identical support and mass but different \(\pm a\) coefficients and signed Weil arithmetic/Gamma evaluations. Therefore **the graph alone cannot be a faithful image of the original signed Hermitian pairing**. The phase coefficients (or equivalent full complex correlations) are additional required data. IV030's reported phase-information obstruction is recovered explicitly with the correlation dictionary in (PI019-corr).

**CP015.** CP015 constructs an original Euler/RS finite-height zero-source saturation **Lean proof candidate**; even if its proposed \(N(149.5)=52\) and no-seam-zero conclusions are accepted, those are **zero-roster/count information**. They do NOT by themselves specify the test-to-spectrum map, conjugation convention, spectral weights, cutoff finite part, or the diagonal mass coefficient. A full spectral functional applied to \(D_{\rm even}\) may be compared only once the actual Mellin/Fourier test map is supplied. PI019 does not infer anything about CP015's source count being false or true from this observation.

**PI018.** The complete original Gamma distribution A on smooth compact h is source-intrinsic, while the constant \(-\gamma-\log\pi\) is a **coordinate-specific** contact coefficient relative to the auxiliary nonsmooth anchor \(\eta_{3/2}\). Contact-free differences such as \(D_{\rm even}\) are gauge invariant and thus provide a logically prior compatibility gate. The final scalar can only be checked after source/operator renormalization is independently fixed.

## 7. Exact mathematical regression, no compiler/Actions

\`scripts/pi019_exact_phase_contact_no_go.py\` checks the Gaussian-rational coefficients of sβ correlations, identity of masses at hβ(0), the exact even/odd phase differences, \(h_\beta(\pm a)=\beta^{\pm1}J/2\), even-arch reduction to −2I_a and odd-arch cancellation, and finite two-test scalar-contact countermodels. Coefficients use \`fractions.Fraction\` only: it does NOT numerically integrate C*K or pretend to evaluate an independent spectral operator.

There are **zero new .lean files, workflows, draft PRs or Actions runs in PI019**. This preserves the analytic-first rule and NF's existing compiler capacity. The original Masullo manuscript has not been independently peer- or Lean-verified by this source reading. No new global Weil positivity, RH, or cross-projection equivalence theorem is asserted.

## 8. PI020 analytic-only decision gate

1. Follow the actual manuscript's proof of its \(\varphi(1)\)-dependent logarithmic cutoff subtraction and identify the precise **finite-part trace** for a **radial compact test with h(0)≠0**, separately decomposing the two pole terms, primes and archimedean place. Do not replace this operator calculation with the PI018 original Gamma distribution.
2. Evaluate the already theorem-admissible phase difference \(D_{\rm even}=C(u+a)+C(u-a)\) against the source spectral and geometric trace expressions. A mismatch with original fully accounted Weil terms cannot be repaired by ANY scalar contact shift.
3. If the contact-free gate passes, compute just **one** independent diagonal finite-part normalization on an actual smooth autocorrelation (preferably h1), with the same cutoff/Haar convention. Then \(c\) in (PI019-affine) becomes testable; the opposite-phase diagonal supplies a built-in consistency check.
4. Feed the resulting **phase-bearing**, **gauge-covariant** compatibility condition into IV and CP analytic investigations without launching compiler jobs. A finite zero count or a support graph is not a substitute for a test-level spectral/Weil equality.

**PI019 conclusion:** the manuscript already specifies nuclear cutoff operators on more tests than its headline trace formula covers; the missing theorem is the *normalized diagonal trace identity*, not bare operator existence. Moreover, opposite-phase diagonal correlations produce a nonzero, gauge-independent, theorem-admissible **difference**. This is the first discriminating interface test to run BEFORE attempting diagonal scalar calibration.


## 9. Second primary-source discovery: Chapter 13 proposes a TRANSVERSAL moment-zero domain containing diagonals

Directly re-read Masullo's manuscript printed p.522 (PDF index 521), **Theorem 13.3.1.1**, equation **(13.3.1.2)**, with its visible footnote "Correct statement." The author states a trace formula on a finite-codimensional space of tests annihilated by certain Mellin moments, expressed in terms of ALL unitary idele-class characters and derivatives of order \(0\le k\le [F:\mathbb Q]-1\). The chapter also visibly contains an unfinished Theorem 13.3.1.2 ("Insert statement") and proof-plan remarks; thus we do NOT elevate the Chapter 13 statement to an independently established theorem or accepted Lean result. It is, however, a **real source-stated potential diagonal interface** and should not be ignored.

For the **special case \(F=\mathbb Q\)**, \([F:\mathbb Q]=1\), so only **\(k=0\)** occurs. For a **norm-radial** test \(\varphi_h(g)=h(\log|g|_{\mathbb Q})\), integrate first over the compact norm-one fiber. Nontrivial unitary characters of the fiber average to zero. A character trivial on the fiber is \(|g|_{\mathbb Q}^{it}\), and its frequency factor cancels at the source's indicated evaluation \(s=-ix_0(\chi)\). Assuming the source's Haar disintegration and the radial test's admissibility, the collection of Chapter 13 moment conditions therefore reduces to
\[
\boxed{\int_{\mathbb R}h(u)\,du=0.}
\tag{PI019-moment}
\]
This is a DIFFERENT codimension-one condition from the Chapter 12 formula's \(h(0)=0\).

### Genuine smooth nonzero-diagonal autocorrelations in the moment-zero class

Choose \(\rho\in C_c^\infty(\mathbb R;\mathbb R_{\ge0})\), nonzero, and set \(\phi=\rho'\). Then
\[
\int_{\mathbb R}\phi(x)\,dx=0,\qquad
J=\|\phi\|_2^2>0.
\]
For \(a=\log9\) larger than the support diameter, put \(\psi(x)=\phi(x-a)\) and \(s_\beta=(\phi+\beta\psi)/\sqrt2\). All four autocorrelations \(h_\beta=h_{s_\beta,s_\beta}\) are smooth and compact. The elementary correlation identities give
\[
\boxed{
h_\beta(0)=\|s_\beta\|_2^2=J>0,\qquad
\int_{\mathbb R}h_\beta(u)\,du
=\left|\int_{\mathbb R}s_\beta(x)\,dx\right|^2=0.}
\tag{PI019-diagonal-moment}
\]
Therefore the *same four phase-opposed, genuine diagonal tests* excluded by Chapter 12's main vanishing-on-\(C_{\mathbb Q}^1\) hypothesis would be **eligible for the different Chapter 13 moment-condition class**, IF its full stated trace theorem and lift/dictionary are valid. This is a more precise analytic lead than trying to extend the Chapter 12 identity by assertion.

The sign of their phase-sensitive archimedean contrast remains **strictly nonzero**, despite \(\int\phi=0\). Let \(C(v)=\int\phi(x)\phi(x-v)dx\), and \(\lambda_n=2n+1/2\). Because \(a\) exceeds the support diameter, expand
\[
\begin{aligned}
I_a
&=\int C(v)K(a+v)dv\\
&=\sum_{n\ge0}e^{-\lambda_n a}
  \left(\int\phi(x)e^{-\lambda_n x}dx\right)
  \left(\int\phi(y)e^{+\lambda_n y}dy\right)\\
&=\boxed{-\sum_{n\ge0}e^{-\lambda_n a}\lambda_n^2
  \left(\int\rho(x)e^{-\lambda_n x}dx\right)
  \left(\int\rho(y)e^{+\lambda_n y}dy\right)<0.}
\end{aligned}
\tag{PI019-derivative-phase}
\]
Each Laplace integral of the nonnegative \(\rho\) is strictly positive; the sum converges exponentially by \(a>\mathrm{diam}(\mathrm{supp}\,\rho)\). Thus for this **moment-zero diagonal family**, the original Gamma phase contrast \(A(h_1)-A(h_{-1})=-2I_a\) is **strictly positive**, not accidentally annihilated by the moment condition.

The earlier positive-bump result (Section 3) has \(I_a>0\) and a *negative* contrast. They are two distinct smooth experiments, with the sign determined by the bump shape rather than by support adjacency alone.

### Conditional transversality theorem: the scalar gap disappears if BOTH source domains are genuinely paid

Let E be the complex space of compact smooth radial tests, \(e(h)=h(0)\) and \(m(h)=\int h\). These are linearly independent continuous linear functionals (as shown by the derivative-bump autocorrelation). The Chapter 12 theorem domain is \(E_e=\ker e\); the proposed Chapter 13 domain is \(E_m=\ker m\).

**Algebraic uniqueness lemma.** If two continuous complex-linear functionals \(L_{\rm spec}\) and \(L_{\rm orig}\) on E agree on **both** \(E_e\) and \(E_m\), then they agree on **all of E**.

Proof: agreement on \(E_e\) implies \(L_{\rm spec}-L_{\rm orig}=c\,e\), by the PI019 affine-extension lemma. Choose any derivative-bump autocorrelation \(h\in E_m\) with \(e(h)=J>0\). Agreement on \(E_m\) forces \(0=cJ\), hence \(c=0\). No density or operator norm claim is hidden in this elementary linear statement.

**This is the conditional cross-projection opportunity:** a source-exact, independently justified second moment-domain trace law, compatible with the SAME whole arithmetic/pole/prime/Gamma functional and test lift, could **determine the formerly undetermined contact scalar**. It would not, without genuine spectral operator representation, whole signed Weil positivity or global RH proof, establish any of those stronger conclusions.

The conditions cannot be mixed casually: the Chapter 13 source is NOT Chapter 12's proved trace theorem on a larger domain; it has different moment hypotheses and visible unfinished surrounding text. Even if a formula holds on \(E_m\), its prime, archimedean, Mellin pole, Haar and zero multiplicity data must be matched to the SAME global functional already identified on \(E_e\). If the two "extensions" use different renormalized cutoff conventions, agreement on the subspaces need not be meaningful until a common normalization is established.

### Independent exact signed zero-moment control

New analytic-only script \`scripts/pi019_zero_moment_diagonal_exact_preflight.py\` evaluates a **discrete signed two-atom model** (not a smooth test) \(\phi_{\rm disc}=\delta_0-\delta_{\log4}\), whose correlation is
\[
C_{\rm disc}=2\delta_0-\delta_{\log4}-\delta_{-\log4}.
\]
For every N≥1 the finite physical source kernel satisfies the exact rational inequality
\[
2K_N(\log9)-K_N(\log36)-K_N(\log(9/4))<0.
\]
Indeed the nth summand equals
\[
-9^{-\lambda_n}(2^{\lambda_n}-2^{-\lambda_n})^2<0,
\quad \lambda_n=2n+1/2.
\]
At N=1 this is **exactly \(-1/6\)**. The independent Fraction preflight evaluates N=1,…,100 and confirms the strict sign. This is a **regression for the algebraic phase mechanism**, not a substitute for the preceding proof with genuinely smooth derivative bumps, nor proof of the author-stated Chapter 13 theorem.

**Updated PI020 priority:** Before launching another common-compiler Gamma theorem, determine whether the genuine Chapter 13 moment-domain trace claim is actually proved and applies to norm-radial diagonal autocorrelations in \(F=\mathbb Q\). If it does, the two transversal domains may **remove the diagonal scalar ambiguity** without a guessed operator extension. If it does not, record the exact missing analytic theorem and continue the independent finite-part/cutoff study from (10.4.2.10).

Original primary-source screenshots: PDF index 458–460 (Thm. 10.4.2.1, Rmk. 10.4.2.3), 518–519 (Thm. 12.5.1.1), **521 (Thm. 13.3.1.1, stated moments and visible editorial caveats)**.


## 10. Essential source correction: Chapter 13's spectral divisor is NOT the Chapter 12 divisor

The same printed p.522 that states the Chapter 13 moment restriction makes an important definition:
\[
\boxed{
N_{\rm spec}(c):=\min\{N(c),[F:\mathbb Q]\}.
}
\tag{PI019-multiplicity}
\]
For \(F=\mathbb Q\), this is \(\min(N(c),1)\), **not necessarily** the full zero multiplicity \(N(c)\). In Theorem 13.3.1.1 the displayed spectral sum is restricted to \(\sigma(c)=1/2\), whereas the displayed main Theorem 12.5.1.1 sums the full \(N(c)\) over zeros in its specified vertical strip. Their identification on a common domain is **NOT** an immediate consequence of the test-domain comparison; it could require deep and presently unproved zero-location and multiplicity information, or a different source spectral trace formula.

Therefore do NOT use the abstract transversality lemma from Section 9 to claim the two manuscript formulas are automatically identical or that their domains automatically determine a common trace. The transversality lemma says only that **IF** two consistently normalized versions of the **same** functional are established on both hyperplanes, then their common extension is unique. It does not prove those spectral/arithmetical formulations agree. In particular, one cannot silently replace \(N_{\rm spec}\) by \(N\), or a critical-line sum by a full-strip sum, because that would assume part of the intended global zero theorem.

### The exact overlap domain gives a nontrivial falsifier before any diagonal extension

For the **derivative-bump** family \(\phi=\rho'\), all \(h_\beta\) have \(\int h_\beta=0\) and \(h_\beta(0)=J>0\). Their phase difference
\[
D_{\rm even}:=h_1-h_{-1}
\]
satisfies **both**
\[
\boxed{
D_{\rm even}(0)=0,\qquad \int_{\mathbb R}D_{\rm even}(u)\,du=0,
\qquad A(D_{\rm even})=-2I_a>0.
}
\tag{PI019-intersection}
\]
Thus \(D_{\rm even}\) is a genuinely nonzero smooth source test in the **intersection** of the Chapter 12 zero-contact subspace and the Chapter 13 proposed zero-Mellin-moment subspace, for the stated \(F=\mathbb Q\) norm-radial lift. It cannot be dismissed as a trivial test, a finite overlap graph, a contact-only term, or a vanishing Gamma evaluation.

If both purported spectral trace identities were valid under identical normalizations and genuinely represented the same whole Weil functional, their evaluations on \(D_{\rm even}\) MUST coincide, after accounting for every archimedean place, prime, pole, Mellin character, zero-multiplicity and cutoff contribution. A discrepancy on this common domain is a **direct source/projection mismatch that no \(c\,h(0)\) or \(d\,\int h\) correction can repair**, because both contact and total Mellin moment are zero on D.

### Conditional gluing theorem, formulated without assuming RH or simplicity

Let E be the complex vector space of compact smooth radial tests, \(E_e=\ker(h\mapsto h(0))\) and \(E_m=\ker(h\mapsto\int h)\). Since these are distinct hyperplanes and \(E_e+E_m=E\), suppose two independently defined linear source functionals
\[
L_e:E_e\to\mathbb C,\qquad L_m:E_m\to\mathbb C
\]
have been established with consistent signs and conventions and **agree on \(E_e\cap E_m\)**.

Then there exists a **unique** linear \(L:E\to\mathbb C\) extending both.

Proof: choose a smooth compact h0 with \(\int h_0=0\), \(h_0(0)=1\) (normalize a derivative-bump autocorrelation). Any h decomposes \(h=(h-h(0)h_0)+h(0)h_0\), with first part in \(E_e\) and second in \(E_m\). Define L by applying L_e to the first part and L_m to the second. Independence of the choice of h0 follows from overlap agreement. Uniqueness follows because \(E_e+E_m=E\).

**What this does and does not pay:** it eliminates a *linear functional's* one-dimensional contact extension ambiguity **IF the independent Chapter 13 identity and exact overlap agreement are truly proved**. It does not establish a positive operator on a Hilbert space, validate the spectral zero representation or solve RH. A continuity assertion needs boundedness/continuity of the two source functionals and a chosen compatible topology; the algebraic gluing theorem alone makes no automatic continuity claim.

**Next PI020 strict analytic gate:** audit Theorem 13.3.1.1's **actual proof**, its critical-line/capped-multiplicity right side and any outstanding annotations, then test its source functional against the Theorem 12.5.1.1 functional on the explicit \(D_{\rm even}\in E_e\cap E_m\). **Only after the overlap is paid** should the transversal diagonal tests be used to attempt the independent scalar contact normalization. No new Lean or Actions until the existing queue drains.
