# NJDG External Source Pins

**Date:** 2026-09-29  
**Branch:** `research/nextjet-derivative-geometry`  
**Standing:** reconnaissance/source-pin ledger only

## Canonical internal source

### monocap-tech/provenance

Pinned reconnaissance state:

`e4cacb598995490ee7c022cdd3904106b1911ae2`

Load-bearing internal references:

- `rh/checkpoints/RH_KEY_GLOBAL_SOURCE_2_GSR_DOMAIN_NEXTJET_STOP_20260920.md`
- `rh/checkpoints/RH_KEY_SOURCE_II_4_ARBITRARY_ORDER_RENORM_JET_TOWER_20260921.md`
- `rh/checkpoints/RH_KEY_SOURCE_II_5_FINITE_JET_COVARIANCE_NO_BYPASS_20260921.md`
- `rh/checkpoints/RH_KEY_SOURCE_II_6_OBLIVIOUS_QUANTIFIER_AND_TOTAL_SOURCE_SPLIT_20260921.md`
- `rh/checkpoints/RH_KEY_SOURCE_II_7_EXACT_ARCH_TOTAL_SOURCE_TRANSVERSALITY_20260921.md`
- `rh/checkpoints/RH_KEY_SOURCE_II_8_FINAL_GATE_EQUIVALENCE_AND_SOURCE_I_RELOCATION_20260921.md`
- `rh/checkpoints/RH_RELOCATION_KEYC_NEXTJET_20260921.md`

These are canonical constraints for NJDG. They are not copied into Weil-Lab as replacement custody.

## External GitHub reconnaissance

### teal-sea/zeta-lab

Pinned commit:

`783307c8be59317375ae6675622b4d3019222875`

Relevant files:

- `hunts/higher_xi/MISSION.md`
- `hunts/higher_xi/RESUMMED-BRIDGE.md`
- `hunts/higher_xi/RAMS2-CLUSTER.md`
- `hunts/higher_xi/URMS2-051-AUDIT.md`
- `hunts/higher_xi/RESULTS-higher-xi.md`

Reason for inclusion:

- exact untruncated higher-(Xi) resolvent;
- uniform coefficient-square / mean-square architecture;
- higher-derivative zero statistics;
- explicit separation between representation and the missing analytic bound.

Current NJDG disposition:

**STRUCTURALLY RELEVANT, NOT A DIRECT NEXTJET THEOREM.**

Main mismatch:

their strongest bridge is band/mean-square in height; NJDG requires worst-packet complement control after selected-only multiplier freezing.

### ashaffer/riemann-zeta

Pinned commit:

`ca617bed2607aec5dd0c7e2664d7ecbbdd0c1778`

Relevant files:

- `results/ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`
- `results/ZETA23-ADDITIVE-EDGE-PADDING-AUDIT-2026-08-11.md`
- `results/ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md`
- `results/UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`
- `results/ZETA23-BERGMAN-SUPERCONDUCTOR-MOLLIFIER-AND-RECIPROCAL-JET-GATE-2026-08-12.md`

Reason for inclusion:

- Cauchy-Vandermonde endpoint-jet interpolation;
- collision-sensitive singular-value loss;
- target-conditioned Moore-Penrose/Hermite language;
- explicit no-go results showing why ordinary full-spark or bulk-moment data do not give uniform lower edges.

Current NJDG disposition:

**DIRECTLY RELEVANT TO THE FORM OF THE MISSING INVERSE THEOREM; NO IMPORTABLE KPH/NEXTJET BOUND LOCATED.**

### x67ai/riemann-rh-program

Pinned commit:

`92772ac35255b66aba5ebba46414f0ce31e264a7`

Relevant files:

- `rh-program/directions/B3-arithmetic-debranges.md`
- `rh-program/results/verdicts.json`
- derivative-zero / reciprocal-residue numerical and audit files under `rh-program/results/`.

Reason for inclusion:

- mixed ((Xi,Xi')) Gram/cross-correlation idea;
- derivative-zero visibility and Speiser/Levinson-Montgomery lineage;
- adversarial audits explicitly identifying local (1/log T)-scale density as the missing pointwise input.

Current NJDG disposition:

**POTENTIAL DERIVATIVE-GEOMETRY CLUE; ORIGINAL DE BRANGES/JET INTERPRETATION PARTLY WITHDRAWN IN THAT REPO.**

Only independently surviving statements may be reused.

### djplatt/code

Pinned commit:

`42b21426718e542daa2b006dc05ea2d7f26426e6`

Relevant examples:

- `bober/zetap_real_nofft.c`
- `harald/apr_20/residues.cpp`
- `harald/apr_20/residues-rs.cpp`

Reason for inclusion:

rigorous Arb/ACB infrastructure computing (1/zeta'(ho)) at certified critical-line zeros.

Current NJDG disposition:

**NUMERICAL RECONNAISSANCE INFRASTRUCTURE ONLY.**

It can test candidate theorem variables; it cannot establish a worst-packet asymptotic floor.

## Non-GitHub paper leads discovered through GitHub

These are research leads, not yet pinned as imported theorem dependencies:

- Gordon Chavez, arXiv:2409.02106, reciprocal zeta derivative bounds;
- Speiser criterion;
- Levinson-Montgomery zero-count comparison for (zeta');
- Soundararajan / Zhang work on horizontal distribution of (zeta')-zeros;
- Farmer-Gonek-Lee derivative-zero pair-correlation lineage;
- Ji Bian thesis on zeros of higher derivatives of (Xi).

Before any load-bearing use, obtain the primary source, record exact theorem/hypotheses, and classify whether the result is unconditional, RH-conditional, simplicity-conditional, average, density, almost-all, or pointwise.

## Quantifier filter

For every candidate source, record:

[
oxed{
	ext{domain}
+
	ext{selection order}
+
	ext{packet scope}
+
	ext{height uniformity}
+
	ext{exceptional set}
}
]

A result with an exceptional set is not automatically usable for S-II.

A result averaged over zeros or heights is not a worst-packet theorem.

A theorem assuming RH cannot be used inside the false-RH reductio unless only an implication valid before the RH assumption is extracted.


## NJDG-1 hostile control pin

### ashaffer/riemann-zeta — derivative-zero quartet gate

Pinned file:

`results/ZETA23-SPEISER-DERIVATIVE-ZERO-QUARTET-GATE-2026-08-12.md`

Pinned repository commit:

`ca617bed2607aec5dd0c7e2664d7ecbbdd0c1778`

NJDG use:

- exact symmetric quartet polynomial showing off-axis original zeros need not force off-axis derivative zeros;
- explicit warning that (Xi') and (zeta') are different local geometric objects;
- aggregate Speiser / Levinson-Montgomery quantifier audit.

Disposition:

**HOSTILE CONTROL / SEARCH-SPACE PRUNING.**

No theorem from this file is promoted to canonical provenance by NJDG-1. The local pair-capture lemma and inverse-gap cofactor dichotomy in NJDG-1 are derived independently in Weil-Lab.


## NJDG-4 critical-point-frame source audit

### Garaev–Yıldırım — small distances between zeta and zeta-prime zeros

Primary source:

M. Z. Garaev and C. Y. Yıldırım, *On small distances between ordinates of zeros of zeta(s) and zeta'(s)*, IMRN 2007, arXiv:math/0610377.

Verified primary abstract statement:

For every zero
[
ho'=eta'+igamma'
]
of (zeta'), there exists a zero
[
ho=eta+igamma
]
of (zeta) such that
[
|gamma-gamma'|
ll
sqrt{|eta'-1/2|}.
]

NJDG disposition:

**POINTWISE BUT WRONG DIRECTION / ONE ROW ONLY.**

It begins with a derivative zero and locates one zeta zero ordinate. NJDG requires the converse type of input: every dangerous selected zeta packet must force enough derivative-critical rows to reconstruct RENJET. The theorem supplies neither two critical points nor a conditioning floor.

### Haseo Ki — zeros of zeta-prime near the critical line

Primary source:

Haseo Ki, *The zeros of the derivative of the Riemann zeta function near the critical line*, arXiv:math/0701726.

Verified primary abstract statement:

Assuming RH, Ki proves an equivalence between
[
liminf(eta'-1/2)loggamma'
e0
]
and a microscopic nearest-zero approximation
[
rac{zeta'}{zeta}(s)
=
rac1{s-ho}
+
O(log t)
]
uniformly in (|sigma-1/2|<c/log t), where (ho) is the closest zeta zero.

NJDG disposition:

**MICROSCOPICALLY RELEVANT / RH-CONDITIONAL / NO FALSE-RH REENTRY.**

This is exactly the scale NJDG cares about, but the theorem assumes RH and still does not furnish a two-row critical-point frame or a second-resolvent RENJET bound.

### Farmer–Ki — Landau–Siegel zeros and zeta-prime zeros

Primary source:

David W. Farmer and Haseo Ki, *Landau-Siegel zeros and zeros of the derivative of the Riemann zeta function*, arXiv:1002.1616.

Verified primary abstract statement:

If (zeta') has sufficiently many zeros close to the critical line, then (zeta) has many closely spaced zeros.

NJDG disposition:

**AGGREGATE / WRONG QUANTIFIER FOR FRAME SOURCE.**

The hypothesis concerns sufficiently many derivative zeros; it does not produce a uniformly conditioned local derivative frame from one adversarial selected packet.

### Levinson–Montgomery lineage

Primary bibliographic anchor:

Norman Levinson and Hugh L. Montgomery, *Zeros of the derivatives of the Riemann zeta-function*, Acta Math. 133 (1974), 49–65.

Modern source confirmations identify the classical result as the derivative-zero counterpart of Speiser and as a global/counting theorem.

NJDG disposition:

**GLOBAL COUNTING / NO PACKET-LOCAL FRAME.**

The known count comparison and Speiser equivalence do not supply location, separation, or jet order for two derivative rows attached to one selected packet.

### Das–Pujahari — higher derivatives

Primary source:

Mithun Kumar Das and Sudhir Pujahari, *Zeros of higher derivatives of Riemann zeta function*, arXiv:2104.10243.

Verified primary abstract statement:

The work studies mollified mean values in short intervals, refines error terms in zero-density results for (zeta^{(k)}), and proves an almost-all clustering result for zeros of an associated higher-derivative function.

NJDG disposition:

**HIGHER-DERIVATIVE / DENSITY-MEAN-VALUE / NOT POINTWISE FRAME.**

It does not force a confluent or uniformly conditioned derivative configuration on every dangerous packet.

### Guo / Feng / Zhang near-critical-line lineage

Located bibliographic anchors:

- C. R. Guo, *On the zeros of the derivative of the Riemann zeta function*, Proc. London Math. Soc. 72 (1996), 28–62.
- Shaoji Feng, *A note on the zeros of the derivative of the Riemann zeta function near the critical line*, Acta Arith. 120 (2005), 59–68.
- Yitang Zhang, *On the zeros of zeta'(s) near the critical line*, Duke Math. J. 110 (2001), 555–572.

NJDG disposition:

**NEAREST-NEIGHBOR LITERATURE / NO LOCATED EVERY-PACKET TWO-ROW FRAME THEOREM.**

The current source audit did not locate a theorem in this lineage giving, for every prescribed dangerous zeta packet, two derivative-critical points with explicit packet-scale location and projective separation, nor a forced confluent critical point carrying the missing RENJET jet order.

## NJDG-4 source conclusion

No located source crosses the frame-source gate.

The strongest pointwise unconditional input found is one-way derivative-to-zeta ordinate proximity.

The strongest microscopic local logarithmic-derivative input found is RH-conditional.

The higher-derivative sources remain density, mean-value, or almost-all in character.

This is a bounded source audit, not a literature-exhaustion theorem.
