# PS16 — Sign-relevant complementary Schur calibration: positive high-energy sector, nonzero seam penalty, and tight low-mode gap ceilings

**Scope:** W-PHYSICAL-SHIFT, stacked on PS15. **Canonical W-ODD-NEG, W-EVEN-FORM, complete original Weil positivity, and RH remain OPEN.** This checkpoint advances the *actual original signed* source/complement Schur form by (i) improving source coercivity and energy-dual penalty, (ii) proving a true positive **high-arch-energy complementary sector**, (iii) certifying a strictly nonzero original seam Schur correction, and (iv) deriving rigorous **even/odd upper ceilings** for any proposed uniform positive complementary gap using the already-pinned RC315 low-mode certificates. It does **not** establish positivity of the full complementary Schur form or a finite low-energy signed Schur PSD.

## 1. Same source, same complete original signed form and true Schur

Work in the original physical \(I=[-11/10,11/10]\), with zero extension, seven original prime-power translations \(n=2,3,4,5,7,8,9\), exact digamma difference energy
\[
J[f]=\int_0^\infty\frac{e^{-u/2}}{1-e^{-2u}}\|Zf-\tau_uZf\|^2\,du,
\]
scalar \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\), and **both correctly signed original rank-one poles**
\[
Q[f]=J[f]+c_{\rm arch}\|f\|^2
-2\sum_n\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)
+2|\langle f,\cosh(x/2)\rangle|^2-2|\langle f,\sinh(x/2)\rangle|^2.
\]

PS15's genuine sharp \(L^2\)-orthogonal thirteen-source/complement domain split is \(\mathcal D=\mathcal D_P\oplus\mathcal D_C\). Its cross \(B_{PC}\) includes every original arch Carleman seam, every source-to-complement prime shift and both poles. The source restricted operator \(A_P\) is positive; the **correct** complete signed complementary form is
\[
\mathfrak S_C[h]=Q_C[h]-\langle h,T_Ch\rangle,\qquad
T_C=B_{PC}^{*}A_P^{-1}B_{PC}\ge0.
\]
PS15 already proved \(T_C\) positive compact, despite \(\|B_{PC}\|_{\rm essential}\ge\log2\) in unweighted physical \(L^2\).

## 2. An improved original signed source gap and a smaller (still crude) penalty bound

PS14's *entire original* 13-channel matrix/source proof gives a certified 19-edge prime absolute matrix \(W\) with
\[
\max_i\sum_j (W^2)_{ij}<4.534344<
\left(\frac{213}{100}\right)^2,
\]
so the FULL original internal source prime operator norm is **strictly below \(213/100\)**, rather than PS14's rounded \(11/5\).

Replaying exactly the original 64-term positive digamma tail, cross-channel arch kernel and correctly signed odd pole gives strict outward-rational inequalities
\[
J_{\rm diag}+c_{\rm arch}>\frac{2683}{1000},\quad
\|\mathcal A_{\rm cross}\|<\frac{205}{1000},\quad
\text{negative odd pole allowance}<\frac{25}{1000}.
\]
The positive even pole is dropped only in a safe *lower* bound. Hence the **complete original** restricted source operator improves to
\[
\boxed{A_P>\frac{323}{1000}I}
\]
on the same verified sharp-domain carrier. All original 19 prime edges are retained.

With PS15's true complete signed source/complement cross \(\|B_{PC}\|<67/4\), its genuine positive compact energy-dual subtraction obeys
\[
\boxed{
0\le T_C,\qquad
\|T_C\|<
\frac{(67/4)^2}{323/1000}
=\frac{4489000}{5168}
<869.
}
\]
This strictly improves PS15's \(<1734\), but is **far too weak** to prove low-energy complementary positivity.

## 3. A true positive high-energy complement sector

PS11's signed original global lower bound is \(Q[f]\ge J[f]-13\|f\|^2\). It applies to the *same original physical* complement domain. Therefore for all \(h\in\mathcal D_C\),
\[
\begin{aligned}
\mathfrak S_C[h]
&\ge J[h]-13\|h\|^2-\langle h,T_Ch\rangle\\
&>J[h]-882\|h\|^2\qquad(h\ne0).
\end{aligned}
\]
Consequently,
\[
\boxed{
J[h]\ge882\|h\|^2,\ h\ne0\ \Longrightarrow\ 
\mathfrak S_C[h]>0.
}
\]
The restricted original arch form \(J_C\) has compact resolvent on the finite physical support (the PS05/PS07 Fourier-tail compact embedding and PS15 form-domain split). Thus the spectral subspace of \(J_C\) above energy \(882\) is an infinite-dimensional **positive** subspace of the **unshifted original complementary Schur** form. This is a real sign result, not positive shifted-graph stability.

**Critical limitation:** a positive high-\(J_C\)-energy principal block is NOT enough for a global PSD theorem. Mixed original signed low/high complementary terms and the *minus sign* of their Schur response remain to be certified. Any negative direction must have low-energy weight, but cannot simply be assumed to lie in a truncated low-energy subspace.

## 4. The original seam subtraction is demonstrably nonzero

At the true internal right seam \(x_0\) of the PS10 source interval \(I_2\), set \(\epsilon=\delta/64\), \(\delta=11/5-\log9\), and normalized indicators
\[
e_\epsilon=\epsilon^{-1/2}\mathbf1_{[x_0-\epsilon,x_0]},
\quad
h_\epsilon=\epsilon^{-1/2}\mathbf1_{[x_0,x_0+\epsilon]}.
\]
By the PS15 sharp-domain theorem both belong to the respective original source/complement domains. Their support diameter \(2\epsilon\) is smaller than every original prime shift, so the seven original prime mixed contributions vanish exactly. The true original arch cross tends to \(-\log2\); the two signed pole cross terms are \(O(\epsilon)\). The source-rational PS11/PS15 seam bound gives the **finite** strict inequality
\[
|\langle e_\epsilon,B_{PC}h_\epsilon\rangle|>\frac{69}{100}.
\]

For the normalized source step, \(D_{e_\epsilon}(u)=2\min(u/\epsilon,1)\). The full original arch kernel upper \(k(u)\le1/(2u)+1\) for \(0<u\le1\) and \(k(u)\le2e^{-u/2}\) for \(u\ge1\) imply
\[
J[e_\epsilon]<\log(1/\epsilon)+11.
\]
Because \(\delta>1/400\), one has \(1/\epsilon<25600=2^{10}5^2\). Use the exact rational source bounds for \(\log2,\log5,c_{\rm arch}< -5\), together with the even pole norm \(2\epsilon\cosh^2(B/2)\) and the safe dropping of the negative odd pole, to obtain
\[
\boxed{0<Q_P[e_\epsilon]<17.}
\]
Variationally,
\[
\langle h,T_Ch\rangle
=\sup_{e\in\mathcal D_P,\ e\ne0}
\frac{|\langle e,B_{PC}h\rangle|^2}{Q_P[e]}.
\]
Thus a *specific unit complement seam vector* has a certified nonzero correction:
\[
\boxed{
\langle h_\epsilon,T_Ch_\epsilon\rangle>
\frac{(69/100)^2}{17}
=\frac{4761}{170000}>0.028.
}
\]
This is a quantitative **lower** bound on the actual positive Schur subtraction. It demonstrates that ignoring source response would lose a meaningful original signed term. It does **not** produce a negative original Weil or Schur witness.

## 5. Parity-resolved necessary gap ceilings from source-pinned RC315

The thirteen source intervals are invariant under reflection \(x\mapsto-x\) (labels pair \(r\leftrightarrow9/r\)). Therefore \(P,C,A_P,B_{PC}\), and the actual complementary Schur respect even/odd parity.

Use the exact original physically normalized RC315 unit vectors
\[
u_0(x)=1/\sqrt R\quad(\text{even}),\qquad
u_1(x)=\sqrt{3/R}\,x/B\quad(\text{odd}),\quad R=11/5.
\]
For \(h_j=Cu_j\), the exact PS15 variational identity gives
\[
\boxed{
\mathfrak S_C[h_j]
=\inf_{e\in\mathcal D_P}Q[e+h_j]
\le Q[Pu_j+Cu_j]=Q[u_j].
}
\]
The pinned RC315 source intervals certify
\[
Q[u_0]\le\frac{20129633123}{500000000000}\approx0.04025927,
\qquad
Q[u_1]\le\frac{132390744079}{10^{12}}\approx0.13239075.
\]
The source measure is \(13\delta\). Exact \(u_0\) mass gives
\[
\|Cu_0\|^2=1-\frac{13\delta}{R},
\]
and \(|u_1(x)|^2\le3/R\) gives
\[
\|Cu_1\|^2\ge1-\frac{39\delta}{R}.
\]
Both denominators are strictly positive, and source-rational interval checks certify
\[
\boxed{
\frac{\mathfrak S_C[h_0]}{\|h_0\|^2}<\frac{41}{1000}=0.041
\quad\text{(even)},
\qquad
\frac{\mathfrak S_C[h_1]}{\|h_1\|^2}<\frac7{50}=0.14
\quad\text{(odd)}.
}
\]
The first inequality is an **upper**, not a positive lower, bound: \(\mathfrak S_C[h_0]\) could still be negative. No accepted proof of even or odd complementary positivity is implied.

Therefore ANY proposed **uniform strictly positive** complement Schur gap \(\mu\) must satisfy
\(\mu<0.041\) in the even sector and \(\mu<0.14\) in the odd sector. A certificate claiming a bigger global lower margin would contradict the **already source-certified original RC315 low modes**.

## 6. Inertia and finite acceptance target

Because \(A_P>0\) and PS15's exact completion of the square is a domain-preserving invertible triangular change of variables, the negative Morse index of \(Q\) equals that of the **actual** complementary signed Schur form \(\mathfrak S_C\). PS13's source-rational original Fourier/Bessel bound therefore transfers directly:
\[
\boxed{
\operatorname{ind}_-(\mathfrak S_C)=\operatorname{ind}_-(Q)
<352{,}000{,}000.
}
\]
This is a **conservative upper cap**, not a computed inertia. It does not establish zero negative directions.

**PS17:** assemble a useful low-energy *coupled* complementary Gram/Feshbach certificate with strict *positive sign*, including the high/low interactions, all original arch and prime/pole terms, and the full source response. A physically exact CC27 D-Riesz domain/norm bridge and independent review are mandatory for promotion of W-ODD-NEG or RH. This PS16 verifies no positive complementary Schur lower gap.

**Replay:** \`python3 scripts/validate_rpb108_ps16_schur_gap_calibration.py\` replays PS15→PS14→PS13→...→RC315 source pins, uses outward exact-rational original nineteen-prime-edge square, sixty-four-term arch tail, seam step test, and RC315 low-sector enclosures, while retaining canonical research objectives as OPEN. CI checks constants and definitions, not an independently formalized full Weil theorem.
