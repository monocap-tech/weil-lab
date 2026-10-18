# PS23 — Positive nested signed Schur across a genuine noncompact Carleman seam

**W-PHYSICAL-SHIFT · October 17, 2026 · stacked after PS22.** The canonical W-ODD-NEG, W-EVEN-FORM, full original Weil positivity, native CC27 D-Riesz domain/norm bridge and RH remain OPEN. PS23 directly addresses the previously untested **noncompact physical interface** between PS22's positive eight-window subsystem and the remaining complement: two very narrow *adjacent* reflected collars. It proves positivity of the **actual original twice-eliminated residual Schur on the collars**, after paying the full source and eight-window inverse responses, and constructs a single positive combined TEN-window source-eliminated subsystem. This does NOT establish positivity on all the remaining complement.

## 1. Original signed form and true adjacent residual collars

The physical original zero-extended signed Weil quadratic form is **unchanged**:
\[
Q[f]=J[f]+c_{\rm arch}\|f\|^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)
+2|\langle f,\cosh(x/2)\rangle|^2
-2|\langle f,\sinh(x/2)\rangle|^2,
\quad
J[f]=\int_0^\infty\frac{e^{-u/2}}{1-e^{-2u}}\|Zf-\tau_u Zf\|_2^2du.
\]
Here \(I=[-11/10,11/10]\), \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\); all prime powers, genuine nonlocal digamma and both signed poles remain. PS15 proves the full form domain is stable under sharp interval projections, by truncating the original positive kernel, bounding two-sided Carleman cross, and taking monotone limits.

Let \(U\) be the exactly original source-adjusted eight-window positive subsystem of PS22, with \(A_U>19/20\) on its complete original domain. Let \(P\) be PS15's positive thirteen-interval source block \(A_P>323/1000\). Let the uncovered complementary support be \(Z=C\setminus U\), \(C=I\setminus P\).

Choose \(b=5/128\), \(\epsilon=1/2048\). The new **TWO reflected residual collars**
\[
\boxed{
X_-=[-b-\epsilon,-b],\qquad
X_+=[b,b+\epsilon]
}
\]
are wholly in \(Z\), touch the original eight-window intervals \(-J=[-b,-1/32]\) and \(J=[1/32,b]\), respectively, and are disjoint from all other U and source intervals. Each is **adjacent** to U at a real physical point; their mixed arch kernel includes a genuine singular \(1/(2(s+t))\) **noncompact Carleman interaction**. Unlike PS19–PS21's separated physical windows, this is a direct test of the noncompact interface that has been retained as a principal obstruction since PS04.

All \(13\cdot2\cdot7\cdot2=364\) actual source-to-collar original prime shifts are strictly separated. Of the \(8\cdot2\cdot7\cdot2=224\) eight-window-to-collar original prime-shift possibilities, exactly **TWO touch a boundary without positive-measure overlap**: \(X_- -\log2\) ends where \(-J-\log2\) begins and \(X_++\log2\) begins where \(J+\log2\) ends. This follows by **exact algebra of the interval definitions**, not merely tolerance arithmetic. All other 222 incidences are strictly separated. Thus all original \(P/X\) and \(U/X\) prime translation form cross terms vanish almost everywhere, while every other genuine original physical prime interaction **in the remaining complement** is retained.

## 2. Real original collar local energy survives full source response

For ANY complex-valued admissible function supported on a single collar of width \(\epsilon\), its original arch difference-energy satisfies
\[
J[f]\ge2\|f\|^2\int_{\epsilon}^\infty k(u)\,du.
\]
The source-exact positive original expansion \(k(u)=\sum_{m\ge0}e^{-(2m+1/2)u}\) and rational Bernoulli lower \(e^{-x}\ge(1-x/32)^{32}\) certify with **256 exact rational original terms**
\[
T_{256}
=2\sum_{m=0}^{255}
\frac{(1-(2m+1/2)\epsilon/32)^{32}}{2m+1/2},
\qquad
\boxed{c_{\rm arch}+T_{256}>4.}
\]
This retains original nonlocal arch energy, not a finite-mesh surrogate. The two collars have no internal prime autocorrelation: their mutual distance is \(\ll\log2\), and each is shorter than \(\log2\). Their mutual arch kernel is nonzero, but has operator bound
\[
\|B_{\rm arch,X_-X_+}\|
\le\epsilon\left(1+\frac1{4b}\right)<1/250.
\]
The full actual negative odd pole costs \(<1/1000\) times mass on their union; the original positive even pole is dropped only in a safe *lower* bound.

The **complete thirteen-source/collar arch coupling** consists of 26 physically separated kernel rectangles and is Hilbert–Schmidt:
\[
\|B_{\rm arch,PX}\|_{\rm HS}^2
\le \delta\epsilon\sum_{r\in\mathscr O}\sum_{\pm}
\left(1+\frac1{2\,\operatorname{dist}(I_r,X_\pm)}\right)^2
<\left(\frac3{100}\right)^2,
\quad\delta=11/5-\log9.
\]
Both original signed pole source/collar crosses are paid with \(<1/60\) operator norm. All seven source/collar prime powers vanish solely by the explicitly checked original support geometry. Hence
\[
\boxed{\|B_{PX}\|<1/20.}
\]
The TRUE source energy inverse \(A_P^{-1}\) therefore induces an actual signed Schur subtraction
\[
0\le T_{C}|_X=B_{PX}^*A_P^{-1}B_{PX},
\qquad
\|T_C|_X\|<\frac{(1/20)^2}{323/1000}<1/100.
\]
With all actual terms paid, the first source-eliminated original collar form obeys
\[
\boxed{
\mathfrak S_C[x]>\beta\|x\|^2,\quad
\beta=4-\frac1{250}-\frac1{1000}-\frac1{100}
=\frac{797}{200}=3.985
}
\]
for EVERY admissible collar-supported vector, not merely a finite selection of functions.

## 3. Pay the NONCOMPACT eight-window/collar arch seam and all source-mediated cross

The **entire** original eight-window/collar arch mixed operator decomposes into two genuine adjacent seam corner kernels and the 14 other physically separated kernel rectangles.

Each adjacent kernel satisfies \(k(s+t)\le1/[2(s+t)]+1\). The sharp classical Carleman operator norm for \(1/(s+t)\) is \(\pi\); the constant-one kernel has norm \(\sqrt{\epsilon L}\), \(L=1/128\). The two adjacent edge operators act on **orthogonal input/output window pairs**, hence their combined norm is the *maximum*, not their sum:
\[
\boxed{
\|B_{\rm arch,adjacent}\|
\le\pi/2+\sqrt{\epsilon L}
<11/7+1/512.
}
\]
All remaining 14 original arch kernels are retained and bounded by the exact support-distance Hilbert–Schmidt sum
\[
\boxed{
\|B_{\rm arch,nonadjacent}\|_{\rm HS}<1/30.
}
\]
The complete original correctly signed even/odd pole U/X cross has norm \(<1/40\). No genuine U/X prime overlap remains (including the two exact boundary-touching cases).

Crucially **eliminating P creates a NONZERO induced U/X source response**. It is not discarded:
\[
\|1_U T_C1_X\|
\le\|B_{PU}\|\|A_P^{-1}\|\|B_{PX}\|
<\frac{37}{100}\frac{1000}{323}\frac1{20}
<\frac3{50}.
\]
The WHOLE source-eliminated eight-window/collar mixed operator is therefore
\[
\boxed{
\|\widetilde B_{UX}\|
<11/7+1/512+1/30+1/40+3/50
<\frac{17}{10}=1.7.
}
\]
The raw cross **is not compact** in physical \(L^2\): opposing weakly-null step indicators at either real shared boundary yield the original \(-\log2\) arch seam limit, while all prime form crosses vanish and signed pole plus compact source response vanish in the limit. PS23 therefore does NOT hide or remove the principal Carleman interface singularity.

## 4. Main result A: true ORIGINAL twice-eliminated residual Schur is positive ACROSS the physical seams

The actual previously source-eliminated U block has \(A_U>19/20\), including all eight original signed windows and their genuine source response. Thus its complete positive energy-dual *second* subtraction on the collars is bounded by
\[
0\le\langle x,\widetilde B^*A_U^{-1}\widetilde Bx\rangle
<\frac{(17/10)^2}{19/20}\|x\|^2
<\frac{61}{20}\|x\|^2.
\]
The **actual ORIGINAL twice-eliminated residual Schur on both collars**, as defined in PS22,
\[
\mathfrak S_Z[x]=Q[x]-\langle x,T_Cx\rangle
-\langle x,\widetilde B^*A_U^{-1}\widetilde Bx\rangle,
\]
therefore obeys
\[
\boxed{
\mathfrak S_Z[x]
>\left(\frac{797}{200}-\frac{61}{20}\right)\|x\|^2
=\frac{187}{200}\|x\|^2
>\boxed{\frac9{10}\|x\|^2}.
}
\]
**This positive sign applies to EVERY admissible vector on the two collars, despite their direct NONCOMPACT Carleman coupling to the previously eliminated eight-window subsystem.** This is a materially different result from positivity of another detached subspace.

## 5. Main result B: one coupled TEN-window positive original signed Schur module

For arbitrary admissible \(u\in U\), \(x\in X\), the actual source-eliminated signed Schur has
\[
\mathfrak S_C[u+x]
>\alpha\|u\|^2+\beta\|x\|^2-2\gamma\|u\|\|x\|,
\quad
\alpha=\frac{19}{20},\quad\beta=\frac{797}{200},\quad\gamma=\frac{17}{10}.
\]
For proposed strict gap \(\mu=1/8\), exact rational arithmetic checks
\[
\boxed{
\alpha-\mu>0,\quad \beta-\mu>0,\quad
(\alpha-\mu)(\beta-\mu)-\gamma^2>0.
}
\]
Therefore the COMPLETE original source-eliminated Schur on the **single reflection-invariant TEN-window combined carrier** satisfies
\[
\boxed{\mathfrak S_C[u+x]>\frac18\|u+x\|^2}.
\]
All three genuine original internal \(\log2\) U links, all original source energy response, noncompact U/X digamma and correctly signed original poles are preserved. The strict ten-window bound is **local**, NOT a uniform positive gap for the global complement: RC315 already imposes a global even gap ceiling around 0.042.

## 6. Remaining acceptance obligation

Although two real noncompact seams have now been crossed with an accepted analytic *within-scope* positive estimate, many original physical U/rest and source/rest interfaces and all seven prime translations survive in the uncovered complement. This checkpoint proves neither \(\mathfrak S_Z\ge0\) on the FULL uncovered residual nor complete original Weil positivity.

**PS24** should extend this noncompact-seam absorption mechanism to a coherent collection of adjacent collars/regions with rigorously controlled coupling and evaluate the *actual remaining* signed residual Schur. The native CC27 D-Riesz domain/norm identification and independent functional-analytic audit remain mandatory before promoting canonical W-ODD-NEG, W-EVEN-FORM, full Weil positivity or RH.

**Replay:** \`python3 scripts/validate_rpb108_ps23_carleman_seam_collars.py\` reruns PS22→...→source-pinned RC315, verifies all 588 source/U collar signed prime configurations INCLUDING the two exact measure-zero boundary touches, all 26 source arch and 14 nonadjacent U arch distance bounds, two original signed poles, 256-term exact rational original digamma lower, noncompact two-Carleman seam norm, both true inverse responses, nested collar positivity, TEN-window determinant and open-governance custody. Passing CI verifies source-rational constant gates; independent proof review remains outstanding.
