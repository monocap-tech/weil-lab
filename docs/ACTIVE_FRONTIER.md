# Canonical live frontier — 2026-10-16 baseline

**Read [the obligation manifest](../research/obligations.json) for the authoritative active obligation.** This is a human-oriented baseline, not an independent mutable HEAD or a claim of automatic synchronization.

| Field | Current baseline |
| --- | --- |
| Objective | RH via original-zeta Weil-form program |
| Active obligation | `W-ODD-NEG`: complete signed negative-frequency odd-sector control |
| Accepted prerequisite | SI29: `2<s,A_o^-1 s><0.966379<1` for the odd pole alone |
| Structural reduction | SM01: pole-absorbed coercivity and exact remaining negative-frequency Schur gate |
| New reduction | SM02: odd-parity physical packet rank at b=24 <=891 (versus 1781 full-space), with unchanged original negative-frequency error; coupled finite matrix open |
| Sparse reference obstruction | SM03: full original signed negative-frequency interval J=[3.645,3.705] defeats unchanged 14-feature C14 reference (certified margin >0.03 on a physical odd Jensen packet); this is not an original Weil-negative witness |
| Intrinsic negative spectral rank | SM04: 15 original physically supported odd negative packets certify λ15(K_neg,o)>0.0151354>κ=0.001; **any** κI plus positive rank≤14 correction is insufficient to dominate the full K_neg |
| Original supported coupled inverse | SM05: 16 positive true Jensen features give A_o >= 2|s><s| + (21/125)|g_-><g_-| jointly and uniformly on the odd carrier (first exact-rational and focused final-head SM05 source replays passed); **all other negative-frequency modes remain OPEN** |
| Live alternative methods | SM06/RC extend SM05 beyond one coupled negative packet with certified complete residual; alternatively native supported RC high-Schur with explicit carrier transport |
| Separate verification | LF113 full-root Lean CI passed; original-Weil certificate attachment still open |
| Baseline research HEAD | `953df96c900d3e533dff92f30c4eebec65fd60a6` (merged SM01) |
| Full odd signed positivity | **OPEN** |
| Even / full Weil / global bridge / RH | **OPEN** |

The exact remaining odd-sector test is

`R_o (A_o - 2|s><s|)^(-1) R_o* <= I`,

where `R_o` is the **original** negative-frequency analysis operator on the physical odd carrier. The Schur formula is an equivalence, **not** a proof that this inequality holds. The missing result includes the entire negative-frequency family, all cross couplings and the infinite residual.

**Next progress event:** extend SM05's genuinely certified supported two-source joint inequality to **the complete negative-frequency operator**, including packet–packet cross terms and an infinite remainder, or obtain a different structural full-continuum certificate. The current success does not close the original W-ODD-NEG gate.

For current code HEAD, use the live Git branch. For current research priority, use `active_obligation`. For exact acceptance, see its `acceptance` field. This file should be reconciled whenever the active obligation is changed.
