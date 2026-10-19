# SM57 — Original complete 25-source signed odd operator: entire negative-frequency upper

**October 19, 2026 · canonical W-ODD-NEG active · stacks on SM56 PR #239.**

## Why this is a new operator obligation

The verified SM51–SM56 calculations established genuine signed positivity and source-coercivity on a two-dimensional supported sine/\(x\cos\) trial space, and successively sharper whole-frequency **lower matrices** on the original three-dimensional sine/\(x\cos\)/sinh input span. SM56 Actions 39270413282 PASSED its original 3×3 full-mean-error comparison and raised the effective *lower-reference* pole Schur from approximately −0.058442558309 to −0.058397346916 by valid cellwise error selection. The complete 3D source lower remains non-positive-definite, and even a positive 3D trial result would not classify the **25 original supported odd physical directions**, the further original 470-source Astar inverse, or any infinite orthogonal remainder.

SM57 therefore starts the full **original 25-source complete negative-frequency operator bound** rather than adding still more frequencies near the same three input directions.

## Original 25 physically supported source carriers

Use the exact SI10/SM42/SI43 original source geometry \(g_0,\ldots,g_{24}\), with **16 actual zero-extended odd sine functions**, **8 actual zero-extended \(x\cos\) functions**, and \(g_{24}(x)=\mathbf1_{[-B,B]}(x)\sinh(x/2)\), \(B=11/10\). All physical Gram entries and the actual exceptional pole cross vector \(p_i=\langle g_i,g_{24}\rangle\) are recomputed from the original analytic **interval** identities. No orthogonality is assumed among these functions.

Define the original signed odd source form by the inherited physical Fourier/domain identity:
\[
W_o(h)=2\int_0^\infty m_{\rm orig}(\xi)|T_h(\xi)|^2\,d\xi
       -2|\langle h,g_{24}\rangle|^2,\quad
h=\sum_{i=0}^{24}z_i g_i .
\]

Use the exact original positive/negative decomposition
\[
m_{\rm orig}(\xi)=\max\{\kappa,m_{\rm orig}(\xi)\}
   -(\kappa-m_{\rm orig}(\xi))_+,\qquad \kappa=1/1000.
\]

## A genuine complete original signed-negative UPPER

The original SI06/SI07/SI10 all-seven-prime/digamma whole-real sign certificate identifies 973 exhaustive dyadic leaves, grouped into 107 clusters, supporting every possible negative multiplier value on the positive real frequency axis, entirely inside \([0,896]\). For every real \(\xi\) in original leaf \(I=[a,b]\),
\[
0\le(\kappa-m(\xi))_+\le h_I+\kappa .
\]
The zero-negative region outside those leaves (including \(\xi\ge896\)) is not approximated numerically; it is inherited from the original whole-real analytic certificate.

On each such leaf, SM43 independently certifies **all 25 actual original Fourier source amplitudes**
\[
|T_i(\xi)|\le s_{i,I}\quad \text{for every real }\xi\in I,
\]
using full physical sinc/sinc-derivative envelopes for original sine/\(x\cos\) carriers and the actual analytic sinh-pole Fourier envelope. Independently **round \(h_I+\kappa\) and each \(s_{i,I}\) UPWARD to the rational grid \(10^{-9}\)** before forming any products.

For every real 25-source coefficient vector \(z\), apply the *full coupled coefficient inequality*:
\[
\left|\sum_i z_i T_i(\xi)\right|^2
\le\left(\sum_i |z_i|s_{i,I}\right)^2
\le\left(\sum_j s_{j,I}\right)
  \sum_i s_{i,I}z_i^2 .
\]
Thus the full original signed-negative source operator—not just its 25 coordinate diagonals—satisfies the **complete 25×25 Loewner UPPER**
\[
\boxed{K_{\rm neg,25}\preceq D_{57},\qquad
 D_{57}=\operatorname{diag}_i\left(
 2\sum_{I\in\mathrm{SI10}_{973}}|I|
 \,\widehat{(h_I+\kappa)}\,
 \widehat s_{i,I}\sum_{j=0}^{24}\widehat s_{j,I}
 \right).}
\tag{SM57-N}
\]
This bound includes every mixed source direction \(z\), although its diagonal majorant is intentionally conservative. The output records every one of its 25 original negative-frequency upper entries, its 973-leaf and 107-cluster coverage, and the original whole-real outward weight and Fourier envelopes.

## Complete original 25×25 positive LOWER and actual pole UPPER

SM47/SM49 already proved a complete 25-source true original positive [0,4096] *one-sided* lower from the full physical Parseval Gram plus 17 original SM12 positive real windows and 32 original SM49 source-adaptive positive windows. Recompute these original certificates with all 625 entries and the entire coupled error:
\[
A_{\rm pos,25}\succeq
L_{\rm pos,25}:=
\kappa H_q+P_{17}+P_{32}
-\left[\kappa(\operatorname{TAIL}+\epsilon_H)
 +\epsilon_{17}+\epsilon_{32}\right]I_{25}.
\]
The omitted original positive high-frequency tail is nonnegative; neither a symmetric approximation nor the weaker source-2 directional error is substituted for the **full** matrix Loewner fee.

The original true exceptional pole vector \(p_i=\langle g_i,\sinh(x/2)\rangle\) is enclosed by the **entire 25×25 SM42 physical interval Gram**. For rational midpoints \(q_i\) and certified componentwise errors \(e_i\), the exact vector Cauchy inequality yields
\[
2pp^\top\preceq 2qq^\top+
 2\bigl(2\|q\|\|e\|+\|e\|^2\bigr)I_{25}.
\]
All terms are rational interval certified and the scalar fee rounded UP, including the pole *as an actual input source*.

Therefore the entire original 25-source signed odd form has a **true full-matrix lower**:
\[
\boxed{
W_o\big|_{\operatorname{span}\{g_0,\ldots,g_{24}\}}
\succeq L_{57}:=L_{\rm pos,25}-D_{57}-U_{\rm pole,25}.}
\tag{SM57-S}
\]
The resulting exact rational 25×25 matrix is symmetrically rounded to a compact \(10^{-12}\)-grid; a full *max-absolute-row-sum* outward fee is subtracted on the diagonal, so the exported compact matrix is itself a certified genuine **Loewner LOWER**, not a matrix of unconstrained midpoints.

## Explicit limits: no automatic operator-index classification

This is the **first full original 25-source signed-source lower built from a truly exhaustive negative-frequency upper**, not a theorem that \(L_{57}\) is PSD. The negative envelope is intentionally coarse and could obscure already certified SM52 two-source positivity. A negative entry or eigenvalue of \(L_{57}\) would be a weakness of this conservative lower, not proof that the actual \(W_o\) has a negative mode.

The validator **does not** claim full 25-source signed PSD, a negative-index value, the remaining original 470-source Astar inverse or its strong orthogonal residual, W-ODD-NEG O1/O2, even E1–E4, full Weil positivity, CC27 or RH. Those require the genuine full signed operator's negative upper and orthogonal-complement positivity as separate acceptance gates. The inherited SI06/SM42 physical Fourier/form-domain identities and support certificates still require independent mathematical audit: passing GitHub Actions checks the encoded exact rational consequences, not their external validity.

**Next mathematical priority:** replace the coarse 25-source Cauchy diagonal \(D_{57}\) by a genuine frequency-coupled physical Fourier matrix upper (or prove positivity of its orthogonal complement), rather than overinterpreting a negative \(L_{57}\).


## Recovery and exact 25-source inertia gate

The first focused SM57 Actions 39273770072 did **not** pass. It stopped at a leaf-width bookkeeping assertion. Original SI10's returned W=973/32 is **twice** the one-sided sum of 973 retained positive-frequency leaf widths, whereas SM57's width variable accumulates just that positive half. The correct invariant is 2 width=W, with width=973/64; the integral and original negative-frequency quadratic form already use the factor 2. This is a mistaken checker invariant, not a mathematical failure of the leaf amplitude inequality. The script and CI now require the correct two-sided accounting; a subsequent focused Actions pass is still required before this new 25-source result is accepted.

The same SM57 branch now adds **exact full symmetric rational inertia** of the compact outward source matrix L57, using fractional congruence elimination. Nonzero diagonal pivots update via the exact 1×1 Schur complement; if a remaining principal diagonal is identically zero, a nonzero off-diagonal gives an exact 2×2 indefinite symmetric pivot. The result classifies the inertia of the **reference LOWER** without relying on numerical float eigenvalues.

Because \(W_{\mathrm{odd},25}\succeq L_{57}\), the min–max principle proves the precise finite-trial-space ceiling
\[
n_-(W_{\mathrm{odd}}\big|_{\operatorname{span}\{g_0,\ldots,g_{24}\}})
\ \le\ n_-(L_{57}).
\]
If \(n_-(L_{57})=25\), this is trivially true and not a useful improvement. Negative pivots of L57 **never** demonstrate negative vectors of the actual signed operator, nor classify its index exactly. Most importantly this is **not** a negative-index ceiling for the complete infinite-dimensional odd operator or its 470-source/Astar/orthogonal complement.
