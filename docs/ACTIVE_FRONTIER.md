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
| Full constant-weight signed-negative band candidate | SM06: exact 8-panel composite source PASSED; A_o absorbs pole + the whole constant 7/5-weighted J=[3.645,3.705] signed-negative continuum with all higher moments paid, and supported L2 floor >5.644e-5; **not** the variable original signed multiplier on J, other negative bands, or full odd Weil |
| Certified variable-excess obstruction | SM07: full original signed m(ξ)<-2.12269 on J1=[3.645,3.655]; physically supported original negative residual E after SM06's constant-weight band has ||E||>0.0131457, far greater than reported L2 floor 5.6440e-5. **Does not refute domination by full conditioned A_o** |
| Full original negative upper carrier (SM09) | Exact-rational whole-frequency SI10 original seven-prime envelope certified on 973 unresolved half-frequency leaves / 107 clusters; on physical odd carrier, entire K_neg,o is Loewner-dominated by (1+1/1024) P K_cap P with odd dim <=890 plus global infinite cross-coupled remainder <3.014363e-10 (b=24). **Finite supported positive-vs-negative block together with odd pole still OPEN**; scoped CI Actions 39011941429 PASSED |\n| SM08 nonuniform original negative subband | 16-panel exact rational full five-source physical inverse and two complete infinite tails PASSED (Actions 39011691075); simultaneously absorbs pole + constant 7/5 continuum J + added 3/5 continuum J1; positive residual floor >1.682631e-7. **Selected weighted lower subband only**; full W-ODD-NEG OPEN |\n| SM10 explicit full original odd negative cap matrix | Exact-rational 107 rational SPD Taylor moment blocks, 4433 distinct matrix entries, 890 supported odd source columns, plus complete infinite all-frequency error eta=3.014362544201399e-10; focused Actions 39012671893 PASSED. **Actual coupled 891-source original positive inverse/Schur gate remains OPEN** |\n| Live alternative methods | SM10 actual supported 891-source original positive inverse/Schur for D=diag(2,(1+tau)C) and B=A_o-eta I; assess C16 source reference sufficiency or native RC high Schur with proved carrier transfer |
| Separate verification | LF113 full-root Lean CI passed; original-Weil certificate attachment still open |
| Baseline research HEAD | `953df96c900d3e533dff92f30c4eebec65fd60a6` (merged SM01) |
| Full odd signed positivity | **OPEN** |
| Even / full Weil / global bridge / RH | **OPEN** |

The exact remaining odd-sector test is

`R_o (A_o - 2|s><s|)^(-1) R_o* <= I`,

where `R_o` is the **original** negative-frequency analysis operator on the physical odd carrier. The Schur formula is an equivalence, **not** a proof that this inequality holds. The missing result includes the entire negative-frequency family, all cross couplings and the infinite residual.

**Next progress event:** SM10 has made SM09's entire actual negative-frequency UPPER compression an explicit 107-block rational covariance and 890 physical odd Taylor sources; the global residual remains <3.014363e-10. Test the original coupled **891-source** finite physical inverse/Schur inequality, including the odd pole and all intercluster physical Gram entries. A successful moment construction or selected SM08 subband alone cannot close W-ODD-NEG.

For current code HEAD, use the live Git branch. For current research priority, use `active_obligation`. For exact acceptance, see its `acceptance` field. This file should be reconciled whenever the active obligation is changed.
