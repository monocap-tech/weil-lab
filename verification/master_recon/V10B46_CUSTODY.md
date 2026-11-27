# V10B46 — optimized constraint custody and conditional receiver

Status: independent repository-source arithmetic replay PASS; V10B46a/b/c staged, not compiled.
Source: V10B45 coordinate JSON commit ff02606408804d992bc0539786d719db7936248a (blob 3887cf6428125c3fba5eb6587c53df4a3f57613d).
Native integer bank commit aff051a048922ed76f5293b0978a1fdb9e3327ac (blob fd85d71fa26a5d152e2912c725f5bd1f420908ee).
All 2560 native trial integers match the JSON bank exactly.

Independent replay retrieved the committed JSON, reconstructed all physical monomial numerators with arbitrary precision integer binomial sums, and serialized the historical V10B29 representation.
377528 bytes; SHA256 1fea00167929e3f5312c16dcd680154a34ead4b8934a520c7a23fd60e79e8c5f, matching V10B29 receipt. No original V10B19 ZIP authentication asserted.
Reproduction: python3 verification/master_recon/v10b45_optimized_coverage.py

V10B46a (970ec1d453a3bf9b3474ef40d336a2810214352d): certified V10B34a Rodrigues formula as dependency; weighted moment comparison, I_j/I_15 <= 1/256 for j>=17.
V10B46b (5de82290fafb113be2515e22405764d75b30101a): integer leading matrix and column reserve, conditional complex surjectivity.
V10B46c (03de232e83ad5fbccc2d09664d74a45bcd39be9c): high-mode correction and conditional optimized section.

Required literal row identity: after multiplying the physical unit-interval pairings by the dyadic denominator and row factors 2i+1 (and undoing physical measure and load-normalization factors), row i<15 equals the leading trial integer; row 15 equals the leading trial integer plus the odd higher-mode sum of trial integers times I_j/I_15. This identity must be attached to the actual supported trial map and its kernel. The orthogonality/diagonal and parity/deflation attachments remain outstanding. No physical energy or residual congruence adoption. Arithmetic ADOPT 0.
Active audits pinned before V10B46: 45927665008 and 45928064611; not interrupted.
