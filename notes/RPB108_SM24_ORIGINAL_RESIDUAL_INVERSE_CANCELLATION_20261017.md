# SM24 — actual original odd first-source inverse-residual cancellation

**Canonical W-ODD-NEG remains OPEN.** Stacked after [SM23 PR #197](https://github.com/monocap-tech/weil-lab/pull/197) and true original first-source [SM22 PR #165](https://github.com/monocap-tech/weil-lab/pull/165). This checkpoint does not prove complete odd positivity or the 890-column negative-frequency Schur. The new mechanism uses the **actual original supported** \(A_*\), not a surrogate \(B_{14}\), on both sides of the residual.

## 1. Source-pinned original setup

Retain the original seven-prime positive multiplier carrier
\[
A_o=Z^*\mathcal F^{-1}\max(m,\kappa)\mathcal F Z,\quad
A_*=A_o-2|s\rangle\langle s|>0,\quad s=\sinh(x/2),
\]
on the odd physically supported \(L^2([-11/10,11/10])\). SI29 established the original pole-only bound \(B_{14}=C_{14}-2ss^*\preceq A_*\) and \(B_{14}>0\), where \(C_{14}=\kappa I+G\Gamma G^*\) retains all fourteen **true continuous** signed physical SI29 features, full Gram and correctly signed negative odd pole.

The original SM10 first source is \(u(x)=\sin(2\pi(37/64)x)\). SM21–SM22 give exact-rational quantities:
\[
0<n_- \le\|u\|^2\le n_+,\quad
q_-\le \langle u,A_*u\rangle,\quad
\|A_*u\|^2\le M,\quad
\lambda=q_-/M>0,
\quad E_0=u-\lambda A_*u.
\]
Here \(M=1360n_+ +785/1152\) pays all original negative and positive seven-prime frequencies and the unbounded exterior Fourier multiplier; the source energy \(q_-\) includes the actual negative odd pole with a rigorous upper on its subtraction.

SM22 supplies the **original first-source inverse upper**
\[
\langle u,A_*^{-1}u\rangle
\le\langle u,B_{14}^{-1}u\rangle
\le U_B,
\]
where \(U_B=U_C/(1-L)\), \(L=966379/10^6\), and
\[
U_C=\kappa^{-1}n_+-
\kappa^{-2}V_L,\qquad V_L\le q_G^*K^{-1}q_G,\quad
K=\Gamma^{-1}+\kappa^{-1}G^*G.
\]
\(V_L\) is SM22's exact rational **variational lower** based on all 14 original physical feature overlaps and every one of the 105 independent Gram enclosures. The midpoint only selects the rational witness; all acceptance uses signed outward intervals.

## 2. NEW exact original cancellation identity (no substitute inverse)

For any strictly positive self-adjoint \(A_*\) and \(u\in D(A_*)\), the actual forward Ritz residual \(E_0=u-\lambda A_*u\) obeys, with no omission of prime, archimedean or odd-pole interactions,
\[
\boxed{\langle E_0,A_*^{-1}E_0\rangle
=\langle u,A_*^{-1}u\rangle
-2\lambda\|u\|^2+
\lambda^2\langle u,A_*u\rangle.}
\]
The operator-domain hypothesis is satisfied for the actual smooth, sharply zero-extended SM10 source by SM20's full \(a^2\)-graph bound. The signed cross term is **exactly** \(-2\lambda\|u\|^2\), not a Young bound and not a vanishing approximation. This converts the already-certified original inverse \(U_B\) into a genuine **true** residual inverse upper.

For any rational \(r>0\), the **original** forward energy is bounded by Cauchy/Young:
\[
0<\langle u,A_*u\rangle
\le\|u\|\|A_*u\|
\le \frac{n_+}{2r}+\frac{rM}{2}
=:Q_+(r).
\]
Use the explicit rational trial \(r=1/37\); there is no quadrature or point-sampled multiplier substitution. Therefore
\[
\boxed{
0\le\langle E_0,A_*^{-1}E_0\rangle
\le U_B-2\lambda n_-+\lambda^2Q_+(1/37)=:R_{\mathrm{SM24}}.
}
\]
This is an **original physically supported first-source bound**, not the surrogate \(E_0^*B_{14}^{-1}E_0\) bounded in SM22 and SM23. It should improve SM22's Cauchy/Young surrogate upper when checked numerically, without claiming a new bound on the entire true inverse.

## 3. NEW all-column cancellation: what the residual strategy can and cannot buy

For any finite physical SM10 source family \(U:\mathbb R^N\to H_o\) with \(U_j\in D(A_*)\) and actual forward trials \(Y:\mathbb R^N\to D(A_*)\), set \(E=U-A_*Y\). Then
\[
\boxed{
E^*A_*^{-1}E
=U^*A_*^{-1}U-U^*Y-Y^*U+Y^*A_*Y.
}
\]
Writing the SM18 forward-energy Gram as
\(H_Y=U^*Y+Y^*U-Y^*A_*Y\), we get
\[
\boxed{H_Y+E^*A_*^{-1}E=U^*A_*^{-1}U.}
\]
With the *original* SI29 reference \(B_{14}\preceq A_*\), this yields a **rigorous all-column Loewner upper**
\[
\boxed{
H_Y+E^*A_*^{-1}E
=U^*A_*^{-1}U
\preceq U^*B_{14}^{-1}U.
}
\]
Thus spending a large computational budget on refining a forward trial \(Y\) **cannot by itself strengthen the exact completed inverse-energy quantity**, which is independent of \(Y\). It can still help with practical residual upper enclosures; SM23's \(E^*B_{14}^{-1}E\) is a different, generally larger object because \(B_{14}\preceq A_*\). This identity is a method-selection fact, NOT an impossibility claim for all possible 890-source proofs.

**New dependency decision:** If \(U^*B_{14}^{-1}U\) already fails the SM17 890-dimensional target, improving only \(Y\) and substituting the same \(B_{14}\) cannot repair that particular direct bound. One needs a stronger original positive reference, better physical source geometry, or a distinct certified coupled residual evaluation that beats the direct reference upper. This does not show the actual original Weil odd form is negative.

## 4. Audited scope

The focused script replays the full original SM22 first-source geometric/frequency and all 14 true SI29 continuous-source Gram enclosures, constructs \(U_B,\lambda,M,n_\pm\) exactly as Fraction values, certifies the new true residual upper, and independently compares it against both SM22's Young \(B_{14}^{-1}\) upper and the original scalar \(\kappa_*^{-1}D_{00}\). An exact Fraction 3-by-2 finite matrix replay checks the all-column cancellation and Loewner comparison; finite matrices do not constitute an independent audit of the physical Fourier/functional-analysis premises.

**Next mathematical step SM25:** build an actual **two-source true inverse** \(U_{0:2}^*B_{14}^{-1}U_{0:2}\) with *cross* physical Gram intervals, or strengthen the reference itself to cover the true 890-source matrix. Continue canonical W-ODD-NEG with all original negative frequencies, the negative odd pole and true physical domain. Native CC27 D-Riesz, whole original Weil positivity, W-EVEN-FORM and RH OPEN. No source-count extrapolation is permitted from a first-source improvement.

Replay: \`python3 scripts/validate_rpb108_sm24_original_residual_inverse_cancellation.py\`.
