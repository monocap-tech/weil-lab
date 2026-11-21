# PI031 — Exact integer-interval certificate of nine live first-prime Gamma cancellations

**Weil-Lab Potential Interface / controlled research reopening.** Parent \`research/pi030-generic-transversal-prime-gamma-cancellations\`; issue #792. **New level of result:** one *explicit rational relative amplitude* \(u=3/2\), one *fixed annihilator order* \(m=1\), one explicit nonnegative \(C_c^\infty\) bump, and **at least nine distinct true \(n=3\) arithmetic/Gamma cancellation separations**. The proof combines the original source phase law and Gamma bound of PI027–PI030 with a new self-contained Python exact-integer outward-rounded integral-sign certificate. There is **no Lean kernel acceptance**, rigorous root *count equality*, derivative-at-root transversality certificate, zeta-zero computation, operator trace, global Weil positivity, or RH claim. NF acceptance frontier is unchanged at 692/968.

## 1. Freeze the genuinely smooth original-source test

Let
\[
d=\log(10/9),\quad \ell=d/100,\quad \Delta=d/2,\quad x_0=d/5,\quad u=\frac32,
\]
and put
\[
g(y)=\begin{cases}e^{-1/[y(1-y)]},&0<y<1,\\0,&\text{otherwise},\end{cases}
\quad b_\ell(x)=g(x/\ell),\quad
\rho(x)=b_\ell(x-x_0)+u b_\ell(x-x_0-\Delta).
\]
This fixes *one* real, nonnegative, nonzero, compactly supported \(C^\infty\) rho with support inside (0,d), as required in PI027.

Choose exactly \(m=1\), so the PI027 original pole-annihilating operator is \(L_1=D(D^2-1/4)\). Write
\[
\eta=L_1b_\ell,\quad \phi=L_1\rho,\quad
Q(t)=\int_\mathbb R\eta(x)\eta(x-t)\,dx,\quad q=Q(0)>0.
\]
Then the exact physical correlation is
\[
\boxed{C(t)=(1+u^2)Q(t)+uQ(t-\Delta)+uQ(t+\Delta),\qquad J=(1+u^2)q.}
\]
The \(Q\)-channels are disjoint since \(\mathrm{supp}(Q)\subseteq[-\ell,\ell]\), \(\Delta>2\ell\). The pole moments vanish exactly at 0 and ±1/2. The genuine source's Gamma \(B(a)>0\), finite prime \(P(a)\), and full phase
\[
W(h_{\beta,a})=W(C)+[B(a)-P(a)]\Re\beta
\]
are **unchanged** from PI027. A common spatial translation by -1/2 places each physical two-copy test inside the original full \((-11/10,11/10)\) window; it does not put it inside IV's much narrower old collar class.

The exact isolated first-prime window \(a=\log3-t\), \(0\le t\le d\), contains no prime-power sample except \(n=3\) because \(243/100>2\) and \(10/3<4\), so
\[
\boxed{P(\log3-t)=\kappa_3 C(t),\qquad \kappa_3=\frac{\log3}{\sqrt3}>\frac13.}
\]
The actual physical support has total measure at most \(2\ell=d/50\), giving the source-dependent uniform Gamma bound from PI030
\[
\boxed{0<B(a)<2\ell J<J/450}
\]
throughout the window. This estimate uses the compensated original Gamma kernel correctly for the diagonals and ordinary off-contact integral for the phase difference; it does **not** use a divergent naive diagonal physical integral.

## 2. Reduce the extra sign problem to three compact smooth integrals

Introduce \(\delta=\ell^2/4\) and the dimensionless real compact smooth function
\[
E(y)=g'''(y)-\delta g'(y).
\]
Then \(\eta(x)=\ell^{-3}E(x/\ell)\), and for \(0\le\tau\le1\),
\[
\boxed{Q(\ell\tau)=\ell^{-5}\mathcal I(\tau),\qquad
\mathcal I(\tau)=\int_\tau^1 E(y)E(y-\tau)\,dy,\quad
q=\ell^{-5}\mathcal I(0).}
\]
We need *signs* of \(\mathcal I\), not approximate prime/Gamma balancing roots. The exact smooth derivative polynomials of \(L(y)=-1/[y(1-y)]\), writing \(T=1/[y(1-y)]\), \(c=1-2y\), are
\[
\begin{aligned}
L'&=cT^2,\\
L''&=-2T^2-2c^2T^3,\\
L'''&=12cT^3+6c^3T^4,\\
L''''&=-24T^3-72c^2T^4-24c^4T^5.
\end{aligned}
\]
Consequently the algorithm evaluates \(E\) and \(E'\) through **literal polynomial** formulas
\[
E=g[(L')^3+3L'L''+L'''-\delta L'],\quad
E'=g[(L')^4+6(L')^2L''+3(L'')^2+4L'L'''+L''''-\delta((L')^2+L'')].
\]
No numerical differentiation or finite-difference derivative is involved.

The elementary logarithm bounds \(1/10<d<1/9\) imply the exact rational enclosure
\[
\boxed{1/4{,}000{,}000<\delta<1/3{,}240{,}000.}
\]
The implementation carries this **entire interval**, not a rounded decimal approximation of d, through each calculation.

## 3. Reproducible exact integer-interval integral enclosures

The new executable is \`scripts/pi031_exact_integer_interval_correlation_signs.py\`.

All assertions of significance are exact integer/rational comparisons. It does not rely on the Python floating-point numbers used for *displaying* the interval endpoints.

- Represent all intervals with outward-rounded signed integers at scale \(S=10^{45}\). Addition, multiplication, division and nonnegative powers round every lower endpoint down and every upper endpoint up.
- Evaluate the \(e^{-T}\) factor after subdividing its argument by a power of 2 to an interval \(0<z\le1\). The alternating-series 31-term odd partial sum bounds \(e^{-z}\) below and the 30-term even partial sum bounds it above; repeated interval squaring returns a conservative positive exponential interval. The scaled argument is retained as a lower/upper pair through division by powers of two.
- On \(y\in[0,1/20]\cup[19/20,1]\), where \(T\ge20\), use the rigorously verified crude enclosures \(|E(y)|<1\), \(|E'(y)|<500\). They follow from monotonicity of \(T^k e^{-T}\) for \(T\ge20,k\le8\), the exact polynomial derivative bounds, and \(e^{20}>\sum_{k=0}^{16}20^k/k!>10^8\). This avoids evaluating singular rational expressions at the endpoints even though the *flat smooth function* itself extends there.
- Partition each \([\tau,1]\) into **512** equal rational cells of width h. For \(f_\tau(y)=E(y)E(y-\tau)\), enclose the midpoint \(f_\tau\) by exact interval evaluation, enclose \(|f_\tau'|\) on the complete cell by products of the two interval \(E,E'\) bounds, and include the rigorous first-derivative midpoint remainder
\[
\left|\int_{\mathrm{cell}}f_\tau(y)\,dy-hf_\tau(y_{\rm mid})\right|
\le \frac{h^2}{4}\sup_{\mathrm{cell}}|f_\tau'(y)|.
\]
- The sum of these cell intervals encloses the **actual** smooth integral \(\mathcal I(\tau)\). The following intentionally coarse **exact rational acceptance margins** passed:
\[
\boxed{\begin{aligned}
17&<\mathcal I(0)<21,\\
\mathcal I(1/4)&<-5,\\
\mathcal I(3/5)&>6,\\
\mathcal I(3/4)&<-3.
\end{aligned}}
\]
For diagnostic readability only, displayed interval endpoints at 512 cells were approximately \([17.496,20.158]\), \([-7.528,-5.558]\), \([6.563,7.607]\), and \([-4.247,-3.175]\), respectively. **The integer inequalities above—not these rounded displays—are the formal input to the next proof.**

An independent exploratory computation of the same dimensionless integrals via SciPy adaptive quadrature and 55-digit mpmath quadrature is consistent with the rigorous intervals; these approximations are NOT the evidence for the signs. No external interval-arithmetic library, GitHub Actions run, or Lean theorem is claimed.

## 4. Nine disjoint exact IVT brackets

Write \(t=\log3-a\) and \(\Theta(t)=B(\log3-t)-\kappa_3C(t)\). The dimensionless Gamma bound and \(\mathcal I(0)<21\) imply
\[
\ell^5 B(\log3-t)<(1+u^2)\,\mathcal I(0)/450
<\frac{13}{4}\frac{21}{450}=\frac{273}{1800}<\frac16
\]
for all \(0\le t\le d\).

At the positive lobe \(\tau=3/5\), \(\mathcal I(3/5)>6\). At the **central** correlation channel \(t=(3/5)\ell\),
\[
\ell^5 P(t)
=\kappa_3(1+u^2)\mathcal I(3/5)
>\frac13\frac{13}{4}6=\frac{13}{2},
\]
and at both **satellite** channels \(t=\Delta\pm(3/5)\ell\),
\[
\ell^5 P(t)
=\kappa_3u\mathcal I(3/5)>\frac13\frac32\,6=3.
\]
Thus \(\Theta<0\) at all these live \(n=3\) peak controls. At \(t=0\) and \(t=\Delta\), the previously proved exact positive peak \(Q(0)=q>0\) also gives \(\Theta<0\) by these same source bounds.

At \(\tau=1/4,3/4\), the rigorous \(\mathcal I(\tau)<0\) makes the *original* prime correlation \(P<0\); hence \(\Theta=B-P>0\). Evenness of \(Q\) gives the identical signs at \(-\tau\). At the support edges \(Q(\pm\ell)=0\), \(\Theta=B>0\).

Therefore the central sector has the ordered controls (in **t**, not a):
\[
\boxed{\begin{array}{c|cccc}
t/\ell&0&1/4&3/5&3/4\\ \hline
\mathrm{sgn}\,\Theta&-&+&-&+
\end{array}}
\]
and consequently at least **three distinct roots** in
\[
\boxed{(0,\ell/4),\quad (\ell/4,3\ell/5),\quad (3\ell/5,3\ell/4)}
\]
in t-coordinates.

The satellite sector has the ordered controls:
\[
\boxed{\begin{array}{c|rrrrrrr}
(t-\Delta)/\ell&-3/4&-3/5&-1/4&0&1/4&3/5&3/4\\ \hline
\mathrm{sgn}\,\Theta&+&-&+&-&+&-&+
\end{array}}
\]
and consequently at least **six distinct roots**, one in every consecutive open interval between these seven controls.

All nine brackets are disjoint because \(\Delta>2\ell\), lie inside \(0<t<d\), and therefore correspond to distinct separations \(a=\log3-t\) in the **original n=3 interaction window**. At each crossing,
\[
\boxed{P(a)=B(a)>0,\quad W(D_a)=0,\quad W(h_{\beta,a})=W(C)
\qquad (|\beta|=1).}
\]
These are classical consequences of the exact integer enclosure + original source phase law; not claims that the original diagonal \(W(C)\) is positive or zero.

**Theorem PI031:** the explicitly fixed \(m=1,u=3/2\) genuine smooth autocorrelation family has **at least nine distinct, live, exactly phase-flat first-prime separations**. This is an unconditional *classical/source-based* existence count, not merely exploratory numerical roots.

## 5. What PI031 has NOT proved, and PI032 gate

- **No exact total root count**: the test controls imply \(\#\mathrm{roots}\ge9\), not that there are exactly nine. Signed derivative-bump correlations can have additional oscillations.
- **No fixed rational-amplitude transversality certificate**: each bracket contains at least one sign-changing zero, but its derivative may vanish. PI030's "almost all u" does not by itself certify \(u=3/2\).
- **No spectral equality**: CP's full offcritical complex Mellin/zero dictionary and both Masullo Ch12/Ch13 trace hypotheses are unresolved. The source-matched contact-free \(D_a\) at any crossing still satisfies \(W(D_a)=0\); the printed Ch13 normalization, **if** its unproved formula applies, would require \(Z_{13,\rm cap}(D_a)=2B(a)>0\). This is a conditional test, not a computed zero sum.
- **No Lean or NF status change**: exact Python arithmetic supplies a human-auditable interval certificate but is not independently reconstructed inside Lean; original HD/A remains 692/968. No CI/PR/Actions dispatch or historical certificate modification.

**Highest-value PI032 immediate task:** extend the same rational fixed-point interval engine to enclose the **derivative** \(\mathcal I'(\tau)\) on compact subintervals containing each of the nine crossings, derive an explicit bound for \(B'(a)\) from the original positive mode expansion, and prove \(\Theta'(a)\ne0\) throughout those subintervals. That will promote this explicit rational test from \(\ge9\) live crossings to certified simple crossings, potentially with exact root count after complementary no-root interval coverage. A small, source-bound Lean scalar proof candidate can then be prepared; only dispatch an isolated kernel job after verifying repaired source-scoped workflow ancestry and bounded expected fan-out. The PI031 documentation and script match none of the PR-triggered path filters inherited from PI030, but opening a PR against \`main\` requires a separate **full stacked-diff** audit. NF certification priority remains protected.

## 6. Verification status and source custody

- **Source:** original \`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean\` source blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\`, directly rechecked in the IV024 source branch, matching PI027; source polarity \(+\mathrm{pole}-\mathrm{prime}+\Gamma\).
- **Exact arithmetic:** \`python3 scripts/pi031_exact_integer_interval_correlation_signs.py\` — all four integer integral containments and nine-root sign budget **PASS locally**. The script contains no external package dependency.
- **Regression distinction:** source-level mathematical proof and executed exact arithmetic are **not** a Lean kernel proof, nor independent exhaustive review of the interval implementation.
- **CI:** no new workflow or PR; zero dispatched jobs. Prior accepted NF750–NF753 numerical artifacts and strict axiom-audit requirements remain unchanged.
