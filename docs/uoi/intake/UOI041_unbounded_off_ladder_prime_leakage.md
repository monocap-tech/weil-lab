# Weil-Lab — UOI041: the off-ladder positive Rayleigh leakage is unbounded on the nested three-moment kernel

**Status:** Analytic theorem, conditional only on the classical Prime Number Theorem (PNT), plus an elementary explicit five-collar witness. Not Lean kernel-certified. Does **not** establish a negative value of the complete signed Weil form, support-independent positivity, or RH. Does not modify GitHub/CI or the independent NF certification frontier.

## 0. Exact parent and source contracts

This statement uses the **specific UOI040 nested family**, `UOI040_nested_support_arithmetic_leakage.md`, and the original source-pinned formulas at `monocap-tech/weil-lab`, commit `614ba879f7389fdb620c474adaee273b00eac71c`:

- `WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean` defines the **full original** arithmetic quadratic term
  \[
  P(f)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\bigl(C_f(\log n)+C_f(-\log n)\bigr),\qquad
  C_f(s)=\int_{\mathbb R} f(x)\overline{f(x-s)}\,dx.
  \]
  On smooth compactly supported functions, this sum is finite. The diagonal is real and equals \(2\sum_{n\ge2}(\Lambda(n)/\sqrt n)\operatorname{Re} C_f(\log n)\).
- `WeilDefect/Morphology/NeutralWeilSourceMixedForm.lean` defines the exponential pole moments \(m_\pm(f)=\int f(x)e^{\pm x/2}dx\) and their mixed pole form.
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean` provides a source-level signed Gamma lower estimate, but the full arbitrary-support literal-form transfer from the original fixed collars is **not yet Lean certified**.

We set
\[
 t=\log8,\quad N_d=8^d,\quad c_j=(j+\tfrac12)t,\quad
 \delta_j=\frac{8^{-j}}{1000},\quad I_j=(c_j-\delta_j,c_j+\delta_j).
\]
For \(m\ge2\), let \(K_m\subset L^2(\bigcup_{j<m}I_j)\) consist of functions whose restriction to **each** \(I_j\) has three zero moments: \(\int f_j=\int f_je^{x/2}=\int f_je^{-x/2}=0\). The inclusion \(K_m\hookrightarrow K_{m+1}\) is zero-extension.

Let \(P_8\) contain only \(n=8^k\) terms of \(P\), and \(E_m=P-P_8\) restricted to \(K_m\). Define
\[
 \ell_m=\max\bigl(0,\sup\{E_m(f):f\in K_m,\ \|f\|_2=1\}\bigr).
\]
For each fixed \(m\), the relevant full prime sum is a finite Hermitian form, so the number is finite. **The theorem below disproves finiteness of \(\sup_m\ell_m\).**

## 1. Elementary five-collar result: the first extra edge survives all three local moment conditions

Take \(d=4\), \(N=8^4=4096\), and the genuine prime \(p=4099\). Primality is checked by trial division up to \(\lfloor\sqrt{4099}\rfloor=64\). Put
\[
 \varepsilon=\log(p/N)=\log(4099/4096),\qquad 0<\varepsilon<3/4096<\delta_0.
\]
Note \(\delta_4=1/(1000\cdot4096)\). Choose a positive width \(w\) sufficiently small, for example
\[
 0<w<\min\bigl\{\delta_4/8,\ (\delta_0-\varepsilon)/4,\tfrac1{10}\log(4100/4099)\bigr\}.
\]
Let \(\eta\in C_c^\infty((c_4-w,c_4+w))\) be nonzero and choose the nonzero smooth function
\[
 \phi=(\partial_x)(\partial_x^2-\tfrac14)\eta.
\]
The formal adjoint acting on \(e^{\lambda x}\) is \(-\lambda(\lambda^2-1/4)\), so
\[
 \int \phi(x)e^{\lambda x}dx=0\qquad(\lambda=0,\pm\tfrac12).
\]
Define \(g_p(x)=\phi(x+\log p)\), which is supported in \(I_0\) because its center equals \(c_4-\log p=c_0-\varepsilon\). Translation preserves all three zero moments. Hence
\(f=\phi+g_p\in K_5\cap C_c^\infty\).

The two supports have the **exact** shift \(\log p\). All correlations at \(\log n\) with any different integer \(n\ge2\) vanish: each bump is narrower than the spacing in \(\log n\), while the self-support diameters are much smaller than \(\log2\). In particular, the entire \(8\)-power ladder vanishes. Let \(J=\|\phi\|_2^2>0\). Then
\[
 C_f(\log p)=J,\quad P(f)=E_5(f)=2\frac{\log p}{\sqrt p}J,
 \quad \|f\|_2^2=2J.
\]
Therefore
\[
 \boxed{\ell_5\ge\frac{\log4099}{\sqrt{4099}}\approx0.12992896356.}
\]
This already exceeds the **sufficient** uniform-leakage thresholds \(0.0061353\ldots\) for the \(1/3\) margin and \(0.0894686\ldots\) for the \(1/4\) margin in UOI040. It **does not** mean the actual full signed form fails either margin: the UOI040 estimate is one-sided and conservative.

## 2. General two-collar construction: an exact positive Rayleigh value equal to an \(\ell^2\) norm of prime weights

Fix \(\eta_0=1/4000\) (distinct from the bump \(\eta\)). For every integer \(d\ge1\) put \(N=8^d\), and choose the finite set of **ordinary primes**
\[
 \mathcal P_d=\{p\ \text{prime}:Ne^{-\eta_0}\le p\le Ne^{\eta_0}\}.
\]
Assume it is nonempty, as it will be for all sufficiently large \(d\) by PNT. Each
\(s_p=\log p\) satisfies \(|s_p-\log N|\le\eta_0<\delta_0/2\).

Choose \(w_d>0\) so small that
\[
 w_d<\delta_d/8,
 \qquad 4w_d<\min_{\substack{p\in\mathcal P_d\\ n\in\mathbb N,\ n\neq p}}
 |\log n-\log p|,
\]
where the minimum only needs to be taken over integers in a bounded neighborhood of \(N\); separation is positive because integers are discrete. For example \(w_d=1/(10000N)\) works for all sufficiently large \(d\) (the relevant integers lie in a fixed small multiplicative interval about \(N\)).

Choose a nonzero \(\phi_d=(\partial_x)(\partial_x^2-\tfrac14)\eta_d\) with \(\eta_d\in C_c^\infty((c_d-w_d,c_d+w_d))\), and define the translates \(g_p(x)=\phi_d(x+\log p)\). Each \(g_p\) lies in the first collar \(I_0\) and obeys its three local zero moments. Distinct \(g_p\) have disjoint supports because distinct integer logarithms differ much more than \(2w_d\).

Write
\[
 \kappa_p=\frac{\log p}{\sqrt p},\quad
 S_d=\left(\sum_{p\in\mathcal P_d}\kappa_p^2\right)^{1/2},\quad
 f_d=\phi_d+\sum_{p\in\mathcal P_d}\frac{\kappa_p}{S_d}\,g_p.
\]
All terms are smooth, compactly supported, and lie only in \(I_d\cup I_0\). The local moments vanish separately. The supports of \(\phi_d\) and the various \(g_p\) are mutually disjoint, giving
\[
 \|f_d\|_2^2=2\|\phi_d\|_2^2.
\]
For the **full** original prime form, the only nonzero positive-shift prime-power correlations occur at \(n=p\in\mathcal P_d\), with
\[
 C_{f_d}(\log p)=\frac{\kappa_p}{S_d}\|\phi_d\|_2^2.
\]
Every other integer (including every ladder \(8^k\)) misses the supports, and internal autocorrelations are too short to be sampled at \(\log n\ge\log2\). Therefore
\[
 E_{d+1}(f_d)=P(f_d)=2S_d\|\phi_d\|_2^2,
 \qquad
 \boxed{\ell_{d+1}\ge S_d=\left(\sum_{p\in\mathcal P_d}\frac{(\log p)^2}{p}\right)^{1/2}.}
\]
This is an **exact** Rayleigh construction on the three-moment kernel, not a generic operator-norm estimate on unconstrained tests. No arithmetic phase or source-normalization assumption is hidden.

## 3. PNT proves \(\sup_m\ell_m=\infty\)

The classical Prime Number Theorem and partial summation give, for every fixed \(\eta_0>0\),
\[
 \sum_{Ne^{-\eta_0}\le p\le Ne^{\eta_0}}\frac{(\log p)^2}{p}
 =\int_{Ne^{-\eta_0}}^{Ne^{\eta_0}}\frac{\log t}{t}\,dt+o(\log N)
 =2\eta_0\log N+o(\log N),\qquad N\to\infty.
\]
Applying this along \(N=8^d\) gives
\[
 \boxed{\ell_{d+1}\ge\sqrt{2\eta_0\,d\log8+o(d)}
 \longrightarrow\infty,\qquad\eta_0=1/4000.}
\]
Consequently
\[
 \boxed{\sup_{m\ge2}\ell_m=+\infty.}
\]
The \(\ell_m\) are also nondecreasing: zero extension from \(K_m\) to \(K_{m+1}\) preserves \(P\), \(P_8\), and the norm, so the Rayleigh supremum cannot decrease.

**Interpretation:** UOI040's proposed sufficient condition \(\sup_m\ell_m<0.3394686424\ldots\) is **false for this specific nested family**, not simply unproved. The proof invokes PNT, which is an established theorem of analytic number theory; this instance has **not** been reduced to a Lean kernel proof in Weil-Lab.

## 4. Why this is not a disproof of the full Weil positivity objective

The signed original literal form is \(W_{\mathrm{lit}}=\Gamma-P+\operatorname{Re}Q\). Our witnesses lie in the pole radical, so \(Q=0\), but the earlier Gamma estimate \(\Gamma\ge1.0998625\|f\|_2^2\) is **only a floor**. For the witness \(f_d\), the narrowest physical structures have width \(w_d\asymp8^{-d}\). Their Fourier energy spreads to frequencies on the order of \(w_d^{-1}\), where the genuine Gamma multiplier grows logarithmically. It is therefore **not valid** to deduce negativity of \(W_{\mathrm{lit}}\) from \(E(f_d)/\|f_d\|_2^2\to\infty\). The actual Gamma energy may grow and compensate.

Equally importantly, unbounded leakage does not show that the original explicit formula, its zero-side representation, or the proposed source/native dictionary is wrong. It only invalidates the unweighted **uniform additive leakage budget** on UOI040's particular family.

## 5. Mathematical next step: use relative form control instead of a constant leakage cap

The correct next question is whether the **full** off-ladder form is bounded relative to the real signed Gamma quadratic form (or to a comparable logarithmic Fourier-energy form), with constants independent of \(m\):
\[
 E_m(f)\le\theta\,\Gamma(f)+C\|f\|_2^2,\qquad
 f\in K_m\cap C_c^\infty(D_m),
\]
where \(\theta<1\) and \(C\) must be sufficiently small **in combination with** the surviving ladder budget to imply a positive margin. This is a **candidate estimate**, not established here. Alternatively, investigate a scale-sensitive collar-dependent capacity norm that directly pays for the very narrow prime-resonant packets.

To prove full-form positivity on the nested union, one must additionally establish source-level arbitrary-support equality of the literal expression (including exact signs, \(2\pi\) normalization, and both poles), not merely apply the older fixed-collar Lean result.

### Certification ledger

- **UOI041:** exact analytic construction and PNT argument; no Lean acceptance or CI submission.
- **NF:** independent original HD/A gate count unaffected by this analysis.
- **No claim:** global Weil positivity, RH, or an independent spectral-equivalence theorem.