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
