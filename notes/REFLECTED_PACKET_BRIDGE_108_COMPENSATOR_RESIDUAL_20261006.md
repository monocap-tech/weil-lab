# RPB108: actual compensator gain excess equals effective inverse residual energy

Date: 2026-10-06. Source base: `97ca123760cc1d3510234a00b74348c129a1fa14`.
Definitions: [compensator residual](../docs/TERMINOLOGY_RPB108_COMPENSATOR_RESIDUAL.md).
Lane: global/F4. No aperture calculation or actual contact existence is asserted.

## Result

For the fresh actual fixed packet conditional on a nonnegative null window c, reduced signed compensators on nested supports satisfy
\[
C_a=\Pi_{L_a}C_t\quad(0<a<t\le b).
\tag{1}
\]
For any nonzero endpoint-null k, its unchanged selected coefficient u=-R_c k and positive coefficient a=C_cu obey
\[
\boxed{\quad\|C_tu\|^2-\|u\|^2
=\|C_tu-a\|^2
=\langle r_t,G_t^{-1}r_t\rangle>0.\quad}
\tag{2}
\]
The inner product in (2) is real. This is an exact actual gain identity on the same physical vector and fixed finite selection, not a numerical crossing estimate.

Every exact signed synthesis factor at t has at least this gain. Adding components in ker P_t, changing coefficient coordinates unitarily, or dropping reducedness cannot restore contraction. The fresh endpoint maps also give concrete witnesses for the previously imported DouglasUnitData premise; no additional Douglas range theorem is needed for this surjective synthesis.

Finally the inverse-residual step is a lawful actual negative trial with exact energy:
\[
v_t=G_t^{-1}r_t,\qquad
\widetilde k_t=I k-v_t,\qquad
Q_t(\widetilde k_t,\widetilde k_t)
=-\langle r_t,G_t^{-1}r_t\rangle-\|R_tv_t\|^2<0.
\tag{3}
\]
The physical vector in (3) changes. It is the forced effective-inverse vector associated with u, not a same-vector enlarged null witness. These results are consistent with contact followed by negativity, and do not exclude contact.

## Nested projections and actual reducedness

Use the fixed background on D_b and the source maps from FRESH_FIXED_RIGHT_PACKET. For any 0<t<=b, G_t is coercive by support compression. FJ_t is bounded below with closed range L_t. The positive coefficient spaces L_a are nested as physical supports increase. Their orthogonal projections are
\[
\Pi_{L_a}=FJ_aG_a^{-1}J_a^*F,
\]
since (FJ_a)*(FJ_a)=G_a. Writing J_a=J_t I_(a,t) and using R_a=R_t I_(a,t), direct multiplication yields (1). It uses Hilbert adjoints on the fixed logarithmic coefficient carrier, not an identification of the distinct physical Riesz operators.

Every C_t has image in L_t=(ker P_t) perpendicular and satisfies P_tC_t=-R_t*. Thus it is the unique reduced signed synthesis factor. If X is another exact factor, P_tX=-R_t*, then Z=X-C_t has image in ker P_t, and for every u,
\[
\|Xu\|^2=\|C_tu\|^2+\|Zu\|^2.
\tag{4}
\]
This proves its minimal pointwise gain and reduced uniqueness, including when ambient P_t has a nontrivial kernel. It is not a minimum-energy solution for a different coefficient constraint; the exact synthesis equation and its sign are fixed.

Equation (1) gives the entire covariance gap
\[
C_t^*C_t-C_a^*C_a
=(C_t-C_a)^*(C_t-C_a).
\tag{5}
\]
This realizes the already proved finite-source Loewner energy gap as the squared norm of an orthogonal compensator increment. The strictness outside the fixed analytic row redundancy remains the finite-forcing theorem already proved; it is not reproved or assumed from projection order alone.

## Concrete Douglas input for the fresh maps

In Screening/Douglas.lean take Spos=P_t and Sneg=R_t*. The unsigned reduced factor is -C_t. The reduced_exists_unique field follows from (4).

For factorization_iff, an exact contractive factor gives covariance majorization immediately by taking adjoints. Conversely assume covariance majorization. Restrict P_t to L_t: this is an invertible synthesis with covariance G_t. The physical defect is
\[
A_t=P_{t,red}(I-C_tC_t^*)P_{t,red}^*,
\]
where C_t is regarded as a map into L_t. Covariance majorization means A_t>=0, so congruence gives I-C_tC_t*>=0, equivalently ||C_t||<=1. This is a proof from the explicit reduced inverse, not an invocation of DouglasUnitData to prove itself. It supplies the unsigned factor -C_t with Sneg=P_t(-C_t).

Thus both fields of DouglasUnitData R_t* P_t are concretely witnessed for every support in this fixed background interval, including an indefinite support where the factorization_iff simply has two false sides. Existence of the reduced exact factor does not assert it is contractive. At contact it is contractive with unit gain; beyond contact (2) rules out contraction. This closes an imported screening-interface premise for the fresh construction, not for an independently prescribed historical synthesis.

## Exact same-vector increment and enlarged residual

Let k be endpoint-null, u=-R_c k and a=FJ_c k. In D_t, actual support custody preserves Q_t(Ik,Ik)=0 and R_t Ik=-u, but strict-margin rigidity gives r_t=A_t Ik nonzero. Because
\[
r_t=G_t Ik-R_t^*R_t Ik,
\]
one has
\[
C_tu-a=-FJ_tG_t^{-1}r_t=\delta_t.
\tag{6}
\]
By (1), Pi_(L_c) C_tu=C_cu=a, hence delta_t is orthogonal to L_c, including a. Since ||a||=||u|| at the endpoint, Pythagoras gives the first equality in (2). The identity (FJ_t)*(FJ_t)=G_t gives the second. Coercivity and r_t nonzero give strict positivity.

The enlarged physical adjoint is still P_t*Ik=FJ_tIk=a in the fixed coefficient carrier. It is C_tu that changes: it gains a nonzero component orthogonal to the old positive carrier. In fact
\[
P_t\delta_t=-r_t.
\tag{7}
\]
Thus the failed same-vector physicalAdjoint equation is measured exactly by the enlarged mixed residual. Unchanged source samples and neutral J-signature remain lawful; they are insufficient for the new compensator relation.

Equation (4) implies ||Xu||>||u|| for every exact factor X at the enlarged support. A unitary positive/negative coefficient relabelling preserves these norms. An arbitrary nonunitary map changes the metric and cannot be used as an adjoint-preserving same-packet transport. No coordinate choice that preserves the actual Hilbert/source metrics repairs (6)-(7).

## A canonical actual negative trial from the same coefficient

Define v_t and tilde k_t as in (3). Both are in D_t by bounded effective inversion. Actual source covariance gives
\[
\widetilde k_t=-G_t^{-1}R_t^*u,\qquad
C_tu=FJ_t\widetilde k_t.
\]
This formula extends the effective forcing constructor beyond contact, but the null reconstruction theorem applies only to coefficients in ker D_s(t). The unchanged endpoint u is not such a coefficient at t: its gain in (2) is strictly above one.

To verify (3), put e_t=<r_t,G_t^(-1)r_t>. Then Q_t(v_t,Ik)=e_t and
\[
Q_t(v_t,v_t)=\langle v_t,G_tv_t\rangle-\|R_tv_t\|^2
=e_t-\|R_tv_t\|^2.
\]
Expanding Q_t(Ik-v_t) with Q_t(Ik)=0 proves (3). In particular this change of physical vector produces a negative witness, not an enlarged null one. The earlier residual perturbation theorem and finite-response negative-trial mechanism remain valid; this formula chooses the full effective inverse step and identifies its exact energy.

## Exact finite controls and remaining theorem

The rational script uses an invertible analysis factor F=[[alpha,s],[0,tau]], R=(alpha,nu), and endpoint inclusion Jx=(x,0). Its G=F*F is coercive, the endpoint compressed defect is zero, and the enlarged residual is (0,alpha(s-nu)). It checks both compensators, projection identity, gain excess, inverse-residual energy, residual sign (7), and negative-trial energy (3) for rational parameter choices. General factors use P=F*; the actual construction uses the self-adjoint square root. These are algebra controls, not actual-zeta endpoint examples.

The failed implication is now exact: fresh right-limit coefficient custody + endpoint reduced unit gain -> contractive exact screening or the same physical-adjoint relation in a larger support. Equation (2) disproves it on any hypothetical actual contact, without a new aperture estimate. This belongs to null transport and the screening interface. It does not infer that the hypothetical contact is impossible.

The smallest decisive global theorem remains actual nonnegative-contact exclusion, or an arithmetic endpoint estimate that supplies it. The fresh packet, its Douglas data, and its complete analytic morphology no longer need an independent factorization/filtration construction. Prescribed historical identification and Lean certification retain their separate scopes. F4 and FULL TRANSPORT CLOSED remain open.

## Custody and validation

Pinned inputs: FRESH_FIXED_RIGHT_PACKET_20261006; FRESH_ARITHMETIC_STOP_20261006; FINITE_SOURCE_LOEWNER_20261006; FINITE_SELECTION_EFFECTIVE_POSITIVE_REALIZATION_20261006; TRANSLATION_NULL_EXTENSION_OBSTRUCTION_20261004; WeilDefect/Screening/Douglas.lean. Blob custody is in the manifest. Analytic checks cover projection types, reduced uniqueness, both Douglas directions, same-vector source custody, inverse-energy equality and the negative-trial expansion. Exact controls repeated; no Lean/compiler/workflow changes or new CI/axiom claim. Historical records preserved.
