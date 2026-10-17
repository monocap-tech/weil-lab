# PS11 — True original energy-inverse channel response: leakage is real, but inverse series converges geometrically

**Lane:** W-PHYSICAL-SHIFT (scoped), stacked on PS10. **Canonical W-ODD-NEG remains OPEN.** This checkpoint (a) demonstrates non-invariance of PS10's 13 physical channels under the actual original signed graph operator, (b) rigorously preconditions its **true** energy inverse with a quantitative geometric error, and (c) moves the entire original seven-prime IMS source to an **exact compact five-channel inverse Gram operator** without falsely assuming invariant channels. It also improves the actual signed IMS pole correction bound by exploiting the physical edge width. No source-channel inverse kernel is yet computed, no full signed Schur PSD, CC27 D-Riesz domain attachment, W-ODD-NEG, W-EVEN-FORM, whole Weil positivity, or RH proof.

## 1. Actual original graph-energy operator and sharper *signed* lower bound

Continue with the **same** original zero-extended physical Weil quadratic form on \(I=[-B,B]\), \(B=11/10\):
\[
q[f]=J[f]+c_{\rm arch}\|f\|^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\operatorname{Re}C_f(\log n)
+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2 ,
\]
where \(J\) is PS01's complete positive digamma translation-difference form,
\(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\),
\(w_n=\Lambda(n)/\sqrt n\),
\(c(x)=\cosh(x/2)\) and \(s(x)=\sinh(x/2)\).

Let \(J_{\rm op}\ge0\) denote the unique self-adjoint operator representing the closed form \(J\) on **physical** \(L^2(I)\). Put
\[
D=J_{\rm op}+20I,\qquad
V=c_{\rm arch}I-2\sum_nw_n\operatorname{Re}C_n
+2|c\rangle\langle c|-2|s\rangle\langle s|,
\qquad
H=D+V.
\]
The prime notation \(\operatorname{Re}C_n\) here means the self-adjoint physical nonperiodic cosine-translation operator of norm \(\le1\), NOT a scalar correlation. The complete sign-correct original graph quadratic form is \(G[f]=q[f]+20\|f\|^2=\langle f,Hf\rangle_{\rm form}\).

Crucially **do not** take absolute values of both signed poles in the same lower bound. Their distinct true \(L^2\) masses are
\[
\|c\|_2^2=B+\sinh B,\qquad
\|s\|_2^2=\sinh B-B.
\]
With \(W=\sum_n w_n\), the **whole original** bounded perturbation obeys the two-sided form bound
\[
v_- I\le V\le v_+ I,\qquad
\begin{cases}
v_- = c_{\rm arch}-2W-2(\sinh B-B),\\
v_+ = c_{\rm arch}+2W+2(B+\sinh B).
\end{cases}
\]
Exact original RC315 source-rational enclosures certify
\[
\boxed{-13<v_-<-12,\qquad 6<v_+<7.}
\]
In particular
\[
\boxed{H\ge J_{\rm op}+7I,\qquad \|H^{-1}\|<\frac17.}
\]
This improves PS08's coarse \(H>2.1I\) using only the existing original pole signs and full seven-prime coefficients.

## 2. A certified convergent inverse with no \(2^{8206}\) matrix

Because \(D\ge20I\), its bounded inverse square root exists. The **actual original** relative bounded source perturbation
\[
S=D^{-1/2}VD^{-1/2}=S^*,\qquad
\|S\|\le\frac{\max(-v_-,v_+)}{20}<\frac{13}{20}
\]
satisfies
\[
H=D^{1/2}(I+S)D^{1/2}
\quad\text{as closed forms}.
\]
Hence the true complete original positive graph-energy inverse is
\[
\boxed{
H^{-1}=D^{-1/2}(I+S)^{-1}D^{-1/2}
=D^{-1/2}\sum_{k=0}^\infty(-S)^kD^{-1/2}.}
\]
For \(N\ge0\), define the **positive**, self-adjoint bounded truncated inverse
\[
T_N=D^{-1/2}\sum_{k=0}^N(-S)^kD^{-1/2}.
\]
Its spectral polynomial \(\sum_{k=0}^N(-t)^k=[1-(-t)^{N+1}]/(1+t)\) is strictly positive on \(|t|<13/20\). The rigorous uniform original-operator error is
\[
\boxed{
\|H^{-1}-T_N\|
<\varepsilon_N:=\frac1{20}\frac{(13/20)^{N+1}}{1-13/20}.}
\]
An **exact Fraction certificate**, not a floating tolerance, gives
\[
\boxed{\varepsilon_{64}<10^{-13},\qquad \varepsilon_{96}<\frac{1}{9\cdot10^{18}}.}
\]
Only 65 or 97 preconditioned source terms are required to give these **abstract operator-norm** tolerances. The base \(D^{-1/2}\) itself still requires the full supported archimedean energy solve. This is **not** a finite-rank matrix nor a claimed practical original inverse computation. It replaces PS08's spectacularly unhelpful *uniform-grid proof architecture* with a geometrically convergent **preconditioner**, not with a completed spectral certificate.

## 3. Channel leakage is genuine

Let \(P_{13}\) be the orthogonal support projector onto the exact union of PS10's 13 intervals, and \(P_5=UU^*\le P_{13}\) the projector onto its five effective fiber modes. There is **no** unproved assertion that \(P_{13}\), \(P_5\), or their sharp supports preserve the complete original graph operator.

In fact \(P_{13}\) **does not reduce \(H\)**. Choose the true PS10 original interval \(I_{\log2}=[-B+\log2,-B+\log2+\delta]\), its right endpoint \(x_0\), and \(\epsilon=\delta/64\). Let
\[
f_\epsilon=\epsilon^{-1/2}1_{[x_0-\epsilon,x_0]},
\quad
g_\epsilon=\epsilon^{-1/2}1_{[x_0,x_0+\epsilon]}.
\]
The true channel gap \(>1/10\) ensures \(f_\epsilon\in P_{13}L^2(I)\) and \(g_\epsilon\in (I-P_{13})L^2(I)\); both are original signed logarithmic-form-admissible step profiles. All **seven** original prime cross terms vanish since the entire combined support diameter \(2\epsilon<\log2\). The scalar graph mass has zero cross term. The exact archimedean cross bilinear form is negative:
\[
b_{\rm arch}(f_\epsilon,g_\epsilon)
=-\frac1{\epsilon}\int_0^\epsilon\int_0^\epsilon k(r+t)\,dr\,dt
\le-\log2+\epsilon/4.
\]
The original **both signed** pole contribution in absolute value is at most \(2\epsilon\cosh B\). Thus
\[
\boxed{
\operatorname{Re}b_H(f_\epsilon,g_\epsilon)
\le-\log2+\epsilon(1/4+2\cosh B)<-\frac{69}{100}<0.
}
\]
If \(P_{13}\) reduced the self-adjoint \(H\), its closed energy form would have no mixed term between these two vectors. Contradiction. Therefore \(P_{13}\) does **not** commute with \(H^{-1}\) or \(H^{-1/2}\). In particular
\[
\boxed{(I-P_{13})H^{-1}P_{13}\ne0.}
\]
This is **real physical source leakage**, not a numerical roundoff artifact. No unsupported lower bound on the inverse leakage *norm* is inferred.

## 4. Exact five-channel *inverse Gram* without fake invariance

Let \(\mathscr C=L^2([0,\delta];\mathbb C^5)\), and let \(U:\mathscr C\to L^2(I)\) be PS10's **fixed isometric** five-mode fiber embedding. The entire original prime-IMS localization remainder is
\[
\mathcal R_{\rm prime}=U\,M_{\rm eff}\,U^*,
\qquad
\|M_{\rm eff}\|=\rho_7=
\left(\sum_{n\in\{2,3,4,5,7,8,9\}}w_n^2\right)^{1/2}<\frac{71}{50}.
\]
Here \(M_{\rm eff}\) is multiplication by PS10's **true continuous** 5-by-5 fiber matrix, not finite rank.

Define the **full-original-energy inverse Gram**
\[
F:=U^*H^{-1}U:\mathscr C\to\mathscr C,\qquad
F_N:=U^*T_NU.
\]
No invariance of \(U\mathscr C\) under \(H\) is assumed. Both \(F,F_N\) are strictly positive, bounded and compact when appropriate: \(F\) is positive **compact** because the full original physical \(H^{-1}\) is compact (PS07), while each finite \(F_N\) is positive but is **not claimed compact without independently checking \(D^{-1}\)** (which is compact on the supported interval by the same arch graph embedding). Source-rational certificates give
\[
0<F\le\tfrac17I,\qquad
\boxed{\|F-F_N\|<\varepsilon_N}.
\]
In particular the inverse leakage is already fully included in the compressed Gram \(F\): it is *not* approximated by inverting the compressed matrix \(U^*HU\).

The original physically graph-energy normalized prime-IMS operator
\[
K_{\rm prime}:=H^{-1/2}\mathcal R_{\rm prime}H^{-1/2}
\]
has the **same nonzero spectrum (including multiplicities)** as the compact self-adjoint **five-channel inverse Gram sandwich**
\[
\boxed{
K_{5,\rm prime}=F^{1/2}\,M_{\rm eff}\,F^{1/2}
\quad\text{on }\mathscr C.
}
\]
Proof: write \(A=H^{-1/2}U\), so \(A^*A=F\), and take the polar decomposition \(A=W F^{1/2}\). Because \(F\) is injective (strictly positive original inverse), \(W\) is an isometry on \(\mathscr C\), and \(K_{\rm prime}=W K_{5,\rm prime}W^*\). No false equality of the two operators on different Hilbert spaces is asserted. The five-channel operator still acts on an **infinite-dimensional** continuum fiber.

The **actual normalized prime size** now admits the sharp-source, signed-graph bound
\[
\boxed{
\|K_{\rm prime}\|
\le\rho_7\|H^{-1}\|
<\frac{71}{350}<\frac{203}{1000}.
}
\]

Even without evaluating \(F_N\), PS11 controls the error of the finite-iteration five-channel spectral operator
\[
K_{5,N}:=F_N^{1/2}M_{\rm eff}F_N^{1/2}.
\]
The square-root operator Hölder inequality for positive operators yields
\[
\|K_{5,\rm prime}-K_{5,N}\|
\le\rho_7(\|F^{1/2}\|+\|F_N^{1/2}\|)\sqrt{\varepsilon_N}.
\]
Since \(\|F\|,\|F_N\|<4/25\), \(\rho_7<71/50\), \(\varepsilon_{64}<1/(3\cdot10^6)^2\) and \(\varepsilon_{96}<1/(3\cdot10^9)^2\), exact rational arithmetic certifies
\[
\boxed{
\|K_{5,\rm prime}-K_{5,64}\|<4\cdot10^{-7},
\qquad
\|K_{5,\rm prime}-K_{5,96}\|<4\cdot10^{-10}.
}
\]
These are *valid uniform spectral-operator error bounds conditional only on the analytically defined \(F_N\)*; the \(F_N\) integral kernels and finite-rank entries have **not** been calculated. This is a substantial **inversion error** reduction, not proof that spatial channel discretization is easy.

## 5. Correctly signed pole cancellation: a much smaller IMS defect

PS07's original pole IMS correction norm estimate \(<12\) ignored that both mask defects vanish away from the tiny edge collar. For each original pole vector \(v=c,s\), the exact rank-one contribution is
\[
2\sigma_v(|\alpha v\rangle\langle\alpha v|
+|\beta v\rangle\langle\beta v|-|v\rangle\langle v|),
\quad \sigma_c=+1,\ \sigma_s=-1.
\]
Set \(e_v=\|1_E v\|\), where \(|E|=2\delta\). Since \(\alpha=0,\beta=1\) off \(E\),
\[
\|\alpha v\|\le e_v,\qquad
\|(\beta-1)v\|\le e_v,
\]
and the rank-one difference estimate gives
\[
\|\mathcal R_{\rm pole}\|
\le2\sum_{v=c,s}\big(e_v^2+2\|v\|e_v\big).
\]
Exact original source enclosures with \(\delta<1/350\),
\[
\sup_E c<7/6,\quad \sup_E|s|<7/12,\quad
\|c\|<8/5,\quad \|s\|<1/2
\]
prove \(e_c<9/100,\ e_s<9/200\). Therefore
\[
\boxed{
\|\mathcal R_{\rm pole}\|
<\frac{549}{800}=0.68625<\frac7{10},
\quad
\|H^{-1/2}\mathcal R_{\rm pole}H^{-1/2}\|<\frac1{10}.
}
\]
This is a source-supported bound on the **actual two correctly signed original poles**, not their omission. Combined with the PS10 sharp prime norm,
\[
\|\mathcal R_{\rm prime}+\mathcal R_{\rm pole}\|<2.12
\quad\text{and}\quad
\|H^{-1/2}(\mathcal R_{\rm prime}+\mathcal R_{\rm pole})H^{-1/2}\|<0.303.
\]
The archimedean IMS correction is still nonzero and has not been shown sufficiently small in the energy graph to close positivity.

## 6. Standing and next discriminator

**What is closed within PS11:** (i) physical 13-channel subspace is genuinely not invariant, (ii) the *true full original energy inverse* admits geometrically convergent source-preconditioned approximants with explicit small uniform errors, (iii) the exact five-mode prime representation persists as an **inverse Gram compression** that automatically includes leakage, and (iv) pole-defect cancellation dramatically reduces the remaining signed localization allowance.

**Still open:** explicit \(D^{-1/2}\) / \(F_N\) action in a computable native carrier, finitely certified source Gram eigenvalues, sufficiently sharp **archimedean** energy-normalized IMS remainder, true signed positive complement Schur gap, complete CC27 D-Riesz norm/domain attachment, whole Weil positivity and RH. PS12 should exploit the tiny-support arch IMS kernel and energy metric to certify the missing correction rather than retry naive PS08 uniform gridding.

Replay: \`python3 scripts/validate_rpb108_ps11_energy_inverse_channel_response.py\`. It replays PS10→PS09→PS07→PS06→PS03→RC315 pinned source identities, uses exact rational inequalities for the two-sided signed-graph bounds, 65/97-term inverse tails, five-channel spectral error, true original leakage witness, pole cancellation and no-promotion governance. All operator identities are analytic and require independent functional-analytic review; passing CI is not a complete Weil or RH proof.
