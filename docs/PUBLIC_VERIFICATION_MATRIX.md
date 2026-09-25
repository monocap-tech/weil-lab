# Public Verification Matrix

## H1-P5.2 — Mathematical standing, Lean status, and source custody

This matrix is intentionally orthogonal to the main mathematical narrative. It distinguishes mathematical standing, formal verification, source ancestry, certificate evidence, and open-interface exposure.

### Stable theorems

| Stable ID | Mathematical standing | Lean status | Imported premise ancestry | Direct/source pin | Certificate evidence | RH-facing dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WD-T01 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T02 | INTERNAL-PROOF + IMPORTED Douglas | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-1 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T03 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T04 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T05 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T06 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T07 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T08 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T09 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T10 | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T02 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T11 | INTERNAL-PROOF | LEAN-CERTIFIED | Transitive | via WD-T03/WD-T02 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T12 | INTERNAL-PROOF | LEAN-CERTIFIED | Transitive | via WD-T10/WD-T02 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T13 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T14 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T15 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T16 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T17 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T18 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T19 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T20 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T21 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T22 | IMPORTED + SPECIALIZED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-2A | Yes — recorded in LEAN_STATUS.md | — |
| WD-T23 | IMPORTED/DERIVED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-2B | Yes — recorded in LEAN_STATUS.md | — |
| WD-T24 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T25 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T26 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T27 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T28 | INTERNAL-PROOF + imported zero count | LEAN-CERTIFIED | Direct | EXT-3 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T29 | INTERNAL-PROOF | LEAN-CERTIFIED | Transitive | via WD-T28 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T30 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T31 | INTERNAL-PROOF + imported zero count | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-3 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T32 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T33 | INTERNAL-PROOF | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | — |
| WD-T34 | DERIVED from IMPORTED compact-window formula | LEAN-CERTIFIED | Direct | EXT-4 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T35 | DERIVED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Direct | EXT-4, EXT-5 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T36 | INTERNAL-PROOF/SHARPNESS | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T35 | Yes — recorded in LEAN_STATUS.md | — |
| WD-T37 | CONDITIONAL COMPOSITE | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T31 and imported ancestry | Yes — recorded in LEAN_STATUS.md | AZ-NEXTJET-LOC; C-ACTUAL-KPH-FLOOR stronger refinement |
| WD-T38 | CONDITIONAL COMPOSITE | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | Transitive | via WD-T34–WD-T36 | Yes — recorded in LEAN_STATUS.md | AZ-FIN-WEIL-NULL-EXTENSION |
| WD-T39 | INTERNAL/CONDITIONAL COMPOSITE | LEAN-CERTIFIED | No load-bearing imported theorem in normalized DAG | — | Yes — recorded in LEAN_STATUS.md | No new interface |

### Sharpness examples

| Stable example ID | Lean status | Certificate evidence | Mathematical role |
| --- | --- | --- | --- |
| WD-X01 | LEAN-CERTIFIED | Yes — recorded in LEAN_STATUS.md | EXAMPLE / sharpness witness |
| WD-X02 | LEAN-CERTIFIED | Yes — recorded in LEAN_STATUS.md | EXAMPLE / sharpness witness |
| WD-X03 | LEAN-CERTIFIED | Yes — recorded in LEAN_STATUS.md | EXAMPLE / sharpness witness |
| WD-X04 | LEAN-CERTIFIED | Yes — recorded in LEAN_STATUS.md | EXAMPLE / sharpness witness |
| WD-X05 | LEAN-CERTIFIED | Yes — recorded in LEAN_STATUS.md | EXAMPLE / sharpness witness |
| WD-X06 | LEAN-CERTIFIED | Yes — recorded in LEAN_STATUS.md | EXAMPLE / sharpness witness |
| WD-X07 | LEAN-CERTIFIED | Yes — recorded in LEAN_STATUS.md | EXAMPLE / sharpness witness |

### Scope rules

| Scope ID | Verification class | Certificate evidence |
| --- | --- | --- |
| WD-S01 | SCOPE-ONLY | Not applicable — jurisdiction rule |
| WD-S02 | SCOPE-ONLY | Not applicable — jurisdiction rule |
| WD-S03 | SCOPE-ONLY | Not applicable — jurisdiction rule |
| WD-S04 | SCOPE-ONLY | Not applicable — jurisdiction rule |
| WD-S05 | SCOPE-ONLY | Not applicable — jurisdiction rule |

## External source boundary

| Pin | External input | Direct consumers |
| --- | --- | --- |
| EXT-1 | Douglas factorization | WD-T02 |
| EXT-2A | Bombieri finite Weil inertia | WD-T22 |
| EXT-2B | Bombieri multiplicity/nullity | WD-T23 |
| EXT-3 | Unit-height zeta zero counting | WD-T28, WD-T31 |
| EXT-4 | Compact-window geometric explicit formula | WD-T34, WD-T35; arithmetic input to WD-T38 |
| EXT-5 | Digamma asymptotic | WD-T35 |

Open interfaces are not verification rows because they are not stable Horizon-1 theorems: AZ-NEXTJET-LOC, C-ACTUAL-KPH-FLOOR, and AZ-FIN-WEIL-NULL-EXTENSION.
