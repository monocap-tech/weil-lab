# RPB108: actual selection augmentation transports the null coefficient by a graph

Date: 2026-10-06 (America/Los_Angeles). Source `cf54521bce68e5a8d5a5266ff6e52168ddd8469f`.
Definitions: [selection augmentation registry](../docs/TERMINOLOGY_RPB108_SELECTION_AUGMENTATION.md).
Global/F4 lane. Whole-domain positivity remains certified through 23/25; the independent 93/100 finite stage has advanced but corrected whole-domain sign is pending.

## Results and scope

For two nested finite actual selections with coercive old effective covariance, the finite source defect has an explicit Schur congruence. Its null coefficient is transported by a graph lift, with the same physical native null vector. Zero-padding is lawful exactly when the added samples on that vector vanish.

A blind prescribed selection can always be enlarged by finitely many actual coordinates to separate the full finite kernel. This discharges an inverse gate for the **enlarged** selection only. It does not discharge the prescribed gate, preserve its coefficient norm automatically, or identify the prescribed synthesis with the enlarged one.

Finally, effective residual gains for two coercive finite selections are locally uniformly comparable. Their quadratic-decay/H1 criterion is invariant under changing selections. Thus choosing more rows cannot close the missing endpoint regularity theorem by improving the rate from nonquadratic to quadratic.

## Exact finite Schur identity

Work on a fixed actual support H with A self-adjoint. Let R and T be disjoint finite coordinate selections from the complete actual negative analysis and suppose G=A+R*R is coercive. Set Gplus=G+T*T, J=I+T G^-1 T* and B=R G^-1 T*. J is positive definite. Woodbury follows by multiplying the two sides by Gplus:
\[
Gplus^{-1}=G^{-1}-G^{-1}T^*J^{-1}TG^{-1}.
\tag{1}
\]
Writing D=I-RG^-1R*, the actual augmented source defect is
\[
Dplus=\begin{pmatrix}
D+BJ^{-1}B^*&-BJ^{-1}\\
-J^{-1}B^*&J^{-1}
\end{pmatrix}.
\tag{2}
\]
For x in M,y in L its exact quadratic is
\[
\langle(x,y),Dplus(x,y)\rangle
=\langle x,Dx\rangle+
\langle y-B^*x,J^{-1}(y-B^*x)\rangle.
\tag{3}
\]
Equivalently, Dplus is the congruence of diag(D,J^-1) by the invertible triangular matrix with upper-right block -B. Therefore negative index and nullity are unchanged, and
\[
\ker Dplus=\{(u,B^*u):u\in\ker D\}.
\tag{4}
\]
This works wherever the old G is coercive, even if A is indefinite. No contact-exclusion assumption is used. Adding source coordinates changes the response matrix dimension but cannot remove its representation of a native kernel.

## Same physical vector, changed selected coefficient

For u in ker D reconstruct h=-G^-1R*u. Then u=-Rh and
\[
B^*u=TG^{-1}R^*u=-Th.
\tag{5}
\]
The augmented coefficient is therefore uplus=(-Rh,-Th). Since Ah=0,
\[
Gplus h=-Rplus^*uplus,
\qquad -Gplus^{-1}Rplus^*uplus=h.
\tag{6}
\]
The physical h in (6) is exactly unchanged. Both its old and new selected coordinates are actual samples of this same h, with their prescribed energy weights. This closes the finite-selection null transport law. It says nothing about native mixed-nullity at a larger support.

Zero-padding (u,0) belongs to ker Dplus if and only if Th=0. When Th is nonzero, its new defect quadratic is the strictly positive second term in (3). A unitary relabelling of the enlarged negative coefficient carrier cannot turn the new coefficient into (u,0), since
\[
\|uplus\|^2=\|u\|^2+\|Th\|^2.
\tag{7}
\]
At nonnegative contact, the root positive coefficient is Gplus^(1/2)h and has this same squared norm. If the old retained neutral total coefficient had norm one, the new same-vector packet has total squared norm
\[
1+2\|Th\|^2.
\tag{8}
\]
Restoring norm one divides h and both coefficient slots by sqrt(1+2||Th||^2). That is the same null ray but a changed physical vector. It cannot be used as transport of a prescribed unchanged normalized k. If Th=0, both selected norm and unit normalization are preserved, and the two root positive coefficients of this particular h have equal norm; global positive-carrier covariance equivalence is still a separate map, since Gplus generally differs from G.

## Repairing a blind prescribed selection

At an actual nonnegative window, K=ker A is finite and the full actual negative analysis is injective on K, by the existing complete source identity and positive-source injection. Start with any prescribed finite R. The blind subspace Kblind=K intersect ker R is finite. Finitely many further actual coordinates separate it; choose them outside the old set because old coordinates vanish on Kblind. Then Rplus is injective on all K, so Gplus is coercive. Partner closure may be added afterwards without losing separation.

This is a lawful finite actual augmentation theorem; it reuses the already proved finite-coordinate compactness argument on Kblind. It constructs a replacement selection, not the prescribed missing inverse. Equations (1)-(4) cannot be applied with a singular old G.

For an attached retained nonzero full-null h whose old selected coefficient is nonzero, the new root packet can still be constructed directly from Gplus and uplus=-Rplus h. Its unit gain and physical adjoint hold on h. Equations (7)-(8) still govern whether the original normalized physical vector survives the WD-T17 unit normalization. No theorem says the separating added coordinate samples vanish on that h.

The blind kernel also explains loss of named physical reconstruction: if G is singular, any d in Kblind obeys Gd=0, Rd=0, and P*d=0 for a synthesis PP*=G. Thus h and h+d have the same retained positive-adjoint and selected negative coefficients, while being different physical vectors. A packet equation alone cannot choose that blind component.

An exact two-dimensional control is A=0, complete positive and negative analyses both identity, R(x,y)=x, and h=(1,1). The old G=diag(1,0) is singular. P(v)= (v,0), C(u)=-u give Cu=P*h with u=-1 and C*C u=u; h+d for d=(0,z) is invisible to this packet. The only new disjoint coordinate is T(x,y)=y. It separates the blind kernel, but Th=1, so the same-vector negative norm increases from one to two. This is an algebraic source control, not an actual-zeta kernel. It disproves automatic zero-padding/normalization-preserving prescribed repair.

Even allowing an orthogonal subspace of the unselected negative carrier does not always repair this: in that control the unselected carrier is one-dimensional and Th is nonzero. Mixing old coordinates into an added row to cancel Th can double-count the old source metric; such a row is not automatically a disjoint coordinate selection with the same actual source covariance.

## Gain-rate invariance under augmentation

On a common support near contact, keep the same full native enlarged residual r_s=A_t Ih. Let G_t and Gplus_t=G_t+T_t*T_t be the two effective covariances. Since G_t is uniformly coercive and finite observations T_t are locally uniformly bounded, there is a finite support-independent M with
\[
0\le T_t^*T_t\le M G_t.
\]
Consequently
\[
G_t\le Gplus_t\le(1+M)G_t,
\qquad
\frac{1}{1+M}G_t^{-1}\le Gplus_t^{-1}\le G_t^{-1}.
\]
The same-vector gain identities therefore give
\[
\boxed{\frac{e_s(h)}{1+M}\le eplus_s(h)\le e_s(h).}
\tag{9}
\]
This compares effective inverse norms of the same native residual; it does not assert that the compensators or unchanged selected coefficient vectors are equal. At the endpoint their coefficients are related by (5).

Any two finite separating selections can be compared through their finite union, so their gain functions are locally uniformly comparable in both directions. In particular O(s^2) and o(s^2) are selection-independent for the same physical null vector. The existing quadratic gain criterion identifies these with global H1. A non-H1 mode retains infinite limsup of gain/s^2 after every such change. Finite source optimization may improve constants but cannot supply the missing regularity rate. This obstruction belongs to endpoint exclusion.

## Remaining theorem and validation

Prescribed attachment: finite augmentation closes the separating-selection existence gate for a newly named packet. It does not prove the exact source/covariance dictionary of a prescribed historical packet or its blind-kernel gate. Same normalized physical-vector replacement additionally needs added samples to vanish; otherwise rescaling must be declared.

Global endpoint: the missing actual quadratic gain estimate on the whole contact kernel remains an arithmetic theorem, invariant under the choice of coercive finite selection. Schur augmentation cannot eliminate a genuine contact zero, and cannot produce enlarged full mixed cancellation. The exact finite-selection transport (6) is distinct from support enlargement; dilation is not used.

Pinned source blobs and repeated rational controls are in notes/data/RPB108_SELECTION_AUGMENTATION_20261006.json. Controls check Schur blocks, graph nullity, reconstruction, failed zero-padding, Woodbury residual energy and inverse-norm comparison; the blind selection control checks normalized-norm loss and nonunique physical reconstruction. These are algebra controls, not actual arithmetic matrices. Analytic arguments are not Lean certified. No Lean/workflow edits or new CI/axiom claim. Historical wording/certificates preserved. F4 and FULL TRANSPORT CLOSED remain open.
