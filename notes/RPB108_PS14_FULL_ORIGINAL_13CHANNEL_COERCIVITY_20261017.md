# PS14 — Coercivity of the full original signed Weil form on the thirteen-channel carrier

Scoped structural certificate, stacked after PS13. Canonical W-ODD-NEG and W-EVEN-FORM remain OPEN. All claims here concern the original physical source form on a restricted, infinite-dimensional support carrier—not positivity of the entire Weil form or RH.

## 1. The full signed original quadratic form, not merely IMS

Set \(B=11/10\), \(\delta=2B-\log9\), \(I=[-B,B]\). The actual SI10/CC27 physical source form is
\[
Q[f]=J[f]+c_{\rm arch}\|f\|^2-2\sum_{n\in N}w_n\Re C_f(\log n)
+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2,
\]
where \(N=\{2,3,4,5,7,8,9\}\), \(w_n=\Lambda(n)/\sqrt n\),
\(J[f]=\int_0^\infty k(u)\|Zf-\tau_uZf\|^2du\), \(k(u)=e^{-u/2}/(1-e^{-2u})\),
\(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\), and \(c=\cosh(x/2),s=\sinh(x/2)\).

Let the EXACT PS10 source intervals be
\[
I_r=[-B+\log r,-B+\log r+\delta],
\quad
r\in\mathscr O=\{1,9,2,3,4,5,7,8,9/2,9/4,9/5,9/7,9/8\}.
\]
They are 13 disjoint original physical intervals. For a function supported in their union, write \(f=\sum_{r\in\mathscr O}f_r\), with each \(f_r\) in the original logarithmic form domain. The latter is justified by PS06's form multiplier method (or via sharp interval projection and bounded disjoint-interface cross forms); for this checkpoint we explicitly require *separately form-admissible* channel pieces, rather than asserting an unsupported sharp-projection domain theorem.

These thirteen intervals contain the **whole** PS10 source-channel carrier, including both thin edges and 11 actual interior windows. The problem here is the **original unshifted \(Q\)** restricted to their full 13-channel infinite-dimensional direct sum. Unlike PS10's IMS correction, its prime part contains extra interior-interior interactions.

## 2. Exact nineteen-edge original prime operator

For any two distinct channel offsets \(r<t\), a nonzero original prime correlation between their intervals at the exact shift \(\log n\) is possible if and only if
\[
\boxed{t/r=n\in N.}
\]
To prove the converse, enumerate the FINITE rational ratios \(t/(rn)\): for every non-equality, source-exact rational checks verify \(t/(rn)\ge101/100\) or \(t/(rn)\le100/101\). The rational log enclosure \(\log(101/100)>\delta\) excludes EVERY near-miss translation for entire intervals of width \(\delta\). Thus **no unexplained almost-resonances** are discarded.

Exactly **19** undirected original prime edges remain, compared with the **13** edges in the PS10 *IMS remainder*. The additional six are genuine interior-interior interactions. In the unitary identification \(\bigoplus_rL^2(I_r)\cong L^2([0,\delta];\mathbb C^{13})\), the **entire original signed prime form** is the constant fiber multiplication operator \(M_Q\) whose offdiagonal entries are \(-(w_n)\) on ratio-\(n\) edges and zero otherwise. This is not the PS10 5-mode IMS matrix.

Let \(W=|M_Q|\) denote its entrywise absolute-value matrix. The original-source rational calculation establishes
\[
\boxed{\max_i\sum_j(W^2)_{ij}<\frac{121}{25},\qquad
\|M_Q\|=\|W\|<\frac{11}{5}.}
\]
The second implication uses self-adjointness, the spectral-radius identity \(\|W\|^2=\rho(W^2)\), and \(\rho(W^2)\le\|W^2\|_\infty\). This is a certified 13-by-13 **signed original prime operator bound** over its entire continuous \(L^2\) fiber, not an approximate 13-mode finite-rank reduction of \(L^2(I)\).

## 3. Archimedean diagonal energy and off-channel control

Every channel interval has length \(\delta<\log2\). For any separately form-admissible \(f_r\), every prime diagonal correlation vanishes, and the original arch difference energy has
\[
J[f_r]\ge2\int_\delta^\infty k(u)du\cdot\|f_r\|^2.
\]
From the **original** nonnegative kernel series \(k(u)=\sum_{m\ge0}e^{-(2m+1/2)u}\), Bernoulli's exact bound with exponent 32 gives
\[
T_{64}=2\sum_{m=0}^{63}
\frac{[1-(2m+1/2)\delta/32]^{32}}{2m+1/2}
>8.055,\qquad
\boxed{c_{\rm arch}+T_{64}>\frac83}.
\]
All inequalities are certified by outward-rational original-source arithmetic.

The nonlocal arch cross operator between distinct channel intervals has kernel \(-k(|x-y|)\). The exact minimum offset gap is \(>1/10\); therefore their physical point-to-point separation exceeds
\(g=1/10-\delta>1/10-1/350=17/175\).
For all \(u>0\), the original \(k(u)\le1/(2u)+1\). Schur's test over the other 12 narrow channels gives
\[
\boxed{
\|\mathcal A_{\rm cross}\|
<12\delta\left(1+\frac1{2g}\right)
<\frac14.
}
\]
The diagonal arch energy is kept fully in the local \(J[f_r]\); only the genuine cross-window portion is bounded.

## 4. Both correctly signed original poles and the resulting positivity

The positive even pole can be discarded for a LOWER bound, but the original odd pole must be retained and paid:
\[
-2|\langle f,s\rangle|^2
\ge-2\|1_{\cup_r I_r}s\|^2\|f\|^2
\ge-26\delta\sinh^2(B/2)\|f\|^2
>-\frac1{30}\|f\|^2.
\]

Putting together the original arch self-energy, all NINETEEN original prime channel edges, the nonlocal arch cross and negative signed odd pole gives
\[
\begin{aligned}
Q[f]
&>\left(\frac83-\frac{11}{5}-\frac14-\frac1{30}\right)\|f\|^2\\
&=\frac{11}{60}\|f\|^2>\boxed{\frac16\|f\|^2}.
\end{aligned}
\]
Therefore every nonzero \(f\) with independently form-admissible components supported in the actual thirteen PS10 source intervals satisfies
\[
\boxed{Q[f]>\frac16\|f\|_2^2.}
\]
This is an **infinite-dimensional full original signed-form coercivity theorem on the thirteen-source carrier**, with all original prime-power interactions inside that carrier, original arch and both pole terms. This is stronger than PS13's one-window result. It does NOT establish that an arbitrary interior \(\beta f\) belongs to this restricted carrier, nor control cross terms with its orthogonal complement.

## 5. Correct frontier after PS14

The PS10 source carrier is now known to be strictly positive even for the entire original \(Q\), not merely for the IMS correction. But PS04/PS11 already established that **physical boundary coupling is noncompact and source-channel projection does not reduce the full \(Q\)**. Hence this is not a global Schur certificate.

**PS15** should attach the full signed edge/source-to-complement coupling in the true original graph-energy norm and certify the complementary signed Schur gap; alternatively derive a native CC27 D-Riesz domain identification and useful computable low-energy Gram estimate. The present certificate does not verify full unshifted Weil positivity, W-ODD-NEG, W-EVEN-FORM, F4 or RH.

Replay: \`python3 scripts/validate_rpb108_ps14_full_original_13channel.py\` checks all exact-rational 13 offsets, 19 original prime edges including the six missing IMS-only edges, every near-miss original shift gap, \(W^2\) row norms, 64-term arch source tail, original signed odd-pole allowance and canonical governance. CI verifies rational gates for the analytic theorem; independent mathematical review is outstanding.
