# RPB108: whole-domain positivity across the first prime-7 threshold

Definitions: [actual eleven-panel Gram and corrected conversion](../docs/TERMINOLOGY_RPB108_PRIME7_GRAM96_0973.md). This completes the matched coupling test at aperture 973/1000 after the complete native block and eleven-panel source published in commits df6ce55bb542ef47632ede187873b4276b1ee952 and 3d40b852e2e2a71cbf7600c65574c811f2570a2d. Historical scripts and certificates remain unchanged.

The actual native form at 973/1000 now satisfies Q >= 8e-31 times physical mass and Q >= 3e-33 times Elog. The exact certified coercivities are approximately 8.955024755918063e-31 and 3.7312603149658594e-33. This advances the fixed-aperture whole-domain positivity frontier through the first prime-7 threshold. The stronger historical bounds at 97/100 remain intact.

Two fresh complete Gram constructions, each starting from an absent checkpoint, retain all eleven panels, all 96 source columns and projections, the universal endpoint logarithm and all smooth/mixed terms. Both final files and both cumulative checkpoints repeat byte for byte. Maximum residual entry width is approximately 3.037802123921003e-111. The decoded Gram SHA256 is 0f83c73059a45bdf62552b11868ecde09a91bffb74985c6958e3296a2131374c; the complete contraction checkpoint SHA256 is 460b3891c607b22a0657a651f1c093cd256ca045d16390a12406018330d8e3f5.

The source error eta remains approximately 6.599752767135603e-35. The surrogate residual norm bound is M approximately 6.055636543036702. Consequently the actual Gram correction delta=eta(2M+eta) is approximately 7.993140806334790e-34. The complete audit verifies every normalized column and the full error aggregation; no mixed source terms or prime-7 boundary profiles are omitted.

Independent exact endpoint-log projections check all 9216 native/source pairings with both enclosure widths and the actual source-column allowance. All 9216 displaced pairing controls are rejected. A second independent reconstruction uses closed binomial Legendre coefficients, rational endpoint-log-squared Hankel moments, 320 alternating terms for pi and 400-digit arithmetic. It reconstructs all 9216 residual entries directly from the saved contractions with exact integer projection intervals; every finer interval lies inside the saved enclosure, and all 9216 displaced residual controls are rejected. No old-aperture projection nesting identity is asserted for this changed aperture.

The independently proved complement c=423/500 gives a positive corrected Schur matrix Q96-(500/423)R96-[(500/423)delta+tau]I on all 96 coordinates, with tau=1/17179869184000000000000000000. The 160-digit constructor repeats byte for byte. A separate widened 80-digit audit rechecks every corrected pivot, all input hashes and the actual source correction. The lift integer bound is L=8. The exact full-domain conversion uses mu=tau*c/[tau+c(1+L^2)]; its 2-by-2 determinant is mu squared, while doubling mu gives a negative determinant. The negative diagonal control is also rejected.

The changed prime support requires a new logarithmic budget. The audit verifies log(7)<2a<log(8), prime powers 2,3,4,5,7, 2 times the sum of their amplitude ceilings approximately 5.852468364352818<6, a<1 and pole loss<12. Together with the existing archimedean lower bound m0>=w/10-6 this gives Garding constant 24=6+6+12. Thus kappa=mu/[10(mu+24)] exceeds the published 3e-33 floor. The old prime-5 Garding-23 condition is not reused.

The Gram, pairing and residual reconstruction audit flags describe the extraction stage before the sign decision. Final whole-domain standing is recorded in `RPB108_PRIME7_WHOLE96_0973_VALIDATION_20261007.json`, after the corrected sign and domain conversions have been checked.

Restore the complete gzip archives, verify their compressed and decoded hashes, and rerun the audits with:

```sh
python scripts/restore_native_prime7_source96_0973_archive.py
python scripts/restore_native_prime7_gram96_0973_archives.py
python scripts/validate_native_prime7_complete_gram96_0973.py notes/data/RPB108_PRIME7_GRAM96_0973_CERTIFICATE_20261007.json.gz notes/data/RPB108_PRIME7_GRAM96_0973_CERTIFICATE_20261007.json.gz notes/data/RPB108_PRIME7_GRAM96_0973_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz notes/data/RPB108_PRIME7_GRAM96_0973_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz
python scripts/validate_native_prime7_pairing96_enclosures_0973.py notes/data/RPB108_PRIME7_GRAM96_0973_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz
python scripts/validate_native_prime7_residual96_reconstruction_0973.py notes/data/RPB108_PRIME7_GRAM96_0973_CERTIFICATE_20261007.json.gz notes/data/RPB108_PRIME7_GRAM96_0973_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz
python scripts/certify_native_prime7_schur96_0973.py > schur0973_repeat.json
python scripts/validate_native_prime7_whole96_0973.py schur0973_repeat.json
```

Supplying the same archives twice checks custody, not a second fresh construction. Reproduce the fresh-repeat claim by running the Gram constructor twice with two distinct absent checkpoint paths and comparing both full outputs and checkpoints. The checkpoint codec now supports eleven completed panels, while the historical nine-panel codec is untouched.

[Custody manifest](data/RPB108_PRIME7_GRAM96_0973_CUSTODY_20261007.json) binds the full archives, new scripts, audits and unchanged dependencies. Concurrent global/F4 research is preserved. Next aperture trial requires new support/membership checks, complement and matched calculations. Global endpoint exclusion, F4, full transport and Lean formalization remain open; no RH claim.
