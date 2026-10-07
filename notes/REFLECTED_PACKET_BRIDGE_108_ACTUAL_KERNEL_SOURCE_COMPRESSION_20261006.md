# RPB108: exact raw-positive packet from the actual kernel source image

Date: 2026-10-06 (America/Los_Angeles). Live source 4dd48a72b817ce28dd9e9a12448bb1aa93cbfea5.
Definitions: [kernel source compression registry](../docs/TERMINOLOGY_RPB108_ACTUAL_KERNEL_SOURCE_COMPRESSION.md).
Global/F4 lane. Conditional on a hypothetical actual nonnegative null window; no contact existence claim.

## What the source tails can and cannot do

Fix the actual canonical logarithmic carrier H, complete normalized analyses P0,N0, nonnegative A=P0*P0-N0*N0 and finite full kernel K. Existing positive carrier equivalence makes L=P0*P0 coercive. Complete source injection makes N0 injective on K.

For any finite-coordinate exhaustion Pi_n,
\[
\varepsilon_n:=\|(I-\Pi_n)N_0|_K\|\longrightarrow0.
\tag{1}
\]
Choose an H-orthonormal basis e_1,...,e_r of K. Cauchy-Schwarz gives epsilon_n^2<=sum_j ||(I-Pi_n)N0 e_j||^2, and each tail tends to zero in the complete actual l2 carrier. This proves uniformity on the finite kernel without derivative regularity, a new aperture certificate or an effective tail rate. It does not prove operator-norm tail decay on the whole H.

On K the coordinate-selected raw-positive defect is precisely its tail Gram:
\[
Q_{\rm raw,n}(k)=\|P_0k\|^2-\|\Pi_nN_0k\|^2
=\|(I-\Pi_n)N_0k\|^2.
\tag{2}
\]
Thus ||Q_raw,n|K||<=epsilon_n^2, but exact raw selected neutrality at a finite stage still requires the tail to vanish. Arbitrarily small positive tails do not force zero.

Since N0|K is bounded below on this finite-dimensional space, (1) also proves sufficiently large coordinate selections separate K. That existence theorem was already closed; (1)-(2) add metric/tail control, not a new separating-packet identity.

The published ENERGY_TAIL_TEST bounds Green interpolation tails by derivative energy. It cannot be applied to the hypothetical full K by assuming H1: the derivative-chain ceiling explicitly supplies a rough mode when K is nonzero. Here (1) uses the already extended complete bounded analyses on H. It obtains no rate competing with a varying Green interpolation inverse Gram.

## Exact finite-rank compression

Define W=N0(K), Pi_W the orthogonal projection in the **complete actual negative coefficient metric**, R_W=Pi_W N0:H->W, and B_W=(I-Pi_W)N0. W is finite-dimensional of dimension dim K, and
\[
B_W|_K=0,\qquad R_W|_K=N_0|_K.
\tag{3}
\]
This is an exact observation construction using the actual source image. It need not be a finite actual-coordinate selection: a basis of W can contain vectors with infinitely many nonzero divisor coordinates. Source multiplicities and normalizations stay inside the inherited metric.

At the nonnegative window the raw-positive compressed defect obeys
\[
\Delta_W=L-R_W^*R_W=A+B_W^*B_W\ge0,
\qquad \ker\Delta_W=K.
\tag{4}
\]
For the kernel equality, a zero diagonal in the sum of nonnegative forms forces Ak=0 and B_W k=0; conversely (3) kills both on K. Its operator need not equal A on all H. Effective G_W=A+R_W*R_W is also coercive by existing finite-rank stabilization, but is not L unless B_W=0 everywhere.

Keep the **complete raw positive synthesis**
\[
P=P_0^*:\mathcal H_+\to H,\qquad
C_W=-P_0L^{-1}R_W^*:W\to\mathcal H_+.
\tag{5}
\]
Then PP*=L and PC_W=-R_W*. The isometry U=P0 L^(-1/2) satisfies U*U=I_H, and
C_W=-U L^(-1/2)R_W*.
From R_W*R_W<=L in (4), the latter factor is contractive. Hence C_W is contractive. This is an actual raw-positive compensator, with bounded inverse L supplied by the existing positive carrier equivalence.

For every unchanged k in K set
\[
u=-R_Wk,\qquad a=P_0k.
\]
Because Lk=N0*N0k=R_W*R_Wk, equations (5) give
\[
C_Wu=P_0k=P^*k,\qquad
C_W^*C_Wu=-R_Wk=u,\qquad
\Delta_W k=0,\qquad Ak=0.
\tag{6}
\]
Thus a fresh exact finite-dimensional raw-positive unit-gain/physical-adjoint packet exists on the whole actual full kernel, with no omitted background on that kernel. This is stronger than merely an effective-positive packet on K. The actual full-null equation in (6) is separately retained; it is not inferred by equating Delta_W and A on all H.

This construction discharges raw-positive compatibility for a newly declared orthogonal source compression. It does **not** discharge actual prescribed finite-coordinate attachment or construct a contact kernel unconditionally.

## Exact finite-coordinate compatibility and normalization

For a prescribed coordinate projection Pi_s, raw selected neutrality of k in K is exactly
\[
N_0k\in\operatorname{Ran}\Pi_s.
\tag{7}
\]
For the whole kernel, exact coordinate compatibility is W subset Ran Pi_s. Every W vector is then finitely supported within that prescribed set. Finite dimension alone does not imply this condition.

A coordinate-selected effective packet on the same k has total coefficient norm squared 2||Pi_s N0 k||^2. The raw-positive compressed packet in (6) has total norm squared 2||N0 k||^2, differing by
\[
2\|(I-\Pi_s)N_0k\|^2.
\tag{8}
\]
So replacing the former by the latter changes a prescribed normalized packet unless (7) holds. Renormalizing scales physical k; carrier isometries cannot conceal this norm change. The positive analysis and physical vector in (6) are actual and unchanged, but the negative coefficient carrier has become W.

An H-unit k may be freshly scaled to give neutral total norm one in this construction. That is legal for a newly chosen null witness, not transport of an unchanged prescribed normalized k. Historical filtration, right-limit membership, arithmetic density and stop fields remain separate; the generic algebraic fields alone do not attach them.

## Infinite-support control with exact geometric tails

Take H=C, A=0, P0 h=h, and complete negative analysis N0 h=v h, where
v_j=(4/5)(3/5)^j for j>=0. Then ||v||=1 and the full source identity holds. K=H and W=span(v) has dimension one but infinite coordinate support.

For the first n coordinates the exact tail norm squared is (9/25)^n, strictly positive for every finite n. Coordinate selections separate K as soon as n>=1, and their effective packets are exactly neutral. Their raw selected defect is still (9/25)^n |h|^2, never zero. Uniform tails tend to zero, but no finite coordinate-selected raw packet is neutral on a nonzero h.

Compression onto W is exact at rank one: in the unit basis v it has R_W=1, P=1, C_W=-1. It obeys all equations (6). This demonstrates the distinction between exact finite-rank source compression and exact finite-coordinate selection. It is an algebraic complete-source control, not actual divisor data or an actual-zeta kernel.

Further finite-dimensional rational controls verify (4)-(6) and explicitly distinguish Delta_W from A off K. They certify algebra only.

## Remaining F4 obligations

| Route | Closed here | Still required |
| --- | --- | --- |
| Finite coordinate approximation on K | Uniform tails and approximate raw neutrality | Exact prescribed tail vanishing for raw attachment |
| Fresh kernel-compressed raw packet | Actual inherited source metric, finite negative dimension, unit gain, adjoint, full-null k | Lawful historical replacement dictionary and retained fields |
| Prescribed finite-coordinate raw packet | Exact compatibility reduced to (7) on k | Prove it for the named retained packet |
| Global endpoint | No change | Exclude the hypothetical nonnegative zero kernel |
| Enlarged null transport | No change | Same-vector enlarged equation; existing rigidity obstructs nonzero full-null persistence |

Category: retained attachment. The construction removes an intrinsic finite-dimensional raw-positive obstruction if arbitrary orthogonal source compression is allowed. Historical selected-coordinate morphology is not silently broadened. Neither a small tail nor W's finite dimension identifies it with a prescribed finite actual divisor packet.

Source custody and repeated controls: notes/data/RPB108_ACTUAL_KERNEL_SOURCE_COMPRESSION_20261006.json. The earlier source normalization, positive carrier equivalence, raw/background distinction and derivative-tail limitations retain their exact scopes and external dependencies. No new external theorem, Lean source/build, axiom audit or CI claim. Certified positivity through 19/20 is preserved. F4 and FULL TRANSPORT CLOSED remain open.
