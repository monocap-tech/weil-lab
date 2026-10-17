# SM04 — fifteen independently certified signed-negative odd packets: an intrinsic reference-rank obstruction

**Active mathematical obligation:** W-ODD-NEG, **OPEN**.  
**Parent:** SM03 at merged research HEAD 07033f45f0d2e9471eb5dd10d8697c3c17a2cc7a.  
**Standing:** conditional until original signed interval and exact rational Gram replays pass on final head. The conclusion concerns finite-rank *positive lower references*, not the negativity of the original Weil form.

## Structural question

SM03 proved the original SI29 rank-14 positive reference could not absorb the full signed negative frequency operator. Was its particular choice of fourteen positive windows the problem, or is there a deeper obstruction to **every rank-14 positive reference of that form**?

SM04 identifies an intrinsic spectral answer independent of where the 14 positive features are placed.

## 1. Original signed odd form and genuine negative-frequency bands

On \(H_o=L^2([-11/10,11/10])_{\rm odd}\) retain the complete CC27/RC312–313 original seven-prime Fourier multiplier
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n).
\]
Following SI11, let \(\kappa=1/1000\), \(r(\xi)=(\kappa-m(\xi))_+\), and
\(K_{{\rm freq},o}=\Pi_o Z^*\mathcal F^{-1}r\mathcal FZ\Pi_o\).
The original signed form is \(Q_o=A_o-K_{{\rm freq},o}-2|s\rangle\langle s|\).

Choose *15 fixed rational centers*
\[
c_j\in\{1.90,7.26,14.42,20.04,27.32,39.08,44.70,59.12,
66.40,76.48,83.76,103.80,142.88,187.56,246.68\}.
\]
Their pairwise separation is at least \(5\). Fix \(\rho=1/100\) and \(\delta=2/5\).
The validator must certify
\[
\boxed{m(\xi)<-\delta\quad
\text{for every }\xi\in\bigcup_{j=1}^{15}([c_j-\rho,c_j+\rho]\cup[-c_j-\rho,-c_j+\rho]).}
\]
Each whole rational band is subdivided into four cells. Every cell uses the SI06 original-seven-prime exact cosine enclosure, derivative magnitude \(<69\), and the rigorously upper-enclosed infinite Euler digamma series of SM03 evaluated at the cell's right endpoint. These are certified *continuum* inequalities, not 15 numerical point samples.

## 2. Fifteen true odd continuous-frequency packets

For each such band, define a physically supported odd vector
\[
g_j(x)=\frac1{2\rho}\int_{c_j-\rho}^{c_j+\rho}
\sin(2\pi\xi x)d\xi
=\sin(2\pi c_jx)\operatorname{sinc}(2\pi\rho x).
\]
The **original full** negative-frequency operator satisfies
\[
\boxed{K_{{\rm freq},o}\succeq \gamma\sum_{j=1}^{15}|g_j\rangle\langle g_j|,
\qquad \gamma=4\rho\delta=\frac2{125}.}
\]
Here every original frequency interval and its reflection are present; all unselected negative frequencies only add a further PSD contribution.

Let \(G:\mathbb R^{15}\to H_o\) synthesize these fifteen *true averaged physical* odd vectors. Set \(H=G^*G\), their actual physical Gram.

The SI18 exact rational sine Gram formula, with all signed off-diagonal entries, provides enclosures of
\(\langle h_{c_i},h_{c_j}\rangle\), where \(h_c(x)=\sin(2\pi cx)\).
Put \(e=(2\pi_{\rm hi}\rho B)^2/6\), \(B=11/10\). Pointwise \(|\operatorname{sinc}(2\pi\rho x)-1|\le e\) and \(\operatorname{sinc}\ge1-e\), so
\[
H_{ii}\ge(1-e)^2\langle h_{c_i},h_{c_i}\rangle_{\rm lo},
\quad
|H_{ij}|\le|\langle h_{c_i},h_{c_j}\rangle|_{\rm up}+4Be.
\]
The validator checks the **full fifteen-by-fifteen** physical Gram Gershgorin lower bound
\[
\boxed{\lambda_{\min}(H)\ge
\min_i\bigg[H_{ii,\rm lo}-\sum_{j\ne i}|H_{ij}|_{\rm up}\bigg]
>9/10.}
\]
Therefore the fifteenth nonzero eigenvalue of the original full supported negative-frequency operator obeys, by operator monotonicity/min–max,
\[
\boxed{\lambda_{15}(K_{{\rm freq},o})>\gamma\cdot\frac9{10}
=\frac{9}{625}>\frac1{1000}=\kappa.}
\]
The replay also checks a stronger rational threshold \(\lambda_{15}>14/1000\). All of these are actual **odd physical supported** directions, not unconstrained frequency delta masses.

## 3. Consequence: arbitrary 14-feature lower reference cannot work

For *any* positive operator of the form
\[
C=\kappa I+T,\qquad T\succeq0,\quad\operatorname{rank}(T)\le14,
\]
the dimension-15 packet space contains a nonzero \(f\) with \(Tf=0\).
Because \(K_{{\rm freq},o}\) has an actual fifteen-dimensional spectral subspace with Rayleigh quotients \(>\kappa\), the proper min–max argument shows there is an \(f\) in that spectral subspace and \(\ker T\) such that
\(\langle f,(K_{{\rm freq},o}-C)f\rangle>0\).
Thus
\[
\boxed{\text{For every }T\succeq0,\ \operatorname{rank}T\le14:
\qquad \kappa I+T\not\succeq K_{{\rm freq},o}.}
\]

This is stronger than SM03: it does not depend on SI29's particular positive source locations, coefficients, or intervals. The pole subtraction from a positive reference only weakens that candidate further. It gives a **necessary reference rank ≥15**, but does not assert rank 15 is sufficient.

The original \(A_o\) is **not** a scalar floor plus only fourteen positive modes. It retains the actual entire multiplier \(a(\xi)\) and full support effects, so the obstruction does **not** establish negativity of \(A_o-K_{{\rm freq},o}-2|s\rangle\langle s|\), Stage I, or RH.

## 4. Research consequence

SM03's failed sparse reference was not merely poorly positioned. If SM04 replays successfully, *every* fourteen-feature-plus-\(\kappa I\) Loewner minorant is structurally incapable of dominating the full original negative-frequency operator, even before the negative pole is included.

**Next actionable obligation:** Establish a whole-original-operator inverse response on the physical odd carrier, or a genuinely expanded positive reference with enough dimension and certified full cross coupling. The low-rank reference class should not be revisited as a terminal certificate.

**Replay:** \`python scripts/validate_rpb108_sm04_negative_packet_rank.py\`. Passing exact rational inequalities certify this operator-theoretic obstruction *conditional on* the inherited signed original explicit-formula identity; passing CI is not independent peer review or Lean formalization.
