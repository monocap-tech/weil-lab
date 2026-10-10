# RPB108 — CC110: integrate 85 directions and isolate the three comparison deficits

Parent: CC109, `eaa176a0fe27b3cf71cc6537ab7f05f3ef7d8555`.
Read-only DNE recovery: DNE44, `bb7220c07aa66c2fea00bbc36452a59130ee3fb1`.
Read-only Native recovery: NF55, `29cd9381adeb08a9093b74e1ec487051d68e956b`.
Definitions: `docs/TERMINOLOGY_RPB108_CC110_EXTENDED_PACKET_INTEGRATION.md`.

CC110 advances integrated original positivity from 72 to 85 retained directions, plus every original infinite F112 vector, at aperture a=53/50. The original high floor remains 603/1000. The previous 72-direction span is contained exactly, and the enlarged span retains a common physical gap greater than 1e-38. Twenty-seven retained dimensions remain uncovered. Whole original positivity at 1.06 remains open.

## Source recovery and fresh arithmetic

DNE44 extends Z36 to Z44=(T4*S,X[0:40]) in the unchanged DNE32 frame. Four authenticated analytic runs supply complete original source Grams: N=360 at precision 600 and N=400 at precision 620, for both parities. All 324 new upper-triangle correlations per parity are paid, including every new-old mixed term. The first 36 columns and their original source Grams are reused unchanged. The projected source Gram subtracts all 56 retained coordinates from the whole analytic source Gram; it represents the complete infinite high projection.

CC imports immutable source and positive-subspace certificates, validators, producer controls, terminology, custody and the DNE44 note with their original Git blob identities. It authenticates DNE44's source and positive-subspace audit hashes and their attachment to DNE43's original 0.603 floor, independently replayed in CC109. The inherited DNE audits contain 83,180 source checks and 26,401 subspace checks; these are not counted as new CC checks.

The new CC consumer passes **38,823 checks**, including rational inequalities and custody/structural checks. It freshly reconstructs all 7,744 primary/replay source entries across four 44x44 matrices from whole-source integrals minus retained-coordinate products. It verifies physical and projected norm bounds, the original operator remainder, coefficient rounding errors and every cross-source error payment, then checks primary containment of replay intervals. It checks that the replay's original 36-column native/source blocks, labels, masses and frame-certificate identity agree exactly with the authenticated DNE40 data used by CC109.

The source integrals themselves are not recomputed by CC110. DNE44's independently validated raw physical packet materialization and analytic/form-domain attachment remain inherited. CC's new work is a consumer audit of stored source arithmetic, exact positive-column retained ranks, congruences, prefix containment and physical-gap transfer. It is not a second analytic derivation.

## Collective comparison and exact containment

With Q44 the native form, G44 the complete paid high-source Gram, and k=603/1000, the uniform comparison is H44=kQ44-G44. CC uses the authenticated exact embeddings B and D, retaining all mixed terms in the full congruences. It freshly proves native positivity, B^t H44 B>0 and -D^t H44 D>0 by rational triangular congruences and outward rational Gershgorin margins. It checks the exact full rank of the joined embeddings (B,D), so the certified comparison inertias are:

| Parity | Positive retained rank | Negative comparison rank | Zero comparison rank |
|---|---:|---:|---:|
| Even | 42 | 2 | 0 |
| Odd | 43 | 1 | 0 |

The first 36 columns of B are exactly the identity prefix in each parity. Together with the unchanged physical frame and source block, this preserves the prior CC109 span. The exact physical columns in the authenticated DNE44 certificates have freshly checked retained-projection ranks 42 and 43. Coverage is therefore 85 within one compatible original frame; it is not a sum of ranks from unrelated frames.

## Physical transfer and remaining scope

For the fresh coefficient floor d of B^t H44 B, exact physical column-mass sum M and complete compressed source trace upper T, CC pays

    gap = min{(d/k)/(4(M+T/k^2)), k/2}.

The resulting fresh physical lower bounds are approximately 1.016409499746274e-38 even and 9.394560767285254e-34 odd. Both exceed 1e-38. Physical normalization uses actual exact physical column masses, rather than the native normalization. Complete exact fractions, source hashes and frozen congruences are recorded in `notes/data/RPB108_CC110_EXTENDED_PACKET_INTEGRATION_20261010.json`.

The remaining 27 retained dimensions split into 24 outside the two 44-column packets (12 per parity) and three comparison deficits inside them (two even, one odd). The full uniform 44-column criterion is rigorously rejected at the same floor by the negative comparison subspaces. This says nothing about negativity of the original operator. The highest certified whole-aperture anchor remains 21/20; whole 53/50, RH, F4 and Lean remain open.

## Implication for the source-response question

This extension closes by the plain remaining-source comparison on a larger positive subspace. It does not establish a collective packet where response succeeds while the plain same-floor comparison fails. The source-response correction remains algebraically positive semidefinite, and CC106's genuine original same-floor directional separation remains valid; neither establishes computational savings for a complete collective certificate.

CC110 supplies a sharper next target: test a complete response correction on the three certified comparison deficits in this exact Z44 frame, paying all positive/negative cross terms and the high-source response data at the certified 0.603 floor. A positive response-corrected full packet would demonstrate a strictly stronger collective certificate because plain H44 has proven negative inertia. Until that complete test is positive, collective separation remains unproved. Raising the scalar floor is an alternative route and would not establish same-floor separation.

Native NF55 resolves its earlier stored probes and freezes new ones, but uses a different physical frame. Its ranks and response data are not added to this original Z44 result. No Native or DNE branch receives writes.

## Reproduction

From the integration root:

```sh
python scripts/certify_cc110_extended_packet_integration.py --output notes/data/RPB108_CC110_EXTENDED_PACKET_INTEGRATION_20261010.json
```

Require PASS, exact source/certificate custody, both positive and negative comparison proofs, both physical retained ranks, identity-prefix containment and physical guards greater than 1e-38. Imported input custody and milestone custody record stored-byte hashes; compressed certificate references use decoded JSON hashes where specified.
