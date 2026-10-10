# RPB108 — DNE43 establishes the full-packet high target

Parent: DNE42, `b6b5cbe5a9f59dbf9f03ae931083289dbf11bf13`, on `research/rpb108-direct-null-exclusion`.
Terminology: `docs/TERMINOLOGY_RPB108_DNE43_HIGH_TARGET.md`, registered before computation.

DNE43 establishes the original infinite F112 lower bound **603/1000=0.603**. It discharges both DNE42 conditional full-packet targets, closing all three outstanding comparison directions inside the computed packet. Original positivity advances **69 -> 72 retained directions**, 36 per parity, plus the entire infinite F112. Forty retained dimensions outside this packet remain open. No source integration or actual inverse evaluation is repeated.

## Prime norm certificate

Let P be the positive clipped prime-translation operator on I=(-53/50,53/50), including the original powers 2,3,4,5,7,8 and both translation orientations. Its coefficients are Lambda(n)/sqrt(n), with Lambda(4)=Lambda(8)=log(2). Symmetry and the weighted Schur inequality give ||P|| <= ess sup(Pw/w) for a strictly positive weight w. Every translated interval is clipped to I.

The producer tests the actual step functions P^m 1, starting with the already used m=7. It reaches the prescribed prime-norm ceiling with **w=P^17 1**. The numerator is P^18 1. Symbolic cuts are +/-a+log(q) with exact rational q, and their ordering is accepted only after rational log enclosures are disjoint. No sampled maximum or rounded boundary chooses a clipping decision.

| Quantity | Certified value or decimal display |
|---|---:|
| Weight bands | 7,485 |
| Numerator and common bands | 8,899 |
| Minimum weight, lower bound (display) | 105,117.34231457 |
| Primary maximum row-ratio upper (display) | 2.1686256632405123 |
| Replay maximum row-ratio upper (display) | 2.1686256613028605 |
| Prescribed strict prime-norm ceiling | 2.16935 |
| Inherited strict archimedean-minus-pole floor | 2.772351243732 |
| Derived strict original high floor | 0.603001243732 |
| Rounded original infinite F112 floor | 0.603 |

The primary uses 60-digit outward rational grids and 130 logarithm-series terms. The replay uses 80 digits and 180 terms. Logarithms are range reduced before the rational atanh series. Interval event sweeps may widen under repeated subtraction; the replay is tighter. Both enclose the actual positive step functions and satisfy the same strict norm ceiling.

The recorded powers are diagnostic controls: the maximum bound at m=16 is about 2.169687054486 and does not reach this ceiling; m=17 does. A failed power weight means only that this particular bound did not close the target. It does not prove an operator-norm obstruction.

## Independent high audit

The verifier reconstructs every power using positive sums of actual translated source-band values, rather than replaying event sweeps. Its logarithms use independent 100-digit outward arithmetic and a range-reduced 160-term series. It verifies every symbolic cut, exact clipping coverage, strict positivity, source-band containment, stored value enclosure, and each common-band row ratio. It independently replays the inherited archimedean Fourier-shell and pole payments, proving that the original infinite high restriction exceeds the rounded floor 0.603.

The compressed certificates are base64-encoded deterministic gzip files. Their recorded hashes refer to the decoded JSON bytes. The audit was run on those identical decoded bytes; the transfer audit authenticates the compressed copies against the high-audit hashes.

## Full packet and physical guard

DNE42 certifies u N36-G36 positive at u=0.60240095 even and u=0.59548416 odd. Both u are below the now established original high floor 0.603. Thus the original high restriction also satisfies each u, and the previously conditional square-completion estimates become actual positive estimates on the full 36-column packet in each parity and the entire infinite high space.

All original native/source mixed correlations remain paid. No inverse response is evaluated. DNE41 authenticated the exact full retained rank 36 of each packet; its positive and negative comparison embeddings together span that packet. Therefore the full packet contains the previous 69-direction positive span exactly. For a sharper actual bound, the inherited native certificate gives N36 >= d_N I, and the DNE42 target certificate gives u N36-G36 >= d_u I. Thus at the established floor k=0.603, k N36-G36 >= (d_u+(k-u)d_N) I. The transfer audit authenticates both certificates and computes this exact rational increment. With the inherited exact physical mass M and paid source trace T, square completion gives min{((d_u+(k-u)d_N)/k)/(4(M+T/k^2)),k/2}. The full-packet physical lower bounds are approximately 4.056688522e-40 even and 6.705005973e-35 odd, giving a common actual guard **1e-40**. The prior **1e-39** guard remains valid on its smaller 69-direction span.

Historical DNE42 statements remain conditional within their original stage; this new high certificate discharges their hypothesis. Historical DNE41 comparison inertia at k=0.578 remains correct for that old comparison. DNE43 does not reinterpret negative comparison directions as original negative or null vectors.

The high audit passes **1,729,240 new exact rational checks**; the authenticated full-packet transfer passes **36 additional checks**. Both validation artifacts report PASS. All three new scripts pass syntax compilation. DNE42 and DNE41 checks are inherited and are not counted again.

## Next obligation and reproduction

The three-direction obstruction within the existing source packet is now closed by a stronger original high bound. The next source obligation is the forty retained dimensions outside the packet: twenty per parity. Whole a=53/50 positivity, first-contact exclusion, RH and Lean remain open. Actual inverse response remains unevaluated and is not required for this packet's certificate.

Run the producer with `DNE43_GRID_DIGITS=60 DNE43_LOG_TERMS=130` for the primary and `DNE43_GRID_DIGITS=80 DNE43_LOG_TERMS=180` for the replay. Pass each output path ending in `.json.gz.b64` to `scripts/certify_dne43_prime_schur.py`. Run `scripts/validate_dne43_high_floor.py PRIMARY REPLAY --output HIGH_VALIDATION.json`, followed by `scripts/validate_dne43_full_packet_transfer.py --output notes/data/RPB108_DNE43_FULL_PACKET_VALIDATION_20261010.json` with the recorded dependency paths. Require both audits to PASS before publication.
