# GERM-87 recovery and reporting correction — recorded during GERM-88

**Date:** 2026-09-28  
**Standing:** ADDITIVE CUSTODY / REPORTING CORRECTION; NO CANONICAL PROMOTION  
**Affected historical head:** 37d28daff273ff5bccfc96e225b759408682c5e7

## 1. Repository verifier versus executed bundle

At the affected head, tools/sz_post_c10_tenth_map_audit.py had Git blob e16a6cdf95200f91013658a471cbbc1b22a70aec. It contains malformed `els` plus backtick tokens, a changed conditional sign, altered composition calls, an incorrect extra target assertion, and output-label transcription changes. It cannot be the successfully replayed Python artifact described by the historical receipt. The prior statement that the repository verifier was byte-identical to the executed certificate is withdrawn.

The mounted GERM-87 certificate bundle supplied a different verifier. Its exact identifiers are:

```text
SHA-256: 7194b18fbfd427038f4fe5b73f5adcc46038f0cc8d89da82ae9c7d88025ea18f
Git blob: df63d04fc29402ca873a945c4c4962385e6eb121
stdout SHA-256: 9dad372a549c5d0c2a8e777ba071f792d1b3ad33db81eefd41725147572ca7d3
```

This bundled executable was run during GERM-88 with assertions enabled and exit code zero. Its complete stdout matches the historical receipt exactly. It has been restored to the repository without changing its bytes. The historical receipt's SHA-256 was for this bundled artifact; its Git-blob association was wrong. The old commits and original receipt remain historical records. This addendum is the recovery authority.

The bundled source validates the actual GERM-87 word domains and cone bounds. GERM-88 also re-proves that entire parameter strip directly from GERM-86 ninth equations. The GERM-87 exclusion interval and endpoint are not withdrawn or enlarged by the recovery itself.

## 2. Remainder-width reporting

The bundled output and historical note incorrectly reported that rho9 remained after L87=L86+omega10. The correct width to the GERM-86 eighth/ninth formula endpoint was

```math
(L_{85}+\sigma_8)-L_{87}=\rho_9-\omega_{10}
=0.00000000808051818639638649733314961753\ldots.
```

The larger value rho9=0.00000000875911804477083925517585367378... was the remainder at L86. This was a reporting error; the GERM-87 endpoint vector, word domains, and cone certificates are unchanged. The original bundled executable and output are preserved for reproducibility, including their superseded reporting field. GERM-88 computes the corrected width independently rather than importing that field.

## 3. Prose and word-display corrections

The GERM-87 eleventh rotation is y -> y+omega11 modulo c11, not the omega10 displayed in the corrupted repository note. Its actual executable uses omega11. The complete (s,N)=(4,5) chronological word is V,U1,U1,U1,U1; a shorter receipt transcription is not authoritative. The forward and inverse norm estimates use the same matrix representative and its actual inverse; malformed LaTeX in the old note is not a different mathematical statement.

All Q/R/S here remain GERM-86-local ninth matrices. A chronological word V,U0,...,U1 corresponds to a matrix product acting rightmost first; chronology is not permission to reverse the product order.

## 4. Standing

No ratification or public promotion occurs. Canonical cursor remains SZ-CROSS-COLLAR-3. GERM-88's proof and receipt supply the corrected endpoint bookkeeping and the new continuation. The restored GERM-87 script is a reproducible historical certificate, not a new theorem pass.
