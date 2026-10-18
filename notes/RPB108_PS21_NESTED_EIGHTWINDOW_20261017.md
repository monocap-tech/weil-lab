# PS21 — Genuine two-level residual positivity and a coupled eight-window original signed Schur module

**October 17, 2026 · W-PHYSICAL-SHIFT · stacked after PS20.** The canonical W-ODD-NEG, W-EVEN-FORM, original Weil full positivity, CC27 D-Riesz norm/domain bridge, and RH all remain **OPEN**.

PS21 responds directly to PS20's missing interface obligation. It does **not** merely certify another positive window before coupling. It establishes strict original **second-level residual Schur positivity after eliminating BOTH the 13-source block and the original six-window block**, on a new genuinely prime-linked two-window subspace. It then recombines that new subspace with PS20's complete six-window module to obtain a **single eight-window, source-eliminated, reflection-invariant positivity theorem**, with all W/Q interactions paid. The complete remaining residual outside these eight windows is still unproved positive.

## Original form and the exact new physical support

Keep precisely the zero-extended physical signed original Weil form of PS01–PS20:

[
Q[f]=J[f]+c_{arch}\|f\|^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)
+2|\langle f,\cosh(x/2)\rangle|^2
-2|\langle f,\sinh(x/2)\rangle|^2,
]
where (J[f]=\int_0^\infty e^{-u/2}(1-e^{-2u})^{-1}\|Zf-\tau_uZf\|^2du) and (c_{arch}=-\gamma-\pi/2-3\log2-\log\pi). All original physical prime and signed pole interactions remain.

Let (P) be PS15's exact 13-interval source projector. Let (Wsubset C=1-P) be PS20's six-window reflection-invariant source complement module, and (R=C\setminus W) its genuine uncovered remainder. Write (L=1/128) and \(\ell_2=\log2\). Define

[
\boxed{Q_+=[\ell_2/2-L/2,\,\ell_2/2+L/2],\quad Q_-=-Q_+}.
]

Both windows lie strictly in the ACTUAL remaining physical support (R), with minimum distance (>1/20) from every original source interval and (>1/8) from every existing PS20 window. By construction \(Q_-+\log2=Q_+\) **exactly**, so this new two-window subsystem contains a genuine, nonzero signed (log2) prime translation operator of norm (w_2=log2/sqrt2<1/2). All other n=3,4,5,7,8,9 internal prime shifts are absent by outward original-source logarithm enclosures.

The source-rational validator also checks **every one of the (2(13+6)\cdot7\cdot2=532) genuine prime translations** connecting the two new windows to either the 13-source block P or the original six-window module W. Each shifted interval is STRICTLY separated from its target, with source clearance >1/20 and W clearance >1/100. Hence the *original physical prime portions* of (B_{P,Q}) and (B_{W,Q}) vanish **only by proven geometry**. The full prime operator on the rest of the complement is NOT discarded.

## Direct original form on the new two-window carrier

Sharp single-window restrictions preserve the original logarithmic form domain by the same truncated-kernel, bounded Carleman and monotone-convergence proof used in PS15/PS20. For arbitrary separately admissible components (q=q_-+q_+), the true original 64-term positive digamma kernel tail gives (J[q_\pm]+c_{arch}\|q_\pm\|^2>11/5\|q_\pm\|^2).

The real original (log2) internal prime interaction contributes operator norm (w_2<1/2). The nonzero archimedean cross between the two separated windows is retained and has norm (<1/70). The complete actual negative odd pole on their union costs (<1/80) mass; the original positive even pole is dropped only in a safe lower estimate.

Thus for all nonzero such (q),
[
\boxed{
Q[q]>\left(\frac{11}{5}-\frac12-\frac1{70}-\frac1{80}\right)\|q\|^2.
}
]

## FIRST: retain the entire original 13-source response

The full original source-to-new-window arch kernel uses all 26 source/new physical interval pairs and obeys an exact outward-rational Hilbert–Schmidt estimate
[
\|B_{P,Q;arch}\|_{HS}^2<\left(\frac{11}{100}\right)^2.
]
Both actual signed original rank-one source poles contribute norm (<9/100), and ALL 364 original source-to-Q prime shifts are geometrically absent. Hence
[
\|B_{P,Q}\|<\frac15.
]
The true original source operator includes all 19 source-internal prime edges and is positive (A_P>323/1000) (PS16). Consequently the **actual complete signed source Schur penalty** on the new windows is
[
\langle q,T_Cq\rangle
=\|A_P^{-1/2}B_{P,Q}q\|^2
<\frac{(1/5)^2}{323/1000}\|q\|^2
<\frac18\|q\|^2.
]
No physical source-inverse cross terms are neglected.

## SECOND: retain and eliminate the entire original six-window module

The full real W/new-window mixed arch operator has all 12 nonzero separated physical kernels, with
[
\|B^Q_{W,Q;arch}\|_{HS}^2<\left(\frac1{14}\right)^2.
]
The two correctly signed W/new-window original poles contribute (<1/10); all 168 genuine W/new-window prime translations were checked disjoint. Source elimination induces the additional NONZERO compact cross
[
\|1_W T_C1_Q\|
\le \|B_{P,W}\|\,\|A_P^{-1}\|\,\|B_{P,Q}\|
<\frac{31}{100}\frac{1000}{323}\frac15.
]
The complete signed *already-source-eliminated* mixed operator is therefore
[
\boxed{
\|\widetilde B_{W,Q}\|
<\frac1{14}+\frac1{10}+\frac{31}{100}\frac{1000}{323}\frac15
<\frac38.
}
]
This retains the nonzero physical arch/pole cross and ALL source-mediated W/Q interactions: **the primes alone vanish** by geometry.

PS20 proved that the true complete source-eliminated operator on W satisfies (A_W>7/6), including its two real original signed (log2) internal links. The second-level signed Schur correction for the new Q carrier obeys
[
\|\widetilde B_{W,Q}^*A_W^{-1}\widetilde B_{W,Q}\|
<\frac{(3/8)^2}{7/6}
=\frac{27}{224}<0.121.
]

## MAIN result A: TRUE signed second-level residual Schur positivity

For EVERY nonzero original form-admissible (q) supported on both real new windows,
[
\boxed{
\begin{aligned}
\mathfrak S_R[q]
&=Q[q]-\langle q,T_Cq\rangle
-\langle q,\widetilde B_{W,Q}^*A_W^{-1}\widetilde B_{W,Q}q\rangle\\
&>\Big(\frac{11}{5}-\frac12-\frac1{70}-\frac1{80}
-\frac18-\frac{27}{224}\Big)\|q\|^2\\
&>\frac75\|q\|^2.
\end{aligned}
}
]
This is the **actual signed nested residual after eliminating two entire infinite-dimensional positive blocks**, not an independent-window calculation. It has one genuine signed (log2) prime edge and both parities.

## MAIN result B: genuine joint eight-window original Schur positivity

For every admissible (w\in W) and (q\in Q), the exact nested completion of squares gives
[
\mathfrak S_C[w+q]
=\|A_W^{1/2}(w+A_W^{-1}\widetilde B_{W,Q}q)\|^2
+\mathfrak S_R[q].
]
The operator (A_W^{-1}\widetilde B_{W,Q}) has norm (<(6/7)(3/8)=9/28). Therefore the triangular map ((w,q)\mapsto(w+A_W^{-1}\widetilde B_{W,Q}q,q)) has inverse norm (<37/28). Since the two positive diagonal lower bounds are (7/6) and (7/5), respectively, the original complete **source-eliminated** signed Schur obeys
[
\boxed{
\mathfrak S_C[w+q]
>\frac76\left(\frac{28}{37}\right)^2
(\|w\|^2+\|q\|^2)
>\frac23\|w+q\|^2.
}
]
Thus a **single infinite-dimensional eight-window reflection-invariant combined carrier** is certified positive, including its three genuine signed (log2) prime links, all cross-window arch and poles, and the full thirteen-source inverse. This is a real coupled-subsystem extension of PS20, not just a separate new positivity island.

## What remains OPEN

All functions outside the eight-window module are still in the original complementary residual and couple to it. The nested residual on this entire remainder is NOT proved PSD and is not guaranteed by any of the local margins above. The source-to-rest and window-to-rest noncompact arch Carleman seams and all original seven prime translations persist; the full energy-dual response must be retained. The PS16 original RC315 even small-gap ceiling (<0.041) continues to apply globally, and the (>2/3) eight-window margin is emphatically *local*, not a candidate global lower bound.

**Next PS22:** redo the exact source-aware Schur on the full uncovered complement after eliminating the now-positive eight-window carrier, and quantify all new boundary and prime/source couplings. Only a genuine complete residual PSD or valid negative witness can resolve whole original Weil positivity. Native CC27 D-Riesz attachment and independent proof review remain necessary.

**Replay:** `python3 scripts/validate_rpb108_ps21_nested_eightwindow.py`. It runs PS20→PS19→...→RC315, checks all 532 source/W-to-new prime shifts, 26 source/new and 12 W/new arch distances, two signed poles, original 64-term arch tail and genuine internal log2 link, full source inverse and six-window inverse, both nested coercivity margins, parity symmetry and no-RH-promotion governance.
