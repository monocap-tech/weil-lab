# RPB108 — DNE44 certifies 85 retained directions with the extended source packet

Mathematical parent: DNE43, `5ec8aeeb73fa67eff670e0716a1a752f5d3e64b3`. Preparation checkpoint: `ba0b901b914998999dbd9263edbbe1a2c8261bc0`. Branch: `research/rpb108-direct-null-exclusion`.
Terminology was registered before computation in `docs/TERMINOLOGY_RPB108_DNE44_JOINT_SOURCE_EXTENSION.md`. The preparation note records its earlier state and remains unchanged.

DNE44 advances original positivity **72 -> 85 retained directions**, 42 even and 43 odd, together with the entire infinite F112. The previous 72-direction span is contained exactly. The enlarged physical gap guard is **1e-38**, strengthening the previous 1e-40 guard. The original infinite high floor remains **603/1000**. Twenty-seven retained dimensions remain uncovered: twenty-four outside the computed packet and three inside it.

## Complete extended source packet

The fixed packet is Z44=(T4*S,X[0:40]), using the unchanged DNE32 native-normalized remainder columns. It extends the DNE40 packet Z36 exactly by eight columns per parity. Normalization is native normalization; physical masses are independently reconstructed in the orthonormal physical Legendre basis.

Each parity now has a complete paid 44x44 original projected-source Gram, 1,936 entries. Together these are 3,872 entries. The 36x36 leading blocks are reused unchanged from their authenticated primary/replay inputs. The extension computes 324 new upper-triangle correlations per parity, including every new-old mixed entry and every new-new entry. No mixed native or source term is dropped.

Four analytic source runs complete: primary (N,P)=(360,600) and replay (400,620), in both parities. They include the original archimedean source, signed pole source, all active prime powers 2,3,4,5,7,8 in both orientations, all seven half-interval panels, logarithmic endpoint terms, and closed log-squared moments. Whole-source integrals minus all 56 retained projection coordinates give the complete infinite high source Gram. There is no finite high-tail cutoff or sampled quadrature.

The source helper is the unchanged `scripts/dne23_dne16_source_input.py`, SHA256 `e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8`. The inherited analytic operator error is paid as eta_N=2a(550/19)(106/125)^N+3e-99. Common polynomial coefficient rounding uses 250 digits, with physical source errors and all Gram cross payments retained. The existing Gram entries are not reintegrated; their source polynomials are reconstructed as needed for new correlations.

## Outward integer moment integration

Repeated antiderivative evaluations are replaced by exact sign-aware integer sums against analytic moment enclosures. Moment endpoints are rounded outward to the common absolute grid 10^-P. For an integer coefficient c, the lower product uses c*moment_lower when c>=0 and c*moment_upper otherwise; the upper product uses the opposite endpoint. Summing those integers and dividing by the exact coefficient/moment denominator encloses the analytic polynomial integral. The final conversion back to the source Decimal interval is outward at both endpoints.

The regular, logarithmic and log-squared moments retain their closed analytic definitions. This arithmetic changes how the integrals are enclosed, without weakening source payments. The independent audit tests signed sums, outward endpoint conversion and the resulting exact rational integral bounds, and verifies that the signed no-carry polynomial convolution is identical to the previously certified implementation. Each convolution also enforces its exact no-carry bound during production.

All four runs finish in approximately 22.3–24.3 minutes. Atomic per-panel checkpoints authenticate parity, column count, order, precision, packet/reuse hashes and producer hash. These checkpoints preserve completed panels, while final decoded source archives are saved in the repository. The compressed archives use deterministic gzip/base64, and mathematical input hashes refer to their decoded JSON bytes.

## Preserved span, signs and inertia

Let H=(603/1000)N44-G44. The leading 36-dimensional coordinate block is the old DNE43 certified packet. As in DNE41, a midpoint solve proposes a rational approximation J to the inverse mixed-block solve, and a midpoint Schur eigensystem proposes rational extension vectors. These calculations choose candidates only. The exact positive embedding B has the first 36 coordinate vectors as its unchanged first columns, followed by six positive extensions even and seven odd. The exact negative comparison embedding D has two columns even and one odd.

Rational congruences with paid outward Gershgorin margins prove B*H B>0 and -D*H D>0. The independent audit verifies every matrix entry, congruence, sign margin, full rank of (B,D), exact retained rank 44 of the raw packet, and containment of the previous coordinate span. The full original native matrix N44 also passes its own positive congruence control.

| Quantity | Even | Odd |
|---|---:|---:|
| Joint source packet dimension | 44 | 44 |
| Preserved positive prefix | 36 | 36 |
| New positive extension directions | 6 | 7 |
| Certified positive retained rank | 42 | 43 |
| Negative comparison rank | 2 | 1 |
| Fixed comparison inertia (+,-,0) | (42,2,0) | (43,1,0) |

The signs exhaust all 44 dimensions in each parity, certifying maximal positive dimension for this fixed comparison. These three negative comparison directions do not assert original Weil negativity or nullity. The actual inverse response can be smaller than G44/(603/1000). A basis change alone cannot make the same full comparison positive.

## Original physical guard and audit

The producer reconstructs all exact physical columns and masses of the positive embeddings, including their high polynomial components. If U*(B*H B)U has minimum paid Gershgorin margin m, set d=m/||U||_F^2. With k=603/1000, exact physical mass sum M, and paid source trace upper T, the original all-high physical gap is at least min{(d/k)/(4(M+T/k^2)),k/2}. The verifier independently reconstructs the columns, masses, compressed source trace and gap; the saved trace must enclose the independently computed rational trace.

The physical gap lower bounds are approximately **1.016409500e-38 even** and **9.394560767e-34 odd**. The common guard **1e-38** is strictly below both certified bounds. It holds on all 85 retained directions plus the entire infinite high space, including the previous 72-direction span.

The source audit passes **83,180 new exact rational checks**. The positive-subspace audit passes **26,401**. Total: **109,581 new checks**, both artifacts PASS. All six DNE44 scripts pass syntax compilation. Historical high-floor and source checks are authenticated dependencies and are not counted again. Actual high inverse evaluation, full remaining source certification, whole a=53/50 positivity, first-contact exclusion, RH and Lean remain open.

## Next obligation and reproduction

Twenty-four retained source directions remain outside Z44, twelve per parity. Three directions inside Z44 still require additional original high/response information. The resulting uncovered count is 24+3=27. Further source extension can cover the exterior twenty-four, while closing the current three-direction comparison gate needs a stronger original estimate; comparison signs alone cannot decide actual original positivity.

Run `scripts/certify_dne44_joint_source_Gram.py PARITY --output RAW.json` at the recorded primary/replay environment settings. Encode the four completed JSON outputs as deterministic gzip/base64 at their recorded paths. Run `scripts/validate_dne44_joint_source.py EVEN_PRIMARY EVEN_REPLAY ODD_PRIMARY ODD_REPLAY --output notes/data/RPB108_DNE44_JOINT_SOURCE_VALIDATION_20261010.json`. Then run `scripts/certify_dne44_positive_subspace.py PARITY --output CERTIFICATE.json.gz.b64` in each parity and `scripts/validate_dne44_positive_subspace.py EVEN_CERTIFICATE ODD_CERTIFICATE --output notes/data/RPB108_DNE44_POSITIVE_SUBSPACE_VALIDATION_20261010.json`. Require both audits to PASS before publication.
