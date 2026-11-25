# IV098 — source-only staging

Base commit: d104f814b2871916398ad977b8d2db8f16950fb5 (IV097). Consolidates issue #935 comments 7150555019, 7150577680, 7150704451. Exactly 24 named theorem candidates; no placeholders in module. Static source check only; no Lean invocation or receipt. The workflow template is intentionally under notes/provisional, not .github/workflows. Activate on research/iv098-original-reflected-collar-sector-gate only after upstream verification and review; the staging branch must not be merged or adopted. Any repaired IV097 base requires source reattachment. No global positivity or RH claim.

Terminal declarations: Pair_margin, Pair_cutoff8944, Pair_cutoff20000, Pair_mass_zero_iff. The zero pair is included, and all mixed signed Weil terms remain in the original finite diagonal. The audit uses explicit names, permitted foundational axioms, fresh native .olean, and SHA-256 source/output binding.

## Repaired dependency and activation custody

- Original staging baseline: IV097 d104f814b2871916398ad977b8d2db8f16950fb5 (superseded for activation).
- Repaired IV097 head: bac3713058e76d7b979685556c9b8f27b68e181d; blob f8867fd4d93a8d24a389bc020e8714b74638bd82.
- Repaired IV096 blob: 79acb8066d49fc2263dda4f8977474a6079c7f49; dual native PASS.
- Repaired IV098 module: eb56c610984851b5bfeddce0a7ca4212b52aa80d at staging commit 3cfa825c2e8d1e056af4c6a9741e2b71479152de.
- Complete recursive source-tree audit: repaired IV097 head and staging share all 628 tracked Lean/build-configuration blobs; staging adds only IV098 within that scope. See issue #935 comment 7153010914.
- IV097 PR receipt: run 45546751224, job 138978099838, 9268 build jobs, fifteen strict named axiom receipts PASS; artifact 14991957926, SHA256 563d4b72b75bdf7e04ce2f92358b8e1bfbc15534e717eb53075fe2e7dc7a67fb. See issue #935 comment 7153136993.
- IV097 push receipt: run 45546755058, outstanding at this snapshot. Do not treat the first receipt as dual acceptance.
- Rechecked source declarations, print-axiom entries and both workflow name lists: exact matching 24 names, no placeholders in the source.

Activation procedure: after successful audit of the IV097 push receipt, verify the current staging source identities, create research/iv098-original-reflected-collar-sector-gate from the staging head, install the reviewed template at .github/workflows/iv098-original-reflected-collar-sector.yml, and open a draft PR against research/iv097-original-smooth-plateau-gate. Record exact activation commit and push/PR workflow IDs. No adoption, merge or claim of global positivity follows from activation or a restricted sector receipt.
