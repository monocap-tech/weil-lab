# PI032 — Explicit nine transversal first-prime prime/Gamma cancellations

**Weil-Lab Potential Interface / controlled reopening.** Parent branch: \`research/pi031-exact-nine-first-prime-cancellation-signs\`; original source ledger PI027, source SHA \`14d8f01ce34f764900eccc68399d7323b4f4a25c\`; registry #792. **New classical theorem:** the fixed explicit PI031 smooth test (\(m=1\), rational relative amplitude \(u=3/2\)) has **at least nine distinct genuine n=3 prime/Gamma cancellation roots with nonzero original phase derivatives**. Each is the *unique* root within its stated rational bracket. The **total** count over the first-prime window is still unknown. The proof uses exactly outward-rounded Python integer arithmetic plus explicit analytic derivative estimates; it is NOT a Lean kernel theorem, a certified zeta zero computation, an operator trace, global signed Weil positivity, or RH.

## 1. Fixed original source test and derivative problem

Use \(d=\log(10/9)\), \(\ell=d/100\), \(\Delta=d/2\), \(x_0=d/5\), \(u=3/2\), the explicit flat bump \(g(y)=\exp[-1/(y(1-y))]\) for \(0<y<1\) (zero elsewhere), \(b_\ell(x)=g(x/\ell)\), \(\rho=b_\ell(\cdot-x_0)+u b_\ell(\cdot-x_0-\Delta)\), \(L_1=D(D^2-1/4)\), and \(\phi=L_1\rho\). All source signs, pole moments, actual von Mangoldt weights, Hermitian autocorrelation orientation, and source Gamma distribution are inherited *unchanged* from PI027.

Write \(E(y)=g'''(y)-\delta g'(y)\), \(\delta=\ell^2/4\); then \(\eta=L_1b_\ell=\ell^{-3}E(\cdot/\ell)\). Its correlation \(Q(t)=\int\eta(x)\eta(x-t)dx\) satisfies
\[
Q(\ell\tau)=\ell^{-5}\mathcal I(\tau),\qquad
\mathcal I(\tau)=\int_\tau^1 E(y)E(y-\tau)dy
\quad(0\le\tau\le1).
\]
\(\mathcal I\) extends to an even smooth compact correlation on \(\mathbb R\), because \(E\) is smooth/flat and supported in [0,1].

The full actual two-subbump correlation is
\[
C(t)=\frac{13}{4}Q(t)+\frac32Q(t-\Delta)+\frac32Q(t+\Delta),\quad
J=C(0)=\frac{13}{4}\ell^{-5}\mathcal I(0).
\]
Throughout \(a=\log3-t\), \(0\le t\le d\), the **only** original finite prime term is
\[
P(a)=\kappa C(\log3-a),\quad\kappa=\log3/\sqrt3>1/3,
\]
and the exact original phase law is
\[
W(h_{\beta,a})=W(C)+[B(a)-P(a)]\Re\beta,\qquad
\Theta(a)=B(a)-P(a).
\]
The original gamma amplitude \(B(a)>0\), and PI030's support estimate is \(B(a)<J/450\). No RH or spectral assumptions enter.

## 2. Uniform original Gamma **derivative** bound

For \(s>0\), \(K(s)=e^{-s/2}/(1-e^{-2s})\) obeys
\[
\frac{-K'(s)}{K(s)}
=\frac12+\frac{2e^{-2s}}{1-e^{-2s}}.
\]
On the entire n=3 separation window, the physical Gamma arguments satisfy \(s\ge a-d\ge\log(243/100)>\log2\). Thus
\[
K(s)\le K(\log2)=2\sqrt2/3<1,\qquad
|K'(s)|<\frac12+\frac23=\frac76.
\]
Differentiate the absolutely convergent off-contact physical interaction, then Cauchy–Schwarz on the union of two supports of total length at most \(2\ell=d/50<1/450\):
\[
\boxed{|B'(a)|\le\frac76\Bigl(\int|\phi|\Bigr)^2
\le\frac76(2\ell)J<\frac{7J}{2700}.}
\]
The physical integral used here is only the **phase interaction**, away from the contact \(h(0)\) distribution. No divergent naive diagonal Gamma integral is taken.

Multiply by \(\ell^6\), noting \(\ell<1/900\) and \(J\ell^5=(13/4)\mathcal I(0)<(13/4)21\):
\[
\boxed{0<\ell^6|B'(a)|<
\frac7{2700}\frac{13\cdot21}{4\cdot900}<\frac1{1000}.}
\]
Likewise \(\ell^5B(a)<(13/4)21/450<1/5\). These are conservative exact rational comparison bounds.

## 3. New exact integer interval results for \(\mathcal I\), \(\mathcal I'\), and \(\|\!E'\!\|_2^2\)

The companion standalone \`scripts/pi032_exact_interval_transversality.py\` uses \`fractions.Fraction\` and outward-rounded signed integer intervals at scale \(S=10^{40}\). Its rational coefficients enclose the true \(\delta\) in \([1/4{,}000{,}000,1/3{,}240{,}000]\); it never substitutes a rounded floating-point value for d. For each pointwise integral it uses 4096 midpoint cells and an explicitly enclosed \(h^2\sup|f'|/4\) error per cell. A 512-cell check recovers \(17<\mathcal I(0)<21\).

For \(L(y)=-1/[y(1-y)]\), \(T=1/[y(1-y)]\), \(c=1-2y\), exact source-free calculus gives
\[
\begin{aligned}
L'&=cT^2,\\
L''&=-2T^2-2c^2T^3,\\
L'''&=12cT^3+6c^3T^4,\\
L''''&=-24T^3-72c^2T^4-24c^4T^5,\\
L'''''&=360cT^4+480c^3T^5+120c^5T^6.
\end{aligned}
\]
The code evaluates \(E,E',E''\) by the exact Bell-polynomial formulas for \(g''',g'''',g'''''\), including \(-\delta g'\), \(-\delta g''\), \(-\delta g'''\). The remaining flat endpoint regions use directly proved bounds \(|E|<1/4\), \(|E'|<112\), \(|E''|<62000\), valid for \(T\ge20\). An exact rational truncated series through degree 24 establishes \(e^{20}>4\cdot10^8\); each \(T^ke^{-T}\) decreases for \(T\ge20\), \(0\le k\le10\). Exponential interval evaluation uses alternating-series lower/upper sums (odd/even degrees) after repeated-halving of the positive argument, followed by outward-rounded squaring.

The **strict rational acceptance results** for three brackets \(I_j=(l_j,r_j)\subset(0,1)\) are:

| \(j\) | Rational \(\tau\)-bracket \((l_j,r_j)\) | \(\mathcal I(l_j)\) | \(\mathcal I(r_j)\) | \(\mathcal I'(c_j)\), \(c_j\) rational |
|---|---|---|---|---|
| 1 | \((106/1000,115/1000)\) | \(>2/5\) | \(<-1/3\) | \(<-90\), \(c_1=111/1000\) |
| 2 | \((477/1000,490/1000)\) | \(<-2/5\) | \(>2/5\) | \(>65\), \(c_2=484/1000\) |
| 3 | \((692/1000,704/1000)\) | \(>2/5\) | \(<-1/3\) | \(<-75\), \(c_3=698/1000\) |

The independently enclosed norm satisfies
\[
\boxed{0<\int_0^1|E'(y)|^2dy<9000.}
\]
As \(E\) is flat at the boundaries, differentiating the autocorrelation and integrating by parts gives
\[
\mathcal I'(\tau)=-\int E(y)E'(y-\tau)dy,\quad
\mathcal I''(\tau)=-\int E'(y)E'(y-\tau)dy,
\]
hence by Cauchy–Schwarz
\[
\boxed{|\mathcal I''(\tau)|\le\|E'\|_2^2<9000.}
\]

The largest distances \(|\tau-c_j|\) within these brackets are, respectively, \(5/1000,7/1000,6/1000\). Therefore on the **entire brackets**, not just at midpoint samples:
\[
\boxed{\begin{array}{c|c}
I_1&\mathcal I'(\tau)<-90+9000(5/1000)=-45\\
I_2&\mathcal I'(\tau)>65-9000(7/1000)=2\\
I_3&\mathcal I'(\tau)<-75+9000(6/1000)=-21.
\end{array}}
\]
In particular \(|\mathcal I'|>2\) on every bracket, with known sign.

**Local reproducibility:** all four independent parts of the exact script, invoked \`--part core\`, \`--part 1\`, \`--part 2\`, and \`--part 3\`, passed in the local execution environment. Printed approximate decimal endpoints are diagnostic only; every acceptance assertion is an exact rational/integer comparison. The primary numerical evidence is the integer-interval certificate, not the separate SciPy exploration used to choose these rational brackets.

## 4. The nine **simple**, live and unique-in-bracket original cancellations

Write \(t=\log3-a\). In the **central** sector \(t=\ell\tau\) (\(\tau>0\)), \(\ell^5P=\kappa(13/4)\mathcal I(\tau)\). In the two **satellite** sectors \(t=\Delta\pm\ell\tau\), \(\ell^5P=\kappa(3/2)\mathcal I(\tau)\); note that \(\mathcal I\) is even, so its derivatives have opposite signs for the mirrored satellite.

At positive \(\mathcal I\)-endpoint controls, \(\ell^5P>(1/3)(3/2)(2/5)=1/5>\ell^5B\), so \(\Theta<0\). At negative \(\mathcal I\)-endpoint controls, \(P<0<B\), so \(\Theta>0\). Thus **each bracket has a phase sign change**, once in the central sector and once in each of the two symmetric satellite sectors: at least nine roots.

For any \(a\) in any of these nine brackets, differentiating the ORIGINAL \(n=3\) source law gives
\[
\boxed{\Theta'(a)=B'(a)+\kappa\,C'(\log3-a).}
\]
The derivative of \(C\) is the corresponding channel coefficient (central \(13/4\), satellite \(\pm3/2\)) times \(\ell^{-6}\mathcal I'(\tau)\). Therefore
\[
\ell^6|\kappa C'|>\frac13\frac32\cdot2=1
\qquad\text{while}\qquad
\ell^6|B'|<\frac1{1000}.
\]
Consequently \(\Theta'\) is **strictly nonzero with fixed sign throughout each bracket**, and each bracket contains **exactly one** root (IVT plus strict monotonicity). All nine roots are distinct because the physical sector brackets do not overlap, and each root is **transversal/simple**. At each one,
\[
\boxed{B(a_*)=P(a_*)>0,\quad \Theta'(a_*)\ne0,\quad
W(D_{a_*})=0,\quad W(h_{\beta,a_*})=W(C)\ \ (|\beta|=1).}
\]

This is a rigorous constructive transversality instance at the **specific rational amplitude \(u=3/2\)**, strengthening PI030's almost-every-amplitude theorem and PI031's nine-crossing count. It does **not** prove that there are no other roots outside these nine brackets.

## 5. Verification boundary, cross-projection fingerprint and CI

- **Original source:** literal IV011 pole-minus-prime-plus-Gamma normalization and original \(n=3\) von Mangoldt coefficient \(\log3/\sqrt3\), with unchanged source blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\`, as reopened in PI031.
- **Classical numerical proof:** four separate exact Python Fraction/outward-integer subcertificates plus analytic Gamma derivative, integration by parts, Cauchy–Schwarz and IVT. Not independently Lean-certified; root count \(\ge9\), not \(=9\).
- **Spectral dictionary:** the full off-critical complex shifted Mellin response remains required for CP comparison. At a crossing \(W(D)=0\); printed Masullo Ch12 would require \(Z_{12}(D)=0\), while printed Ch13 (if its unfinished distinct trace identity actually applied under the same canonical source) would require \(Z_{13,\rm cap}(D)=2B>0\). None is a computed zero-divisor equality or evidence for RH.
- **CI:** PI032 commits only this mathematical memo and one new Python script, with no PR/Lean module/Actions workflow or dispatch. On the inherited PI branch there are 12 workflow files and 8 source-scoped PR triggers. A PR against main must separately review the *complete stacked diff* for fan-out. Preserve NF's 692/968 original HD/A frontier and strict \`#print axioms\` acceptance requirements.

**Next — PI033:** certify **exhaustive** first-prime root counting by covering the complement of the nine root brackets with outward interval signs (possibly with adaptive subdivision and \(|\mathcal I'|\le\|E\|_2\|E'\|_2\) Lipschitz bounds), and begin a source-bound Lean scalar derivative proof in isolation. Do not claim exact nine, open heavy CI, or identify an independently proved trace equality until those gates are met.
