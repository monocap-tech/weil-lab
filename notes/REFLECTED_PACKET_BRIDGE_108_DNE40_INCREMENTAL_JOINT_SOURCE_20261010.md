# RPB108 — DNE40 incremental thirty-six-column original source comparison

Mathematical parent: DNE39, `f15eea0a2d0a4b527bf62d73c17efd940b6eb12f`. Publication parent: interruption checkpoint `3dbaa8a43b92682ed671936b273603f6e65dc69b`, on `research/rpb108-direct-null-exclusion`.
Terminology: `docs/TERMINOLOGY_RPB108_DNE40_INCREMENTAL_JOINT_SOURCE.md`, registered before computation.

## Packet and original operator

The physical packet is Z36=(T4 S,X[0:32]), with the unchanged DNE32 rational frame X=hatY U. All scaled tested columns, native mixed entries (Ps-As J)U32 and remainder correlations remain present. Native normalization does not imply physical normalization. Every physical column mass is paid.

The complete original projected source Gram G36 includes the entire infinite F112 source tail. The source is reconstructed with exact logarithmic endpoint terms, the signed pole, all six prime powers {2,3,4,5,7,8} in both orientations, and analytic polynomial/logarithmic/log-squared moments over seven half-interval cells. No quadrature or sampled maximum supplies a certificate.

## Incremental reuse

At each parity and precision, the first twenty-eight columns match the authenticated DNE38 packet. Their 406 upper-triangle whole-source integrals and all retained coordinates are reused without changes. The expansion adds eight columns and computes all 260 new upper-triangle pairs. It reconstructs every source column to verify identical old polynomial-rounding ledgers. The 56 retained source coordinates per new column are computed and subtracted from the whole-source integral. All source error payments are rebuilt with the original operator remainder and exact physical norm bounds.

Primary regular order/decimal precision is 360/600; replay is 400/620. Polynomial coefficient rounding uses 250 digits, outward stored endpoints use 100 digits. Exact signed packed convolutions assert a no-carry bound. All projection subtraction, interval source norms and source-error payments are rational.

## Signed criterion and physical scope

The original infinite high restriction satisfies Q_F112 >= (289/500) I by DNE39. This stage attaches that existing certified floor by hash. It does not recompute the prime-floor proof.

H40=(289/500)N36-G36 is a sufficient original Schur comparison. The true inverse response is bounded above by G36/(289/500); the inverse is not evaluated. Numerical midpoint calculations propose rational congruences and trial vectors. Exact outward congruence evaluation and positive Gershgorin margins prove positivity; exact negative rational trial energies prove failures of this uniform comparison. Such failures do not prove original Weil negativity or a null vector.

For a positive prefix of rank n, a rational congruence V with V*H40 V >= m I yields d=m/||V||_F^2 and original Schur coefficient floor d/kappa, kappa=289/500. If M is the exact sum of physical column masses and T an upper trace of the projected source Gram, the paid original physical gap is at least min{(d/kappa)/(4(M+T/kappa^2)),kappa/2}. Exact retained minors prove independence. The resulting span includes the entire infinite high space and the specified lifted retained directions. It is not the raw first n Legendre modes.

## Validation and next frontier

The independent rational audit passes **61,227 new exact checks**. The existing DNE39 high-floor audit of 96,416 checks is authenticated and reused; it is not newly rerun here. All four source runs completed with seven analytic cells and matching inherited rounding ledgers. The complete source Grams have 1,296 entries each, 2,592 across the two parities.

| Quantity | Even | Odd |
|---|---:|---:|
| Complete joint source dimension | 36 | 36 |
| Certified positive prefix dimension | 29 | 33 |
| Certified remainder prefix dimension | 25 | 29 |
| First failing uniform-comparison prefix | 30 | 34 |
| Paid negative trial upper at that first failure, decimal display | approximately -0.009692188238 | approximately -0.001849730164 |
| Paid full 36-column negative trial upper, decimal display | approximately -0.024400948897 | approximately -0.017484153405 |
| Necessary uniform floor for the full selected trial | greater than 0.6024009 | greater than 0.5954841 |
| Original Schur coefficient floor on positive prefix, decimal display | approximately 0.0001201617593 | approximately 0.002990436084 |
| Paid physical gap on positive prefix plus F112, decimal display | approximately 3.00390132e-39 | approximately 7.47554705e-34 |

Original all-high positivity extends **56 -> 62 retained directions**, 29 even and 33 odd. Exact retained minors prove independence and the expanded prefixes contain both DNE39 positive spans. The common physical L2 guard on this enlarged span is **1e-39**. DNE39's stronger 1e-38 guard remains valid on its smaller 56-direction span; it is not replaced there. The other **50 retained directions**, whole-aperture positivity at a=53/50, RH and Lean remain open.

Both complete native 36-column matrices have certified positive rational congruences. The full signed uniform comparison fails in both parities, with exact paid rational trials. The unrounded seventh-power prime row floor also fails on the full selected trials. These are failures of the sufficient uniform-high-floor comparison, not proofs of original Weil negativity or of an original null vector.

The next obligation is to strengthen the comparison on the already-computed 36-column packet. Its even full selected trial requires a uniform floor above 0.6024009; merely repeating the same 0.578 comparison cannot close that packet. A stronger paid original high estimate, a directional high-response bound, or additional certified positive subspaces can be tested before further source integration. None is presumed to pass. The complete 56-column parity frames still have 20 uncomputed remainder columns each. Historical wording and certificates remain unchanged.

## Reproduction

Run `certify_dne40_joint_source_Gram.py PARITY --output SOURCE.json` in both parities at defaults and with DNE16_ORDER=400, DNE16_PRECISION=620 for replay. The source helper, DNE32 frame/certificate and DNE38 source inputs must be present at their authenticated paths. Compress each completed JSON with deterministic gzip (mtime=0) and base64 to the recorded notes/data path.

Run `certify_dne40_signed_comparison.py PRIMARY REPLAY --output COMPARISON.json` in each parity, with DNE39 high certificates at their unchanged paths. Then run `validate_dne40_signed_source.py EVEN_PRIMARY EVEN_REPLAY EVEN_COMPARISON ODD_PRIMARY ODD_REPLAY ODD_COMPARISON --output VALIDATION.json`. Its status must be PASS before publication. Custody records new files and all reused source and high-floor inputs.

## Recovery and checkpoint behavior

The earlier interruption record is preserved at `notes/REFLECTED_PACKET_BRIDGE_108_DNE40_INTERRUPTED_CHECKPOINT_20261010.md`, commit `3dbaa8a43b92682ed671936b273603f6e65dc69b`. Recovery found no surviving source process and no completed source JSON. The final computation therefore restarts all four runs; it does not claim to recover completed final integrals from those lost jobs.

The source producer now saves completed-cell Gram accumulators, retained moment accumulators and polynomial-rounding ledgers atomically after each of seven cells. Its resume identity binds parity, count, order, precision, producer hash, exact packet hash and reused source hash. Decimal endpoints serialize as exact strings; a direct round-trip check preserves both endpoints at 600 digits. Resume restores only these interval accumulators after reconstructing the same source and moment tables. A checkpoint is an intermediate producer state, not a certificate or validation PASS.
