# RPB108: one finite actual selection reduces the local aperture family

Base: research 72f0b33d3d8c1316f0d24b0f499f9c6dca399a48.
Definitions: docs/TERMINOLOGY_RPB108_LOCAL_FINITE_SOURCE_MATRIX.md.

## Local theorem

Suppose c>0 is an actual nonnegative null window, with r=dim ker Q_c>0. Pull all nearby forms back by physical L2 dilation to H=D_1. There is one finite selection s of actual negative divisor coordinates, independent of nearby aperture t, and epsilon>0 such that
\[
G_s(t)=A(t)+R_s(t)^*R_s(t)\ge\beta I_H,\quad\beta>0,
\quad |t-c|<\epsilon.
\tag{1}
\]
Here A(t) is the actual full native form operator on the fixed H, and R_s(t) is selected actual negative analysis of the physical vector U_t h. Both maps are norm-continuous.

Define on the fixed selected coefficient space M=l2(s)
\[
S(t)=G_s(t)^{1/2},\qquad
C(t)=-G_s(t)^{-1/2}R_s(t)^*,\qquad
D_s(t)=I_M-C(t)^*C(t)
      =I_M-R_s(t)G_s(t)^{-1}R_s(t)^*.
\tag{2}
\]
These are norm-continuous. At every aperture in that neighborhood,
\[
A(t)=S(t)\bigl(I_H-C(t)C(t)^*\bigr)S(t),\qquad
R_s(t)^*=-S(t)C(t).
\tag{3}
\]
The exact finite matrix controls the full native sign and nullity:
\[
A(t)\ge0\iff D_s(t)\ge0,\quad
n_-(A(t))=n_-(D_s(t)),\quad
\dim\ker A(t)=\dim\ker D_s(t).
\tag{4}
\]
Thus local source selection and effective positive factorization persist even on the immediately indefinite side. Full compensator contraction does not: it holds precisely where the finite matrix is nonnegative.

The entries of D_s(t) still contain the infinite-carrier inverse G_s(t)^{-1}. No actual matrix values, numerical determinant, explicit selected ordinates, or new sign certificate are computed by this theorem.

## Fixed physical carrier and finite selected rows

Use the already proved dilation U_t h(x)=t^{-1/2}h(x/t). The actual pulled-back form is
\[
q_t(f,h)=Q_t(U_t f,U_t h)=\langle f,A(t)h\rangle_H.
\]
The canonical weights are uniformly equivalent on compact positive t intervals. The prior first-contact theorem proves A(t)=I+compact and operator-norm continuity, including prime thresholds. At a threshold the new translation compression has zero overlap; this is form continuity, not a differentiability assertion.

For a fixed actual divisor coordinate q, its normalized negative source row is
\[
n_q(U_t h)=\tfrac12\bigl(F_{U_t h}(\bar z_q)-F_{U_t h}(z_q)\bigr).
\]
After substituting x=t y, each row is sqrt(t) times an integral of h(y) against a fixed finite combination of exponentials depending smoothly on t, on y in [-1,1]. On a compact positive t interval these kernels and their t derivatives are uniformly bounded in L2(-1,1). The inclusion H->L2(-1,1) is bounded. Therefore each selected row is continuous in its H-dual norm, and a fixed finite collection R_s(t):H->M is operator-norm continuous.

No norm continuity of the entire infinite positive or negative sampling analysis is assumed. Finite selected rows suffice.

At c, the preceding effective-positive realization provides finite s with R_s(c) injective on K=ker A(c) and G_s(c)>=b I for some b>0. This statement remains valid in the pulled-back Hilbert norm because U_c is a bounded isomorphism of the canonical domains. Since
\[
\|R_s(t)^*R_s(t)-R_s(c)^*R_s(c)\|
\le(\|R_s(t)\|+\|R_s(c)\|)\|R_s(t)-R_s(c)\|,
\]
G_s(t) is norm-continuous. Shrink epsilon until ||G_s(t)-G_s(c)||<b/2; then (1) holds with beta=b/2.

The same actual selected indices are used throughout. This is a local result about a derived selection, not agreement with a prescribed historical packet or a selection valid at every aperture.

## Minimal selection and copies

The selected coordinate functionals of full N_0 restricted to K span K^*: if their span were proper, a nonzero k in K would annihilate every negative coordinate, contradicting ||N_0k||=||P_0k||>0. Since dim K=r, choose a basis of r such coordinate functionals. Consequently one may take |s|=r and R_s(c)|K an isomorphism.

Identical multiplicity-copy rows cannot both occur in this independent basis. Raw multiplicity energy is nevertheless retained in all complete analyses. An arbitrary set of r copies need not work, and this basis selection need not satisfy a historical packet's partner-orbit convention.

If selection is enlarged by finitely many actual coordinates, its covariance G_s(c) increases by a positive finite-rank covariance and retains the coercive lower bound. Thus a separately specified finite partner closure can be accommodated when lawful, although its larger matrix need not have dimension r. This is not an identification with an unseen retained packet.

## Square roots, actual WD-T10, and the change of coefficient coordinates

On positive operators bounded below by beta I and locally bounded above, the maps G->G^{-1}, G->G^{1/2}, and G->G^{-1/2} are operator-norm continuous. For the square-root functions this follows by uniform polynomial approximation on one compact spectral interval and continuity of polynomial evaluation; for the inverse it also follows from the resolvent identity. Thus (2) gives legitimate continuous bounded maps on fixed H and M.

At any nearby t, actual full analyses still obey
\[
G_s(t)=P_0(t)^*P_0(t)-B(t)^*B(t).
\]
Its positivity gives background domination ||B(t)h||<=||P_0(t)h|| even if A(t) is indefinite. The actual positive analysis is a bounded isomorphism onto its closed range H_+(t). Therefore
\[
\widetilde S(t)=P_0(t)^*
 \bigl[I-(B(t)P_0(t)^{-1})^*(B(t)P_0(t)^{-1})\bigr]^{1/2}
\]
is exactly the WD-T10 effective positive synthesis and satisfies
\[
\widetilde S(t)\widetilde S(t)^*=G_s(t).
\]
The same coercivity argument as in the previous pass makes this synthesis invertible. Put
\[
V(t)=S(t)^{-1}\widetilde S(t):H_+(t)\longrightarrow H.
\]
It is a bounded bijection and V(t)V(t)^*=I, hence unitary. The compensators obey
\[
\widetilde C(t)=-\widetilde S(t)^{-1}R_s(t)^*
              =V(t)^*C(t).
\]
Consequently their selected covariance is identical:
\[
\widetilde C(t)^*\widetilde C(t)=C(t)^*C(t).
\]
The fixed-H square-root factor therefore retains the actual WD-T10 selected matrix through an explicit unitary coefficient identification. No continuity of the varying H_+(t) or of V(t) is needed or claimed.

This unitary change concerns positive coefficient coordinates. The physical vector h and its actual physical realization U_t h are not renamed. The global physical vector changes with dilation as t varies; no same-vector enlarged null persistence follows.

## Exact finite inertia by two completions

For any C:M->H consider the Hermitian block form
\[
\mathcal B(x,u)=\|x\|^2+2\operatorname{Re}\langle x,Cu\rangle+\|u\|^2.
\]
Completing in the H slot gives
\[
\mathcal B(x,u)=\|x+Cu\|^2+\langle u,(I_M-C^*C)u\rangle.
\tag{5}
\]
Completing in the M slot gives
\[
\mathcal B(x,u)=\|u+C^*x\|^2+\langle x,(I_H-CC^*)x\rangle.
\tag{6}
\]
Both changes of variables are bounded invertible. Thus I_H-CC^* and I_M-C^*C have identical negative index and nullity, and one is nonnegative exactly when the other is. The extra identity blocks have neither negative index nor kernel.

Congruence (3) preserves the same properties because S(t) is invertible. Equations (5)-(6) prove (4) without importing an infinite-dimensional determinant or replacing the complete native negative analysis by selected energy alone. The background covariance has already been paid in G_s(t).

For u in ker D_s(t), the actual null-vector reconstruction is
\[
h=S(t)^{-1}C(t)u=-G_s(t)^{-1}R_s(t)^*u.
\tag{7}
\]
It satisfies R_s(t)h=-u, C(t)u=S(t)h, and A(t)h=0. Conversely h in ker A(t) maps to u=-R_s(t)h. These maps are inverse, so the selected unit-gain coefficients and actual physical null vector remain attached.

## Local crossing in the minimal matrix

The prior actual null-window index theorem gives, near the nonnegative null window c,
\[
n_-(A(t))=0,\ \ker A(t)=0\quad(t<c),\qquad
n_-(A(t))=r,\ \ker A(t)=0\quad(t>c).
\]
Take the minimal selection |s|=r. By (4),
\[
D_s(t)>0\ (t<c),\qquad D_s(c)=0,\qquad D_s(t)<0\ (t>c)
\tag{8}
\]
after possibly shrinking the neighborhood. The central equality follows because the r-dimensional matrix has nullity r. For a larger finite selection, precisely r eigenvalues vanish at c and cross to the negative side; the remaining directions stay positive locally.

Therefore det D_s(c)=0 and det D_s(t) is nonzero on either nearby side. In the minimal selection its sign is positive on the left and (-1)^r on the right. For even r, determinant sign alone would miss the negative-definite transition; full matrix inertia is the correct observable.

Equation (8) supplies no linear crossing slope. The actual family is proved norm-continuous, including moving prime compressions, and is not asserted analytic or differentiable at c. No first-jet or transversality floor is obtained.

## An attained finite-sector sequence with fresh custody

For any nonzero u_* in ker D_s(c), scale ||u_*||=1 and reconstruct
\[
h_*=-G_s(c)^{-1}R_s(c)^*u_*.
\]
Then R_s(c)h_*=-u_* and S(c)h_*=C(c)u_*; both endpoint coefficient norms equal one. Keep this h_* fixed on H and take t_n<c tending to c inside the neighborhood. Define the actual effective positive and selected negative coefficients
\[
d_n=\sqrt{\|S(t_n)h_*\|^2+\|R_s(t_n)h_*\|^2},\qquad
a_n=S(t_n)h_*/d_n,\quad
u_n=-R_s(t_n)h_*/d_n.
\]
The physical vector for this pair is U_{t_n}h_*/d_n. Since S(t_n) is invertible, d_n>0, and ||a_n||^2+||u_n||^2=1. Exact actual covariance custody gives
\[
\|a_n\|^2-\|u_n\|^2
=\frac{\langle h_*,A(t_n)h_*\rangle}{d_n^2}
\ge0,\qquad
\|a_n\|^2-\|u_n\|^2\longrightarrow0.
\]
Norm continuity gives strong limits a_*=C(c)u_*/sqrt(2) and u_lim=u_*/sqrt(2), each squared norm one half. Moreover
\[
a_n-C(t_n)u_n
=S(t_n)^{-1}A(t_n)h_*/d_n\longrightarrow0.
\]
The compensator relation is exact at the endpoint, not asserted before contact. This construction retains genuine actual analysis coefficients at every n; replacing a_n by C(t_n)u_n prematurely would generally lose that same-vector analysis custody.

The endpoint physical vector h_*/sqrt(2) satisfies the unit-gain and physical-adjoint equations. This is a fresh attained actual source sequence conditional on an actual null window. It is not a construction of the historical monotone coefficient-carrier family A(t) required by the full WD-T17/WD-T38 constructor, nor proof that the sequence belongs to that unseen family. No critical right-approach convention is substituted by the displayed left-approach sequence. These distinctions prevent an unwarranted claim that the entire Lean morphology has been instantiated.

## Remaining independent input and validation

This pass closes local constancy of a suitable finite selection, coercivity of the actual effective background covariance on both sides, norm-continuity of the fixed-coordinate compensator, and an exact finite native sign/nullity reduction with same-vector reconstruction.

It does not determine whether a finite nonnegative null window exists. The earlier first-contact constructor still requires a lawful actual negative vector; endpoint exclusion still requires independent actual information. Computing or bounding the finite matrix requires control of G_s(t)^{-1} and actual selected samples. A formal finite determinant is not that control.

Primary repository inputs, pinned at the base:
- ACTUAL_FIRST_CONTACT_CONSTRUCTOR_20261004: the fixed-domain dilation and norm-continuous actual family.
- NULL_WINDOW_INDEX_COUNT_20261005: exact isolated local index crossing.
- FINITE_SELECTION_EFFECTIVE_POSITIVE_REALIZATION_20261006: actual finite selection and WD-T10 synthesis.
- Previously attached actual normalized source/native mixed identity and positive closed-range carrier.

Analytic verification: dual-norm continuity of finite exponential rows, the explicit coercivity perturbation, bounded functional-calculus continuity, two block completions, the null reconstruction signs, and the coefficient normalization. No computed actual matrix or numerical sign certificate is claimed. No Lean/workflow changes or new CI run; historical notes unchanged. Numerical frontier 81/100. Historical retained packet/sequence identification, independent endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain open.
