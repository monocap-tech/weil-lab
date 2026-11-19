# NF673 — original 242-source triangular H entry custody and Phase III terminal bridge

## Distinguish kernel mathematical soundness from source-specific numerical truth

The outstanding Phase III original-source result is already available
conditionally in `neutralNF625OriginalPhysical_strict_of_checks`
and `neutralNF626OriginalPhysical_of_fast_checks`. Their hypotheses are
**real** computational obligations, not ambient axioms:

- valid original moment bank and source-wide index coverage;
- true H and V entry interval widenings from authentic analytic integrals;
- checked integer center cache tied to the SAME original frame/data;
- true uniform defect/residual and all 242 selected-box payments.

NF673 does not silently close any of these. It changes the entry gate's
mathematical verification workload without changing its semantics.

## Original physical H symmetry is already a Lean theorem

`neutralNF606PhysicalH_symm` was proved from the genuine real integral,
not from a precomputed matrix, and used in NF658/669.

The previous `neutralNF625EntryCheck` performs 242×242 = **58,564**
H comparisons and 242×4 = **968** mixed V comparisons.

The new `neutralNF673EntryCheck` instead checks

1. **29,403** lower-triangle H interval widenings (`j ≤ i`);
2. exact rational symmetry of the proposed original H center matrix,
   `H0[i,j]=H0[j,i]` (58,564 inexpensive, finite rational equality tests);
3. all **968** existing mixed V interval widenings.

For `i<j`, the generic proof derives H membership from the actual
integral symmetry, checked center symmetry, and the accepted reversed
lower-triangle widening; it never postulates symmetry of the external
numerical approximations.

This saves **29,161** expensive H-ball comparisons in the eventual full
original numerical attachment. It does **not** reduce the original
242 selected payments, moment-bank coverage obligations, or original
analytic moment proof requirements.

## New proposed Lean module

`WeilDefect/Arithmetic/ActualZetaOriginalPhysicalTriangularEntryCustody.lean`:

- `neutralNF673EntryCheck_sound`:
  source-wide original NF624 moment validity + reduced Boolean receipt
  implies ALL 58,564 true physical H bounds and 968 V bounds.
- `neutralNF673OriginalPhysical_of_triangular_fast_checks`:
  feeds those bounds into the existing NF625 real rational payment theorem,
  reusing exactly the NF626 checked integer cache/fast payment theorem.
  It targets existence/uniqueness of the physical solve AND the exact
  242-coefficient frozen-box containment.
- `neutralNF673OriginalPhysical_strict_of_triangular_fast_checks`:
  feeds the authenticated box into the established NF610 original
  signed-Weil carrier theorem and preserves its **strict corrected 2/5**
  margin, smooth approximants, and exact moment transport.

ALL THREE are currently **proof candidates**, not kernel-certified
NF673 claims. Their hypotheses must not be erased.

## Pinned source audit

`scripts/audit_nf673_original_triangular_centers.py` authenticates the
unchanged NF631 widened original entry artifact
`14459025571` by the recorded archive SHA256
`e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9`.
It verifies the source schema, manifest digest, 242 ordered rows,
exact 29,403 lower H centers/radii, 968 mixed entries, nonnegative radii,
and the precise center-symmetrization layout. The external source audit
cannot certify analytic H/V containments or the Lean Boolean checks.

## Compiler gate

`.github/workflows/nf673-original-triangular-custody.yml` contains two
independent jobs:

1. Lean-build the generic soundness and *conditional* strict original
   carrier theorem, auditing only standard axioms.
2. Validate original pinned NF631 center layout and manifest SHA with
   independent integer-only Python parsing.

No CI success is claimed until these jobs complete successfully.

## Phase III remaining truth obligations

A complete *unconditional* Phase III terminal theorem still needs
the actual original data to satisfy the five Boolean conditions:
`hbank`, `hcov`, `htri`, `hcache`, `hpay`.
The NF621/NF631 external arithmetic pays these numerically; the
Lean checker must establish each actual literal gate using the
pinned original archives and source-derived analytic moments.

The additional NF670–672 full physical Gram/Schur work is NOT
an automatic Phase III exit prerequisite. Its compiler jobs were queued
when NF673 was started.

Strict positivity of this ORIGINAL signed Weil carrier, even once
fully certified, is not global Weil positivity and does not prove RH.
