# PS19 — Genuine original complementary Schur positivity on four coupled, parity-stable windows

**W-PHYSICAL-SHIFT · Stacked after PS18 · Canonical W-ODD-NEG OPEN.** The original complete signed SI10/CC27 physical Weil form is unchanged. This is a mathematically explicit **infinite-dimensional strict positivity theorem for the true *source-eliminated* complementary Schur form on FOUR coupled physical windows**, including **two genuine nonzero \(\log2\) original prime translations**. Both even and odd subspaces are covered. It is **not** whole complementary Schur PSD, full Weil positivity, CC27 D-Riesz attachment or RH.

## 1. The exact reflection-invariant four-window original complement

Let \(B=11/10\), \(I=[-B,B]\), \(w=1/128\), \(J=[1/32,5/128]\), \(\ell_2=\log2\). Define four **actual disjoint physical intervals**
\[
W_1=-J-\ell_2,\quad W_2=-J,\quad
W_3=J,\quad W_4=J+\ell_2.
\]
Each has width \(w\); reflection swaps \(W_1\leftrightarrow W_4\) and \(W_2\leftrightarrow W_3\). The union \(W\) is an infinite-dimensional \(L^2(W)\) source-complement carrier.

The positive original source \(P\) remains PS15's exact 13-interval carrier \(I_r=[-B+\log r,-B+\log r+\delta]\), \(\delta=2B-\log9\), \(r\in\{1,9,2,3,4,5,7,8,9/2,9/4,9/5,9/7,9/8\}\). The strict original rational interval checker establishes that all four \(W_i\) lie in its complement \(C\), with a strictly positive source-support gap.

**Complete signed source-prime check:** for every \(i=1,\ldots,4\), all thirteen \(r\), all seven genuine original \(n=2,3,4,5,7,8,9\), and both signs,
\[
(W_i\pm\log n)\cap I_r=\varnothing .
\]
Every one of the **728 source/window/shift pairs** has exact outward rational positive clearance. Hence the **entire true original source-to-W prime cross** vanishes: \(PB_{\rm prime}1_W=0\). This does **not** remove prime interactions within \(W\) or elsewhere in the original complement.

Inside \(W\), the **only** original prime connections are the exact
\[
W_1+\log2=W_2,\qquad W_3+\log2=W_4.
\]
Thus there are **two genuine \(\Lambda(2)/\sqrt2=\log2/\sqrt2\) signed prime couplings**, each a full translation of an infinite-dimensional fiber. Their full original prime operator is unitarily a direct sum of two \(2\times2\) matrices with offdiagonal \(-w_2\), so
\[
\boxed{\|V_{\rm prime}|_{L^2(W)}\|=w_2=\frac{\log2}{\sqrt2}<\frac12.}
\]
All remaining n=3,4,5,7,8,9 internal edges are excluded by the exact physical shift enclosures—not assumed zero by truncation.

## 2. True form-domain compatibility of window decomposition

Let \(\mathcal D=\{f\in L^2(I):J[f]<\infty\}\), where \(J\) is the actual original digamma translation-difference energy. Indicators of any finite interval \(W_i\) are bounded multipliers on this logarithmic form domain. As in PS15, truncate \(k\) to \(k_M=\min(k,M)\). The mixed interval/complement operator is a two-sided Carleman \(1/(2(s+t))\) singularity plus a bounded regular kernel:
\[
\|1_{W_i}B_{\rm arch}(1-1_{W_i})\|
\le\frac{\pi}{\sqrt2}+\sqrt{w(2B)}
<\frac{5}{2}.
\]
Expanding \(J_M[f]\), using the uniform mixed bound, then applying monotone convergence proves both \(1_{W_i}f,(1-1_{W_i})f\in\mathcal D\) whenever \(f\in\mathcal D\). The full lower-order original signed prime/pole perturbations are \(L^2\)-bounded, so they do not change the domain.

Accordingly, for **every** original-form-admissible \(h\) supported on the union \(W\), its four separate physical components \(h_i=1_{W_i}h\) are individually form-admissible. All subsequent estimates are for **arbitrary complex-valued components**, not step test functions.

## 3. Original unshifted diagonal plus genuine inter-window signed couplings

The original physical signed form is
\[
Q[f]=J[f]+c_{\rm arch}\|f\|_2^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\Re C_f(\log n)
+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2,
\]
with \(k(u)=e^{-u/2}/(1-e^{-2u})\), \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\), \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\). Both original pole signs and all seven genuine prime powers remain.

For each arbitrary channel \(h_i\) with support width \(w=1/128\), disjoint translates at \(u\ge w\) yield
\[
J[h_i]\ge2\int_w^\infty k(u)du\,\|h_i\|^2.
\]
Use the source-exact nonnegative expansion \(k(u)=\sum_{m=0}^\infty e^{-(2m+1/2)u}\). Bernoulli's fully rational bound gives
\[
T_{64}=2\sum_{m=0}^{63}\frac{[1-(2m+1/2)w/32]^{32}}{2m+1/2},
\qquad
\boxed{T_{64}+c_{\rm arch}>\frac{11}{5}.}
\]
Thus the entire original diagonal arch-plus-scalar contribution is \(>11/5\) times mass for the **four-component sum**.

Cross-window archimedean contributions are NOT zero. The true original cross kernel is \(-k(|x-y|)\); for separated \(W_i,W_j\) with minimum separation \(d_{ij}>0\),
\[
\|1_{W_i}B_{\rm arch}1_{W_j}\|
\le w\left(1+\frac{1}{2d_{ij}}\right).
\]
All six actual pairs are checked. The full weighted symmetric row sum is
\[
\boxed{\|B_{\rm arch,cross}|_{L^2(W)}\|<\frac1{10}.}
\]
The original even pole is nonnegative and dropped only when taking a **safe lower bound**. The full original negative odd pole is globally bounded on the whole \(W\) by
\[
-2|\langle h,s\rangle|^2
\ge-2(4w)\sinh^2(B/2)\|h\|^2
>-\frac1{40}\|h\|^2.
\]
Combining the true direct n=2 internal signed prime shift (norm <1/2), all inter-window arch interactions (<1/10), and both true pole signs,
\[
\boxed{
Q[h]>\left(\frac{11}{5}-\frac12-\frac1{10}-\frac1{40}\right)\|h\|^2
=\frac{63}{40}\|h\|^2
\qquad(\operatorname{supp}h\subset W).
}
\]

## 4. Complete source-to-W arch/pole and actual energy-dual Schur subtraction

Although all 728 prime source-window cross terms vanish, the source-to-W nonlocal archimedean and both pole couplings are **retained and paid**. For each source interval \(I_r\), each \(W_i\), let \(d_{ri}=\operatorname{dist}(I_r,W_i)>0\). The complete original physical signed arch cross is Hilbert–Schmidt on these separated supports:
\[
\|P B_{\rm arch}1_W\|_{\rm HS}^2
\le\delta w\sum_{r=1}^{13}\sum_{i=1}^4
\left(1+\frac1{2d_{ri}}\right)^2
<\frac1{49},
\]
hence \(\|P B_{\rm arch}1_W\|<1/7\).

For the **same correctly signed original** even and odd rank-one source-cross operators, use \(\sqrt{13\delta}<1/5\), \(\sqrt{|W|}=\sqrt{1/32}<9/50\), \(\sup_I c<7/6\), \(\sup_I|s|<7/12\). Consequently
\[
\|P B_{\rm pole}1_W\|
\le2\sqrt{13\delta}\sqrt{|W|}
\left(\frac{49}{36}+\frac{49}{144}\right)
<\frac{49}{400}<\frac18.
\]
Thus **the full original signed** source-to-W cross satisfies
\[
\boxed{\|B_{PC}1_W\|<\frac17+\frac18=\frac{15}{56}<0.27.}
\]
No source-to-W prime contribution remains, by the **exact 728-case geometry check** above.

The genuine source operator from PS16 satisfies \(A_P>\frac{323}{1000}I\), including all 19 original internal source prime edges. Accordingly the **complete source-eliminated signed Schur penalty**
\[
T_C=B_{PC}^*A_P^{-1}B_{PC}\ge0
\]
has on \(W\) the rigorous upper
\[
\boxed{
\langle h,T_Ch\rangle
<\frac{(15/56)^2}{323/1000}\|h\|^2
<\frac9{40}\|h\|^2.
}
\]
This uses the **true original source inverse** by its accepted coercivity, not a diagonal approximation or an assumption of source invariance.

## 5. Main result: a coupled, parity-invariant, infinite-dimensional ORIGINAL Schur-positive module

For **every nonzero original-form-admissible \(h\) supported on all four windows**, the actual original signed complementary Schur is
\[
\boxed{
\begin{aligned}
\mathfrak S_C[h]
&=Q_C[h]-\langle h,T_Ch\rangle\\
&>\left(\frac{11}{5}-\frac12-\frac1{10}
-\frac1{40}-\frac9{40}\right)\|h\|^2\\
&=\boxed{\frac{27}{20}\|h\|^2}
>\frac43\|h\|^2.
\end{aligned}
}
\]
This is a **substantive strict unshifted full source-eliminated Schur positivity result with genuine signed \(\log2\) prime coupling**, all six nonlocal cross-window arch interactions, both signed poles, and the complete 13-source inverse response. Its admissible support space is infinite-dimensional and invariant under reflection, so the same strict lower applies to its **even and odd parity sectors**.

**Boundary:** this is **not** \(\mathfrak S_C\ge0\) on the whole PS15 complement. Actual cross couplings to functions outside \(W\) remain, and no complete original Weil positivity, CC27 D-Riesz transfer, W-ODD-NEG, W-EVEN-FORM or RH is claimed. Nor is the margin \(27/20\) a candidate *global* margin: RC315 already restricts any possible global positive even Schur margin below \(0.041\).

## 6. Next acceptance obligation

**PS20:** continue constructing a *coherent gap-certified complementary partition* using positive modules of this kind. The next barrier is not the two \(\log2\) edges within \(W\), but **nonlocal coupling of \(W\) to its remaining complement**, including additional genuine prime translations, 24 original source Carleman seams and signed pole effects. A valid whole-domain PSD certificate must provide an accepted positive complement-after-elimination sign or a genuine negative witness. Independent CC27 D-Riesz norm/domain audit remains mandatory.

**Replay:** \`python3 scripts/validate_rpb108_ps19_coupled_quiet_fourblock.py\`. It replays PS18→PS17→...→RC315 source pins; checks all 728 original source-window prime configurations, all six inter-window arch pairs, exact two original log2 resonance edges, 64-term original arch tail, whole-window signed odd pole, full 52-pair source arch HS and both rank-one poles, true energy-dual Schur penalty, reflection and canonical no-RH-promotion custody. All infinite-dimensional form claims are analytic and still require independent proof-level review.
