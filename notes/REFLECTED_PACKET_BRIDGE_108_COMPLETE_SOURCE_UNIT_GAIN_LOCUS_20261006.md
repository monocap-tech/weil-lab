# RPB108: complete-source unit gain is isolated and equals the actual kernel image

Date: 2026-10-06 (America/Los_Angeles). Live source abcfc270813eb3cd2f44085f084aa6c2f5a3ffa2.
Definitions: [complete-source unit-gain locus](../docs/TERMINOLOGY_RPB108_COMPLETE_SOURCE_UNIT_GAIN_LOCUS.md).
Analytic fixed-window attachment theorem; no new actual endpoint estimate.

## Intrinsic source characterization

At a hypothetical nonnegative actual window, keep H the canonical logarithmic carrier, A=P0*P0-N0*N0=I+compact, and K=ker A. The complete actual positive covariance L=P0*P0 is coercive by the existing positive carrier equivalence.

Define the minimal complete-source compensator and response
\[
C_{\rm all}=-P_0L^{-1}N_0^*,\qquad
D_{\rm all}=I-C_{\rm all}^*C_{\rm all}
=I-N_0L^{-1}N_0^*.
\tag{1}
\]
Since A>=0, N0*N0<=L and C_all is contractive. Its exact unit-gain locus is
\[
\boxed{\ker D_{\rm all}=N_0(K).}
\tag{2}
\]
To prove this directly, for u in ker D_all set h=-L^(-1)N0*u. Then N0h=-u and
Ah=Lh-N0*N0h=-N0*u+N0*u=0. Moreover C_all u=P0h, so the physical adjoint for P=P0* is automatic. Conversely for h in K, u=-N0h gives D_all u=0 and reconstructs the same h. N0 is injective on K, so these are inverse linear bijections. No finite selected rows, regularity assumption or enlarged window is used.

Thus the finite-dimensional compression W=N0(K) from the preceding pass is intrinsic: W is exactly the unit-gain eigenspace of the complete actual compensator, rather than an arbitrary selected observation space. This characterization is not an endpoint exclusion: if an actual nonzero K exists, C_all attains gain one exactly there.

## Strict complement gap without compact negative analysis

Set
\[
T=N_0L^{-1/2},\qquad
B=L^{-1/2}AL^{-1/2}=I-T^*T,\qquad
U=P_0L^{-1/2}.
\tag{3}
\]
U is an isometry and C_all=-UT*. B is positive Fredholm, because it is the invertible congruence of A. Its kernel is E=L^(1/2)K. Hence there is eta>0, chosen <=1, such that
B>=eta(I-Pi_E).
No compactness of N0 or of C_all is being assumed.

On E, T is an isometry onto W. Also T(E perpendicular) is contained in W perpendicular, since T*T acts as identity on E. The restriction of T to E perpendicular has norm at most sqrt(1-eta), by (3). T* maps W perpendicular into E perpendicular. The adjoint restricted norm gives
\[
\boxed{\eta(I-\Pi_W)\le D_{\rm all}\le I-\Pi_W.}
\tag{4}
\]
The upper bound follows from 0<=D_all<=I and D_all annihilating W. This proves a fixed-window spectral gap away from the finite unit-gain locus on the entire negative coefficient carrier.

Equivalently, for every complete negative coefficient v,
\[
\eta\operatorname{dist}(v,W)^2
\le\|v\|^2-\|C_{\rm all}v\|^2
\le\operatorname{dist}(v,W)^2.
\tag{5}
\]
If K={0}, (4) says ||C_all||<1. If K is nonzero, ||C_all||=1 and gain is attained on the finite W. These alternatives match existing native coercivity/nullity; (4) supplies no independent argument selecting one.

The constants are nonconstructive and fixed-window. No numerical eta, source-tail rate, moving-kernel continuity or global aperture bound is claimed.

## Prescribed finite-coordinate unit gain

Let i_s:M_s->H_- be the actual isometric inclusion of the prescribed finite selection. Its minimal raw-positive compensator is C_s=C_all i_s, with P C_s=-R_s*, R_s=i_s*N0. Equation (5) gives
\[
\eta\operatorname{dist}(i_su,W)^2
\le\|u\|^2-\|C_su\|^2
\le\operatorname{dist}(i_su,W)^2.
\tag{6}
\]
In particular,
\[
\ker(I-C_s^*C_s)
=\{u:i_su\in W\}.
\tag{7}
\]
A nonzero exact raw-positive selected unit-gain packet exists if and only if Ran i_s intersects W nontrivially. Its reconstructed physical h satisfies Ah=0, N0h=-i_su, and has zero unselected background. This is exactly the prior one-vector tail-vanishing condition in intrinsic source coordinates.

If the intersection is zero, finite dimensionality gives a positive minimum angle distance on the selected unit sphere; then ||C_s||<1. This can happen for **every** finite coordinate selection even while W is nonzero and ||C_all||=1. A strict estimate at each finite cutoff does not exclude full-source gain one without a lower bound on the angle deficits uniform over the exhaustion.

The earlier effective-positive C=-G_s^(-1/2)R_s* can still attain gain one on any full-null vector when R_s separates K. Its positive covariance differs from the raw L. Equation (7) is for the raw-positive compensator and must not be transferred to the effective one.

## Historical padding and why the adjoint equation matters

Suppose the prescribed historical positive synthesis is actually P=P0* and its signed row factor is PC_hist=-R_s*. Surjectivity of P follows from coercive L, and
\[
C_{\rm hist}=C_s+Z,\qquad PZ=0.
\tag{8}
\]
Ran C_s lies in Ran P0=(ker P) perpendicular. If the retained equations also give
a=C_hist u=P*k,
then Zu=0. Unit gain C_hist*C_hist u=u now implies ||C_su||=||u||, so (7) puts i_su in W. Moreover C_su=P*k and (2) reconstruct a full-native h. Since P*=P0 is injective, h=k. Thus the retained physical vector is exactly recovered, not projected or silently replaced.

These are conditional consequences of **named actual** carrier, raw-positive synthesis and row custody. They do not identify the historical P with P0*, or show that its rows are these actual prescribed coordinates.

Without the physical-adjoint equation, positive padding can manufacture exact unit gain. For P=(5,0):C^2->C, R=3, take C_hist=(-3/5,4/5). Then PC_hist=-R*, C_hist*C_hist=1 and A=PP*-R*R=16>0 has no kernel. The nonzero padding slot prevents C_hist u=P*k for every nonzero u. This is a rational algebra control, not an actual-zeta packet. It rejects unit gain plus signed factor -> actual nullity when adjoint custody is absent. The existing padding-vanishing argument is reused; its unit-gain-locus consequence is new here.

## Infinite-support limit control

Reuse v_j=(4/5)(3/5)^j, H=C, P0=1, N0h=v h and A=0. C_all=-v* has W=span(v), with D_all=I-Pi_W and eta=1. For any finite coordinate carrier, its intersection with W is zero because v has infinitely many nonzero coordinates.

For the first n coordinates,
\[
\|C_n\|^2=1-(9/25)^n<1,
\qquad \|C_n\|\longrightarrow1.
\tag{9}
\]
The selected unit coefficient proportional to Pi_n v has angle deficit (9/25)^n, and exactly that gain loss. Every finite raw compensator is strict, yet the complete compensator has attained unit gain. This is a complete-source algebra control; no actual divisor support or contact is constructed.

## Minimal remaining theorem and F4 scope

Category: retained attachment. For prescribed raw-positive coordinates, the exact intrinsic gate is i_s u in W=ker D_all, with the named synthesis/row/adjoint identities. The current source-tail theorem gives angles tending to zero, not their exact vanishing. Historical normalization and arithmetic/filtration custody remain separate.

Category: endpoint exclusion. A strict complete-source bound ||C_all||<1 at every actual nonnegative candidate would exclude K and close the existing global dichotomy. The present theorem identifies this with the unresolved native kernel exclusion; it does not derive that bound from arithmetic. Finite selected strict bounds without a uniform angle gap do not suffice.

Same physical k is retained in all reconstructed endpoint equations. No dilation, support enlargement or enlarged mixed cancellation is supplied. The finite source compression remains a fresh source-space object, not a prescribed historical actual divisor packet.

Pinned sources and repeated rational controls: notes/data/RPB108_COMPLETE_SOURCE_UNIT_GAIN_LOCUS_20261006.json. Controls verify complement gaps, selected angle loss, off-locus strictness, exact geometric limit gaps and fake padded unit gain without an adjoint. Analytic Fredholm/spectral arguments are not Lean certified here. No Lean module/build, new axiom audit or CI result. Historical claims and the aperture lane are preserved. F4 and FULL TRANSPORT CLOSED remain open.
