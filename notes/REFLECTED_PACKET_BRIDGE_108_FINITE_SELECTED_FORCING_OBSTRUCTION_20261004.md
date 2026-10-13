# RPB108: finite selected forcing cannot rescue enlarged weak-null transport

Base: research 25f59b6c700005e5278cc85e4833af4d62d1c44e.

## Actual finite-selection theorem

Let s be any finite set of actual divisor copies. Write P,N for normalized complete source analysis, R=Pi_s N for selected negative analysis and B=(I-Pi_s)N for background negative analysis. On the canonical supported logarithmic domain,
\[
Q_{{\rm bg},s}(g,h)=Q(g,h)+\langle Rg,Rh\rangle,
\]
where Q is the actual full native Weil form.

Two conclusions hold.

1. A selected-background weak-null vector h satisfies actual native weak-nullity on the same domain if and only if Rh=0. If Rh!=0, the same actual vector has strictly negative native energy and a nonzero finite exponential forcing.
2. For 0<a<b, no nonzero actual logarithmic h supported in [-a,a] can be weak-null for Q_bg,s against all of D_b. This holds for every finite selection, without assuming translation covariance of Q_bg,s.

The second statement extends the previous full-source obstruction. Finite selection is exactly the type implemented by neutralActualZetaSelectedProjection; no infinite-selection conclusion is imported.

## Exact mixed forcing

Orthogonality of the selected and background coefficient projections gives
\[
\langle Ng,Nh\rangle=\langle Rg,Rh\rangle+\langle Bg,Bh\rangle.
\]
Together with the full-domain source/native mixed identity, this proves the displayed selected form equality. If h is selected-background weak-null, then
\[
Q(g,h)=-\langle Rg,Rh\rangle
\quad(g\in D_c),
\tag{1}
\]
or, in bounded logarithmic Riesz operators,
\[
A_c h=-R_c^*R_c h.
\tag{2}
\]
No unbounded physical operator-domain premise is used.

If Rh=0, equation (1) is native weak-nullity. Conversely, native weak-nullity and (1), tested with g=h, give ||Rh||^2=0. Thus this condition is necessary and sufficient.

In particular
\[
Q(h,h)=-\|Rh\|^2.
\tag{3}
\]
A selected-null vector with nonzero removed energy is already a lawful native negative vector once its actual carrier/null identity has been attached. It could supply the preceding fresh full-source first-contact constructor. No historically unattached record is silently converted into such an input here.

## Physical finite exponential forcing

For each selected raw coordinate q with actual ordinate z_q, set
\[
n_q(h)=\tfrac12(F_h(\bar z_q)-F_h(z_q)),
\qquad
\eta_q(x)=\tfrac12(e^{-iz_qx}-e^{-i\bar z_qx}).
\]
These are the repository's normalized negative source conventions, with both sqrt(2) factors already applied. For a supported physical vector,
\[
n_q(g)=\int \overline{\eta_q(x)}\,g(x)\,dx.
\]
Define the entire exponential polynomial
\[
H_{s,h}(x)=\sum_{q\in s}n_q(h)\eta_q(x).
\]
On the window containing g,h,
\[
\langle Rg,Rh\rangle
 =\int\overline{g(x)}H_{s,h}(x)\,dx.
\]
Thus selected weak-nullity is the native weak forcing equation
\[
Q(g,h)=-\int\overline{g(x)}H_{s,h}(x)\,dx.
\tag{4}
\]
The physical forcing H is not itself the logarithmic Riesz vector R^*Rh. The latter is the physical inclusion adjoint applied to the window restriction of H. These carriers are kept distinct.

Copies at the same ordinate have identical n_q and eta_q and add as multiplicity weights. They do not create independent forcing directions. The forcing space is finite-dimensional even before quotienting these redundancies.

If Rh!=0, H cannot vanish identically on the physical window, since
\[
\int\overline{h(x)}H(x)\,dx=\|Rh\|^2>0.
\]
An entire exponential polynomial which vanishes on an open interval is identically zero. Therefore native compact-test cancellation on even one nonempty open subinterval of the selected-null window forces Rh=0: equation (4) and the compact-test fundamental lemma force H zero there, then everywhere. Nonzero selected forcing cannot be hidden entirely at the endpoints.

This statement is about the actual native mixed form. A typed frozen action still requires its exact dictionary and any stated symbol premise.

## Finite-dimensional forcing preimages

For every intermediate window c, the native operator is
\[
A_c=I+K_c
\]
with K_c compact, hence ker A_c is finite-dimensional, as proved previously.

For any finite-dimensional subspace V of D_c, the algebraic preimage
\[
M=A_c^{-1}(V)=\{f:A_cf\in V\}
\]
is finite-dimensional. Indeed A_c maps M into V, with kernel ker A_c. The quotient M/ker A_c injects into V, so
\[
\dim M\le\dim\ker A_c+\dim V.
\]
Equivalently choose preimages of a basis of A_c(M); together with a basis of ker A_c they span M. No surjectivity or physical spectral-domain claim is required.

## Strict-margin selected-nullity is impossible

Suppose h!=0 has support in [-a,a] and satisfies selected-background weak-nullity on D_b, b>a, for some finite s. By (4) it satisfies
\[
Q_b(g,h)=-\int\overline g\,H
\quad(g\in D_b)
\]
with H=H_s,h.

Choose a<c<b and epsilon>0 with a+epsilon<c and c+epsilon<b. For |u|<epsilon, tau_u h lies in D_c, and tau_-u g lies in D_b for every g in D_c.

The full native form is simultaneously translation invariant, as proved in the preceding record. Changing variables in the forced equation gives
\[
Q_c(g,\tau_u h)
 =Q_b(\tau_{-u}g,h)
 =-\int\overline{g(x)}H(x-u)\,dx.
\tag{5}
\]
No translation invariance of the selected-background form is asserted or used.

Every translate H(x-u) belongs to the fixed finite-dimensional span E of the exponentials e^{-iz_qx},e^{-i bar(z_q)x}, q in s. Let V_c be the span of the logarithmic Riesz representatives of their physical pairings on D_c. It has dimension at most 2|s|. Equation (5) shows
\[
A_c(\tau_u h)\in V_c
\quad(|u|<\epsilon).
\]
Hence all these translates lie in A_c^{-1}(V_c), a finite-dimensional space.

Distinct translates of nonzero compactly supported h are linearly independent by the Fourier/exponential-polynomial Vandermonde argument already proved. Arbitrarily many shifts in (-epsilon,epsilon) contradict the finite dimension of that preimage. This proves the theorem.

The empty selection gives V_c={0} and recovers the prior full-source result. At critical-line coordinates eta_q=0, so those selected copies contribute no forcing; the argument still holds.

## Endpoint factorization cannot persist with the same finite selection

Suppose h!=0 is selected-background weak-null on D_a for fixed finite s. Its selected-background diagonal is zero. On inclusion into D_b, the same physical vector and all actual source coordinates are unchanged, so
\[
Q_{{\rm bg},s,b}(h,h)=0.
\]
Let C_b be the bounded self-adjoint Riesz operator for this selected-background form on D_b. The theorem proves C_b h!=0.

If unit domination held on D_b, C_b would be positive. For a positive bounded operator, zero quadratic value implies C_bh=0, contradicting the theorem. Therefore fixed-selection unit domination cannot persist in any strict enlargement of that endpoint.

There is also an explicit negative vector. Put r=C_bh, s_0=||r||^2>0, d=|Q_bg,s,b(r,r)|, t=s_0/(s_0+d). Then
\[
Q_{{\rm bg},s,b}(h-tr,h-tr)
 \le-t\|r\|^2<0
\]
by the same Riesz mixed perturbation calculation as the full-source residual theorem. This disproves that enlarged fixed-selection contraction on a lawful actual vector.

If the selection changes between windows, the unchanged witness's new diagonal need not remain zero. The general strict-margin null obstruction still applies to any finite new selection, but the preceding explicit zero-diagonal perturbation statement requires that diagonal hypothesis.

## Research implication

The proposed same-vector enlarged weak-null transport is obstructed for both the full native form and every finite selected-background correction implemented in the current carrier. Finite selection cannot supply an exception merely because its form lacks translation covariance: its translated forcing still occupies a fixed finite-dimensional space.

A selected endpoint null equation alone also cannot yield native central cancellation. It either has nonzero selected energy, giving genuine native negative energy and analytic forcing, or has zero selected energy and reduces to the full endpoint-null case. Neither case supplies the required same-vector enlarged null equation.

Potential departures would require genuinely different input: a changed physical witness with new custody, an infinite forcing correction outside this finite-selection theorem, or a transport statement weaker than enlarged native/selected weak-nullity. None is constructed or asserted here, and a new representation wrapper cannot change this conclusion.

This is not an RH contradiction. No actual endpoint or false-RH zero is asserted. The fresh first-contact route remains a valid endpoint constructor from lawful native negativity; its proposed same-vector enlarged-null continuation is what fails.

## Validation and cursor

Analytic theorem derived from the actual finite selected projection, full-domain source/native identity, finite nullity and native translation covariance. No new external arithmetic input. No Lean source/workflow changes or new CI claim. Existing certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 25f59b6, finite selected-background weak-nullity gives the exact native forcing equation A_native h=-R*R h. Native central cancellation on the old domain holds iff Rh=0; if Rh!=0 then Q_native(h)=-||Rh||^2<0 and the finite exponential forcing cannot vanish on any open interval. More strongly, no nonzero supported actual logarithmic vector can be weak-null for any finite selected-background form on a strictly larger window. Translating the assumed forced equation gives infinitely many independent translates whose native residuals lie in one finite-dimensional exponential span; finite native nullity makes that preimage finite-dimensional, a contradiction. Therefore finite selected corrections do not rescue same-vector enlarged-null transport. Fixed-selection endpoint unit domination also cannot persist after enlargement when the unchanged vector has zero selected-background diagonal. This is an analytic theorem-level obstruction to both full and finite-selected persistence routes, not an RH contradiction. Infinite/non-finite forcing or a changed physical witness would require genuinely different input and new custody; neither is constructed. Lean unchanged; FULL TRANSPORT CLOSED and F4 entry remain open.
