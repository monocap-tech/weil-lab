# NF — Cap-only preflight without constructing the inverse Galerkin response

**October 23, 2026. Active obligation:** W-ODD-NEG OPEN. **Standing:** exact algebraic reduction for the natural original SM35 source-space Galerkin family, independently auditable in rational toy matrices. Original 470-source stiffness and cap data are not yet computed. Neither a cap-only pass nor failure has been established for the original operator.

## A. Exact elimination of the first inverse

Let \(J:\mathbb R^{470}\to H_o\) be the *original* SM35 469 odd physical polynomial source generators plus the true sinh pole, with full-rank physical Gram \(H=J^*J\succ0\). Let \(A_\star=A_o-2|s\rangle\langle s|\succeq\kappa_\star I\) under SI29/SM19 assumptions. Let \(K_{\mathrm{cap}}\succeq K_-\ge0\) be **one specified complete original** SM10/SM37/etc. 890-column/107-block negative cap including \(\eta I\), with no improper mixing of cap versions. Define full original raw source matrices
\[
 A_J:=J^*A_\star J,\quad C_J:=J^*K_{\mathrm{cap}}J,\quad H:=J^*J.
\]
The supported full source strong domain is addressed in the separate [odd470 domain note](RPB108_ODD470_STRONG_DOMAIN_20261023.md), conditional on the genuine operator realization. We have \(A_J\succ0\) and \(H\succ0\).

**Choose the initial, natural Galerkin trial space \(V=\operatorname{ran}J\)**, with trial response \(Z=JQ\), \(Q=A_J^{-1}H\). Then
\[
 J^*(J-A_\star Z)=H-A_JQ=0,
 \qquad
 Z^*(J-A_\star Z)=0,
\]
so \(Z\) satisfies the true Galerkin orthogonality *without approximating* \(A_\star^{-1}J\). Its cap-only forms are
\[
 G_0=Z^*A_\star Z=Q^*A_JQ,\qquad
 N_{0,\mathrm{cap}}=Z^*K_{\mathrm{cap}}Z=Q^*C_JQ.
\]
Therefore,
\[
 \boxed{\Delta_0=\frac{51}{56}G_0-N_{0,\mathrm{cap}}
  =Q^*\left(\frac{51}{56}A_J-C_J\right)Q.}
\]
Since \(Q\) is invertible, **cap-only SPD for this exact original Galerkin trial is equivalent to**
\[
 \boxed{T_J:=\frac{51}{56}A_J-C_J\succ0.}
\]
This calculation completely eliminates the first explicit matrix inverse from the *cap-only sign test*, not from the later MG07 residual. It does not require the full \(470\times470\) inverse, Woodbury preconditioner or strong-action second moment to decide cap-only feasibility.

The normalized strict reserve obeys another exact congruence:
\[
 \Delta_0\succeq\delta G_0
 \quad\Longleftrightarrow\quad
 T_J\succeq\delta A_J.
\]
Equivalently \(C_J\preceq(51/56-\delta)A_J\). Its sharp reserve is
\(\delta_{\max}=51/56-\lambda_{\max}(C_J,A_J)\), provided the original matrices are correctly certified.

## B. A legitimate one-ray stopping certificate

A rigorous rational physical source vector \(v\in\mathbb Q^{470}\) with
\[
 \boxed{v^*\big((51/56)A_J-C_J\big)v\le0}
\]
rules out the positive cap-only margin for the exact fixed \(V=\operatorname{ran}J\), specified \(K_{\mathrm{cap}}\), and therefore the full MG07 sufficient gate using this identical Galerkin response, **even if its nonnegative residual charge could be reduced to zero**. This is a method-class stopping witness. It is **not** a negative direction for the actual signed operator \(A_\star-K_-\), since the upper cap can be conservative and \(51/56<1\); it also does not exclude enriched trial spaces \(V\supsetneq\operatorname{ran}J\) or a new tighter negative cap.

This suggests a strict economy of proof effort: inspect selected rational original physical source rays, especially the archived numerical cap-inflation suspects, and certify an all-frequency **upper** on \(v^*A_Jv\) and an exact physical cap **lower** on \(v^*C_Jv\). One rigorously negative ray suffices to reject the initial geometry. To establish the positive alternative, test all 470 coefficients through a rigorous Loewner lower or rational LDL decomposition with controlled matrix uncertainty. Positive results on selected rays do **not** suffice.

The signed original pole belongs in \(A_J\) exactly once, and the entire high-frequency logarithmic positive archimedean action belongs in its upper bound. \(C_J\) must evaluate the **same** actual physical source \(Jv\) against the full selected 890-column cap plus \(\eta\|Jv\|^2\), not a sampled Fourier substitute. No conditional finite toy or nonrigorous 25-source plot may be called an original witness.

## C. Acceptance and the remaining residual

A positive \(T_J\) is only cap-only eligibility. For the **same** \(Q\), form the actual \(Z=JQ\), strong residual \(R=J-A_\star Z\), and complete SI29-weighted \(D_B=R^*B_{14}^{-1}R\). MG07 still requires ONE uniform rational \(t>0\):
\[
 (1+t)N_{0,\mathrm{cap}}+
 (1+t^{-1})(H_-/\kappa_\star)D_B
 \preceq(51/56)G_0.
\]
In raw source coordinates this is congruent to
\[
 (1+t)C_J+(1+t^{-1})(H_-/\kappa_\star)
 Q^{-*}D_BQ^{-1}\preceq(51/56)A_J.
\]
The residual term is **not** discarded merely because cap-only feasibility simplifies. The entire analytic operator-realization transfer, even sector, CC27, global Weil bridge and RH remain open.

## D. Strong-residual elimination: a complete inverse-free raw-source MG07 gate

The same special Ritz space produces a stronger simplification than the cap-only test. Define the *physical* orthogonal projection \(P_J=JH^{-1}J^*\) onto the exact original \(470\)-dimensional source space and
\[
 E=(I-P_J)A_\star J
   =A_\star J-JH^{-1}A_J,\qquad J^*E=0.
\]
Because \(Q^{-1}=H^{-1}A_J\), the **actual complete strong residual** obeys
\[
 R=J-A_\star Z
  =J-A_\star JQ
  =-EQ.
\]
Write the full original strong-action moment \(S_J=(A_\star J)^*(A_\star J)\). Exact projection algebra yields
\[
 \boxed{E^*E=S_J-A_JH^{-1}A_J\succeq0.}
\]
This is the *Schur complement of the physical source Gram* in the combined source/action Gram. It is a covariance measuring failure of source-space invariance under \(A_\star\), **not** merely the qualitative positive definiteness of \(S_J\). An upper bound for it is useful; an isolated lower bound for \(S_J\) is not.

Let \(B_{14}\succ0\) be the unchanged original SI29/SM19 pole-conditioned lower reference and \(H_-=\|K_-\|_{\mathrm{certified}}\), with the original MG07 coefficient \(H_-/\kappa_\star\). Then
\[
 D_B=R^*B_{14}^{-1}R
   =Q^* E^*B_{14}^{-1}EQ.
\]
Thus **the complete fixed-\(V=\operatorname{ran}J\) MG07 sufficient matrix gate**, not just its cap-only part, is exactly equivalent by invertible congruence to
\[
 \boxed{
 (1+t)C_J+
 (1+t^{-1})\frac{H_-}{\kappa_\star}
 E^*B_{14}^{-1}E
 \preceq\frac{51}{56}A_J
 \quad\text{for ONE uniform }t>0.
 }
\]
There is no \(A_J^{-1}\) in this *raw-source inequality*. Its residual term depends on the **physical** inverse \(H^{-1}\), the complete original whole-frequency first and second action/source Grams, the 14 true SI29 feature overlaps, and the true pole. The actual operator \(A_\star\), not a compressed replacement, is retained in \(E\).

Because \(s\) is a column of \(J\), the source orthogonality also gives \(E^*s=0\). The **positive** pole-inverse correction in \(B_{14}^{-1}\) need not vanish, since generally \(E^*C_{14}^{-1}s\ne0\). This forbids incorrectly dropping the pole term from the Woodbury residual.

For a controlled first screen, keep the exact raw cap-only \(T_J=(51/56)A_J-C_J\). If it fails on one rigorous original physical source ray, do not compute \(E^*B_{14}^{-1}E\) for this fixed \(V\)/cap pair. If \(T_J\succ0\), evaluate the complete original \(E\)-covariance and SI29 feature/pole response and test the boxed inequality, preserving every coupled cross term.

**Proof custody:** the exact-rational regression now also uses a nontrivial 4-dimensional positive-operator model with a 3-source physical synthesis, nonzero orthogonal strong residual, positive reference \(B\preceq A\), and a nonzero cap. It independently checks \(J^*E=0\), \(R=-EQ\), the strong-action Schur covariance, and full MG07 Loewner congruence. This is an algebraic regression, NOT a computation of the actual 470-dimensional source/action matrices.

## E. Proof custody

[Exact-rational replay](../scripts/validate_rpb108_mg07_cap_only_source_congruence.py) verifies the algebra on a noncommuting rational SPD triple \(H,A_J,C_J\), a positive normalized reserve and an explicit negative-source-ray counterexample. The script also checks source-orthogonal strong-residual and full MG07 matrix congruence on a rational 4D/3-source model; it reuses the genuine SM35 source-count / cap geometry check but does **not** evaluate \(A_J\) or \(C_J\) for 470 true sources. Required next calculation: original raywise cap-versus-whole-action scalar certificates; advance to the complete Loewner test only if no method-specific obstruction is found.
