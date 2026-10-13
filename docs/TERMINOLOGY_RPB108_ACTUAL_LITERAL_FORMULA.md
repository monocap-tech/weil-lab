# RPB108 actual-divisor literal formula terminology

Definitions accompany their first local load-bearing use; earlier history is unchanged.

| Term | Definition and role |
| --- | --- |
| neutralActualZetaLiteraturePointEquiv | Identity equivalence between the actual open-strip zero subtype and the carrier of Zeta23.zetaZeros Zeta23.zetaSeam. Both predicates are riemannZeta ρ = 0 ∧ 0 < re ρ ∧ re ρ < 1. |
| Multiplicity correspondence | The external zeroMult and our neutralActualZetaMultiplicity are both analyticOrderAt riemannZeta ρ converted to ℕ. No simplicity assumption is used. |
| Ordinate correspondence | External gammaOf ρ = (ρ−1/2)/I equals our −I(ρ−1/2), so both use ρ = 1/2 + Iγ. |
| Transform correspondence | neutralRawTransform and Zeta23.paperFT have the same integral and positive exponent Izt for every complex z. |
| Divisor collapse | Summable.tsum_sigma collapses Σρ Fin(mρ); the inner finite sum is mρ times the sample. It is applied to the already certified summable inverse-correlation samples. |
| neutralActualZetaGreenPrimeForm | The literal von Mangoldt term Σn (Λ(n)/√n)(J(log n)+J(−log n)), evaluated on the exact constructed inverse correlation J_a(v,w). |
| neutralActualZetaGreenArchimedeanForm | (1/(2π))∫r H(J,r) gammaBracket(r), where gammaBracket = Re digamma(1/4+Ir/2)−log π. It retains the certified literal normalization. |
| Literal same-carrier arithmetic identity | Z_a(v,w) equals the existing canonical Green-image pole pairing minus the defined prime term plus the defined digamma term. It does not yet identify the prime/digamma terms with the existing Fourier multiplier source form. |

The definitions and six theorem bridges are in WeilDefect/Arithmetic/ActualZetaLiteralFormula.lean. Prime/digamma absolute-integrability, spectral dictionary and retained WD-T38 identity are not asserted by these names.
