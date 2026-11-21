# PI021 — Unconditional infinite exponential rigidity under a full translation half-line; conditional zero-divisor consequence

**Independent Weil-Lab PI### Potential Interface — ANALYTIC-ONLY.** Stacked on \`research/pi020-analytic-double-annihilator-spectral-defect\` with PI001–PI020 history intact. **No pull request, no new .lean module, no GitHub Actions or numerical workflow.** NF### continues its numerical Lean certification; IV### and CP### remain analytic-first.

**Result:** the missing analytic uniqueness mechanism in PI020 **can be proved** for an infinite discrete zero divisor satisfying unconditional zero-density and bounded-strip conditions, provided source agreement holds for BOTH phase probes across **every sufficiently large real translation**. The proof is elementary complex analysis of a Laplace-transformed, absolutely convergent spectral exponential series; it does not use RH, zero simplicity, Masullo's claimed Chapter 13 formula, or original global Weil positivity. **The unproved step is still whether the two differently stated manuscript trace formulas really agree on those probes.** This distinction is essential: the conditional corollary is strong enough to imply RH and noncentral zero simplicity, so it cannot be presented as a proof of either without first supplying the missing source theorem.

## 1. Original source audit and exactly what is being compared

Reopened the actual November 2026 primary manuscript by Alessandro Maria Masullo, *The Music of the Primes*, https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf :

- Printed **pp.519–520**, Theorem **12.5.1.1** (PDF page indices 518–519): the trace formula on \(\varphi(C_F^1)=0\), with **full zero multiplicities** and zeros in a **specified relative vertical strip**.
- Printed **p.522**, Theorem **13.3.1.1** (PDF page index 521): a different claimed formula under Mellin moment annihilation, using the **critical-line-only** sum and \(\boxed{N_{\rm spec}(c)=\min\{N(c),[F:\mathbb Q]\}}\). In the very same page the text uses “Theorem ??” and an unfinished Theorem 13.3.1.2 with “Insert statement / State and prove the Main Theorems”. The required full-divisor-to-critical/capped-divisor replacement is **not demonstrated in a completed proof** there.

**Crucial caution:** the two statements may involve source-dependent strip, test lift, Haar, pole or cutoff conventions. The mathematical result below does NOT assert these have been matched. On \(F=\mathbb Q\) norm-only tests, assuming the actual idelic test lift and compact fiber Haar disintegration, the Chapter 12 domain is \(\ker(h\mapsto h(0))\) and Chapter 13's stated moment-domain specializes to \(\ker(h\mapsto\int h)\). Their intersection is nontrivial; PI019–PI020 constructed explicit phase-opposed smooth autocorrelation differences lying in it.

## 2. The unconditional spectral counting needed — and no more

Write a nontrivial \(\zeta\)-zero as \(\rho=\beta+i\gamma\) with \(0<\beta<1\), and its shifted Fourier frequency under the original positive transform as
\[
z_\rho=\gamma-i(\beta-\tfrac12),\qquad
\widehat h(z)=\int_{\mathbb R}h(u)e^{izu}\,du.
\]
Then
\[
\boxed{|\Im z_\rho|=|\beta-\tfrac12|<\tfrac12.}
\tag{PI021-strip}
\]
This is the **classical critical strip**, NOT the critical-line assertion RH.

The unconditional Riemann–von Mangoldt zero-counting law yields
\[
N_\zeta(T)=O(T\log(2+T))
\tag{PI021-count}
\]
(counting multiplicities, with positive and negative ordinates handled symmetrically). This is sufficient. No zero-density estimate close to the critical line, lower gap or simplicity assumption is needed.

The source-compatible candidate *spectral defect* between the Chapter 12 full divisor and Chapter 13 critical/capped divisor has coefficients
\[
b_\rho=
\begin{cases}
m(\rho),&\beta\neq\tfrac12,\\
m(\rho)-\min\{m(\rho),1\},&\beta=\tfrac12.
\end{cases}
\]
For actual \(\zeta\), these are **nonnegative integers**. If an author-specific strip excludes any zeros or the two sides have different additional terms, the coefficients/dictionary must first be adjusted; PI021 does not silently remove such a source requirement.

## 3. The smooth phase probes supply a rapidly convergent ENTIRE test transform

Fix a smooth real nonnegative compactly supported function \(\rho_0\), not identically zero, and let \(\phi=\rho_0'\). Put
\[
R(z)=\int\rho_0(x)e^{izx}\,dx,\quad
C(u)=\int\phi(x)\phi(x-u)\,dx.
\]
For real \(a>\operatorname{diam}(\operatorname{supp}\rho_0)=d\), the phase-opposed smooth differences of the actual autocorrelations are
\[
D_e(a;u)=C(u+a)+C(u-a),\quad
D_o(a;u)=i\big(C(u-a)-C(u+a)\big).
\]
They are all smooth compactly supported and satisfy **both** source-candidate admissibility constraints
\[
\boxed{D_e(a;0)=D_o(a;0)=0,\qquad
\int D_e(a;u)du=\int D_o(a;u)du=0.}
\tag{PI021-admissibility}
\]
Their source-positive entire Fourier transforms are
\[
\boxed{\begin{aligned}
\widehat{D_e(a)}(z)&=
 z^2R(z)R(-z)\big(e^{iaz}+e^{-iaz}\big),\\
\widehat{D_o(a)}(z)&=
 i z^2R(z)R(-z)\big(e^{iaz}-e^{-iaz}\big).
\end{aligned}}
\tag{PI021-transform}
\]

For every integer \(L\ge0\) and every fixed strip \(|\Im z|\le M\),
\[
\boxed{|R(z)|\le C_{L,M}(1+|\Re z|)^{-L}.}
\tag{PI021-R-decay}
\]
Proof by repeated integration by parts; compact support bounds \(e^{-\Im(z)x}\) uniformly for \(|\Im z|\le M\). Thus for coefficients \(|b_\rho|\le m(\rho)\), put
\[
\boxed{t_\rho:=b_\rho z_\rho^2R(z_\rho)R(-z_\rho).}
\tag{PI021-weights}
\]
The unconditional counting law gives
\[
\boxed{\sum_\rho|t_\rho|<\infty.}
\tag{PI021-absolute}
\]
Repeated zeros are combined into one frequency with its total \(b_\rho\); the nontrivial zeros form a locally finite set in the horizontal \(z\)-strip. The complex exponential series
\[
G(a)=\sum_\rho t_\rho e^{iaz_\rho}
\]
converges absolutely and locally uniformly for real a, with the elementary growth bound
\[
|G(a)|\le e^{|a|/2}\sum_\rho|t_\rho|.
\tag{PI021-growth}
\]
Hence the Chapter12-vs-13 defect on both source-phase families, IF the full zero/pole/prime dictionary has been paid, becomes
\[
\boxed{\mathfrak B(D_e(a))=G(a)+G(-a),\quad
\mathfrak B(D_o(a))=i[G(a)-G(-a)].}
\tag{PI021-phase-pair}
\]

## 4. Main mathematical theorem PI021-HALF-LINE-RIGIDITY

**Theorem.** Let \(\Lambda\subset\mathbb C\) be a **locally finite, pairwise distinct** set with \(|\Im z|\le M<\infty\), and let \((t_z)_{z\in\Lambda}\) satisfy \(\sum_{z\in\Lambda}|t_z|<\infty\). Define \(G(a)=\sum_{z\in\Lambda}t_z e^{iaz}\) for real a. If for some real A
\[
\boxed{G(a)=0\quad\text{for ALL real }a>A,}
\tag{PI021-halfline}
\]
then \(\boxed{t_z=0\text{ for every }z\in\Lambda}\).

**Full proof (no RH):**

1. Set \(\sigma=\sup_{z\in\Lambda}\Re(iz)=\sup_{z\in\Lambda}(-\Im z)\le M\). For \(\Re s>\sigma\), absolute convergence allows Fubini:
\[
\begin{aligned}
\mathcal L_+G(s)
&:=\int_0^\infty e^{-sa}G(a)\,da\\
&=\sum_z t_z\int_0^\infty e^{-(s-iz)a}da
=\boxed{\sum_z\frac{t_z}{s-iz}}.
\end{aligned}
\tag{PI021-Laplace}
\]
The interchange is justified by \(\sum|t_z|<\infty\) and the uniform bound \(\Re(s-iz)>\Re s-\sigma>0\).

2. Since \(\Lambda\) is locally finite and \(\sum|t_z|<\infty\), the Cauchy-type series \(\mathcal R(s)=\sum_z t_z/(s-iz)\) converges normally on compact sets avoiding the discrete candidate poles \(i\Lambda\). Hence \(\mathcal R\) is **meromorphic on all \(\mathbb C\)** with at most simple poles, and its residue at \(s=iz\) is exactly \(t_z\).

3. If \(G(a)=0\) for a>A, then its Laplace transform is an integral over the *finite* positive interval \([0,\max(A,0)]\), so
\[
H(s)=\int_0^{\max(A,0)}e^{-sa}G(a)\,da
\]
is **entire** (if A<0, this integral is zero and \(G\) is zero already on \(a\ge0\)). By Step 1, \(H(s)=\mathcal R(s)\) for all \(\Re s>\sigma\).

4. Analytic continuation on the connected domain \(\mathbb C\setminus i\Lambda\) forces \(\mathcal R=H\) there. Every apparent pole \(s=iz\) is therefore removable. Its residue \(t_z\) must be zero. QED.

This is an **INFINITE-SPECTRUM theorem**, with no spectral truncation, no positivity of weights, and no real-frequency assumption. It is stronger than PI020's finite Vandermonde lemma, but it requires **vanishing on a FULL UNBOUNDED TRANSLATION HALF-LINE**, not merely a bounded open interval.

**Validity check / why the stronger hypothesis is essential.** Fix any smooth compact real bump \(\rho_0\) with support diameter \(d\ll\pi\). Let \(C(u)=\int\rho_0(x)\rho_0(x-u)dx\), and periodize it by \(F(a)=\sum_{k\in\mathbb Z}C(a+2\pi k)\). Then
\[
\sum_{n\in\mathbb Z}n^2|R(n)|^2e^{ina}=-2\pi F''(a).
\tag{PI021-periodic-counterexample}
\]
The coefficients are **nonnegative, rapidly decreasing**, the spectral set \(\mathbb Z\setminus\{0\}\) is real and has linear counting, yet the nonzero sum vanishes on any bounded interval disjoint from the periodic support of \(C\). Its even/odd phase combinations likewise vanish there. It is **not** zero on every sufficiently large a because it repeats near \(2\pi\mathbb Z\). Thus a bounded open-interval infinite-series uniqueness assertion would be FALSE even for benign positive coefficients. The half-line assumption is doing real mathematical work.

## 5. Generic nonvanishing of all smoothed coefficients, including infinitely many zeros

The infinite theorem forces the *smoothed* \(t_\rho=0\). To conclude \(b_\rho=0\) at a given noncentral frequency \(z_\rho\ne0\), one needs \(R(z_\rho)R(-z_\rho)\ne0\).

This can be achieved **simultaneously at all noncentral zeta frequencies** without RH or an unproved zero-free region.

Take any fixed smooth nonnegative \(\rho_0\not\equiv0\) with \(\int\rho_0>0\), and define
\[
\rho_\varepsilon(x)=\varepsilon^{-1}\rho_0(x/\varepsilon),\quad
R_\varepsilon(z)=R_0(\varepsilon z).
\]
For each **fixed** \(z\ne0\), \(\varepsilon\mapsto R_0(\pm\varepsilon z)\) are analytic functions near the real \(\varepsilon\)-axis, with nonzero values at \(\varepsilon=0\) equal to \(\int\rho_0\). Their positive-real zero sets are discrete (hence countable). The union of these excluded \(\varepsilon\) over the **countable** noncentral zero divisor is countable. Choose any sufficiently small positive \(\varepsilon\) outside this union. Then
\[
\boxed{
R_\varepsilon(z_\rho)R_\varepsilon(-z_\rho)\ne0
\quad\text{for ALL }z_\rho\ne0.
}
\tag{PI021-generic-bump}
\]
The smoothing and compact-support assumptions are preserved. No numerically computed zeta-zero roster is needed to choose such an \(\varepsilon\); this is an existence proof, not an effective algorithm.

## 6. CONDITIONAL source consequence: why the missing Chapter 13 proof is decisive

**Explicit hypothesis H, NOT established by PI021:** both Masullo Chapter 12 and Chapter 13 trace identities genuinely hold on the **same** norm-radial \(F=\mathbb Q\) smooth test space with the **same** local/global pole, prime, archimedean, Haar and cutoff normalization, their zero strips/character indexing have been reconciled to the entire nontrivial ζ divisor, and their right-hand geometric functionals truly agree on every smooth compact test in \(E_e\cap E_m\).

If H holds, then for *every real translation* \(a>d\), both phase probes in (PI021-transform) are admissible, so the proposed divisor difference satisfies
\[
\mathfrak B(D_e(a))=\mathfrak B(D_o(a))=0.
\]
By the paired phase equations, \(G(a)=0\) for all \(a>d\). PI021-HALF-LINE-RIGIDITY then forces every smoothed spectral defect coefficient \(t_\rho=0\). Choose the generic bump from Section 5 to conclude
\[
\boxed{b_\rho=0\quad\text{at EVERY NONCENTRAL nontrivial ζ-zero.}}
\tag{PI021-conditional-divisor}
\]
Hence **IF H were proved**, there would be **no off-critical nontrivial zeros and no excess critical-line multiplicities away from \(z_\rho=0\)**. This is a **conditional** conclusion. The ordinary \(\zeta(1/2)\ne0\) also follows independently by the alternating eta-series for \(0<s<1\), so for the Riemann zeta function the central exception does not leave an actual zero. Therefore, under H, RH and simplicity of all nontrivial ζ-zeros would follow.

**This is NOT a proof of RH or simplicity:** the strong source-comparison hypothesis H is neither derived from Chapter 12 alone nor authenticated by Chapter 13's visibly unfinished proof. Indeed the conditional consequence illustrates how deep that missing Chapter 13 replacement theorem is. Do not declare the manuscript's labeled theorem independently established; do not silently use its desired conclusion as an assumption in a proof of H.

**Further scope limitations:** this argument uses the *full unbounded family* of translated smooth radial tests. It does NOT follow from the original IV fixed two-collar n=9 tests at a SINGLE translation \(a=\log9\). For general number fields/nontrivial Hecke characters, central zeros may occur and additional character/test-fiber identifications are necessary. For the \(\zeta\)-case, this is a test-level conditional zero-divisor statement, not positivity of an independently constructed operator.

## 7. Audit of the original manuscript's analytic requirements

The zero-side summability in Section 3 and infinite exponential uniqueness in Section 4 require only classical analytic number theory and compact smooth Fourier decay, and are **fully proved classically here**. They do **not** solve the exact missing source requirements:

1. **Chapter 13 proof:** establish its claimed critical-line/capped zero sum on the stated moment-zero class, rather than merely asserting that theorem and citing Chapter 12 (different domain and divisor).
2. **Common geometric side:** ensure the two pole Mellin evaluations, real place Gamma, full prime sums, Haar measure and cutoff scheme match the same original global signed Weil functional, not just a similar printed expression.
3. **Radial lift:** confirm the norm-pullback \(C_c^\infty(\mathbb R)\to\mathcal D(C_\mathbb Q)\), Haar compact-fiber disintegration and the two imposed test restrictions reduce to \(h(0)=0\) and \(\int h=0\), including continuity in the source topology.
4. **Full zeros/strip:** compare the same full divisor with multiplicity. If the Chapter 12 strip does not contain all nontrivial ζ-zeros, fix it with proof, not by silently enlarging the sum.
5. **Contact and actual operator:** even when the two source expressions agree on \(E_e\cap E_m\), the separate PI019 gluing step and Masullo finite-part cutoff normalization must be paid to identify a diagonal trace and derive an intrinsic whole-test functional. A zero-divisor conclusion conditional on H is not a direct identification with an operator's coercivity/positivity.

The independent zero counting \(N_\zeta(T)=O(T\log T)\) is standard unconditional background (Riemann–von Mangoldt), not a project compiler certificate or a zeta zero-free proof.

## 8. Exact algebra checks without inflating Actions

\`scripts/pi021_exact_laplace_pole_preflight.py\` checks **21** exact Gaussian-rational finite-meromorphic residue-isolation bounds for synthetic noncentral frequencies \(z_n=n+i/4\), with exactly resolved pole locations \(s=iz_n\) and positive rapidly decaying rational coefficients. The direct algebra test confirms that, on the finite model, every pole's residue equals its own coefficient and a holomorphic Laplace continuation could not hide nonzero isolated residues. The script **does not** prove the infinite theorem; that proof is Section 4. The script does NOT compute genuine ζ-zeros, actual Masullo traces, or any Fourier inversion from Weil-Lab's pending Lean candidates.

**No new PR, no Lean source, no GitHub Actions workflow, and no NF/IV/CP modifications.** Source branch is separate and the PI registry records this analytical stage without triggering generic repository PR CI.

## 9. PI022 — next analytic-only gate

The infinite uniqueness lemma is now a classical analytic ingredient rather than an unresolved assumption. PI022 must focus on **hypothesis H** itself:

- Inspect Chapter 13's actual proof references, cutoffs and divisor definitions, including whether its geometric side truly matches Theorem 12.5.1.1 for **all sufficiently separated** radial phase test translations, not merely one fixed collar or one Mellin moment.
- Establish the exact \(\mathcal D(C_\mathbb Q)\) radial test and Haar disintegration dictionary, including independent agreement of the two poles and source prime term. No operator equality may be introduced by definition.
- If the manuscript lacks the required Chapter 13 proof (as the inspected November edition does), keep H **OPEN** and record the resulting implication as a proof audit, not a theorem about ζ.
- Only after authenticated overlap equality, apply the source-exact infinite rigidity result. Subsequently the PI019 two-domain gluing/contact calibration remains separate; the original signed Weil positivity and Masullo operator trace identity beyond its literal hypotheses are not outcomes of PI021.
- NF compiler certification and CI recovery continue independently. PI, IV and CP remain analytic-first.

**PI021 conclusion:** PI020's finite-vs-infinite uniqueness concern can be resolved under the genuinely available full translation half-line and standard unconditional zero growth. The bottleneck moves to the **independent validity and common-source normalization of the Chapter 13 trace identity**. This is potentially a very strong conditional implication and is emphatically not a completed RH argument.
