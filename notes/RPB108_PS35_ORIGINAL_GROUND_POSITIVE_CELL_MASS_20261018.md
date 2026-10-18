# PS35 — Actual original pole-free even ground: positive mass in sixteen explicit macroscopic physical cells

**W-PHYSICAL-SHIFT · October 18, 2026 · stacked on PS34 draft PR #203.**

**Scope and honesty.** This is a **genuine original-operator conditional analytic deduction**: given the previously established PS17/18, PS27–PS33 source bounds, the PS28 even-cone order property, and PS29's normalized nonnegative even ground eigenfunction, it produces a **strict, explicit lower** for the ground-state mass **inside each** of sixteen ordinary physical cells of width \(1/256\). That is qualitatively different from PS34's mass *outside* a cell, and it does NOT use PS34's unaudited characteristic-cut eigenvector step. The numerical mass floor remains exponentially tiny, so it does not certify PS31 weighted graph positivity, \(\lambda_1\ge0\), the original restored even pole angle, signed Weil positivity or RH. Independent mathematical audit of the original infinite-dimensional premises remains required.

## 1. Fixed true original operator and sixteen physical cells

Work on \(I=[-B,B]\), \(B=11/10\), in the exact PS15 complement \(C\) of all thirteen source intervals. Define the original pole-free source-eliminated even operator
\[
L=J_C+V_{0,C}-R,\qquad
R=B_0^*A_0^{-1}B_0,
\quad A_0>\frac{1997}{9000}I,\quad
\|B_0\|<\frac{1403}{80}.
\]
All seven signed original prime powers \(n=2,3,4,5,7,8,9\), original digamma zero extension and true source Schur response are retained. The positive even pole was removed *before* eliminating the source; on the even sector the negative odd pole is zero.

PS18 certified the true prime-quiet original physical interval
\[
J_{\rm quiet}=[q,q+1/16]\subset C_+,\qquad q=269/5000.
\]
Partition it **exactly** into sixteen nonoverlapping macroscopic subintervals
\[
\boxed{H_j=\left[q+\frac{j}{256},\;q+\frac{j+1}{256}\right],
\quad j=0,\ldots,15,\quad |H_j|=\frac1{256}.}
\]
Let \(E_j=H_j\cup(-H_j)\), physical length \(1/128\), and \(\mu(A)=2\int_A\phi_0^2 dx\) the *actual* PS31 normalized even ground measure on \(C_+\).

The actual PS29 lowest original even pole-free eigenpair is
\[
L\phi_0=\lambda_0\phi_0,\quad
\phi_0\ge0\quad\text{a.e.},\quad
\|\phi_0\|_{L^2(C)}=1,\quad
-1406<\lambda_0<-4.359740.
\]
The lower spectral envelope \(\lambda_0>-1406\) is the original PS31 result; the upper negative witness is true PS27/RC315. No numerical eigenfunction or new spectral index is assumed.

## 2. A bounded original-operator test that **avoids sharp characteristic multiplication**

For each \(j\), let \(c_j=q+(j+\tfrac12)/256\), \(r=1/512\) and define the *globally Lipschitz* even tent function
\[
\boxed{
g_j(x)=\left(1-\frac{||x|-c_j|}{r}\right)_+,\qquad
\operatorname{supp}g_j=E_j.
}
\]
It is nonnegative, has Lipschitz constant at most \(512\), is zero at the physical cell boundaries, and belongs to the **actual original PS15 complementary logarithmic operator domain**, because its zero extension is Lipschitz, the original difference operator is \(L^2\)-bounded on it as proved directly below, and every lower-order/source term is bounded on \(L^2(C)\).

Direct exact physical integral identities:
\[
\boxed{\int_C g_j\,dx=\frac1{256},\qquad
\|g_j\|_2^2=\frac1{384},\qquad |E_j|=\frac1{128}.}
\]
For the **actual original digamma operator**, not its finite exponential truncation,
\[
(Jg)(x)=\int_0^\infty k(u)\,[2g(x)-g(x-u)-g(x+u)]\,du,
\quad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\]
The genuine PS18 bound \(k(u)\le1/(2u)+1\) for \(0<u\le1\), together with \(k(u)<2e^{-u/2}\) for \(u\ge1\), and the tent Lipschitz/height bounds give, for **every** physical or full-line \(x\),
\[
\begin{aligned}
|Jg_j(x)|
&\le 2\int_0^\infty k(u)\min(512u,1)\,du\\
&<1+\frac1{512}+\log512+2+8\\
&<18,
\end{aligned}
\]
where \(\log512=9\log2<63/10\) uses the original outward \(\log2<7/10\). Hence \(\|1_CJg_j\|_2<18\sqrt{11/5}<27\).

The actual **bounded original** pole-free even part has
\[
\|V_{0,C}\|<13+\frac{539}{90}<19,\qquad
\|R\|<\left(\frac{1403}{80}\right)^2\frac{9000}{1997}<1387.
\]
Using \(|\lambda_0|<1406\) and \(\|g_j\|_2=1/\sqrt{384}<1/19\), obtain the **same uniform true-original bound for every one of the 16 cells**
\[
\boxed{
\|(L-\lambda_0)g_j\|_{L^2(C)}
<27+\frac{19+1387+1406}{19}
=\boxed{175}.
}
\]
This is the critical *operator-domain* estimate: no characteristic function is applied to \(\phi_0\), and no unknown \(L^\infty\) bound on the true ground is used.

## 3. True original **off-diagonal attraction** forces the ground state into every physical cell

Let \(p=1_{E_j}\phi_0\) and \(z=1_{C\setminus E_j}\phi_0\), **only as L² bookkeeping**; there is no assumption that \(1_{E_j}\phi_0\) belongs to the operator/form domain.

For \(x\in C\setminus E_j\), \(g_j(x)=0\), so the exact original digamma generator satisfies
\[
(Jg_j)(x)=-\int_{E_j} k(|x-y|)g_j(y)\,dy.
\]
The original seven-prime off-diagonal contributions to \(V_{0,C}g_j\) have negative sign on the nonnegative even cone. PS28–PS30 establish that the genuine source response \(R=B_0^*A_0^{-1}B_0\) is positivity preserving on that cone; thus \(-(Rg_j)(x)\le0\) a.e. on \(C\setminus E_j\). The arch scalar times \(g_j\) and the removed positive even pole contribute zero there.

The original physical diameter is \(2B=11/5\). PS30 already proves \(k(u)>3/10\) for \(0<u\le2B\). It follows **for a.e. \(x\in C\setminus E_j\)** that
\[
\boxed{
[(L-\lambda_0)g_j](x)
\le-\frac3{10}\int_{E_j}g_j(y)\,dy
=-\frac3{2560}=:-m_0.
}
\]
No actual prime/source attractive contribution is removed from \(L\); their nonpositive signs make this a rigorous LOWER forcing from the original archimedean kernel.

Self-adjointness and the actual original ground equation give
\[
0=\langle\phi_0,(L-\lambda_0)g_j\rangle
\le \|p\|_2\,\|(L-\lambda_0)g_j\|_2
-m_0\int_{C\setminus E_j}\phi_0.
\]
Since \(\phi_0\ge0\) and \(|E_j|=1/128\),
\[
\int_{C\setminus E_j}\phi_0
=\int_C\phi_0-\int_{E_j}\phi_0
\ge\int_C\phi_0-|E_j|^{1/2}\|p\|_2.
\]
Therefore
\[
\bigl(175+m_0/\sqrt{128}\bigr)\|p\|_2
>m_0\int_C\phi_0,
\quad
m_0=\frac3{2560}.
\]
Because \(175+m_0/\sqrt{128}<176\), exact integer arithmetic shows \(m_0/176>2^{-18}\), hence
\[
\boxed{\|1_{E_j}\phi_0\|_2>2^{-18}\|\phi_0\|_{L^1(C)}.}
\]
This is a positive original **mass-inside** estimate, unlike PS34's outside-mass theorem, and it is valid for **each** of the sixteen explicit physical cells, with no appeal to an unproved physical Harnack principle.

## 4. Combine with the true ORIGINAL PS33 quantitative global L¹ lower

PS33 proves, using the exact original zero-extension Fourier estimate and true PS28 effective \(d\ge1\) cone result,
\[
\boxed{\left(\int_C\phi_0\right)^2>\frac3{8000\cdot2^{2025}}.}
\]
This bound comes from the original \(J[\phi_0]<1401\) source estimate and the optimally selected PS18 digamma Fourier cut, not from a fabricated numerical ground-state eigenfunction. Thus the new direct eigen-equation test certifies for **every \(j=0,\ldots,15\)**
\[
\boxed{
\mu(H_j)=\int_{E_j}\phi_0^2
>\frac3{8000\cdot 2^{2061}}>0.
}
\]
The sixteen cells are mutually disjoint up to null endpoints, so in particular
\[
\boxed{
\mu(J_{\rm quiet})=\sum_{j=0}^{15}\mu(H_j)
>\frac3{500\cdot2^{2061}}.
}
\]
**This is the first explicitly quantified original ground-state positive lower mass on each of 16 actual macroscopic source-complement cells in the PS chain.** It does not determine any of those masses to useful numerical precision, bound \(\phi_0\) pointwise from above, or certify PS31's physical \(w_{ij}= \operatorname*{ess\,inf} K_N/(2\phi_0(x)\phi_0(y))\).

## 5. Acceptance limits and next obligation

A \(2^{-2061}\)-scale positive original ground mass is **not** comparable to a practical spectral-gap acceptance margin of size \(>4.359740\); multiplying a microscopic positive lower by sixteen does not change that. The PS31 graph still needs genuine useful physical lower weights \(w_{ij}\), within-cell original short-distance digamma coercivity, and an upper on actual \(|\lambda_0|\) tight enough to compare with its weighted Poincaré gap. Nor does this imply PS29 effective-pole angle \(\Delta>0\). The source-cone preservation, original continuous-kernel generator/domain, and original ground eigenspace all require independent audit.

**PS36:** use the actual original even pole-free ground equation on each cell to sharpen the interior forcing and improve the exponentially weak PS33 global \(L^1\) estimate (or obtain usable local upper ground-profile bounds), then evaluate genuine original PS31 \(w_{ij}\) and the second eigenvalue sign. A different direct one-negative-index route remains legitimate if local graph estimates stay noncompetitive. Do not substitute a finite toy operator for the original physical form.

**Custody:** Explicit PS-scoped NF, canonical W-ODD-NEG active and open. No W-EVEN-FORM, W-ODD-NEG, complete original Weil, CC27 D-Riesz bridge, or RH closure. The PS34 job's result must be verified independently before claiming it passed; PS35's exact Fraction regression likewise does not independently formalize infinite-dimensional source-order assumptions.

Replay: \`python3 scripts/validate_rpb108_ps35_original_ground_positive_cell_mass.py\`.
