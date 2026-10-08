# RPB108 NF11 / IP11 — Native retained matrix reconstruction at a=53/50, stage one

Date: 2026-10-08. Independent branch `research/rpb108-phase-geometry-localization`. Historical whole original positivity anchor: CC18 at `a=21/20`; fresh actual infinite physical F112 complement: NF10 `C_53/50 >= 17/100 I`. Read-only active Coupled mathematical parent last recovered CC38 `d679b712df8485411a760519a5b563d1dd4f2d47`. Paused Global NF71 and Shadow PS3 untouched.

**Result (evaluated, A):** The complete original six-prime-power translation contribution to the first EIGHT normalized physical Legendre modes at a=53/50 has a rigorously enclosed interval 8x8 matrix. Both translation orientations of the prime powers {2,3,4,5,7,8} are included, with Lambda(4)=Lambda(8)=log2. All even–odd crosses vanish exactly. The first two diagonal entries match independent original translated-overlap formulas from NF9, and the entire 8x8 matrix passes a separate numeric Gaussian-quadrature sanity check at 28 nodes. The finite prime submatrix is new arithmetic data at the enlarged aperture.

**Result (scaffolding, NOT evaluated):** A fresh target-specific FULL native 112-row interval constructor and a resume/checkpoint wrapper have been added as separate scripts. Their new target guards and six-prime support code have been statically audited, but the expensive full source has NOT been executed: no whole 112 native entries involving the archimedean/pole terms, no full native matrix sign, no original source/action Gram, no corrected Schur sign, and no new whole-domain positive aperture are claimed.

## 1. Exact low-eight prime matrix and independent verification

Set a=53/50, q_n=log(n)/(2a), c_n=Lambda(n)/sqrt(n), and normalized physical Legendre basis e_j(x)=sqrt((2j+1)/(2a)) P_j(x/a), 0<=j<8. The ORIGINAL finite prime translation part has

\[
Q_{\rm prime}(e_i,e_j)
=-\sqrt{(2i+1)(2j+1)}
\sum_{n\in\{2,3,4,5,7,8\}}
 c_n\,[I_{ij}(q_n)+I_{ji}(q_n)],
\]
\[
I_{ij}(q)=\int_0^{1-q}
  P_i(2u-1)\,P_j(2(u+q)-1)\,du.
\]

Use the exact shifted Legendre polynomial identity
\[
P_j(2u-1)=\sum_{k=0}^j(-1)^{j-k}{j\choose k}{j+k\choose k}u^k.
\]
Polynomial composition, finite integration, 250-term positive atanh logarithm enclosures, 120-digit rational square-root enclosures, and directed rational operations produce the full 8x8 interval matrix. The committed producer emits all 36 symmetric lower-triangle interval entries at a 10^-40 grid; its internal interval widths are <10^-58. No pointwise numerical quadrature is used to PRODUCE the interval certificate.

Reconstruction/validation: [exact 8x8 prime matrix producer](../scripts/certify_native_prime8_lowblock_nf11_106.py), [independent closed-form validator](../scripts/validate_native_prime8_lowblock_nf11_106.py), [selected exact interval manifest](data/RPB108_NF11_LOW8_PRIME_MATRIX_106_20261008.json).

Representative entries (the ORIGINAL prime-only contribution, NOT the full Q):
- Q_prime(e0,e0) in [-1.9876777177172331407676724869358827027456,-1.9876777177172331407676724869358827027455].
- Q_prime(e1,e1) in [+1.4531067120911515804754440737629005832747,+1.4531067120911515804754440737629005832748].
- Q_prime(e0,e2) about -0.49886864742045428106.
- Q_prime(e1,e3) about -0.23087016530783618566.
- Q_prime(e2,e2) about +0.48874250579137313690.

The degree-0 and degree-1 terms independently equal
\[
-2\sum_n c_n(1-q_n),\qquad
-2\sum_n c_n(1-3q_n+2q_n^3)
\]
respectively, in agreement with NF9. Independent 28-node Gauss-Legendre polynomial overlap integration at standard floating precision disagrees with the interval midpoints by at most 4.311e-15 across all 64 entries. This is an INDEPENDENT numerical sanity check, not a replacement for rational enclosures. The raw exact-rational 8x8 producer passed and independent closed-form rational tests passed. The 12-mode brute polynomial interval algorithm was attempted but did NOT finish in the available run window; it is NOT a theorem failure or evidence that the 12-mode block is nonpositive.

## 2. New target-specific full native producer (prepared, NOT run)

The original CC18 `certify_native_legendre112_105.py` accepts only 21/20. NF11 makes a separate target engine:
- [native 112 Legendre engine for 53/50](../scripts/certify_native_legendre112_106.py),
- [full native interval-matrix wrapper with SHA-bound checkpoints](../scripts/certify_native_prime8_matrix112_nf11_106.py).

The port retains the ORIGINAL correlation polynomials, logarithmic endpoint integrals, both pole moments and the six original prime-power terms, with a new target-only guard. It replaces the old exponential majorant 67 and kernel allowance 21/4 by target-appropriate conservative choices 70 and 53/10. Since `4a=106/25=4.24<log70`, `4a<6` and `log8<2a<log9`, the stated support and truncation guards remain in their intended chamber. The old source tree and SHA-pinned 21/20 outputs are untouched.

The wrapper writes a bound-to-source incomplete checkpoint after each completed native row and supports an explicit `--max-rows` prefix. It must not call a prefix matrix a full certificate. On eventual completion it checks exact parity, interval widths, and attempts a finite 112 positive-pivot audit; a failed sufficient pivot is reported as **not certified**, never labeled an actual negative original Weil vector.

This port needs runtime validation against the target-specific source files before any new native matrix certificate can be accepted. No source-operator reconstruction, action-row Gram or infinite Schur lower has been produced. The target's existing NF10 complement lower is c=17/100, much smaller than CC18's 699/1000, so even a positive finite retained matrix may not close the source-corrected full sign.

## 3. Jurisdiction, decision and NF12 gate

**Proved:** a fully evaluated 8x8 original prime-only matrix at a=53/50, independent rational low-mode checks, parity reflection and an independent numerical quadrature crosscheck. **Prepared:** target-specific 112 native matrix construction with resumable checkpoint, but not executed. **Unproved:** full native 112 signed matrix, its positivity, entire original source/action Gram, full Schur correction and whole-domain positivity a=53/50.

Next NF12 should run the NEW target full native producer with a SHA-bound prefix checkpoint (e.g., 4 or 8 complete rows), independently validate those COMPLETE archimedean + prime + pole entries, then continue in checkpointed batches through all 112 rows; do not attempt the slow brute-polynomial prime-only path beyond its audited 8 rows. Once complete, the next distinct requirement is to reconstruct fresh actual positive-source action/Gram and signed even/odd Schur tests under the true NF10 physical complement `c=17/100`. A finite matrix positive pivot is not itself a whole-domain sign.

Certified original whole-domain positivity stays a=21/20, even0/odd0. RH/F4, global non-stalling, full transport, Lean closure remain open. Coupled is sole active integration frontier; this remains an independent computational check and read-only handoff.

## Subsequent NF12 complete native finite sign

[NF12 — complete original signed native low16 positive certificate](REFLECTED_PACKET_BRIDGE_108_NATIVE_LOW16_NF12_20261008.md) independently reconstructs all original archimedean, six-prime and signed-pole entries for physical normalized Legendre degrees 0..15 on the new aperture a=53/50. The 16x16 original interval matrix passes exact rational shifted LDL, yielding a rigorous finite low16 physical bound >5e-13. The new optimized kernel-moment integration overcomes NF11's brute prime-only 12-mode timeout. It still does **not** supply the full native 112, target source/action Grams, corrected whole Schur sign, or original whole-domain positivity at 1.06. The NF10 complement c=17/100 and CC18 1.05 archive are unchanged.
