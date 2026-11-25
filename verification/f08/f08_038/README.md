# F08-038 — original native complex L² dilation: strong-continuity transfer from a dense class

**Uncompiled source-only candidate until true frozen IV023 Lean 4.34.0 compiler PASS.**

This one-declaration gate proves a conditional *functional-analytic transfer*, not the full analytic continuity theorem. For the exact original `RealComplexL2` nonzero-frequency dilation `Uλ`, if a given subset `s : Set RealComplexL2` is dense and `Uλg→g` at λ→1 for every `g∈s`, then `Uλk→k` for every original `k : RealComplexL2`. The true nonzero scale parameter is a subtype; no arbitrary definition at λ=0 is required. The proof combines actual Mathlib `Dense.exists_dist_lt` and `Metric.tendsto_nhds` with the **independently accepted** F08-035 original exact source-native inequality `‖Uλk-k‖≤2‖k-g‖+‖Uλg-g‖`.

### What this does not prove
It does **not** prove its compact-core convergence premise `Uλg→g`. The latter requires actual original Schwartz-to-Lp a.e. identification and dominated convergence on a common bounded interval, and F08-037's still-unaccepted original native compact Schwartz dense-image theorem. Neither weighted/logarithmic strong continuity nor physically compactly supported smooth form-core density follows automatically. The complete original smooth signed Weil mixed-form identity, source extension, F42 global positivity and RH remain open.

Pinned original research `614ba879f7389fdb620c474adaee273b00eac71c`, canonical original domain `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`, Lean `v4.34.0`. Predecessor F08-027/029/030/033/035 genuine source blobs must be pinned and staged in the original research build; one exact named strict ordinary-only axiom report and separate original compiler artifact are mandatory. Separate hosted custody still required after compiler PASS.

Parent research ledger #932, master ledger #898.
