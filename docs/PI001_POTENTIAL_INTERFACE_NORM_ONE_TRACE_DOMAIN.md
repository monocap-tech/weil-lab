# PI001 — Potential Interface: mixed Weil correlations to norm-one trace tests

**New independent research lane: PI### (Potential Interface).**
PI is an explicit *interface experiment* under the broader CP001 compatibility hypothesis (draft PR #790). PI does not replace CP###, Phase IV IV### (currently IV020, draft PR #788), or Phase III NF### (currently NF750, draft PR #789). PI001 is based on main to avoid importing unaccepted IV009–IV020 proofs.

**Status:** mathematical domain-gate investigation and exact-rational support preflight only. NO Lean acceptance, no isometry, no equality of arithmetic and spectral traces, no RH/GRH claim.

## A. Primary sources and the reverse-engineering question

- Original Weil-Lab literal signed zeta form and exact old/new windows: IV011, IV015–IV020, notably IV019 https://github.com/monocap-tech/weil-lab/pull/787 and IV020 https://github.com/monocap-tech/weil-lab/pull/788 .
- Masullo, *The Music of the Primes*, November 2026 manuscript, chapter 1 page 28 (also chapter 1 subsection 1.8.4), https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf . The displayed trace formula assumes both (a) \(\varphi\in\mathcal D(C_F)\), smooth and compactly supported, and (b) \(\varphi(C_F^1)=0\), where \(C_F^1=\ker|\cdot|_F\). The full theorem 12.5.1.1 and the subsequent zero-location argument require independent verification, not merely this introduction.
- Independent Masullo Lean effort (not an author proof certificate): https://github.com/mccorvie/riemann-masullo .
- Alpöge Comparator target statements: https://github.com/Deicyde/riemann-hypothesis/blob/main/src/Challenge.lean . This establishes target propositions, NOT a test-function map from the arithmetic proof.
- CP001 full finite-compression conjecture: https://github.com/monocap-tech/weil-lab/pull/790 .

**PI001 question:** Does the authentic original Weil mixed correlation, after a correctly normalized norm-pullback, enter the admissible test domain of Masullo's trace formula? If so, under which restrictions can one compare the full signed prime/pole/Gamma expression with the spectral trace, without losing zero multiplicities?

## B. Fix the proposed map and prove the elementary domain gate

For \(s,t\in C_c^\infty(\mathbb R;\mathbb C)\) or genuine complex compactly supported Schwartz tests, fix
\[
h_{s,t}(u)=\int_\mathbb R t(x)\,\overline{s(x-u)}\,dx .
\]
This is a compactly supported smooth function and \(h_{s,t}(0)=\int t(x)\overline{s(x)}\,dx=\langle t,s\rangle_{L^2}\) (subject to explicitly choosing the inner-product convention).

For a number field \(F\), let \(C_F\) be its idele class group, \(\ell_F(g)=\log|g|_F\), and \(C_F^1=\ker\ell_F\). Define the **candidate**, not-yet-certified operator-trace test:
\[
\Phi_{s,t}(g)=h_{s,t}(\ell_F(g)).
\]
Because \(\ell_F(g)=0\) on \(C_F^1\), the exact algebraic identity is
\[
\Phi_{s,t}|_{C_F^1}=h_{s,t}(0)=\langle t,s\rangle_{L^2}.
\]
Therefore
\[
\boxed{\Phi_{s,t}(C_F^1)=0\quad\Longleftrightarrow\quad \langle t,s\rangle_{L^2}=0.}
\]
This is a **necessary test-domain seam**, not an operator equivalence.

For the genuine original old two strict collars
\(E_- =(-11/10,-11/10+1/500)\),
\(E_+=(11/10-1/500,11/10)\),
and the new central interval
\(E_0=[1/5-1/500,1/5+1/500]\),
every \(s\) supported on \(E_-\cup E_+\) and \(t\) supported on \(E_0\) have disjoint supports. Hence \(h_{s,t}(0)=0\). In fact \(h_{s,t}\) vanishes on an open neighborhood of \(u=0\); the source-support separation is strictly positive.

**Diagonal obstruction:** for each nonzero \(t\), \(h_{t,t}(0)=\|t\|_2^2>0\); the naive norm pullback \(\Phi_{t,t}\) fails Masullo's stated vanishing condition. No linear combination of zero-at-zero mixed correlations can reproduce a diagonal correlation with nonzero value at zero. This specifically prevents inferring full diagonal Weil positivity from the mixed test-domain match.

**Further unproved conditions:** It is NOT enough to show vanishing on \(C_F^1\). Establish rigorously that \(\Phi\) belongs to the required \(\mathcal D(C_F)\) (its topology, smoothness, compactness, and any regularization hypotheses), using a justified norm-map/properness argument. Verify Haar normalizations. Norm-only pullback is \(C_F^1\)-invariant; it cannot by itself detect an arbitrary nontrivial Hecke-character isotypic sector. For PI001, restrict the first source comparison to \(F=\mathbb Q\) and the trivial-character sector. Twisting is a later explicit additional map, not a free identification.

## C. Exact three-cell prime geometry to retain

Freeze old support centers \(\pm1099/1000\), each with radius \(1/1000\); new support center \(1/5\), with radius \(1/500\) (the doubled-radius IV019/IV020 case).

For old center \(c_o\), new center \(c_n\), define
\[
\Delta_{o,n}=c_n-c_o,\qquad R=r_o+r_n=3/1000.
\]
A necessary sufficient geometric noninteraction for the original prime-side correlation at signed shift \(\sigma\log n\) is
\[
|\Delta_{o,n}-\sigma\log n|>R,\qquad \sigma\in\{-1,+1\}.
\]
The original cutoff \(n\ge 10\) follows if \(\log 10>11/5\) and every correlation comes from the original physical window \([-11/10,11/10]\). For all \(2\le n<10\), the preflight tests *every integer* (a stronger condition than restricting to \(\Lambda(n)\ne 0\)). New-self shifts are excluded by \(\log 2>2r_n\). **Old-old \(n=9\) is not excluded**; the old collar centers differ by \(1099/500\) and \(n=9\) remains a genuine arithmetic interaction.

The independent script \(scripts/pi001_norm_pullback_preflight.py\) checks those geometric inequalities and the old-old \(n=9\) overlap using only rational atanh-series bounds on real logarithms. It makes NO claims about trace-class convergence or arithmetic-spectral equality.

## D. Backward dictionary: explicit checks, not assumed equivalences

To compare the two original formulas after the domain gate, prove separately:

1. The full \(\Phi_{s,t}\) test belongs to the Masullo theorem's actual domain, including the correct smooth compact support on \(C_\mathbb Q\) and any required spectral/trace assumptions.
2. Mellin on \(C_\mathbb Q\) of a norm-pullback agrees with the bilateral Laplace/Fourier transform of \(h_{s,t}\), with a **specified Haar quotient constant** and the same \(s\mapsto s-\tfrac12\) centering. A formal substitution \(u=\log|g|\) is not sufficient.
3. The complete genuine von Mangoldt prime/power coefficients, both \(\pm\log n\) samples and the **surviving old-old \(n=9\)** agree with the relevant local geometric trace terms. No missing nontrivial-character terms may be silently dropped.
4. The two original pole evaluations and full signed digamma/Gamma archimedean term agree with Masullo's corresponding trace normalization and regularization.
5. The spectral side retains **all zeros with full multiplicity** in the comparison. Check exact trace-domain restrictions, any strip boundary terms, possible spectral truncation and topology dependence; do not assume Masullo's final spectral realization is proved.
6. Explain how a full diagonal form would be recovered. A candidate correction \(h\mapsto h-h(0)\eta\), with smooth compact \(\eta\) and \(\eta(0)=1\), is admissible at zero but changes the full original arithmetic functional by \(h(0)W(\eta)\). Prove any correction term instead of omitting it.
7. For Alpöge, identify an actual source-exposed arithmetic test functional and a map from the original weighted von Mangoldt sum to the same \(h\). Until such a map exists, no three-way identification is claimed.

**Important type mismatch:** \(h_{s,t}\) is sesquilinear in \((s,t)\), whereas Masullo's trace is a *linear functional of \(\Phi\)*. An equality of scalar traces for some \(\Phi\) does NOT give a linear isometric map from physical test Hilbert spaces or preserve positive quadratic forms automatically.

## E. PI-C1 — falsifiable first compatibility conjecture

Fix \(F=\mathbb Q\), the trivial Hecke-character sector, and one pair of explicit nonzero smooth bumps \(s\) in an original strict collar and \(t\) in the doubled-radius central interval, with the exact correlation \(h_{s,t}\) above. Define \(\Phi_{s,t}=h_{s,t}\circ\ell_\mathbb Q\).

**PI-C1 (unproved):** After fixing Masullo's precise trace domain and Haar normalization, \(\Phi_{s,t}\) is admissible, and the *complete*, regularized trace formula evaluated at \(\Phi_{s,t}\) equals the original signed Weil **mixed** pairing of \(s,t\), with both sides written in matching complex/Hermitian conventions, all primes/powers, both poles, the whole archimedean term, and all pertinent zeros/multiplicities.

Potential falsifiers / stop conditions:
- The proposed \(\Phi\) fails a real domain condition not fixable while preserving the original correlation.
- A genuine local trace term disagrees with a corresponding original prime/pole/Gamma term after normalizations are frozen and independently checked.
- A mass/pairing-preserving map cannot be extended to diagonal \(t=t\) without nonzero correction terms; such a failure falsifies a stronger **full-form** identification, though not PI-C1 for the mixed test.
- A character or multiplicity sector required for the claimed comparison is absent from the norm-pullback image.

This is a mathematically definite first seam, not global Weil positivity, RH/GRH or proof-method equivalence.

## F. Parallel work and PI numbering

- **PI001:** freeze primary source clauses, formulate the norm-one domain-gate lemma, run rational support/prime-gap preflight; file as a draft research branch; no Lean PASS yet.
- **PI002 (next):** prove the full \(F=\mathbb Q\) test-domain and Haar/Mellin conversion, pin a Masullo trace formula version and compute the actual first mixed entry with all terms.
- **PI003:** source-specific diagonal correction or rigorous obstruction, spectral zero-multiplicity and character-sector audit.
- **PI004:** extract a usable test-functional from Alpöge's released Lean source and test the arithmetic leg.
- **PI005:** compare PI's exact dictionary against CP001's finite normalized 3x3 compression; stop on disagreement.

**Custody:** PI operates on its own branch from main. No modifications to NF###, IV###, CP### theorem modules or status ledgers. The real Phase IV certification and Phase III numerical production proceed independently. No unverified source assumption may be labeled Lean PASS.
