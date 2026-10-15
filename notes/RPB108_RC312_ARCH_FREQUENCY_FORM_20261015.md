# RC312 — independent archimedean frequency-to-form reconstruction and exact Poisson cancellation

**Parent:** RC311 merged at \`887c3c4bd26f4628faad75a3ba4bfc3ecf8ad9c8\`.  
**Original aperture:** \(B=11/10\), full interval length \(R=2B\), Fourier convention \(\widehat f(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx\).  
**Status:** original Weil prime/pole source identification, positivity, signed inverse, 314-Schur, Stage I, F4, RH, Lean remain **OPEN**.

## 1. Two different frequency multipliers share the *same* singular supported form

The two relevant frequency forms are

\[
 L_{\log}:\quad \log |\xi|,\qquad
 L_{\rm arch}:\quad a_{\rm arch}(\xi)
 =\mathop{\mathrm{Re}}\psi(1/4+i\pi\xi)-\log\pi.
\]

For any supported polynomial \(q\) on \([-B,B]\), extended by zero, set \(M=\|q\|_2^2\) and \(C(r)=\mathop{\mathrm{Re}}\langle q,T_rq\rangle\). Since the zero extension has support diameter \(R\), \(C(r)=0\) for \(r\ge R\).

The singular truncated overlap is

\[
 \mathcal S(q)=\int_0^R \frac{M-C(r)}r\,dr.
\]

This integral is finite for supported polynomial inputs, including inputs with jumps at their support endpoints. A purely physical decomposition gives

\[
 \mathcal S(q)
 =\frac12\int_{-B}^B
 \overline{q(x)}\int_{-B}^B
 \frac{q(x)-q(y)}{|x-y|}\,dy\,dx
 +\int_{-B}^B W_B(x)|q(x)|^2dx
\]

where

\[
 W_B(x)=\log 2-\tfrac12\log(1-(x/B)^2).
\]

Indeed the difference-square on the overlap contributes \(\frac14\iint |q(x)-q(y)|^2/|x-y|\,dx\,dy\), while the two lost-support strips contribute \(\frac12\log(R/(B-x))+\frac12\log(R/(B+x))=W_B(x)\). The associated difference operator

\[
 (Jq)(x)=\frac12\int_{-B}^B
 \frac{q(x)-q(y)}{|x-y|}\,dy
\]

obeys \(J P_n=H_nP_n\) for **every** \(n\). One concise proof uses \(JP_0=0\) and the commutator with multiplication \(Xq(t)=tq(t)\):

\[
 [J,X]f(t)=\tfrac12\int_{-1}^1\operatorname{sgn}(t-u)f(u)\,du.
\]

For \(n\ge1\), \(\int_{-1}^tP_n(u)du=(P_{n+1}(t)-P_{n-1}(t))/(2n+1)\), while \(X P_n=(n+1)P_{n+1}/(2n+1)+nP_{n-1}/(2n+1)\). Inductively \([J,X]\) and \(H_{n+1}-H_n=1/(n+1)\) give \(JP_n=H_nP_n\). Thus \(\mathcal S=\langle q,(J+W_B)q\rangle\), an **all-degree** identity on the polynomial form core. This is independent of fitting RC309's endpoint matrix.

### An independent frequency-space derivation of \(\log|\xi|\)

For \(\epsilon>0\), Frullani integration gives

\[
 \int_0^\infty e^{-\epsilon r}\frac{1-\cos(\omega r)}r\,dr
 =\tfrac12\log(1+\omega^2/\epsilon^2),\quad\omega=2\pi\xi.
\]

Integrate against \(|\widehat q|^2\). In physical space the portion \(r>R\) is \(\int_R^\infty e^{-\epsilon r}M\,dr/r\), and

\[
 \lim_{\epsilon\downarrow0}
 \left[\int_R^\infty\frac{e^{-\epsilon r}}r\,dr+\log\epsilon\right]
 =-\gamma-\log R.
\]

Therefore

\[
 \boxed{
 \langle q,L_{\log}q\rangle
 =\mathcal S(q)-[\gamma+\log(2\pi R)]M
 =\langle q,(J+W_B+c_R I)q\rangle
 },
\quad c_R=-\gamma-\log(2\pi R).
\]

The logarithmic Fourier integral is legitimate for zero-extended supported polynomials: their Fourier transform decays at least as \(1/|\xi|\), and \(\log|\xi|\) is locally integrable at zero. The equality extends by polarization to the polynomial form core.

## 2. The original digamma multiplier has *precisely the same constant*

Euler's digamma series gives, with \(a_k=k+1/4\), \(\alpha_k=2k+1/2\), and \(\omega=2\pi\xi\),

\[
 \frac1{a_k}-\frac{a_k}{a_k^2+\omega^2/4}
 =2\left(\frac1{\alpha_k}
 -\frac{\alpha_k}{\alpha_k^2+\omega^2}\right).
\]

The right side is \(2\int_0^\infty e^{-\alpha_k r}(1-\cos\omega r)\,dr\). Every term is nonnegative; monotone convergence sums the geometric kernel

\[
 j(r)=\sum_{k\ge0}e^{-(2k+1/2)r}
 =\frac{e^{-r/2}}{1-e^{-2r}}.
\]

Consequently

\[
 a_{\rm arch}(\xi)=\psi(1/4)-\log\pi
 +2\int_0^\infty j(r)[1-\cos(2\pi\xi r)]\,dr.
\]

Split \(j(r)=1/(2r)+r_{\rm reg}(r)\) for \(0<r<R\). The exact renormalized mass constant is

\[
 c_{\rm arch}=\psi(1/4)-\log\pi+
 \lim_{\epsilon\downarrow0}
 \left[2\int_\epsilon^\infty j(r)\,dr+\log\epsilon\right]-\log R.
\]

With \(z=e^{-\epsilon/2}\),

\[
 2\int_\epsilon^\infty j(r)\,dr
 =2\operatorname{atanh}z+2\arctan z,
\]

so the bracket tends to \(\log4+\pi/2\). The quarter-digamma formula, independently reducible to harmonic progressions and the Leibniz series, is

\[
 \psi(1/4)=-\gamma-\frac\pi2-3\log2.
\]

Combining the constants yields exactly

\[
 \boxed{c_{\rm arch}=-\gamma-\log(2\pi R)=c_R}.
\]

Thus **there is no surviving new contact mass** in the difference of the digamma and logarithmic forms. The regular part contributes only the physical convolution

\[
 K_{\rm reg}q(x)=
 \int_{-B}^B r_{\rm reg}(|x-y|)q(y)\,dy,
\]

giving \(\langle q,L_{\rm arch}q\rangle=\langle q,(J+W_B+c_R I-K_{\rm reg})q\rangle\).

The validator independently regenerates all 193 exact Taylor coefficients of \(r_{\rm reg}\) from two distinct formal power-series divisions, and checks the inherited RC46 coefficient vector **byte-for-byte at the rational level**. Its inherited uniform analytic remainder estimate is retained, not reproved here.

## 3. Exact supported Poisson-remainder cancellation

For \(\xi\neq0\),

\[
 \log(e+|\xi|)
 =\log|\xi|+\underbrace{\log(1+e/|\xi|)}_{m(\xi)}.
\]

The additional supported physical map is

\[
 \mathcal R
 =\chi_{[-B,B]}\mathcal F^{-1}m\mathcal F\chi_{[-B,B]}.
\]

Although \(m\) is unbounded at \(\xi=0\), it is square-integrable on the real line:

\[
 \int_{\mathbb R}m(\xi)^2d\xi
 =\frac{2e\pi^2}{3}.
\]

For a supported input \(|\widehat q(\xi)|\le\sqrt{2B}\|q\|_2\); hence

\[
 \|\mathcal Rq\|_2^2
 \le\frac{4Be\pi^2}{3}\|q\|_2^2.
\]

RC312 certifies a rational bound using \(e<11/4\), \(\pi<22/7\), retaining the supported-input qualifier.

We have independently reconstructed both forms on the dense supported polynomial form core:

\[
 L_{\rm arch}=J+W_B+c_R I-K_{\rm reg},\qquad
 L_{\rm can}=J+W_B+c_R I+\mathcal R.
\]

Subtract:

\[
 \boxed{K_{\rm arch}:=L_{\rm arch}-L_{\rm can}
 =-K_{\rm reg}-\mathcal R.}
\]

In the original Weil assembly \(N_0\), the supported Poisson term \(\mathcal R\) cancels against the corresponding canonical-metric decomposition. This is an exact **form identity**, not a numerical near-cancellation; the surviving original source is the bounded \(K_{\rm reg}\) contribution plus the separate original prime, signed-pole and endpoint pieces. Because \(K_{\rm reg}\) and \(\mathcal R\) are bounded supported operators, their difference extends uniquely from the dense supported polynomial core to physical \(L^2\).

The conclusion uses standard Euler's digamma series, Plancherel, Frullani, monotone/dominated convergence, the Basel identity, and the standard integral for Euler's constant. These are analytic ingredients of the proof, not Lean formalizations.

## 4. Independent original singular-overlap regression

Beyond the all-degree argument, RC312 computes \(\mathcal S(q)\) **without** referring to RC309 or RC311's endpoint coefficients. For a polynomial \(p(t)\), the overlap

\[
 C(Bs)/B=\int_{-1}^{1-s}p(t+s)p(t)\,dt
\]

is an exact rational polynomial in \(0\le s\le2\). The code expands its full monomial polynomial, integrates \([C(0)-C(Bs)]/s\) coefficientwise, and compares that independent rational answer with \(J+W_B\) computed through Legendre harmonic diagonalization and exact logarithmic moments.

The test includes all \(P_0,\ldots,P_{10}\) and signed mixed even and odd inputs. All arithmetic is rational, no floating-point quadrature or sampling of the singular integral.

## 5. Remaining boundary

This genuinely discharges the archimedean frequency-to-form and supported Poisson cancellation identity on the polynomial core, subject to the standard analytic lemmas above. It does **not** by itself independently derive the original Weil explicit-formula prime and signed-pole distributions or certify their normalization for all supported inputs.

The next step is therefore **RC313**, an original prime and pole distributional-source audit that can connect the now independently identified archimedean form with RC310's bounded native original-action model. After such identification, spectral positivity, the signed Chebyshev inverse, the rank-314 Schur gate, Stage I, F4, and RH would remain separate proof obligations.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc312_arch_frequency_form.py --output certificates/rpb108_rc312_arch_frequency_form.json
python scripts/validate_rpb108_rc312_arch_frequency_form.py --output certificates/rpb108_rc312_arch_frequency_form.json --replay
\`\`\`

This checkpoint certifies reproducible mathematical algebra and exact arithmetic under the cited standard analytic results. It is not independent peer review of a complete Riemann Hypothesis proof.
