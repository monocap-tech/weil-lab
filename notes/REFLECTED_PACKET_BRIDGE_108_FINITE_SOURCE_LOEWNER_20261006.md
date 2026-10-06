# RPB108: strict Loewner monotonicity of the actual finite source matrix

Base: research 4853bbf788711bf4e5f450a35d775ad1df73cbe6.
Definitions: docs/TERMINOLOGY_RPB108_FINITE_SOURCE_LOEWNER.md.

## Result

Fix one finite selection s of actual negative divisor coordinates. On each physical canonical domain D_t write
\[
\mathfrak g_t(f,h)=Q_t(f,h)+\langle R_t f,R_t h\rangle,
\quad G_t=A_t+R_t^*R_t,
\]
where Q_t is the full native form and R_t is normalized actual selected negative analysis. Suppose G_a and G_b are strictly coercive for 0<a<b. Define on the same selected coefficient space M=l2(s)
\[
L_s(t)=R_tG_t^{-1}R_t^*,\qquad D_s(t)=I_M-L_s(t).
\tag{1}
\]
Then
\[
L_s(b)-L_s(a)\ge0,\qquad D_s(a)-D_s(b)\ge0.
\tag{2}
\]
The kernel of either difference is exactly the fixed selected-source redundancy space Z defined below. Thus (2) is strictly positive on Z^\perp, equivalently on M/Z.

This is the same finite matrix as in the preceding dilation construction, expressed intrinsically through physical support inclusion. It does not require equality of Hilbert Riesz operators in different domains. It does not exclude a zero of D_s, compute its entries, or supply a quantitative crossing slope.

## Common row redundancy, before counting rank

Let eta_q be the normalized negative source profile at actual coordinate q:
\[
\eta_q(x)=\tfrac12(e^{-iz_qx}-e^{-i\bar z_qx}),\qquad
n_q(g)=\int\overline{\eta_q(x)}g(x)\,dx.
\]
For u in M set
\[
H_u(x)=\sum_{q\in s}u_q\eta_q(x),\qquad
Z=\{u:H_u\equiv0\}.
\tag{3}
\]
For every t>0,
\[
Z=\ker R_t^*.
\tag{4}
\]
Indeed R_t^*u=0 means integral conj(g) H_u=0 for every g in D_t, hence for every compact smooth interior test. The analytic exponential polynomial H_u vanishes on (-t,t), and therefore identically. The converse is immediate.

Thus Z is independent of the support window. It contains dependencies from identical copies, any zero critical-line negative rows, and other linear relations among selected profiles. It is the kernel of the actual finite selected forcing map; cardinality alone does not determine its codimension.

L_s(t) annihilates Z and, being self-adjoint, preserves Z^\perp. D_s(t) is the identity on Z. Those directions are constant and do not participate in contact. The finite matrix on Z^\perp retains the negative index and nullity of D_s(t), and hence of the full native form wherever G_t is coercive.

## Exact variational identity under physical inclusion

For u in M let h_t(u)=G_t^{-1}R_t^*u, the unique actual physical vector in D_t satisfying
\[
\mathfrak g_t(g,h_t(u))=\langle R_tg,u\rangle
\quad(g\in D_t).
\tag{5}
\]
This is defined by the positive form, independent of which equivalent Hilbert coordinates are used to compute the Riesz inverse.

Physical inclusion D_a->D_b preserves the original vector, all actual selected source values, and the full native mixed form. In particular
\[
\mathfrak g_b(g,h)=\mathfrak g_a(g,h)\quad(g,h\in D_a).
\tag{6}
\]
The different frozen prime index sets do not invalidate (6): newly present translations have disjoint old supports and zero old-domain pairing, including equality thresholds.

The variational formula is
\[
\langle u,L_s(t)u\rangle
=\sup_{h\in D_t}\left[
2\operatorname{Re}\langle R_th,u\rangle-\mathfrak g_t(h,h)
\right].
\tag{7}
\]
Complete the square at h_t(u) to prove it; coercivity gives the unique maximizer. Domain inclusion and (6) immediately yield (2).

More precisely, writing h_a for its unchanged physical inclusion in D_b,
\[
\boxed{\quad
\langle u,[L_s(b)-L_s(a)]u\rangle
=\mathfrak g_b(h_b(u)-h_a(u),h_b(u)-h_a(u)).
\quad}
\tag{8}
\]
To check this identity, the h_b term has energy <u,L_s(b)u>, the h_a term has energy <u,L_s(a)u>, and (5) gives the cross term <R_bh_a,u>=<u,L_s(a)u>, which is real. This proves the exact nonnegative gap, rather than relying on a comparison of inverse operators on unrelated Hilbert spaces.

Equation (8) vanishes if and only if h_b(u)=h_a(u). This is where strictness needs more than an abstract variational argument.

## Strictness from actual finite exponential forcing rigidity

Suppose u is not in Z and equality holds in (8). Equation (4) and coercivity imply h_a(u)!=0. The common vector h=h_a(u)=h_b(u) is supported in [-a,a] and satisfies, against every g in D_b,
\[
Q_b(g,h)=\langle R_bg,u-R_bh\rangle
=\int\overline{g(x)}H_{u-R_bh}(x)\,dx.
\tag{9}
\]
The right side is a finite exponential polynomial forcing.

The existing strict-margin finite-forcing proof rules out any nonzero compactly supported actual logarithmic vector satisfying such an equation on a strictly larger window. For clarity, its argument does not require the forcing to have the special selected-null coefficient -Rh:

Choose a<c<b and a small shift range such that translating h stays in D_c and translating any test in D_c stays in D_b. Actual native simultaneous translation covariance converts (9) into equations for all small translates of h on D_c. Every translated forcing is still in the fixed finite-dimensional span of the exponentials underlying H. Its physical pairings therefore have logarithmic Riesz representatives in one finite-dimensional subspace V of D_c.

The actual native operator A_c has finite kernel, so
\[
\dim A_c^{-1}(V)\le\dim\ker A_c+\dim V<\infty.
\]
All the small translates would lie in this finite-dimensional space. Distinct translates of a nonzero compactly supported vector are independent by the already proved Fourier exponential-polynomial argument, giving a contradiction. No positivity at the intermediate native window is needed.

Thus equality in (8) is impossible for u outside Z. For u in Z both h_a(u) and h_b(u) are zero, so equality holds. We have proved
\[
\ker[L_s(b)-L_s(a)]=Z,\qquad
L_s(b)-L_s(a)>0\ \hbox{on }Z^\perp.
\tag{10}
\]
Because Z^\perp is finite-dimensional, each fixed pair a<b has a positive minimum eigenvalue of this difference there. Its value is not computed and no lower bound uniform as b approaches a is established.

The forcing argument uses the full actual native form and genuine physical support margin. No translation covariance of a selected-background form is asserted.

## Agreement with the dilation matrix

Let U_t:D_1->D_t be physical L2 dilation, which is a bounded isomorphism of canonical logarithmic domains. Pulling back (5)-(7) by U_t gives exactly the fixed-carrier inverse and selected matrix from the preceding pass. The scalar suprema for every u agree, so polarization identifies their entire matrices.

Thus the Loewner order compares one actual coefficient matrix, even though the physical supports and canonical domain norms vary. No unitary equivalence of the physical inclusions or presumed equality of the differently represented Riesz operators is needed.

Near a nonnegative null window, the previous theorem provides one finite s with coercive G_t throughout a neighborhood. Equations (2) and (10) apply to every ordered pair of apertures within that neighborhood. On the observable quotient the matrix D_s(t) is strictly decreasing in Loewner order.

For the minimal r-row selection independent on the contact kernel, Z=0. Its r-dimensional matrix therefore decreases strictly between any two distinct nearby apertures, is zero at contact, positive definite on the left, and negative definite on the right. The independent-row condition on the kernel implies independence of the entire selected profiles, so this minimal selection has no hidden global forcing redundancy.

## Consequences and limits

On any interval where the same G_t is coercive, compress D_s(t) to Z^\perp and order its d=dim Z^\perp eigenvalues. Strict Loewner order makes each ordered eigenvalue strictly decreasing between distinct apertures. Each can hit zero at most once. Therefore
\[
\sum_{t\ {\rm in\ the\ interval}}\dim\ker Q_t\le d.
\tag{11}
\]
This is a local fixed-selection rank budget, not a global finite defect-index assumption. If effective covariance loses coercivity, the inverse and matrix need a new construction; the selection is not extrapolated beyond its proved interval.

The identity (8) also supplies a direct target for future quantitative work: bound the effective-form energy of the change in the actual forced solution. Strictness alone does not give a derivative, first-jet coercivity, a numerical inverse bound, or a lower crossing rate. The existing family is proved continuous and is not asserted differentiable at prime thresholds.

This monotonicity is compatible with finite contact. A strictly decreasing positive matrix can reach zero and become negative, exactly as the local contact theorem permits. Neither Loewner order nor the finite-source representation proves that the actual matrix remains positive at every aperture. Independent actual sign information is still required.

## Validation and custody

Analytic validation: the support-consistent mixed form, exact square completion and gap identity, fixed analytic row redundancy, generalized finite-forcing translation contradiction, and finite-dimensional min-max order are explicit. No actual inverse matrix entries or numerical controls are presented as universal proof.

Primary pinned repository sources:
- LOCAL_FINITE_SOURCE_MATRIX_20261006: local fixed selection, coercive effective covariance, exact full-native inertia matrix and null reconstruction.
- FINITE_SELECTED_FORCING_OBSTRUCTION_20261004: finite translated forcing preimages and strict-margin contradiction.
- POSITIVE_CARRIER_EQUIVALENCE_20261004 and ACTUAL_FIRST_CONTACT_CONSTRUCTOR_20261004: actual complete source/native domain and support/dilation custody.

No historical retained packet identification, actual endpoint existence, endpoint exclusion, raw Green preimage, global positivity or RH conclusion. No Lean/workflow changes or new CI run; historical notes unchanged. Numerical frontier remains 81/100. F4 and FULL TRANSPORT CLOSED remain open.
