# RC333 — Original signed degree-254 covariance; cumulative 252+254 residual

**Parent:** RC332 and independent SI11 integrated at \`c5f2550213e5c153f03d59e1b199f1fb09d4be5b\`. **Original operator:** CC27/RC313 signed Weil \(D\)-Riesz form with \(B=11/10\). **Ritz:** unchanged RC330 four-vector on degrees \(244,246,248,250\), not a new finite inverse.

## Exact degree-254 interface

RC333 computes the original \(C_{254,m}\), \(m=244,246,248,250\), from 28 native seven-prime translated Legendre overlaps in exact rational arithmetic. The calculation pays the real-log shifts, prime coefficient and moving-support uncertainties, original logarithmic endpoint, complete RC324 regular high compression and signed even pole in both canonical \(D\) normalizations. Independently it reconstructs \(b_{254}\) using RC323's signed Legendre coefficient recurrence and complete true-source error.

The target signed covariance is
\[
\langle P_{254}Tx,P_{254}CY_4x\rangle_D=b_{254}\sum_{m\in\{244,246,248,250\}}C_{254,m}y_m.
\]
It may be favorable, adverse or inconclusive. **No sign is assumed before exact Actions replay.** All resulting rational intervals and the sign classification are printed as deterministic diagnostics.

## Cumulative complete residual, not one isolated improvement

Unlike RC332, RC333 **preserves the already certified degree-252 split** as a frozen input. The complete original high residual is decomposed orthogonally into the four represented degrees, degree 252, degree 254 and every even mode \(n\ge256\).

The known degree-252 source and high-action energies are subtracted from independently certified whole-original source and cross-action norms before degree 254 is analyzed. Then \(b_{254}\) and the actual \(C_{254,*}Y_4\) are isolated, the remaining energy bound is conservatively charged through all \(n\ge256\), and the represented residual plus two signed residuals are summed in squares.

If the new degree-254 split weakens the upper bound, the prior complete RC332 bound is preserved exactly. The validator must maintain \(\|Tx-CY_4x\|_D<0.0012\) and the correct-sign RC314 penalty \(<0.00025\). New strict improvement, if any, is reported only from the exact computed inequality.

## Scope

This is original signed operator arithmetic conditional on the existing CC27/RC313 identification, not independent mathematical peer review. Even a favorable degree-254 covariance yields only a local improvement to a trial-dependent residual bound. The 278-mode high inverse, positive original low three-dimensional Schur **lower** bound, remaining 119 even and 195 odd low coordinates, Stage I, F4, Lean and RH are all **open**.

**Next RC334:** signed degree-256 covariance and more efficient accumulation of the remaining native signed high-head interactions while retaining every infinite mode.

**Reproduce:**
\`\`\`bash
python scripts/validate_rpb108_rc333_signed_254_cumulative.py --output certificates/rpb108_rc333_signed_254_cumulative.json --replay
\`\`\`
