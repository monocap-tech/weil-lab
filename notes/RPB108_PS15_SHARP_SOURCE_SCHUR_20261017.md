# PS15 — Full original sharp thirteen-source form-domain split and exact signed Schur reduction

**W-PHYSICAL-SHIFT, scoped after PS14. Canonical W-ODD-NEG remains OPEN.** This checkpoint proves the *actual sharp support projector* onto the thirteen disjoint PS10/PS14 source intervals preserves the entire physical logarithmic Weil-form domain, including all twenty-six interior interval boundaries. It then constructs the **complete original signed Weil off-diagonal source/complement operator**, proves it is bounded **but not compact in physical L²**, and gives the **exact infinite-dimensional Schur reduction** with a **positive compact** energy-dual correction. The **sign of the complementary Schur form is NOT established**. This is not whole Weil positivity, CC27 D-Riesz transfer, or RH.

## 1. Same original physical signed quadratic form and source carrier

On \(I=[-B,B]\), \(B=11/10\), with zero extension \(Zf\), preserve the original signed PS01–PS14 form
\[
Q[f]=J[f]+c_{\rm arch}\|f\|^2-2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\operatorname{Re}C_f(\log n)+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2 ,
\]
where \(J[f]=\int_0^\infty k(u)\|Zf-\tau_u Zf\|^2du\), \(k(u)=e^{-u/2}/(1-e^{-2u})\), \(w_n=\Lambda(n)/\sqrt n\), \(c=\cosh(x/2)\), \(s=\sinh(x/2)\), \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\). All seven original prime powers and both pole signs are retained.

Let \(\delta=2B-\log9\), \(I_r=[-B+\log r,-B+\log r+\delta]\), with the same **thirteen distinct exact rational labels**
\[
\mathscr O=\{1,9,2,3,4,5,7,8,9/2,9/4,9/5,9/7,9/8\}.
\]
Set \(P=\mathbf1_{\cup_{r\in\mathscr O}I_r}\), \(C=I-P\) on \(L^2(I)\). Intervals touch the physical endpoints for \(r=1,9\) and have 24 other internal boundaries, so the support interface has **24 internal edges** (two internal endpoints for each of the other eleven intervals, one for each extreme interval): total \(2\cdot11+2=24\). At every such boundary the source/complement interaction is nonlocal and must be retained. The source measure is \(|\operatorname{supp}P|=13\delta\).

**Analytic domain claim:** with \(\mathcal D=\{f\in L^2(I):J[f]<\infty\}\), *both* \(Pf\) and \(Cf\) lie in \(\mathcal D\) for every \(f\in\mathcal D\). The same argument applies separately to all thirteen characteristic channel projections \(1_{I_r}\).

## 2. Bounded complete original off-diagonal operator — every seam retained

For \(e\in L^2(P)\), \(h\in L^2(C)\) initially form-admissible independently, define the mixed Hermitian form \(b(e,h)\) of the **same original signed Q** by
\[
Q[e+h]-Q[e]-Q[h]=2\operatorname{Re}b(e,h).
\]
Since the supports are disjoint, the scalar mass term has no cross contribution.

The actual signed **archimedean** cross is
\[
b_{\rm arch}(e,h)=-\iint_{\operatorname{supp}P\times\operatorname{supp}C}
k(|x-y|)\,e(x)\overline{h(y)}\,dx\,dy.
\]
Its kernel has a genuine Carleman \(1/(2(s+t))\) singularity at each of the 24 source/complement interfaces. For each source interval \(I_r\), split the complement into left and right portions. The globally valid bound
\(k(u)\le1/(2u)+1\), the sharp Carleman \(L^2(0,\infty)\)-norm \(\pi\), and the regular constant-one Hilbert–Schmidt piece give the bound for its output into \(L^2(I_r)\):
\[
\|P_r B_{\rm arch}C\|
\le\frac{\pi}{\sqrt2}+\sqrt{\delta R},
\quad R=2B=11/5.
\]
The thirteen outputs are orthogonal, hence
\[
\|B_{\rm arch}\|
\le\sqrt{13}\left(\frac{\pi}{\sqrt2}+\sqrt{\delta R}\right)
<\frac{35}{4}=8.75.
\]
The strict outward rational proof uses \(\pi<22/7\), \(\sqrt2>7/5\), \(\sqrt{13}<15/4\), and \(\delta<1/350\) giving \(\sqrt{\delta R}<2/25\). This bound is conservative; it handles **all** interfaces, not just the two PS04 edge seams.

The entire original prime cross operator (including shifts *out of* the source carrier) has
\[
\|B_{\rm prime}\|\le 2\sum_n w_n<\frac{71}{10}.
\]
This is a bound on the full original nonperiodic physical signed shifts, not PS10's thirteen-interval internal 19-edge matrix.

The genuine source–complement pole coupling obeys
\[
\|B_{\rm pole}\|\le2\|Pc\|\|Cc\|+2\|Ps\|\|Cs\|<\frac9{10},
\]
by \(|\operatorname{supp}P|=13\delta\), \(\sqrt{13\delta}<1/5\), \(\sup_I c<7/6\), \(\sup_I|s|<7/12\), \(\|c\|<8/5\), \(\|s\|<1/2\). This includes *both* correctly signed original rank-one poles.

Thus the complete original signed offdiagonal operator \(B_{PC}:L^2(C)\to L^2(P)\) exists as a bounded extension and obeys
\[
\boxed{\|B_{PC}\|<\frac{35}{4}+\frac{71}{10}+\frac9{10}
=\frac{67}{4}=16.75<17.}
\]

## 3. Exact sharp-support form-domain theorem (not an assumed domain transfer)

For cutoff \(M>0\), define the integrable positive truncation \(k_M(u)=\min(k(u),M)\) and
\[
J_M[f]=\int_0^\infty k_M(u)\|Zf-\tau_uZf\|^2du.
\]
For any \(f\in L^2(I)\), \(J_M[f]\) is finite, and \(J_M[f]\uparrow J[f]\) as \(M\to\infty\) by monotone convergence.

Set \(e=Pf\), \(h=Cf\). Exact quadratic expansion of the **original physical** difference kernel gives
\[
J_M[e]+J_M[h]
=J_M[f]+2\operatorname{Re}\iint_{P\times C}
k_M(|x-y|)e(x)\overline{h(y)}\,dx\,dy .
\]
The mixed integral is uniformly bounded in \(M\) by the **same complete** Carleman-plus-regular operator norm \(35/4\), since \(0\le k_M\le k\). Therefore
\[
J_M[e]+J_M[h]\le J[f]+2(35/4)\|e\|\,\|h\|
\le J[f]+\frac{35}{4}\|f\|^2.
\]
Monotone convergence yields the concrete **domain-stable sharp projector** inequality
\[
\boxed{
J[Pf]+J[Cf]\le J[f]+\frac{35}{4}\|f\|^2<\infty.
}
\]
Similarly each \(P_r\) and its complement preserve \(\mathcal D\). All **bounded signed prime/pole perturbations** retain the identical original form domain. Hence
\[
\boxed{\mathcal D=(\mathcal D\cap L^2(P))\oplus(\mathcal D\cap L^2(C))}
\]
as a true orthogonal \(L^2\) **domain decomposition**, with sharp source and complement restrictions, not the overlapping PS06/PS07 partition. This repairs the PS14 independently-admissible-components limitation for the whole physical realization.

## 4. The physical cross remains noncompact: an explicit seam witness

Take one of the original inner source interval endpoints \(x_0\), for example the **right** endpoint of \(I_2\), and \(0<\epsilon\ll\delta\). Let
\[
e_\epsilon=\epsilon^{-1/2}\mathbf1_{[x_0-\epsilon,x_0]},\qquad
h_\epsilon=\epsilon^{-1/2}\mathbf1_{[x_0,x_0+\epsilon]}.
\]
They lie in the source and complement respectively, are physical logarithmic-form admissible, and converge weakly to zero. For \(\epsilon<\delta/64\), the combined support diameter is smaller than every original prime shift \(\log n\); thus **all seven signed prime cross terms vanish exactly**. Both pole cross terms are \(O(\epsilon)\). The actual original arch form has
\[
b_{\rm arch}(e_\epsilon,h_\epsilon)
=-\frac1\epsilon\int_0^\epsilon\int_0^\epsilon k(s+t)\,ds\,dt
\longrightarrow-\log2.
\]
Therefore
\[
\boxed{\|B_{PC}\|_{\rm essential}\ge\log2>0.69.}
\]
This rules out approximating the full original offdiagonal coupling in unweighted physical L² by finite-rank matrices with vanishing operator-norm remainder. It does NOT refute the signed Schur approach.

## 5. Exact original signed Schur reduction and compact energy penalty

Let \(A_P\) be the self-adjoint operator represented by \(Q\) **restricted to the now-proved genuine source form domain** \(\mathcal D_P=\mathcal D\cap L^2(P)\). PS14 certifies
\[
Q[e]>\frac16\|e\|^2
\quad(e\in\mathcal D_P\setminus\{0\}),
\]
including every one of the 19 true original internal prime connections. The restricted form is closed: it is the original positive arch form plus bounded signed source terms. Thus \(A_P\ge(1/6)I\).

PS05/07's **complete original logarithmic Fourier-growth** on bounded support makes the form embedding \(\mathcal D_P\hookrightarrow L^2(P)\) compact. Accordingly, \(A_P^{-1/2}\) and \(A_P^{-1}\) are compact; crucially this does not require \(P\) to commute with the full \(Q\) operator.

For \(h\in\mathcal D_C=\mathcal D\cap L^2(C)\), set the **actual signed energy-dual correction**
\[
T_C=B_{PC}^*A_P^{-1}B_{PC}\ge0.
\]
It is compact, self-adjoint and bounded on \(L^2(C)\), with conservative rigorous norm
\[
\boxed{\|T_C\|<6\cdot17^2=1734.}
\]
This is **not a smallness certificate** and is too crude to conclude complement positivity.

Let \(Q_C\) be the original restricted signed form on \(\mathcal D_C\). The exact original signed completing-the-square identity is
\[
\boxed{
Q[e+h]
=\left\|A_P^{1/2}(e+A_P^{-1}B_{PC}h)\right\|^2
+\mathfrak S_C[h],
\qquad
\mathfrak S_C[h]=Q_C[h]-\langle h,T_Ch\rangle.
}
\]
The minimizer \(e_*=-A_P^{-1}B_{PC}h\) belongs to the original source operator domain and is admissible. Consequently,
\[
\boxed{\inf_{e\in\mathcal D_P}Q[e+h]=\mathfrak S_C[h].}
\]
Thus **positivity of the entire original physical signed Weil form is equivalent to positivity of the true complementary Schur form** \(\mathfrak S_C\). Its sign has NOT been determined.

This is an exact **full-original-domain** infinite-dimensional Schur assembly with correct minus sign, noncompact seam retained, and compact energy-dual penalty. It is stronger structurally than PS14's isolated source positivity, but not a proof of whole Weil positivity.

## 6. Status, verification and actual next gate

**PS15 establishes:** 24 physical source/complement seams, source and complement characteristic projectors preserve the complete original form domain with explicit bound, true full signed offdiagonal norm <17 and essential norm \(\ge\log2\), strict source coercivity from PS14, and the **exact signed complementary Schur form** with compact nonnegative penalty.

**PS16 remains:** compute an actionable quantitative approximation to \(T_C\) in the *correct source energy* and certify \(\mathfrak S_C\ge0\) or find a valid obstruction. The whole physical CC27 D-Riesz norm/domain identification and independent proof audit are still mandatory. No W-ODD-NEG, W-EVEN-FORM or RH closure follows.

Replay: \`python3 scripts/validate_rpb108_ps15_sharp_source_schur.py\`. Source-pinned PS14→PS13→...→RC315 replays, exact thirteen-interval offset and 24-boundary count, outward rational Carleman/prime/pole mixed upper <17, original sharp-projector domain control, seam essential norm and exact signed Schur minus-penalty governance. Operator theory is proved analytically and requires independent mathematical review; numerical CI is a constant/source gate, NOT an evaluated signed Schur PSD.
