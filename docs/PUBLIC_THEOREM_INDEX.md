# Public Theorem Index

## H1-P5.2 — Stable theorem lookup

This is the compact public lookup surface for WD-T01 through WD-T39.

The table separates mathematical standing from Lean verification standing.
Direct dependencies are the normalized proof-DAG inputs, not an exhaustive
list of every auxiliary lemma. Imported-source ancestry is made explicit in
the verification matrix.

| Stable ID | Public name | Role | Direct inputs | Main output | Mathematical standing | Lean status | Sharpness | Canonical source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WD-T01 | Defect identity and index transfer | Abstract screening core | — | Defect identity and equality of coefficient/physical negative index | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md) |
| WD-T02 | Contractive screening equivalence | Abstract screening core | WD-T01; EXT-1 Douglas | Nonnegative defect iff contractive Douglas screening exists | INTERNAL-PROOF + IMPORTED Douglas | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md) |
| WD-T03 | Reduced-screening graph normal form | Abstract screening core | WD-T02 | Reduced-screening graph normal form under exact range inclusion | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md) |
| WD-T04 | Abstract screening taxonomy | Abstract screening core | WD-T02 | Abstract screening taxonomy including attained/non-attained criticality | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-X02 | [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md) |
| WD-T05 | Rank-one defect specialization | Abstract screening core | WD-T02 | Rank-one defect specialization | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md) |
| WD-T06 | Monotone positive screening | Abstract screening core | — | Monotone positive-channel restoration and nonincreasing negative index | INTERNAL-PROOF | LEAN-CERTIFIED | WD-X01 | [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md) |
| WD-T07 | Selected/background custody | Selected/background transfer | — | Selected negativity survives negative-background aggregation; converse custody fails | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T08 | Finite selected-sector index cap | Selected/background transfer | WD-T07 | Finite selected-sector negative-index cap | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T09 | Shared screening budget | Selected/background transfer | WD-T07 | Selected and background channels share one screening budget | INTERNAL-PROOF | LEAN-CERTIFIED | WD-X03 | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T10 | Background elimination and residual budget | Selected/background transfer | WD-T02; WD-T09 | Contractively screened background reduces to residual positive synthesis | INTERNAL-PROOF | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T11 | Finite-sector singular-value inertia | Selected/background transfer | WD-T03 | Finite-sector inertia/nullity counted by singular values of residual screening map | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T12 | Sequential background consumption | Selected/background transfer | WD-T10 | Sequential background consumption is closed under the defect calculus | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T13 | Shorted-covariance reduction | Selected/background transfer | uniformly positive Schur-complement hypotheses | Complement elimination replaces direct compression by Schur/shorted covariance in the uniformly positive setting | INTERNAL-PROOF | LEAN-CERTIFIED | WD-X04 | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T14 | Finite positive-shadow separation | Selected/background transfer | — | Finite positive shadows preserve sign but not analysis-space admissibility | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md) |
| WD-T15 | Right-limit projection and gap duality | Support filtration and persistence | — | Right-limit projection convergence and gap-space duality | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Support Filtration](SUPPORT_FILTRATION_PERSISTENCE.md) |
| WD-T16 | Fixed-sector persistence | Support filtration and persistence | WD-T15; fixed finite selected sector | Fixed finite negative sector forces a nonzero persistent nonpositive/negative right-limit ray | INTERNAL-PROOF | LEAN-CERTIFIED | WD-X05 | [Support Filtration](SUPPORT_FILTRATION_PERSISTENCE.md) |
| WD-T17 | Fixed-sector critical dichotomy | Support filtration and persistence | WD-T15; fixed finite selected sector | Fixed-sector critical dichotomy: attained neutral limit or negative fall-through | INTERNAL-PROOF | LEAN-CERTIFIED | WD-X05, WD-X06 | [Support Filtration](SUPPORT_FILTRATION_PERSISTENCE.md) |
| WD-T18 | Endpoint-jump index bound | Support filtration and persistence | WD-T15 | Endpoint-jump quotient bounds new right-limit negative index | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Support Filtration](SUPPORT_FILTRATION_PERSISTENCE.md) |
| WD-T19 | Boundary amplification and representative blow-up | Support filtration and persistence | new endpoint vector; common bounded physical realization/right continuity | New endpoint vectors force boundary amplification / representative blow-up | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Support Filtration](SUPPORT_FILTRATION_PERSISTENCE.md) |
| WD-T20 | Conjugate-pair diagonalization | Zeta-Weil zero-side specialization | — | Canonical conjugate-pair diagonalization into positive/negative Weil channels | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T21 | Simple quartet pair geometry | Zeta-Weil zero-side specialization | WD-T20 | One simple zeta quartet contributes two negative pair coordinates | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T22 | Finite Weil inertia saturation | Zeta-Weil zero-side specialization | EXT-2A Bombieri finite inertia | Finite Weil negative index equals number of distinct nonreal conjugate pairs | IMPORTED + SPECIALIZED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T23 | Multiplicity-null reduction | Zeta-Weil zero-side specialization | EXT-2B Bombieri multiplicity/nullity | Multiplicity-null directions must be quotiented before independent index counting | IMPORTED/DERIVED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T24 | Finite exponential independence | Zeta-Weil zero-side specialization | — | Finite distinct-frequency exponential independence on a nonempty interval | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T25 | No exact finite positive compensation | Zeta-Weil zero-side specialization | WD-T24 | No exact finite positive compensation for an anchored selected negative cell | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T26 | Selected zero-moment residue law | Zeta-Weil zero-side specialization | WD-T20 | Selected negative raw residues satisfy the zero-moment law $\mathbf{1}^Tv=0$ | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T27 | Universal inverse-square far decay | Zeta-Weil zero-side specialization | WD-T26 | Zero moment gives universal $R_v(z)=O(\lvert z\rvert^{-2})$ far decay | INTERNAL-PROOF | LEAN-CERTIFIED | WD-X07 | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T28 | Native Problem-1 compactness | Zeta-Weil zero-side specialization | EXT-3 zero counting; native resolvent estimate | Native Problem-1 zero synthesis is Hilbert-Schmidt; off-axis helper covariance is trace class | INTERNAL-PROOF + imported zero count | LEAN-CERTIFIED | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T29 | Quantitative finite-head approximation | Zeta-Weil zero-side specialization | WD-T28 | Exact bounded-budget infinite-helper target requires quantitative finite-head approximation | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md) |
| WD-T30 | Two-mode selected-preserving multiplier | Explicit-formula arithmetic | two-mode selected-preserving hypotheses | Two-mode selected-preserving scalar multiplier exists | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) |
| WD-T31 | Zero-count far-tail estimate | Explicit-formula arithmetic | WD-T27; EXT-3 zero counting; bounded multiplier | Zero moment + zero counting gives $O((\log R)/R)$ far complementary tail | INTERNAL-PROOF + imported zero count | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) |
| WD-T32 | Weighted completed next-jet representation | Explicit-formula arithmetic | completed-Ξ local response identities | Near complementary response is represented by the weighted completed $\Xi$ next-jet field | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) |
| WD-T33 | Adaptive cocancellation guard | Explicit-formula arithmetic | fixed-cutoff explicit-formula cocancellation setup | At a fixed cutoff, adaptive near-minus-archimedean cancellation collapses the corresponding prime term onto the far term | INTERNAL-PROOF | LEAN-CERTIFIED | — | [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) |
| WD-T34 | Finite compact-window prime translations | Explicit-formula arithmetic | EXT-4 compact-window formula | Fixed compact support activates only finitely many prime-power translations | DERIVED from IMPORTED compact-window formula | LEAN-CERTIFIED | — | [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) |
| WD-T35 | Logarithmic compact-window form order | Explicit-formula arithmetic | WD-T34; EXT-4 compact-window formula; EXT-5 digamma asymptotic | Compact-window Weil form has logarithmic Fourier/form order | DERIVED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) |
| WD-T36 | No free positive-Sobolev bootstrap | Explicit-formula arithmetic | WD-T35 | Logarithmic form control yields no uniform positive-Sobolev coercive estimate; finite translations add no smoothing | INTERNAL-PROOF/SHARPNESS | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md) |
| WD-T37 | Persistent negative morphology | Composite morphology | WD-T16; WD-T07; WD-T26; WD-T27; WD-T31; WD-T32; WD-T33; fixed-packet negative-branch hypotheses | Fixed-packet persistent negative defect localizes to zero-moment source + weighted near next-jet morphology, stopping at AZ-NEXTJET-LOC | CONDITIONAL COMPOSITE | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Negative Defect Morphology](NEGATIVE_DEFECT_MORPHOLOGY.md) |
| WD-T38 | Attained neutral morphology | Composite morphology | WD-T17; WD-T34; WD-T35; WD-T36; attained/unit-gain physical-realization hypotheses | Attained unit-gain neutral branch gives a carrier-identified compact-window null mode with logarithmic order + threshold-aware finite shifts, stopping at AZ-FIN-WEIL-NULL-EXTENSION | CONDITIONAL COMPOSITE | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | — | [Neutral Defect Morphology](NEUTRAL_DEFECT_MORPHOLOGY.md) |
| WD-T39 | Noncompact background morphology | Composite morphology | WD-T15–T17; WD-T07; WD-T14; fixed selected-ray hypotheses where invoked | Full-coefficient moving escape, unselected-background escape, and fixed full-divisor negative weak limits are distinct compactness morphologies | INTERNAL/CONDITIONAL COMPOSITE | LEAN-CERTIFIED | WD-X05, WD-X06 | [Noncompact Background Morphology](NONCOMPACT_BACKGROUND_MORPHOLOGY.md) |

## Reading rule

- **Mathematical standing** answers what kind of mathematical claim the item is.
- **Lean status** answers what the pinned Lean development verifies.
- A `LEAN-CERTIFIED-FROM-IMPORTED-PREMISE` row certifies the downstream
  deduction from an explicit formal premise; it does not certify the external
  theorem represented by that premise.
- Open RH-facing interfaces are not theorem IDs and are therefore not inserted
  into the theorem sequence.

## RH-facing outputs

| Theorem | Boundary output |
| --- | --- |
| Negative morphology (WD-T37) | AZ-NEXTJET-LOC; C-ACTUAL-KPH-FLOOR is stronger refinement |
| Neutral morphology (WD-T38) | AZ-FIN-WEIL-NULL-EXTENSION |
| Noncompact morphology (WD-T39) | No new interface; inherits fixed-branch stops where applicable |

See [RH Interface Appendix](RH_INTERFACE_APPENDIX.md) for the full boundary specification.
