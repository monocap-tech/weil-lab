# RPB-108 — actual reflected Mellin identity and factorial envelope (2026-10-03)

Parent promoted head: `f2191a1e7b2335d13b086c95285ab97698b17238`.

### RPB-108: actual reflected Mellin identity and factorial envelope (2026-10-03)

Mathlib's actual modified zero-parameter theta kernel is identified with
the large-t tail plus its t^(-1/2)-weighted inverse. Both pieces are
Mellin-convergent, and completedRiemannZeta₀(z) is exactly half the sum
of the two actual tail integrals at z/2 and (1-z)/2.

The actual completed term is bounded by the existing factorial moment
bound on every natural-radius disk. Pole clearing gives the actual
entire-function majorant
A_n = n(n+1) C n!/(p/2)^n exp(-p/2)/(p/2) + 1.
For 2(|T|+2) ≤ n, the actual circle envelope is at most A_n and the
actual height-window multiplicity count is at most log(A_n)/log 2.
Positive p and C come from the actual theta kernel; no divisor-count
or spectral-domain premise is supplied.

Next: choose a natural moment order proportional to |T|+1 and convert
log(A_n) into a uniform O((|T|+1) log(|T|+2)) cumulative count bound.
The logarithmic rate, local unit-height counts, bounded logarithmic-domain
sampling and full Weil-form extension are not certified by this chunk.

WD-T38 source/null attachment and enlarged central cancellation remain
open. Spectral L2 unproved and unassumed; threshold closed; F-4 pending.
RH standing unchanged.

See [actual Mellin representation and envelope](../notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_MELLIN_REPRESENTATION_20261003.md).


## Proof route

1. Extend the actual large-t theta remainder by zero outside (1,∞).
2. Identify its weighted indicator with the complex tail integrand.
3. Use the certified factorial tail bounds to prove Mellin convergence at every exponent.
4. Use the actual theta functional equation to identify the modified FE-pair kernel with the tail plus the t^(-1/2)-weighted inverted tail. At t=1 all three terms vanish.
5. Establish convergence of the reflected term via the pinned Mellin power substitution theorem.
6. Split the convergent Mellin integral, apply the pinned exponent shift and inversion identities, and retain the defining one-half normalization of completedRiemannZeta₀.
7. Apply the two actual tail bounds and triangle inequality to bound completedRiemannZeta₀ on natural-radius disks.
8. Bound |z| |z-1| by n(n+1) on |z|≤n and retain the added endpoint value 1.
9. Bound the actual circle supremum by the same majorant, normalized to at least one.
10. Feed the actual envelope bound into the certified actual multiplicity-weighted Jensen count bridge.

## Remaining cursor

The analytic identification and explicit factorial envelope are complete.
The next task is the scalar logarithmic conversion, including the natural moment-order choice, yielding a cumulative O(T log T) growth estimate. No local O(log T) unit-height density or sampling-conditioning statement follows merely from this cumulative estimate. Full sampling/form extension remains downstream.

No SOURCE traversal, threshold reopening or spectral operator-domain assumption enters this proof chunk. The existing WD-T38 attachment is not assumed.

## Validation

Exact candidate `4fc7534156b635a6c2c1ff5841398d0642e496a7` passed [run 37162369635](https://github.com/monocap-tech/weil-lab/actions/runs/37162369635), job `111318270964`. The isolated representation, factorial envelope and full `lake build WeilDefect` passed (3,206, 9,007 and 9,051 jobs). All eleven new theorem audits report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom gate passed.

The theorem source, root imports, terminology and proof notes are promoted separately from the validation workflow and validation dependency manifest. The runner saved the full compiled project/dependency tree and its root manifest under `rpb108-mellin-manifest-final-v1`. Reuse draft PR #35 and the existing validation branch for the next bounded scalar-growth chunk, synchronizing the promoted head before further import changes.
