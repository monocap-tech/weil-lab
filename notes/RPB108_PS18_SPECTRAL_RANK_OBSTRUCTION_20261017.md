# PS18 — A certified spectral-rank obstruction to the PS17 cutoff strategy

**W-PHYSICAL-SHIFT, scoped after PS17.** The canonical W-ODD-NEG, W-EVEN-FORM, original whole Weil positivity and RH remain **OPEN**. This checkpoint **does not** fabricate the PS17 low finite matrix or its eigenvalue sign. Instead it certifies that the low spectral projection proposed in PS17 is *provably astronomically large* for the cutoffs needed by the existing uniform high-response estimate, and shows why a different, energy-aware sign architecture is required. A finite-dimensional reduction may be mathematically valid without being computationally viable.

## 1. Same true original physical source and complement

Keep the original nonperiodic, zero-extended signed seven-prime physical Weil form of PS01–PS17 on \(I=[-B,B]\), \(B=11/10\), with positive digamma archimedean difference energy
\[
J[f]=\int_0^\infty k(u)\|Zf-\tau_uZf\|_{2}^{2}du,\qquad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\]
The true original unshifted \(Q\) retains all \(n=2,3,4,5,7,8,9\) signed prime translations, scalar \(c_{\rm arch}\), positive even pole and negative odd pole. Let \(C\) be the genuine sharp complement of PS15's thirteen-channel physical source, and \(J_C\) the closed nonnegative restricted original arch operator on \(\mathcal D_C\). PS15 certifies the sharp domain split and PS05/07 prove the compact logarithmic arch form embedding, so \(J_C\) has compact resolvent.

PS17's exact true complement Schur has \(\mathfrak S_C=J_C+M_C\) with \(\|M_C\|<882\), and its genuine finite-low spectral projection is
\[
L_\Lambda=\mathbf1_{[0,\Lambda)}(J_C).
\]
For cutoffs \(\Lambda>882\), the complete original signed high response is bounded by \(882^2/(\Lambda-882)\). PS17 **does not compute** the low block \(D_{LL}=L_\Lambda(J_C+M_C)L_\Lambda\), and neither does PS18.

## 2. One explicit original complementary interval has a huge low-arch subspace

The source-pinned exact PS10/15 channels immediately neighboring the positive central complement gap are
\[
I_3=[-B+\log3,\ B-\log3],\qquad
I_4=[-B+\log4,\ -B+\log4+\delta],
\quad \delta=2B-\log9.
\]
Original outward-rational logarithm enclosures give
\[
B-\log3<\frac18,\qquad \log4-B>\frac{3}{16}.
\]
Thus the **fixed actual physical interval**
\[
\boxed{J_0=[1/8,\,3/16]\subset\operatorname{supp}C,
\qquad |J_0|=1/16}
\]
lies entirely in the sharp original complementary carrier. The other source channels are farther away; no false interior support assumption is needed.

For any positive integer \(M\), divide \(J_0\) into \(M\) equal cells of length \(h=1/(16M)\). Define \(\mathscr W_M\) as the **M-dimensional linear space of arbitrary complex cellwise-constant functions supported on \(J_0\)**, extended by zero everywhere else. These discontinuous functions are **genuinely admissible** for the original logarithmic form, as the following direct estimate proves.

For \(f\in\mathscr W_M\) and \(0<u<h\), the exact translation-difference norm is the sum of jump-square energies times \(u\); the elementary inequality \(\sum_{\mathrm{jumps}}|a_{j+1}-a_j|^2\le4\sum_j|a_j|^2\) yields
\[
\|Zf-\tau_uZf\|_2^2\le\frac{4u}{h}\|f\|_2^2.
\]
For \(u\ge h\), the norm is at most \(4\|f\|_2^2\). Use the **original kernel**, with valid elementary bounds
\[
k(u)\le\frac1{2u}+1 \quad(0<u\le1),
\qquad k(u)<2e^{-u/2}\quad(u\ge1).
\]
Integrate explicitly over \(0<u<h\), \(h<u<1\) and \(1<u<\infty\):
\[
\begin{aligned}
\frac{J[f]}{\|f\|_2^2}
&\le(2+2h)+(2\log(1/h)+4-4h)+16e^{-1/2}\\
&<22+2\log(1/h)=22+2\log(16M).
\end{aligned}
\]
The inequality is uniform over the **entire M-dimensional space**, not just a list of numerical trial functions, and uses no surrogate operator.

## 3. A true exponential lower bound on the native spectral low rank

For every integer cutoff \(\Lambda\ge100\), set
\[
m=\lfloor\Lambda/2\rfloor,\qquad M=2^{m}.
\]
Using the outward-rational original source inequality \(\log2<7/10\),
\[
J[f]<\left(22+2(m+4)\log2\right)\|f\|^2
<\left(\frac{138}{5}+\frac7{10}\Lambda\right)\|f\|^2
<\Lambda\|f\|^2
\quad(f\in\mathscr W_M\setminus0).
\]
The last strict inequality holds uniformly for \(\Lambda\ge100\).

The exact **min–max principle** for the actual compact-resolvent \(J_C\) forces at least \(M\) eigenvalues strictly below \(\Lambda\), with multiplicity. Consequently,
\[
\boxed{
\dim\mathbf1_{[0,\Lambda)}(J_C)L^2(C)
\ \ge\ 2^{\lfloor\Lambda/2\rfloor}
\quad(\Lambda\in\mathbb Z,\ \Lambda\ge100).
}
\]
This is a rigorous **lower bound on the dimension of the spectral LOW space**. The \(\mathscr W_M\) cell basis provides the min–max witness; it is **not asserted to be the spectral eigenbasis** or invariant under \(J_C\).

In particular, the two exact PS17 cutoffs require
\[
\begin{aligned}
\boxed{\dim L_{2^{26}}\ge2^{33\,554\,432}},\\
\boxed{\dim L_{2^{30}}\ge2^{536\,870\,912}}.
\end{aligned}
\]
The notation is exponent-only; **no such matrix, cell count or basis is allocated by the validator**.

The fact that \(J_C\)'s spectrum grows logarithmically in frequency means increasing the energy cutoff even modestly forces an exponential increase in spectral-low dimension. PS17's uniform high-response truncation is therefore **an analytically legitimate but computationally noncompetitive certificate architecture**.

## 4. A companion whole-original Fourier/Bessel upper counting estimate

The source-pinned original arch Fourier multiplier is
\[
j(\xi)=2\int_0^\infty k(u)(1-\cos2\pi\xi u)\,du
\ge\log(|\xi|/2)-1/\pi-1/2\qquad(|\xi|\ge2).
\]
For any integer \(\Lambda\ge100\), choose the **symbolic** Fourier bandwidth
\(X=2^{3\Lambda+1}\). Original rational \(\log2>693/1000\) and \(\pi>3\) imply
\[
j(\xi)>3\Lambda\frac{693}{1000}-\frac56
>2\Lambda,\qquad |\xi|\ge X.
\]
For every unit vector \(f\) in the true finite-dimensional low spectral subspace of \(J_C\), one has \(J[f]\le\Lambda\), so strictly more than half of its zero-extended Fourier mass is within \([-X,X]\).

For any orthonormal basis of that subspace, Bessel's inequality for the restricted plane waves on the **actual support \(I\)** gives
\(\sum_j|\widehat{Zf_j}(\xi)|^2\le|I|=R=11/5\). Integrating over \([-X,X]\) yields
\[
\boxed{
2^{\lfloor\Lambda/2\rfloor}
\le\dim L_\Lambda
<\frac{44}{5}\,2^{3\Lambda+1}.
}
\]
Both bounds are **analytic source-rational operator statements**; the upper confirms finiteness without pretending to enumerate eigenfunctions. The lower shows the relevant finite matrix is not an actionable computational target by exhaustive spectral construction.

## 5. The PS17 high-response acceptance thresholds are already impractical

The true PS17 signed high-response **sufficient bound** is
\[
\varepsilon_{\mathrm{high}}(\Lambda)
=\frac{777924}{\Lambda-882}.
\]
To certify \(\varepsilon_{\mathrm{high}}<1/80\) **using that bound alone** requires
\[
\Lambda>882+80(777924)=62\,234\,802,
\]
so the smallest integer cutoff satisfying this conservative gate is \(62\,234\,803\). The above min–max lower implies its finite low space has at least
\[
\boxed{2^{31\,117\,401}}
\]
dimensions.

For \(\varepsilon_{\mathrm{high}}<1/1000\), the conservative gate requires \(\Lambda>777\,924\,882\), with minimum integer cutoff \(777\,924\,883\); the original spectral low dimension is at least
\[
\boxed{2^{388\,962\,441}}.
\]

**Interpretation:** these numbers are computational lower bounds **for the particular PS17 native spectral-cutoff workflow and its conservative sufficient response criterion**. They are not lower bounds on the number of actually negative directions, mathematical complexity of RH, possible efficient basis sizes for different operator representations, or rank needed by an energy-adapted proof.

## 6. A crucial positive counterweight, and the correct research pivot

The entire witnessing \(\mathscr W_M\) is supported inside the same short original complementary interval \(J_0\) of length exactly \(1/16\). Thus **PS13's genuine unshifted original signed local theorem applies uniformly**:
\[
\boxed{
Q[f]>\frac14\|f\|^2
\qquad(f\in\mathscr W_M\setminus0).
}
\]
This is true for arbitrarily enormous \(M\), with all seven physical prime autocorrelations identically zero on this single support interval and the original negative odd pole paid.

**Do not conflate this with \(\mathfrak S_C[f]>0\)**: the source energy-dual subtraction \(\langle f,T_Cf\rangle\ge0\) remains, and the orthogonal spectral projection of \(\mathscr W_M\) to \(L_\Lambda\) need not preserve this local positivity. Nevertheless it demonstrates why an enormous low-ARCH spectral space need not correspond to an enormous set of genuinely problematic Weil directions. This is positive structure the PS17 brute spectral cutoff ignores.

**Next PS19:** replace exhaustive native \(J_C\) low eigenspace construction with an *energy-adapted local positivity / inter-window coupling / compact source-response Feshbach* certificate that treats proven-positive local support families **en bloc**. Prioritize an explicit finite set of *coherent cross-window or pole-mediated* directions and a mathematically accepted residual that is small relative to the RC315 even upper-gap ceiling \(0.041\). Do not claim a future signed positive matrix exists until its true entries and residuals are actually evaluated. The complete original CC27 D-Riesz map and independent proof review remain mandatory.

## 7. Replay and standing

Run \`python3 scripts/validate_rpb108_ps18_spectral_rank_obstruction.py\`. It replays PS17→PS16→PS15→...→RC315 source; verifies the original complement window and kernel inequalities, *symbolic* enormous min–max lower and Bessel upper rank statements, exact signed high-response necessary *method thresholds*, PS13 local unshifted positivity witness, and W-ODD-NEG/no-RH-promotion custody. The analytic min–max proof is not machine-formalized just by successful rational CI.

**Status:** PS18 closes the **feasibility diagnosis of the PS17 spectral-cutoff approach**, not the actual finite low signed Schur PSD. Original full complementary Schur positivity, canonical odd/even obligations, CC27 D-Riesz and RH remain OPEN.

## 8. New positive sign result: an entire prime-quiet complementary Schur window

The rank diagnosis above also suggests a *positive* use for PS13's local coercivity: choose a window where **none of the seven original prime shifts reaches the thirteen-source carrier**, then bound the true signed source-response subtraction quantitatively rather than merely bounding the original \(Q\).

The exact source-rational witness is
\[
J_{\rm quiet}=\left[\frac{269}{5000},\,\frac{1163}{10000}\right]
=[0.0538,0.1163],\qquad |J_{\rm quiet}|=\frac1{16}.
\]
It lies entirely in the original PS15 complement \(C\), strictly between source intervals \(I_3\) and \(I_4\). For **every** one of the 13 exact source interval labels \(r\) and **all seven** \(n\in\{2,3,4,5,7,8,9\}\), check the two translated sets \(J_{\rm quiet}\pm\log n\). Outward original-source log interval arithmetic verifies that **each is disjoint from \(I_r\)**, with minimum strict separation exceeding \(1/20000\). Therefore
\[
\boxed{B_{\rm prime,PC}h=0\qquad
(\operatorname{supp}h\subset J_{\rm quiet}).}
\]
This is a complete original **source-to-complement prime cross statement**, not a claim that global original prime shifts are absent.

The source/complement **archimedean** kernel remains \(-k(|x-y|)\). Define \(d_r=\operatorname{dist}(I_r,J_{\rm quiet})>0\). Because \(k(u)\) decreases and satisfies \(k(u)\le1/(2u)+1\), the **entire original arch** mixed operator restricted to this window has
\[
\begin{aligned}
\|P B_{\rm arch}1_{J_{\rm quiet}}\|_{\rm HS}^2
&=\sum_{r\in\mathscr O}\int_{I_r}\!\int_{J_{\rm quiet}}
k(|x-y|)^2\,dy\,dx\\
&\le\delta|J_{\rm quiet}|
\sum_{r\in\mathscr O}\left(1+\frac1{2d_r}\right)^2
<\left(\frac7{40}\right)^2.
\end{aligned}
\]
Every source interval appears in the **exact rational** sum; no boundary or off-channel arch interaction is discarded.

For the original correctly signed even/odd rank-one poles, \(|\operatorname{supp}P|=13\delta\), and the source-rational bounds
\[
\sqrt{13\delta}<\frac{19}{100},\quad
\cosh(B/2)<\frac{29}{25},\quad
\sinh(B/2)<\frac{29}{50},
\]
\[
\cosh(\sup J_{\rm quiet}/2)<\frac{501}{500},
\quad
\sinh(\sup J_{\rm quiet}/2)<\frac{59}{1000}
\]
give the true complete source-to-window pole bound
\[
\|P B_{\rm pole}1_{J_{\rm quiet}}\|
\le 2\big(\|Pc\|\|1_{J_{\rm quiet}}c\|
+\|Ps\|\|1_{J_{\rm quiet}}s\|\big)
<\frac{23}{200}.
\]
Together with exact prime-cross disappearance,
\[
\boxed{
\|B_{PC}1_{J_{\rm quiet}}\|
<\frac7{40}+\frac{23}{200}
=\frac{29}{100}.
}
\]
The PS16 source positivity \(A_P>\frac{323}{1000}I\) controls the **genuine full original energy-dual subtraction**
\[
\langle h,T_Ch\rangle
=\langle B_{PC}h,A_P^{-1}B_{PC}h\rangle
<\frac{(29/100)^2}{323/1000}\|h\|^2
<\frac{261}{1000}\|h\|^2.
\]
For every original-form-admissible \(h\) supported in \(J_{\rm quiet}\), PS13's same-original-form 32-term digamma certificate gives \(Q_C[h]=Q[h]>\frac{133}{500}\|h\|^2\). The resulting **true unshifted original complementary Schur** theorem is
\[
\boxed{
\mathfrak S_C[h]
=Q_C[h]-\langle h,T_Ch\rangle
>
\left(\frac{133}{500}-\frac{(29/100)^2}{323/1000}\right)\|h\|^2
>\frac1{200}\|h\|^2.
}
\]
**This is genuine signed complementary Schur positivity on an infinite-dimensional, separately admissible window subspace**, even after eliminating the complete original thirteen-source block. The proof retains all original source archimedean and both pole couplings, and rules out all seven prime-to-source terms by exact physical geometry.

It is **not** whole complementary positivity: multiple quiet/nonquiet windows may have cross interactions, and the original complement contains functions outside this one interval. The theorem also does not imply that the \(J_C\) low spectral projection of this window stays in the window. It nevertheless provides an explicit **coercive source-aware local module** to use in PS19 instead of brute native low-energy eigenspace enumeration.

The validator independently checks every source-to-quiet prime shift and every arch-distance/pole interval constant with exact rational arithmetic. Passing its focused CI certifies its scoped inequalities; this theorem still requires independent proof review before any main-objective promotion.
