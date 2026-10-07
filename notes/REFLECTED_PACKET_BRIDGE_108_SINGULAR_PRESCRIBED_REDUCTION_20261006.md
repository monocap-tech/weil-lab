# RPB108: prescribed separation is unnecessary for reduced neutral morphology

Date: 2026-10-06 (America/Los_Angeles). Live source 0eecdec00fb819d24466c26f4957fb6a2df90b50.
Definitions: [singular prescribed covariance registry](../docs/TERMINOLOGY_RPB108_SINGULAR_PRESCRIBED_REDUCTION.md).
Analytic conditional actual compatibility result; not a concrete historical instance or Lean certification.

## A stronger compatibility implication

The earlier PRESCRIBED_REDUCTION used a separating prescribed selection to make G=A+R*R coercive and construct an invertible physical root synthesis. That separation remains necessary for the stated full-space inverse. It is **not necessary** for:

- deriving actual full-nullity of the retained same physical vector from the attached equations; or
- replacing its positive coefficient carrier by a canonical unitary quotient while preserving the neutral morphology and the same physical k.

The independent named attachment gates for this narrower construction are:
1. actual physical/logarithmic carrier and extension custody;
2. the prescribed actual finite rows R and their metric/normalization;
3. the same-domain identities PP*=A+R*R and PC=-R*.

The retained unit-gain, physical-adjoint, attained-neutral, filtration and arithmetic/stop fields remain their original input data. None of the three named actual gates is proved here. This result removes whole-kernel separation from the conditional quotient/morphology compatibility implication, not from the fresh coercive inverse architecture.

## Positive Fredholm range and the quotient unitary

At a nonnegative actual window, A=I+compact and R is finite rank. Thus G>=0 is positive Fredholm. Define
\[
N=\ker G=\ker A\cap\ker R,\qquad H_{\rm vis}=N^\perp,\qquad i:H_{\rm vis}\hookrightarrow H.
\]
The kernel equality follows by summing the two nonnegative energies. G_vis=i*G i is coercive: positive Fredholm spectrum has a gap away from zero on its kernel complement. Write F_vis=G_vis^(1/2) and G^+=i G_vis^(-1)i*, the bounded inverse on H_vis and zero on N.

PP*=G implies P*n=0 for n in N. Conversely each h in H_vis has
\[
h=P(P^*G^+h).
\]
Hence Ran P=H_vis is closed. For L=(ker P) perpendicular,
\[
\Pi_L=P^*G^+P,\qquad
U_{\rm all}=F_{\rm vis}^{-1}i^*P,\qquad
U_{\rm all}U_{\rm all}^*=I_{H_{\rm vis}},\quad
U_{\rm all}^*U_{\rm all}=\Pi_L.
\tag{1}
\]
Thus U=U_all restricted to L is a unitary L->H_vis, with inverse P*i F_vis^(-1).

R annihilates N, so Ran R* lies in H_vis. Define
\[
P_{\rm red}=iF_{\rm vis}:H_{\rm vis}\to H,\qquad
C_{\rm red}=-F_{\rm vis}^{-1}i^*R^*.
\tag{2}
\]
The full physical carrier is still H. In particular,
\[
P_{\rm red}U_{\rm all}=P,\quad
P_{\rm red}P_{\rm red}^*=G,\quad
P_{\rm red}C_{\rm red}=-R^*,\quad
P_{\rm red}P_{\rm red}^*-R^*R=A.
\tag{3}
\]
This synthesis is injective on its positive coefficient carrier H_vis but is not onto the full physical H when N is nonzero. Calling it the previously constructed invertible full-space S would be incorrect. The compensator is nevertheless derived contractive: R*R<=G implies C_red C_red*<=I on H_vis after sandwiching by F_vis^(-1), so ||C_red||<=1. Thus the unit-budget property survives the singular reduction; full physical invertibility does not.

Every attached historical compensator decomposes
\[
C=U^*C_{\rm red}+Z,\qquad Z=(I-\Pi_L)C,\qquad PZ=0.
\tag{4}
\]

## Retained same-vector nullity never needed G inverse

Let the original retained equations be
\[
a=Cu=P^*k,\qquad C^*Cu=u.
\tag{5}
\]
Because P*k lies in L, Zu=0. The signed factor identity gives
\[
Rk=-C^*P^*k=-u,\qquad
Gk=PCu=-R^*u.
\]
Therefore
\[
\boxed{Ak=Gk-R^*Rk=0.}
\tag{6}
\]
No inverse or separating selection is used in this calculation. It is actual **full native** nullity once the named covariance and row identities are actually attached.

Define a_red=Ua. Equations (1)-(5) give
\[
a_{\rm red}=C_{\rm red}u=P_{\rm red}^*k,\qquad
C_{\rm red}^*C_{\rm red}u=u.
\tag{7}
\]
Indeed U_all C=C_red, and C*C=C_red*C_red+Z*Z with Zu=0. The norms of a,u and their signature are preserved. Equations (3), (6)-(7) supply the same actual physical-null operator and physical-adjoint relation on the unchanged k.

The abstract NeutralDefectMorphology accepts P from its positive coefficient Hilbert carrier into an independent physical Hilbert H. It imposes no surjectivity or full-space invertibility of P. Thus the singular synthesis species in (2) matches its declared fields. This is a written morphology construction, not a compiled Lean instance.

## Physical kernel padding is retained, not silently projected away

The inverse equation determines only
\[
k_{\rm vis}:=ii^*k=-G^+R^*u,\qquad
k=k_{\rm vis}+n,\quad n\in N.
\tag{8}
\]
The retained positive/selected coefficients cannot see n:
P*n=0 and Rn=0. Complete actual background samples can still see it. Nothing in (5) proves n=0.

The attained branch has u!=0, so (8) has k_vis!=0. Both k_vis and n are full-native null by (6) and N subset ker A. But replacing k by k_vis changes the physical vector unless n=0. It also changes its physical Fourier density, complete samples and extension whenever n is nonzero.

The smallest extra theorem for the **same-vector inverse reconstruction** k=-G^+R*u is therefore
\[
\boxed{\Pi_N k=0.}
\tag{9}
\]
Whole-kernel separation N={0} is a stronger sufficient condition. Equation (9) is not required for the reduced morphology that retains the original k through (7). No physical projection is performed in that construction.

Adding actual selected rows would repair the whole-space inverse, but the existing augmentation theorem changes the selected coefficient by the added samples. It is not identity with the prescribed packet and is not used here.

## Retained right-limit geometry and stop fields

As in the earlier quotient proof, intersect the historical filtration B(t) with L plus M, then apply W=U plus identity_M. This is a unitary onto H_vis plus M. Closedness, monotonicity and the exact rightLimit intersection identity follow unchanged. The retained endpoint (a,u) is already reduced, so its image (a_red,u) belongs to the reduced right limit.

The original attained-neutral norms are preserved. A constant right-approach sequence at (a_red,u), with the same increasing index subsequence construction already proved, supplies the reduced NeutralCriticalBranch fields. Keep the original physical H, k, extend k, arithmetic/stop record and null-extension interface unchanged.

This preserves the morphology without changing its physical vector. It does not identify the historical filtration with physical support, attach named arithmetic fields to actual Fourier data, or prove the unresolved persistenceGoal. Any missing named custody remains independent.

## Exact controls and reduced F4 gates

The rational control uses
\[
A=\operatorname{diag}(0,t^2,0),\quad
R=\begin{pmatrix}r&0&0\\0&0&0\end{pmatrix},\quad
G=\operatorname{diag}(r^2,t^2,0).
\]
The full kernel contains e1 and e3, and the prescribed R misses e3. A rank-two padded synthesis and compensator obey both named factor identities. The retained k=(1,0,v) and u=(-r,0) obey unit gain and physical adjoint. Their reduced morphology retains k exactly; pseudoinverse reconstruction gives (1,0,0), different when v!=0. Invisible positive coefficient padding may also be present globally, but vanishes on this attained coefficient.

These are algebra controls, not actual divisor rows or hypothetical actual contact constructions. They reject the implication retained equations -> no invisible physical component, while verifying that absence of whole-kernel separation does not obstruct the singular quotient morphology.

| Target | Separation requirement |
| --- | --- |
| Actual full-nullity of retained k from named covariance/row identities | None |
| Canonical positive quotient and reduced neutral morphology retaining k | None; use H_vis and singular synthesis |
| Same-vector pseudoinverse reconstruction | Exactly Pi_N k=0 |
| Invertible synthesis onto all physical H | Exactly N={0}, the prescribed kernel-separation gate |
| Enlarged same-vector native cancellation | Still an independent, obstructed equation |

Remaining category: **retained attachment**. The new closure is a compatibility implication with fewer gates; the named actual carrier/row/covariance attachment itself remains unproved. Actual zero-eigenvalue endpoint exclusion, enlarged transport and F4 stay open.

## Source custody and validation

Pinned live source blobs and repeated exact controls: notes/data/RPB108_SINGULAR_PRESCRIBED_REDUCTION_20261006.json. The actual Fredholm/stabilization architecture, existing coercive quotient/intersection proof, one-vector attachment distinction and selection augmentation are reused.

243 singular covariance cases pass and repeat; 162 cases explicitly reject replacing the physical k by its projected inverse reconstruction. No Lean compiler/build, new axiom audit or CI result is claimed. Historical files and certificates remain unchanged. Complete 19/20 Gram/scalar-obstruction custody and certified 47/50 positivity are preserved. F4 and FULL TRANSPORT CLOSED remain open.
