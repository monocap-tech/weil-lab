# PS33 — True original even ground-pole overlap: optimal dyadic Fourier split and endpoint-precision correction

**W-PHYSICAL-SHIFT · October 18, 2026 · stacked on PS32 draft PR #201.**
Scope: original zero-extended seven-prime, thirteen-source-eliminated **positive-even-pole-free** even Schur \(L=\mathfrak S_C^{(0)}|_{\rm even}\), with original PS28 effective pole \(d\ge1\), true nonnegative normalized ground eigenfunction \(\phi_0\) inherited from PS29, and PS32 genuine original whole-frequency digamma energy bound. This is a **new quantitative optimization** of a true-original-operator spectral coupling, not an independently computed eigenfunction, physical graph-cell \(\mu_i,w_{ij}\), positive \(\lambda_1\), positive pole-angle \(\Delta\), or any signed Weil/RH closure. All infinite-dimensional original PS17–PS32 premises need independent audit.

## 1. Separate two different Fourier goals

PS32 used \(X=2^{8096}\) so that **at least \(3/4\)** of the true normalized original ground-state Fourier mass lies in \((-X,X)\). This is a valid, very coarse nonconcentration result, but an extremely inefficient choice of frequency band for the *different* task of establishing the positive even-pole ground overlap \(a=\langle d,\phi_0\rangle\).

Keep the actual source-eliminated original pole-free even operator
\[
L=J_C+V_{0,C}-B_0^*A_0^{-1}B_0,\quad
T=13+\frac{539}{90}+\frac{(1403/80)^2}{1997/9000},
\]
and true normalized nonnegative ground \(\phi_0\). PS32's source-pinned original analytic bound is
\[
\boxed{J[\phi_0]<M:=T-\frac{4359740}{10^6}<1401.}
\]
Here \(J\) is the **full original zero-extended digamma form**, with all seven original prime/pole/source interactions paid in the original operator bound \(T\).

PS18's original Fourier convention gives
\[
j(\xi)\ge \log(|\xi|/2)-1/\pi-1/2
\quad(|\xi|\ge2).
\]
For every dyadic \(X_e=2^e\), integer \(e\ge 2\), the existing exact lower \(\log2>693/1000,\pi>3\) yields
\[
j(\xi)>s_e:=(e-1)\frac{693}{1000}-\frac56
\qquad(|\xi|\ge X_e).
\]
For every \(e\) with \(s_e>M\), the genuine original Fourier mass satisfies
\[
\int_{|\xi|\ge X_e}|\widehat{Z\phi_0}|^2<\frac{M}{s_e},
\qquad
\int_{|\xi|<X_e}|\widehat{Z\phi_0}|^2>
p_e:=1-\frac{M}{s_e}.
\]
The true original ground \(\phi_0\ge0\), \(\|Z\phi_0\|_2=1\), is compactly supported, so \(|\widehat{Z\phi_0}(\xi)|\le\int_C\phi_0\) and Plancherel give for **every** such dyadic choice
\[
\boxed{
a^2=\langle d,\phi_0\rangle^2
\ge\Big(\int_C\phi_0\Big)^2
>\frac{p_e}{2^{e+1}}.
}
\]
This is a *true original* ground/pole estimate, conditional only on the inherited analytic original source-cone/eigenfunction results, not on pointwise regularity of \(\phi_0\).

## 2. NEW optimized dyadic acceptance

Because \(M\) is a fixed rational and \(s_e\) increases affinely with \(e\), the rational function \(p_e=1-M/s_e\) is increasing and has **strictly decreasing** increments \(p_{e+1}-p_e\) once \(s_e>0\). Exact Fraction comparisons yield:
\[
s_{2023}\le M,\qquad 0<p_{2024},\quad
p_{2025}>2p_{2024},\quad
p_{2026}<2p_{2025}.
\]
For all \(e\ge2025\), decreasing increments and monotonic positivity imply \(p_{e+1}<2p_e\). Therefore
\[
\boxed{
e_*=2025\text{ uniquely maximizes } \frac{p_e}{2^{e+1}}
\text{ among all admissible integer dyadic }e.
}
\]
This is a theorem about the specified PS18 **rational Fourier split bound**, *not* a claimed optimum of every possible Fourier method.

The exact original-source rational calculation additionally establishes
\[
p_{2025}>\frac{3}{4000}.
\]
Consequently the original ground/effective-pole angle obeys the substantially improved, still weak bound
\[
\boxed{
a^2>
\frac{p_{2025}}{2^{2026}}
>
\frac{3}{8000\cdot2^{2025}}.
}
\]
With the **actual source-renormalized** PS28 positive-pole coefficient \(\alpha>3994/2907\),
\[
\boxed{
\alpha a^2>
\frac{3994}{2907}\,
\frac{3}{8000\cdot2^{2025}}.
}
\]
The earlier PS32 overlap lower \(3/(8\cdot2^{8096})\) is beaten by a factor \(2^{6071}/1000>1\). This is a **very large multiplicative improvement of an exponentially small numerical floor**, not progress toward proving \(\Delta=a^2-|\lambda_0|\beta>0\) without original \(\beta\). No restored positive-even-pole Schur inequality has been checked.

## 3. Precision caution: frequency localization and overlap have different optima

At \(X=2^{2025}\), the certified original low Fourier fraction is only \(p_{2025}\approx 0.000751\), not \(3/4\). The optimized **overlap** result **does not replace** PS32's \(X=2^{8096}\) Fourier-tail \(<1/4\) or its true tiny-physical-set nonconcentration certificate. In particular the new \(X\) gives no useful positive **macroscopic-cell mass** lower for the original PS31 graph.

The PS31 even-sector one-negative-index \(\lambda_1\ge0\), original physical bin weights, coherent pole \(d\)-orthogonal \(\beta\) and \(\Delta\) remain the real bottlenecks. The quick optimization identifies that *larger Fourier cutoffs are not automatically better*: choose the scale to match the actual acceptance objective.

## 4. Additional method audit

A bound on only the logarithmic Fourier energy \(J[\phi_0]<1401\) generally cannot imply an \(L^\infty\) bound on all admissible normalized functions: already one may build normalized smooth bumps on physical intervals of length \(\varepsilon>0\) with peak \(O(\varepsilon^{-1/2})\) and finite original digamma energy \(O(1+\log(1/\varepsilon))\), growing as \(\varepsilon\to0\). This does **not** rule out boundedness or Harnack estimates for the **specific true original ground eigenfunction**, which solves a more constrained equation, but it invalidates any inference of global physical \(L^\infty\) solely from "finite log-form energy." Proving a useful uniform bound from the fixed *numerical* budget \(1401\), rather than arbitrary finite energy, also needs separate analysis.

**PS34:** recover a **macroscopic** lower/upper ground-state profile by using the original eigenfunction equation, positivity-improving source resolvent, genuine all-frequency nonlocal kernel (including the integrable source-mediated Schur interactions), or a direct ground-independent proof that the original even pole-free Schur has only one negative eigenvalue. Do not pretend PS33's optimized exponentially small pole overlap controls original \(\beta,\Delta\), the PS31 graph, or even positivity.

**Custody:** Explicit PS-scoped NFQ continuation; canonical active obligation W-ODD-NEG unchanged. True original \(\lambda_1\), pole-angle \(\Delta\), W-EVEN-FORM, W-ODD-NEG, native CC27 D-Riesz, complete original signed Weil positivity and RH are all OPEN.

Replay: \`python3 scripts/validate_rpb108_ps33_optimized_original_ground_pole_overlap.py\`.
