# SM06 — first orthogonal signed-negative frequency moment coupled to the odd pole

**Active original-math obligation:** W-ODD-NEG, still **OPEN**.  
**Parent:** merged SM05 and its custody reconciliation (PRs #132–133).  
**Status:** passed original exact-rational N=16 three-source source run `39004369440`, optimized N=8 *complete uniform-band* run `39005014089`, and independent infinite-tail job `117314615797`. Full variable original negative multiplier remains open.

## 1. Exact new operator term, not a new point-sample mode

Let \(H_o=L^2([-B,B])_{\rm odd}\), \(B=11/10\), and let \(A_o\) be the original physically supported positive-frequency operator of SM05 with scalar floor \(\kappa=1/1000\). Retain the genuine original signed negative-frequency interval
\[
J_-=[3.645,3.705],\quad c=147/40,\quad r=3/100,
\quad m(\xi)<-7/5\quad(\xi\in J_-\cup-J_-).
\]
SM03 certified the *entire continuum* in this interval, not just its midpoint.

Write \(u=(\xi-c)/r\), \(h_\xi(x)=\sin(2\pi\xi x)\) and \(E=\frac12\int_{-1}^{1}\). Define the exact physical odd vectors
\[
g_0=E[h_{c+ru}]=\sin(2\pi cx)\operatorname{sinc}(2\pi rx),\qquad
g_1=3E[u\,h_{c+ru}].
\]
These are *genuinely distinct* Legendre frequency moments. The first moment is not estimated by a derivative sample and is retained as an actual continuous signed integral.

Bessel/Parseval applied to the orthonormal frequency functions \(1,\sqrt3u\) establishes the original signed physical **Loewner lower bound**
\[
\begin{split}
K_{{\rm freq},o}
&\succeq 2\delta\int_{J_-}|h_\xi\rangle\langle h_\xi|d\xi\\
&\succeq 4r\delta |g_0\rangle\langle g_0|
+\frac{4r\delta}{3}|g_1\rangle\langle g_1|\\
&=\frac{21}{125}|g_0\rangle\langle g_0|
+\frac7{125}|g_1\rangle\langle g_1|,
\quad\delta=7/5.
\end{split}
\]
The source \(s(x)=\sinh(x/2)\) retains its coefficient \(2\). This proof is entirely on the physically supported odd carrier.

## 2. Three-source supported inverse certificate

Reuse SM05's original signed-positive sixteen genuine Jensen means and coefficient matrix \(\Gamma\), whose entire frequency bands have been certified in SI21–SI29 and SM05. The same positive lower reference
\[
C_{16}=\kappa I+G\Gamma G^*\preceq A_o
\]
is valid independently of which source vectors are tested. This avoids incorrectly spending positive-frequency mass twice.

Now define the three-column genuine source operator
\[
V=(s,g_0,g_1),\quad
D=\operatorname{diag}(\sqrt2,\sqrt{21/125},\sqrt{7/125}),
\]
and the supported Gram matrices \(H=G^*G\), \(Q=G^*V\), \(P=V^*V\), \(M=\Gamma^{-1}+H/\kappa\succ0\).
The matrix Woodbury/variational identity yields for **any** rational 16-by-3 dual trial \(Z\)
\[
V^*A_o^{-1}V
\preceq V^*C_{16}^{-1}V
\preceq\kappa^{-1}P-\kappa^{-2}
(Q^*Z+Z^*Q-Z^*MZ).
\]
The positive missing dual residual \((Q-MZ)^*M^{-1}(Q-MZ)\) is not dropped as a negative error; the displayed sign is the upper bound.

The exact-rational validator encloses all physical entries of \(H,Q,P\), including **all three cross-source entries** \((s,g_0)\), \((s,g_1)\), \((g_0,g_1)\), using original supported sine/sinh intervals and signed composite Simpson enclosures. The new degree-one moment uses eight rational Simpson subpanels; its fourth derivative is bounded by
\[
3(4\beta^3+\beta^4),\quad\beta=2\pi_{\rm hi}rB,\quad
\varepsilon_1\le\frac{3(4\beta^3+\beta^4)}{180}(2/8)^4.
\]
The accepted upper bound is not built from an unsupported whole-line reciprocal or a finite-cutoff inverse. Crucially, the entrywise intervals enclose the entries of the **explicit Loewner-majorant matrix**, not the entries of the true supported inverse response; the true response is dominated by that majorant in PSD order.

The actual real symmetric normalized 3-by-3 Birman–Schwinger response is \(D V^*A_o^{-1}VD\). The proof encloses the entries of that explicit symmetric **Loewner majorant**, then uses rational upper weights
\[
\sqrt{2(21/125)}<29/50,\quad
\sqrt{2(7/125)}<67/200,\quad
\sqrt{(21/125)(7/125)}<97/1000
\]
for an exact Gershgorin row-sum test. The conservative row maxima must **all** be strictly below one. This establishes
\[
\boxed{
A_o\succeq2|s\rangle\langle s|
+\frac{21}{125}|g_0\rangle\langle g_0|
+\frac7{125}|g_1\rangle\langle g_1|
}
\]
on every supported odd input if the source replay passes.

## 3. Scope and needed progress

A passing first-moment test absorbs one more *independent continuous-frequency direction* than SM05, with complete cross coupling to the existing two. It is not full control of the original negative operator. The remaining signed band variance (Legendre degrees >=2), other negative-frequency bands and entire infinite remainder remain *positive terms subtracted from the true form* and must still be controlled. No inference to full odd positivity, even sector, Stage I or RH is justified.

Replay: \`python scripts/validate_rpb108_sm06_first_negative_moment.py\`.

**Acceptance:** exact rational final-head source checks, preserving all true supported domains, and a consistent canonical obligation ledger. Independent peer review or Lean formalization is separate.


## 4. A rigorously paid *infinite* Legendre remainder on this band

An additional exact rational replay, \`scripts/validate_rpb108_sm06_band_legendre_tail.py\`, proves a full infinite-dimensional tail bound for the **constant certified negative floor** \(\delta=7/5\) on \(J_-\). Let
\[
T_{J,\delta}:=2\delta\int_{c-r}^{c+r}|h_\xi\rangle\langle h_\xi|d\xi.
\]
The exact Legendre decomposition gives
\[
T_{J,\delta}=\frac{21}{125}|g_0\rangle\langle g_0|
+\frac7{125}|g_1\rangle\langle g_1|+R_{J,\ge2},
\quad R_{J,\ge2}\succeq0.
\]
For any odd physically supported \(f\), the orthogonal Legendre projection error is no greater than the affine Taylor approximation error of \(v(u)=\langle f,h_{c+ru}\rangle\). Since \(E[u^4]=1/5\) and
\(\|h''_\xi\|_2^2\le(2\pi_{\rm hi})^4(2B^5/5)\),
\[
\boxed{
0\preceq R_{J,\ge2}\preceq
\varepsilon_{J,\ge2}I,\qquad
\varepsilon_{J,\ge2}
=\frac{\delta r^5(2\pi_{\rm hi})^4 2B^5}{25}
<7\cdot10^{-6}.
}
\]
This is a **whole-infinite-tail** statement, not an order-truncation assumption. It is valid on the original supported odd Hilbert space, conditional only on SM03's inherited certified interval and the explicit Taylor/Parseval estimate.

If the certified three-source normalized BS **largest row upper** \(\theta\) satisfies \(\theta<993/1000\), then
\(A_o-2|s\rangle\langle s|-\gamma_0|g_0\rangle\langle g_0|
-\gamma_1|g_1\rangle\langle g_1|\succeq(1-\theta)A_o
\succeq(1-\theta)\kappa I>7\cdot10^{-6}I\),
which absorbs **all** of \(R_{J,\ge2}\). Hence that *conditional* gate would certify
\[
A_o\succeq2|s\rangle\langle s|+T_{J,\delta}.
\]
This controls the complete **uniform \(\delta\)-weighted component** of a genuine continuous original negative band, not the original variable \(r(\xi)\) on that band: the extra nonnegative multiplier \(r(\xi)-\delta\), as well as every other negative band, remains to be paid. The margin condition cannot be assumed merely because the three-source test gives \(\theta<1\); it must pass \(\theta<0.993\) explicitly.

**Automated composite acceptance (SM06):** the final three-source checker additionally requires \(\theta<0.993\), replays the independent exact-rational infinite-tail bound, and verifies the strict residual \(L^2\) floor \((1-\theta)\kappa-\varepsilon_{J,\ge2}>0\). Only a passing *composite* source run warrants the conclusion \(A_o\succeq2|s\rangle\langle s|+T_{J,\delta}\). The true nonconstant excess \((\kappa-m)_+-\delta\) on \(J\) and all other bands are not included.


## 5. Accepted exact-rational composite outcome

The optimized eight-panel source certificate (Actions \`39005014089\`) gives a normalized 3×3 supported odd Birman–Schwinger **Loewner-majorant**, with row upper bounds
\[
\theta_0<0.936728,\qquad\theta_1<0.900964,\qquad
\theta_2<0.019407.
\]
The independent original signed-band infinite remainder certificate (job \`117314615797\`) bounds every Legendre degree ≥2 combined by \(6.831361\times 10^{-6}\) in operator norm. Its explicitly checked composite \(L^2\) residual floor is strictly above \(5.6440\times 10^{-5}\). Therefore, conditionally on the inherited exact original seven-prime multiplier identification,
\[
\boxed{A_o-2|s\rangle\langle s|
-2\frac75\int_{3.645}^{3.705}|h_\xi\rangle\langle h_\xi|d\xi
\succeq 5.6440\times10^{-5}I}
\]
on the entire physically supported odd Hilbert space.

**Not included:** the true original negative multiplier's variable excess
\(((\kappa-m(\xi))_+-7/5)\mathbf1_{[3.645,3.705]}(\xi)\), its reflected excess, every other signed-negative band and the original global/even/RH bridge. The accepted inequality does *not* prove full original odd Weil positivity. GitHub Actions source replay is not independent peer review or Lean formalization.
