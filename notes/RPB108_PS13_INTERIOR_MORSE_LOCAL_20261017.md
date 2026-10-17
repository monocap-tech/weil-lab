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

## An explicit finite negative-index bound for the WHOLE original form

PS11's true sign-aware original-source comparison gives \(Q[f]\ge J[f]-13\|f\|^2\) on the entire original domain. The full arch Fourier multiplier is
\[
j(\xi)=2\int_0^\infty k(u)(1-\cos(2\pi\xi u))du
\ge\log(|\xi|/2)-1/\pi-1/2,\quad |\xi|\ge2.
\]
Choose the physical frequency cutoff \(\Lambda=2^{22}\). Source-rational \(\log2>693/1000\) and \(\pi>3\) give
\[
j(\xi)>L_*=\frac{41159}{3000}>13\qquad(|\xi|\ge\Lambda).
\]
Thus every \(f\) with \(Q[f]\le0\) obeys the necessary Fourier concentration inequality
\[
\int_{|\xi|\le\Lambda}|\widehat{Zf}(\xi)|^2d\xi
\ge(1-13/L_*)\|f\|^2.
\]
For ANY linear subspace \(V\) of the original physical form domain on which \(Q[f]\le0\) for every \(f\in V\), choose an arbitrary finite \(L^2\)-orthonormal family \(f_1,\ldots,f_d\). Bessel applied to the exponential \(x\mapsto e^{2\pi i\xi x}\) restricted to I yields
\[
\sum_{j=1}^d|\widehat{Zf_j}(\xi)|^2\le |I|=11/5 .
\]
Integrate over the frequency band and compare with the preceding necessary mass bound:
\[
\boxed{d<\frac{2(11/5)2^{22}}{1-13/(41159/3000)}<352{,}000{,}000.}
\]
This gives a conservative **finite negative Morse-index upper bound** for the complete original signed physical form, and hence for any nonpositive subspace contained in the PS12 beta-localized range. The full physical form has compact resolvent by PS05/PS07's original log-energy compact embedding and bounded signed prime/pole perturbations. This is NOT a computed negative eigenvalue count and asserts neither existence nor absence of negative eigenvalues.

## Custody and next obligation

The single-window theorem and the finite-index bound make progress toward identifying the remaining **coherent multi-window low-energy** interior obstruction. They do not prove \(Q[\beta f]\ge0\) on its entire range. Both parities, the cross-window signed form, complete CC27 D-Riesz domain attachment, a verified full signed Schur positive margin, and RH stay OPEN.

**PS14** should build a rigorous original low-energy coupled interior/edge Gram or Schur certificate that retains all original seven prime shifts, archimedean interactions and both signed poles. Do not promote the positive shifted PS12 frame to unshifted Weil positivity.

Replay: \`python3 scripts/validate_rpb108_ps13_interior_morse_local.py\` reruns the source-pinned PS12→PS11→PS10→PS09→PS07→PS06→PS03→RC315 chain, checks the rational Bernoulli tail and strict \(\frac14\) margin, and checks the exact-rational Fourier Bessel dimension bound and W-ODD-NEG custody. Focused CI is not independent proof-level review.
