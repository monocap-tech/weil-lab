# CC61: identical complete finite sources do not determine the missing Schur sign

Read [definitions](../docs/TERMINOLOGY_RPB108_SAME_SOURCE_COMPLETION_CC61.md) first. This exact abstract control specifies the limitation of the current finite-source/high-floor REDUCTION. It does not change the fixed Weil arithmetic or prove nonimplication from its complete identities. Native NF22 remains the staged source producer; CC61 computes no new native residual.

## Result

Three selfadjoint finite operators have IDENTICAL physical source vectors on the observed retained-plus-two-high carrier, identical complete finite source-square Gram, identical native observed form block, identical compensated sources and their P,H,Z correlation Grams, and the SAME exact high floor207/1000. Their full Schur signs nevertheless cross from negative through null to positive.

The observed source map has an identical strict lower frame >=9 I throughout. The compensated retained physical source Gram is I3 throughout. Thus even an evaluated complete finite source Gram and a positive finite source frame cannot, by themselves, exclude a complete null or certify positivity on correlation-blind directions. The missing datum is high inverse action on the unmeasured source. This is a partial-data insufficiency theorem, not an original Weil counterexample.

## Complete exact construction

Let retained E have dimension3, measured H have dimension2, and unmeasured U have dimension3, all physical orthonormal. Set

    kappa=207/1000,  A=4 I3,  B=0,  C2=3 I2,
    K=[[3,0],[0,3],[0,0]],  sigma=I3,
    D_U(d)=diag(kappa+9/(3-kappa), kappa+9/(3-kappa), d).

The full high block is C(d)=[C2,K*;K,D_U(d)], and the mixed retained-high block is [0,I3]. The complete original MODEL operator Q(d) is the corresponding eight-dimensional symmetric block matrix. For every d>=kappa, C(d)>=kappa I. Its first coupled pair has the actual eigenvector (3,-(3-kappa)) at eigenvalue kappa, so the high floor is EXACTLY the same kappa for every completion, not merely a shared loose lower bound.

Only d varies. It occurs solely in an unobserved high column. The entire source matrix L|_(E+H), consisting of the first five physical columns of Q(d), is independent of d. Its observed native form is diag(4 I3,3 I2), strictly positive. Its complete physical source-square Gram is

    D_source=[[17 I3,K],[K*,18 I2]],

which is >=9 I5 by exact positive-semidefinite testing. This is not a sector Gram: ALL physical coordinates of all five source columns are fixed. In particular P=I3, H=9 I2, Z=K* and every finite retained/measured covariance stays fixed.

Eliminating the two measured modes gives

    D_eff=diag(q,q,d),
    q=kappa[1+9/(3(3-kappa))],
    full Schur=diag(4-1/q,4-1/q,4-1/d).

The first two diagonal entries are strictly positive. The third gives the exact crossing:

| Completion d | Complete third Schur entry | Complete sign |
|---|---|---|
| 207/1000 | 4-1000/207 <0 | Negative direction |
| 1/4 | 0 | Actual null |
| 1 | 3 | Strictly positive |

At d=1/4, the actual complete null vector is retained e3 minus4 times unmeasured e3. It is not an observed-carrier polynomial or merely a source truncation. At d=kappa the corresponding optimized vector has negative original energy; at d=1 the high block and all Schur entries are strictly positive, hence the entire operator is strictly positive.

## Why the refined finite estimate cannot decide this control

The retained third direction belongs to ker(Z). CC59's correlated majorant therefore equals1/kappa there, independent of d, and exceeds S2=4. At d=kappa it attains the true response; at d=1/4 or1 it is a strict upper bound. Neither CC59 optimization nor any CC60 rational trial can certify the blind direction using just this data package. The impossibility is exact: the SAME data admit a negative completion as well as a positive one.

Adding physical coordinates with growing diagonal energies orthogonal to the finite source spans yields compact-resolvent infinite controls with the same sources, floor and Schur signs. All observed vectors belong to the operator domain. Thus domain membership, physical L2 sources and compact resolvent do not resolve this finite-source ambiguity either. No such arbitrary completion is asserted admissible for the actual Weil identities.

The finite source lower frame here remains strictly positive at complete contact. This does not contradict CC56's finite polynomial source injection: the actual null includes unmeasured components, and the original operator annihilates the COMPLETE vector. A lower frame on an observed finite carrier is not a lower frame on the actual critical eigenspace, nor a defect-relative source-shell bound.

## Genuine positive-level controls

Let Q0=Q(1/4). It is positive semidefinite with the displayed actual null h. For mu=10^-40,1/100,1/20 define Q_mu=Q0+mu I on the ENTIRE physical space. Then h is a genuine positive ground eigenvector, Q_mu h=mu h and Q_mu(h,h)=mu||h||²>0. The whole-mass shift returns the null; shifting only the three retained diagonals leaves positive energy on h. These level controls do not keep the original source columns identical to Q0; source invariance is asserted only for the d-completion family above. They prevent interpreting a shifted positive level as an original null.

## Minimal additional arithmetic obligation

CC60 gives dim ker(Z)>=54 per actual retained parity and a nonzero blind vector in every actual three-dimensional retained Ritz plane. No source residual on those vectors has yet been enclosed. On that space the current partial-data sufficient gate requires the actual upper correlation

    sigma* sigma < kappa S2  restricted to ker(Z),

or a sharper bound on the TRUE high inverse response there. A native three-plane on which P>=kappa S2 in every direction would already refute the two-source correlated sufficient estimator, because that plane intersects ker(Z); it would not refute actual positivity. This is a useful small-matrix stopping test once the complete original compensated sources are available. A directional witness alone cannot establish a collective plane inequality or a56-dimensional gate.

If the physical gate fails on a blind vector, the actual high form can still be much larger than the guaranteed floor on its source. A rigorous source-aligned high inverse/form-dual estimate or stronger high-block information can settle that case. Additional finite source norms alone cannot distinguish the explicit completions above. For a complete collective certificate, active/blind cross terms must also be controlled; positivity on separate diagonal subspaces is not enough.

This isolates why the currently recovered arithmetic estimates have not yet certified cap-uniform old-gap-independent leakage or a uniform defect-relative lower frame. It does not establish that the complete original identities fail to imply them: those identities constrain the missing high form, but their required quantitative correlations remain unevaluated. The immediate native producer task remains rigorous arch-prime/pole crosses and compensated sources, including both measured high-source vectors. If its sufficient gate fails, a true C-form-dual test remains available.

## Validation and standing

[Validator](../scripts/validate_same_source_completion_cc61.py), [validation](data/RPB108_SAME_SOURCE_COMPLETION_CC61_VALIDATION_20261009.json), [custody](data/RPB108_SAME_SOURCE_COMPLETION_CC61_CUSTODY_20261009.json): all three identical-column/Gram cases, exact common high eigenfloor, observed lower frame, complete Schur signs, actual null and negative vector, fixed correlated upper bound and three genuine positive ground levels pass using Fraction arithmetic. Finite tests accompany the displayed exact construction; they are not a replacement for the operator argument.

No new native full-source Gram or residual is computed. Whole positivity remains21/20. Target53/50 full sign, actual Weil contact exclusion, all-cap leakage/frame, RH/F4, full transport and Lean remain open. Global, Aperture, Shadow and generic endpoint/continuity routes remain paused; historical wording is unchanged.
