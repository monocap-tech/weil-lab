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
