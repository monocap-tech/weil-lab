# MG21 — Positive source moments are analytically SPD; return to the original signed residual

October 19–20, 2026. This is a **methodological acceptance correction**, not a claim of Riemann-hypothesis progress. It follows the exact MG20 original nonflat frequency-source rank result, which PASSED dedicated Actions 39366482406. On 24 certified genuinely nonflat original pilot cells, MG20's rational source midpoint frame alone is FULL RANK 24, its rational derivative frame alone is FULL RANK 24, and its 48-vector affine frame is FULL RANK 24. Both ideal first and second positive multiplier-weighted affine source references are rigorously SPD (24+,0−,0). These IDEAL references omit the true physical Fourier uncertainty. The MG18 actual certified LOWER references still have inertia (3+,21−,0).

## A useful theorem that changes what we should optimize

**Lemma (strict positivity of a compactly supported finite-source positive-frequency moment).**

Let B>0. Let f_1,...,f_n be linearly independent L²(R) functions supported in [-B,B] (a.e.). Let I⊂R be any bounded interval with nonempty interior. Let w:I→(0,∞) be measurable, locally bounded above, and bounded below by a positive kappa almost everywhere in I. For any exponent p>0 such that the weighted Fourier integrals exist, define the Hermitian matrix

  M_{I,p}[i,j] = ∫_I w(xi)^p F(f_i)(xi) overline{F(f_j)(xi)} dxi.

Then M_{I,p} is **strictly positive definite**.

**Proof.** For any coefficient vector z, let f_z=∑ z_j f_j. Since f_z has bounded support and belongs to L², it also belongs to L¹. Its Fourier–Laplace transform F(f_z)(zeta)=∫[-B,B] f_z(x) exp(-2π i x zeta)dx is entire in complex zeta, by dominated differentiation on compact sets. Moreover

  z* M_{I,p} z = ∫_I w(xi)^p |F(f_z)(xi)|² dxi ≥0.

If this equals 0, w>0 almost everywhere gives F(f_z)=0 a.e. on I. Continuity upgrades the vanishing to every xi in I. By the identity theorem for holomorphic functions, F(f_z) vanishes identically on C. Uniqueness of the Fourier transform on L¹ (or L² Plancherel) implies f_z=0 a.e. Linear independence of the f_j forces z=0. QED.

**Application to original SI10/MG11–MG20 pilot.** The full 25 physical supported odd pilot generators have a certified strictly positive Gram (SM42). The MG11 transform h_i=f_i−a_i s−c_i f_q with 23 free coordinates plus the genuine odd sinh pole s is algebraically injective on coefficients (the 23 free rows and pole row form an identity subblock). Thus these **24 original actual physical functions** are independent in L², regardless of the rational-point approximations used in MG20. Every MG17 nonflat interval has a_o>kappa>0 across the whole cell, and the positive multiplier also stays ≥kappa on arbitrary intervals under the inherited original Fourier definitions. Therefore for p=1 and p=2, the TRUE full original selected-frequency *positive* source-moment matrices are strictly positive definite. **This is analytic, not a computer-derived quantitative matrix margin**.

The conclusion does NOT depend on affine Fourier approximations or the particular 24 chosen pilot cells. It applies to **any fixed interval of nonempty width**, no matter how narrow, with source-independent w>0. It does **not** say the finite moment has a useful numerical eigenvalue: on a poor interval its minimum generalized eigenvalue can be unimaginably small. Indeed a positive lower-reference matrix can remain extremely indefinite from interval overpayment while the true finite positive source moment is strictly PD.

## What this proves and what it does NOT prove

Because the fixed finite physical Gram H is SPD, this theorem gives for each fixed I and p an **existential but not explicit** positive constant

  gamma_{I,p} = min_{z ≠0} (z* M_{I,p} z)/(z* H z) > 0.

This assertion comes from finite-dimensional compactness. It supplies **NO constructive lower bound**, cannot be substituted for SM32's quantitative outer complement estimate, and cannot pay any negative signed source penalty or prove a 51/56 full 470-source relative-resolvent margin. The positive Fourier source moment is not the original signed Weil operator. In particular it gives no bound on the coupled action with K_-, no classification of the original even sector, no original source470 inverse, and no RH result. Independent identification of the full original Fourier form, its closure, and its operator domain remains open.

**MG21 method acceptance:** Do NOT keep attempting to prove mere qualitative positive definiteness of the true first/second positive-multiplier source moment by eliminating the 21 negative pivots of loose LOWER reference matrices. Actual strict positivity is already a mathematical consequence of compact support and independence. The real obligation is to compute a **quantitative** certified lower bound in the true physical metric, with a simultaneous sufficiently sharp strong-action and pole-corrected Galerkin residual upper, and compose it with the full signed negative term and infinite complement. Finite narrow-window trace/inertia contests alone are no longer an acceptable objective.

## Complete original pole correction to be paid next

Let A_o be the original positive Fourier multiplier operator on the appropriate common domain, s the supported odd sinh pole (normalization as in SM41), P=|s><s| and A_*=A_o−2P. Let F:C^n→L² be a matrix of original physical source functions INCLUDING s as one of its columns, and write

  H=F*F;  G_o=F*A_o F;  S_o=F*A_o² F,
  b=F*s;  c=F*A_o s;  sigma=<s,s>.

Then the true complete source action of A_* and A_*² must satisfy the EXACT operator algebra identities

  **G_*=G_o−2bb***,

  **S_*=S_o−2(cb*+bc*)+4 sigma bb***.

The second formula is for the **strong source action** S_*[i,j]=<A_* f_i,A_* f_j>. It needs the complete original Fourier-frequency G_o, S_o, not merely selected-cell pieces; the rank-one pole correction is nonlocal in Fourier frequency. In the source basis with a genuine s channel, b is the pole column of H and c is the pole column of G_o, so the pole responses can be recovered without inventing new physical couplings.

For a target original source map J and candidate full-domain trial response Y, the actual Galerkin residual is R=J−A_*Y and

  **R*R = J*J − J*A_*Y − Y*A_*J + Y*A_*²Y**.

No componentwise sign estimate or selected-cell surrogate may be promoted to a complete residual. The original full470 negative cap and inverse gate requires this complete operator and a quantified margin over the negative term.

## Falsifiable immediate continuation

1. Validate the original supported source independence and Fourier transform analytic assumptions separately from the inherited full Weil-form domain closure.
2. Build a **complete original source band partition** covering [0,Lambda] with explicit low-band integration and MG11's full logarithmic tail. Treat unselected frequencies as an OPEN/paid positive action, not implicitly zero.
3. Construct full **G_o** and **S_o** compatible with the *same source basis*, with rational matrix error budgets and exact source pole column.
4. Apply the complete original pole formulas above; compute a rigorous R*R upper as a Loewner bound, and test the actual relevant MG07 470-source 51/56 gate with SI29 positive preconditioning.
5. Stop if the certified residual margin is still far too large; report no-go and redesign the approximation geometrically. Do not hide it through more cell-count checkpoints.

The accompanied MG21 deterministic Fraction-only validator checks the two complete pole-source matrix identities and residual identity on a nontrivial original-style rational finite-dimensional toy operator. It is **only an algebraic regression**, not a machine proof of Fourier analytic unique continuation or original operator positivity.

All signed odd/even, Weil/CC27 and RH acceptance gates remain OPEN.
