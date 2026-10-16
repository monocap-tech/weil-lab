# RC333 — Original signed degree-254 covariance; cumulative 252+254 residual

**Parent:** RC332 and independent SI11 integrated at \`c5f2550213e5c153f03d59e1b199f1fb09d4be5b\`. **Original operator:** CC27/RC313 signed Weil \(D\)-Riesz form with \(B=11/10\). **Ritz:** unchanged RC330 four-vector on degrees \(244,246,248,250\), not a new finite inverse.

## Exact degree-254 interface

RC333 computes the original \(C_{254,m}\), \(m=244,246,248,250\), from 28 native seven-prime translated Legendre overlaps in exact rational arithmetic. The calculation pays the real-log shifts, prime coefficient and moving-support uncertainties, original logarithmic endpoint, complete RC324 regular high compression and signed even pole in both canonical \(D\) normalizations. Independently it reconstructs \(b_{254}\) using RC323's signed Legendre coefficient recurrence and complete true-source error.

The target signed covariance is
\[
\langle P_{254}Tx,P_{254}CY_4x\rangle_D=b_{254}\sum_{m\in\{244,246,248,250\}}C_{254,m}y_m.
\]
The exact GitHub Actions replay establishes the **strictly negative original signed covariance** (an adverse sign for this unchanged four-mode trial):

\[
-2.425855412138193\times10^{-10}
<b_{254}(CY_4x)_{254}
<-1.072405329512688\times10^{-10}<0.
\]

The signed source itself is positive, \(b_{254}>1.0034161\times10^{-4}\), while the original four-mode action is negative, \((CY_4x)_{254}<-1.06875\times10^{-6}\). The full exact rational source, four cross entries, action, covariance and residual intervals are frozen in the certificate. This sign is not conjectured from RC329.

## Cumulative complete residual, not one isolated improvement

Unlike RC332, RC333 **preserves the already certified degree-252 split** as a frozen input. The complete original high residual is decomposed orthogonally into the four represented degrees, degree 252, degree 254 and every even mode \(n\ge256\).

The known degree-252 source and high-action energies are subtracted from independently certified whole-original source and cross-action norms before degree 254 is analyzed. Then \(b_{254}\) and the actual \(C_{254,*}Y_4\) are isolated, the remaining energy bound is conservatively charged through all \(n\ge256\), and the represented residual plus two signed residuals are summed in squares.

If the new degree-254 split weakens the upper bound, the prior complete RC332 bound is preserved exactly. The validator must maintain \(\|Tx-CY_4x\|_D<0.0012\) and the correct-sign RC314 penalty \(<0.00025\). The n254 covariance is adverse, so its isolated residual is larger than its uncorrected source coefficient. **Nevertheless the cumulative original high residual UPPER bound improves** through orthogonal Parseval accounting:

| Complete original residual norm | Certified bound |
|---|---:|
| Inherited RC332 (signed n252 only) | \(<0.001150859\) |
| RC333 (signed n252 and adverse n254) | \(<0.001150649\) |

The corrected-sign RC314 penalty is \(<0.000243992\), versus RC332's \(<0.000244081\). The improvement comes from less wasteful whole-space norm accounting, **not** from beneficial signed cancellation at degree 254. This remains weaker than the distinct RC328 three-mode residual certificate.

## Scope

This is original signed operator arithmetic conditional on the existing CC27/RC313 identification, not independent mathematical peer review. Even a favorable degree-254 covariance yields only a local improvement to a trial-dependent residual bound. The 278-mode high inverse, positive original low three-dimensional Schur **lower** bound, remaining 119 even and 195 odd low coordinates, Stage I, F4, Lean and RH are all **open**.

**Next RC334:** certify the genuine original n254 diagonal and test whether a positive original signed five-mode Ritz extension can absorb this adverse direction, or whether continuing signed n256 covariance is more efficient. Keep the n252 signed split and infinite remainder.

**Reproduce:**
\`\`\`bash
python scripts/validate_rpb108_rc333_signed_254_cumulative.py --output certificates/rpb108_rc333_signed_254_cumulative.json --replay
\`\`\`
