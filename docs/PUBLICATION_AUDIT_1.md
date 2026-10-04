# PUBLICATION-AUDIT-1 — canonical status reconciliation

Base publication branch: `publication/preprint-audit`  
Reconciled live research snapshot: `936e723ac9c22592f9fb0901f2f25bbf238227c2`

## Result

The publication-control inconsistency identified in PUBLICATION-AUDIT-0 is
resolved by adding [PUBLICATION_STATUS.md](PUBLICATION_STATUS.md) as the sole
current publication-status authority.

Historical status files remain unchanged as provenance/evidence surfaces.

## Reconciliation rule

Current publication status is resolved by axis, not by whichever summary file
has the strongest wording:

1. **formal certification** — exact declaration map in `LEAN_STATUS.md`;
2. **mathematical standing / H1-P4 audit** — `THEOREM_LEDGER.md`;
3. **public name / dependency role** — `PUBLIC_THEOREM_INDEX.md`;
4. **post-Horizon actual-zeta certification** — live RPB-108 notes and modules.

This prevents phase-completion language from silently promoting a theorem's
formal status.

## WD-T40 determination

The exact formal declaration map controls.

Therefore, at this snapshot:

- mathematical standing: **INTERNAL-PROOF / CONDITIONAL on WD-T38 hypotheses**;
- audit standing: **P4-AUDIT-PASSED**;
- formal standing: **LEAN-BLOCKED**.

The current formal blocker is the source-faithful polarization/complexification
of EXT-4 into the required compact-test operator identity and cutoff extension
to the Hermitian Gaussian dual test.

Earlier summary language saying `LEAN-H1 EXHAUSTED` or that Horizon 1 is
complete is treated as package/handoff history, not as an override of this
exact theorem-level formal status.

## Stable theorem ledger

PUBLICATION_STATUS now contains a reconciled WD-T01–WD-T40 table with separate
columns for:

- public theorem name;
- mathematical standing;
- audit/source status;
- Lean status;
- dependencies;
- manuscript role;
- Lean declaration custody.

No theorem is upgraded by this reconciliation.

## Live RPB-108 separation

Post-Horizon RPB-108 results are deliberately kept outside the stable WD ID
namespace for now.

The publication authority lists as certified infrastructure:

- actual-zeta zero/divisor custody;
- actual growth / explicit-formula transport;
- logarithmic/source carriers;
- actual Green graph and packet-density construction;
- graph analysis and copy observability;
- carrier factorization;
- finite background tests;
- mixed background Gram obstruction.

These may enter manuscript exposition, but stable public theorem IDs should not
be assigned until the live family boundaries stop moving.

## Current P0 publication blockers

The authority preserves four live blocker classes:

1. **actual unshifted background sign**;
2. **retained same-vector WD-T38 attachment**;
3. **central cancellation / transport completion**;
4. **AZ-NEXTJET-LOC and C-ACTUAL-KPH-FLOOR**.

No manuscript top claim may pass these blockers by inference from surrounding
infrastructure.

## Archive consequence

The archive now has a clean status model:

[
	ext{historical ledgers/evidence}
longrightarrow
	ext{PUBLICATION_STATUS reconciliation}
longrightarrow
	ext{manuscript claims}.
]

Automated paper generation must consume PUBLICATION_STATUS, not independently
scrape PROOF_STATUS, PUBLIC_THEOREM_INDEX, or LEAN_STATUS.

## Next cursor

[
oxed{	exttt{PUBLICATION-AUDIT-2 / DECLARATION-TO-FILE + CERTIFICATE MAP}}
]

Next required outputs:

1. resolve each stable WD theorem to its exact Lean source file(s);
2. attach exact validation commit/run evidence to each publication row;
3. do the same for the RPB-108 theorem families intended for manuscript use;
4. identify imported declarations that are wrappers around external premises;
5. produce the machine-readable theorem manifest that the manuscript and
   eventual Prove2Me/archive pipeline can consume.

This is the last major metadata-normalization pass before prose extraction can
begin safely.
