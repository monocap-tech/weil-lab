# PS30 — Original even pole-free Schur ground-state jump form and quantitative gap obligation

**W-PHYSICAL-SHIFT · October 18, 2026 · stacked on PS29 draft PR #196.** Scoped **analytic form-theoretic reduction**, not proof of the sign of the original second even eigenvalue. It retains the original PS15 sharp thirteen-source/support decomposition, PS27 source-first pole-free Woodbury and PS28 true positive source resolvent. **W-ODD-NEG, W-EVEN-FORM, original full Weil, native CC27 D-Riesz transfer, and RH remain OPEN.** Functional-analytic details require independent review.

## 1. Original object, and real order structure after eliminating the source

On \(I=[-11/10,11/10]\), \(P\) is the original thirteen-source reflection-invariant sharp carrier, and \(C=I\setminus P\). Let \(L=\mathfrak S_C^{(0)}|_{\mathrm{even}}\) be the **original pole-free even** complementary Schur form, with the original positive even pole removed **before** eliminating the source:
\[
L[h]=J_C[h]+c_{\rm arch}\|h\|^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\Re C_h(\ell_n)
-\langle h,Rh\rangle,
\quad
R=B_0^*A_0^{-1}B_0,\;
\ell_n=\log n,\;
w_n=\frac{\Lambda(n)}{\sqrt n}>0.
\]
This is **not** the full signed Weil form. The original odd rank-one pole vanishes on even vectors, and the positive even pole has been removed by design. \(J_C\) is the actual original zero-extended digamma difference form, \(k(t)=e^{-t/2}/(1-e^{-2t})\).

PS28 proves on the **even** source cone that \(A_0^{-1}\) is positivity preserving. On the nonnegative even complementary cone, the *actual* source/complement mixed operator \(B_0\) is negativity preserving, including every original negative arch/prime cross-coupling. Its adjoint has the same sign property. Hence the composite
\[
\boxed{R=B_0^*A_0^{-1}B_0\quad\text{is positivity preserving on the nonnegative even }L^2(C)\text{ cone}.}
\]
This is stronger than merely \(R\succeq0\) as a Hilbert-space operator: for **nonnegative even** \(u,v\), \(\langle u,Rv\rangle\ge0\). Both properties are used separately.

## 2. Strict positive ground-state carrier and an original signed ground transform

PS29 provides compact resolvent and a simple negative bottom eigenvalue \(\lambda_0<0\), with real nonnegative normalized even ground eigenfunction \(\phi_0\). Strictly positive original archimedean cross-kernel \(k(|x-y|)>0\) across any two positive-measure nontrivial even subsets ensures the form is *irreducible* on the even cone. By the standard irreducible positivity-preserving semigroup theorem, this upgrades the PS29 ground eigenfunction to
\[
\boxed{\phi_0>0\quad\text{a.e. on genuine }C.}
\]
The positivity-improving semigroup/domain step is an **analytic proof obligation for independent review**, not machine-certified in this PR.

Let \(g\) be real even and bounded Lipschitz (so \(\phi_0 g,\phi_0 g^2\) are in the original logarithmic form domain by the stable-multiplier rule); ultimately extend by form closure. Define \(h=\phi_0g\). Using \(L\phi_0=\lambda_0\phi_0\), the **exact original even pole-free ground-state identity** is
\[
\boxed{
L[\phi_0g]-\lambda_0\|\phi_0g\|_2^2
=\mathcal J_{\phi_0}[g]
+\mathcal P_{\phi_0}[g]
+\mathcal R_{\phi_0}[g].
}
\]
Here
\[
\mathcal J_{\phi_0}[g]=
\int_{\substack{x,y\in C\\x>y}}
k(x-y)\phi_0(x)\phi_0(y)|g(x)-g(y)|^2\,dx\,dy\ge0,
\]
\[
\mathcal P_{\phi_0}[g]=
\sum_{n}w_n
\int_{\substack{x\in C\\x-\ell_n\in C}}
\phi_0(x)\phi_0(x-\ell_n)
|g(x)-g(x-\ell_n)|^2\,dx\ge0,
\]
and the **entire genuine source-elimination interaction** contributes
\[
\boxed{
\mathcal R_{\phi_0}[g]
=\langle R\phi_0,\phi_0g^2\rangle
-\langle R(\phi_0g),\phi_0g\rangle\ge0.
}
\]
The last sign is not the operator-semidefinite property alone; it follows from the **positivity-preserving kernel/order property of R**: approximate any bounded even g by finite-valued even step functions on level sets, and expand
\[
\mathcal R_{\phi_0}[g]
=\sum_{i<j}(g_i-g_j)^2
\langle \phi_0 1_{A_i},R(\phi_0 1_{A_j})\rangle\ge0.
\]
Norm/positive-cone convergence extends to bounded g. All source archimedean and seven-prime nonlocal contributions remain contained in this **positive, source-mediated jump term**; they are not deleted or replaced by pointwise source kernel approximations.

The diagonal archimedean constant and zero-extension boundary killing vanish in the *ground-state difference* after the eigenfunction equation; the negative odd pole is identically zero on the even subspace.

**Interpretation:** the original source Schur correction \(-R\) is attractive in the untransformed form, but its order-preserving cross-coupling gives a **nonnegative** contribution to the jump energy **relative to the true pole-free ground state**. This does **not** say the original unshifted \(L\), much less the complete signed Weil form, is positive.

## 3. The previously open second-eigenvalue test becomes an exact weighted nonlocal Poincaré gate

Since \(\lambda_0\) is simple and the original \(L\) has compact resolvent, min–max and the strictly positive ground mode give the **exact** condition
\[
\boxed{
\lambda_1-\lambda_0
=\inf_{\substack{g:\ \int_C\phi_0^2g=0\\
                       \int_C\phi_0^2g^2=1}}
\left(\mathcal J_{\phi_0}[g]
+\mathcal P_{\phi_0}[g]
+\mathcal R_{\phi_0}[g]\right).
}
\]
The infimum is over transformed original form-admissible real even functions, not arbitrary inadmissible L² point data. Thus
\[
\boxed{
\lambda_1\ge0
\quad\Longleftrightarrow\quad
\inf_{\substack{\int \phi_0^2g=0\\\int\phi_0^2g^2=1}}
(\mathcal J_{\phi_0}+\mathcal P_{\phi_0}+\mathcal R_{\phi_0})\ge|\lambda_0|.
}
\]
This is a **new constructive spectral-gap representation of the PS29 one-negative-index obligation** retaining every original signed contribution. It does not certify the needed weighted Poincaré constant, \(\lambda_1\), the pole overlap \(a\), or the pole-angle margin \(\Delta\).

## 4. Rational scale comparison: why the uniform arch-kernel floor cannot close the gate

The original \(C\) lies in a physical interval of diameter \(R=11/5\). For \(0<u\le R\),
\[
k(u)>\exp(-R/2)=\exp(-11/10)>\frac3{10}.
\]
For the last strict bound, use elementary exact inequalities \(e<3\) and \(e^{1/10}<10/9\), so \(e^{11/10}<10/3\).

If, **as an additional unproved condition**, \(\phi_0\in L^\infty\) with finite \(M_\infty=\|\phi_0\|_\infty\), then for \(g\) of \(\phi_0^2\)-mean zero and \(\|\phi_0g\|=1\),
\[
\mathcal J_{\phi_0}[g]\ge \frac{3}{10M_\infty^2}
\int_{x>y}\phi_0(x)^2\phi_0(y)^2(g(x)-g(y))^2\,dx\,dy
=\frac{3}{10M_\infty^2}.
\]
Because \(\|\phi_0\|_2=1\), one always has \(M_\infty^2\ge1/|C|\), so **the numerical guaranteed lower bound obtainable from this specific constant-floor comparison alone is never greater than**
\[
\boxed{\frac{3}{10M_\infty^2}\le\frac{3}{10}|C|<\frac{33}{50}=0.66.}
\]
In contrast, the original PS27 RC315 constant-mode witness \(\mathfrak S_C^{(0)}[h_C]<-4.359740\) with \(\|h_C\|^2=|C|/R<1\) forces
\[
\boxed{\lambda_0<-4.359740,\qquad |\lambda_0|>4.359740.}
\]
Therefore **this particular constant-floor-only guaranteed spectral-gap comparison cannot certify \(\lambda_1\ge0\)**; its best possible certified lower from that route is below 0.66, while the true acceptance threshold exceeds 4.359740. This is **a method-specific obstruction, not evidence that the true \(\lambda_1<0\)**. Source, prime, and the short-distance singular growth of the full digamma kernel all remain available in the exact \(\mathcal J+\mathcal P+\mathcal R\) identity.

If \(M_\infty\) is unknown/infinite, even the \(3/(10M_\infty^2)\) statement is not an unconditional positive gap. No unsupported ground-state L∞ regularity has been inserted into the acceptance logic.

## 5. Next scoped acceptance

**PS31:** Build a **certified nonconstant short-scale/prime/source weighted Poincaré lower** for the actual \(\phi_0\), or bound a *genuine original* \(\lambda_1\) through a different source-pinned min–max route, retaining the full seven-prime and source-mediated interaction. Proving \(\lambda_1\ge0\) is necessary but still not sufficient for W-EVEN-FORM: one must additionally settle PS29's effective-vector nullspace and \(\Delta,\alpha\) coherent pole-angle gates.

**Custody:** PS30 gives a new analytic **exact original jump-form identity** and a rigorous rational *insufficiency of a specified crude bound*, with a finite exact-Fraction replay. It does not compute the true weighted Poincaré constant, \(\lambda_1\), or the source-renormalized pole-angle margin. No original odd or even signed Weil positivity; no RH. Proof of irreducibility/strict positive \(\phi_0\), form-multiplier density, and positivity of source-mediated jump form requires independent review.

Replay: \`python3 scripts/validate_rpb108_ps30_ground_state_gap.py\`.
