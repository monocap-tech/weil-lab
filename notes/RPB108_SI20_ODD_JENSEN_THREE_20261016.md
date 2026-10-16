# RPB108 SI20 — three-window physical Jensen minorant with certified Simpson Gram and inverse dual

**Parent:** merged SI19 at \`780927fcd0e7875bb8dd7f69897827fe32b29c99\` (PR #114).  
**Track:** Structural Investigation (SI) on the original CC27/RC312–313 signed Weil archimedean and seven-prime source. Independent of the native RC334 original high-Schur chain.  
**Standing:** explicitly certified **three-direction positive supported Loewner reference** and a small, correct-sign odd inverse comparison. Does **not** establish the actual original inverse vector, SI11's full finite-dimensional Birman–Schwinger matrix, full original Weil positivity, Stage I, F4, Lean or RH.

## 1. Actual original operator, signed frequency windows

Recall \(\kappa=1/1000\), \(B=11/10\), and on the odd physical Hilbert space \(H_o\subset L^2([-B,B])\), the positive supported operator
\[
A_o\succeq \kappa I_o+\sum_{j=1}^3\delta_j T_{J_j,o},\qquad
T_{J_j,o}=2\int_{c_j-r}^{c_j+r}|h_\xi\rangle\langle h_\xi|\,d\xi,\quad
h_\xi(x)=\sin(2\pi\xi x).
\]
The **original** signed archimedean-plus-prime Fourier multiplier \(m(\xi)\) is certified strictly greater than \(\kappa+\delta_j\) on each entire reflected interval \(J_j=\pm[c_j-r,c_j+r]\), with
\[
(c_1,c_2,c_3)=(3/10,19/25,6/5),\quad r=1/50,\quad
(\delta_1,\delta_2,\delta_3)=(27/10,5/4,17/20).
\]
The exact-rational validator checks all 128 positive-frequency subintervals in each window by the complete original signed seven-prime cosine interval routine from SI06 and an archimedean monotone Euler/digamma lower bound from SI13. It pays the entire between-midpoint error using the *all-real* prime derivative estimate \(|p'|<69\), not a floating-point grid inference. Symmetry pays the negative-frequency windows.

## 2. Exact positive Jensen lower reference — no adverse floor erosion

Set
\[
g_{c_j}(x)=\frac1{2r}\int_{c_j-r}^{c_j+r}h_\xi(x)\,d\xi
=\sin(2\pi c_jx)\operatorname{sinc}(2\pi r x)
\]
on the actual bounded physical interval, and \(\gamma_j=4r\delta_j>0\). The exact operator-variance identity from SI19 is
\[
T_{J_j,o}-4r|g_{c_j}\rangle\langle g_{c_j}|
=2\int_{c_j-r}^{c_j+r}|h_\xi-g_{c_j}\rangle
  \langle h_\xi-g_{c_j}|\,d\xi\succeq0.
\]
Thus **on the complete odd Hilbert space**
\[
\boxed{
A_o\succeq C_o=\kappa I_o+\sum_{j=1}^3\gamma_j
|g_{c_j}\rangle\langle g_{c_j}|.}
\]
There is *no* reduction in the original positive floor \(\kappa\), and no need to assign an adverse sign to an approximation remainder.

## 3. Rigorous full physical source Gram via Simpson-averaged sine basis

The exact averaged supported vectors \(g_c\) are retained in the **operator** inequality. We use normalized Simpson only as an **interval enclosure device** for their physical overlaps:
\[
\tilde g_c(x)=
\frac{h_{c-r}(x)+4h_c(x)+h_{c+r}(x)}6.
\]
The exact Simpson fourth-derivative theorem, applied at every physical \(x\), gives
\[
\sup_{|x|\le B}|g_c(x)-\tilde g_c(x)|
\le \tau:=\frac{(4\pi r B)^4}{2880}
<3\cdot10^{-6}.
\]
Indeed \(\partial_\xi^4 h_\xi(x)=(2\pi x)^4h_\xi(x)\); no unproved quadrature convergence assumption is invoked.

Both \(g_c\) and \(\tilde g_c\) are convex averages of bounded \(|h_\xi(x)|\le1\) sine functions, hence their \(L^2\)-norms are bounded by \(\sqrt{2B}\). The original odd pole satisfies \(\|s\|_2<1/2\). Consequently
\[
\begin{aligned}
|\langle s,g_c\rangle-\langle s,\tilde g_c\rangle|
&<\tfrac34\,\tau,\\
|\langle g_{c_i},g_{c_j}\rangle-
  \langle\tilde g_{c_i},\tilde g_{c_j}\rangle|
&\le 4B\,\tau.
\end{aligned}
\]
The \(\tilde g_c\) physical Gram and pole overlaps are *exact finite rational linear combinations* of SI18's analytic supported integrals
\[
\langle s,h_\xi\rangle,\qquad
\langle h_\xi,h_\eta\rangle.
\]
The original SI06/12/14 \(\pi,\sin,\cos,\sinh,\cosh\) enclosures yield full outward rational intervals, with all nine Gram entries, source signs and signed off-diagonal interactions explicitly accounted for.

This approach is much more accurate than SI19's simple \(\|g_c-h_c\|\)-estimate, especially when the window radius is increased from \(1/125\) to \(1/50\).

## 4. Correct-sign 3×3 Woodbury without a fragile interval inverse

Let \(G:\mathbb C^3\to H_o\) synthesize the three exact averaged functions, \(H=G^*G\succeq0\) their true physical supported Gram, and \(q=G^*s\). Let \(\Gamma=\operatorname{diag}(\gamma_j)\). The reference matrix
\[
M=\Gamma^{-1}+\kappa^{-1}H\succ0.
\]
By the exact supported **reference-only** Woodbury identity,
\[
2\langle s,A_o^{-1}s\rangle
\le 2\left[
\frac{\|s\|_2^2}{\kappa}
-\frac{q^*M^{-1}q}{\kappa^2}\right].
\]
For any **rational test vector** \(z\in\mathbb Q^3\),
\[
\boxed{
q^*M^{-1}q
\ge 2z^\top q-z^\top Mz.
}
\]
The equality case would take \(z=M^{-1}q\). SI20 obtains a *candidate* rational vector by solving with the midpoints of the exact outward Gram and overlap intervals, then checks a **lower bound on the entire variational expression with original exact rational interval operations**. Every off-diagonal term is included with its *actual coefficient sign*; no matrix determinant is silently rounded, and the candidate itself is not used as an unverified numerical equality.

With the strictly certified full response upper, this gives a fully supported inequality on the original odd inverse, without replacing \(A_o^{-1}\) by unrestricted pointwise \(1/a(\xi)\). The exact rational validator explicitly asserts the reference upper bound **below 6**, compared with SI19's prior \(<18\); if final-head CI passes, its printed stronger enclosure is recorded in the PR.

## 5. Meaning and remaining obligation

SI20 establishes a much stronger *one-direction scalar upper* on the same original odd-pole inverse response. It is a **mathematically meaningful improvement to the positive reference**, but not the odd-pole threshold \(2\langle s,A_o^{-1}s\rangle\le1\). Even that one-pole threshold would be insufficient to establish the entire signed Weil form because SI11's additional negative-frequency operator and its cross-couplings still enter the full Birman–Schwinger block.

**SI21 proposed gate:** investigate a fourth independent physical positive-frequency feature or derive a *non-scalar supported spectral floor* using the complete continuous positive multiplier, then benchmark rank versus actual signed Schur coupling. If a rank-one pole bound starts to approach 1, calculate a directly supported response with original residual and retain the \(\kappa^{-1}R^*R\) correction. Keep the smaller native RC high Schur route independently active.

**Replay:** \`python scripts/validate_rpb108_si20_odd_jensen_three.py\` and full SI GitHub Actions regression suite. Mathematical operator identities are analytic; the Fraction validator checks the full numerical and interval-rational gate. No Lean formalization, peer-reviewed complete RH proof or global Weil positivity is claimed.
