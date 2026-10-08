# RPB108: prime-power-8 direct attempt — corrected 112-vector certificate fails

2026-10-08 UTC (2026-10-07 Pacific). Initial recovered live head: 401f6b3970280a79da974661cbb806b78b4ea1ca, ahead of the supplied 2ae3bc383d38bf245ab137cbcb6799cd59ee0dba. Concurrent Global/F4 heads e23adbbc8ceebac5b67d359dcf6dd88cd0d477c9 and 1b5db1dc92717e7e0dcd85341ac1494de97c0b70 were subsequently recovered. The final prepublication head 47e0ada898cdc2b9d57a209db683019a3a43f40e also includes NF58 and NF59. Publication is an additive, leased fast-forward from the freshly recovered head; no historical or concurrent file is replaced. Definitions: [prime-8/scalability](../docs/TERMINOLOGY_RPB108_PRIME8_SCALABILITY_105.md).

## Required report

| Item | Result |
| --- | --- |
| Target | Exact a=21/20, crossing log(8)/2 and below log(9)/2 |
| Arithmetic/source geometry | Prime powers 2,3,4,5,7,8; Lambda(8)=log(2); fourteen cuts, thirteen panels; exact order and overlaps in the [preflight report](REFLECTED_PACKET_BRIDGE_108_PRIME8_PREFLIGHT_105_20261008.md) |
| Direct 112-vector preflight | PASS after fresh geometry, joint prime norm, complement, budgets and strict Garding checks |
| Native finite restriction | PASS with fresh 420/420 native data, descending parity elimination, margin 1/(262144*10^28), independent wider 80-digit audit |
| Complete target source | PASS: 112 columns, 1456 panels, full actual map allowance about 3.6780234340922796e-36 |
| Complete target residual Gram | PASS: two independently initiated thirteen-panel constructions/checkpoints repeat byte for byte; maximum product degree 942; all mixed/log/projection terms retained |
| Actual-error-corrected Schur | FAIL with an exact rational 112-coordinate witness, independently rechecked at wider intervals |
| Whole-domain result at 21/20 | NOT CERTIFIED; no physical/logarithmic conversion is promoted after the failed sign |
| Latest certified whole-domain aperture | a=1, preserved certificate 811b0826abf45d688d1e2da7900cda852103ddee |
| All-aperture theorem | Complement recoverability proved analytically; full Schur/continuation criteria remain conditional; unchanged origin-series implementation is obstructed uniformly |
| Smallest justified next experiment | Same-aperture 113-vector native/source preflight and conditioning/error analysis; its complement-only probe is already positive, but it is NOT a complete 113-vector certificate |

The publication commit itself is the new publication head; the custody manifest records its freshly recovered parent. This report does not identify publication with a positivity result.

## 1. Exact new support regime

In physical coordinates the prime-power-8 plus term is supported on [-21/20,21/20-log(8)], and its reflected minus term on [-21/20+log(8),21/20]. The exact overlap length is 21/10-log(8), approximately 0.02055845832016407. The per-orientation amplitude is log(2)/sqrt(8). Both orientations, all earlier active terms and the changed 2/4 event order are retained.

The independent support audit checks all 156 signed branches. The complete all-arithmetic edge audit checks 1344 profiles and 75936 coefficient jumps, including all twelve interior arithmetic support events, both orientations, reflection, normalizations and Mangoldt multiplicities. All 1344 omitted-profile controls are rejected. The separate newly active prime-8 endpoint-Beta audit covers the first native row and all 112 diagonals (223 distinct pair checks).

At the next arithmetic threshold log(9)/2, 9=3^2 activates with amplitude log(3)/3; its extreme support cuts appear and the prime-3 cuts meet at the center and reverse order. It requires fresh data and estimates, not support-inclusion extrapolation.

## 2. What passes for 112 vectors

The joint prime norm is at most 1063939/500000=2.127878. Two weighted constructions repeat exactly; independent finer logarithms and exact translated-row checks cover 3277 weight cells, 4339 refined cells and 52068 signed transitions. The physical complement bound is c=699/1000, strictly below unrounded 0.6997921531086909. Independent damping/rate/infinite-tail checks cover all 144 finite degree bounds, three tails and four comparison regions. The original 93/100 constant and old 179/10 cutoff are not reused.

Native orders 400/400 satisfy a standalone width threshold but fail ascending interval elimination. Orders 420/420 reduce the maximum entry width to 4.268501620424048e-46. Ascending elimination still fails at the same early even pivot. Descending-degree and descending-diagonal orders pass on those SAME intervals. Fresh descending-parity finalization and its exact repeat give physical finite margin 1/(262144*10^28), about 3.814697265625e-34.

Independent raw-to-physical reconstruction and compact inclusions audit all 12544 entries. All 112 shifted pivots pass again at wider 80-digit arithmetic with the proved margin, and the negative diagonal control is rejected. The original 400-order data and the unsuccessful ascending/selected-margin reordering probes are preserved. The experiment does not prove 420 is the minimum necessary order. It shows both precision and elimination conditioning must be verified; a raw entry-width cutoff alone is insufficient.

The complete source uses orders 100/130, gamma 56, Machin 160, 400-digit outward intervals and 40-digit coefficient quantization. All actual error contributions are retained. Independent normalization/error aggregation, 606424 coefficient floor checks, 1456 displaced-floor controls, all arithmetic edge profiles and finer constant/Bernoulli checks pass. Repeat assembly from the same saved columns gives exactly the same decoded source and canonical sorted bytes; the two original serialization hashes are distinct and both are preserved. This repeat scope is not mislabeled as a second independently computed source.

## 3. Complete corrected coupling and rigorous failure

Two independently initiated complete residual integrations use initially absent separate checkpoints. Every endpoint-log, smooth, mixed and 112-coordinate projection term is retained through degree 942. The complete results and checkpoints repeat byte for byte. The maximum residual interval width is about 8.94725070912547e-81.

Independent exact endpoint-Hankel pairing audit checks every one of the 12544 native/source pairings, with actual source allowance and enclosure widths retained. Independent 400-digit reconstruction checks all 12544 residual entries using closed binomial Legendre coefficients, separate endpoint-log-squared moments and Machin 320. Every finer enclosure lies inside its saved enclosure; all displaced controls are rejected.

The COMPLETE surrogate Gram gives M about 7.313857472430691. With the COMPLETE actual source allowance eta about 3.6780234340922796e-36, the correction is

    delta=eta(2M+eta) about 5.380107835442201e-35.

The complete target sufficient form is

    S=Q_E-(1000/699)(R+delta I).

The sign decision tries the full original, descending-parity and descending-diagonal permutations while retaining every matrix entry. It does not find a positive certificate. Instead it constructs an EXACT rational coefficient vector v, stored in SCHUR112_105_CERTIFICATE, with outward intervals proving

    v* S v < -7.21785e-34,
    Q_E(v) > 5.38189e-32,
    ||v||_2^2 about 2.873239098190553.

The physical vector is h(x)=sum_(n=0)^111 v_n sqrt((2n+1)/(2a)) P_n(x/a), supported on [-a,a]. These are physical coefficient/mass normalizations, not coefficient Gram eigenvalues interpreted as operator eigenvalues. The primary result and a separately repeated sign decision use 160-digit outward arithmetic. The independent wider 80-digit audit recomputes delta, the witness form and actual native Q; it confirms negative S and POSITIVE actual native Q.

Removing the source-error correction still gives a rigorous negative surrogate sufficient value, approximately -5.00636527335685e-34. Therefore merely reducing eta or raising the coefficient grid CANNOT repair THIS chosen c=699/1000 certificate on this witness. About 2.211493016491256e-34 of the corrected loss comes from the actual source allowance; the rest already exists in Q_E-c^-1R.

For the SAME 112-vector surrogate/error data, positivity on this witness requires

    c > (v*R v + delta||v||^2)/Q_E(v).

Independent outward intervals give a stored rigorous lower ratio approximately 0.7083745550661842. This is substantially above the proved 0.699 and nearly exhausts the positive-Bessel method ceiling below 0.708399. It is a quantified obstruction to the chosen scalar-complement sufficient estimate. It does NOT prove a negative actual Weil vector, intrinsic insufficiency of every 112-vector realization, or impossibility of a sharper complement inverse/action estimate.

No target whole-domain physical/logarithmic conversion is promoted. Positivity at a=1 remains intact; F4, full transport, endpoint exclusion and Lean closure remain open.

## 4. Smallest dimension experiment, without aperture retreat

After the exact failure was located, the one-vector enlargement k=113 was tested ONLY for complement coercivity at the SAME a=21/20. Cutoffs 15*(113/112),16*(113/112),17*(113/112), the unchanged rigorously verified target prime norm and fresh degree/tail calculations give

    c_113 >= 70867/100000=0.70867,

strictly below unrounded 0.7086702751031646. The independent finer recurrence/interval audit checks all 144 damped degree terms and three tails. This exceeds the old witness's required scalar ratio.

F_113 is a DIFFERENT complement from F_112. One must NOT insert c_113 into the old 112-vector Gram. The new source coordinate, all its mixed pairings, the changed residual projection, finite conditioning and FULL error budget must be recomputed. In particular adding a retained direction can improve complement coercivity while making the finite block's smallest margin smaller. No claim that 113 vectors suffice follows from this complement probe.

The smallest justified remaining experiment is a complete 113-vector native/source preflight at 21/20, tying source accuracy to the NEW finite margin, followed by fresh matched 113-coordinate Grams if that gate is viable. It is not another aperture step. A sharper inverse-complement Schur bound is an alternative mathematical route that would require its own proof and exact data.

## 5. Strategic scalability outcome

The [scalability report](REFLECTED_PACKET_BRIDGE_108_APERTURE_SCALABILITY_20261008.md) proves an explicit parameterized cofinite bound: at T=k/(10a), low Fourier mass is at most (245/552)k(33/35)^(2k). For every fixed finite aperture, finite prime bound and valid pole allowance, its resulting complement lower bound tends to infinity as k grows. Complement recovery is thus not the all-aperture obstruction by itself.

The complete corrected Schur sign, finite conditioning and adequate source accuracy remain independent obligations. The present direct Bernoulli remainder proof requires a<3/2; the single origin series has actual complex radius 2pi and cannot cover all required distances once a>pi/2. A segmented or different certified archimedean kernel representation is required for an all-aperture implementation.

Existing norm continuity supports conditional local continuation, not ordinary upward support inclusion. The recovered concurrent NF57 theorem adds a reusable canonical prime-smearing approximation with sharp logarithmic error rate. It retains the actual archimedean/pole terms and supplies no smeared sign or full changing-aperture modulus. Its worst-domain rate and tiny conservative gaps quantify an efficiency issue. Recovered NF58 improves sign-transfer error on bounded original eigenlevels; NF59 excludes a fixed-positive-width prime-only all-aperture smeared lower bound by a prime/pole main-term mismatch. Adaptive widths remain open. None closes the corrected Schur condition for all apertures.

The outcome is a completed rigorous fixed-target ATTEMPT, an exact sufficient-inequality obstruction, a smallest dimension probe, a proved analytic complement-recovery theorem and explicit remaining uniform-method tasks. It is not an all-aperture theorem or a Lean certificate.

## Reproduction and evidence levels

Run restore_native_prime8_105_archives.py after retrieving the committed gzip blobs. Its manifest verifies every compressed and restored hash, and only reconstructs byte-identical repeat aliases. The source serialization repeat is separately archived because its bytes differ despite identical decoded/canonical data.

Constructors/auditors and exact source/raw/checkpoint hashes are pinned in PRIME8_105_CUSTODY. Saved unquantized source columns can be regenerated with the pinned source constructor; their 112 record hashes are preserved in the independent source recovery audit. The failed 400-order restriction, complete 420-order raw restriction, descending finite certificate, both complete Gram/checkpoint results, exact Schur witness and widened audits are preserved.

Finite rational/interval validation proves the stated finite enclosures, sign decisions and arithmetic inequalities. Actual form/complement and whole-domain criterion arguments are separately analytic and source-pinned. The new generic complement/scalability proof is documented, with 58 finite controls that are not substituted for its analytic proof. Lean files, axioms and CI are unchanged, and no global positivity or RH claim is made.
