# SM18 — certified original supported inverse through forward residuals

**Active obligation:** W-ODD-NEG OPEN. **Upstream:** SM17 conditional 890-source cap gate, pending merge. **Standing:** analytic and finite-dimensional exact-rational *verification architecture*, not a bound on the actual original 890-source matrix. No RH/whole-odd completion is asserted.

## A. Target with no formally unjustified inverse

As in SI29–SM17, let \(H_o=L^2([-11/10,11/10])_{\rm odd}\) and let
\[
 A_*=A_o-2|s\rangle\langle s|\succeq\kappa_* I,\quad
 \kappa_*=\frac{33621}{10^9},
\]
with the **original supported** positive frequency operator \(A_o\), not a pointwise Fourier reciprocal. SM10 constructs an actual 890-column odd physical Taylor synthesis \(U:\mathbb R^{890}\to H_o\), a real symmetric positive-definite rational moment matrix \(C\), and a rigorous original-frequency cap
\[
 K_{{\rm neg},o}\preceq (1+1/1024)UCU^*+\eta I,
 \qquad 0\le\eta<302/10^{12}.
\]
SM17 reduces a *sufficient* W-ODD-NEG condition to
\[
 U^*A_*^{-1}U\ \preceq\ \mu_0 C^{-1},\qquad \mu_0=999/1000.
\]
The equivalence follows by congruence of the positive definite rational \(C\); no matrix square-root arithmetic is required.

## B. Exact forward-action/residual identity

**SM18-A (analytic, proof).** For any bounded synthesis \(U:\mathbb R^n\to H\), any self-adjoint \(A\succeq k I>0\) on \(H\), and any finite synthesis \(Y:\mathbb R^n\to\operatorname{Dom}(A)\), define
\[
 E=U-AY,\qquad H_Y=U^*Y+Y^*U-Y^*AY.
\]
Then the exact finite-matrix identity holds:
\[
 \boxed{U^*A^{-1}U=H_Y+E^*A^{-1}E.}
\]
Indeed, writing \(X=A^{-1}U\), \(E=A(X-Y)\), gives
\(E^*A^{-1}E=(X-Y)^*A(X-Y)\); expanding and using \(AX=U\) proves the identity. Consequently
\[
 \boxed{U^*A^{-1}U\preceq H_Y+k^{-1}E^*E.}
\]
The right-hand matrix is constructed from the original **forward operator** \(A\), finite supported trial functions, and a complete physical residual Gram. It is an upper enclosure: unlike ordinary Ritz inverse estimates, it does not reverse the inequality direction.

**Corollary (SM18 sufficient gate for W-ODD-NEG).** If a checked original supported \(Y\), a rational symmetric upper enclosure \(\overline H\succeq H_Y\), and a rational positive-semidefinite residual upper \(\overline E\succeq E^*E\) satisfy
\[
 \boxed{\frac{999}{1000}C^{-1}-\overline H-
             \frac{10^9}{33621}\overline E\succeq0,}
\]
then \(U^*A_*^{-1}U\preceq(999/1000)C^{-1}\), and the previously certified SM10/SM17 error budget establishes \(Q_o\succeq0\) on the **entire original physically supported odd form domain**. All 890 columns and cross terms must be retained; the rational cap \(C\) is the actual SM10 block matrix. This is a **conditional theorem**; no such \(Y,\overline H,\overline E\) have been evaluated or certified for the actual original odd data.

The use of \(k^{-1}=10^9/33621\) is costly: rough residual bounds will be almost certainly inconclusive. It cannot be dropped, changed in sign, or replaced by unverified spectral estimates.

## C. Practical Ritz implementation and exact inequality accounting

A viable first candidate is \(Y=V(V^*A_*V)^{-1}V^*U\) for a finite family of physically supported trial functions \(V\) contained in \(\operatorname{Dom}(A_*)\). A rigorous implementation must enclose the positive definite finite Ritz matrix, invert it with directed rational bounds, and bound *both* the physical forward residual and its exact mixed Gram. The Galerkin residual \(V^*E=0\), giving \(H_Y=U^*Y\) (symmetric) when the exact Galerkin equations hold; this identity simplifies a validated implementation but gives only a **lower** inverse bound by itself, never the required upper.

For SM10's supported polynomial-modulated sine Taylor features and sufficiently smooth physical trial functions, logarithmic high-frequency multiplier growth makes \(AY\in H_o\). One possible original forward-action evaluation is the exact supported projection of \(\mathcal F^{-1}a\mathcal F(ZY)\) minus the true odd pole \(2s\langle s,Y\rangle\). All finite frequency cells, signed original seven-prime oscillations, archimedean tail, pole, and physical interval boundaries must receive rigorous enclosures. The frequency tail must cover \(a^2|\widehat{ZY}|^2\) for \(E^*E\), **not just** \(a|\widehat{ZY}|^2\) for the energy form. Original high-frequency \(a=O(\log(2+|\xi|))\) and supported \(O(1/|\xi|)\) source Fourier decay permit a finite but potentially expensive analytic tail budget.

The matrix can be certified without irrational Cholesky square roots: SM10's \(C\) has an exact rational LDL decomposition; invert this rational SPD matrix or compare via a congruent rational block matrix. A pure SPD threshold on approximate independent diagonal entries is forbidden. Require an **entire matrix** nonnegative rational LDL/Schur proof, with every off-diagonal retained; if a bound is inconclusive, report diagnostic only.

## D. Exact rational regression and fail-closed limits

The accompanying script checks SM17's precise \(\mu_0\) margin and a nontrivial rational \(2\times2\) prototype \(A=\begin{psmallmatrix}4&1\\1&3\end{psmallmatrix}\), \(U=I\), \(Y=\operatorname{diag}(1/4,1/3)\), \(k=2\), \(C=\operatorname{diag}(1,2)\). It checks:
1. \(A\succeq kI\), with rational principal-minor proof.
2. Exact matrix identity \(U^*A^{-1}U=H_Y+E^*A^{-1}E\).
3. Rigorous matrix \(H_Y+k^{-1}E^*E-U^*A^{-1}U\succeq0\), with all mixed terms.
4. Whole-matrix sufficient margin \((999/1000)C^{-1}-(H_Y+k^{-1}E^*E)\succ0\) on the prototype.
5. Deliberately inadequate trial/threshold example is **rejected**, rather than labeled PASS positivity.

**Scope:** this toy exact-arithmetic replay does **not** compute the actual 890-column \(Y\), \(H_Y\), or \(E^*E\), and does not establish the original infinite-dimensional residual inequality. These remain the research task.

## E. Next frontier / stopping condition

Construct a computationally tractable physically supported Ritz synthesis \(Y\) adapted to all 890 odd Taylor columns (the native RC high-Schur basis is one candidate). Obtain independently certified original forward-action upper matrices \(\overline H,\overline E\), including all real frequencies, source/physical boundary errors, and odd pole. Test the exact rational 890-column PSD gate above. If the conservative \(k^{-1}\overline E\) budget is terminal, derive a **proved complement coercivity enhancement** instead of hiding it behind increasingly fine unstructured scans.

W-ODD-NEG, even/whole Weil, global bridge, independent mathematical review, and RH remain OPEN.
