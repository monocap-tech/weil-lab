# RPB-106 — actual pole growth and prerequisite certification repair

**Date:** 2026-09-30 (America/Los_Angeles)
**Research base:** d1f633a40afec05a8a5eba2456d16a36423cf15a
**Effective status:** CORRECT-TARGET BUILD AND AXIOM AUDIT PASSED / RPB-104–105 REPAIRED / EXPLICIT TWO-EXPONENTIAL POLE GROWTH CONSTRUCTED / GAUSSIAN ADMISSIBILITY ASSEMBLED CONDITIONAL ON THE EXACT COMPACT EXT-4 WITNESS / CONCRETE WITNESS ATTACHMENT STILL OPEN / COERCIVITY NOT STARTED.

The final determination in sections 4–8 supersedes the initial in-progress snapshot below. It does not retroactively validate the wrong-target RPB-104/105 runs.

## 1. Recovered validation defect

The recorded RPB-104 validation head `8e8cf915220bf5bff355d4df006b3c18b926a780` and RPB-105 validation head `646adabb7d5423b4eafbd388150a6d0cd0cba2f8` both contain workflow blob `f194e9564577d3b79831b7abfb91b5933f3af98f`.

Its build command is:

```text
lake build WeilDefect.Examples.WeakCriticalFallthrough
```

It is NOT either named cutoff target. The attempted target replacements were no-ops. Runs `36800396833` and `36801083567` therefore do not certify `NeutralGaussianCutoff` or `NeutralGaussianCutoffPairing`. Their green statuses remain historical facts; the scope attributed to them in RPB-104/105 and the status ledgers was incorrect.

At discovery, the RPB-104 and RPB-105 source constructions remained in the repository, but their build-certified status was withdrawn until a direct build succeeded. No mathematical counterexample was asserted by this withdrawal. The corrected source is now certified by the new run in section 5, not by the original runs.

## 2. Initial correct-target repair snapshot

Validation branch: `validation/rpb106-pole-growth-audit`.
Validation PR: #20, based on the research branch rather than main.
Initial repair head: `82dcfd54706cc31a8f9c00cddcb4772af726804c`.
Initial correct-target run: `36801740183`; job `110177376381`.

The workflow explicitly checks out the PR head, prints source/toolchain hashes, builds `WeilDefect.Morphology.NeutralGaussianCutoffPairing` (including the cutoff dependency), and prints the transitive axioms of the three cutoff endpoint theorems. At this initial snapshot no success was claimed.

## 3. Source-pole recovery and attachment boundary

EXT-4 is pinned to Zhu, arXiv:2608.24827v2. The source's Lemma 6.1 and its proof resolve the two pole evaluations through `exp(x/2)` and `exp(-x/2)`, with opposite signs in even/odd parity coordinates. Source: https://arxiv.org/html/2608.24827v2#S6.SS1

For fixed coefficients A and B, the explicit function

```math
p(x)=A e^{x/2}+B e^{-x/2}
```

satisfies

```math
|p(x)|\le (|A|+|B|)e^{|x|/2}.
```

For a compact physical representative h, the implemented pole uses the coefficient pair

```math
M_s(h)=\int_{-c}^{c}h(y)e^{sy}\,dy,
\qquad
p_h(x)=M_{-1/2}(h)e^{x/2}+M_{1/2}(h)e^{-x/2}.
```

This is a concrete candidate with the source's parity structure. The code proves its moment integrability and growth; it does not reconstruct the source's entire compact-window explicit formula.

The existing `RightLimitWeilWeakRealizationPremise` accepts an arbitrary locally integrable `pole`. It does NOT assert that this pole is the concrete two-exponential function. Any constructor must either specialize the compact EXT-4 premise to that named function or require an explicit equality identifying it. Local integrability is not silently upgraded to exponential decomposition.

## 4. Actual compiler repairs

The correct-target build exposed real source defects that the previous unrelated green targets could not detect.

1. Run `36801740183` failed in `neutralGaussianCutoffScalar_one`: the bump's inner radius needed explicit reduction to 1. Repair commit `6db184934954ec0626eb3bc043674c8e6554bb3c` preserves its statement and all hypotheses.
2. Run `36802164341`, job `110178681501`, built the cutoff module and then exposed four API/tactic problems in the pairing module. The repair uses the actual indicator simplifier, factors the cutoff scalar before dominated convergence, normalizes the scalar norm, and uses eventual equality through `Tendsto.congr'`. The generic theorem still assumes only integrability of the product, not separate measurability of its second factor.
3. Run `36802741546`, job `110180459020`, built both repaired cutoff modules and failed at the real/complex exponential norm calculation in the new pole module. Commit `65b8ce1ddcdbcbc02c71bc3ffd9f0a0311e3bbe5` repaired that simplification. A conflicting duplicate write was rejected; the existing repair was preserved.
4. Run `36803078330`, job `110181497099`, built the cutoff, pairing, and pole modules. Its only remaining error was the assembly threshold normalization `8 * (1/2) = 4`. Commit `5a89b0771206d38dbdba426e39dea3a31e534ea8` repaired it. The subsequent same-source head `d9c0b171263862ed088620597f3d8d5ff7512278` superseded the cancelled run `36803446097`.

No mathematical hypotheses were strengthened to repair these compiler errors.

## 5. Final direct build certificate

```text
repository: monocap-tech/weil-lab
validation branch: validation/rpb106-pole-growth-audit
PR: 20
run: 36803460601
job: 110182696916
checked-out HEAD: d9c0b171263862ed088620597f3d8d5ff7512278
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
actual command: lake build WeilDefect.Morphology.NeutralGaussianAssembly
result: PASS (8947 build jobs)
```

Run evidence: https://github.com/monocap-tech/weil-lab/actions/runs/36803460601/job/110182696916

Exact source blobs printed by that runner:

```text
NeutralGaussianCutoff.lean:
1cbe03541d4521026205de8475f78a733e62abe0

NeutralGaussianCutoffPairing.lean:
1accc07c182e5348212734f0b00cdf676a02b164

NeutralWeilPoleGrowth.lean:
2c1b440bb7b8c32dcde58ac5addc0fbbeab607a2

NeutralGaussianAssembly.lean:
01ce40bffd08cf73eb7d70e70f544ff479bfb4ce
```

The subsequent `#print axioms` check printed exactly `[propext, Classical.choice, Quot.sound]` for each of these six endpoints:

```text
movingGaussianFilteredModeCompactCutoff_tendsto
movingGaussianFilteredModeCompactCutoff_residual_pairing_tendsto
movingGaussianFilteredModeCompactCutoff_pole_pairing_tendsto
neutralWeilExponentialPole_norm_le
neutralWeilSourcePole_growthData
rightLimitWeilGaussianAdmissibility_sourcePole
```

No `sorryAx` or project axiom appeared in those dependency closures. The repository's declaration rejection gate also passed. Imported assumptions remain explicit parameters; this axiom audit does not establish those external mathematical assumptions.

This certificate covers the named target and its transitive imports. It is not a claim that every unrelated project module or the root aggregate was rebuilt in this run. The validation-only workflow is not part of the research-source promotion.

## 6. Certified construction delivered

`NeutralWeilPoleGrowth.lean` now provides the two-exponential pole, the concrete compact-carrier moments, their integrability, and `NeutralPoleExponentialGrowthData` for the named `neutralWeilSourcePole carrier`. Its growth rate is 1/2 and its growth constant is the sum of the two coefficient norms. The pole-side Gaussian completion condition therefore becomes `4 ≤ R * (residual.a - c)`.

`NeutralGaussianAssembly.lean` now supplies:

```text
rightLimitWeilGaussianCutoff_of_growth
rightLimitWeilGaussianAdmissibility_of_growth
rightLimitWeilGaussianAdmissibility_sourcePole
```

The first constructor assembles every field of the actual cutoff premise from the Gaussian Schwartz realization, the repaired cutoff topology theorem, the repaired ordinary-integral limits, and explicit growth data. The second derives Gaussian admissibility through the existing compact-test limit constructor. The third instantiates growth with the named two-exponential source pole.

The Gaussian weak identity is derived, not added as a new premise. However, the last constructor explicitly requires:

```lean
hEXT4 : RightLimitWeilWeakRealizationPremise
  c carrier residual hSymbol (neutralWeilSourcePole carrier)
```

along with `hc`, `hR`, and the existing large-R conditions. This is `LEAN-CERTIFIED-FROM-IMPORTED-PREMISE` for the downstream admissibility deduction, not Lean reconstruction of EXT-4 or EXT-5D.

## 7. Effective burden ledger

```text
A. actual moving filtered mode as SchwartzMap: CERTIFIED
B. compact cutoff and full Schwartz convergence: CERTIFIED AFTER RPB-106 REPAIR
C. residual ordinary-integral cutoff limit: CERTIFIED AFTER RPB-106 REPAIR
D. pole ordinary-integral cutoff limit: CERTIFIED WITH EXPLICIT GROWTH DATA
E1. named concrete two-exponential pole growth: CERTIFIED
E2. identify the imported/project EXT-4 pole with that named pole: STILL EXPLICIT / OPEN
Assembly from the exact compact EXT-4 witness: CERTIFIED CONDITIONAL CONSTRUCTOR
Logarithmic coercivity: NOT STARTED
```

Thus the technical growth-and-assembly construction is complete, while the actual witness attachment must not be erased from the dependency chain. The earlier slogan that only a growth estimate remained was incomplete at the interface level.

## 8. Next cursor

```text
RPB-107 / WD-T40 F-4
CONCRETE EXT-4 POLE ATTACHMENT + TEST-DUALITY AUDIT
```

First recover the concrete compact EXT-4 witness or the exact equality relating its pole to `neutralWeilSourcePole carrier`, retaining the source's coefficients, signs, and Fourier convention.

Then check the duality of the Gaussian test before using its weak identity as an energy identity. The current distribution pairing is bilinear in test and residual; a Hermitian Fourier energy requires the appropriate conjugation/reflection. A phase-scaling check distinguishes alpha-squared scaling from absolute-alpha-squared scaling. This is a required audit, not a claim that a corrected energy identity has been proved or disproved.

Do not begin logarithmic coercivity until these attachments have been made explicit. Do not restart the certified Gaussian seed or cutoff constructions, and do not treat the original wrong-target green runs as certificates.
