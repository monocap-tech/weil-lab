# PS17 — Complete signed complementary low/high Feshbach reduction with a tunable rigorous elimination error

**W-PHYSICAL-SHIFT, scoped, stacked after PS16.** The canonical obligation remains **W-ODD-NEG (OPEN)**. This checkpoint constructs the **true, domain-compatible finite-dimensional low-energy Feshbach operator** of the entire original signed Weil complement, including source energy response, and rigorously bounds the correction from eliminating **all** high-energy complementary modes. The exact rational bound is below **1/80** using an archimedean cutoff \(2^{26}\), and below **1/1000** at cutoff \(2^{30}\). These are **conditional finite-dimensional acceptance criteria**, NOT evaluated low matrices or positivity certificates. Original CC27 D-Riesz transfer, W-ODD-NEG, W-EVEN-FORM, whole original Weil positivity and RH remain OPEN.

## 1. Source-true full signed complementary Schur

Let \(I=[-B,B]\), \(B=11/10\); keep the complete zero-extended original physically supported signed form
\[
Q[f]=J[f]+c_{\mathrm{arch}}\|f\|^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)
+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2,
\]
where \(J[f]=\int_0^\infty\frac{e^{-u/2}}{1-e^{-2u}}\|Zf-\tau_uZf\|^2du\), \(c_{\mathrm{arch}}=-\gamma-\pi/2-3\log2-\log\pi\), \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\). There is no periodic wrapping, artificial physical cutoff, substituted sign, or omitted original prime power.

Let \(P\) be PS15's sharp characteristic projector onto the exact thirteen physical PS10 source intervals. Write \(C=I-P\). PS15 proves
\[
\mathcal D(Q)=\mathcal D_P\oplus\mathcal D_C
\]
as a source/complement \(L^2\)-orthogonal, **form-domain-compatible** split (including all 24 archimedean Carleman interfaces), and the complete signed cross \(B_{PC}:L^2(C)\to L^2(P)\) is bounded but noncompact in physical \(L^2\). The positive original source operator \(A_P\) satisfies PS16's sharpened \(A_P>(323/1000)I\).

The exact original signed Schur on the full physical complementary domain is
\[
\mathfrak S_C[h]=Q_C[h]-\langle h,T_Ch\rangle,\qquad
T_C=B_{PC}^*A_P^{-1}B_{PC}\ge0.
\]
The source response is positive **compact**, with the true (still coarse) original bound
\[
\|T_C\|<869.
\]
Nothing in PS17 replaces \(T_C\) by a finite-rank physical \(B_{PC}\), neglects a seam, or inverts only the restricted thirteen-channel matrix.

## 2. The real restricted arch energy and a bounded signed perturbation

On the **same original complementary form domain** \(\mathcal D_C\), let \(J_C\ge0\) be the positive self-adjoint operator represented by the full original digamma difference-energy \(J|_{\mathcal D_C}\). The form embedding \(\mathcal D_C\hookrightarrow L^2(C)\) is compact by the original logarithmic Fourier-tail theorem and PS15's sharp restriction. Hence \(J_C\) has compact resolvent.

All original lower-order terms are bounded on \(L^2(I)\). Denote their actual signed physical operator by \(V\), including the original scalar \(c_{\rm arch}\), all seven nonperiodic prime translations and both rank-one poles. The PS11 **sign-aware** two-sided form bound
\[
-13I<V<7I
\]
implies for its true complement compression \(V_C=CVC\) that
\(\|V_C\|<13\). In particular
\[
\boxed{
\mathfrak S_C[h]=
\langle h,J_C h\rangle_{\mathrm{form}}+
\langle h,M_Ch\rangle,
\qquad M_C=V_C-T_C=M_C^*,\quad\|M_C\|<882.
}
\]
This is an exact identity, preserving **all original signed** source and complement interactions through \(V_C\) and \(T_C\).

## 3. True finite spectral low/high decomposition, with all cross terms

Choose any **real** cutoff \(\Lambda>882\) outside a chosen eigenvalue ambiguity (use the Borel spectral projection at \([0,\Lambda)\), and include eigenvalues exactly equal to \(\Lambda\) in the high side). Set
\[
L_\Lambda=\mathbf1_{[0,\Lambda)}(J_C),\qquad
R_\Lambda=I-L_\Lambda.
\]
Because \(J_C\) has compact resolvent, \(L_\Lambda L^2(C)\) is **finite-dimensional**. Both spectral projections preserve \(\operatorname{Dom}J_C^{1/2}=\mathcal D_C\), and \(J_C\) has **zero low/high mixed form**. All the remaining cross interactions are exactly the bounded **signed** \(M_C\); none are discarded.

Relative to \(L_\Lambda\oplus R_\Lambda\), the actual complement Schur form has the block representation
\[
\begin{pmatrix}
D_{LL}&K_{LH}\\
K_{HL}&D_{HH}
\end{pmatrix},
\]
\[
\begin{aligned}
D_{LL}&=L_\Lambda(J_C+M_C)L_\Lambda
\quad\text{(genuine finite-dimensional matrix)},\\
K_{LH}&=L_\Lambda M_C R_\Lambda,\quad K_{HL}=K_{LH}^{*},\\
D_{HH}&=R_\Lambda(J_C+M_C)R_\Lambda
\quad\text{(closed-form high operator)}.
\end{aligned}
\]
For every nonzero high vector \(z\) in the restricted form domain,
\[
\langle z,D_{HH}z\rangle
>(\Lambda-882)\|z\|^2.
\]
Thus \(D_{HH}\) is self-adjoint and has a bounded positive inverse with
\[
\|D_{HH}^{-1}\|<\frac1{\Lambda-882},
\quad
\|K_{HL}\|<882.
\]
The completing-the-square **exact original signed Feshbach form** on the finite low space is
\[
\boxed{
F_\Lambda=
D_{LL}-K_{LH}D_{HH}^{-1}K_{HL},
}
\]
and its positive semidefinite *subtractive* high-response penalty obeys
\[
\boxed{
0\le K_{LH}D_{HH}^{-1}K_{HL},
\qquad
\|K_{LH}D_{HH}^{-1}K_{HL}\|
<\frac{882^2}{\Lambda-882}.
}
\]
The explicit inverse is the entire original signed HIGH complementary inverse; it is **not** replaced by \((R_\Lambda J_CR_\Lambda)^{-1}\).

For any \(x\) in the low eigenspace and high admissible \(z\),
\[
\mathfrak S_C[x+z]=
\|D_{HH}^{1/2}(z+D_{HH}^{-1}K_{HL}x)\|^2+
\langle x,F_\Lambda x\rangle.
\]
Consequently
\[
\boxed{
Q\ge0\text{ on the entire original physical form domain}
\iff
\mathfrak S_C\ge0
\iff
F_\Lambda\ge0.
}
\]
This is an **exact reduction to a finite but not yet computationally evaluated original signed low matrix**. The finite-dimensional matrix entries of \(J_C\), \(V_C\), \(T_C\), and the low/high high inverse have not been computed. There is no assumption that low and high sectors are uncoupled.

## 4. Quantitative, rational, fail-closed acceptance tolerances

Since \(882^2=777924\), exact integer arithmetic gives two explicit examples:
\[
\begin{array}{c|c|c}
\Lambda &\text{maximum high-response subtraction}&\text{sufficient acceptance}\\\hline
2^{26}&\frac{777924}{2^{26}-882}<\frac1{80}=0.0125&
D_{LL}>\tfrac1{80}I\\
2^{30}&\frac{777924}{2^{30}-882}<\frac1{1000}=0.001&
D_{LL}>\tfrac1{1000}I
\end{array}
\]
Each sufficiency statement means **if a future exact interval/eigenvalue certificate establishes that strict finite low-block inequality, then** \(F_\Lambda>0\) follows. Neither low-block inequality is presently known.

For the proper *parity-resolved* version, the original signed form, exact thirteen-source carrier, and \(J_C\) commute with reflection. Thus every object above is parity-block diagonal. The even PS16/RC315 necessary uniform full-Schur gap ceiling **\(0.041\)** and odd ceiling **\(0.14\)** remain in force. A hypothesized positive even margin cannot be inferred merely because \(1/80<0.041\): the actual finite low matrix must still be calculated.

The tunable bound for arbitrary target \(0<\varepsilon<1\) is explicit:
\[
\boxed{\Lambda>882+\frac{777924}{\varepsilon}
\quad\Longrightarrow\quad
\|D_{LL}-F_\Lambda\|<\varepsilon.}
\]
This makes the missing finite low matrix and its needed margin **precisely defined acceptance obligations**. However the associated low subspaces for \(2^{26},2^{30}\) are likely extremely large and their eigenfunctions/inverse responses are not constructed. These inequalities are analytical error gates, **not** a computationally practical finite-rank Schur certification.

## 5. Negative inertia and witness recovery

The exact low/high completing-square map is boundedly invertible on the relevant product *form domains* for fixed \(\Lambda>882\), because the mixing is bounded and \(D_{HH}^{-1}\) maps \(L^2\) into the high operator domain. Therefore the negative index of the full original form \(Q\) equals the negative index of \(F_\Lambda\) (PS15 already equated \(Q\)'s index with \(\mathfrak S_C\)'s). In particular,
\[
\operatorname{ind}_-(Q)=\operatorname{ind}_-(F_\Lambda)
<352{,}000{,}000
\]
using PS13's conservative global source-rational cap. This does NOT compute either index.

If an independently accepted vector \(x\) with \(\langle x,F_\Lambda x\rangle<0\) were found, a true negative original physical-form direction is reconstructed by
\[
z_*=-D_{HH}^{-1}K_{HL}x,\quad
h=x+z_*,\quad
e_*=-A_P^{-1}B_{PC}h,
\]
so \(Q[e_*+h]=\langle x,F_\Lambda x\rangle<0\). Likewise, a verified \(F_\Lambda\ge0\) would prove whole physical \(Q\ge0\), but **would still require native CC27 D-Riesz domain/norm attachment** before an RH promotion.

## 6. What PS17 does and does not close

The actual high/low *form-domain and sign* issue is resolved structurally: the infinite high-energy complement has a strict positive block; all its interactions are included as one **subtractive, bounded, positive finite-dimensional Feshbach correction**. Rigorous response allowances \(<1/80\) or \(<1/1000\) are established by exact arithmetic, not assumed.

**Still open:** actual spectral resolution/eigenfunctions and original signed finite \(D_{LL}\) entries; a *certified positive eigenvalue margin* for \(F_\Lambda\) or a genuine obstruction; efficient energy-adapted representation avoiding astronomical low rank; accepted complete CC27 D-Riesz domain identification, external proof audit, W-ODD-NEG, W-EVEN-FORM and RH.

**PS18:** use the real physical source response and a practical energy-adapted basis to compute an accepted \(D_{LL}\) matrix/positive-margin certificate with rigorous residuals (or a negative witness). Do not treat the \(2^{26}\) arch cutoff itself as a solved finite matrix.

Replay: \`python3 scripts/validate_rpb108_ps17_low_high_feshbach.py\`. The validator replays PS16→PS15→PS14→PS13→...→original RC315 pin, checks the sign-aware \(\|V_C\|<13\), \(T_C<869\), two exact-rational Feshbach error and acceptance gates, reflection custody, and open theorem standing. The infinite-dimensional analytic proof is not independently peer-reviewed merely by successful Actions.
