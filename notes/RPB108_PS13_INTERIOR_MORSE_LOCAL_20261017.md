# PS13 — Unshifted local form and spectral index

Scoped mathematical investigation. W-ODD-NEG, W-EVEN-FORM, full Weil positivity and RH remain open.

Two targets: certify positivity of the original physical quadratic form on single short-support intervals; certify a finite upper bound on the dimension of a nonpositive subspace by Fourier concentration.

## Exact original signed form and a uniform short-support theorem

On I=[-B,B], B=11/10, let Zf denote zero extension. Use the unchanged SI10/CC27 physical signed seven-prime form
\[
Q[f]=J[f]+c_{\rm arch}\|f\|^2-2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\Re C_f(\log n)
+2|\langle f,\cosh(x/2)\rangle|^2-2|\langle f,\sinh(x/2)\rangle|^2,
\]
where \(J[f]=\int_0^\infty k(u)\|Zf-\tau_u Zf\|^2du\),
\(k(u)=e^{-u/2}/(1-e^{-2u})\), \(w_n=\Lambda(n)/\sqrt n\) and \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\).

**Theorem A:** For EVERY original-form-admissible nonzero \(f\) supported in ANY SINGLE interval of width \(\le L_0=1/16\) inside I,
\[
\boxed{Q[f]>\frac14\|f\|^2.}
\]
This applies in particular to actual beta-localized interior vectors whose RESULTING support lies within such one window; it is not a whole-interior theorem.

Proof: \(L_0<\log2\) kills all seven prime autocorrelations by genuine support separation. For \(u\ge L_0\), the translates do not overlap, so \(J[f]\ge 2\int_{L_0}^\infty k(u)du\cdot\|f\|^2\). The positive even pole can be dropped safely; the true negative odd pole is at worst \(-2L_0\sinh^2(B/2)\|f\|^2\).

Use the original kernel's exact nonnegative expansion \(k(u)=\sum_{m\ge0}e^{-(2m+1/2)u}\). The inequality \(e^{-x}\ge(1-x/32)^{32}\) for \(0\le x\le32\) gives the fully RATIONAL lower:
\[
T_{32}=2\sum_{m=0}^{31}
\frac{(1-(2m+1/2)L_0/32)^{32}}{2m+1/2}>5.68035.
\]
The source-pinned RC315 exact outward rational coefficient replay verifies
\(c_{\rm arch}+T_{32}-2L_0\sinh^2(B/2)>1/4\).
Different windows retain cross-prime and cross-arch couplings, so this theorem **cannot** be summed into global positivity.
