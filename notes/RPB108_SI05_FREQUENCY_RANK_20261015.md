# RPB108 SI05 — certified finite-rank compression of the negative Weil-frequency operator

**Front:** Structural Investigation, separate from the RC original high Schur-inverse chain.  
**Parent:** merged RC329 \`d861029424f2c361a3a85e24402d8fd70f083c6e\`.  
**Dependencies:** RC312/313 original archimedean and signed prime/pole Fourier form; SI04's *rigorously certified* frequency-safe region \(|\xi|\ge2048\) and \(0\le m_-(\xi)<13\).  
**Standing:** an explicit dimension-independent **operator-norm finite-rank approximation** with an exponentially tiny certified remainder. The rank bound is large (20,480); **not a computational shortcut or full positivity theorem**.

## 1. The native negative multiplier

In SI04, on the physical supported interval \(I=[-B,B]\), \(B=11/10\), the complete original signed archimedean-plus-seven-prime multiplier is \(m=m_+-m_-\), with
\[
\operatorname{supp}m_-\subset(-\Omega,\Omega),\quad\Omega=2048,\qquad0\le m_-<13.
\]
The negative physical operator, with \(Z\) zero extension and the original RC313 Fourier convention, is
\[
K_-=Z^*\mathcal F^{-1}m_-\mathcal F Z
=\int_{-\Omega}^{\Omega}m_-(\xi)
|\phi_\xi\rangle\langle\phi_\xi|\,d\xi,
\quad \phi_\xi(x)=e^{2\pi i\xi x}\ \ (x\in I).
\]
The integral converges in trace norm; \(K_-\succeq0\), and
\[
\operatorname{tr}K_-=2B\int m_-\le4B\Omega(13).
\]
The negative odd original pole \(2|s\rangle\langle s|\), \(s(x)=\sinh(x/2)\), is treated separately as an **exact rank-one** operator.

## 2. Universal plane-wave Legendre-tail inequality

Let \(u_n(x)=\sqrt{(2n+1)/(2B)}P_n(x/B)\), and let \(\Pi_N\) project onto the first \(N\) physical Legendre modes \(u_0,\ldots,u_{N-1}\).

Rodrigues' formula and \(n\) integrations by parts (with vanishing endpoints of \((1-t^2)^n\)) yield, for all \(z\in\mathbb R\),
\[
\left|\int_{-1}^1P_n(t)e^{izt}\,dt\right|
\le \frac{2|z|^n}{2^n n!}.
\]
Consequently, for \(z=2\pi B\xi\),
\[
\boxed{
|\langle u_n,\phi_\xi\rangle|^2
\le2B(2n+1)\left(\frac{|z|^n}{2^n n!}\right)^2.
}
\]
The elementary factorial bound \(n!\ge(n/e)^n\), together with \(\pi<22/7\) and \(e<11/4\), turns this into a geometric tail.

Take \(N=20480\), \(\Omega=2048\). Then
\[
|z|\le Z=\frac{495616}{35},\quad
\frac{(11/4)Z}{2N}=\frac{1331}{1400}<\frac{24}{25}.
\]
Set \(q=(24/25)^2=576/625\). For every \(n\ge N\) and \(|\xi|\le\Omega\),
\[
|\langle u_n,\phi_\xi\rangle|^2\le2B(2n+1)q^n.
\]
Sum the entire infinite Legendre tail **exactly**:
\[
\|(I-\Pi_N)\phi_\xi\|_2^2
\le 2B q^N\left(\frac{2N+1}{1-q}+
\frac{2q}{(1-q)^2}\right).
\]
The rational prefactor is \(<2^{21}\); \(q^9=(24/25)^{18}<1/2\); and \(N\ge9(2275)\). Hence
\[
\boxed{
\sup_{|\xi|\le2048}\|(I-\Pi_N)\phi_\xi\|_2^2
<2^{-2254}.
}
\]
This is a **uniform high-degree bound for every plane wave in the original entire possible negative frequency band**, not an empirical or sampled spectral tail.

## 3. Finite-rank operator-norm reduction

Set \(K_-^{(N)}=\Pi_N K_-\Pi_N\), a positive semidefinite operator of rank at most \(N\). For vectors \(u,v\), the rank-one identity and operator norm inequality give
\[
\||u\rangle\langle u|-|v\rangle\langle v|\|
\le(\|u\|+\|v\|)\|u-v\|.
\]
With \(u=\phi_\xi\), \(v=\Pi_N\phi_\xi\), \(\|\phi_\xi\|=\sqrt{2B}\), and \(m_-\ge0\), conclude
\[
\|K_--K_-^{(N)}\|
\le2\sqrt{2B}\left(\int m_-(\xi)d\xi\right)
\sup_{|\xi|\le\Omega}\|(I-\Pi_N)\phi_\xi\|_2.
\]
The SI04 bounds imply \(\int m_-<2\Omega(13)=53248<2^{16}\), while \(2\sqrt{2B}<4\). Therefore
\[
\boxed{\|K_--\Pi_N K_-\Pi_N\|<2^{-1109}<2^{-1000}.}
\]
All bounds are symbolic and follow from exact rational inequalities, plus Rodrigues, factorial and projection facts.

Include the negative odd pole *exactly*:
\[
K_{\rm negative}=K_-+2|s\rangle\langle s|,\qquad
K_{\rm negative}^{(N)}=\Pi_NK_-\Pi_N+2|s\rangle\langle s|.
\]
Then
\[
\boxed{
\operatorname{rank}K_{\rm negative}^{(N)}\le20481,\quad
\|K_{\rm negative}-K_{\rm negative}^{(N)}\|<2^{-1000}.
}
\]
The min–max principle implies \(\lambda_{20482}(K_{\rm negative})<2^{-1000}\), counting eigenvalues in descending order with multiplicity. In the even sector the rank-one negative pole is absent; in the odd sector it is retained without numerical approximation.

For any supported polynomial \(f\) in the original form domain,
\[
Q_{\rm Weil}(f)=Q_+(f)-\langle f,K_{\rm negative}f\rangle
\ge Q_+(f)-\langle f,K_{\rm negative}^{(N)}f\rangle
-2^{-1000}\|f\|_2^2,
\]
where \(Q_+(f):=\int m_+|\widehat f|^2+2|\langle\cosh(x/2),f\rangle|^2\ge0\).
This is a rigorous **finite-rank lower-comparison formulation**, not a certificate that the RHS is nonnegative.

## 4. Decision: this explicit SI04 route is not competitive yet

The original RC314 finite-dimensional potentially nonpositive problem has rank **301** (and its buffered references 317). The currently certified *frequency-only* compression uses **20,481** possible negative directions, roughly sixty-eight times the rank-301 count. Its huge precision is mathematically legitimate but not a useful reduction of the RC workload.

The theorem proves that *some* constructive finite-rank compression exists with explicit error. It does not prove that \(20,481\) is **necessary** or optimal. SI04's cutoff \(2048\) and bound \(m_-<13\) were deliberately conservative; a much smaller effective-frequency support could improve the required rank dramatically.

A highly accurate approximation of the negative part alone also cannot establish positivity: the positive background \(Q_+\) may have arbitrarily small values along relevant directions, so the \(2^{-1000}\) error does not automatically create a spectral gap.

## 5. SI06 frontier

**Optimize the structural representation before larger calculations:**

1. Certify the *actual negative-frequency support* and its integrated weight using interval enclosures for the full oscillatory signed multiplier \(m(\xi)\), rather than worst-case \(2C\) across the entire high-frequency region.
2. Use frequency-adaptive Legendre approximation or time–bandwidth concentration estimates to infer a **smaller rank with a useful operator error**.
3. Preserve SI03's compact-support prime gap; do not apply that bound pointwise in Fourier frequency or to noncompact Fourier projections.
4. Benchmark against RC329's rigorously signed original Schur-inverse route, which continues independently. If the rank/error budget remains substantially worse, record the obstruction and avoid transferring the main program onto SI.

**What is not claimed:** positive original full Weil form, Stage I, F4, complete Lean proof, or RH.

## Reproduction

\`\`\`bash
python scripts/validate_rpb108_si05_frequency_rank.py
\`\`\`

The Fraction validator checks every finite numeric rational inequality underpinning the above all-degree analytic proof. It is not a Lean formalization of Rodrigues' formula, the Fourier spectral factorization, or the min–max principle.
