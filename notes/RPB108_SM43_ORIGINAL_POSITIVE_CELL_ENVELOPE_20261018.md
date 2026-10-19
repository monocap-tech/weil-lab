# SM43 — True-original positive low-frequency rational cell envelope and complete 25-source Loewner error

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM42 #224 (final-head focused CI SUCCESS).**

## What is and is not certified

SM41 established a true-original full HIGH positive digamma/seven-prime Fourier logarithmic tail on the selected 25 genuine SI10 odd source functions, while SM42 certified the exact original whole 25×25 physically supported source Gram (including every sin/xcos/pole cross), its true pole norm and a **coarse** original LOW multiplier Loewner sandwich. The numerically stable Gauss8/Gauss16 original LOW weighted source matrix is **not interval enclosed**. The next step is to build a mathematically valid, source-aware, **mesh-refinable low-frequency error enclosure** instead of promoting two agreeing floating quadratures.

**SM43 delivers a scoped, rigorous entire-source-matrix error for the UNION of original 25-source-centered physical frequency windows and [0,1], NOT the entire [0,4096] low band.** It does not rigorously evaluate the cell source Fourier-Gram integrals, so it remains a *certified reduction to piecewise weighted cell Gram integrals*, not a finished stiffness certificate. All original W-ODD-NEG O1/O2 and RH acceptance still OPEN.

## 1. Two-sided whole-real original positive multiplier intervals, including crossings

The original actual signed multiplier and true pole-free positive scalar are
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi-
2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\log p(n)}{\sqrt n}\cos(2\pi\xi\log n),
\qquad a_o(\xi)=\max(\kappa,m(\xi)),\quad\kappa=\tfrac1{1000}.
\]

Let \(I=[a,b]\subset[0,4096]\) be any true original real frequency interval; \(h=b-a>0\). The genuine digamma archimedean real contribution is increasing on \(\xi\ge0\), by its convergent positive-series representation. Hence the existing exact SM39 rational left-bound \(\mathcal A_{\rm lo}(a)\) is a whole-real lower. For a whole-real upper, use the **same genuine digamma series** and, for \(y=\pi_{\rm up}b\), its positive first \(K=64\) terms plus the full decreasing-series integral from \(K-1\):
\[
\mathcal A_{\rm up}(b)=
\sum_{k=0}^{63}\frac{y^2}{(k+1/4)((k+1/4)^2+y^2)}
+\frac12\log_{\rm up}\!\left(1+
\frac{y^2}{(K-1+1/4)^2}\right)
-C_{\rm lo}.
\]
The exact original SI06 constant lower
\[
C_{\rm lo}<
\gamma+\frac{\pi}{2}+3\log2+\log\pi,
\quad C_{\rm lo}=\frac{57}{100}+
\frac{\pi_{\rm lo}}2+3(\log2)_{\rm lo}
+(\log\pi_{\rm lo})_{\rm lo}
\]
is justified by SI06's rational harmonic lower \(\gamma>57/100\), while all logs are SI06 exact rational outward enclosure. We deliberately round \(\mathcal A_{\rm up}\) further **upward** to \(10^{-10}\) and the constant **downward** to \(10^{-10}\); the proof remains outward even though the intermediate exact fractions have large denominators.

For the original genuine **all-seven-prime** component \(p\), use both independently certified SI06 and SM40 full-real interval enclosures. Let \(x=(a+b)/2\). With original SI06 \(M=69\), true all-seven-prime curvature bound \(D_2\) from SM40, and SI06 rational \(p_{\rm lo/up}(t)\) at endpoints/midpoint:
\[
\begin{aligned}
p_I^-&=\max\Big(
 p_{\rm lo}(x)-Mh/2,\quad
 \min[p_{\rm lo}(a),p_{\rm lo}(b)]-D_2h^2/8\Big),\\
p_I^+&=\min\Big(
 p_{\rm up}(x)+Mh/2,\quad
 \max[p_{\rm up}(a),p_{\rm up}(b)]+D_2h^2/8\Big).
\end{aligned}
\]
These are legitimate whole-real original seven-prime bounds, and intersection tightens them without discarding any original cross. Thus for EVERY true real \(\xi\in[a,b]\):
\[
\boxed{
\ell_I=\max(\kappa,\mathcal A_{\rm lo}(a)+p_I^-)
\le a_o(\xi)\le
u_I=\max(\kappa,\mathcal A_{\rm up}(b)+p_I^+).
}
\]
The \(\max(\kappa,\cdot)\) operator is monotone, so this is valid across **every unsolved nonsmooth crossing \(m=\kappa\)**. No step relies on a sampled crossing count or Gauss node.

## 2. A genuine, COMPLETE 25×25 original source-form Loewner mesh error

For each actual source \(g_j\) from the original 25 selected physically supported SI10 odd sine/k1 xcos/sinh pole directions, its physical sine transform
\[
T_j(\xi)=\int_{-B}^{B}g_j(x)\sin(2\pi\xi x)\,dx,\quad B=11/10
\]
is precisely the SM38 analytic supported source formula. For any complete real frequency cell \(I\) and any \(\xi\in I\), certify a **nonnegative rational upper** \(|T_j(\xi)|\le s_{j,I}\) using:
- \(|\operatorname{sinc}u|\le\min(1,1/(\pi|u|))\), \(\pi>3\), and rational distances of the entire cell from both \(\pm c_j\) (no false disjoint frequency support);
- \(|\operatorname{sinc}'u|\le\min(\pi/2,1/|u|+1/(\pi u^2))\), SI06 \(\pi<22/7\), for each true \(x\cos\) source;
- the exact true odd pole \(\sinh(x/2)\): \(|T_s|\le4(\cosh(B/2)-1)\), and, for \(\xi\ge1\), \(|T_s|\le2/(5\xi)\) from the exact original supported pole transform and SI41 elementary rational bounds.

For a selected union of **pairwise disjoint original frequency cells**, let
\[
C_I=2\int_I T(\xi)T(\xi)^*\,d\xi,\qquad
w_I=\frac{\ell_I+u_I}{2},\qquad
\mathsf B_{\mathcal W}=\sum_{I\subset\mathcal W}w_I C_I.
\]
**Crucial distinction:** \(C_I\) and hence \(\mathsf B_{\mathcal W}\) are *exactly defined original physical-source Fourier Gram integrals*, **not numerically or interval evaluated by SM43**. The new result is a certified complete-source-matrix error bound:
\[
\boxed{
-\epsilon_{\mathcal W}I_{25}
\preceq
\mathsf A_{o,\mathcal W}-\mathsf B_{\mathcal W}
\preceq
\epsilon_{\mathcal W}I_{25},
\qquad
\epsilon_{\mathcal W}:=
\sum_{I\subset\mathcal W}
|I|\,(u_I-\ell_I)\,\sum_{j=1}^{25}s_{j,I}^2.
}
\]
Indeed for every **arbitrary coupled source coefficient vector** \(z\),
\[
\left|2\int_I(a_o-w_I)|z^*T(\xi)|^2d\xi\right|
\le |I|(u_I-\ell_I)\|z\|^2\sum_js_{j,I}^2,
\]
by the full Cauchy inequality \(|z^*T|^2\le\|z\|^2\|T\|^2\). The estimate pays **all 25×25 original cross interactions together**, not just diagonal entries. Every factor in the displayed epsilon is an EXACT nonnegative rational computed from full original real-frequency interval bounds. This is a genuine operator-form statement, albeit possibly conservative and **only for the covered union**.

## 3. Experimental source-window target and explicit nonpromotion

Build source-centered windows \(c_j\pm1/2\) around **all 16 distinct original selected SI10 frequency centers** and the original low [0,1] window; merge overlapping windows without double counting. These are physical original frequency intervals; their union is a STRICT SUBSET of [0,4096]. Compare exact rational mesh certificates with maximum step 1/4 vs 1/8, preserving the **identical union, original 25 source functions and exact whole-real multiplier**.

The pilot checks whether the source-aware entire-source Loewner epsilon contracts. It reports the actual number of original real cells and those which could contain a crossing \(m=\kappa\), without assuming actual root counts. If contraction is weak, refine only frequency regions with large certified contribution \(|I|(u-\ell)\sum s_j^2\), rather than uniform global 4096 subdivision.

**This is not a completed original positive LOW band certificate**. The rest of [0,4096] outside these source-centered windows is not processed at this resolution. Even inside the windows, the true cell Fourier Gram integrals \(C_I\) are only defined, not yet rigorously evaluated. Thus the accepted exact-\(\epsilon\) statement alone does not give a numerically useful stiffness matrix to invert. We do not replace \(C_I\) by unverified Gaussian quadrature samples.

## 4. SM44 and canonical acceptance

SM44 should rigorously enclose the original selected physically supported \(C_I=2\int_I T T^*\) with validated source-analytic Fourier integration (or an exact time-domain sinc kernel plus rigorous quadrature), and combine this with the SM43 certified whole-real **multiplier** error. For the complement of source windows, use adaptive source-leverage weight error targets and certified log high tail from SM41. When **all** [0,4096] is covered with a numerically usable enclosure and the high positive tail is added, certify the genuine full 25-source positive \(A_o\) source stiffness and true odd pole-conditioned \(A_*\) and strong residual before attempting all 470 original degree-k sources.

Original signed W-ODD-NEG complete O1/O2, original even E1–E4, whole signed Weil, native CC27 D-Riesz and RH all **OPEN**, as is the independent original Fourier/closed-form-domain mathematical audit. A passing SM43 interval-envelope replay is NOT RH proof, complete odd positivity, or a certified full positive resolvent.


## 5. Initial original constant-weight certificate passed, but proves the need for a *second-order* reference

First focused GitHub Actions run **39180315885 PASSED** the whole-real source-window **constant-step** certificate and exact operator-level Loewner error:
\[
|\mathcal W|=\frac{1029}{64}=16.078125,\qquad
\begin{array}{c|cc}
& \text{mesh}\le1/4&\text{mesh}\le1/8\\
\hline
\text{real signed-original positive cells}&65&129\\
\text{possible }m=\kappa\text{ cells}&55&44\\
\text{certified entire source-window }|\Delta A|\preceq\epsilon I_{25}
&\boxed{\epsilon<192.726657761}&\boxed{\epsilon<81.189344451}
\end{array}
\]
This is a **real mathematical error enclosure under inherited Fourier premises**, not the difference between floating Gaussian integrations. However, \(\epsilon=81.2\) remains **much too large** to certify true positive source stiffness or original complete odd sign. It is not evidence of the magnitude of the true numerical error: it measures conservatism of the complete source/Cauchy and multiplier envelopes. Uniformly pushing that original **piecewise-CONSTANT** method to a spectral tolerance would be computationally impractical.

### New SM43A mathematical development: interpolate the SIGNED original multiplier, *then* apply its positive part

Instead of approximating the genuinely variable positive weight by a constant on each source frequency cell, let \(m_\ell(a),m_u(a),m_\ell(b),m_u(b)\) be the exactly rational original endpoint signed seven-prime/digamma enclosures obtained from existing SI06/SM39/SM43. Define signed rational midpoint endpoints \(q_a=(m_\ell(a)+m_u(a))/2\), \(q_b=(m_\ell(b)+m_u(b))/2\), the original signed-multiplier **affine reference**
\[
q_I(\xi)=(1-t)q_a+tq_b,\qquad t=(\xi-a)/(b-a),
\]
and its **positive reference**
\[
\boxed{w_I^{\rm aff}(\xi)=\max\{\kappa,q_I(\xi)\}.}
\]
This reference is piecewise affine with **at most one rational crossing inside a cell**, regardless of how many actual crossings the original multiplier has.

Unlike \(a_o=\max(\kappa,m)\), the underlying original signed \(m\) is smooth. Write the original digamma-arch positive sum with \(v=k+1/4\), \(t=\pi\xi\):
\[
\mathcal A(\xi)=\text{constant}+\sum_{k\ge0}
\frac{t^2}{v(v^2+t^2)}.
\]
Its actual second derivative summands obey
\[
\left|\frac{d^2}{dt^2}
\frac{t^2}{v(v^2+t^2)}\right|
=\left|\frac{2v(v^2-3t^2)}{(v^2+t^2)^3}\right|
\le\frac{6}{(v^2+t^2)^{3/2}}.
\]
Using monotonicity of \((v^2+t^2)^{-3/2}\), for the entire real frequency \(\xi\ge a\ge1\), SI06 exact \(\pi_{\rm lo},\pi_{\rm hi}\) give the rational bound
\[
\boxed{
|\mathcal A''(\xi)|\le D_{\rm arch}(a)
:=6\pi_{\rm hi}^2\left[
\frac{4}{(1/4)^2+(\pi_{\rm lo}a)^2}
+\frac{1}{(\pi_{\rm lo}a)^2}
\right].
}
\]
For the initial physical band near \(\xi=0\), use the separate globally valid finite bound \(6\pi_{\rm hi}^2(64+8)\), avoiding a division by zero. The entire original signed seven-prime contribution obeys SM40's exact real \(|p''|\le D_2\). Thus
\[
\boxed{|m''(\xi)|\le D_I:=D_2+D_{\rm arch}(a)\quad\text{for every real }\xi\in[a,b].}
\]
Classical endpoint linear interpolation implies \(|m(\xi)-\mathrm{interp}(m(a),m(b))|\le D_I(b-a)^2/8\), and original endpoint signed multiplier uncertainties contribute at most \(\tfrac12 W_I\), where
\(W_I=\max(m_u(a)-m_\ell(a),m_u(b)-m_\ell(b))\). The positive-part map is **1-Lipschitz**, including at arbitrarily many actual \(m=\kappa\) crossings:
\[
\boxed{
|a_o(\xi)-w_I^{\rm aff}(\xi)|
\le\frac{W_I}{2}+\frac{D_I(b-a)^2}{8}.
}
\]
If the entire signed m is proved below \(\kappa\), both the true a_o and the rational affine reference are the constant \(\kappa\), and the error is **exactly zero**.

The complete original 25-source coupled operator error on the same frequency-window union \(\mathcal W\) is
\[
\boxed{
-\epsilon_{\mathcal W}^{\rm aff}I_{25}\preceq
A_{o,\mathcal W}
-\sum_{I\subset\mathcal W}
2\int_I w_I^{\rm aff}(\xi)T(\xi)T(\xi)^*\,d\xi
\preceq\epsilon_{\mathcal W}^{\rm aff}I_{25},
}
\]
where the exact rational computed error is
\[
\boxed{
\epsilon_{\mathcal W}^{\rm aff}
=\sum_I 2|I|\left(\frac{W_I}{2}
+\frac{D_I|I|^2}{8}\right)
\sum_{j=1}^{25}s_{j,I}^2
}
\]
(with zero replacement on certified \(a_o=\kappa\) constant cells).

This **removes the O(h) first-derivative oscillation fee** of SM43's constant weights, replaces it by a true original **O(h²) second-order curvature fee** plus rational endpoint interval uncertainty, and handles **every actual sign crossing** without root-finding. The reference *still* contains the true Fourier source cell integrals, which have **NOT YET** been rigorously evaluated. The complement of the chosen 16 original source frequency windows in [0,4096] is likewise OPEN. The follow-up SM43A code computes and compares the new exact source-coupled error against the original \(\epsilon<81.19\) bound at the same mesh, and is required by the updated focused CI.

**SM44 decision:** if the new certified affine error is materially tighter, integrate its **piecewise rational affine positive weight** against actual source-supported Fourier sine products using validated quadrature or an analytic sinc-kernel method, and expand source-leverage cells until the true complete original low positive band is covered. The rank-one odd pole and original high logarithmic tail remain separate and must be assembled with the true source stiffness. Nothing here is a complete original Wodd O1/O2 or RH certificate.
