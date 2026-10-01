# RPB-106 — actual pole growth and prerequisite certification repair

**Date:** 2026-09-30 (America/Los_Angeles)
**Research base:** d1f633a40afec05a8a5eba2456d16a36423cf15a
**Status:** IN PROGRESS — RPB-104/105 certificate claims superseded pending correct-target validation.

## 1. Recovered validation defect

The recorded RPB-104 validation head `8e8cf915220bf5bff355d4df006b3c18b926a780` and RPB-105 validation head `646adabb7d5423b4eafbd388150a6d0cd0cba2f8` both contain workflow blob `f194e9564577d3b79831b7abfb91b5933f3af98f`.

Its build command is:

```text
lake build WeilDefect.Examples.WeakCriticalFallthrough
```

It is NOT either named cutoff target. The attempted target replacements were no-ops. Runs `36800396833` and `36801083567` therefore do not certify `NeutralGaussianCutoff` or `NeutralGaussianCutoffPairing`. Their green statuses remain historical facts; the scope attributed to them in RPB-104/105 and the status ledgers was incorrect.

The RPB-104 and RPB-105 source constructions remain in the repository, but their build-certified status is withdrawn until a direct build succeeds. No mathematical counterexample is asserted by this withdrawal.

## 2. Correct-target repair

Validation branch: `validation/rpb106-pole-growth-audit`.
Validation PR: #20, based on the research branch rather than main.
Initial repair head: `82dcfd54706cc31a8f9c00cddcb4772af726804c`.
Initial correct-target run: `36801740183`; job `110177376381`.

The workflow explicitly checks out the PR head, prints source/toolchain hashes, builds `WeilDefect.Morphology.NeutralGaussianCutoffPairing` (including the cutoff dependency), and prints the transitive axioms of the three cutoff endpoint theorems. No success is claimed yet.

## 3. Source-pole recovery

EXT-4 is pinned to Zhu, arXiv:2608.24827v2. The source's Lemma 6.1 and its proof resolve the two pole evaluations through `exp(x/2)` and `exp(-x/2)`, with opposite signs in even/odd parity coordinates. Source: https://arxiv.org/html/2608.24827v2#S6.SS1

For fixed coefficients A and B, the explicit function

```math
p(x)=A e^{x/2}+B e^{-x/2}
```

satisfies

```math
|p(x)|\le (|A|+|B|)e^{|x|/2}.
```

For a compact physical representative h, the source operator has the natural coefficient pair `A = integral h(y) exp(-y/2) dy`, `B = integral h(y) exp(y/2) dy` over its support. Formal growth and assembly code is being prepared; it is not yet certified.

The existing `RightLimitWeilWeakRealizationPremise` accepts an arbitrary locally integrable `pole`. It does NOT assert that this pole is the concrete two-exponential function. Any constructor must either specialize the compact EXT-4 premise to that named function or require an explicit equality identifying it. Local integrability is not silently upgraded to exponential decomposition.

## Current cursor

```text
RPB-106 / WD-T40 F-4
CORRECT-TARGET CUTOFF CERTIFICATION REPAIR
THEN EXPLICIT SOURCE-POLE GROWTH + CONDITIONAL ASSEMBLY
```

Do not enter logarithmic coercivity. Preserve this correction additively; do not rewrite the historical run results as if the original targets were correct.
