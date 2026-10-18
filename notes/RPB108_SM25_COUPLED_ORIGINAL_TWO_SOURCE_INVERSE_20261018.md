# SM25 — True original odd two-source coupled inverse Loewner envelope (complete-operator acceptance retained)

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM24 draft PR #198.** This is an **actual original physically supported, coupled two-column partial spectral certificate**, not a positivity certificate for all 890 source columns, complete original odd signed operator, original even Schur, whole Weil, native CC27 D-Riesz or RH. The mandatory PS36 original whole-odd O1/O2 acceptance gates apply; they are **OPEN**.

## 1. Why the next action is a full coupled inverse instead of more forward-Ritz tweaks

Let \(A_*=A_o-2|s\rangle\langle s|\succ0\) be the true original SI29/SM01 odd **pole-absorbed** positive operator on the original physical odd Hilbert carrier, with all genuine signed-positive frequency response, original odd pole, and supported-domain couplings. Let \(U\) be the actual SM10 **890-column** physically supported odd sine-Taylor synthesis, \(C\) its exact 107-block SPD rational negative-cap moment matrix, with the true full all-frequency negative cap
\[
K_{\mathrm{neg},o}\preceq(1+\tau)UCU^*+\eta I,\quad
\tau=1/1024,\quad0<\eta<3.02\cdot10^{-10}.
\]
The canonical **complete original** sufficient acceptance remains
\[
\boxed{
S_{890}:=((1+\tau)C)^{-1}
-U^*(A_*-\eta I)^{-1}U\succeq0,
}
\]
together with its exact original physical/domain attachment, all 890 coupled entries and the full \(\eta\) infinite residual. SM24 proves \(H_Y+E^*A_*^{-1}E=U^*A_*^{-1}U\) exactly: changing a forward trial cannot alter the **complete** inverse Gram. SM25 therefore evaluates a nontrivial **two-column, complete-coupling submatrix** of a supported inverse envelope, instead of a further isolated residual decrease.

**Scope caution:** SM25 directly bounds \(U_2^*A_*^{-1}U_2\) for the two genuinely original degree-zero SM10 sources from the **first two distinct complete negative-cap clusters**, and not yet \(U_2^*(A_*-\eta I)^{-1}U_2\). Resolvent correction for the full 890 spectral gate requires an explicit separate estimate using the original \(\kappa_\star=33621/10^9>\eta\); one must not replace one by the other without paying the positive correction.

## 2. Exact original physical two-column data

Write \(c_0,c_1\) for the two first distinct cluster centers reconstructed from SM10's full original SI10 973-leaf/107-cluster signed seven-prime cover. They are **not chosen toy frequencies**. Define genuine original physical odd sources
\[
u_j(x)=\sin(2\pi c_j x),\quad x\in[-11/10,11/10],\quad j=0,1.
\]
Each is the \(k=0\) column in the actual 890-column SM10 \(U\). Construct the **complete signed physical** two-source Gram
\[
G_{ab}=\langle u_a,u_b\rangle
\]
with SI18's original exact physical sine integration and outward rational interval enclosures, including signed \(G_{01}\). Construct all \(14\times2\) signed overlaps with SI29's original full continuous physical positive reference functions \(g_i\),
\[
Q_{ia}=\langle g_i,u_a\rangle,
\]
and the **complete symmetric 14×14 signed** reference Gram \(H_{ij}=\langle g_i,g_j\rangle\). As in SM22–24, signed Simpson/Legendre bounds are outward enclosures of the *actual continuous* source integrals, not point-sampled replacements. With \(\Gamma=\operatorname{diag}(\gamma_i)\), \(\kappa=1/1000\), define
\[
C_{14}=\kappa I+G_{14}\Gamma G_{14}^*,\quad
K=\Gamma^{-1}+\kappa^{-1}H .
\]
The true SI29 pole-conditioned reference satisfies
\[
B_{14}=C_{14}-2|s\rangle\langle s|
\preceq A_*,
\qquad
0<1-2\langle s,C_{14}^{-1}s\rangle>1-L_{\rm pole}
\]
where \(L_{\rm pole}=966379/10^6<1\).

## 3. New coupled 2×2 matrix Loewner certificate

For a **rational 14×2 witness** \(Z\), the exact all-column variational identity gives
\[
Q^*K^{-1}Q\succeq
Q^*Z+Z^*Q-Z^*KZ=:M(Z).
\]
This includes **all 14×14 physical reference correlations and both actual source columns**; it is not two separate scalar estimates. Midpoint linear solves select a rational witness \(Z\), but **do not certify it**. Every true \(Q,K,G\) is enclosed by rational signed intervals from the actual physical sources. Outward interval arithmetic encloses all entries of \(M(Z)\). For a symmetric 2×2 interval matrix \(X\in[\underline X,\overline X]\), form its midpoint \(X_m\) and half-width error \(\epsilon_{ij}\) and use the rigorously Loewner-safe signed matrix
\[
X_-=X_m-\operatorname{diag}(\epsilon_{00}+\epsilon_{01},\,\epsilon_{11}+\epsilon_{01}),
\quad
X_+=X_m+\operatorname{diag}(\epsilon_{00}+\epsilon_{01},\,\epsilon_{11}+\epsilon_{01}).
\]
Because \(\epsilon_{ii}+\epsilon_{01}\) pays both the diagonal error and the *whole signed off-diagonal error*, \(X_-\preceq X\preceq X_+\). A diagonal-only interval replacement would be unsound.

Use \(M_-\preceq M(Z)\) and \(G\preceq G_+\). The **true original signed fourteen-source conditioned two-column inverse Gram** obeys
\[
\boxed{
0\preceq
X_2:=U_2^*A_*^{-1}U_2
\preceq U_2^*B_{14}^{-1}U_2
\preceq T_2:=
\frac1{1-L_{\rm pole}}\!
\left(\frac{G_+}{\kappa}-\frac{M_-}{\kappa^2}\right).
}
\]
Every displayed term in \(T_2\) is an explicitly constructed **exact rational 2×2 matrix** in the focused validator, not an unevaluated inverse symbol or the diagonal of two separate source tests. \(B_{14}\preceq A_*\) holds on the entire true odd physical carrier, so this is a valid *coupled principal block* upper for the true original inverse. Full odd \(\smash{S_{890}}\) acceptance is **not** inferred.

An additional valid **eta-shift transfer** avoids an unproved equality between the two inverses:
\[
\boxed{
U_2^*(A_*-\eta I)^{-1}U_2
\preceq\frac1{1-\eta/\kappa_*}\,T_2,\quad
\kappa_*=\frac{33621}{10^9},\quad\eta<\frac{302}{10^{12}}.
}
\]
Here \(\eta/\kappa_*<1\), since \(A_*\succeq\kappa_*I\). This is a true original **complete-negative-carrier two-column** bound with the inherited entire infinite residual paid in coefficient. For the two original degree-zero columns (different SM10 covariance blocks), define the actual original signed-negative cap block
\[
D_2=((1+\tau)C_2)^{-1},
\quad
C_2=\operatorname{diag}(C_{00},C_{11}),\qquad
C_{jj}=2\sum_{\ell\subset{\rm cluster}\;j}(\kappa+h_\ell)|\ell|.
\]
Then the concrete 2×2 sufficient spectral test is
\[
\boxed{D_2-\frac{T_2}{1-\eta/\kappa_*}\succeq0.}
\]
A **passing** result would be accepted only as a verified **principal necessary block of the 890-column full positive Schur** (positive 2×2 alone never proves 890×890 positive). A failed sufficient comparison only shows the present upper envelope is too weak; it does not establish an original odd negative eigenvalue.

## 4. Fail-closed conclusion and next work

The focused exact-Fraction regression reconstructs actual true two original SM10 centers, all 2×2 physical Gram entries, all 28 true signed source-to-SI29 overlaps, all 105 distinct true signed SI29 Gram entries, source inverse 14×2 rational variational witness, Loewner-safe 2×2 intervals, actual SI29 pole Woodbury coefficient, and the SM10 \(\eta\) infinite residual/2-block covariance. It independently tests a nontrivial signed finite two-source model in which separate positive diagonal minors coexist with a non-PSD full coupled matrix.

**Proof standing:** a new rigorous matrix **UPPER** on one actual original source two-plane, dependent on SI29/SM10/SM22 source-analytic premises. This is not the original \(\operatorname{ind}_-(W_o)=0\), not the whole signed odd PSD, and not the even pole-free spectral classification.

**SM26:** extend the actual original source-wise physical inverse Gram construction to a **complete, scalable original 890×890 coupled Loewner upper** or a block-controlled spectral decomposition with the **entire original low/high source and frequency residual**. Seek an executable global matrix acceptance, not 444 pairs of isolated certificates. Preserve PS36 O1/O2 acceptance gates, canonical W-ODD-NEG, and all RH closure flags OPEN.

Replay: \`python3 scripts/validate_rpb108_sm25_coupled_original_two_source_inverse.py\`.
