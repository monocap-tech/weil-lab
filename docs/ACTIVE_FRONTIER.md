# Canonical live frontier — 2026-10-16 baseline

**Read [the obligation manifest](../research/obligations.json) for the authoritative active obligation.** This is a human-oriented baseline, not an independent mutable HEAD or a claim of automatic synchronization.

| Field | Current baseline |
| --- | --- |
| Objective | RH via original-zeta Weil-form program |
| Active obligation | `W-ODD-NEG`: complete signed negative-frequency odd-sector control |
| Accepted prerequisite | SI29: `2<s,A_o^-1 s><0.966379<1` for the odd pole alone |
| Structural reduction | SM01: pole-absorbed coercivity and exact remaining negative-frequency Schur gate |\n| New reduction | SM02: odd-parity physical packet rank at b=24 <=891 (versus 1781 full-space), with unchanged original negative-frequency error; coupled finite matrix open |
| Live alternative methods | SM03/SI30 actual odd signed finite packet response; RC335 native high-Schur |
| Separate verification | LF113 full-root Lean CI passed; original-Weil certificate attachment still open |
| Baseline research HEAD | `953df96c900d3e533dff92f30c4eebec65fd60a6` (merged SM01) |
| Full odd signed positivity | **OPEN** |
| Even / full Weil / global bridge / RH | **OPEN** |

The exact remaining odd-sector test is

`R_o (A_o - 2|s><s|)^(-1) R_o* <= I`,

where `R_o` is the **original** negative-frequency analysis operator on the physical odd carrier. The Schur formula is an equivalence, **not** a proof that this inequality holds. The missing result includes the entire negative-frequency family, all cross couplings and the infinite residual.

**Next progress event:** a certified full-negative operator inequality, a quantitatively non-tautological structural bound, or a proved obstruction that redirects the method. SM02 is a real dimension/cost reduction, **not** a passed finite negative-frequency matrix eigenvalue. Merely creating SM02/SI30/RC335 or passing a retained prerequisite replay is not such an event.

For current code HEAD, use the live Git branch. For current research priority, use `active_obligation`. For exact acceptance, see its `acceptance` field. This file should be reconciled whenever the active obligation is changed.
