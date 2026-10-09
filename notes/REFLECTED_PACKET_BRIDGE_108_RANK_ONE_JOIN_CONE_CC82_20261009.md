# CC82 — necessary and sufficient rank-one repair of the joined lower matrix

Integration parent CC81: 68d23fd4b746f9ae2496433d2ea34af38bd7b65d. Read-only Native Source remains NF42: f2c49f8d2ff95374d3ee2c3b1836ec772e4817dc. Read [CC82 definitions](../docs/TERMINOLOGY_RPB108_RANK_ONE_JOIN_CONE_CC82.md) before the cone criterion. No source producer or other branch is changed.

## A full-matrix acceptance target beyond the frozen witness

CC81 gives necessary additional response along NF38's fixed witness. Passing that one quotient does not settle the joined matrix because the new response also changes its leading pair and mixed border. CC82 eliminates those changes exactly.

For the exact true quantities in the source enclosures, write K1=[[E,r],[r*,c]], with E>0 and s=c-r*E^-1r<0. The new rank-one response is p*p/b, b>0. Its leading block is E+pE*pE/b>0. Sherman–Morrison in that block gives the updated condensed margin

    s_new = s + |p2-r*E^-1 pE*|^2 / (b+pE E^-1 pE*).

Therefore the whole three-by-three lower matrix passes if and only if

    |p2-beta pE*|^2 > (-s)(b+pE E^-1 pE*),  beta=r*E^-1.

Equivalently, since K1 has two positive and one negative eigenvalue,

    b+p K1^-1 p* < 0.

The determinant lemma gives det(K1+p*p/b)=det(K1)(1+p K1^-1 p*/b). The positive updated leading pair and negative det(K1) turn this scalar determinant sign into the full matrix sign. This equivalence uses all signed coordinates; it is not a criterion obtained from independent diagonal scores.

The response must align with the negative Schur direction after paying its positive-pair coupling. Large |p h| on the old fixed witness alone can fail because the positive-pair contribution also enlarges the denominator. A new exact control has K1=diag(1,1,-1), p=(10,0,2), b=1: its old negative witness gains 4 and becomes positive, but the complete updated margin is -1+4/101<0.

## Original arithmetic coefficients now certified for the acceptance target

The new consumer authenticates the unmodified NF42 parity certificates through CC81's pinned hashes. Separate exact rational interval arithmetic encloses E^-1, beta and s from the original full joined lower matrices and checks the condensed values against NF42. It does not reconstruct a new original source column.

| Positive deficit -s in the exact cone, outward display | Even | Odd |
| --- | ---: | ---: |
| Interval enclosure | (9.3952,9.8493)e-23 | (1.4591,1.4720)e-21 |

These are unnormalized three-coordinate Schur deficits. They differ from CC81's necessary fixed-witness thresholds; neither is a physical spectral gap. The signed beta coefficients and complete E^-1 intervals are stored in the machine-readable CC82 certificate. The lower end of a deficit interval is only a necessary rejection screen. For a robust pass, the numerator's proved lower bound must exceed the deficit upper bound times the positive denominator upper bound.

For a source-provided p,b, first enclose t=p2-beta pE*. If its interval crosses zero, the safe lower bound for |t|² is zero. Otherwise use the square of its smaller absolute endpoint. Enclose b+pE E^-1pE* with every source error paid and certify positive lower endpoint. A strictly positive lower margin from the complete cone inequality is sufficient, even when interval overestimation forgets true correlations. An inconclusive enclosure is not rejection of the actual source row. Direct full-matrix interval or rational-congruence checking remains available when the cone enclosure loses too much correlation.

## Relation to the actual original form

Under the explicit remaining-high floor and operator-domain/source hypotheses, D1=A-A1>=0, d1>0 and completion of its defect square imply A>=A2=A1+f1 f1*/d1. Hence the actual joined Schur matrix dominates K1+p*p/b. Passing the cone in both parities certifies the six retained directions with all original high directions. It still leaves 106 retained directions and their collective couplings.

The equivalence is necessary and sufficient for this exact rank-one lower certificate, not necessary for actual original positivity: the actual residual response may be larger. Rescaling the candidate source column multiplies p by a nonzero scalar and b by its square, leaving the cone unchanged. No old whole-domain margin enters this acceptance target. The remaining-high floor is a standing explicit hypothesis and is not established anew by CC82.

## Verification

Run:

    python scripts/certify_cc82_rank_one_join_cone.py notes/cc81-source --output notes/data/RPB108_CC82_RANK_ONE_JOIN_CONE_20261009.json

Six exact mixed controls use a starting matrix with all positive diagonals and inertia (2+,1-), at scales 1 and 10^-18. The direct determinant, updated pair condensation and inverse-quadratic condition agree at positive/null/negative crossings. The witness-only countercontrol fails the full cone despite paying the frozen witness. The independent original interval coefficient consumer passes in both parities. Python syntax compilation passes. Original source integrations are not replayed here.

## Next source deliverable and standing

The source producer should freeze and certify an additional independent high column, retaining all signed attachment and source covariance terms needed for p and b. CC82 provides the full-matrix acceptance target for that deliverable. If one column's cone fails, the result rejects its rank-one minorant only; it does not reject every independent column or a larger multi-column response.

No new original source row, simultaneous six-direction sign or physical gap is claimed. The separate CC74/CC78 full-high restrictions and the whole-domain 21/20 anchor remain preserved. Whole 53/50, remaining background transport, uniform all-cap continuation, RH/F4/full transport and Lean remain open. Historical wording, Native Source, DNE and paused branches are unchanged.
