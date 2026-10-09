# CC84 — one combined source column suffices whenever a finite batch passes

Integration parent CC83: f867b20e04d6783125a8a2ae0870b15ac16a40aa. Read-only source NF43: b21b3df8e026db1b8b253325442b6dfaa63f05ef. Read [CC84 definitions](../docs/TERMINOLOGY_RPB108_SOURCE_SPAN_COMPRESSION_CC84.md) before the span theorem. Source and other branch refs remain unchanged.

## Structural result at the current one-negative-direction stage

NF43's exact conditional joined lower matrix K2 has a positive leading two-dimensional pair and one negative condensed direction in both parities. CC84 shows that, for a completely certified finite source span, a passing multi-column response can always be represented by a suitable single linear combination for purposes of the full three-dimensional joined sign. A sequence of individually passing columns is therefore not required. Individual trial columns may all fail even though their span contains a passing combination.

This is a theorem about the fixed three-retained-direction restriction and a proposed finite source span under the stated original high-floor/source hypotheses. It is not a claim that an already measured or arbitrary finite span passes, nor a global continuation theorem.

## Complete finite-span acceptance and proof

Let Y be candidate original high polynomials, F=D2Y, G=Y*D2Y>0, B=G+F*A2^-1F>0 and P=F*A2^-1R. Positivity of D2 implies D2>=F G^-1F*, so the actual joined Schur matrix dominates

    Kbatch=K2+P*B^-1P.

Write K2=[[E,r],[r*,c]], s=c-r*E^-1r<0, and P=(PE,p_last). Eliminating the updated positive leading pair using Woodbury gives

    M=B+PE E^-1PE*>0,
    t=p_last-PE E^-1r,
    s_batch=s+t*M^-1t.

Thus the complete batch certificate passes exactly when theta=t*M^-1t>-s. This is the full signed Schur test, not a sum of individual response norms.

For any nonzero coefficients a, the original combined polynomial y=Y a has response row a*P and denominator a*B a. Its updated condensed margin is

    s_combined=s+|a*t|^2/(a*M a).

The metric Cauchy–Schwarz inequality bounds this quotient by theta. Taking a=M^-1t attains theta whenever t is nonzero. Consequently the batch and this one combined column have exactly the same condensed margin. Their complete response matrices generally differ; the single-column matrix is no larger than the batch credit in positive-semidefinite order, and physical gap constants are not asserted equal.

The equivalent signed test is

    a*(B+P K2^-1P*)a<0.

Indeed K2's block inverse yields B+P K2^-1P*=M+t t*/s. At a=M^-1t the quadratic equals theta+theta^2/s, which is negative precisely when theta>-s. Since this is a positive matrix plus one negative rank-one term, it has a negative direction exactly in the passing case. This also gives an inertia proof of the batch equivalence.

## Consequence for source selection and paid arithmetic

The missing arithmetic task can be posed as finding a negative quadratic on the signed finite-span matrix B+P K2^-1P*, or equivalently paying theta>-s. Selection should retain the complete native defect Gram, inverse metric and all signed response crosses. Choosing the largest physical shell coefficient or separately maximizing each witness contribution is not this objective.

True source moments may be irrational. A rational midpoint solve can select a trial coefficient vector, but the proof must then enclose that frozen vector's original signed quadratic with all physical errors paid. A strictly negative outward upper endpoint proves the corresponding original combined column passes the full joined lower certificate. No exact equality with the ideal optimizer is needed. When interval inversion is poorly conditioned, the frozen quadratic and full matrix provide alternatives to a direct outward theta enclosure.

Any rational combination of the certified polynomial columns remains an original polynomial with the inherited linear operator attachment. Its covariance, native energy and physical norm must still be paid from the complete packet. The source-span theorem does not authorize discarding crosses, silently extending the floor hypothesis, or claiming positivity from selected midpoint data. A passing span is sufficient, not necessary for actual original positivity.

## Original inertia and new exact controls

The consumer authenticates NF43 certificates through CC83's pinned hashes and independently rechecks positive leading pair and negative complete determinant/condensed margin. This supplies the actual one-negative-direction premise; original source integrations are not replayed here.

Six new exact two-column controls cross positive/null/negative at scales 1 and 10^-18. Every individual column fails, while the optimized combination passes in the positive control. Direct full-matrix condensation equals both the batch formula and combined-column formula. A separate three-column control retains a correlated positive denominator and checks the same equivalence without replacing it by its diagonal. The signed quadratic and condensed signs agree exactly.

Run:

    python scripts/certify_cc84_source_span_compression.py notes/cc83-source --output notes/data/RPB108_CC84_SOURCE_SPAN_COMPRESSION_20261009.json

Result: PASS for the authenticated original inertia and exact finite-span controls. Python syntax compilation passes. The general proposition is proved above; controls verify its implementation, not its universal validity by sampling.

## Boundary and next deliverable

Native Source may certify one new column directly or a finite candidate packet whose signed span contains a passing rational combination. The next column must use the updated NF43 witness/operator and preserve attachment to all five existing high columns. No currently available new candidate packet has been shown to satisfy the span criterion by CC84. The original conditional deficits remain those of CC83.

No new original source span, simultaneous six-direction restriction or physical gap is claimed. The separate CC74/CC78 full-high restrictions and whole-domain 21/20 anchor remain preserved. Whole 53/50, remaining-background transport, uniform all-cap continuation, RH/F4/full transport and Lean remain open. Historical wording, Native Source, DNE and paused branches are unchanged.
