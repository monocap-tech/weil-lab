# SM05 — a genuine original supported inverse certificate for the odd pole and one continuous negative packet

**Canonical obligation:** W-ODD-NEG (still OPEN).  
**Parent:** SM04 integrated as PR #131, at research head 9f62862a254a497c74e76b08592fe14d0facd28a.  
**Evidence status:** full original supported 16-feature, two-source exact-rational inverse certificate passed first GitHub Actions source replay `39001092441` at commit `268d49e149ea3218c1b17d609c649a7c17814c`; streamlined final-head source/obligation integration remains a separate gate. No full odd-frequency continuum, Stage I or RH claim.

## 1. Changing the kind of object certified

SM03 and SM04 showed that neither SI29's fixed C14 nor *any* rank ≤14 correction to the scalar reference floor \(\kappa=10^{-3}\) can dominate the **entire** negative-frequency operator. These are barriers to method classes, not obstructions to the true positive \(A_o\).

SM05 instead tests a genuinely coupled *supported inverse* on the original \(H_o=L^2([-11/10,11/10])_{\rm odd}\): the negative pole \(s(x)=\sinh(x/2)\) **together with** SM03's actual negative-frequency continuous Jensen packet
\[
g_-(x)=\frac1{2\rho}\int_{c-\rho}^{c+\rho}\sin(2\pi\xi x)\,d\xi,
\quad c=147/40,\quad \rho=3/100.
\]
SM03 previously certified the original seven-prime multiplier \(m(\xi)<-7/5\) on the whole reflected band. Thus
\[
K_{{\rm freq},o}\succeq\gamma_-|g_-\rangle\langle g_-|,
\qquad \gamma_-=4\rho\cdot 7/5=21/125.
\]
The new gate is a strict *sufficient* inequality for the **selected packet plus pole**
\[
\boxed{A_o\succeq 2|s\rangle\langle s|+\frac{21}{125}|g_-\rangle\langle g_-|.}
\]
This is not full odd Weil positivity: the rest of the original negative-frequency continuum remains unsigned and unabsorbed.

## 2. A physically supported sixteen-feature positive minorant

Take nine retained true signed Jensen means from SI29's original sources (four SI21 means, two SI23 means, and 2.10, 2.32, 3.40), and append seven original signed positive intervals
\[
\begin{array}{c|c|c}
c_j&\rho_j&\delta_j\\\hline
3.80&.019&.7\\
3.25&.019&2.2\\
3.45&.019&2.7\\
4.15&.019&.5\\
3.85&.019&2.4\\
4.65&.019&.5\\
5.00&.019&1.2
\end{array}
\]
all reflected, pairwise disjoint from the nine retained positive intervals and from each other. The validator must certify \(m(\xi)>\kappa+\delta_j\) **at every real point** of each new interval, with the SI06/28 original seven-prime rational phase bounds, derivative remainder, and original digamma monotonicity.

The true physically supported Jensen mean for each is
\[
g_j(x)=\sin(2\pi c_jx)\,\mathrm{sinc}(2\pi\rho_jx),
\quad \Gamma_j=4\rho_j\delta_j.
\]
Original signed frequency positivity and Bessel/Jensen yield
\[
A_o\succeq C_{16}:=\kappa I+\sum_{j=1}^{16}\Gamma_j|g_j\rangle\langle g_j|.
\]
This keeps the true infinite-dimensional **support** and the complete positive reference, not a whole-line inverse reciprocal or a kernel truncated without a residual.

## 3. Full mixed original supported inverse — correct-sign upper matrix

Let \(G=(g_1,\ldots,g_{16})\), \(V=(s,g_-)\). The actual supported inverse response
\[
V^*A_o^{-1}V\preceq V^*C_{16}^{-1}V
\]
is bounded by a **true signed physical 16-by-16 Gram**, including all cross terms. Put \(H=G^*G\), \(Q=G^*V\), \(P=V^*V\), \(M=\Gamma^{-1}+H/\kappa\succ0\). Woodbury gives
\[
V^*C_{16}^{-1}V=\kappa^{-1}P-\kappa^{-2}Q^*M^{-1}Q.
\]
For any rational two-column trial \(Z\), completion of squares yields the rigorously correct-sign matrix upper
\[
\boxed{
V^*A_o^{-1}V\preceq
\kappa^{-1}P-
\kappa^{-2}(Q^*Z+Z^*Q-Z^*MZ)
=:\widehat U.
}
\]
Every entry of \(P,Q,H\) is enclosed on the **actual physical carrier** using exact rational sine/sinh overlaps plus rational composite Simpson errors. The midpoint solve only chooses rational \(Z\); its numerical precision is not a proof. The complete interval calculation pays all 256 positive Gram entries and all 32 mixed source overlaps with signs intact. The positive residual \((Q-MZ)^*M^{-1}(Q-MZ)\) is not incorrectly dropped from an *upper* bound.

The normalized two-source Birman–Schwinger matrix is
\[
D\,V^*A_o^{-1}V\,D,\qquad D=\mathrm{diag}(\sqrt2,\sqrt{21/125}).
\]
Because \(\sqrt{42/125}<3/5\), exact rational Gershgorin row bounds can certify its norm strictly below one without irrational acceptance. This is the genuine original two-source **coupling** neglected by pole-only estimates.

## 4. Exact-rational successful source replay, not merely a numerical screen

A preliminary floating-point supported Gram screen with true Jensen means suggests a 16-feature two-source matrix near
\[
\begin{pmatrix}0.9140&0.00783\\ 0.00783&0.8854\end{pmatrix}
\]
after the \(D\) normalization. The screen was **not** used as the certificate. GitHub Actions run `39001092441` subsequently passed the complete 16-feature exact-rational source test, including all seven original whole positive-band margins and the 16-by-16 and 16-by-2 signed physical Gram intervals. It gives the following outward upper endpoints for the **unscaled** two-source inverse matrix (V^* A_o^{-1} V):

\[
\widehat U_{00}<0.458573661,\qquad
|\widehat U_{01}|<0.017429924,\qquad
\widehat U_{11}<5.277776913.
\]

The rigorous rational Gershgorin weighted row ceilings are
\[
2\widehat U_{00}+\frac35|\widehat U_{01}|<0.927606<1,\qquad
\frac{21}{125}\widehat U_{11}+\frac35|\widehat U_{01}|<0.897125<1.
\]

The maximum original positive-composite-Simpson remainder was below (6.418\cdot10^{-7}); the negative packet remainder was below (4.012\cdot10^{-8}). Final acceptance is conditioned on replaying the *same theorem* at the final PR head, with the signed-band optimization independently validated. In particular, these are genuine supported-inverse upper enclosures, **not** the numerical screen.

## 5. What remains after a passing SM05

This result, if certified, would show the **full original positive operator**, via a correctly supported lower reference, defeats the original odd pole and *at least one actual continuous negative-frequency Jensen packet in combination*, for every odd physical input. It would be a genuine joint-signed inequality, but the difference
\[
K_{{\rm freq},o}-\frac{21}{125}|g_-\rangle\langle g_-|
\succeq0
\]
still needs a quantitative finite-plus-infinite bound, and there are other signed-negative intervals. No inference from one packet to the full continuum is permitted.

Replay: \`python scripts/validate_rpb108_sm05_two_source_original_inverse.py\`; valid source scope and checked CI are distinct from independent review or Lean formalization.
