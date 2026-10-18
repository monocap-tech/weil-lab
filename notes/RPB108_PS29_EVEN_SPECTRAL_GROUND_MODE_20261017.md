# PS29 — Original pole-free even Schur ground mode and exact spectral pole-angle gate

**W-PHYSICAL-SHIFT · October 17, 2026 · stacked on PS28 draft PR #195.** This is an **analytic spectral reduction**, not a proof of the sign of the original even Schur. The true original seven-prime, zero-extended, digamma, source-eliminated, **positive-even-pole-free** quadratic remains the object. Original signed W-ODD-NEG, W-EVEN-FORM, native CC27 D-Riesz, complete Weil positivity and RH remain OPEN. All infinite-dimensional arguments need independent mathematical audit.

## 1. Original setting and what PS28 actually supplied

On the genuine PS15 even source complement C, let
\[
L=\mathfrak S_C^{(0)}|_{\mathrm{even}},\quad
\mathfrak S_C=\mathfrak S_C^{(0)}+\alpha|\langle d,h\rangle|^2,\quad
d=c_C-B_0^*A_0^{-1}c_P\ge c_C\ge1,\quad
\frac{3994}{2907}<\alpha<\frac{240000}{120169}.
\]
Here the **original** source \(A_0>1997/9000\) and \(B_0\) retain every original negative seven-prime translation and digamma coupling (positive even pole removed *before* the source Schur). PS27's normalized restricted constant test gives
\(\mathfrak S_C^{(0)}[h_C]<-4.359740\); thus the even \(L\) has at least one negative direction. The auxiliary negativity is not original Weil negativity.

## 2. NEW analytic spectral property: a unique strictly negative bottom eigenvalue with a fixed-sign eigenfunction

The actual original zero-extension digamma form
\[
J[f]=\int_0^\infty k(u)\|Zf-\tau_uZf\|_2^2\,du,\quad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}>0
\]
has Fourier multiplier \(m(\xi)=2\int_0^\infty k(u)(1-\cos(\xi u))\,du\), growing logarithmically as \(|\xi|\to\infty\) (lower bound \(m(\xi)\ge c\log(2+|\xi|)-C\) for suitable constants). On the bounded physical interval, the original closed logarithmic form embeds compactly in L², including its sharp PS15 source-complement restriction. Since the original even \(Q_0|_C\) differs from \(J_C\) by bounded c_arch mass and seven actual signed prime translations, and \(B_0^*A_0^{-1}B_0\) is bounded on L² by PS15/PS27, **L is self-adjoint, bounded below, and has compact resolvent** on the even L²(C) carrier.

For any real even \(f\) in the full pole-free original form domain, \(|f|\) remains even and admissible. Original digamma and all **negative** prime translation coefficients give \(Q_0[|f|]\le Q_0[f]\). More strongly, if \(f\) changes sign on positive-measure sets, then
\[
J[f]-J[|f|]
=4\int_0^\infty k(u)\int f_+(x)f_-(x-u)+f_-(x)f_+(x-u)\,dx\,du>0.
\]
The strict inequality uses the actual positive original \(k\) between any two subsets of positive measure, not a local surrogate. In the even sector the original negative odd rank-one pole is exactly zero, and the positive even pole was removed, so the other contributions cannot undo this strict modulus improvement.

For any real even \(h\in\mathcal D_C\), let \(p_h=-A_0^{-1}B_0h\) be its unique original pole-free **source minimizer** and \(f=p_h+h\). Disjoint source and complement supports imply \(|f|=|p_h|+|h|\), hence
\[
L[|h|]\le Q_0[|f|]\le Q_0[f]=L[h],
\]
with **strict** inequality if h changes sign on positive-measure subsets of C.

The compact-resolvent min–max principle yields a bottom eigenfunction \(\phi_0\), real, L²-normalized and nonnegative; the negative constant-mode witness forces its eigenvalue \(\lambda_0<0\). A sign-changing bottom eigenfunction would contradict the strict modulus inequality. If the bottom eigenspace had dimension >1, real orthogonal ground eigenfunctions could be combined to give a sign-changing ground eigenfunction, also impossible. Therefore
\[
\boxed{\lambda_0<0\text{ is simple},\qquad \phi_0\ge0,\quad \|\phi_0\|_2=1.}
\]
As \(d\ge1\) a.e., the actual source-renormalized pole has **strict coupling to this lowest negative eigenmode**:
\[
\boxed{a=\langle d,\phi_0\rangle\ge\int_C\phi_0>0.}
\]
This establishes neither that \(\lambda_0\) is the **only** negative eigenvalue, nor that its pole compensation is sufficient.

## 3. NEW exact spectral criterion: reduce the two even variational gates to a pole-angle margin

Denote the subsequent even eigenvalues by \(\lambda_1\le\lambda_2\le\cdots\). If \(\lambda_1<0\), the original even update \(L+\alpha|d\rangle\langle d|\) is **indefinite for every** \(\alpha\): a rank-one correction cannot eliminate two negative directions. This remains an untested potential failure branch.

Suppose instead \(\lambda_1\ge0\). Let \(N=\ker L\), possibly \(\{0\}\). An additional **necessary** condition for the rank-one update to be nonnegative is \(d\perp N\): if some \(z\in N\) has nonzero pole pairing, a linear combination of z and the negative \(\phi_0\) can cancel the pole while retaining negative L energy.

Assuming \(d\perp N\), write the *L²* decomposition (not a form-domain assumption on d)
\[
d=a\phi_0+b,\quad b\in H_+:=(\operatorname{span}\{\phi_0\}\oplus N)^\perp,\qquad L_+=L|_{H_+}>0.
\]
Compact resolvent ensures a **strict** positive spectral gap on \(H_+\), hence \(L_+^{-1}\) is bounded; define
\[
\beta=\langle b,L_+^{-1}b\rangle\ge0,\qquad
\Delta=a^2-|\lambda_0|\beta.
\]
An exact positive-block Schur calculation, valid at form level, gives
\[
\boxed{L+\alpha|d\rangle\langle d|\succeq0
\iff \Delta>0\ \text{and}\ \alpha\Delta\ge|\lambda_0|},
\]
**provided** \(\lambda_1\ge0\) and \(d\perp N\). Equivalently the full test, with no assumption on \(d\)'s log-form regularity, is:
\[
\boxed{
\lambda_1\ge0,\quad d\perp\ker L,\quad
\Delta>0,\quad \alpha\Delta\ge|\lambda_0|.
}
\]
This does NOT certify any of these outstanding inequalities for the true original \(L\); it says precisely which spectral facts would do so.

The two original PS28 form gates acquire a more informative division:
* **Effective-pole orthogonal** \(K_{\rm eff}\) PSD is equivalent, when \(\lambda_1\ge0\) and \(d\perp N\), to \(\Delta\ge0\).
* **One coherent scalar** requires the strict margin \(\Delta>0\) and \(\alpha\ge|\lambda_0|/\Delta\).
If \(\Delta=0\), K_eff may be semidefinite but **no finite positive pole coefficient closes the scalar gate**. Strict overlap \(a>0\) alone cannot replace the \(\Delta\) test.

## 4. Concrete acceptance corridor from the ORIGINAL PS28 coefficient bounds

No evaluation of the original \(A_0^{-1}c_P\) or of the original L eigenpairs has been made. Nevertheless, \(\alpha\)'s certified two-sided rational interval supplies an exact **threshold corridor**. With the first three spectral prerequisites above in force define \(m=\Delta/|\lambda_0|\).

* **Sufficient**: \(m\ge2907/3994\) implies \(\alpha m>1\) by PS28's lower \(\alpha>3994/2907\), hence original even Schur is nonnegative (strict on \(N^\perp\)).
* **Impossible**: \(m\le120169/240000\) implies \(\alpha m<1\) by PS28's upper \(\alpha<240000/120169\), hence original even Schur remains indefinite.
* Between these two rational endpoints the existing source coefficient bounds alone cannot determine the sign.

This **does not** provide a lower bound on \(m\), \(\lambda_1\), \(a\), or \(\beta\). It supplies a rigorously typed target for the next original-operator computation: first decide the second spectral sign, then quantify the effective-pole angle to the positive spectral sector. Exact rational finite-dimensional replays validate algebra and the corridor, **not** the uncomputed original spectral parameters.

## 5. PS30 / outstanding obligations

1. Prove or disprove \(\lambda_1\ge0\) for the original even pole-free source Schur (the one-negative-mode index gate).
2. If nullspace is present, prove \(d\perp\ker L\); otherwise rule it out. Certify \(m=\Delta/|\lambda_0|\), ideally against \(2907/3994\), with all seven prime shifts and true source inverse.
3. Independently attack the original odd Schur \(W\)-ODD-NEG, including the negative signed odd pole; audit the source cone argument, compactness and strict modulus step, and the CC27 D-Riesz transfer.

**Custody:** PS29 is a structural spectral theorem conditional on existing PS15/PS27/PS28 analytic premises. It is not a numerical eigenvalue certificate, an even/odd positivity closure, a source inverse evaluation, or RH. The original canonical active obligation stays W-ODD-NEG. Replay: \`python3 scripts/validate_rpb108_ps29_even_spectral_ground_mode.py\`.
