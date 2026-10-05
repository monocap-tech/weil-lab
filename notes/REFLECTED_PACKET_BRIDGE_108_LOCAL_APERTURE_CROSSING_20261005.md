# RPB108: the local crossing at a positive endpoint

Base: research a95b26157e6c2fe8f5d01d1dac8744c361ef8dca.

## Theorem

Suppose the actual native form Q_a is nonnegative and has a nonzero kernel of dimension r. There exists epsilon>0 such that, for every a<b<a+epsilon,
\[
n_-(Q_b)=r,\qquad \ker Q_b=\{0\}.
\tag{1}
\]
In the preceding exact inertia decomposition, the reduced remainder R0 is strictly coercive for these b. Its positivity in this local interval is derived, not imported as background positivity.

Thus the first enlargement creates exactly as many negative directions as the endpoint had null directions. No new null mode can occur arbitrarily close on the right. This is conditional on a positive endpoint; it does not assert that one exists.

## Terminology before use

**Pulled-back endpoint kernel:** K=ker A(a) on the fixed logarithmic Hilbert domain H=D_1, where A(t) represents Q_t after physical dilation U_t.

**Positive-complement gap:** gamma>0 satisfying A(a)|K^perp >= gamma I.

**Local crossing interval:** a right neighborhood on which the negative index is exactly dim K and the kernel is zero.

**Strictly expansive dimension:** the largest dimension of a linear subspace of the actual positive-analysis range on which ||N_b P_b^(-1)k||>||k|| for every nonzero k. This is a quadratic-form index; no choice of singular vectors is built into the term.

## Previously proved actual premises

The first-contact constructor proved that physical dilation
\[
(U_t f)(x)=t^{-1/2}f(x/t)
\]
identifies every D_t with H as a bounded isomorphism, with uniformly equivalent logarithmic norms on compact positive t intervals. The pulled-back actual mixed forms have bounded self-adjoint Riesz operators
\[
A(t)=I+K(t)
\]
with compact K(t), and t -> A(t) is continuous in operator norm. This includes finite prime activation thresholds: the compressed translation is zero at first support contact, so there is no jump.

The preceding exact inertia theorem proved that any nonzero positive endpoint kernel K_a couples injectively to the new-test complement at every b>a. Therefore n_-(Q_b)>=r for every such b.

These are actual form statements. Physical spectral-domain membership, raw synthesis, retained membership and full graph density are not additional premises of the argument below.

## Positive-complement gap

Since A(a) is nonnegative I+compact, K is finite-dimensional. Its restriction to K^perp has a strictly positive lower bound gamma.

For completeness, if no such bound existed, choose unit f_j in K^perp with <f_j,A(a)f_j> -> 0. Positivity gives
\[
\|A(a)f_j\|^2\le\|A(a)\|\langle f_j,A(a)f_j\rangle\longrightarrow0.
\]
Compactness of K(a) then supplies a strongly convergent subsequence of
f_j=A(a)f_j-K(a)f_j. Its unit limit lies both in K and K^perp, a contradiction.

Choose epsilon>0 such that
\[
\|A(b)-A(a)\|<\gamma/2
\quad(a<b<a+\epsilon).
\]
Consequently
\[
\langle f,A(b)f\rangle\ge(\gamma/2)\|f\|_H^2
\quad(f\in K^\perp).
\tag{2}
\]

## A dimension bound for every nonpositive subspace

Let L be any linear subspace on which the quadratic of A(b) is nonpositive. The orthogonal projection L -> K is injective: a vector in its kernel lies in K^perp, where (2) makes its quadratic strictly positive unless it is zero.

Hence
\[
\dim L\le r.
\tag{3}
\]
The actual endpoint coupling supplies an r-dimensional strictly negative subspace N_b after pullback to H. Equation (3) first proves that its dimension is maximal, so n_-(Q_b)=r.

Moreover N_b direct-sum ker A(b) is nonpositive: the kernel pairs to zero with every vector, and it meets N_b only at zero. Applying (3) to this sum gives
\[
r+\dim\ker A(b)\le r.
\]
Thus ker A(b)=0, and bounded dilation gives ker Q_b=0. This proves (1) without selecting eigenvalue branches or assuming a simple crossing.

## Actual positivity of the exact remainder

The exact inertia theorem gives
\[
n_-(Q_b)=r+n_-(R_0),\qquad
\dim\ker Q_b=\dim\ker R_0.
\]
Equation (1) therefore implies n_-(R0)=0 and ker R0=0. Since R0 is self-adjoint I+compact, it is nonnegative and has a strictly positive lower bound, by the same compactness argument used above.

This coercivity is for each fixed b in the local crossing interval. No uniform bound as b decreases to a is asserted. The full enlarged form remains indefinite: its r forced negative directions survive despite this derived remainder positivity.

## Consequences at the canonical aperture

If the canonical full-source positivity aperture A is finite, the previous aperture theorem gives Q_A>=0 and a nonzero finite-dimensional endpoint kernel. The local theorem then produces epsilon>0 for which every A<b<A+epsilon has exactly r negative directions and no weak-null vector.

Thus later indefinite-window kernels, if any, must lie outside this immediate right neighborhood. The general warning that later kernels may occur remains valid; this theorem resolves only their possible accumulation at the first positive endpoint.

Via the actual bounded isomorphism P_b onto its closed range, the same index is the strictly expansive dimension of T_b=N_b P_b^(-1). It equals r in this interval, and the full-source unit contraction fails there. This uses actual full analyses; a selected-background projection is a different form.

Dilation compares forms at different windows. It does not identify the analyses of U_a f with those of U_b f. Physical old endpoint vectors used in the coupling proof retain their unchanged full analyses when included in D_b. No square-completion coordinate is promoted to a retained source witness.

The independent global question is still whether the finite canonical endpoint is possible. Local crossing and local null exclusion do not exclude the endpoint itself, instantiate actual negativity, or supply the endpoint-to-Gaussian upper estimate.

## Validation and cursor

Analytic proof from actual norm continuity, compactness, strict-enlargement coupling and the exact inertia split. No new external input or Lean source/workflow change. The existing certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775. This theorem has not been newly formalized in Lean.

At a95b261, the norm-continuous actual fixed-carrier family A(t)=I+compact yields a local crossing theorem. Conditional on a nonnegative endpoint Q_a with nonzero kernel dimension r, the positive complement of the pulled-back endpoint kernel has gap gamma>0. Choose epsilon so ||A(b)-A(a)||<gamma/2 for a<b<a+epsilon. Every nonpositive subspace then projects injectively to the r-dimensional endpoint kernel, so its dimension is at most r. Strict-enlargement coupling already supplies r actual negative directions. Hence n_-(Q_b)=r and ker Q_b=0 throughout that right neighborhood; the exact inertia remainder R0 is strictly coercive there. At a finite canonical positivity aperture this gives a null-free immediate supercritical interval, not endpoint exclusion or a proof that the aperture is finite. Full-source gain has exactly r strictly expansive directions in the quadratic-index sense. Actual source vectors retain their own analyses; dilation is only a form comparison. No raw preimage, selected unit bound, background positivity, physical operator domain, RH conclusion or new Lean/CI result. FULL TRANSPORT CLOSED remains open.
