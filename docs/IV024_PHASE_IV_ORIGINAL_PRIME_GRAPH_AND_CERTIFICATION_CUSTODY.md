# Weil-Lab — IV024: Original arithmetic graph and certification-frontier custody

**Independent Phase IV head:** IV024, stacked on IV023 PR #805. Phase III numerical NF### original-source certification remains separate and unchanged.

**Formal status:** no new Lean positivity theorem. This stage creates (1) an independently calculated exact-rational original arithmetic prime-power interaction graph, (2) a 14-module original Phase IV source-chain inventory, (3) two deliberately NONKERNEL GitHub Actions preflight checks, and (4) two explicitly falsifiable compatibility conjectures. Source-only verification is not kernel certification.

## 1. The existing Lean proof frontier is still queued

Real GitHub Actions status at IV024 inspection:

| Original source stage | Run | Observed state |
|---|---|---|
| IV009 repaired Schwartz finite-sum polarization | [44850887402](https://github.com/monocap-tech/weil-lab/actions/runs/44850887402) | QUEUED |
| IV018 | [44850967574](https://github.com/monocap-tech/weil-lab/actions/runs/44850967574) | PENDING |
| IV019 | [44851439481](https://github.com/monocap-tech/weil-lab/actions/runs/44851439481) | QUEUED |
| IV020 | [44851946887](https://github.com/monocap-tech/weil-lab/actions/runs/44851946887) | QUEUED |
| IV021 | [44852596209](https://github.com/monocap-tech/weil-lab/actions/runs/44852596209) | QUEUED |
| IV022 | [44853338807](https://github.com/monocap-tech/weil-lab/actions/runs/44853338807) | QUEUED |
| IV023 | [44854690456](https://github.com/monocap-tech/weil-lab/actions/runs/44854690456) | QUEUED |

Prior IV009 run 44844586039 FAILED because an invalid definitional change attempted to identify the actual original raw correlation-transform summability with the original Schwartz divisor pair function. The source repair rewrites through the authenticated original correlation-transform identity, and was propagated through IV023. There has been no subsequent compiler/axiom result demonstrating that the repair compiles. Additional queued workflows are not evidence of Lean success.

## 2. A separate independent finite arithmetic object

Define the physical intervals:

- Original old left: center −1099/1000, radius 1/1000.
- Original old right: center +1099/1000, radius 1/1000.
- First new: center +1/5, radius 1/500.
- Second new: center −1/5, radius 1/4000.

Let G_Λ(E) be the directed signed interaction graph of pairs of such cells whose physical intervals overlap after translating one by ±log(n), for genuine active prime powers 2 ≤ n < 10.

This graph is defined **independently of the Lean Weil-form implementation** using exact rational cell endpoints, elementary integer prime-power detection, and rigorous 96-term rational-series intervals for real log(n). A sample is CLEAR only if its certified lower distance exceeds the sum of radii, OVERLAP only if its certified upper distance is smaller, and UNKNOWN otherwise. UNKNOWN fails closed. This proves or refutes **potential support overlap**, not nonzero values of arbitrary prime correlations.

Actual exact arithmetic results independently replicated during IV024:

- Active n are exactly 2,3,4,5,7,8,9.
- The only surviving directed signed overlap edges are old-left to old-right at +log(9), and old-right to old-left at −log(9).
- There are no first-new, second-new, or new-new active prime-power overlap edges.
- The least certified positive clearance is approximately 0.08429436111989062.
- Exact physical union measure is 17/2000.
- The previous source's **conditional, coarse** signed residual is exactly 7/10−75·(17/2000) = 1/16.

The committed independent script also verifies that permutations of physical cell labels leave the canonical physical graph and signed width unchanged.

## 3. Two falsifiable counterexamples

**Prime collision:** Replace the second new interval with a small cell centered at the first-new center plus 693/1000. Its separation rigorously overlaps a true ±log(2) prime-power translation; the exact arithmetic graph contains two extra directed n=2 edges. Thus the graph preservation law is NOT valid for arbitrary extensions.

**Loss of analytical capacity without prime collision:** Instead widen the second cell at −1/5 to radius 1/1000. The prime interaction graph still has only its two historical old-old n=9 edges; however support measure becomes 1/100 and the coarse signed margin 7/10−75/100 is negative. Therefore arithmetic admissibility and the positivity of this particular analytic lower bound are **distinct requirements**. A negative coarse bound is not evidence the original Weil form is negative.

## 4. Intrinsic versus chosen quantities

Once the original signed Weil form and a test are fixed, its quadratic pairing, genuine prime functional, signed Gamma integral, both pole evaluations, true physical L² mass, and actual shifted correlations are intrinsic values of that specified realization.

The physical union measure, finite arithmetic overlap graph, and presence of the exceptional old n9 interaction are properties of a CHOSEN PHYSICAL SUPPORT DOMAIN, independent of arbitrary labels or finite basis order but not invariant under moving support centers or changing radii.

The two smooth cutoff functions, the gamma two-regime lower estimates, Fourier L¹ low-band bound, factor-eight pole estimate, original blanket prime cost 2/5 and resultant margin 1/16 are auxiliary sufficient estimates. Neither 1/16 nor graph adjacency is an identified optimal spectral eigenvalue.

## 5. Two precise compatibility conjectures, not equivalence claims

**IV024-A — original arithmetic source compatibility.** Hypotheses: a true Schwartz partition into the old original two collars and both added cells; the complete ORIGINAL zeta prime term agrees with the literal finite active ±log(n) correlation expansion under the original window; this domain's graph has no new active prime-power edges; and the historical original NF600 old n9 bound applies. Conclusion to prove: for every supported f, the complete original prime expression equals that of the OLD Schwartz component, including the surviving n9 term, and satisfies the old 2/5 mass bound. Together with the gamma/two-pole signed source estimates and support width 17/2000, this implies the restricted four-cell original Weil lower bound 1/16. IV023 contains a source-level Lean CANDIDATE proof, but no verified kernel acceptance.

**IV024-X — distinct cross-projection conjecture, not proved.** Require a truly independent arithmetic or spectral space H, densely defined operator A (or a separately defined pairing), a common test domain D, and an explicit map T:D→Dom(A). Compatibility would require the exact complex sesquilinear identity

    W_original(f,g) = <T(f), A T(g)>_H,

with the conjugation conventions, both original poles, signed gamma and prime components all explicitly accounted for. If mass is claimed preserved, separately prove ||T(f)||² = Mass(f); likewise prove any desired injectivity, density, domain and extension properties. Test potential original prime support edges versus the actual couplings under T. The finite arithmetic graph is only a **necessary geometric constraint on possible prime interactions**, not an independent spectral representation of the whole original Weil form.

Falsification: a nonzero source prime correlation on an edge certified CLEAR, a genuine original n9 term omitted by the proposed dictionary, a failure of support partition, a spectral quadratic pairing unequal to its original counterpart on an admissible test, or missing normalization/domain assumptions. Failure of a coarse bound at larger width is NOT a counterexample to the original Weil form itself.

## 6. Machine-checkable separate custody

Independent arithmetic graph and counterexample script: scripts/iv024_original_prime_interaction_graph.py.

Fail-closed source inventory: scripts/iv024_phaseiv_source_chain_gate.py. It checks all 14 original source modules for IV009 and IV017–IV023, their actual local import paths, local theorem names, direct source #print axioms targets, missing or forbidden local declarations and the preserved IV009 source repair. A separate read-only GitHub inspection of these files found matching declaration/audit inventories and no local forbidden commands; **none of these static checks elaborate Lean proofs**.

Dedicated pure-Python workflow: .github/workflows/iv024-original-prime-graph-source-preflight.yml. Its two jobs are explicitly labeled NONKERNEL; they do not install or claim to run Lean.

The actual IV009–IV023 standard-only Lean/Mathlib compiler jobs, their original source SHA-bound .olean artifacts and #print axioms are still the sole acceptance gate for the proposed Weil source theorems.

**Next IV025:** recover actual compiler diagnostics and repair the earliest failing Lean proof, without adding another uncompiled positivity layer. Then parameterize arbitrary finite prime-safe support cells and seek a genuinely independent spectral/arithmetic model for IV024-X. Phase III NF### continues separately.

No global Weil positivity, RH, or independent spectral equivalence is claimed.
