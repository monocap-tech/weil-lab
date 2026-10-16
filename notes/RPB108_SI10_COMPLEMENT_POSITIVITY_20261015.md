# RPB108 SI10 — direct positivity of the original signed Weil form on a cofinite physical subspace

**Front:** independent Structural Investigation (SI).  
**Parent:** integrated SI09 at \`c62d6d2f7d37cab17586062ab9e60e1a2b7d4dbf\`.  
**Source:** original CC27 signed Weil form, audited in RC312–313; SI06 actual seven-prime Fourier multiplier positivity for \(|\xi|\ge896\); SI07/08 support-preserving signed interval/tail machinery.  
**Standing:** conditional on certified exact-rational validator, a **direct nonnegative/strictly positive original complete Weil form** on a closed physical **finite-codimensional subspace**. This is NOT positivity on the omitted finite span, a full signed Schur/Stage I completion, transport to RH, or Lean formalization.

## 1. The new question is positivity, not simply reducing approximation rank

The original supported physical quadratic form, on its polynomial/regular form core and by continuity where defined, is
\[
Q_{\rm Weil}(f)=\int_{\mathbb R}m(\xi)|\widehat{Zf}(\xi)|^2\,d\xi
+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2,
\]
where \(I=[-B,B]\), \(B=11/10\), \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\), \(Z\) is zero extension and
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}
\cos(2\pi\xi\log n).
\]

Prior SI05–09 derived *accurate approximations to the negative part*. Those approximations do not, by themselves, prove any lower bound on \(Q_{\rm Weil}\). SI10 instead introduces a **protected positive frequency margin**, and requires both the negative term and the mass that escapes into the uncertain frequency cover to be quadratically tiny on the orthogonal complement.

## 2. Protected positive multiplier and certified uncertain-band cover

Fix \(\kappa=1/1000\). Let \(U\) denote the union of rational unresolved dyadic intervals (and their reflections), constructed as follows.

On each integer cell \([j,j+1]\), \(0\le j<896\), Euler's exact positive quarter-digamma series gives the monotone archimedean lower bound \(A_j\) used in SI07. SI06's original seven-prime rational cosine enclosures and global derivative bound \(|p'|<69\) imply for every dyadic interval \([l,r]\) centered at \(x\),
\[
m(\xi)\ge
L_{l,r}:=A_j+p_{\rm lower}(x)-\frac{69}{2}(r-l)
\quad\text{at every }\xi\in[l,r].
\]
Certify a whole interval as **protected positive** only if \(L_{l,r}>\kappa\). Otherwise subdivide at most six times and include any remaining interval in \(U\), even when its true sign is unknown. This ensures
\[
\boxed{m(\xi)>\kappa\quad (\xi\notin U,\ |\xi|<896).}
\]
On \(896\le|\xi|\le1200\), the SI06 certified monotone archimedean bounds and signed-prime derivative-based dyadic enclosures are replayed with the **stronger positivity threshold \(\kappa\)**. For \(|\xi|\ge1200\), the original digamma monotone lower envelope satisfies \(a_{\rm arch}(\xi)-2C>\kappa\) independently of the prime phases, using the full original seven-prime scalar \(2C\), **not** SI03's physically truncated operator bound. Thus
\[
\boxed{m(\xi)>\kappa\text{ on the entire real complement of }U.}
\]

Each remaining unresolved dyadic leaf \(L=[l,r]\) has the exact outward cap
\[
0\le m_-(\xi)\le h_L:=10^{-6}\max\{0,\lceil 10^6(-L_{l,r})\rceil\}
\quad (\xi\in L).
\]
Let \(W=|U|\) count both positive and negative frequencies, and let \(M=2\sum_{\text{positive leaves}}|L|h_L\) be the rigorously covered full negative multiplier mass. SI10's validator checks both by **exact rational** summation, without inferring any sign or size from floating-point grids.

## 3. Physically supported finite-span complement theorem

Let \(I_j=[a_j,b_j]\) denote the maximal connected groups in the positive-frequency half of \(U\), with centers \(c_j=(a_j+b_j)/2\), widths \(w_j=b_j-a_j\), and corresponding reflected groups.

For each selected integer \(b\ge1\), choose Taylor orders \(p_j\) through SI08's exact rational test
\[
\varepsilon_j=\frac{[(22/7)Bw_j]^{p_j}}{p_j!}<2^{-b}.
\]
Let the finite dimensional physically supported complex span be
\[
V_b=\operatorname{span}\{e^{\pm2\pi ic_jx}x^k\mathbf1_I:
0\le k<p_j,\ j=1,\dots,J\}
+\operatorname{span}\{s\}.
\]
All functions are smooth on the finite physical support and lie in the natural original Weil form domain. Their physical zero extensions need not be bandlimited, nor is a Fourier cutoff being applied to the inputs.

For \(f\in V_b^\perp\), where orthogonality is physical \(L^2(I)\), each plane wave on a covered frequency cluster has a Taylor approximant inside \(V_b\) with \(L^2\)-error at most \(\sqrt{2B}2^{-b}\). Hence by Cauchy–Schwarz,
\[
\boxed{\int_U|\widehat{Zf}(\xi)|^2\,d\xi
\le 2B\,W\,2^{-2b}\|f\|_2^2.}
\]
Likewise, use the **actual signed-negative weight cap** on each leaf:
\[
\boxed{\int_U m_-(\xi)|\widehat{Zf}(\xi)|^2\,d\xi
\le 2B\,M\,2^{-2b}\|f\|_2^2.}
\]
The original *negative odd pole* vanishes exactly for \(f\in V_b^\perp\), because \(s\in V_b\). The original positive even pole is retained and discarded only in the safe lower bound.

Combine Parseval \(\int_{\mathbb R}|\widehat{Zf}|^2=\|f\|_2^2\) and \(m\ge\kappa\) outside \(U\):
\[
\begin{aligned}
Q_{\rm Weil}(f)
&\ge \kappa\int_{U^c}|\widehat{Zf}|^2-
\int_Um_-|\widehat{Zf}|^2\\
&\ge
\boxed{\left[
\kappa(1-2BW\,2^{-2b})-2BM\,2^{-2b}
\right]\|f\|_2^2.}
\end{aligned}
\]
This is a **direct whole-original-form lower bound on a finite-codimensional closed physical subspace**. It neither assumes the initial 301-dimensional RC Schur floor nor falsely turns an approximation of the negative operator into positivity of the complete form.

If the bracket is strictly positive, the form is strictly positive on \(V_b^\perp\cap\operatorname{Dom}Q_{\rm Weil}\). In particular its negative spectral index is bounded by \(\dim V_b\), provided the standard closed-form realization is used. This positive \(L^2\) lower bound is not automatically a uniform \(D\)-coercivity bound because the \(D\)-norm is stronger at high degree.

## 4. Exact computational gate and competitiveness

The GitHub Actions standard-library \`Fraction\` validator:
1. Reconstructs the complete original signed \(0\le|\xi|\le896\) protected-positive cover with \(\kappa=1/1000\);
2. Replays whole \(896\le|\xi|\le1200\) positivity **above \(\kappa\)** and the analytic \(|\xi|\ge1200\) bound;
3. Computes outward rational \(W,M\) and all physically supported Taylor orders for \(b\in\{9,10,12,16,32\}\);
4. Accepts a claim only if its exact positive coefficient exceeds \(1/2000\), including the complete negative pole and every unknown frequency leaf.

The complete original signed certified Fourier audit on the first GitHub Actions replay gives:

- Whole protected nonnegative-frequency cutoff: \(m(\xi)>1/1000\) outside the certified uncertain cover (including **all frequencies above 896**).
- On \(0\le\xi<896\): 9,261 strictly protected-positive dyadic cells, 973 unresolved leaves in 107 grouped positive-frequency intervals, and both reflected intervals.
- The full rational uncertain-band cover has **total width \(W=30.40625\)**; the genuine negative-frequency mass satisfies \(M\le37.59565259375\).
- On \(896\le\xi\le1200\): 2,535 intervals positively certified above \(1/1000\); minimum rational lower certificate \(>0.0036925\). For all \(|\xi|\ge1200\), the monotone digamma bound also exceeds \(1/1000\).

For compactly supported modulated-polynomial spans \(V_b\) including the exact signed odd pole vector, the resulting **entire original signed Weil form** obeys:

| Local approximation bits | Sufficient physical codimension \(\dim V_b\le\) | Certified physical lower bound on \(V_b^\perp\) |
|---:|---:|---:|
| 9 | **939** | \(Q_{\rm Weil}(f)>(68/100000)\|f\|_2^2\) |
| 10 | 1003 | \(Q_{\rm Weil}(f)>(92/100000)\|f\|_2^2\) |
| 12 | 1121 | \(Q_{\rm Weil}(f)>(995/1000000)\|f\|_2^2\) |
| 16 | 1367 | \(Q_{\rm Weil}(f)>(999/1000000)\|f\|_2^2\) |
| 32 | 2151 | \(Q_{\rm Weil}(f)>(999/1000000)\|f\|_2^2\) |

The first source replay also reports larger actual outward rational margins (approximately \(0.0006842295477,\,0.0009210573869,\,0.0009950660867,\,0.0009999807269,\,0.001\), respectively). The table uses deliberately weaker **rational inequalities**, now mandatory in the validator. The \(b=9\) case is the smallest certified codimension among these five constructions and yields the direct **whole-original-form** positive complement statement on an infinite-dimensional closed physical subspace of codimension at most **939**.

The finite exceptional block of size ≤939 and its cross-couplings remain open. The RC314 argument already has a tighter **301-dimensional** possible-negative-sector localization in a different \(D\)-Riesz representation: SI10 is therefore a separate structural positivity construction, **not** a computational shortcut relative to the RC chain.

**Comparison:** RC314 already certified possible nonpositive directions in a 301-dimensional low space through the actual \(D\)-Riesz model. This SI10 route may produce a larger codimension and is **not** a more efficient Stage I proof by itself. Its distinction from SI05–09 is that it establishes an actual **positive original Weil form** on the certified complement, not only a small negative-operator approximation residual.

The finite-dimensional block \(V_b\), its couplings to \(V_b^\perp\), and the required actual signed Schur positivity remain unresolved. A positive diagonal compression on \(V_b^\perp\) alone cannot establish positivity of the full operator.

**SI11:** choose a reference \(b\) that balances codimension and physical gap; derive an explicitly paid finite-dimensional *correct-sign* Schur/Dirichlet-to-Neumann criterion using the original form and its native couplings, and check whether this is competitive with RC331's smaller \(D\)-Riesz positive complement. Avoid replacing a 301-dimensional problem with a larger unverified numerical inverse.

## Reproduce

\`python scripts/validate_rpb108_si10_complement_positivity.py\`

The mathematical proof invokes original RC312–313 Fourier source identification, exact Euler's digamma series, Plancherel, compact physical support, and the classical real-phase Taylor remainder. CI regression checks numerical rational margins, but is not independent peer review or Lean formalization. Full Stage I positivity, the complete F4 bridge, and the Riemann Hypothesis remain open.
