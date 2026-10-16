# RPB108 SI03 — exact native prime shift-graph Dirichlet factorization and signed-pole absorption

**Front:** Structural Investigation (SI), independent of the RC finite-Schur chain.  
**Parent:** integrated RC324 \`3022b035ef24658abefc1d192bf36db822b3329a\`.  
**Dependencies:** RC313 original CC27 signed prime/pole form; RC43 seven-prime support-chain bound; SI02 canonical D carrier and boundary-adapted Legendre difference geometry.  
**Standing:** a strictly positive **combined prime difference-energy plus signed-pole** subform on physical \(L^2\), after isolating a large negative scalar from the original prime form. This is NOT positivity of the full Weil form, nor a rank-317 Schur or RH claim.

## 1. Original source and exact positive-semidefinite factorization

Set \(I=[-B,B]\), \(B=11/10\), and let \(Z:L^2(I)\to L^2(\mathbb R)\) be zero extension, \(P=Z^*\) restriction. For \(\ell>0\), define
\[
T_\ell=P\tau_\ell Z,\qquad (T_\ell f)(x)=\widetilde f(x+\ell),\qquad
T_\ell^*=T_{-\ell},\qquad \|T_\ell\|\le1.
\]
With \(\Lambda(n)\) the von Mangoldt weight and \(c_n=\Lambda(n)/\sqrt n>0\), RC313's original, **signed** prime operator is
\[
K_{\rm prime}=-\sum_{n\in\mathcal A}c_n(T_{\log n}+T_{-\log n}),\qquad
\mathcal A=\{2,3,4,5,7,8,9\}.
\]
The coefficients for powers \(4,8,9\) use the base-prime logarithm, not \(\log n\).

For any \(f\in L^2(I)\), the unitary real-line translation identity is
\[
\|\widetilde f-\tau_\ell\widetilde f\|_2^2
=2\|f\|_2^2-\langle f,(T_\ell+T_{-\ell})f\rangle.
\]
Define \(C=\sum_{\mathcal A}c_n\) and the **native nonlocal Dirichlet form**
\[
\mathcal E_{\rm prime}(f)
=\sum_{n\in\mathcal A}c_n\|\widetilde f-\tau_{\log n}\widetilde f\|_{L^2(\mathbb R)}^2\ge0.
\]
Then the exact original-source identity, with no uncharged boundary effects, is
\[
\boxed{\langle f,K_{\rm prime}f\rangle
=\mathcal E_{\rm prime}(f)-2C\|f\|_2^2.}
\]
Equivalently, the Fourier multiplier of the positive term is
\(4\sum_n c_n\sin^2(\pi\xi\log n)\), applied to the transform of **zero-extended** \(f\).
Crucially \(\mathcal E_{\rm prime}\) is a *sum of actual squared norms*, preserving all interference and cross-covariance under an arbitrary low-source basis change. It is not a sum of individually bounded Legendre column errors.

## 2. Source support gives an exact positive gap (finite translation paths)

For \(0<\ell<2B\), the cut-down shift \(T_\ell\) acts, after splitting physical \(L^2(I)\) along residues modulo \(\ell\), as a direct integral of finite unilateral shift matrices. Each fiber is a consecutive path of length at most
\[
L_\ell=\lceil2B/\ell\rceil
\]
(in the essential, measure-theoretic sense; the exceptional interval endpoints have measure zero). On a length-\(L\) path, \(T_\ell+T_\ell^*\) is the tridiagonal path adjacency matrix, whose eigenvalues are
\[
2\cos(j\pi/(L+1)),\quad 1\le j\le L.
\]
The maximal length occurs on a positive-measure family of fibers. Consequently,
\[
\boxed{\|T_\ell+T_\ell^*\|=2\cos\frac{\pi}{L_\ell+1}},\qquad
\boxed{2I-T_\ell-T_\ell^*
\succeq 2\bigl(1-\cos\frac{\pi}{L_\ell+1}\bigr)I.}
\]
This is an operator inequality on **all** of \(L^2(I)\), not merely finitely many Legendre inputs. It is the support-chain mechanism underlying the RC43 norm estimate, now made explicit as a collective nonlocal Poincaré inequality.

Rigorous rational logarithm enclosures yield the following path lengths, with no near-endpoint ambiguity:
\[
L_{\log 2}=4,\quad L_{\log 3}=3,\quad
L_{\log n}=2\quad(n=4,5,7,8,9).
\]
Define \(\varphi=(1+\sqrt5)/2\) and
\[
M=\varphi c_2+\sqrt2\,c_3+c_4+c_5+c_7+c_8+c_9.
\]
This is a valid (not necessarily sharp joint) bound
\[
\|K_{\rm prime}\|\le M<4.10315,
\]
recovering RC43's \(4.103149\)-scale physical source bound from exact path geometry. More importantly,
\[
\boxed{\mathcal E_{\rm prime}(f)\ge
\gamma\|f\|_2^2,\quad
\gamma:=2C-M>2.97185.}
\]
This inequality applies to **all** even and odd physical sources, including every boundary-adapted polynomial combination. The separate shift operators do not commute, so \(M\) and \(\gamma\) are bounds, not claims of the exact spectrum of their sum.

## 3. The negative odd pole is absorbed by this positive difference energy

RC313 identifies the native signed cross-pole contribution as
\[
K_{\rm pole}=2|c\rangle\langle c|-2|s\rangle\langle s|,
\quad c(x)=\cosh(x/2),\quad s(x)=\sinh(x/2).
\]
The positive even term is retained, and the negative odd term has exact mass
\[
\|s\|_2^2=\int_{-B}^{B}\sinh^2(x/2)\,dx=\sinh B-B.
\]
Therefore Cauchy-Schwarz gives, for **every** (real or complex) \(f\in L^2(I)\),
\[
\boxed{
\mathcal E_{\rm prime}(f)+\langle f,K_{\rm pole}f\rangle
\ge
\bigl(\gamma-2(\sinh B-B)\bigr)\|f\|_2^2
+2|\langle c,f\rangle|^2.
}
\]
The exact rational bounds on prime weights, algebraic path eigenvalues, and the Taylor tail of \(\sinh B\) establish
\[
\boxed{\eta:=\gamma-2(\sinh B-B)>2.5005>0.}
\]
Thus **the complete nonlocal prime difference energy absorbs the negative odd-pole contribution collectively**, without a mode-by-mode diagonal audit or independent pole subtraction.

This is a strictly positive statement about an explicitly identified subform, **not the entire original Weil quadratic form**.

Indeed, the unavoidable scalar \(-2C\|f\|_2^2\) remains in the original prime form:
\[
\boxed{
Q_{\rm Weil}(f)=Q_{\rm arch}(f)
-2C\|f\|_2^2+
\bigl(\mathcal E_{\rm prime}(f)+Q_{\rm pole}(f)\bigr).
}
\]
The original archimedean term, including its logarithmic metric/contact normalization, is still required to overcome the scalar and prove complete positivity. We cannot discard it, and the bound \(+\eta\|f\|_2^2\) is **not** a positive lower bound proportional to \(\|f\|_D^2\) uniformly in degree.

## 4. Connection to SI02: all-degree adapted-basis Gram, no covariance loss

For any finitely supported boundary-adapted even or odd polynomial
\(q=\sum_k a_k(P_{d_k}-P_{d_k-2})\), let \(U_n=(I-\tau_{\log n})Z\) and let
\(G_n\) denote the resulting Gram matrix with
\[
(G_n)_{ij}
=\langle U_n F_{d_i},U_nF_{d_j}\rangle_{L^2(\mathbb R)}.
\]
Then \(G_n\succeq0\) and
\[
\mathcal E_{\rm prime}(q)
=\sum_n c_n\,a^*G_na.
\]
This is a **whole-family positive Gram factorization** with all signed overlap/cross terms retained. It is compatible with SI02's exact tridiagonal \(D\) metric; neither one requires separate upper bounds on each translation column.

For a polynomial of Legendre degree \(\le K\), write \(d_K=H_K+s\). Since
\(\|f\|_2^2\ge d_K^{-1}\|f\|_D^2\) on this finite-degree space, this subform has a positive finite-cap \(D\) lower bound \(\eta/d_K\). Because \(d_K\to\infty\), this **does not** give a degree-independent \(D\)-coercivity bound or Stage I closure.

## 5. What SI03 resolves and what remains

**Established analytically:** exact whole-operator prime Dirichlet factorization; all-degree physical gap via support-chain decomposition; absorption of the signed negative odd pole; preservation of all mixed source interference under arbitrary basis change. The path geometry is a structural explanation of an inherited RC43 norm bound, not a new stronger numerical prime estimate.

**Reproduced in exact arithmetic:** rational \(\operatorname{atanh}\) log enclosures establish \(\mathcal A\) path lengths; integer-square-root outward enclosures establish \(\varphi\), \(\sqrt2\) and \(c_n\); rational Taylor bounds establish \(\sinh B\). A standard-library validator confirms the displayed strict margins, plus exact characteristic polynomials of the length-2/3/4 paths. Its finite checks are *regressions of the all-degree proof*, not independent formal verification of the functional-analytic path decomposition.

**Not established:** the actual full Weil form's positivity, a uniform \(\mathcal H_D\)-coercivity inequality, nonpositive-direction exclusion, RC323/324 native inverse covariance, Stage I, F4, RH or Lean closure.

**Next SI04 direction:** retain \(\mathcal E_{\rm prime}\) as a collectively positive nonlocal component when comparing the archimedean logarithmic contribution against the exact scalar \(-2C\). Explore spectral/frequency localization of this positive Gram instead of paying the original prime operator only by its worst-case norm; independently examine the odd pole against the *full positive background* once established. Do not mistake the positive Dirichlet subform for an RH proof.

## Replay

\`\`\`bash
python scripts/validate_rpb108_si03_prime_graph_pole.py
\`\`\`
