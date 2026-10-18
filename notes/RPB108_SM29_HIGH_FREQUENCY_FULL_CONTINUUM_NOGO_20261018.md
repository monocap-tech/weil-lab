# SM29 — Full thirteen-band positive CONTINUUM still fails the original complete odd cap at a remote packet

**October 18, 2026 · Canonical W-ODD-NEG · stacked on SM28 draft PR #209 (focused Actions PASS).**

**NEW result (inherited analytical assumptions):** A true ORIGINAL physically supported odd packet at signed-negative frequency \(c=38956/100=389.56\) witnesses a **strict negative margin** against the original SI29 pole-conditioned fourteen-source positive reference **plus the ENTIRE original thirteen-band positive-frequency continuum of SM28**, not merely its first 26 Legendre vectors. This transfers, by the complete original SM10 890-source cap and a full Schur inertia argument, to the **entire 890-source continuum-enriched surrogate spectral gate**, whose negative index is at least one. The *genuine* complete original \(A_*=A_o-2|s\rangle\langle s|\) still includes other positive-frequency continuum not captured by the reference, and its signed odd form could be positive; this is a **method no-go**, not a true Weil negative mode or RH counterexample. PS36 O1/O2 stays OPEN.

## 1. Physical support, signs and remote genuine original packet

Let \(H_o=L^2([-11/10,11/10])_{\mathrm{odd}}\), \(B=11/10\), \(\kappa=1/1000\), with the true original complete seven-prime signed odd spectral decomposition
\[
 W_o=A_*-K_{\neg,o},\quad
 A_*=A_o-2|s\rangle\langle s|,\quad s(x)=\sinh(x/2).
\]
SM11 previously certified **seventeen whole-real signed-negative bands** and all physical cross-Grams, including its remote original negative window centered at
\[
 \boxed{c=38956/100=389.56,\quad \rho=1/100,\quad
  g(x)=\sin(2\pi c x)\operatorname{sinc}(2\pi\rho x),\quad x\in[-B,B].}
\]
The *true* original full negative-frequency operator has its actual signed-continuum Jensen lower bound
\[
 K_{\neg,o}\succeq\frac2{125}\sum_{j=1}^{17}|g_j\rangle\langle g_j|
 \quad\Longrightarrow\quad
 \langle g,K_{\neg,o}g\rangle\ge\frac2{125}\|g\|_2^4.
\]
No delta-function frequency probe, surrogate negative multiplier or assumed separation of odd physical Fourier features is used.

The TRUE original SI29 reference is
\[
 B_{14}=\kappa I+\sum_{i=1}^{14}\gamma_i|p_i\rangle\langle p_i|
      -2|s\rangle\langle s|,\quad
 \gamma_i=\frac{4r_i\delta_i}{3^{\mathbf1_{\deg_i=1}}},
 \qquad B_{14}\succeq\kappa_*I,\quad \kappa_*=\frac{33621}{10^9}.
\]
Its fourteen actual continuous *degree-zero or degree-one* Legendre features are
\[
 p_{i0}=\frac12\int_{-1}^1 h_{c_i+r_it}\,dt,
 \quad p_{i1}=\frac32\int_{-1}^1 t h_{c_i+r_it}\,dt,\quad
 h_\xi(x)=\sin(2\pi\xi x).
\]
The source coefficient \(\gamma_i=4r_i\delta_i/3\) for \(\deg_i=1\) pays the \(\sqrt3\) first moment exactly; **do not ignore or double count first moments**.

SM28 adds the full thirteen original SM14 certified sign-positive *continuous* frequency windows \(J_j=[d_j-r,d_j+r]\), \(r=3/200\), and \(\sum_j\delta_j=35\):
\[
 T_{13}:=\sum_j 2\delta_j\int_{J_j}|h_\xi\rangle\langle h_\xi|\,d\xi
 =\sum_j 4r\delta_j\sum_{n\ge0}(2n+1)|q_{jn}\rangle\langle q_{jn}|.
\]
Thus all infinitely many true Legendre modes are included; \(T_{13}=T_{13}^{[2]}+R_{13,\ge2}\) exactly. SI29/SM14 signed-band disjointness proves the genuine FULL physical order
\[
 \boxed{\kappa_* I\preceq B_{14}\preceq F_{13}:=B_{14}+T_{13}\preceq A_*.}
\]

## 2. NEW uniform exact-rational physical overlap bound for ALL positive continuum in F13

Every actual original SI29 14 source window and all thirteen SM14 added positive windows lie inside \(0<\xi<20\), whereas the original SM11 negative packet has \(c=389.56\). The original full physically supported sine Gram satisfies, for every \(0<\xi<20\),
\[
 \left|\langle h_c,h_\xi\rangle_{[-B,B]}\right|
 \le\frac{1}{2\pi(c-\xi)}+\frac{1}{2\pi(c+\xi)}
 <\frac1{6\cdot369}+\frac1{6\cdot389}.
\]
The original Jensen negative packet has a **true pointwise** sinc envelope error
\[
 |g(x)-h_c(x)|\le e_\rho
 :=\frac{(2\pi_{\rm up}\rho B)^2}{6},\quad
 \pi_{\rm up}<22/7,\quad |x|\le B,
\]
so, uniformly across **every real frequency** in every positive reference band,
\[
 \boxed{
 |\langle g,h_\xi\rangle|
 \le\frac1{6\cdot369}+\frac1{6\cdot389}
       +2B\frac{(2(22/7)\rho B)^2}{6}
 <u:=\frac3{1000}.}
\]
This is a **uniform all-real continuum original supported overlap**, not point samples and not a false orthogonality assertion.

For actual SI29 degree-zero means, \(|\langle g,p_{i0}\rangle|\le u\); for the normalized degree-one means, \(|\langle g,p_{i1}\rangle|\le3u/2\), and the coefficient \(4r_i\delta_i/3\) makes
\[
 \gamma_i|\langle g,p_i\rangle|^2
 \le4r_i\delta_i\,u^2
 \qquad(\deg_i=0\text{ or }1),
\]
since \(3u^2/4\le u^2\). The real SI29 sum
\(\boxed{\Sigma_{14}:=\sum_{i=1}^{14}4r_i\delta_i<200}\)
is replayed from the **original fourteen** source definitions with exact Fractions. Likewise the **ENTIRE**, not truncated, thirteen-band positive continuum obeys
\[
 \boxed{\langle g,T_{13}g\rangle
 \le\sum_j4r\delta_j u^2
 =\frac{21}{10}u^2.}
\]
The negative odd pole term of \(B_{14}\) is nonpositive and is retained with the correct sign. With \(\|g\|_2^2\le2B=11/5\),
\[
 \boxed{
 \langle g,F_{13}g\rangle
 <\kappa(11/5)+(200+21/10)u^2.
 }
\]
Crucially: this already includes **all** of the SM28 infinite Legendre tail. It is not being discarded to improve the obstruction.

## 3. Complete original negative lower, strict quantitative obstruction

The physical sine norm has the exact lower bound
\[
 \|h_c\|_2^2
 =B-\frac{\sin(4\pi Bc)}{4\pi c}
 > B-\frac1{12c},
\]
because \(\pi>3\). The original pointwise sinc error bounds the **actual** packet norm:
\[
 \|g\|_2^2
 \ge (1-e_\rho)^2\|h_c\|_2^2
 >(1-e_\rho)^2\left(B-\frac1{12c}\right).
\]
Therefore the TRUE original SM11 negative band gives the **exact rational** lower
\[
 \boxed{
 \langle g,K_{\neg,o}g\rangle
 >\frac2{125}
 \left[(1-e_\rho)^2\left(B-\frac1{12c}\right)\right]^2.
 }
\]
An exact Fraction comparison in the focused validator certifies
\[
 \boxed{
 \langle g,(K_{\neg,o}-F_{13})g\rangle
 >\frac{3}{200}>0.
 }
\]
The numerical margin \(3/200\) is a deliberately weakened strict bound. All SI29 original degree-one sources, full thirteen bands, actual negative odd pole sign, original physical integration and full seven-prime continuous negative Jensen packet are charged. This certificate remains conditional on the accepted original Fourier/Weil identification, signed SM11/SM14 windows and SI29 pole-floor analytic lemmas, not merely on arithmetic CI.

Thus the entire CONTINUUM-enriched physical reference is deficient on at least one genuine high-frequency original negative packet. Enlarging the original rank-14 reference by *all Legendre moments in just these thirteen local bands around 14* is insufficient as a **complete odd lower reference**, even though it rescues the SM27 diagnostic packet **at 14.42**. This is a frequency-coverage defect, not a Legendre truncation defect.

## 4. NEW: complete original 890-source continuum-conditioned spectral index

SM10's ORIGINAL complete 890-source Taylor upper includes all original signed negative-frequency bands, 107 exactly positive rational moment covariance blocks, every original cross within the synthesis and the uniform entire-frequency residual:
\[
 K_{\neg,o}\preceq U D U^*+\eta I,\quad
 D=(1+\tau)C_{890}\succ0,\quad
 \tau=1/1024,\quad
 0<\eta<302/10^{12}<\kappa_*.
\]
Consequently the **same physical original \(g\)** satisfies
\[
 \langle g,(F_{13}-\eta I-U D U^*)g\rangle
 \le\langle g,(F_{13}-K_{\neg,o})g\rangle
 <-\frac3{200}.
\]
Although \(F_{13}\) is infinite-rank beyond its scalar floor, it is bounded on \(H_o\), and
\(F_{13}-\eta I\succeq(\kappa_*-\eta)I\succ0\).
The exact original infinite-dimensional block
\[
 {\cal B}=
 \begin{pmatrix}
 F_{13}-\eta I & U\\ U^*&D^{-1}
 \end{pmatrix}
\]
has both diagonal factors strictly positive. Complete bounded Schur-inertia congruence gives the **true full original negative-cap surrogate source Schur**
\[
 \boxed{
 S^{(13\rm \,cont)}_{890}
 =D^{-1}-U^*(F_{13}-\eta I)^{-1}U,
 \qquad
 \operatorname{ind}_{-}(S^{(13\rm \,cont)}_{890})\ge1.
 }
\]
This is a **complete 890-source result with all original thirteen positive continuum bands, all of their positive infinite Legendre variance, the original odd pole, and the entire SM10 negative-frequency infinite residual included**. No numeric 890×890 inversion and no high/low truncation is needed.

**The order limitation is decisive:** \(A_*\succeq F_{13}\), so \(S^{\mathrm{true}}_{890}=D^{-1}-U^*(A_*-\eta I)^{-1}U\succeq S^{(13\rm cont)}_{890}\). An indefinite LOWER surrogate does **not** imply the true \(A_*\) or \(W_o=A_*-K_{\neg,o}\) has a negative eigenvalue. Original complete O1/O2 sign and even E1–E4 remain OPEN. Additional genuine positive continuum **near 389.56 and other negative bands** may repair this defect.

## 5. What SM29 actually directs next

SM28 resolved **within-window** structure (all Legendre degrees). SM29 proves that **window placement** is a separate mandatory dimension: a perfectly represented local positive-frequency continuum around 14 cannot cover the true signed negative continuum at 389.56. Thus continuing by increasing Legendre order on those same bands cannot close PS36 original complete odd O1/O2.

**SM30 acceptance-directed:** identify and certify original whole-real sign-positive bands *near this remote source* and other uncovered SM11 negative packets, paying the original supported sine overlaps and **entire** odd pole/source coupling. A source-placement design can use the original full SM10 107-cluster map and the original SM11 17-packet cover, but must test **all** 890 modes, including the infinite \(\eta\) residual. The success metric is actual complete original \(A_*\)-conditioned Loewner PSD, not local diagnostic positivity. SM12 already has positive sign-certified bands at 389.26; those may help, but C33's single mean does not automatically guarantee domination. Original E1–E4, whole Weil, native CC27 D-Riesz, and RH remain OPEN.

**Replay**: \`python3 scripts/validate_rpb108_sm29_high_frequency_full_continuum_nogo.py\`. It checks the exact original high remote SM11 whole-negative band, SI29 original 14 degree 0/1 source weights and 12 source frequency intervals, SM28 entire thirteen positive-band geometry, exact all-real rational sine-decay bound, full original negative physical packet norm lower, true SI29 odd-pole reference floor, SM10 all 107/890 blocks plus \(\eta\), and a fully coupled finite inertia regression. Machine CI alone does not independently certify the inherited original analytic identification.
