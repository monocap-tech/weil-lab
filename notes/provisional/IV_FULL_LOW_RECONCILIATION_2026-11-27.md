# Phase IV original full-low composition — focused reconciliation

**Date:** 2026-11-27 Pacific / 2026-11-28 UTC. **Status:** research gate and evidence audit, not a new theorem, Lean receipt, acceptance decision, or RH claim. **Active focus:** the primary Phase IV target in [#193](https://github.com/monocap-tech/weil-lab/issues/193#issuecomment-7083442300). Other programme lanes remain historically intact but are not advanced in this pass.

## Exact object and evidence grades

Work on the original complex, first-slot-antilinear signed Weil form on `I=(-11/10,11/10)`, with the NF599 Gamma source, both-sign true von Mangoldt shifts `n=2,3,4,5,7,8,9`, and both crossed Mellin poles. No positive surrogate, graph-plus-mass proxy, or source-free projection may replace it. The underlying source identification, Gamma physical inverse, logarithmic form completion, sharp-cell domain, and smooth density require their own source-attached proof.

| Input | What the cited record actually supplies | Unpaid before admission |
|---|---|---|
| [IV046](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7059883201) | Classical signed source Dirichlet rewrite and four exact-rational 16-cell *upper* variational trials; even low trial reported `0.00839320<W[v]/||v||²<0.00862610`. | No lower full-sector sign, Gamma/form-domain Lean bridge, or inverse receipt. |
| [IV047](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7060072772), [IV051](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7063454686) | Analytic original high compression on the 100,000-cell zero-mean complement, strengthened to `W[q]>(49/100)||q||²`; exact arithmetic preflights, not a kernel certificate. | Full low block and its mixed correction. |
| [IV048](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7060435637), [IV049](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7063138188), [IV050](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7063240617) | True mixed block does not vanish with mesh refinement; sparse-column energy bounds do not control dense low vectors. IV050 gives a dense but coarse `||QWΠ||<341/10<35`. | With only `c>49/100`, the resulting `35²/c` correction upper budget is nearly 2500, far too coarse to decide the small IV046 low trial. |
| [IV052](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7063663296), [IV053](https://github.com/monocap-tech/weil-lab/issues/826#issuecomment-7063774358) | Analytic dense jump estimate `||QWv||<25||Δa||+(2w/3)||v||`; a *joint two-low plus entire high* positive class. The printed conservative determinant is exactly `73541319/48995000000000>0`, independently recalculated here with Python `Fraction`. | Remaining 99,998 low directions and their complete Schur interactions. The source reports/checkers are now copied byte-for-byte into [the native packet](iv_sources/README.md), but not independently recompiled as Lean by this pass. |

The historical #834 blanket hold expired; its **lineage-specific fan-out and source-manifest controls** still apply. This pass adds no Lean source or Actions dispatch and does not rely on a green workflow for a source-level claim.

## The theorem-shaped fixed-window gate

Let `D` be the source-matched closed logarithmic form domain of supported tests, subject to proof of its identity with the original source form and smooth-core density. For `M=100000`, let `L=ran Π_M` be all physical-cell indicators and `H=ker Π_M`. First prove `D=L⊕(D∩H)` in the **form** sense. For each `v∈L`, the functional `q↦W(q,v)` must be continuous in the positive high energy norm `W[q]^(1/2)`; denote its high Riesz representative by `t_v`, so `W(q,t_v)=W(q,v)` under the fixed slot convention. Then define the complete effective form

`S(v)=W[v]-W[t_v]`.

If the stated domain, continuity, source and positivity hypotheses hold, completing the square gives `W[v+q]=S(v)+W[q+t_v]`. Thus **full fixed-window nonnegativity is equivalent to `S(v)≥0` for every `v∈L`**. This form statement does not assume a bounded inverse of an unbounded Gamma operator. Where an actual operator inverse is justified, it agrees with the familiar `A−B* C^(-1)B`. Every coefficient, prime phase, Gamma seam, pole and high correction remains in `S`.

This is a *conditional reduction*, not a sign certificate. The next mathematical result must be either (a) a reproducible source-faithful lower bound for the **complete** low effective form, (b) a genuine negative original-form witness, or (c) a precise obstruction to the proposed bound with a better testable estimate. A separate arbitrary-support exhaustion/domain extension is required even after a fixed-window sign result.

## First falsifiable diagnostic: the aligned IV046 even trial

Each of IV046's 16 coarse cells has width `11/80`; each IV053 fine cell has width `11/500000`. Their exact ratio is **6250**, so every 16-cell piecewise-constant trial lies in the very same `L=ran Π_100000`. Take the normalized IV046 even vector with left-half coefficients `[189,390,574,738,846,964,1000,989]` and reflected right half. Its reported source-rational low energy is positive but small. Test an explicit `q∈D∩H` with exact original `a=W[v]`, `b=W(v,q)`, `c=W[q]>0`, including all source terms and interval errors.

- If `a<0`, `v` is already a negative form witness (after the required smooth form-core transfer).
- If `|b|²>a c`, minimizing `W[v+zq]` over complex `z` gives a **negative original signed-form witness**. With `||v||=1`, the reported upper bound `a<0.00862610` supplies a useful sufficient comparison, but it must be redone with exact outward rational endpoints and the same source revision.
- If the tested direction does not cross the threshold, it is **inconclusive** about both `S(v)` and the other 99,999 low directions. To prove positivity even on this one `v`, bound the supremum over **all** high `q`, not just one contrast.

The IV048 single-cell contrast is a proof that mixed interactions matter, but it is attached to another low vector; its loss cannot be subtracted from this IV046 trial without computing their actual original mixed pairing. The 16-to-100,000 alignment and the IV053 rational determinant were checked in this pass; no source checker, full Gram, high inverse, or fresh Lean run was executed.

## Next controlled operation

The [IV046–IV053 native packet](iv_sources/README.md) now contains 11 exact-SHA checker scripts, eight reports, eight historical JSON receipts, a README and a SHA manifest. All 29 retained files were read back from the branch; the IV053 preflight replayed PASS locally from the exact dependency chain. Recheck the signed source identity and form-domain compatibility at exact commits. Then design one source-correct high response for the aligned IV046 trial and interval-enclose its `2×2` determinant. A positive or inconclusive diagnostic only narrows method choice; the full low gate remains open. Before any heavy compiler submission, audit the selected branch's actual PR-trigger fan-out and source preflight ordering.
