# RPB108 exact prime spectral transport terminology

Definitions and existing normalization precede their load-bearing use.

| Term | Definition and role |
| --- | --- |
| neutralActualZetaGreenPrimeSummand | The literal coefficient Λ(n)/√n multiplying J_a(v,w)(log n)+J_a(v,w)(−log n). |
| rightLimitPrimePowerFinset a | Existing finite prime-power set with log n ≤ 2a; equality-threshold prime powers are retained. This pass preserves that convention. |
| Prime cutoff identity | Outside the right-limit set, either Λ(n)=0 or both correlation samples vanish by their proved support in [−2a,2a]. |
| Spectrum S_a(v,w) | The already defined conjugate of the first Green L² Fourier transform times the second, using Mathlib's 2π normalization. Its L¹ integrability was already proved. |
| Symmetric phase dictionary | J(t)+J(−t)=∫ξ S(ξ)·2 cos((2πξ)t), derived from the same inverse integral and two unit-norm phases. |
| compactWindowPrimeCoefficient n | Existing coefficient 2Λ(n)/√n. The factor 2 is obtained from the two correlation samples. |
| rightLimitPrimeSymbol a t | Existing finite sum of compactWindowPrimeCoefficient n · cos(t log n), over rightLimitPrimePowerFinset a. |
| Exact prime spectral transport | The literal prime form equals ∫ξ rightLimitPrimeSymbol(a,2πξ)·S_a(v,w)(ξ). This is on the same Green Fourier carrier. |

All new declarations are in WeilDefect/Arithmetic/ActualZetaPrimeTransport.lean. This pass does not identify the digamma term with the archimedean multiplier or supply the retained WD-T38 source/null identity.
