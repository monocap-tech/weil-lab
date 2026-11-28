# Weil-Lab — IV051
## Original signed Weil positivity on the equal-cell-mean subspace and exact arithmetic shift-phase law

**Standing:** New classical/source-aligned mathematical result with **executed exact-Fraction preflight PASS**. **NONKERNEL**: no newly compiled Lean theorem, no `.olean` receipt, no `#print axioms` audit of IV051. The real original Gamma Fourier-atom/operator-domain bridge from IV043/PI007–PI008 remains a formal dependency. No new branch, PR, workflow, dispatch, or heavy CI was introduced.

**Preserved data:** The complete source signed zeta Weil form on the original logarithmic window
\(I=(-11/10,11/10)\), Fourier convention \(\widehat f(\xi)=\int e^{-2\pi i\xi x}f(x)dx\), actual NF599 quarter-digamma real Gamma symbol, source von Mangoldt double shifts at precisely \(n=2,3,4,5,7,8,9\), first-slot-anilinear Hermitian mixed pairing, and both original Mellin crossed pole residues. The correct form is
\[
 W[f]=\gamma(0)\|f\|_2^2+D[f]-P[f]
       +|\langle h,f\rangle|^2-|\langle k,f\rangle|^2,
 \quad h=\sqrt2\,\mathbf1_I\cosh(x/2),\quad k=\sqrt2\,\mathbf1_I\sinh(x/2),
\]
with \(D[f]=\tfrac12\iint K(x-y)|f(x)-f(y)|^2dxdy\), \(K(s)=e^{-|s|/2}/(1-e^{-2|s|})\) off the diagonal, and the *actual* original prime sum \(P[f]=\sum_{n} \kappa_n\langle f,(U_{\log n}+U_{-\log n})f\rangle\), \(\kappa_n=\Lambda(n)/\sqrt n>0\). These remain physical-source classical identities pending a source-specific compiled Lean Gamma inversion and form-domain attachment.

## 1. Main IV051 fixed-mesh original signed theorem

Set \(L=|I|=11/5\), \(M=100000\), \(w=L/M=11/500000\). Let \(J_j\) be the 100000 equal physical intervals, \(\Pi_M\) their \(L^2\)-cell-average projection, and \(Q_M=1-\Pi_M\). Define the **equal-cell-mean Schwartz class**
\[
 \mathcal S_{\mathrm{equal}}:=\left\{f\in C_c^\infty(I;\mathbb C):
 \int_{J_0}f=\int_{J_1}f=\cdots=\int_{J_{M-1}}f\right\}.
\]
It is an infinite-dimensional complex linear subspace containing nonzero low-average directions: for example, place a smooth bump of the same integral strictly inside each cell and add arbitrary zero-mean smooth perturbations.

**Theorem (classical mathematics; Lean OPEN).** Every nonzero \(f\in\mathcal S_{\mathrm{equal}}\) satisfies the **complete original signed** coercivity estimate
\[
\boxed{\operatorname{Re}W_{\mathrm{original}}(f,f)>\frac{19}{500}\|f\|_2^2.}\tag{IV051-main}
\]
No phase, parity, or pole-null hypothesis is imposed. This strictly enlarges IV047's high-mode-only positivity theorem by including a genuine nonzero physical-cell-constant low direction. It does **not** include arbitrary low cell-average patterns; it does **not** establish the RH-facing full-window/global Weil positivity theorem or equivalence with an independent PI/CP spectral object.

### Step 1. High complement: dramatically sharpen IV047's pole cost

The real original NF599 finite positive-gain certificate used by IV047 at \(|t|\ge26000\) gives \(\gamma(t)>8091/1000\). The exact 100000-cell Fourier lowband upper fraction is \(\beta=(23837/125000)^2\), with global \(\gamma(t)>-28/5\). Consequently for every high \(q\in Q_M\) in the logarithmic form domain,
\[
 \Gamma[q]>
 \left[\frac{8091}{1000}-\left(\frac{8091}{1000}+\frac{28}{5}\right)\beta\right]\|q\|_2^2.
\]
All genuine prime coefficients are bounded by the upstream exact original operator estimate \(P[q]<(71/10)\|q\|_2^2\).

Crucially, **the negative original pole does not cost a uniform \(12/25\) on a cell-mean-zero vector**. Since \(k'=h/2\), and \(\int_{J_j}q=0\), the sharp cellwise Neumann Poincaré inequality applied to \(k\) gives
\[
 |\langle k,q\rangle|^2\le\|Q_Mk\|_2^2\|q\|_2^2
 \le\frac{w^2}{\pi^2}\|k'\|_2^2\|q\|_2^2
 <\frac5{36}w^2\|q\|_2^2.
\]
The positive even pole is retained (and may be dropped only for a *lower bound*). The genuine signed high complement therefore satisfies
\[
\boxed{
 W[q]>c_*\|q\|_2^2,\quad
 c_*:=\frac{8091}{1000}-\left(\frac{8091}{1000}+\frac{28}{5}\right)\beta
      -\frac{71}{10}-\frac5{36}w^2>\frac{49}{100}.
}\tag{IV051-high}
\]
The last strict rational inequality is independently checked by the IV051 script. The older IV047 bound was only \(>1/100\). **This is an improved positive form lower bound**, not a new negative-spectrum conclusion.

### Step 2. The genuine original full Weil form on the normalized constant physical indicator

Write \(e:=\mathbf1_I/\sqrt L\), so \(\|e\|_2=1\). IV045's original-source exact arithmetic gave the previously established enclosure
\[
 0.0402<W[e]<0.0405,
 \quad\text{in particular } W[e]>\frac{201}{5000}.\tag{IV051-low}
\]
This includes **every** original n=2,3,4,5,7,8,9 prime-power shift and both genuine crossed Mellin pole residues. Its original finite form-domain interval-indicator derivation is a classical result; the current checker pins and reruns that exact source arithmetic, rather than assuming a newly proven Lean theorem.

### Step 3. The full low/high coupling of this low direction is small, despite IV048's nonvanishing operator norm

On \(x\in I=(a,b)\), the original physical Gamma potential of \(e\) is
\[
 \Gamma e(x)=\gamma(0)e(x)+L^{-1/2}\left[H(x-a)+H(b-x)\right],
 \qquad H(s)=\int_s^\infty K(u)du.
\]
The \(\gamma(0)e\) term is killed by \(Q_M\). The exact \(H\) has the IV048/049 closed expression \(\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2})\). Using
\[
 \left|K(s)-\frac1{2s}\right|\le1,
 \qquad K(s)\le\frac1{2s}+1,
\]
we bound one endpoint potential as follows. On its first cell the centered logarithmic profile \(\tfrac12(-\log u)\) has \(L^2\) standard deviation \(1/2\), with an error at most \(w\). On the \(j\)-th subsequent cell, \(j\ge1\), its oscillation is at most \(1/(2j)+w\). Thus
\[
 \left\|Q_M\frac{H(x-a)}{\sqrt L}\right\|_2^2
 \le\frac1M\left[(1/2+w)^2+\frac12+18w+Mw^2\right]<\frac1M.
\]
The harmonic bound \(\sum_{j=1}^{M-1}j^{-1}<18\) is witnessed by 17 dyadic blocks (\(M<2^{17}\)), and \(\sum j^{-2}<2\). The reflected endpoint has the same bound. Hence
\[
\boxed{\|Q_M\Gamma e\|_2<\frac2{\sqrt M}.}\tag{IV051-Gamma-column}
\]

Every genuine source prime shift \(d=\log n\) lies strictly within \((w,L-w)\), even \(n=9\), by exact logarithmic bounds. Each \(U_{\pm d}e\) has just **one fractional step inside the physical window**, so its cell-mean-zero projection obeys \(\|Q_MU_{\pm d}e\|_2\le1/(2\sqrt M)\). Using the upstream true original \(2\sum_n\kappa_n<71/10\),
\[
\boxed{\|Q_MP e\|_2<\frac{71}{20\sqrt M}.}\tag{IV051-prime-column}
\]

Finally, because \(e\) is even, \(\langle k,e\rangle=0\). Since \(h'=k/2\), \(\|h\|^2<5\), and \(\|k\|^2<1/2\), cellwise Poincaré gives
\[
\boxed{\|Q_M(|h\rangle\langle h|-|k\rangle\langle k|)e\|_2<\frac w3.}\tag{IV051-pole-column}
\]
Therefore for the **complete original source**, with \(B_M=Q_MW\Pi_M\),
\[
 \boxed{\|B_Me\|_2<\frac2{\sqrt M}+\frac{71}{20\sqrt M}+\frac w3
                    <\frac6{\sqrt M}.}\tag{IV051-mixed}
\]
This is **direction-specific**. It does not contradict IV048's and IV050's global bounds on \(\|B_M\|\) for arbitrary dense low vectors.

### Step 4. Complete the Schur inequality, without computing the infinite inverse

Every \(f\in\mathcal S_{\mathrm{equal}}\) decomposes orthogonally as \(f=\alpha e+q\), \(q\in Q_M\), and \(\|f\|^2=|\alpha|^2+\|q\|^2\). Although the piecewise \(q=f-\alpha e\) is not generally Schwartz, it belongs to the closed logarithmic Gamma form domain, in which the IV047 high-mode estimate extends. Apply the actual Hermitian original mixed form and Young's inequality:
\[
\begin{aligned}
 W[f]&\ge\frac{201}{5000}|\alpha|^2-\frac{12}{\sqrt M}|\alpha|\|q\|+\frac{49}{100}\|q\|^2\\
 &\ge\left(\frac{201}{5000}-\frac{72}{(49/100)M}\right)|\alpha|^2
        +\frac{49}{200}\|q\|^2.
\end{aligned}
\]
At \(M=100000\), the first coefficient equals \(201/5000-72/49000>19/500\); the second is \(49/200>19/500\). This proves (IV051-main) for every nonzero supported complex Schwartz test with equal physical cell averages.

**Strict scope:** a single low physical direction plus the *whole infinite-dimensional high complement* is controlled. The remaining \(M-1\) independent low cell-average directions and their full Schur complement are still unresolved.

## 2. A second exact arithmetic–projection dictionary: fractional prime-shift phase

For arbitrary dense low \(v=\sum_{j=0}^{M-1}a_je_j\), \(e_j=\mathbf1_{J_j}/\sqrt w\), extended by zero outside I, let \(d/w=m+\rho\) with \(m=\lfloor d/w\rfloor\in\mathbb Z\), \(0\le\rho<1\), and extend all coefficients \(a_i=0\) for out-of-range indices. **For arbitrary complex coefficients** the exact identity is
\[
\boxed{
 \|Q_MU_d\Pi_M v\|_2^2
 =\rho(1-\rho)\sum_{j=0}^{M-1}|a_{j-m}-a_{j-m-1}|^2.
}\tag{IV051-phase}
\]
Proof: on output cell \(J_j\), the shifted step function has values \(a_{j-m-1}/\sqrt w\) on a relative fraction \(\rho\) and \(a_{j-m}/\sqrt w\) on the other \(1-\rho\); subtracting its exact mean leaves weighted variance \(\rho(1-\rho)|a-b|^2\). This works for \(d>0\), \(d<0\), and arbitrary complex \(a_j\), including genuine boundary truncation. No asymptotic argument or surrogate arithmetic graph is used.

The prime low/high block consequently has the *actual source-projection* upper bound
\[
 \|Q_MP\Pi_M\|
 \le4\sum_{n\in\{2,3,4,5,7,8,9\}}
 \frac{\Lambda(n)}{\sqrt n}\sqrt{\rho_{n,M}(1-\rho_{n,M})},
 \qquad \rho_{n,M}=\{(M/L)\log n\}.
\]
Exact outward **rational** logarithm/square-root enclosures for all seven shifts verify
\[
\boxed{\|Q_{100000}P\Pi_{100000}\|<\frac{29}{5}=5.8,}
\qquad
\boxed{\|Q_{132000}P\Pi_{132000}\|<\frac{13}{2}=6.5.}\tag{IV051-prime-block}
\]
The pole low/high block is actually \(O(w)\), because \(h\) and \(k\) are smooth:
\[
\|Q_M\mathrm{Pole}\,\Pi_M\|\le\frac w\pi\|h\|_2\|k\|_2<\frac{2w}{3}.
\]
Combined with IV050's full dense Gamma block \(<22\), this sharpens the **whole original signed** mixed norm at the existing meshes to
\[
\boxed{\|Q_{100000}W\Pi_{100000}\|<28,\qquad
       \|Q_{132000}W\Pi_{132000}\|<29.}\tag{IV051-dense-refinement}
\]
These remain far too coarse for *all* low directions at M=100000, but they improve IV050's prior universal \(<35\) and explain a new exact mesh arithmetic dependence. The fractional phase \(\rho_{n,M}\) is **coordinate/projection dependent**; it is not independently an intrinsic spectral invariant. A proposed PI/CP equivalence would need to transport the underlying translation operator and physical projection, not merely these numerical phases.

## 3. Reproducibility, precise nonclaims, and CI status

The standard-library script `IV051_equal_mean_schur_checker.py` was executed and **PASSED**. It binds the exact predecessor checkers IV045/047/049/050 by SHA-256, checks the 100000-cell original high-mode improvement and Young margin using Fraction, derives prime support geometry from 128-term rational arctanh-log intervals, encloses the fractional prime shifts for both historical meshes, verifies complex two-piece shift mean/variance identities with signed boundary truncation, and writes `IV051_equal_mean_schur_receipt.json` with a hash of its own unchanged source. All arithmetic assertions passed; the script does **not** prove the continuum Fourier inversion, Poincaré inequality, form closure, or Hilbert–space Schur theory and is **not** a Lean kernel certificate.

**Current source/CI lineage observation:** The previous IV023 head SHA `17deb63f…` was superseded by SHA `b966f42cd51541a78c060b1cc22f0edab142f800` on PR #805. That one four-file commit *did* source-scope historical NF456 and the NF471 receipt workflow, and moved the pinned `lake update`/manifest creation before the unchanged IV018/IV023 source preflights, with source-specific Lean/axiom steps still present. However the updated 611-workflow branch also visibly retains **other unscoped historical PR triggers**, e.g. NF453, NF454, NF457 and NF463. A complete trigger/required-check fan-out audit and actual isolated compiler outcome on the new head have NOT been demonstrated. Therefore **no heavy Phase IV Actions was launched** as part of IV051; scoped source delivery may proceed only after the user's controlled-submission gate is met.

**Certification baseline:** NF750–NF753 true original numerical Lean/strict-axiom kernel-passed frontier **692/968**, still distinct from the historical registry body's 628/968 until archive reconciliation. IV009 original Schwartz polarization Lean PASS; IV018 and IV023 prior failures arose in Python preflight before actual Lean proof compilation. IV051 mathematical results do not alter those certificates. Complete original Weil positivity, independent spectral equivalence, and RH remain OPEN.

## 4. Highest-value next tasks (IV052)

1. **Finite-M low-mode certification:** Use the exact shift-phase identity to build the genuine source prime low/high block, and a boundary-adapted Gamma corrector for *smooth/dense* low vectors; distinguish modes near physical boundaries from oscillatory low-grid modes. Seek a genuinely a posteriori lower bound on the entire Schur complement, not simply a positive finite compression.
2. **Original Lean bridge:** Formalize the constant-indicator Gamma boundary potential, the exact cellwise variance identity, and the mean-zero pole derivative bound; maintain source SHA/source Fourier sign/domain custody and standard-only `#print axioms`. The IV051 full coercivity theorem remains a candidate until compiled.
3. **Controlled CI:** Complete all 611-workflow active-head trigger/required-check scope inventory; verify no unrelated PR fan-out and the *real* manifest/source preflight sequence. Stage IV018 and IV023 genuine compilers one at a time, preserving all historic source identity and accepted artifacts; submit an IV051 proof job only when the effective lineage is certified safe.
4. **Cross-projection falsifier:** Test whether proposed independent arithmetic/spectral carriers preserve the exact complex translation variance law and crossed-pole parity, rather than only low-spectrum eigenvalue matches.

**Nonclaims:** This is a fixed-support, fixed-mesh, equal-cell-average infinite-dimensional theorem and a source-specific projection identity. It is not a support-independent/full original Weil positivity theorem, not source-bound Lean PASS, and not RH.
