# RPB108: prescribed covariance determines the reduced actual packet

Date: 2026-10-06 (America/Los_Angeles). Source `974e20325cc7a980b827c84f44668fd2c4378ca5`.
Definitions: [prescribed reduction registry](../docs/TERMINOLOGY_RPB108_PRESCRIBED_REDUCTION.md).
Global/F4 lane; no aperture computation or contact existence assertion.

## Closure obtained and entry gates retained

At a hypothetical actual nonnegative window, a prescribed historical synthesis can be identified with the fresh actual root synthesis after its canonical positive-kernel quotient. An independent positive-coordinate unitary compatibility premise is unnecessary **once the exact covariance and prescribed row gates hold**. The unitary is constructed below.

Moreover, a retained attained-neutral morphology admits an additive replacement on that reduced carrier with the same physical vector, selected coefficient, arithmetic data and null-extension interface. Its historical filtration can be reduced by intersection, and its sequence reconstructed constantly from the attained right-limit packet. No invariance of that filtration under orthogonal projection is required.

This closes a fixed-packet compatibility implication. It does not establish that any prescribed historical P,C or selected rows satisfy the actual gates. It does not identify its filtration with physical support, exclude contact, or supply enlarged nullity.

The precise independent gates are:

1. Identify the historical physical Hilbert carrier with actual H=D_c, preserving the logarithmic metric and physical L2/extension custody.
2. Identify its prescribed selected rows and normalization with one actual finite map R. This is a named-selection claim, not existence of some separating selection.
3. Establish the same-domain actual covariance and signed factor identities
   \[
   PP^*=A+R^*R=G,\qquad PC=-R^*.
   \tag{1}
   \]
4. For these prescribed rows prove ker A intersect ker R={0}. At a nonnegative Fredholm window this is exactly coercivity of G.

Given these gates, all positive-coordinate reductions below are explicit. The covariance identity in (1) may be obtained from an exact all-domain quadratic identity by polarization, using boundedness of the compared forms; analogous formulas on different domains do not suffice. No physical operator-domain membership or global H1 is assumed.

Equivalently, writing the historical negative synthesis as N_hist=-PC, it suffices to attach N_hist=R* and its full physical neutral operator PP*-N_hist N_hist*=A. A selected-only operator is not the full A: using the complete actual positive synthesis with only selected negatives generally leaves the unselected negative covariance. That omitted background cannot be removed by the quotient theorem.

## Explicit quotient unitary

Let G>=beta I with beta>0, F=G^(1/2), and L=(ker P) perpendicular. Since PP*=G, P is onto: h=P(P*G^-1h). Its range-adjoint L is closed, and
\[
\Pi_L=P^*G^{-1}P,
\qquad U_{all}=F^{-1}P,
\qquad U_{all}U_{all}^*=I_H,
\qquad U_{all}^*U_{all}=\Pi_L.
\tag{2}
\]
Thus U=U_all restricted to L is a Hilbert unitary L to H with inverse U*=P*F^-1. The canonical quotient V/ker P, with its Hilbert quotient metric, is represented by L. There is generally no unitary on the entire original V identifying P with the injective root synthesis when ker P is nonzero.

On this reduced carrier,
\[
P|_L=FU,\qquad U(P^*h)=Fh,
\qquad U\Pi_L C=-F^{-1}R^*=C_0.
\tag{3}
\]
The equations include the specified Hilbert adjoints; an arbitrary bounded carrier isomorphism would not establish them. They are fixed-window identities and do not assert a common unitary on changing apertures or changing prescribed selections.

Every prescribed factor C satisfying (1) decomposes as
\[
C=U^*C_0+Z,\qquad Z=(I-\Pi_L)C,\qquad PZ=0.
\tag{4}
\]
In particular ||Cv||^2=||C_0v||^2+||Zv||^2 for all v in M. Thus C can differ globally from the reduced actual compensator; identical physical synthesis equations alone do not identify the full historical positive coefficient map.

## The attained vector has no padding

Suppose the retained endpoint equations on the same k,u are
\[
a=Cu=P^*k,\qquad C^*Cu=u.
\tag{5}
\]
Since P*k belongs to L, Zu=0. The signed factor in (1) and (5) give
\[
Rk=(-PC)^*k=-C^*P^*k=-u,
\quad Gk=PCu=-R^*u,
\quad Ak=Gk-R^*Rk=0.
\tag{6}
\]
Hence these actually attached retained equations yield full native nullity, not effective-background nullity. The physical vector k is unchanged. The selected coefficient u is exactly -Rk, not a newly chosen coefficient on another selection. Coercivity gives k=-G^-1R*u, the established actual finite null reconstruction.

Applying (3)-(4) to the retained witness gives
\[
a_0=Ua=Fk=C_0u,\qquad C_0^*C_0u=u.
\tag{7}
\]
The last equality follows from C*C=C_0*C_0+Z*Z and Zu=0; it is an operator equation on the same u, not just equality of norms. Endpoint nonzero and norm/signature are preserved by the unitary on L. Positive source analysis becomes Fk in the root coefficient metric. Raw complete actual source coordinates remain those of the unchanged physical k; the positive metric here is the effective covariance metric, not a relabelling of the complete raw P_0 coordinates.

This derives the unitary comparison previously listed as an independent sufficient target in GLOBAL_F4_ENTRY_AUDIT, under the explicit covariance gates. It neither silently assumes the gates nor identifies an existential finite selection with R.

## Historical right-limit geometry survives by intersection

Let B(t) be the retained monotone closed submodule of V plus the finite negative carrier M. Set V_red=L plus M and W=U plus identity_M. Define
\[
\widehat B(t)=W\bigl(B(t)\cap V_{red}\bigr).
\tag{8}
\]
Each intersection is closed in V_red, W is a unitary onto H plus M, and these spaces are monotone. The repository rightLimit is the intersection of B(t) for t>c. Therefore
\[
\operatorname{rightLimit}\widehat B(c)
=W\bigl(\operatorname{rightLimit}B(c)\cap V_{red}\bigr).
\tag{9}
\]
This uses intersection and a bijective isometry, not the image of an arbitrary closed subspace under a noninjective projection.

The retained endpoint (a,u) is in rightLimit B(c), and a belongs to L by (5). Thus (a_0,u) is in rightLimit of the reduced filtration. AttainedNeutral in CriticalDichotomy.lean retains ||a||^2=1/2 and jValue(a,u)=0, so ||u||^2=1/2 and the reduced total coefficient norm is one.

Use t_n=c+1/(n+1), a'_n=a_0, u'_n=u and phi'(n)=n. Then every coefficient belongs to the reduced filtration at t_n, has norm one and signature zero. Both coefficient sequences converge strongly to their constant limit, and phi' is strictly increasing. These are exactly the four NeutralCriticalBranch fields, as well as the right-limit/nonzero fields of NeutralDefectMorphology. No projection of the original sequence is used.

Together with (7), P'=F and C'=C_0 supply its coefficientCarrier, unitGain and physicalAdjoint fields. Its physical null operator is F^2-R*R=A, so physicalNull is on the same k. Keeping the attached arithmetic record, extend map and original null-extension interface unchanged preserves their types and the equality kExt=extend k. Thus every retained morphology field has an analytic reduced replacement when the gates hold. This is an additive mathematical construction; no replacement of historical source text or compiled Lean instance is claimed.

Transporting a record preserves its arithmetic assertions but does not identify independently named density/Q or stop operators with the actual ones. If that custody is absent, it remains an independent gate for the prescribed record. Alternatively FRESH_ARITHMETIC_STOP constructs fresh actual arithmetic and stop data for this now-attached physical k, in an additively named replacement. That alternative is not identity with the prescribed historical arithmetic/stop fields and still returns the obstructed persistenceGoal.

Equation (8) preserves the historical filtration through reduction. It does not identify it with the fresh physical-support filtration built in FRESH_FIXED_RIGHT_PACKET. If a downstream theorem needs that additional physical interpretation of B(t), the smallest remaining gate is its actual support/subspace identity on the relevant windows. The morphology record itself does not contain that identity.

## Projection pitfall and controls

Orthogonally projecting an arbitrary historical sequence or subspace can destroy neutrality or membership. In rational coordinates let l and z be orthonormal positive directions and let e1,e2 be negative directions. Set w=(l,-e1) and v=(z,e2). Both have zero signature. Let B be their span. Projection onto span(l) in the positive slot sends v to (0,e2), which is strictly negative and is not in B. Nevertheless w is already reduced; B intersect the reduced carrier is its span, and the constant sequence w survives exactly. Normalization by sqrt(2) supplies the abstract unit coefficient required by WD-T17.

The exact script also uses P=r(cos,sin), R=(r,0), and columns C=(-l,zeta z), with rational orthonormal l,z. It checks PP*=r^2, PC=-R*, projection/coisometry identities, compensator decomposition, retained unit gain on u=(-r,0), reconstructed h=1, and the fact that global invisible padding need not vanish. These are padded algebra controls, not actual divisor or historical packet realizations.

## Remaining obligations and F4 scope

The fixed-window positive-coordinate compatibility theorem and reduced retained morphology replacement are now analytic consequences of the explicit named gates. The remaining prescribed attachment theorem is the same-domain actual covariance/signed-row dictionary and separation condition for that prescribed selection, after actual physical-carrier custody. The existing fresh existential selection does not prove that theorem.

Actual density/Q, arithmetic and stop custody retain their independent scopes when a prescribed historical field is demanded. The reduction removes neither those identifications nor an independently requested physical interpretation of the historical filtration.

Global actual nonnegative-contact exclusion remains independent. Same-vector enlarged full native cancellation remains obstructed: (6) supplies endpoint nullity only, and the unchanged k has nonzero residual on every strict enlargement. Reducing coefficient padding cannot change that residual. No dilation is used anywhere in (2)-(9). Completing a reduced historical morphology does not complete its persistenceGoal or the F4 support-gap upper pairing.

Pinned custody and exact repeated controls are in notes/data/RPB108_PRESCRIBED_REDUCTION_20261006.json. Proofs are analytic; no Lean/compiler/workflow change or new CI/axiom certificate. Frontier remains whole-domain 23/25 with independent 93/100 inputs pending. Historical wording/certificates preserved. F4 and FULL TRANSPORT CLOSED remain open.
