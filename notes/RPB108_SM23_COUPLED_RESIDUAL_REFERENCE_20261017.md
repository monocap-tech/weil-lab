# SM23 — coupled original odd residual Woodbury matrix and feature-null floor

**W-ODD-NEG still OPEN.** Original SM22 true first-source SI29 fourteen-feature reference, physically supported seven-prime odd carrier, correct negative odd pole and full SM10 negative-frequency source family. Stacked after SM22 PR #165. **This checkpoint is an exact algebraic/evaluation architecture, not a completed original 890-source enclosure or an odd positivity certificate.**

## 1. The original true supported objects

On the real odd physical \(H=L^2([-11/10,11/10])_{\rm odd}\), retain the original signed seven-prime positive carrier \(A_o=Z^*\mathcal F^{-1}\max(m,\kappa)\mathcal F Z\), with \(\kappa=1/1000\), and \(A_*=A_o-2|s\rangle\langle s|\), \(s=\sinh(x/2)\).

Use exactly SI29's 14 *genuine continuous* positive source functions, not Simpson-point substitutes:
\[
G:\mathbb R^{14}\longrightarrow H,\quad
\Gamma=\operatorname{diag}(\gamma_j)>0,\quad
C_{14}=\kappa I+G\Gamma G^*\preceq A_o,\quad
B_{14}=C_{14}-2|s\rangle\langle s|\preceq A_*.
\]
The SI29 pole certificate is \(2\langle s,C_{14}^{-1}s\rangle\le L=966379/10^6<1\). Thus \(B_{14}\succ0\), \(A_*\succ0\), and \(0<A_*^{-1}\preceq B_{14}^{-1}\). These are inherited theorems, not rederived in this checkpoint.

Let \(E:\mathbb R^N\to H\) collect genuine original SM18–22 residuals \(E_j=u_j-A_*Y_j\) (ultimately \(N=890\), currently only SM22's first column has been evaluated). Define the exact original physical finite objects
\[
K=\Gamma^{-1}+\kappa^{-1}G^*G\succ0,\;
D=E^*E,\;V=G^*E,\;h=s^*E,\;c=G^*s,\;
\theta=1-2\langle s,C_{14}^{-1}s\rangle\ge1-L.
\]
\(D,V,h,c,K\) are original *continuous physical* couplings. No entries for the unknown remaining 889 columns are inferred.

## 2. Exact coupled signed residual inverse matrix

Woodbury and the correctly signed negative odd-pole Sherman–Morrison identity give
\[
C_{14}^{-1}=\kappa^{-1}I-\kappa^{-2}GK^{-1}G^*,\quad
B_{14}^{-1}=C_{14}^{-1}+\frac2\theta|C_{14}^{-1}s\rangle\langle C_{14}^{-1}s|.
\]
Therefore **for every** finite physically supported residual family \(E\),
\[
\boxed{
E^*B_{14}^{-1}E
=\kappa^{-1}D-\kappa^{-2}V^*K^{-1}V+
\frac2\theta\,p^*p,
\quad p=\kappa^{-1}h-\kappa^{-2}c^*K^{-1}V.
}
\]
The middle source term is **negative**, and the last true negative-pole inverse correction is **positive**. This is the correct coupled signed matrix, retaining all cross terms, unlike the coarser separated Young bound in SM22. It is **not** an estimate of the true 890-column matrix without evaluating \(D,V,h,K,c\).

## 3. NEW source-aligned exact-rational Loewner UPPER requiring no evaluated inverse

For an arbitrary *rational* \(14\times N\) trial \(Z\), define
\[
F=V-KZ,\qquad
M_Z=Z^*V+V^*Z-Z^*KZ,\qquad
p_Z=\kappa^{-1}h-\kappa^{-2}c^*Z.
\]
The exact completion-of-squares identity is
\[
V^*K^{-1}V=M_Z+F^*K^{-1}F\succeq M_Z.
\]
Because \(K\succeq\Gamma^{-1}\), we have \(K^{-1}\preceq\Gamma\), and for every \(\delta>0\), positive-rank-one Cauchy and matrix Young yield
\[
(p_Z-\kappa^{-2}c^*K^{-1}F)^*(p_Z-\kappa^{-2}c^*K^{-1}F)
\preceq(1+\delta)p_Z^*p_Z+
(1+\delta^{-1})\kappa^{-4}(c^*\Gamma c)\,F^*\Gamma F.
\]
Hence a **genuine source-grounded matrix UPPER** (provided the actual continuous data receive outward-rational enclosures) is
\[
\boxed{
E^*A_*^{-1}E\preceq E^*B_{14}^{-1}E
\preceq\mathcal U_\delta(Z)
}
\]
where
\[
\boxed{\mathcal U_\delta(Z)=
\kappa^{-1}D-\kappa^{-2}M_Z+
\frac{2}{1-L}\left[
(1+\delta)p_Z^*p_Z+
(1+\delta^{-1})\kappa^{-4}(c^*\Gamma c)F^*\Gamma F\right].}
\]
This is a *Loewner matrix* inequality for any N, not an assertion about the unknown original matrix's eigenvalues. It becomes directly usable with the existing SM18–19 sufficient test \(H_Y+\mathcal U_\delta(Z)\preceq (999/1000)C^{-1}\) after **every original residual, full signed cross-Gram and native source evaluation has been certified**. No such 890-column check is claimed.

The rational choice \(Z\) is a trial witness, NOT an unverified numerical inverse. The negative source correction \(-\kappa^{-2}M_Z\) is retained with its sign. With exact \(Z=K^{-1}V\), \(F=0\), the bound is tight up to the inherited pole margin and matrix Young factor, and the *exact identity* has no Young loss.

## 4. NEW finite-rank ceiling / feature-null lower bound on this preconditioner

Let \(\mathcal W=\operatorname{span}(\operatorname{ran}G,s)\) in the actual physical odd \(H\), with dimension at most 15, and \(\Pi_{\mathcal W^\perp}\) its orthogonal projection. On \(\mathcal W^\perp\),
\[
B_{14}=\kappa I,\qquad B_{14}^{-1}=\kappa^{-1}I.
\]
This is a reducing decomposition (all finite-rank updates are supported in \(\mathcal W\)). Therefore
\[
\boxed{
E^*B_{14}^{-1}E\succeq
\kappa^{-1}E^*\Pi_{\mathcal W^\perp}E.
}
\]
Consequently **no improvement of the fourteen-feature B14 preconditioner can remove its scalar floor on residual components orthogonal to the fourteen sources and odd pole.** This lower bound is on the chosen *upper-bound preconditioner*, not on the true \(A_*^{-1}\) and not on the signed Weil quadratic. It does not establish any RH obstruction.

There are up to 890 negative cap columns but only 15 preconditioning feature directions, so measuring the residual feature-null Gram is an essential future diagnostic, more informative than shrinking an isolated first-source norm.

## 5. Acceptance and next frontier

**Achieved, analytic/exact algebra:** correct full N-column original-variable Woodbury formula, constructive signed rational matrix upper \(\mathcal U_\delta(Z)\), and feature-null floor. The scoped exact-Fraction finite-dimensional regression exercises the true negative pole sign, a nonzero trial error, the exact Gram identity, and the Loewner bound, but does **not** compute original 890 original source columns.

**OPEN:** The actual physical \(V=G^*E\), \(h=s^*E\), full \(D=E^*E\) and all signed cross terms for the SM10 890-column family; actual matrix envelope and Schur PSD; original negative-frequency entire tail; odd W-ODD-NEG; W-EVEN-FORM; CC27 D-Riesz bridge; whole Weil positivity; RH. SI29/source assertions also still require independent mathematical audit.

**SM24:** compute the *actual SM22 first source* \(V_0=G^*E_0\), \(h_0=s^*E_0\), \(D_{00}\) with original \(\max(m,\kappa)\) and correctly signed odd pole, then certify a rational \(Z_0\) and \(\mathcal U_\delta(Z_0)\); subsequently prioritize cross-column residual feature-null and full signed Gram. Do not prematurely claim that a mere 15-feature reference controls the 890 negative source directions.

Replay: \`python3 scripts/validate_rpb108_sm23_coupled_residual_reference.py\`. The full SI29/SM22 original chain is replayed by the inherited SM22 action; the SM23 script checks the new finite algebra and fail-closed governance.
