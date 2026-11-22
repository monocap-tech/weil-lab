# Weil-Lab — UOI040: genuinely nested sparse supports, uniform Gamma control, and the exact arithmetic leakage obstruction

**Status:** Analytic theorem/proof and a conditional full-form inequality; **not Lean kernel certified**. No global Weil positivity, source/native equivalence, or RH assertion. No new repository or CI submission. The independent NF gate acceptance count is not changed here.

## Exact basis and normalization

This note extends the *specific UOI039 report*, `UOI039_sparse_support_prime_cycles_and_uniform_margin.md`, and its pinned original definitions in `monocap-tech/weil-lab`, research commit `614ba879f7389fdb620c474adaee273b00eac71c`. Those original definitions use

- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean`, `neutralIV017SignedGamma_lower`: for smooth complex Schwartz `f`,
  \[
  \Gamma(f)\ge \tfrac{11}{10}\|f\|_2^2-\tfrac{67}{10}\int_{-5}^5|\widehat f(\xi)|^2d\xi,
  \]
  where \(\widehat f(\xi)=\int f(x)e^{-2\pi i\xi x}dx\).
- `WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean`: the **full** signed original prime term, not the half-weight physical translation shell:
  \[
  P(f)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \{C_f(\log n)+C_f(-\log n)\},\quad
  C_f(s)=\int f(x)\overline{f(x-s)}dx.
  \]
  For compact support the sum is finite, and \(P(f)\) is real on the diagonal.
- `WeilDefect/Morphology/NeutralWeilSourceMixedForm.lean`: \(m_\pm(f)=\int f(x)e^{\pm x/2}dx\), and the pole form
  \(Q(f,g)=\overline{m_-(f)}m_+(g)+\overline{m_+(f)}m_-(g)\).
- `WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean`: the original sign convention \(W_{\mathrm{lit}}=\Gamma-P+\operatorname{Re}Q\). The **Lean identity** between this entire literal expression and the new arbitrary-support Schwartz correlation remains a separate outstanding compiler obligation; the older source-proved `neutralNF600SmoothWeil_split` only covers its historical collars.

Throughout, \(\|f\|_2^2=M\). We work only with compactly supported smooth inputs, so all displayed Fourier/Gamma expressions are defined. Do not confuse these form values with the zero-side theorem or a completed spectral bridge.

## 1. A genuinely nested family

Put \(t=\log8\), \(r=8^{-1/2}\), and for each \(j\ge0\) choose
\[
 c_j=(j+\tfrac12)t,\qquad \delta_j=\frac{8^{-j}}{1000},\qquad I_j=(c_j-\delta_j,c_j+\delta_j).
\]
Let \(D_m=\bigcup_{j=0}^{m-1}I_j\), \(m\ge2\). The \(I_j\) are pairwise disjoint, lie strictly to the right of the old \([-1,1]\), and their centers tend to infinity. **Unlike UOI039,** the interval \(I_j\) never changes once added, hence
\[
 \boxed{D_m\subset D_{m+1}\text{ strictly}.}
\]

On each \(I_j\) let \(K_j\) be the closed complex subspace of \(L^2(I_j)\) on which **all three local functionals** vanish:
\[
 \int_{I_j}u(x)dx=0,\quad \int_{I_j}u(x)e^{x/2}dx=0,\quad
 \int_{I_j}u(x)e^{-x/2}dx=0.
\]
Set \(K_m=\bigoplus_{j<m}K_j\) with zero extension. Then \(K_m\subset K_{m+1}\) is an isometric inclusion; each \(K_j\) is infinite-dimensional of codimension three. To exhibit supported smooth vectors in it, take \(u=(\partial_x)(\partial_x^2-1/4)\eta\) for arbitrary \(\eta\in C_c^\infty(I_j)\); integration by parts kills \(1,e^{x/2},e^{-x/2}\). There is no claim that **all** vectors in \(L^2(D_m)\) satisfy these conditions.

For \(f\in K_m\cap C_c^\infty(D_m)\), both **global** pole moments vanish, hence \(Q(f,g)=0\) for every compact-support test \(g\). This is genuine extension stability of the pole radical.

## 2. Uniform low-frequency control on the nested spaces — proved

Write \(f=\sum_{j<m} f_j\), with \(f_j\) supported in \(I_j\), and use the local **ordinary integral zero** on each collar. For \(|\xi|\le5\), the elementary bound
\(|e^{-2\pi i\xi y}-1|\le2\pi |\xi||y|<32\delta_j\) for \(|y|<\delta_j\) implies
\[
\begin{aligned}
|\widehat f(\xi)|
&=\Bigl|\sum_{j<m}e^{-2\pi i\xi c_j}
\int_{I_j}f_j(x)(e^{-2\pi i\xi(x-c_j)}-1)dx\Bigr|\\
&\le32\sum_{j<m}\delta_j\sqrt{2\delta_j}\,\|f_j\|_2\\
&\le32\Bigl(2\sum_{j<m}\delta_j^3\Bigr)^{1/2}\|f\|_2.
\end{aligned}
\]
The last inequality is Cauchy–Schwarz **over collars**. In particular, there is no factor growing with \(m\). Integrating over the band of length ten yields
\[
\boxed{
\int_{-5}^5|\widehat f(\xi)|^2d\xi\le
20480\Bigl(\sum_{j<m}\delta_j^3\Bigr)M
\le\underbrace{\frac{4096}{199609375}}_{\displaystyle B\approx2.05201\times10^{-5}}M.}
\]
The last equality uses \(\sum_{j\ge0}\delta_j^3=(1/1000)^3/(1-1/512)\). Consequently the **original signed Gamma contribution** satisfies the uniform lower bound
\[
\boxed{\Gamma(f)\ge G M,\qquad
G=\frac{11}{10}-\frac{67}{10}B
=\frac{2195428693}{1996093750}>1.09986.}
\]
This is a genuine result for nested, increasing, unbounded-support *admissible subspaces*. It does not invoke any prime estimate or positivity of the complete Weil form.

## 3. What remains controlled: the arithmetic 8-power ladder

Define \(P_8(f)\) by retaining just the genuine prime powers \(n=8^d\) (\(d\ge1\)) in the original prime sum; set \(E_m(f):=P(f)-P_8(f)\) on the finite-support domain \(D_m\). Although **new non-ladder prime powers** may now occur, the ladder itself remains absolutely bounded for every test:
\[
\begin{aligned}
|P_8(f)|
&\le2\sum_{d\ge1}\frac{\log2}{\sqrt{8^d}}\,
|C_f(d\log8)|\\
&\le\frac{2\log2}{\sqrt8-1}\,M
<\frac{695}{914}M.
\end{aligned}
\]
Indeed \(|C_f(s)|\le M\) by Cauchy–Schwarz/translation isometry, and the geometric series converges. The rational upper certificate is inherited from UOI039: \(\log2<139/200\), \(\sqrt8>707/250\).

The new **non-ladder leakage** \(E_m\) is itself a finite Hermitian quadratic form for every fixed \(m\), since all tests have compact support. Its positive Rayleigh bound on the pole- and local-mean-neutral subspace is
\[
\ell_m:=\max\Bigl(0,\sup\{E_m(f): f\in K_m,\ \|f\|_2=1\}\Bigr)\in[0,\infty).
\]
Here \(E_m(f)\) is real, and the sup extends to the closed \(L^2\) subspace by boundedness of the **finite** translation sum. We are **not** asserting that \(\sup_m\ell_m\) is finite or small.

Combining the three exact constituents of the literal signed expression gives the **conditional nested extension theorem**
\[
\boxed{
W_{\mathrm{lit}}(f)\ge
\left(\underbrace{\frac{154834167288}{456107421875}}_{\displaystyle M_0\approx0.339468642390}-\ell_m\right)\|f\|_2^2.
}
\]
This follows from \(G-695/914=M_0\). In particular:

- If \(\sup_m\ell_m < M_0\), the **entire nested union** carries a uniform strictly positive literal-form margin (no claim about its complement).
- To retain the simpler \(W_{\mathrm{lit}}\ge\frac13M\), it is enough to prove
  \[
  \sup_m\ell_m\le M_0-\frac13
  =\frac{8395079989}{1368322265625}\approx0.00613530906.
  \]
- To retain \(W_{\mathrm{lit}}\ge\frac14M\), it suffices to show \(\sup_m\ell_m\le M_0-1/4\approx0.0894686424\).

**None of these leakage hypotheses has been proved.** The advantage is that the outstanding problem is isolated to one explicitly defined, falsifiable arithmetic operator quantity; Gamma and pole stability are not the source of this uncertainty for this family.

## 4. A no-go theorem for copying UOI039's exact prime graph into a nested chain

**The first explicit failure already occurs at the fifth collar (index \(j=4\)).** The center spacing from \(I_0\) to \(I_4\) is \(4\log8=\log4096\). The integer **4099 is prime** (direct trial division by every integer \(2\le d\le64\) shows none divides it), so \(\Lambda(4099)=\log4099>0\). Yet
\[
0<\log4099-4\log8=\log(1+3/4096)<3/4096<1/1000=\delta_0.
\]
Thus a genuine **non-ladder** prime term can connect \(I_0\) and \(I_4\) even though UOI039's fixed-\(m\) construction excluded every such term. The right collar \(I_4\) is tiny, but that is no obstruction to constructing arbitrarily tiny test bumps supported there. This gives an entirely elementary, finite-support counterexample for **every** nested stage \(m\ge5\): the original prime compression cannot equal the pure 8-power Toeplitz matrix on the unrestricted supported test space.

There are also arbitrarily remote independent resonances. For every \(\varepsilon>0\) there are arbitrarily large positive integers \(d,k\) for which
\[
\boxed{0<|d\log8-k\log3|<\varepsilon.}
\]
**Proof.** The real number \(\alpha=\log8/\log3\) is irrational: a rational equality \(d\log8=k\log3\) would imply \(8^d=3^k\), contradicting unique prime factorization. Dirichlet's approximation theorem gives infinitely many \(k/d\) with \(|\alpha-k/d|<1/d^2\), so \(0<|d\log8-k\log3|<\log3/d\to0\). **Every \(3^k\) is a genuine von Mangoldt prime power** with coefficient \(\log3/3^{k/2}>0\).

Fix \(\delta_0=1/1000\) and use the nested family above. Either take the **explicit** \(d=4, n=4099\) resonance or pick \(d,k\) from the infinitely many prime-power approximants above so \(0<|d\log8-k\log3|<\delta_0/4\), and put \(\epsilon=\log n-d\log8\), with \(n=4099\) in the explicit example and \(n=3^k\) in the infinite family. Choose two tiny **nonnegative** smooth bumps supported respectively around \(c_0-\epsilon\) in \(I_0\) and around \(c_d\) in \(I_d\), with bump halfwidth
\[w<\min\{\delta_0-|\epsilon|,\ \delta_d,\ |\epsilon|/3\}.\]
Their translated ordinary overlap at shift \(d\log8\) is zero (their relative local offsets differ by \(\epsilon\neq0\)), while the overlap at the **non-ladder** shift \(\log n\) is strictly positive. The ladder terms at other separations are zero by disjoint collar geometry. For the sum of these two nonnegative bumps, \(P_8(f)=0\), but \(P(f)>0\) because the chosen non-ladder \(n\)-summand is strictly positive and all other prime-correlation contributions are nonnegative. Thus **the full prime operator on nested physical supports is not the pure 8-power Toeplitz operator** for infinitely many support levels.

This witness is on the **unrestricted smooth support space**: nonnegative bumps cannot themselves satisfy \(\int_{I_j}f_j=0\). It disproves exact prime-graph identity on the whole physical support space, not a uniform lower bound for \(\ell_m\) on the constrained \(K_m\). Whether these extra arithmetic interactions have significant positive Rayleigh norm *on the pole-neutral filtered spaces* is precisely the open quantitative question.

For an illustrative high-precision (not symbolic) instance, \(d=1054, k=1995\) gives
\(|1054\log8-1995\log3|\approx0.000130962331766<0.00025\). This is a numerical illustration of the general irrational-approximation proof; the proof does not depend on this particular pair.

## 5. How this changes the research direction

1. **Unconditional analytic progress:** nested subspaces \(K_m\subset K_{m+1}\) really exist; the exact pole radical survives the inclusions, and \(\Gamma(f)\ge G\|f\|_2^2\) uniformly in \(m\). This overcomes UOI039's non-nesting issue for **two of the three components**, not for the full signed form.
2. **Definitive obstruction:** the original prime correction cannot stay the exact finite 8-power Toeplitz operator under this nesting. A genuinely new prime edge \(n=4099\) already appears between collars 0 and 4 (so \(m=5\) is enough); infinitely many further \(3\)-prime-power near-resonances follow from irrationality and Dirichlet approximation. No deep prime-distribution theorem is needed.
3. **Single measurable missing input:** bound \(\ell_m\) uniformly. A finite-m numerical experiment must verify the genuine \(\Lambda(n)\) coefficients, source support, full two-sided correlation convention, and the local moment constraints. Observing a small \(\ell_m\) at a few moderate \(m\) does **not** establish the all-m theorem.
4. **Cross-projection compatibility:** the inherited prime-ladder bound is coordinate invariant only under a specified unitary that preserves the decomposed **full original prime form**; the partition into ladder and leakage depends on the chosen collar coordinates. An independent spectral construction must reproduce the **complete** arithmetic correction, not just the universal 8-ladder matrix.

### Remaining Lean obligations (no new CI submission in this note)

- Source-level arbitrary-support literal \(\Gamma-P+Q\) identity for a compact Schwartz autocorrelation, including all signs, both pole moments, exact \(2\pi\) Fourier normalizations and all surviving prime powers.
- In Lean, construct fixed \(I_j\), the local three-moment kernels, zero-extension embeddings \(K_m\hookrightarrow K_{m+1}\), and their exact pole radical laws.
- Formalize the local-mean-subtracted Fourier bound and finite/infinite geometric series to certify \(G\) with strict standard axiom audit.
- Define the Hermitian off-ladder compressed prime form and bound its positive Rayleigh supremum; this is the **actual missing mathematical estimate**, not a bookkeeping lemma. The irrational-rotation no-go proof can be formalized separately and must not be confused with a successful bound.

**Result:** UOI040 is a genuine nested-support advance for Gamma and pole terms, paired with an elementary but decisive warning that exact UOI039 prime geometry cannot persist under this nesting. It stops before any unproved all-m arithmetic leakage claim.
