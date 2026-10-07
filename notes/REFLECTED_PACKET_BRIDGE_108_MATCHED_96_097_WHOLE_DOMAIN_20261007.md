# RPB108: whole-domain positivity at aperture 97/100

Definitions: [96-vector Gram and corrected sign](../docs/TERMINOLOGY_RPB108_96_GRAM_SIGN_097.md). This completes the pending coupling test after the fresh 96-vector native/source milestone, commit 7593adb73042479f707be8d531244a57fd29c627. Historical 84-vector certificates, method obstructions and the 24/25 certificate remain unchanged.

At aperture 97/100, the actual native form now has whole-domain lower bounds Q >= (9/10^30) times physical mass and Q >= (4/10^32) times Elog. The computed exact physical and logarithmic coercivities are approximately 9.313225746154785e-30 and 4.049228585284689e-32. The 96-moment complement is 477/500; the matched corrected Schur form Q96-(500/477)R96-(500/477)delta96 I has certified positive shifted pivots on all 96 coordinates, with finite shift 1/2147483648000000000000000000. The lift norm integer bound is 7.

The complete nine-panel residual Gram was constructed twice from fresh, empty checkpoints. Both final Gram files and both complete checkpoints repeat byte for byte. All endpoint-log, smooth and mixed terms are retained. The largest Gram enclosure width is approximately 3.043023749626518e-114. Independent rational endpoint projections verify all 9216 source/native pairings, with both enclosure widths included; all 9216 displaced controls are rejected. The unchanged source error eta < 2e-34 gives actual Gram allowance delta=eta(2M+eta), approximately 2.4058756318183517e-33. This correction is subtracted in the sign test.

The first 84 source rows agree exactly with the historical 84-source certificate. An independent exact Hankel projection audit verifies all 7056 entries of R84 = R96 restricted to those rows plus the Gram of projection coordinates 84..95. This explains the surrogate residual reduction; the whole-domain result instead depends on the corrected sign and complement proof.

The Schur constructor uses 160-digit outward intervals and repeats byte for byte. A separate 80-digit reconstruction rechecks all 96 corrected pivots, actual source correction and exact physical conversion. The conversion determinant equals mu squared; doubling mu gives a negative determinant. A negative diagonal control is also rejected. The logarithmic conversion uses the independently checked Garding constant 23 at 97/100, including log(7)>2(97/100), prime loss <5 and pole loss <12. The published lower bounds are rounded downward from the exact rationals.

The Gram and pairing audit files intentionally describe the extraction stage before the sign decision. Their false/pending whole-domain flags are not a verdict on the subsequent Schur certificate. The final whole-domain validation is `RPB108_PRIME5_WHOLE96_097_VALIDATION_20261007.json`.

The complete raw checkpoints are in custody. GitHub's blob endpoint failed even for a small UTF-8 probe during publication, while tree writes worked. Accordingly the new gzip archives are transported as UTF-8 base64; the checkpoint is split into three ordered parts. Restore and verify both compressed and decoded SHA256 hashes with:

```sh
python scripts/restore_native_prime5_gram96_097_archives.py
python scripts/validate_native_prime5_complete_gram96_097.py notes/data/RPB108_PRIME5_GRAM96_097_CERTIFICATE_20261007.json.gz notes/data/RPB108_PRIME5_GRAM96_097_CERTIFICATE_20261007.json.gz notes/data/RPB108_PRIME5_GRAM96_097_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz notes/data/RPB108_PRIME5_GRAM96_097_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz
python scripts/validate_native_prime5_pairing96_enclosures_097.py notes/data/RPB108_PRIME5_GRAM96_097_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz
python scripts/validate_native_prime5_96_projection_nesting_097.py notes/data/RPB108_PRIME5_GRAM96_097_CERTIFICATE_20261007.json.gz notes/data/RPB108_PRIME5_GRAM96_097_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz
python scripts/certify_native_prime5_schur96_097.py > schur96_097_repeat.json
python scripts/validate_native_prime5_whole96_097.py schur96_097_repeat.json
```

Passing the same archived paths twice verifies archive integrity, not a new independent construction. To reproduce the recorded fresh-run claim, run the Gram constructor twice with two absent checkpoint paths and compare their full outputs and checkpoints. The recorded audit includes both original fresh runs.

[Custody manifest](data/RPB108_MATCHED_96_097_WHOLE_DOMAIN_CUSTODY_20261007.json) binds the new scripts, archives and audits. This advances the fixed-aperture whole-domain positivity frontier from 24/25 to 97/100. Further aperture enlargement needs new matched calculations. Global endpoint exclusion, F4, full transport and Lean formalization remain open; no RH claim. Concurrent global/F4 work and its historical wording are preserved.
