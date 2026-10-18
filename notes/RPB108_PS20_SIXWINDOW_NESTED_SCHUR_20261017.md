# PS20 — Six physical windows and nested signed Schur

Scoped original physically supported Weil form investigation, stacked on PS19. Canonical W-ODD-NEG, W-EVEN-FORM, CC27 D-Riesz carrier, full Weil positivity, and RH remain OPEN.

This theorem has two parts: a six-window source-eliminated complementary positivity bound, and an exact second-level Schur decomposition against the uncovered original physical complement. This does NOT prove positivity of that residual complement.

## I. A coupled six-window module for the true ORIGINAL signed Schur form

Write \(B=11/10\), \(w=1/128\), \(J=[1/32,5/128]\), \(V=[1/6,1/6+w]\), \(\ell_2=\log2\). The six physical intervals are
\[
\mathcal W=(-J-\ell_2)\cup(-V)\cup(-J)\cup J\cup V\cup(J+\ell_2).
\]
They are disjoint, contained in PS15's source complement \(C\), and invariant under reflection. They contain all four PS19 windows and two new reflected intervals. The nonlocal digamma interaction between the old and new windows is **included**, not assumed zero.

The unchanged original signed form on \(I=[-B,B]\) is
\[
Q[f]=J_{\rm arch}[f]+c_{\rm arch}\|f\|^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)
+2|\langle f,\cosh(x/2)\rangle|^2-2|\langle f,\sinh(x/2)\rangle|^2,
\]
where \(J_{\rm arch}[f]=\int_0^\infty e^{-u/2}(1-e^{-2u})^{-1}\|Zf-\tau_u Zf\|^2du\) and \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\). All terms are zero-extended on the physical real line. PS15's Carleman-plus-truncated-kernel argument guarantees the sharp six-interval restrictions preserve the SAME logarithmic form domain.

The exact source labels remain PS10's thirteen actual intervals \(I_r=[-B+\log r,-B+\log r+\delta]\), \(r\in\{1,9,2,3,4,5,7,8,9/2,9/4,9/5,9/7,9/8\}\), \(\delta=2B-\log9\). The rational validator checks all **1092** signed source/window shifts \(6\cdot13\cdot7\cdot2\): NONE of the original seven prime powers connects any source interval to these six windows. This is only the **source–six-window cross**, not a claim that primes disappear on the remainder of the original domain.

The original signed prime interaction INTERNAL to the six-window carrier contains exactly TWO nonzero physical \(\log2\) links, from \(-J-\ell_2\) to \(-J\), and from \(J\) to \(J+\ell_2\). The exact original prime norm on the six-window compression is \(\log2/\sqrt2<1/2\). All five other prime powers are excluded by genuine physical translation geometry.

For EACH form-admissible component on one width-\(1/128\) window, the original 64-term Bernoulli integrated digamma tail gives
\[
J_{\rm arch}[h_i]+c_{\rm arch}\|h_i\|^2>\frac{11}{5}\|h_i\|^2.
\]
All **15 original archimedean cross-window kernels** are retained and their symmetric operator row bound is \(<17/100\). The true original negative odd pole on the entire six-window support costs \(<1/30\) mass; the positive even pole is safely dropped only in the lower estimate.

The original complete source/six-window mixed arch kernel has Hilbert–Schmidt norm \(<4/25\), from all **78 nonzero source/window** distance terms. Both correctly signed original rank-one source/window poles contribute norm \(<3/20\). All actual source/window prime terms were *separately certified zero* by the 1092 tests. Thus
\[
\|B_{P,\mathcal W}\|<\frac4{25}+\frac3{20}=\frac{31}{100}.
\]
The TRUE PS16 source operator \(A_P>323/1000\), including 19 original internal source prime couplings, therefore gives the complete signed source Schur subtraction
\[
\langle h,T_C h\rangle
=\langle B_{PC}h,A_P^{-1}B_{PC}h\rangle
<\frac{(31/100)^2}{323/1000}\|h\|^2<\frac3{10}\|h\|^2 .
\]
For **every nonzero form-admissible six-window vector**, not just piecewise constant tests,
\[
\boxed{
\mathfrak S_C[h]
> \left(\frac{11}{5}-\frac{17}{100}-\frac12-\frac1{30}-\frac3{10}\right)\|h\|^2
=\frac{359}{300}\|h\|^2>\frac76\|h\|^2.
}
\]
The six-window carrier is infinite-dimensional and reflection-invariant. This is genuine original **unshifted source-eliminated Schur positivity** on an *enlarged connected-by-arch and connected-by-prime* module, valid in both parities. It does NOT imply a comparable global Schur gap; the RC315 even low mode precludes a global lower gap larger than 0.041.

## II. The exact original signed Schur AFTER eliminating all six windows

Inside the original PS15 source complement \(C\), denote the just-proved-positive six-window carrier by \(W=L^2(\mathcal W)\) and the **actual uncovered complement** by \(R_*=L^2(C\setminus\mathcal W)\). The PS15 truncated-kernel/Carleman sharp projector proof applies to **each of these six real interfaces**; hence the full original physical form domain splits as
\[
\mathcal D_C=(\mathcal D_C\cap W)\oplus(\mathcal D_C\cap R_*).
\]
The already source-eliminated signed Schur form is \(\mathfrak S_C=Q_C-T_C\). Let \(A_W\) be its restricted strictly positive self-adjoint operator on \(W\); Part I proves \(A_W>7/6\). Its inverse is compact by original physical logarithmic Fourier-energy compact embedding and bounded perturbations, including the original compact source response \(T_C\).

The WHOLE true \(W/R_*\) mixed operator of this **source-eliminated** Schur is
\[
\widetilde B=B^{Q}_{W,R_*}-1_W T_C1_{R_*}.
\]
The FIRST term retains every original nonlocal digamma W/rest interaction, all seven physical W/rest prime translations and the TWO signed poles; the SECOND retains the complete compact thirteen-source-mediated interaction. Neither is discarded.

Source-rational conservative operator envelopes:
\[
\begin{aligned}
\|B^{Q}_{W,R_*;\rm arch}\|&<6
&&\text{(six two-sided Carleman outputs)},\\
\|B^{Q}_{W,R_*;\rm prime}\|&<71/10
&&\text{(all seven genuine prime powers)},\\
\|B^{Q}_{W,R_*;\rm poles}\|&<1
&&\text{(both original signed poles)},\\
\|1_W T_C1_{R_*}\|
&\le\|B_{P,W}\|\|A_P^{-1}\|\|B_{P,R_*}\|\\
&<\frac{31}{100}\frac{1000}{323}\frac{67}{4}<17.
\end{aligned}
\]
Thus \(\|\widetilde B\|<311/10<32\). The original physical W/rest arch output bound uses the same genuine \(1/(2(s+t))\) interface singularity and regular tail as PS15.

**Crucially this is NOT compact in physical \(L^2\).** Choose normalized adjacent \(\epsilon\)-step indicators on opposing sides of one window/rest internal boundary. They converge weakly to zero. Their *original* arch mixed form tends to \(-\log2\); all seven genuine prime shift correlations vanish if \(2\epsilon<\log2\), and both signed pole terms are \(O(\epsilon)\). Because \(T_C\) is compact on \(L^2(C)\), its matrix element on this weakly-null sequence tends to zero. Therefore
\[
\boxed{\|\widetilde B\|_{\rm essential}\ge\log2>0.69.}
\]
One cannot approximate the raw original coupling in unweighted physical operator norm by arbitrarily accurate finite-rank matrices.

However the **nested positive energy-dual penalty** is compact:
\[
\boxed{T_{R_*}^{(2)}
=\widetilde B^* A_W^{-1}\widetilde B\ge0,\quad
\text{compact},\quad
\|T_{R_*}^{(2)}\|
<\frac{32^2}{7/6}=\frac{6144}{7}<878.}
\]
The upper bound is too large to imply residual positivity. The complete **correct signed residual** is
\[
\boxed{
\mathfrak S_{R_*}[r]
=\mathfrak S_C[r]-\langle r,T_{R_*}^{(2)}r\rangle,
\quad r\in\mathcal D_C\cap R_*.
}
\]
For every original physical \(p\in\mathcal D_P,\ w\in\mathcal D_C\cap W,\ r\in\mathcal D_C\cap R_*\), the EXACT twice-completed-square identity reads
\[
\begin{aligned}
Q[p+w+r]
&=\|A_P^{1/2}(p+A_P^{-1}B_{PC}(w+r))\|^2\\
&\qquad+\|A_W^{1/2}(w+A_W^{-1}\widetilde Br)\|^2
+\mathfrak S_{R_*}[r].
\end{aligned}
\]
All operators refer to the SAME original zero-extended physical form, including full prime, arch and signed pole source. Thus
\[
\boxed{Q\ge0\ \text{on its complete original physical domain}
\iff \mathfrak S_{R_*}\ge0\ \text{on its true uncovered residual domain}.}
\]
**This is an exact equivalence, NOT a certification that the residual has the required sign.**

## III. Consequences and custody

The four-window module of PS19 has been **strictly enlarged** to an interacting six-window module and a TRUE whole-domain second-level Schur now records precisely how it couples to the remainder. This is directly responsive to the main obligation of assessing *cross-module* interactions, rather than collecting isolated positive tests.

The residual contains noncompact digamma seams, genuinely nonzero prime connections, and energy-dual source and six-window penalties. Its sign is open; the conservative penalty bound \(<878\) is far too weak. A new proof needs a sharper source- and six-window-energy estimate, gap-compatible with the RC315 even necessary upper ceiling below 0.041, or a certified negative witness.

**Next PS21:** sharpen the full original energy-dual \(W/R_*\) response, particularly physical seams, and construct a sign-relevant residual low-energy Gram/Feshbach without PS17's exponential spectral enumeration. Independent CC27 D-Riesz norm/domain attachment and external mathematical audit are mandatory before W-ODD-NEG, W-EVEN-FORM or RH promotion.

**Replay:** \`python3 scripts/validate_rpb108_ps20_sixwindow_nested_schur.py\` reruns PS19→...→RC315 true original source; explicitly checks 1092 source/window signed prime-shift configurations, 15 window/window digamma interactions, two genuine \(\log2\) edges, all 78 source/window arch distances, both original signed poles and source energy inverse, conservative W/rest all-prime/Carleman/pole/source coupling, full original form-domain custody and exact Schur minus sign. GitHub Actions validates the rational gates; it is not an independent formal proof of all analytic operator identities.
