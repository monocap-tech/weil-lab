# RPB108: residual Gram enclosures for the finite native response matrix

Base: research a8a2d86ddc7dfdb0e5f3bb4803ade15b75ae5e73.
Definitions: docs/TERMINOLOGY_RPB108_FINITE_SOURCE_RESIDUAL_ENCLOSURE.md.

## Exact certificate mechanism

At one lawful actual window use H=D_a, actual selected analysis R:H->M, and the coercive effective covariance G=A+R^*R. Write L=RG^{-1}R^*, D=I_M-L. Let Y:M->H be any specified finite trial map, approximating G^{-1}R^*.

Define its Hilbert residual and Hermitian trial response by
\[
E=R^*-GY,\qquad
V=RY+Y^*R^*-Y^*GY.
\tag{1}
\]
Then
\[
L-V=E^*G^{-1}E\ge0.
\tag{2}
\]
If G>=beta I_H with a certified beta>0, the complete residual Gram K=E^*E gives
\[
V\le L\le V+\beta^{-1}K,\qquad
I-V-\beta^{-1}K\le D\le I-V.
\tag{3}
\]
The response error is quadratic in the residual. Cross-column correlations are retained in K; replacing K by its diagonal is generally not an upper bound.

This is a certificate mechanism, not an evaluated actual selected matrix. The selection, trial functions, source values, residual Gram, and coercivity constant must be attached and rigorously enclosed before a sign is certified.

## Proof by completion on the same actual vectors

Put X=G^{-1}R^*. Expand
\[
(X-Y)^*G(X-Y)
=X^*GX-X^*GY-Y^*GX+Y^*GY.
\]
Since GX=R^* and X^*G=R, X^*GX=L; the other terms give exactly L-V. Also X-Y=G^{-1}E, proving (2). A positive inverse satisfies G^{-1}<=beta^{-1}I_H, which proves (3).

For a generic trial map, RY need not be Hermitian and cannot simply be called the finite response approximation. The symmetrized variational expression V in (1) is essential.

If Y is a Galerkin solution in a lawful finite-dimensional trial subspace W of H, then Y^*E=0. Hence RY=Y^*GY is Hermitian and V=RY. The same residual correction remains necessary for all uncomputed carrier directions. A finite Galerkin solve alone is not the inverse.

## Physical residuals can replace the logarithmic dual residual Gram

Suppose each residual functional is represented by a physical interior L2 source: for F:M->L2(-a,a),
\[
\langle g,Eu\rangle_H
=\langle J_a g,Fu\rangle_{L2}
\quad(g\in H).
\tag{4}
\]
Equivalently E=J_a^*F, where J_a is the physical inclusion, not an identity between the physical source and its logarithmic Riesz representative.

There are two lawful sufficient bounds.

1. If G>=beta I_H, then ||J_a||<=1 because w>=1, so E^*E<=F^*F. Equation (3) holds with K replaced by F^*F.

2. More directly, if the actual effective form satisfies
\[
\mathfrak g(h,h)\ge\beta_{\rm phys}\|J_a h\|_2^2
\tag{5}
\]
with certified beta_phys>0, then
\[
E^*G^{-1}E\le\beta_{\rm phys}^{-1}F^*F.
\tag{6}
\]
To prove it, set z=G^{-1}Eu. The actual equation and (4) give
\[
\mathfrak g(z,z)
=\operatorname{Re}\langle J_a z,Fu\rangle
\le\|J_a z\|_2\|Fu\|_2
\le\sqrt{\mathfrak g(z,z)/\beta_{\rm phys}}\|Fu\|_2.
\]
If the energy is nonzero, divide and square; otherwise the claimed bound is immediate. Apply this to every coefficient combination u to obtain (6).

The inverse in this argument already exists by the independently established coercivity of G. A physical L2 lower bound alone is not silently promoted to a bounded inverse on H.

## Explicit residual source from trial functions

For the actual normalized selected source profiles eta_q, let y_q=Y e_q and let q_{y_q} be its full native interior physical action. Whenever that action is genuinely L2, define
\[
F_q(x)=\eta_q(x)-q_{y_q}(x)
       -\sum_{p\in s}n_p(y_q)\eta_p(x),\qquad |x|<a.
\tag{7}
\]
The actual mixed source dictionary gives (4). The native action q_y includes the actual archimedean multiplier, all frozen prime translations including threshold equalities, and both Hermitian pole moments. The last term in (7) is the selected covariance added to form G. Dropping it changes the inverse problem.

Polynomial y_q, extended by zero outside [-a,a], are lawful trial vectors. Their Fourier transforms are O(1/|xi|), so the logarithmic multiplier action is globally L2. The explicit archimedean interior source constructor from the earlier Schur pass extends to every finite a: the polynomial differences cancel the 1/s kernel singularity and the remaining support-edge terms have logarithmic growth, which is L2. Finite translated polynomials and the local pole are also L2. No H1 zero-extension premise is needed; endpoint jumps are allowed.

Thus (7) can be built on a specified polynomial trial map using the existing actual prime/pole/digamma constructor. It does not attach an arbitrary abstract retained vector or require a raw Green preimage.

The needed physical residual Gram is
\[
K_{\rm phys}(p,q)=\int_{-a}^a\overline{F_p(x)}F_q(x)\,dx.
\]
Source enclosures must retain these mixed entries. Existing rigorous treatment of logarithmic endpoints and prime panels can be reused, but no enclosure of these selected-source columns has been performed in this pass.

## A concrete negative native vector without solving the inverse

For every u in M, a direct same-vector identity is
\[
Q_a(Yu,Yu)
=\|u\|^2-\langle u,Vu\rangle-\|RYu-u\|^2.
\tag{8}
\]
Indeed expand the last square and use V from (1), with G=A+R^*R.

Consequently, if a rigorously enclosed I-V has a strictly negative direction u, the specified physical trial vector Yu already has strictly negative full native energy. This witness needs no evaluation of G^{-1}. In fact (8) remains valid without coercivity of G; it only needs the attached actual mixed form and trial values.

This is stronger custody than reporting a negative eigenvalue of an implicit inverse matrix. It supplies an explicit vector in the actual canonical carrier, suitable as input to the existing actual first-contact constructor. No such actual negative direction is obtained here.

For positivity, a certified nonnegative lower matrix I-V-beta^{-1}K establishes D>=0. Together with coercive G and the preceding finite-source reduction, it establishes the full native form nonnegative. A strictly positive lower matrix excludes a full native null vector at that window.

A zero numerical band proves neither nullity nor its absence.

## Arithmetic matrix enclosures

Suppose Hermitian arithmetic approximations V_tilde and K_tilde obey
\[
\|V-V_{\rm tilde}\|\le\delta_V,\qquad
K\le K_{\rm tilde}+\delta_K I,
\]
where K is the chosen certified Hilbert or physical residual Gram and the corresponding certified correction constant is beta^{-1}. Then
\[
I-V_{\rm tilde}-\delta_V I
-\beta^{-1}(K_{\rm tilde}+\delta_K I)
\le D\le I-V_{\rm tilde}+\delta_V I.
\tag{9}
\]
A strict negative direction in the right matrix certifies the explicit native trial witness by (8), while a nonnegative left matrix certifies full native positivity under the stated coercivity premise.

At the already certified aperture 81/100, Q>=mu||h||_2^2 with mu=1/(202*10^29), so every actual finite selection has the same physical lower bound for G. That yields the available physical correction factor 202*10^29. Its size makes residual accuracy demanding; this pass does not replace it by a guessed conditioning floor or claim a numerical aperture advance.

At a hypothetical larger contact, the previous finite-selection argument derives some coercive G, but its constants and selected rows are not numerically known. Assuming a convenient beta would hide exactly the unresolved inverse estimate.

## Exact controls, reproduction, and limits

scripts/certify_finite_source_residual_enclosure.py checks 24 finite real rational comparison cases and four exact Galerkin cases. It verifies the completion identity, both enclosure directions, and the explicit negative-trial identity. It rejects controls which drop residual cross correlations, reverse the correction sign, or omit the inverse coercivity factor. It also checks that a generic RY is not automatically Hermitian.

The script reproduced notes/data/RPB108_FINITE_SOURCE_RESIDUAL_CONTROLS_20261006.json byte for byte, SHA-256 f0a5705bb7a95516ec810aacf31332a08aabd232eb61a2eaf0c1ca3f57cda396. The data pins the script SHA-256 and research base.

These are finite real comparison controls. They do not evaluate an actual zeta coordinate, inverse, residual, or matrix, and do not mechanically certify the universal complex Hilbert-space argument. That analytic proof is given above. No full-source sign or negative witness is promoted from these controls.

Pinned repository inputs:
- LOCAL_FINITE_SOURCE_MATRIX_20261006 and FINITE_SOURCE_LOEWNER_20261006: exact actual response, inertia and physical custody.
- ACTUAL_SCHUR_RESIDUAL_20261005: native polynomial source constructor and physical residual-to-form estimates.
- COUPLED_RESIDUAL_PRECISION_20261005: mixed Gram/source error control and the limits of repeated quadrature.
- Current cursor's certified 81/100 physical and logarithmic margin.

Next actual computation requires an identified finite selection and trial map, rigorous selected source/action/Gram enclosures, and a certified coercivity constant. This pass provides the error and witness mechanism; it does not supply those data.

No historical retained packet attachment, actual negative input, endpoint existence/exclusion, global positivity or RH conclusion. Lean/workflows unchanged; no new CI run. Numerical frontier 81/100. F4 and FULL TRANSPORT CLOSED remain open.
