# PS32 — True original even ground-state Fourier tail, physical mass nonconcentration, and effective-pole overlap

**W-PHYSICAL-SHIFT · 2026-10-18 · stacked on PS31 draft PR #200.** A new **actual original-operator, ground-state-specific analytic certificate**, not a computed eigenfunction, competitive PS31 physical graph weights, second eigenvalue sign, restored even positivity or RH.

The object is unchanged: true seven-prime, zero-extended, PS15 thirteen-source-eliminated even pole-**free** Schur \(L=\mathfrak S_C^{(0)}|_{\rm even}\), with source \(A_0\), cross \(B_0\), and effective positive even pole \(d\) from PS27–29. PS29's compact-resolvent / positive normalized ground-state analytic claim is an explicit prerequisite awaiting independent mathematical review.

## 1. NEW: genuine original ground-state logarithmic energy UPPER

Write \(L=J_C+V_{0,C}-B_0^*A_0^{-1}B_0\) on the original complementary logarithmic form domain, with \(\phi_0\ge0\) even, \(\|\phi_0\|_2=1\) and \(L\phi_0=\lambda_0\phi_0\), \(\lambda_0<-4359740/10^6\) from original PS27 RC315 constant-mode witness. Here \(J_C\ge0\) is the original *zero-extended* digamma form; \(V_{0,C}\) retains **every original seven-prime negative translation** and the true archimedean scalar, but excludes the positive even pole *before* source elimination.

Use the existing original-source outward rational bounds, without a new physical surrogate:
\[
V_C>-13I\quad(\text{PS17, \emph{full-pole} signed lower order}),\qquad
\|c_C\|^2<\frac{539}{180},\qquad
A_0>\frac{1997}{9000}I,\qquad
\|B_0\|<\frac{1403}{80}.
\]
Because \(V_{0,C}=V_C-2|c_C\rangle\langle c_C|\) on even vectors,
\[
V_{0,C}-B_0^*A_0^{-1}B_0
>
-TI,\quad
\boxed{T=13+\frac{539}{90}+\frac{(1403/80)^2}{1997/9000}<1406.}
\]
The first eigenvalue relation is an *equality*, not a comparator:
\[
J[\phi_0]=\lambda_0-\langle\phi_0,
(V_{0,C}-B_0^*A_0^{-1}B_0)\phi_0\rangle.
\]
Combine the true RC315 \(\lambda_0<-4.359740\) and this bounded original perturbation:
\[
\boxed{0\le J[\phi_0]< T-\frac{4359740}{10^6}<1401.}
\]
The last \(1401\) bound is a genuine quantitative estimate for the **unknown original negative ground eigenfunction itself**. It does *not* presume \(\phi_0\in L^\infty\), approximate the original source inverse numerically, or estimate the actual second eigenvalue. It uses the accepted PS17 / PS27 functional-analytic source bounds, still subject to independent review.

## 2. NEW: certified actual original Fourier concentration at an explicit (very large) bandwidth

In the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R} f(x)e^{-2\pi i\xi x}dx\) for the original zero extension, the original arch multiplier \(j(\xi)\ge0\) satisfies PS18's true all-frequency bound
\[
j(\xi)\ge\log(|\xi|/2)-1/\pi-1/2\qquad(|\xi|\ge2).
\]
Choose the **explicit symbolic bandwidth**
\[
\boxed{X=2^{8096}.}
\]
The original rational bounds \(\log2>693/1000\), \(\pi>3\) give for all \(|\xi|\ge X\)
\[
j(\xi)>(8095)\frac{693}{1000}-\frac56
=\frac{3365401}{600}>5604=4(1401).
\]
[The exact numerator of this rational is verified by the focused Fraction script; its value must not be inferred from a decimal approximation.]

Consequently Plancherel and the original full digamma energy yield
\[
\boxed{
\int_{|\xi|\ge X}|\widehat{Z\phi_0}(\xi)|^2\,d\xi
<\frac{1401}{5604}=\frac14,\qquad
\int_{|\xi|<X}|\widehat{Z\phi_0}(\xi)|^2\,d\xi>\frac34.
}
\]
This is a first quantitative **true original source-Schur ground eigenfunction Fourier-mass certificate**, albeit at a bandwidth far beyond any practical PS31 graph discretization. No such eigenfunction was calculated.

## 3. NEW: actual ground state cannot concentrate on an arbitrarily tiny physical set

Let \(E\subset I\) be **any** measurable physical subset, including unions of sharp source-complement components. Write the true zero-extended \(\phi_0=f_{<X}+f_{\ge X}\), where \(f_{<X}\) is the full-line Fourier projection onto \((-X,X)\). Cauchy–Schwarz and Plancherel give
\[
\|f_{<X}\|_\infty\le\sqrt{2X}\|f_{<X}\|_2\le\sqrt{2X},\qquad
\|f_{\ge X}\|_2<\frac12.
\]
Thus the following **quantitative physical concentration bound** holds for the true original \(\phi_0\), regardless of its pointwise boundedness:
\[
\boxed{
\|\mathbf1_E\phi_0\|_2
<\sqrt{2X|E|}+\frac12.
}
\]
For \(|E|\le(128X)^{-1}\), this is \(<5/8\), hence
\[
\boxed{
\int_E\phi_0(x)^2dx<\frac{25}{64}.
}
\]
In the PS31 actual even half-carrier normalization \(d\mu(x)=2\phi_0(x)^2dx\) on \(C_+=C\cap(0,B)\), any measurable half-set \(A\subset C_+\) of \(|A|\le(256X)^{-1}\) obeys the genuine original ground-mass cap
\[
\boxed{\mu(A)=\int_{A\cup(-A)}\phi_0^2\,dx<\frac{25}{64}.}
\]
It is **not** a positive lower mass for a particular macroscopic cell. The threshold \(\sim2^{-8096}\) is astronomically small, a concrete feasibility warning: a coarse log-Fourier-energy estimate alone cannot supply physically useful PS31 cell masses or pointwise \(W_N\) lower bounds.

## 4. NEW: explicit quantitative overlap with the true PS28 effective positive even pole

The actual normalized even ground is nonnegative (\(\phi_0\ge0\) from PS29), and PS28 proves the original effective renormalized even pole \(d=c_C-B_0^*A_0^{-1}c_P\ge1\) on physical \(C\). Since \(Z\phi_0\ge0\) and \(\|Z\phi_0\|_1<\infty\) by physical support, \(|\widehat{Z\phi_0}(\xi)|\le\|\phi_0\|_{L^1(C)}\). The above original Fourier **low mass**, without any L∞ ground assumption, forces
\[
\frac34
<\int_{-X}^X|\widehat{Z\phi_0}(\xi)|^2d\xi
\le2X\left(\int_C\phi_0\right)^2.
\]
Therefore
\[
\boxed{
\left(\int_C\phi_0\right)^2>\frac3{8X},\qquad
a^2=\langle d,\phi_0\rangle^2>\frac3{8X}
=\frac3{8\cdot2^{8096}}.
}
\]
Together with PS28's actual source coefficient \(\alpha>3994/2907\),
\[
\boxed{\alpha a^2>\frac{3994}{2907}\frac3{8\cdot2^{8096}}.}
\]
This upgrades PS29's **qualitative** \(a>0\) to the first explicit **true original ground/pole quantitative overlap lower** without evaluating \(d\) or \(\phi_0\). It is far too small to establish PS29's required pole-angle margin \(\Delta=a^2-|\lambda_0|\beta>0\); no coherent-scalar or restored even sign is asserted.

## 5. Limits and next certificate

Unlike PS31's conditional \(w_{ij}\) cells, these bounds apply **now** to the uncomputed original ground eigenfunction, subject to the inherited PS17–PS30 analytic premises. Exact Fraction replay verifies all constants and the Fourier-band, concentration, and pole-overlap inequalities as *symbolic deductions*. It does not evaluate \(\phi_0\), any true cell mass at macroscopic scale, \(w_{ij}\), \(\lambda_1\), \(\beta\) or \(\Delta\). Original negative odd and positive even poles remain correctly separated. A passing CI is no substitute for independent mathematical review of those premises.

**PS33:** improve the original ground's localized \emph{pointwise / physical-cell} control using its actual eigenfunction equation, an original positive-resolvent comparison / Harnack-type estimate if valid for the logarithmic nonlocal operator, or a ground-independent one-negative-index method. Merely increasing the symbolic Fourier bandwidth is a method no-go for computationally useful PS31 cells. Only after real macroscopic \(\mu_i,w_{ij}\) lower enclosures exist should the PS31 rational graph gap be called an evaluated original certificate.

**Governance:** \`W-PHYSICAL-SHIFT\` explicitly scoped local continuation. Canonical \`W-ODD-NEG\` remains unchanged. \(\lambda_1\ge0\), PS29 effective-pole angle and nullspace, \`W-EVEN-FORM\`, full original signed Weil, native CC27 D-Riesz and RH remain OPEN.

Replay: \`python3 scripts/validate_rpb108_ps32_original_ground_fourier_mass.py\`.
