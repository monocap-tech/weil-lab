# NF650 — retained artifact local custody audit PASS

NF649 staged head 4965a665236e1b0460996a16f0029c0032c85d1a, no additional PR. Relevant NF641–648 jobs and NF627 literal job remained queued at initial inspection; no additional kernel result. Do not multiply automatic workflows while backlog remains.

## New actual evidence (executed locally, not speculative CI)

The GitHub artifact download connector is available. Downloaded seven actual ZIPs into the execution environment; checked their SHA-256 against the recorded GitHub artifact digests. Executed a standalone exact Python replay on the downloaded original bytes. Committed a reproducible copy of the audit, with archive-directory argument substituted for the local path, and its observed report. No generated Lean was compiled locally (Lean/lake unavailable).

| Archive | Artifact ID | Local filename |
|---|---|---|
| NF621 shard 0 | 14443955726 | nf621-shard0.zip |
| NF621 shard 1 | 14443029185 | nf621-shard1.zip |
| NF621 shard 2 | 14442993898 | nf621-shard2.zip |
| NF631 widened entries | 14459025571 | nf631-widened.zip |
| NF632 complete pi proposals | 14458696200 | nf632-pi.zip |
| NF635 full endpoints | 14462990552 | nf635-endpoints.zip |
| NF638 integer table pilots | 14464939237 | nf638-pilots.zip |

All seven archive hashes, 275 manifest-listed file hashes, and shared eight-shard digest inventories agree. Actual compressed shard bytes checked for three shards only (0,1,2), containing all four required canonical keys. Actual pi literal from the accepted NF632 chain equals the retained NF635 pi JSON and Lean Banks literal. All 1281 endpoint coordinate tuples match their corresponding generated Lean literals in stored order (serialization equality, not reference evaluation). Ten leaves needed for the local Gram block independently replayed at full 1200 terms and exactly match retained endpoints. Three NF638 integer caches (36 coordinates) and 42 actual row tuples match the retained shard records. All 56 original moment rows including the negative-real mixed key satisfy exact residual fee, with zero-radius mutations rejected. All 120 widened physical Gram coordinates from the actual NF631 archive reproduce original centers and exact minimal widening computed from external and reference rounding; one-unit radius underpayment rejected for all 120. Maximum 1861198149186/Q. 480 signed source queries consumed, exact zero branch included. Actual byte audit and arithmetic only; no new kernel closure. Source indices and coefficients are the isolated original source block audited NF649, hardcoded in standalone audit.

Reproduce:
`python scripts/verify_nf650_retained_local_data.py /path/to/archives`

## Scheduling
No PR opened, no new automatic workflow, no existing run cancelled. This establishes actual local-data reconciliation while CI is saturated. Next: use downloaded artifacts to test actual emitted Python code and focused repairs before any new PR; recover compiler results. Full endpoint reference identities, local literal Gram proof, whole numerical solve custody, global Weil positivity and RH remain open.
