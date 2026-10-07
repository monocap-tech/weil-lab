# RPB108: complete matched Gram at 49/50 and scalar Schur obstruction

The full eleven-panel residual Gram is certified and independently audited. The scalar Schur route with the proved complement 104/125 fails rigorously. Whole-domain positivity remains certified through 973/1000, with the previously published physical bound 8e-31 and logarithmic bound 3e-33 Elog. No actual negative Weil-form vector is claimed. F4 remains open.

## Complete construction and enclosure custody

Two fresh constructions started with distinct absent checkpoints and completed all eleven panels. The complete Gram outputs and complete checkpoints match byte for byte. All endpoint-log, smooth and mixed terms are retained, with polynomial integration degrees derived from the complete 90/104 source. The maximum residual entry width is approximately 1.503465e-111.

The complete checkpoint contains 27648 outward entries across its three contraction matrices. Independent audits pass all 9216 native/source pairings with both enclosure widths accounted for, and all 9216 residual reconstructions using closed-binomial Legendre coefficients and independently enclosed endpoint-log-squared moments. All 9216 displaced pairing controls and all 9216 displaced residual controls are rejected.

The source allowance is eta approximately 5.254942e-35. The trace bound gives M approximately 6.241213 and the actual operator allowance delta=eta(2M+eta) approximately 6.559442e-34. These values are derived from the hash-bound complete native and source inputs. Extraction-stage flags in the Gram audits precede the final obstruction decision below.

## Rigorous sign decision

Both 160-digit interval Schur tests failed before source correction. A 150-digit decimal midpoint LDL search supplied candidate coordinates; those floating calculations are not proof evidence. The published vector has 96 exact rational coordinates. Its quadratic enclosures are computed from all saved native and residual intervals, then independently checked using the 4656 lower-triangular terms.

For that vector, native Q is approximately 2.322011e-27 and residual R approximately 1.985884e-27. Its squared physical coordinate norm is approximately 2.700761. At c=104/125, the surrogate Schur value is at most approximately -6.486881e-29. Allowing the full source perturbation in the direction most favorable to positivity still gives

\[
v^*(Q-c^{-1}R_{\rm actual})v
\le v^*(Q-c^{-1}R_{\rm surrogate})v+c^{-1}\delta\|v\|^2
<-6.48\times10^{-29}.
\]

Thus this is an obstruction to the scalar complement Schur bound, rather than an interval-pivot precision failure. Subtracting the required source correction and any positive margin cannot restore its positivity. The witness and its exact-rational repeat match byte for byte; an independent triangular audit passes, including a positive-shift control.

This vector alone imposes the necessary scalar complement condition

\[
c>\frac{\underline{v^*R_{\rm surrogate}v}-\delta\|v\|^2}
          {\overline{v^*Qv}}
>0.85524.
\]

The published rational lower bound is 0.832 and its unrounded lower bound is approximately 0.83271743. Both are rejected by the witness. The displayed 0.85524 threshold is necessary for this vector; it is not a sufficient threshold for all 96 directions.

## Reproduction and next gate

The custody manifest records compressed and decoded SHA256 values, all twelve base64 transport parts, every new script/audit file, and unchanged arithmetic dependencies. Restore archives with `scripts/restore_native_prime7_gram96_098_archives.py`. The runtime checkpoint is plain JSON despite its `.gz` suffix; the published checkpoint archive is actual gzip. The decoded checkpoint bytes are preserved exactly.

Run `scripts/certify_native_prime7_schur96_obstruction_098.py`, then `scripts/validate_native_prime7_schur96_obstruction_098.py`. The full-Gram, pairing and residual auditors accept their documented checkpoint arguments. `scripts/certify_native_prime7_schur96_098.py` remains the positive-sign test; it rejects the current inputs at its uncorrected pivot gate and produces no positivity certificate.

The next aperture gate is a stronger complement estimate or a stronger coupling method. Increasing decimal precision or merely rounding the existing complement cannot suffice. This obstruction concerns a sufficient block lower bound and does not establish a negative value of the actual whole-domain Weil form. Global endpoint exclusion, F4, full transport, Lean formalization and RH remain open; concurrent global work is preserved.
