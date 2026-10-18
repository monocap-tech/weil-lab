# PS31 — Original even ground-state exponential layers and finite weighted graph spectral-gap gate

**W-PHYSICAL-SHIFT · 2026-10-18 · stacked on PS30 draft PR #199.**
Scope: the **actual** original zero-extended, thirteen-source-eliminated, positive-even-pole-**free** seven-prime Schur \(L=\mathfrak S_C^{(0)}|_{\mathrm{even}}\), with PS28's genuine positivity-preserving source inverse and PS29–PS30's compact ground-state form. This is a **new explicit conditional spectral-gap certification architecture**, not an evaluated second-eigenvalue lower bound, restored-even-pole certificate, whole signed Weil theorem or RH. Independent audit of the infinite-dimensional PS28–PS30 assumptions remains necessary.

## 1. A previously unused exact positive exponential decomposition of the ORIGINAL digamma kernel

On the real physical \(I=[-B,B]\), \(B=11/10\), the zero-extended archimedean kernel is **exactly**
\[
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}
=\sum_{j=0}^{\infty}e^{-a_ju},
\qquad a_j=2j+\tfrac12,\quad u>0.
\]
For any \(N\ge1\) set
\[
k_N(u)=\sum_{j=0}^{N-1}e^{-a_ju}
=\frac{e^{-u/2}(1-e^{-2Nu})}{1-e^{-2u}},
\quad k(u)-k_N(u)=\frac{e^{-(2N+1/2)u}}{1-e^{-2u}}>0.
\]
These are genuine positive **kernel** lower bounds, not a pointwise truncation of the signed prime multiplier. The remainder is retained as an **unevaluated nonnegative** form contribution. Monotone convergence applies for each admissible ground-transformed test. The singular \(u\to0\) logarithmic-form structure is recovered only by the complete infinite family; no finite \(N\) is asserted to recover that coercivity or the second spectral sign.

## 2. Exact EVEN reflection quotient: a stronger, original physical jump kernel

Let \(C_+=C\cap(0,B)\). PS15's sharp source/complement \(C\) is reflection invariant. The PS30 normalized real even ground eigenfunction \(\phi_0\ge0\), \(\|\phi_0\|_{L^2(C)}=1\), is strictly positive a.e. subject to its previously stated irreducibility audit. For a real admissible even \(g\), PS30's exact original digamma ground-state jump energy, **without modifying any original coupling**, becomes
\[
\boxed{\mathcal J_{\phi_0}[g]
=2\!\int_{\substack{x>y\\x,y\in C_+}}
K_\infty(x,y)\,\phi_0(x)\phi_0(y)
\bigl(g(x)-g(y)\bigr)^2\,dx\,dy,}
\]
where the **true reflection-symmetrized original physical kernel** is
\[
\boxed{
K_\infty(x,y)=k(|x-y|)+k(x+y)
=\sum_{j=0}^\infty
\left[e^{-a_j|x-y|}+e^{-a_j(x+y)}\right].}
\]
Each original positive-half interaction has a mirror contribution; **the reflection term \(k(x+y)\) cannot be discarded when quantifying a global even-sector spectral gap**. On the diagonal the infinite kernel is interpreted through its nonnegative jump form (the diagonal is measure zero), not as a bounded pointwise function. Define \(K_N\) by truncating this exact sum.

For \(0\le y\le x\le B\), every exponential layer satisfies
\[
e^{-a_j(x-y)}+e^{-a_j(x+y)}
=2e^{-a_jx}\cosh(a_jy)\ge 2e^{-a_jB}.
\]
Thus \(\boxed{K_N(x,y)\ge2k_N(B)}\) for every \(N\), and
\(\boxed{K_\infty(x,y)\ge2k(B)}\). This is an **original parity-sensitive stronger floor** than simply minimizing \(k(|x-y|)\) and \(k(x+y)\) independently.

For \(B=11/10\), elementary positive Taylor bounds certify
\[
e^{11/20}<\frac74,\quad e^{11/20}>\frac53,\quad e^{11/5}>8;
\]
hence, with NO floating rounding,
\[
\boxed{\frac47<k(B)<\frac{24}{35}.}
\]
The low-floor value is not close to the target: if one additionally **assumes**, without claiming to have proved, \(M_\infty=\|\phi_0\|_\infty<\infty\), the parity-symmetric constant-floor-only comparison yields
\[
\mathcal J_{\phi_0}[g]\ge \frac{k(B)}{M_\infty^2}
\operatorname{Var}_{\mu}(g),\quad
d\mu(x)=2\phi_0(x)^2dx\text{ on }C_+,\quad\mu(C_+)=1,
\]
while normalization gives \(M_\infty^2\ge1/|C|\); therefore this **particular guaranteed lower bound** is always strictly smaller than
\[
\boxed{\frac{k(B)}{M_\infty^2}\le k(B)|C|
<\frac{24}{35}\frac{11}{5}=\frac{264}{175}<1.51.}
\]
This improves the PS30 floor comparison but **still cannot reach** the necessary true gap \(|\lambda_0|>4.359740\). It is an obstruction ONLY to using this constant-floor proof, not evidence for a second negative eigenmode. With unproved or infinite \(M_\infty\), the displayed floor has no unconditional positive lower-bound value.

## 3. NEW FINITE original-ground weighted graph certificate, without assuming global L-infinity

Let \(\mu=2\phi_0^2dx\) on \(C_+\), and choose an arbitrary finite measurable partition \(C_+=\bigsqcup_{i=1}^q A_i\) with strictly positive masses \(\mu_i=\mu(A_i)\), \(\sum_i\mu_i=1\). Neither \(\mu_i\) nor \(\phi_0\) is currently evaluated. For each \(N\) define the **true original physical** density
\[
W_N(x,y)=\frac{K_N(x,y)}{2\phi_0(x)\phi_0(y)}
\qquad(x,y\in C_+).
\]
Assume **certified** real/rational symmetric nonnegative lower bounds
\(0\le w_{ij}\le\operatorname*{ess\,inf}_{A_i\times A_j}W_N\).
No such numerical physical bounds are claimed here; defining \(w_{ij}\) is an explicit next measurement obligation. The exact reflection identity and positivity of the full original seven prime/source jump terms imply
\[
\lambda_1-\lambda_0
\ge\inf_{\int g\,d\mu=0,\ \int g^2d\mu=1}
\frac12\iint W_N(x,y)(g(x)-g(y))^2\,d\mu(x)d\mu(y).
\]
For \(m_i=\mu_i^{-1}\int_{A_i}g\,d\mu\) and \(v_i=\mu_i^{-1}\int_{A_i}(g-m_i)^2d\mu\), the **exact cellwise variance identity** yields the rigorous lower
\[
\boxed{
\mathcal J_{\phi_0}[g]\ \ge\
\sum_{i<j}w_{ij}\mu_i\mu_j(m_i-m_j)^2
+\sum_i\mu_iv_i\,\ell_i,\quad
\ell_i:=\sum_jw_{ij}\mu_j.}
\]
No within-cell fluctuation is thrown away. Define matrices
\[
G_{ij}=-w_{ij}\mu_i\mu_j\ (i\ne j),\qquad
G_{ii}=\sum_{j\ne i}w_{ij}\mu_i\mu_j,\qquad
D=\operatorname{diag}(\mu_i)-\mu\mu^\top.
\]
**New finite acceptance gate**: if for a certified rational \(\rho>0\)
\[
\boxed{\ell_i\ge\rho\text{ for every }i,\qquad G-\rho D\succeq0,}
\]
then \(\boxed{\lambda_1-\lambda_0\ge\rho}\) for the true original physical even Schur, **provided** the inherited PS28–PS30 ground-transform assumptions and the actual \(\mu_i,w_{ij}\) enclosures are established. The matrix condition is an exact rational Loewner test (equivalently restrict to the \(q-1\) mean-zero directions). The untouched nonnegative prime and source terms can only improve the true gap. They are not claimed to be represented by absolutely continuous \(w_{ij}\) or already numerically measured.

This condition is a **finite, checkable, support-native spectral-gap lower** once the *actual* ground-state densities and original kernel weights are certified, unlike PS17's astronomical spectral-low matrix. The graph may remain too weak; failure of the sufficient inequalities is NOT failure of the original second-eigenvalue sign. More refined intra-cell singular-kernel estimates and direct seven-prime/source interactions may be needed.

## 4. IMPORTANT: a necessary 4.359740 gap is not by itself a sufficient target

PS30 inherited the actual PS27 auxiliary constant witness
\(\lambda_0<-4.359740\), hence \(|\lambda_0|>4.359740\). This is a **lower**, not an upper, bound on the size of the negative ground eigenvalue! Proving a gap of merely \(4.359740\) therefore does **not** establish \(\lambda_1\ge0\).

A conservative **valid upper envelope** follows using the original PS17 complete signed lower-order \(V_C>-13I\), removing the true positive even pole \(2|c_C\rangle\langle c_C|\), the original PS27
\[
A_0>\frac{1997}{9000}I,\qquad
\|B_0\|<\frac{1403}{80},\quad
\|c_C\|^2\le\|c\|^2<
\frac{11}{5}\biggl(\frac76\biggr)^2=\frac{539}{180}.
\]
Because \(J_C\ge0\) and the actual pole-free Schur subtracts \(B_0^*A_0^{-1}B_0\), the original even pole-free operator obeys
\[
\boxed{L>
-\biggl(13+\frac{539}{90}
+\frac{(1403/80)^2}{1997/9000}\biggr)I
>-1406 I.}
\]
Consequently
\[
\boxed{4.359740<|\lambda_0|<1406.}
\]
The upper is deliberately very coarse and is **not** a claimed \(\lambda_0\) numerical determination. The new \(\rho\)-criterion closes \(\lambda_1\ge0\) **only** with a simultaneous certified \(|\lambda_0|\le\rho\). A future \(\rho\ge1406\) would be sufficient from the coarse bound alone, but is not established, expected, or computationally practical here. A sharper genuine original \(\lambda_0\) lower bound is now a parallel acceptance obligation.

## 5. Exact Fraction checks and subsequent obligation

A focused validator exercises the finite even reflection kernel on a four-point mirror model, the exact exponential-geometric decomposition at the genuinely physical displacement \(u=2\log2\), rigorous rational Taylor enclosures for \(k(B)\), an uneven-mass two-/three-cell graph with *within-cell* variances, and the exact rational original \(-1406\) ground-envelope calculation. It replays inherited PS28 source arithmetic and PS30 source-mediated jump algebra; it does **not** manufacture the true original \(\phi_0\), actual physical cell masses, measured \(w_{ij}\), prime/source quantitative bounds or true \(\lambda_1\).

**PS32:** obtain *true original* rigorously bounded ground-state mass / local envelope data on one or more physical half-complement cells, evaluate finite-\(N\) kernel minima and optionally direct signed seven-prime/source jump gains, then test the graph PSD gate with independent original \(\lambda_0\) enclosures. If the graph gate is too weak, develop a short-range within-cell singular \(k(u)\sim1/(2u)\) coercivity inequality or a more effective spectral-index method. Do not claim that more exponential layers alone automatically close the sign.

**Custody:** W-PHYSICAL-SHIFT remains open. Canonical active obligation remains W-ODD-NEG. The PS30 and PS31 weighted-ground transforms, irreducibility, source positivity-cone and sharp form-core arguments need independent review. \(\lambda_1\ge0\), effective-pole nullspace and angle \(\Delta\), W-EVEN-FORM, W-ODD-NEG, full signed Weil, CC27 D-Riesz and RH remain OPEN.

Replay: \`python3 scripts/validate_rpb108_ps31_even_multiscale_gap.py\`.
