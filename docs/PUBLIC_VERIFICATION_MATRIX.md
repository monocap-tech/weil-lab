# Public Verification Matrix

## H1-P5.2 — Mathematical standing, Lean status, and source custody

This matrix is intentionally orthogonal to the main mathematical narrative.
It prevents internal deductions, imported premises, examples, scope rules,
and open RH-facing interfaces from being collapsed into one notion of
"proved."

### Stable theorems

| Stable ID | Mathematical standing | Lean status | Imported premise ancestry | Direct/source pin | RH-facing dependency |
| --- | --- | --- | --- | --- | --- |
| WD-T01 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T02 | INTERNAL-PROOF + IMPORTED Douglas | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-1 | — |
| WD-T03 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | — |
| WD-T04 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | — |
| WD-T05 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | — |
| WD-T06 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T07 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T08 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T09 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T10 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | — |
| WD-T11 | INTERNAL-PROOF | LEAN-CERTIFIED | Transitive | via WD-T03/WD-T02 | — |
| WD-T12 | INTERNAL-PROOF | LEAN-CERTIFIED | Transitive | via WD-T10/WD-T02 | — |
| WD-T13 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T14 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T15 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T16 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T17 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T18 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T19 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T20 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T21 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T22 | IMPORTED + SPECIALIZED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-2A | — |
| WD-T23 | IMPORTED/DERIVED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-2B | — |
| WD-T24 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T25 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T26 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T27 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T28 | INTERNAL-PROOF + imported zero count | LEAN-CERTIFIED | Direct | EXT-3 | — |
| WD-T29 | INTERNAL-PROOF | LEAN-CERTIFIED | Transitive | via WD-T28 | — |
| WD-T30 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T31 | INTERNAL-PROOF + imported zero count | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-3 | — |
| WD-T32 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T33 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | — |
| WD-T34 | DERIVED from IMPORTED compact-window formula | LEAN-CERTIFIED | Direct | EXT-4 | — |
| WD-T35 | DERIVED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-4, EXT-5 | — |
| WD-T36 | INTERNAL-PROOF/SHARPNESS | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T35 | — |
| WD-T37 | CONDITIONAL COMPOSITE | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T31 and other imported ancestry | AZ-NEXTJET-LOC; C-ACTUAL-KPH-FLOOR is stronger refinement |
| WD-T38 | CONDITIONAL COMPOSITE | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T34–WD-T36 | AZ-FIN-WEIL-NULL-EXTENSION |
| WD-T39 | INTERNAL/CONDITIONAL COMPOSITE | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | No new interface; inherits fixed-branch stops where applicable |

### Sharpness examples

| Stable example ID | Purpose | Lean status | Mathematical role |
| --- | --- | --- | --- |
| WD-X01 | Strict finite negativity can screen completely to zero | LEAN-CERTIFIED | EXAMPLE / sharpness witness |
| WD-X02 | Critical screening need not attain a neutral vector in infinite dimension | LEAN-CERTIFIED | EXAMPLE / sharpness witness |
| WD-X03 | Individually screenable negative channels need not be jointly screenable | LEAN-CERTIFIED | EXAMPLE / sharpness witness |
| WD-X04 | Direct compression can remain strong while shorted covariance collapses | LEAN-CERTIFIED | EXAMPLE / sharpness witness |
| WD-X05 | Moving finite sectors can lose every persistent ray | LEAN-CERTIFIED | EXAMPLE / sharpness witness |
| WD-X06 | Positive-coordinate mass loss can strengthen neutrality into negative persistence | LEAN-CERTIFIED | EXAMPLE / sharpness witness |
| WD-X07 | The inverse-square far order is sharp under the zero-moment hypothesis alone | LEAN-CERTIFIED | EXAMPLE / sharpness witness |

### Scope rules

| Scope ID | Rule | Verification class |
| --- | --- | --- |
| WD-S01 | Unweighted sampling/frame statements do not transfer to native Problem-1 coercivity without an explicit metric comparison | SCOPE-ONLY |
| WD-S02 | Prime/pole/archimedean explicit-formula terms are an alternate representation of the Weil form, not additional $K_{+}$ screening coordinates | SCOPE-ONLY |
| WD-S03 | Neutrality is a global quadratic cancellation, not termwise vanishing | SCOPE-ONLY |
| WD-S04 | Weighted near next-jet localization does not imply a source-free uniform lower bound | SCOPE-ONLY |
| WD-S05 | Unselected-background escape does not erase an already anchored fixed selected ray | SCOPE-ONLY |

## External source boundary

| Pin | External input | Direct consumers |
| --- | --- | --- |
| EXT-1 | Douglas factorization | WD-T02 |
| EXT-2A | Bombieri finite Weil inertia | WD-T22 |
| EXT-2B | Bombieri multiplicity/nullity | WD-T23 |
| EXT-3 | Unit-height zeta zero counting | WD-T28, WD-T31 |
| EXT-4 | Compact-window geometric explicit formula | WD-T34, WD-T35; arithmetic input to WD-T38 |
| EXT-5 | Digamma asymptotic | WD-T35 |

Transitive dependence is preserved through the normalized DAG. A theorem can
have an internal proof body while still inheriting an imported premise through
an ancestor.

## Open-interface boundary

The following are **not** verification rows because they are open interfaces,
not stable Horizon-1 theorems:

- `AZ-NEXTJET-LOC`;
- `C-ACTUAL-KPH-FLOOR`;
- `AZ-FIN-WEIL-NULL-EXTENSION`.

Their exact roles are recorded in the RH-facing appendix.
