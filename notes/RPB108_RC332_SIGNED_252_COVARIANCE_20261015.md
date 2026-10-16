# RC332 — Actual original signed n252 outside-high covariance

**Parent:** RC331 integrated and SI09 at \`c62d6d2f7d37cab17586062ab9e60e1a2b7d4dbf\`.  
**Operator:** original CC27/RC313 signed Weil \(D\)-Riesz form at \(B=11/10\).  
**Target:** retain RC330's actual four-mode Ritz vector in \(\{244,246,248,250\}\); compute the original first omitted high coordinate \(n=252\), with signed source and cross-action, without discarding the full \(n\ge254\) complement.

## Construction

For each \(m\in\{244,246,248,250\}\), compute the original signed seven-prime translated Legendre offdiagonal with exact rational-center overlaps and all original true-log, prime-weight, endpoint-displacement and polynomial-derivative error budgets. Add the genuine logarithmic endpoint coefficient, the full high/high RC324 regular-kernel enclosure, even-pole rank-one term and both canonical \(D\) normalizations. This uses 28 exact polynomial integrals and no auxiliary positive matrix.

Independently reconstruct the original \(b_{252}=\langle v_{252},Tx\rangle_D\) from the signed RC323 Legendre interval moment recurrence, original boundary endpoint terms and the complete original physical-to-\(D\) source error. Contract the four exact original \(C_{252,m}\) intervals against **RC330's frozen rational four-mode \(Y_4x\)**. Determine the rigorous signed covariance \(b_{252}(CY_4x)_{252}\) and signed residual \(b_{252}-(CY_4x)_{252}\).

This first pass uses GitHub Actions to compute and print all exact rational source/coupling/covariance intervals. Their exact values and any certified sign must be read from the replay output; no sign is assumed from RC329's adverse degree-250 result.

## Infinite residual and explicit limitations

The entire \(n\ge254\) complement remains rigorously accounted for using RC328's full original signed \(\|Tx\|\) and RC331's original four-input-to-infinite-high-action norm bound. Subtract only the known **squared minimum** source and high-action energies at the isolated \(n=252\), and combine it with the signed residual by orthogonal Parseval. Retain the prior unsplit bound if the local split is unfavorable.

The validator enforces an original complete infinite residual norm \(<0.0012\) and a corrected RC314 residual penalty \(<0.00025\) for the unchanged original four-mode Ritz trial. These are the current coarse **caps**; reporting an improved cap or a covariance sign requires observing the actual signed interval output.

**No full original \(C^{-1}\)**, no positive original three-dimensional low Schur lower bound, no full 278-high finite positivity, Stage I, F4, Lean or RH result is asserted. The isolated signed covariance is a local calculation, not a global Schur certificate.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc332_signed_252_covariance.py --output certificates/rpb108_rc332_signed_252_covariance.json --replay
\`\`\`

When GitHub Actions succeeds it validates the exact source intervals and the inherited Git-blob custody; this is not independent mathematical peer review.
