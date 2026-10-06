# RPB108: independently audited 91/100 enclosure pairing repair

Base custody: `266834ce6d58a8979679b9e2b724a1720a08fa29`.
Definitions: [enclosure pairing](../docs/TERMINOLOGY_RPB108_PAIRING_ENCLOSURES_091.md).

The first failed source-only guard is (i,j)=(1,83): maximal endpoint difference approximately 2.6556762858e-38, source allowance approximately 2.5868524593e-38, and native interval width approximately 5.3113250538e-38. The native enclosure width accounts for the apparent discrepancy; no source coefficient, source-map allowance, native entry or residual correction changes.

An independent integer-Hankel recomputation of the rational endpoint-log projections checks all 7,056 pairings from the complete saved contractions. Exactly (1,83) fails the historical source-only endpoint-difference guard. Every interval gap is strictly below the original source allowance; every endpoint difference is below the allowance plus both enclosure widths. All 7,056 displaced-pair controls reject. The two independently generated checkpoint audits reproduce byte for byte.

The repaired post-contraction guard retains both explicit tests. This is numerical consistency validation alongside the independent source approximation proof, not a derivation of that approximation from overlapping intervals.

The complete nine-panel recovery checkpoint is now stored as `notes/data/RPB108_PRIME5_GRAM84_091_COMPLETE_PANEL_CHECKPOINT_20261006.json.gz`; decompress it to obtain exact JSON SHA256 `0bd01b91366b8944f52489db10f0b886b0e694e921a1257cbc6b0910311c1ddf`. The independently produced primary and repeat checkpoint files were byte-identical. The strict resume wrapper verifies the original constructor hash, unchanged complete contraction byte prefix and every remaining input binding before finalization. It does not accept altered contraction code or altered native/source inputs.

Two repaired finalization runs are pending. The independent stored corrected-sign/conversion validator is prepared but no unfinished result is accepted. Whole-domain positivity remains certified through 9/10. Global endpoint exclusion, historical attachment, F4 and FULL TRANSPORT CLOSED remain open.
