# Weil-Lab — IV052
## The original Gamma jump-coordinate Schur gate and a second nonconstant infinite-dimensional signed-Weil positive class

**Standing (November 21, 2026):** Classical source-matched mathematical derivation, with a genuinely executed standard-library `Fraction` checker and SHA-256-bound receipt. **NONKERNEL**: no new original-source Lean compilation, no `.olean` or `#print axioms` acceptance. No new branch, PR, source commit, workflow dispatch or CI-producing work. The numerical original HD/A kernel-passed frontier remains **692/968**, with the historical registry-body reconciliation distinct. The independently derived classical Gamma inverse/Fourier atom and closed-form-domain identification are still formalization obligations.

### Exact source and fixed domain

Physical window: \(I=(-a,a)\), \(a=11/10\), \(L=2a=11/5\). Fourier: \(\widehat f(\xi)=\int e^{-2\pi i\xi x}f(x)dx\). Actual original signed form, with first-slot antilinearity, is
\[
W[f]=\gamma(0)\|f\|_2^2+D[f]-P_{\rm original}[f]
   +|\langle h,f\rangle|^2-|\langle k,f\rangle|^2,
\quad
D[f]=\tfrac12\iint K(x-y)|f(x)-f(y)|^2dxdy,
\]
where \(K(u)=e^{-|u|/2}/(1-e^{-2|u|})\), \(h=\sqrt2\,1_I\cosh(x/2)\), \(k=\sqrt2\,1_I\sinh(x/2)\). The prime term is the literal two-sign \(\Lambda(n)/\sqrt n\) sum at \(n\in\{2,3,4,5,7,8,9\}\), with the real \(n=9\) contribution retained. The real source symbol has the Lean NF599 gain expansion
\[
\gamma(t)=\gamma(0)+\sum_{n\ge0}\frac{(t/2)^2}{a_n(a_n^2+(t/2)^2)},\quad a_n=n+\tfrac14,
\quad-\tfrac{28}{5}<\gamma(0)<0.
\]
The classical Fourier atom producing \(K\) is mathematically derived but **not** newly compiled into original IV Lean.

## 1. Exact jump-coordinate representation of the original Gamma interface

For \(M\in\{100000,132000\}\), write \(w=L/M\), cell endpoints \(x_r=-a+rw\), normalized cells \(e_j=w^{-1/2}1_{(x_j,x_{j+1})}\), and \(v=\sum_{j=0}^{M-1}a_je_j\). Extend \(a_{-1}=a_M=0\). Define **all** boundary jumps
\[
\Delta_0=a_0,\quad\Delta_r=a_r-a_{r-1}\ (1\le r<M),\quad\Delta_M=-a_{M-1},
\quad \|\Delta a\|_{\ell^2}^2=\sum_{r=0}^{M}|\Delta_r|^2.
\]
The zero-extended physical step function is the finite Heaviside sum \(v(x)=w^{-1/2}\sum_r\Delta_r1_{x>x_r}\). With
\[
H(s)=\int_s^\infty K(u)du=\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2}),\quad s>0,
\]
the exact (a.e.) original Gamma difference-operator potential is
\[
\boxed{
\Gamma v(x)=\gamma(0)v(x)+\frac1{\sqrt w}
\sum_{r=0}^{M}\Delta_r\,\operatorname{sgn}(x-x_r)H(|x-x_r|).}
\tag{IV052-jumps}
\]
It follows by linearity from \(\int K(x-y)(1_{x>x_r}-1_{y>x_r})dy=\operatorname{sgn}(x-x_r)H(|x-x_r|)\). The logarithmic endpoint singularities are in \(L^2\); actual cell indicators belong to the completed original Gamma form and operator domains. The scalar contact \(\gamma(0)v\) vanishes after high-mode projection \(Q_M\).

For a fixed input boundary jump \(r\), project the jump potential to zero mean on output cell \(j\): \(Q_j\). Elementary centered-log variance and \(K(s)\le1/(2s)+1\) give exact universal cellwise estimates:
\[
\left\|Q_j\frac{\operatorname{sgn}(x-x_r)H(|x-x_r|)}{\sqrt w}\right\|_{L^2(J_j)}
\le\begin{cases}
2,&j=r\text{ or }j=r-1,\\[2pt]
\frac1{2d}+w,&d=\min(|j-r|,|j-r+1|)\ge1.
\end{cases}
\]
The majorant matrix has nonnegative row and column sums bounded by \(4+H_M+2Mw\). For both historical meshes, \(M\le132000\) and the positive 16-term Taylor partial sum of \(e^{12}\) exceeds \(132000\), so \(H_M<1+\log M<13\). Since \(Mw=L=11/5\), the row/column sum is strictly below \(4+13+22/5=107/5\). A Hilbert direct-sum Schur test therefore yields
\[
\boxed{\|Q_M\Gamma v\|_2<\frac{107}{5}\|\Delta a\|_{\ell^2}.}\tag{IV052-Gamma-gradient}
\]
The proof uses the actual Gamma kernel and the exact source physical projection, not a replacement graph.

The **original** two-sign prime translations obey the IV051 exact fractional-shift variance law. Each signed shift contributes at most \(\frac12\|\Delta a\|\) after \(Q_M\), and the genuine coefficient sum satisfies \(2\sum_{n=2,3,4,5,7,8,9}\Lambda(n)/\sqrt n<71/10\). Thus
\[
\|Q_MP_{\rm original}v\|\ <\frac{71}{20}\|\Delta a\|.
\]
Both crossed poles give \(\|Q_M(|h\rangle\langle h|-|k\rangle\langle k|)v\|<(2w/3)\|v\|\), using cell Poincaré and \(h'=k/2\), \(k'=h/2\). Hence
\[
\boxed{\|Q_MW_{\rm original}v\|<25\|\Delta a\|+\frac{2w}{3}\|v\|\quad (M=100000,132000).}
\tag{IV052-full-gradient}
\]
The finite, physical, boundary-inclusive \(\ell^2\) jump norm is crucial: the norm of a constant physical indicator is not zero because its two exterior jumps are preserved.

## 2. A new even trial very close to the spectral boundary

Take the normalized, even parabolic physical test
\[
\boxed{p(x)=\frac{1-(x/a)^2}{\sqrt{16a/15}}1_{(-a,a)}(x),\qquad \|p\|_2=1.}
\]
This is a continuous compactly supported piecewise-polynomial \(H^1\) function (not itself \(C_c^\infty\)), in the closed Gamma form domain, approximable there by actual even Schwartz tests supported strictly inside \(I\).

For \(0\le u\le L\), its exact translated correlation is
\[
C_p(u)=1-\frac{5u^2}{4a^2}+\frac{5u^3}{8a^3}-\frac{u^5}{32a^5};
\quad C_p(u)=0\ (u\ge L).
\]
Let \(b_n=2(n+1/4)\), and define \(c_2=5/(4a^2)\), \(c_3=-5/(8a^3)\), \(c_5=1/(32a^5)\). Each exact source Gamma atom has the evaluable form
\[
D_n[p]=2\sum_{m\in\{2,3,5\}} c_m\int_0^L e^{-b_nu}u^mdu+\frac{e^{-b_nL}}{n+1/4},
\]
with \(\int_0^L e^{-bu}u^mdu=(m!/b^{m+1})(1-e^{-bL}\sum_{j=0}^m(bL)^j/j!)\). For the true original prime side, \(P[p]=2\sum_n (\Lambda(n)/\sqrt n)C_p(\log n)\) with all seven listed powers. For the true positive even pole, let
\[
T=\frac{16\cosh(a/2)}a-\frac{32\sinh(a/2)}{a^2};\qquad \mathrm{Pole}[p]=\frac{2T^2}{16a/15},
\]
while the odd pole vanishes by parity; **both** source poles remain defined and their signs respected.

The standard-library exact checker uses rational outward intervals for Machin's \(\pi\), logarithms (arctanh series), square roots (integer \(\operatorname{isqrt}\)), exponentials (positive Taylor with explicit geometric remainder), the Euler–Mascheroni H400 bracket, 350 rational source Gamma atoms, and an integral-test majorant for the tail. It produces:

| Original source component (normalized) | Exact rational interval displayed decimally |
|---|---:|
| \(\gamma(0)\) | −5.372186015600 to −5.372182898393 |
| \(D[p]\) | 2.789367837189 to 2.789369954535 |
| \(P[p]\) | 1.310880857251 (outward interval) |
| Both original poles | 3.894338593501 (outward interval) |
| **Complete source \(W[p]\)** | **0.000639557839 to 0.000644792392** |

Therefore the certified **mathematical** inequality is
\[
\boxed{\frac6{10000}<W[p]<\frac7{10000},\quad\inf\sigma(W_{\rm even})<\frac7{10000}.}
\tag{IV052-even-trial}
\]
This sharply improves IV046's previous one-sided \(0.0087\) bound. It proves neither nonnegativity of the full even sector nor a negative Weil test.

## 3. A second, genuinely nonconstant infinite-dimensional positivity class

For the **100000-cell** mesh, let \(v=\Pi_Mp\). Define
\[
\mathcal S_{\rm parabola}:=\{f\in C_c^\infty(I;\mathbb C):\exists \alpha\in\mathbb C\ \forall j,\ \int_{J_j}f=\alpha\int_{J_j}p\}.
\]
This is a complex *infinite-dimensional* Schwartz subspace. Unlike IV051's equal-means class, its cell-average pattern is **nonconstant**. Every such \(f\) decomposes orthogonally as \(f=\alpha v+q\), \(q\in Q_M\).

New source-form estimates are:

1. **Control of the source form operator on the parabolic trial.** The actual gamma gain satisfies \(g_{a_n}(t)\le|t|/(4a_n^2)\) and \(\sum_{n\ge0}a_n^{-2}<18\). Therefore \(|\gamma(t)|<28/5+(9/2)|t|\). Since \(\|p'\|/\|p\|=\sqrt{5/(2a^2)}<3/2\), the actual Gamma L² operator bound is \(\|\Gamma p\|<247/20\). Adding the true seven-prime norm \(<71/10\) and two-pole signed norm \(<5\) yields \(\|W_{\rm op}p\|<489/20\).
2. **Cell-mean approximation error.** The sharp cell Poincaré inequality gives \(\|p-v\|<(w/\pi)\|p'\|<w/2\). Write \(q_p=p-v\in Q_M\). The *true original* IV051 high-mode theorem gives \(W[q_p]>(49/100)\|q_p\|^2\). Hence \(W[v]=W[p]-2\Re W(p,q_p)+W[q_p]>3/5000-(489/20)w=621/10000000\).
3. **Boundary-inclusive discrete gradient.** The interior jump-square sum of the projected polynomial is \(\le w^2\|p'\|^2\); its two exterior jumps contribute at most \(15w^3/(8a^3)\). Thus \(\|\Delta a(v)\|^2\le w^2(5/(2a^2)+15w/(8a^3))<(3w/2)^2\). IV052-full-gradient yields \(\|Q_MWv\|<(229/6)w=2519/3000000\).
4. **Exact positive Schur inequality.** With \(c=49/100\) for the whole infinite-dimensional high complement and \(\mu=1/20000\), the checker confirms the strictly positive rational margin
\[
\boxed{
 \left(\frac{621}{10000000}-\mu\right)
 -\frac{((229/6)w)^2}{c-\mu}
 =\frac{23505097}{2204775000000}>0.
}
\]
Consequently the **full genuine original signed** form satisfies
\[
\boxed{W[f]>\frac1{20000}\|f\|_2^2\qquad (0\ne f\in\mathcal S_{\rm parabola}).}
\tag{IV052-parabolic-class}
\]
This is a nonconstant low direction **plus the whole infinite-dimensional high complement**. It does **not** certify their span with IV051's constant-low direction; two separately positive subspaces need not have positive cross interactions.

## 4. A second exact low-frequency mesh consequence, still conditional

For the normalized first discrete Dirichlet sine coefficient vector \(a_j=\sqrt{2/(M+1)}\sin(\pi(j+1)/(M+1))\), one has \(\|\Delta a\|=2\sin(\pi/(2(M+1)))<22/[7(M+1)]\). The exact checker verifies the actual original high-mode \(W|_{Q_M}>49/100\) on **both** historical meshes and obtains directionwise energy-relative Schur upper bounds:

| Mesh | Mixed-column upper | Energy-relative Schur cost upper |
|---|---:|---:|
| M=100000 | 0.000800374 | 0.000001307342 |
| M=132000 | 0.000606345 | 0.000000750315 |

These are **conditional utilities** for future finite-dimensional certification. Without a lower bound on the signed original low-form value \(W[v_{\rm sine}]\), no extra sine-low positivity subspace is asserted. The exact parabolic class above *does* have its own independently certified low energy.

## 5. Verification obligations, CI lineage, and cross-projection scope

**Local executable source audit:** `IV052_jump_gradient_and_parabolic_trial_checker.py` and `IV052_jump_gradient_and_parabolic_trial_receipt.json`, exact standard-library fractions and integers, genuine `PASS`, checker SHA-256 `336cc8bdb652b2e745be533e0af298105fd13f9e6f88ad7d34ef78bd0541c0e1`. Verified predecessor script digests IV045/IV047/IV050/IV051. The checker verifies the finite polynomial/source prime integrals, Gamma finite atoms and tail, true pole moments, harmonic/Taylor inequalities, source derivative and mean-gradient rational bounds, Schur arithmetic, and a finite complex jump-telescope sanity model. **A finite rational model is not a Lean kernel proof of the continuum identity.**

**Original formal dependencies:** NF599 quarter-digamma gain theorem; IV011 authentic two-sign prime definition; IV017 actual Gamma spectral attachment; IV044 signed even/odd pole identity; IV045 exact fixed-window source constants; IV047 high-mode source theorem; IV051 source zero-mean improved pole bound; PI007/PI008 classical Fourier inversion. Source Gamma Fourier atom/physical operator identity, compact-support closed log-form, cellwise Neumann Poincaré, jump potential, high-mode and Schur theorems require new original-source Lean compilation and standard-only `#print axioms` receipts.

**Active CI gate, read-only:** IV023 PR #805 head SHA `b966f42cd51541a78c060b1cc22f0edab142f800` retains true Lake-first strict IV018/IV023 preflights and source-scoped NF456/NF471 receipt fixes, but still demonstrably has unrestricted historical PR triggers including NF453/NF454/NF457/NF463. The 611-workflow branch has not been proven bounded in fan-out; do **not** launch a heavy Phase IV compiler against this lineage. User lifted analytical-only research pause, but controlled CI verification is mandatory. Historical IV018/IV023 pre-Lean failures and accepted IV009/NF750–NF753 artifacts remain unmodified. Original HD/A kernel-passed frontier **692/968**; historical canonical registry body reconciliation is separate.

**Next IV053:** source-exact mixed two-low-direction Schur coupling between the constant and parabola profiles, a sharper low-grid graph preconditioner, and/or a rigorous a posteriori low-matrix bound. Submit a small source-bound Gamma jump-interface Lean candidate only after the effective branch workflow inventory, actual bounded PR fan-out, and stagewise IV018/IV023 recovery are verified. PI/CP interoperability must preserve actual form, translation, parity, poles, and the physical projection dictionary; `25`, cell width and fractional-shift phases are **not** intrinsic independent spectral invariants. **No global or support-independent Weil positivity, RH, or independent equivalence is claimed.**
