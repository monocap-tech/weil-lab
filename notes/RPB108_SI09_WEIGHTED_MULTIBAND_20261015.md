# RPB108 SI09 — mass-weighted multi-band polynomial compression with safe cluster merges

**Structural front:** SI09. **Parent:** integrated SI08, commit \`e5417ede89ae7ed4a6301491d584b23f19ce983e\`.  
**Native source:** CC27/RC312–313 original archimedean-plus-seven-prime signed frequency multiplier, with SI06 strict outer safe band and SI07 exactly certified possible-negative dyadic clusters. Signed odd pole retained exactly.

## 1. Question and inherited invariant

SI08 gave a *dimension-independent certified* operator approximation for the negative physical operator
\[
K_{\rm negative}=K_-+2|s\rangle\langle s|,\quad
K_-=Z^*\mathcal F^{-1}m_-\mathcal FZ,\quad s(x)=\sinh(x/2),
\]
with error \(<2^{-72}\) at sufficient rank \(4165\). It used the same Taylor phase-error target \(2^{-80}\) on all 107 distinct positive-frequency clusters.

SI07 actually provides **stronger information than cluster locations**. Every unresolved rational dyadic leaf \(L=[a,b]\) has a certified signed multiplier lower bound \(\underline m_L\), and therefore a positive rational upper envelope
\[
0\le m_-(\xi)\le h_L,\qquad h_L=
10^{-6}\big\lceil 10^6(-\underline m_L)\big\rceil.
\]
These leave **no uncharged negative frequencies**: positive-certified cells contribute none; \(|\xi|\ge896\) contributes none by SI06. By symmetry each positive cluster \(I_j\) carries a certified *two-sided negative Fourier mass*
\[
M_j=2\sum_{L\subset I_j}|L|h_L,\qquad
\boxed{\sum_{j=1}^{107}M_j\le37.59565259375<38.}
\]
SI09 verifies the original signed leaf generation again in its own exact-rational validator instead of merely importing the aggregate SI07 trace bound.

## 2. New exact weighted operator error theorem

Group adjacent clusters when advantageous. A resulting group \(G_j=[a_j,b_j]\) may contain **certified positive gaps**, but the upper mass \(M_j\) is only the *sum of genuine potentially-negative leaves* that the group covers; merging creates **no fictitious negative Fourier mass**.

Choose a modulated physical polynomial Taylor order \(p_j\ge0\) separately for each group, and put
\[
R_j=\frac{22}{7}B(b_j-a_j),\qquad
\varepsilon_j=\min\bigl(1,R_j^{p_j}/p_j!\bigr).
\]
For \(p_j=0\) the group contributes no feature and the trivial approximation \(0\) bounds the norm error by one. The centered Taylor expansion for the real Fourier phase (see SI08) yields
\[
\operatorname{dist}\left(\mathbf 1_{[-B,B]}e^{2\pi i\xi x},
\operatorname{span}_{0\le k<p_j}
\{\mathbf1_I e^{\pm2\pi i c_jx}x^k\}\right)
\le\sqrt{2B}\,\varepsilon_j
\]
for all true negative frequencies in \(G_j\) and its reflection. Here \(c_j=(a_j+b_j)/2\) and the identity is a *physical support-preserving* approximation, not a Fourier projector that destroys input compact support.

Let \(P\) denote physical \(L^2(I)\) orthogonal projection onto the sum of all selected modulated-polynomial spans **plus the exact pole vector \(s\)**. Then the integral rank-one operator inequality shows
\[
\boxed{
\|K_{\rm negative}-PK_{\rm negative}P\|
\le 4B\sum_j M_j\varepsilon_j.
}
\]
The total dimension obeys
\[
\boxed{\operatorname{rank}P\le1+2\sum_jp_j.}
\]
The RHS is an **upper bound on an explicitly generated physical finite-dimensional span**, not an eigenvalue count, numerical Gram inversion, a certificate of positivity of the full Weil operator, or a stable-condition-number guarantee.

## 3. Certified rank optimization (exact arithmetic, no hidden numerical cancellation)

For each error target \(2^{-(b-8)}\), with \(b\in\{40,64,80,96\}\):

1. Rebuild the original 972 dyadic leaf certificates and the full 107 positive-frequency clusters, with their individual **exact outward signed negative masses** \(M_j\).
2. Start from SI08's already-paid uniform \(p_j\) satisfying \(R_j^{p_j}/p_j!<2^{-b}\).
3. Greedily lower individual local polynomial orders if and only if the **exact rational** new value \(4B\sum M_j\varepsilon_j\) remains strictly below the **same** target \(2^{-(b-8)}\). Every accepted reduction is separately proved safe; global optimality of this greedy schedule is not asserted.
4. Attempt adjacent-cluster merges. A merge replaces two separate polynomial families by one centered family only if the group order is strictly smaller than the former total order **and** the exact mass-weighted upper bound does not increase. The intermediate positive frequency gaps between clusters may be included in the Taylor radius, but not charged as negative mass.
5. Use any remaining exact error budget to reduce further local orders.

The verifier asserts equality of all imported/inherited signed source masses, full coverage, each error acceptance inequality, and monotonic nonincrease of the certified dimension relative to SI08. **No approximation lower bound is claimed:** the new ranks are sufficient dimensions for one constructive method.

The exact replay prints the rank/band/error frontier, which is inserted below after final GitHub Actions verification.

## 4. Strategic boundary

Any improvement over SI08 must be compared at **identical operator-error targets**. In particular, the \(b=80\) line should be compared against SI08 rank \(4165\) with error \(<2^{-72}\), not against SI06's rank \(9473\) with error \(<2^{-1000}\).

Even a large reduction of the negative-frequency approximation rank does not itself prove positivity: the complete original signed Weil form is \(Q_+-\langle f,K_{\rm negative}f\rangle\), and the original positive part still needs to dominate the negative operator through a *coupled* operator inequality. RC314's 301-dimensional possible-negative-sector result addresses a different Feshbach/Schur object.

**Next frontier (SI10):** study whether individual cluster spans can be compressed further using real cosine/sine or orthogonal polynomial concentration bases with a **stable and fully certified Gram action**, and compare their rank/error competitiveness against the native RC signed Schur chain. Avoid an unvalidated switch of Stage I onto the structural front.

## Reproduction

\`\`\`bash
python scripts/validate_rpb108_si09_weighted_multiband.py
\`\`\`
This uses Python's standard library \`Fraction\`, the exact inherited SI06 cosine/log/digamma source enclosures, SI07's positive-cell logic, and SI08's real-phase Taylor certificate. The finite regression is not Lean formalization, independent peer review, or proof of RH.
