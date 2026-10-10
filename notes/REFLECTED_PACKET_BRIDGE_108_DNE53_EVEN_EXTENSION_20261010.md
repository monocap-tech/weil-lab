# DNE53: complete 68-pair even extension and six-trial gate

DNE parent: `7d0d03400f78a3bf0d91d01c52a1b6d6a33e4bd4` (DNE52).
CC117 remains pinned read-only at `8d3b66127af94d0dba06389b14579f5b79e9a6d6`.
Only `research/rpb108-direct-null-exclusion` is written.

**The complete even 56-dimensional response budget passes.** With CC117 odd56, the original whole a=53/50 aperture is positive. The combined paid physical gap lower is `1/1000000000000000000000000000000000000000`.

Independent audits pass **60,626 new exact rational checks**: 40,801 source checks and 19,825 response checks. Inherited checks are not recounted. The actual original infinite F112 floor remains **647/1000**; it is not replaced by a hypothetical floor.

## Complete original source obligations

The source order is DNE50's unchanged 59 columns followed by the pure physical Legendre vectors e112,e114,e116. The native map retains every original Z56 column; the high trial map is `[44,45,46,59,60,61]`.

| Original source obligation | Upper correlations | DNE53 disposition |
| --- | ---: | --- |
| DNE50 59-column source block | 1,770 | Literally preserved |
| CC117/CC116 reuse bridge | 115 | Literally preserved |
| Old DNE Y3 against e112,e114 | 6 | Newly integrated twice |
| e116 against all preceding sources and itself | 62 | Newly integrated twice |
| e112/e114 self and mutual controls | 3 | Newly integrated twice; inherited original entries preserved |

Primary order360/precision600 and replay order400/precision620 use the authenticated original source engine, normalized physical columns, the signed regular and pole terms, all six active prime powers in both orientations, seven half-aperture translation panels, exact endpoint logarithms and exact integer polynomial products. No sampled quadrature is used. Each new projected source pairing subtracts **all 56 even retained coordinates** and pays both the original operator remainder and polynomial/log rounding. Each primary fresh pairing contains its replay pairing. The three control pairings intersect the inherited original pairings; they pay new approximant norms without replacing those inherited entries.

The final **original** 62-by-62 projected source Gram is complete and symmetric. Its rounded approximant Gram is deliberately sparse outside the inherited block and the 71 integrated pairs: no uncomputed rounded correlation is represented as a certified zero. The 115 reused entries refer to the same exact original physical source vectors.

## Original native pairings and paid mixed response

The old Y3 native block and Z56/Y3 pairings are preserved. The Z56/e112,e114 pairings and their native self/mutual block are preserved from DNE52. Complete original action coordinates through degree180 pay the old Y3/new-mode pairings and the new e116 pairings against every Z56 column. Symmetric pure-mode pairings are intersected after paying the whole-source error. The producer and independent auditor explicitly check every mixed native entry before using the enlarged response.

With k=.647, the load-bearing quantities are

    E=G_ZY-k Q_ZY,
    W=G_YY-k Q_YY,
    H(J)=k Q_ZZ-G_ZZ+EJ+(EJ)^T-J^T W J.

W has an independently replayed exact rational positive congruence certificate. The six-by-56 J is frozen as exact rationals; floating arithmetic only chooses it. The auditor reconstructs all matrix products using unrounded rational endpoints and checks every paid enclosure.

The independently audited full even budget supplies a Schur coefficient floor and an even whole-high physical gap approximately **1.146108816705e-37**. The common even/odd guard remains **1e-39**. Since the retained charts have full parity rank56 and the entire infinite F112 block is included, this is original whole-aperture positivity at **a=53/50**, not just a finite-grid or selected-vector test. It does not assert RH or positivity at every aperture.

DNE52 ruled out averaging the old DNE and CC comparison families. DNE53 pays the mixed correlations in one enlarged six-trial family and closes the final even direction at the unchanged .647 floor. The true infinite high inverse is not evaluated. RH, F4 and Lean remain open.

## Reproduction and custody

```sh
DNE16_ORDER=360 DNE16_PRECISION=600 python scripts/certify_dne53_even_source_extension.py even --count 62 --output scratch/dne53_even_360.json
DNE16_ORDER=400 DNE16_PRECISION=620 python scripts/certify_dne53_even_source_extension.py even --count 62 --output scratch/dne53_even_400.json
```

Pack each raw JSON with deterministic gzip (`mtime=0`) and base64, preserving the raw bytes, into the named primary/replay source artifacts. Then run:

```sh
python scripts/validate_dne53_even_source_extension.py notes/data/RPB108_DNE53_EVEN_SOURCE_20261010.json.gz.b64 notes/data/RPB108_DNE53_EVEN_SOURCE_REPLAY_20261010.json.gz.b64 --output notes/data/RPB108_DNE53_EVEN_SOURCE_VALIDATION_20261010.json
python scripts/certify_dne53_even_response.py --output notes/data/RPB108_DNE53_EVEN_RESPONSE_20261010.json.gz.b64
python scripts/validate_dne53_even_response.py notes/data/RPB108_DNE53_EVEN_RESPONSE_20261010.json.gz.b64 --output notes/data/RPB108_DNE53_EVEN_RESPONSE_VALIDATION_20261010.json
```

Stored-byte custody hashes and decoded certificate hashes are recorded separately in the DNE53 custody manifest. Both completed seven-panel checkpoints and the exact producer revision that generated them are retained. A hash-variable serialization bug was corrected after integration; `--finalize-checkpoint` reconstructed the final certificates from those checkpoints with the same projection and payments. The independent primary/replay source audit passed after that reconstruction. Historical files and wording remain unchanged. All DNE53 producers and audits completed; no DNE53 computational jobs remain running.
