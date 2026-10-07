# RPB108: parity reduces the null regularity and endpoint targets

Date: 2026-10-06 (America/Los_Angeles). Recovered source: `bdbd90805773ce4341f7ff0bdfae50b50ce3cfd9`.
Definitions: [parity null regularity](../docs/TERMINOLOGY_RPB108_PARITY_NULL_REGULARITY.md).
Global/F4 lane; no aperture computation.

## Conditional actual result

At any hypothetical nonnegative actual null window, the finite full native kernel splits as K=K^+ direct-sum K^- under physical reflection. Put r_p=dim K^p. For each nonzero parity sector,
\[
\boxed{K^p\cap H^{N_p}(\mathbb R)=\{0\},
\qquad N_p=\min(2r_p,2r_{-p}+1).}
\tag{1}
\]
This can be substantially stronger than the recovered whole-kernel H^r ceiling. If a parity sector has no opposite-parity null vectors, it has no nonzero H1 null vector, irrespective of its own dimension. If r_p=1, it has no nonzero H2 null vector, irrespective of the opposite dimension.

The parity-resolved H1 space has
\[
d_p=\dim(K^p\cap H^1)\le\min(r_p,r_{-p}).
\tag{2}
\]
Thus when r_p>r_{-p}, at least r_p-r_{-p} modes in that sector are rough. Its own normalized gain trace must diverge; the sufficient arithmetic trace target need only cover that dominant sector. Neither the parity dimensions nor a bound on that trace is established at an actual contact here.

These are analytic consequences of the existing actual reflection, supported-L2 promotion and finite reconstruction theorems. They do not attach a prescribed historical packet or exclude an actual contact.

## Reflection custody and derivative domain

The actual logarithmic norm and full mixed form are reflection-invariant: the multiplier is even, prime shifts come in opposite pairs, and reflection interchanges the two pole moments. In the pole expression p_h(x)=M_-(h)e^{x/2}+M_+(h)e^{-x/2}, one has M_\pm(Jh)=M_\mp(h), hence p_{Jh}=Jp_h. Consequently J preserves the full actual kernel, and its two eigenspaces give the decomposition above.

The recovered automatic derivative promotion says h in K intersect H1 implies its global L2 derivative lies in K and in the canonical logarithmic domain. Differentiation anticommutes with reflection:
\[
J\partial_x=-\partial_xJ.
\]
It therefore injects K_j^p into K_{j-1}^{-p} for j>=1. Injectivity follows because a global compactly supported L2 function with zero derivative is zero. This does not define differentiation on non-H1 null vectors.

The pole integration by parts and endpoint traces are used only after global H1 has been established, as in the promotion theorem. An interior derivative, or dilation to a larger support, cannot replace this global derivative.

## Single-vector ceiling and refined flags

For nonzero h in K^p intersect H^j, automatic promotion puts all derivatives through order j in K. Their independence follows from the existing Fourier-polynomial argument. The even-order derivatives stay in K^p and the odd-order derivatives lie in K^{-p}. Thus
\[
\lfloor j/2\rfloor+1\le r_p,\qquad
\lceil j/2\rceil\le r_{-p}.
\tag{3}
\]
At j=2r_p the first inequality fails; at j=2r_{-p}+1 the second fails. This proves (1). For a mixed-parity vector the separate components are also H^j, but the original total-kernel ceiling remains available; no definite parity is attributed to a historical witness without proof.

There are useful dimension bounds throughout the flag. For m>=1,
\[
\dim K_{2m}^p\le
\max\big(0,\min(r_p-m,r_{-p}-m+1)\big),
\tag{4}
\]
and for m>=0,
\[
\dim K_{2m+1}^p\le
\max\big(0,\min(r_p-m,r_{-p}-m)\big).
\tag{5}
\]
The recovered total bound dim K_j<=max(r_++r_--j,0) holds as well; summing (4)-(5) does not replace that possibly stronger total bound.

To prove (4)-(5), first note that whenever K_j^p is nonzero and j>=2 its dimension is strictly smaller than dim K_{j-2}^p. Otherwise the nested finite spaces would coincide, making the second derivative an endomorphism of their common space. Iterating would give arbitrarily many independent even-order derivatives of a nonzero vector in that finite space, contradicted by Fourier-polynomial independence. The even flag therefore loses at least one dimension per two steps, starting at r_p. For the odd flag the initial dimension is at most min(r_p,r_{-p}), because the first derivative injects into the opposite sector; strict two-step descent then gives (5). Applying the first derivative to K_{2m}^p and using (5) in the opposite sector also gives the second ceiling r_{-p}-m+1 in (4).

All these statements concern full actual native nullity. Coercive G has zero kernel and supplies no parity null space of its own.

## Finite selected response: avoid an unproved parity block

Let E=ker D(c) and B_c=-G_c^{-1}R_c*:E to K be the actual reconstruction isomorphism. Define E^p=B_c^{-1}K^p. The induced reflection B_c^{-1}JB_c is an involution on E, but need not be unitary in the finite Euclidean norm. A generic separating selection need not make E^+ and E^- orthogonal or make the entire finite response commute with this involution.

Use instead the Euclidean compression of the positive normalized gain Gamma_s to the fixed subspace E^p. The spectral-split proof already established for E applies verbatim within any fixed finite subspace: its regular subspace is B_c^{-1}(K^p intersect H1), dimension d_p. Compactness of the sphere in its fixed orthogonal complement and the truncated weighted Fourier derivative forms give uniform rough divergence there. The regular compression tends to zero, and min-max yields
\[
\lambda_i^p(s)\to0\ (i\le d_p),\qquad
\lambda_i^p(s)\to\infty\ (d_p<i\le r_p).
\tag{6}
\]
The eigenvalues in (6) are those of the compression, not a claimed block diagonalization of Gamma_s.

If r_p>r_{-p}, (2) ensures at least r_p-r_{-p} diverging eigenvalues. Hence
\[
\operatorname{trace}_{E^p}\Gamma_s\longrightarrow\infty.
\tag{7}
\]
A finite liminf of this trace, proved from the actual arithmetic at a hypothetical contact with unequal parity dimensions, would already contradict (7). It is weaker than the full trace target. For a balanced split this argument does not force either individual parity trace to diverge: the total strict flag guarantees at least one rough mode somewhere, but does not choose its parity. A global exclusion theorem would still need a bound in both balanced sectors or another argument for those contacts.

For a fixed nonzero pure-parity h, a bounded gain/s^2 or full collar-mass/(s^2 log(1/s)) ratio along a sequence promotes h to H1. Its derivative has opposite parity, so this criterion immediately excludes such a vector if K^{-p}=0. For higher regularity, (1) gives the exact sufficient single-vector derivative order. The existence of a full-null witness, its parity, its regularity, and any opposite-sector exclusion are independent premises.

## Control: one H1 direction does not exclude a balanced kernel

On [-1,1], let h(x)=(1-|x|)_+. It is even, globally H1, and compactly supported. Its derivative is the odd step profile equal to 1 on (-1,0) and -1 on (0,1), and is globally L2 but not H1. Both profiles belong to the logarithmic domain. V=span{h,h'} has r_+=r_-=1, with differentiation mapping V intersect H1 into V. Yet V intersect H1 is the nonzero even line. Thus one regular null-like direction plus reflection and partial derivative invariance does not imply a finite-dimensional contradiction. V is not an actual native kernel.

More generally, center the r-fold convolution of 1_[0,1] at zero. Its q-th derivative has parity (-1)^q, for 0<=q<r. These independent logarithmic profiles span V_r, and the globally H^j members are precisely combinations with q+j<r. An antisymmetric difference of two disjoint reflected translates supplies the analogous chain starting in odd parity. Counting each parity verifies (4)-(5) and the sector ceilings. The bounds are attained sectorwise by these controls; simultaneous equality in both sector bounds is not asserted, and the strict total flag still applies. These are sharpness controls for the structural implication, not prescribed arithmetic source solutions.

For the two-mode balanced control a positive normalized gain diag(s,1/s), with the first coordinate even, has a vanishing even trace and diverging total trace. Interchanging parity labels puts the regular line in the odd sector. This rejects inferring divergence of a specified sector from the total split alone. Such gain rates are not asserted to be actual responses.

## Remaining theorem and transport boundary

The rejected implication is: one globally H1 full-null vector -> no contact. It remains false structurally in a balanced two-sector space. The new sufficient alternatives are explicit:

1. For a given attached pure-parity witness, exclude the opposite-parity kernel and prove a sequencewise quadratic gain/collar bound for that witness; or establish its global H^{N_p} membership with lawful parity dimensions.
2. At every unequal-parity contact, prove finite liminf of the dominant parity compressed gain trace. Supply the original full trace bound or a separate exclusion for balanced contacts.

These remaining arithmetic or attachment premises are unproved. The obstruction and reduced targets belong to endpoint exclusion. Retained historical P,C,k identity remains separate. The physical h and its zero extension are unchanged during finite reconstruction; differentiation produces a different physical vector, and neither it nor dilation supplies same-vector enlarged null transport. On a larger support the original h remains diagonally neutral but has the already established nonzero full mixed residual. No selected-background cancellation is promoted to enlarged central or full-native cancellation.

## Custody and validation

Pinned sources and repeated controls are in notes/data/RPB108_PARITY_NULL_REGULARITY_20261006.json. Controls count derivative/parity flags and ceilings in centered spline chains and check positive diagonal gain rates; they do not prove an actual arithmetic endpoint estimate. The functional proof above is analytic, not Lean certified. No Lean/lake executable is available in this workspace; no Lean, compiler, workflow or axiom certificate is claimed or changed.

Recovered whole-domain positivity through 93/100 is preserved. Historical notes and certificates are unchanged. F4 and FULL TRANSPORT CLOSED remain open.
