# NF663 — genuine physical real Gram entries to exact integer transformed balls

## Recovered source and CI standing

- NF658 corrected replay **44434056814**: full workflow **SUCCESS**, including exact 120 original physical compact entry containments and final standard-axiom audit.
- NF659 **44430374282**: full workflow **SUCCESS**, including generic real congruence interval transfer, all 225 transformed integer centers, all 225 radii, 15 positive margins, and exact coercivity gate.
- NF661 **44435792632**: the genuine `neutralNF661PhysicalH` and quantitative generic surjective-map coercivity module built. The overall workflow failed later in the NF660 finite-dominance module. That goal was repaired in NF662; the NF660/NF661 retry jobs remained queued at the last inspection.
- NF662 initial run **44437951716** was in progress at the last check, and newer NF662 **44438029711** was pending. None of the NF662 generated 225-entry source-to-real membership targets has yet been claimed as a kernel PASS.

## New NF663 generic scaling mathematics

Committed `ActualZetaOriginalPhysicalGramIntegerRealScale.lean`.

For an arbitrary finite index set `Fin n`, integer preconditioner `k`, integer centers `c`, integer errors `e` and positive real scale `S`:

- Exact transformed integer centers: `T_ij = ∑p∑q k_ip k_jq c_pq`.
- Exact transformed integer radii: `U_ij = ∑p∑q |k_ip k_jq| e_pq`.
- For any *actual real* H with `|H_pq - c_pq/S| ≤ e_pq/S`, set `B=(k/S) H (k/S)^T`.
- Candidate Lean theorem:

`|B_ij - (T_ij : ℝ)/S^3| ≤ (U_ij : ℝ)/S^3`.

The proof reuses NF659's accepted **real** double-sum interval transport lemma, not a numerical approximation or inferred eigenvalue. The denominator `S^3` is essential: two preconditioner factors plus the compact physical-entry scale.

This generic theorem and its `Int.cast_sum`, radius-absolute-value, and finite-sum scale proofs are **Lean pending**.

## Exact authentic 15-generator attachment

Added `scripts/emit_nf663_original_real_scale_gates.py` to generate 15 bounded Lean row modules plus a terminal completion module.

Each of 225 center proof targets cites its actual accepted `nf659Cxx_yy` theorem; each of 225 radius targets cites `nf659Rxx_yy`. The final physical theorem consumes:

1. NF662's actual integral matrix `neutralNF661PhysicalH`, indexing exactly 0..13 and pole 241.
2. NF662's 225 compact physical-ball membership theorems, built from the original NF658 physical enclosures and symmetry rather than a replacement matrix.
3. The new generic exact `S^{-3}` scale lemma and NF659's certified integer double sums.

Target:

`∀ i j : Fin 15, |(K H_I Kᵀ)_ij - (nf659CenterAt i j : ℝ)/10^192| ≤ (nf659RadiusAt i j : ℝ)/10^192`,

where `K = nf658Kints/10^64`.

The new two-job workflow checks the generic theorem independently and rebuilds the original exact pinned source artifacts for the full 450 reused gates and actual physical transformed-real attachment. It audits standard Lean axioms. All NF663 new theorems are **compiler pending**.

## What remains after successful NF663 acceptance

1. Combine the *real* transformed entry bounds with NF659's fifteen positive integer dominance margins to establish `yᵀ(K H_I Kᵀ)y ≥ (minMargin / 10^192)‖y‖²` in Lean (NF660 generic theorem must first pass).
2. Prove the actual rational lower-unit-triangular preconditioner is invertible/surjective and obeys `‖Kᵀ y‖² ≤ (kn/10^128)‖y‖²`. It is insufficient just to assume these hypotheses in the generic NF661 theorem.
3. Apply the already certified integer inequality `minMargin*10^60 > 10^64*kn` to close `xᵀH_I x ≥ 10^-60‖x‖²` for the **actual original 15-source physical block**.

The full 242-source physical matrix, global signed Weil positivity and RH remain **OPEN**. This is a draft stacked against NF662, not a main merge.
