## MG37 — complete verified two-gate conclusion

**Original-source Young arithmetic:** [Actions #39499065523](https://github.com/monocap-tech/weil-lab/actions/runs/39499065523) **PASSED**, including independent exact Fraction audit of 128 original 32-cell × four rational B/cutoff source traces, original accepted MG36 full24 certificate [Actions #39495457084](https://github.com/monocap-tech/weil-lab/actions/runs/39495457084), complete-original-frequency physical pole/source scope and no spectral promotion. Accepted artifact `mg37-original-Young-exact-4case-trace-barrier` ID `12298393388`. Earlier MG37 original-data [Actions #39497690829](https://github.com/monocap-tech/weil-lab/actions/runs/39497690829) also passed (artifact ID `12298883726`), and standalone [#39497690630](https://github.com/monocap-tech/weil-lab/actions/runs/39497690630) passed.

| Original true source B | cutoff | MG32 complete upper trace benchmark | rigorous theoretical BEST Young-family full trace lower bound (optimistically free future rounding) |
|---|---|---:|---:|
| scalar tI | 2^12 | 63.50474075 | **67.22924788** |
| nonscalar ridge | 2^12 | 69.62469569 | **73.46733842** |
| scalar tI | 2^16 | 63.50474524 | **67.22925259** |
| nonscalar ridge | 2^16 | 69.57093939 | **73.39942798** |

**Original structural Loewner obstruction:** [Actions #39499065697](https://github.com/monocap-tech/weil-lab/actions/runs/39499065697) **PASSED** independent exact-Fraction four-case audit against separately accepted MG35, artifact `mg37-original-source-frozen-remainder-no-go` ID `12299416443`. The actual MG35 selected omitted-frequency upper for [4,8]/MG19 additions is THE SAME original MG32 omitted upper. Thus the NEW complete upper MATRIX is exactly old complete upper PLUS an additional original measured-band PSD upper. This cannot improve the full residual upper in Loewner order and its trace is strictly larger in all four cases, **independently of the Young optimal tau computation**. The structural no-go is stronger than a poor finite tau estimate.

**Correct interpretation:** This is a method impossibility for the fixed inherited remainder and fixed actual source-residual covariance decomposition, not an operator negative mode, not evidence about the truth/falsity of RH, and not a no-go for new independent omitted-frequency bounds. MG38 should prioritize a genuine sharp *original remaining-frequency joint covariance* certificate; it must demonstrate a full 24D matrix improvement before repeating any full 470D signed-inverse attempt.

W-ODD-NEG, full 470D strong inverse, 51/56 odd signed cap, independent Fourier/domain, even/Weil/CC27/RH remain OPEN.

---

## Implementation / verification checkpoint

- [PR #286](https://github.com/monocap-tech/weil-lab/pull/286) contains the exact original-source Young infimum diagnostic, separate self-contained mathematical regressions, and independently audited downstream calculation workflow.
- [MG37 standalone Actions #39497690630](https://github.com/monocap-tech/weil-lab/actions/runs/39497690630): **PASS**, including exact rational isqrt enclosures, a two-source synthetic exact optimal tau case P=4,E=9, and zero-error boundary.
- [MG37 original-data Actions #39497690829](https://github.com/monocap-tech/weil-lab/actions/runs/39497690829): **DEPENDENCY GATE ACTIVE**. The workflow requires BOTH successful completion and exact commit SHA of corrected MG36 Actions [#39495457084](https://github.com/monocap-tech/weil-lab/actions/runs/39495457084), then downloads its genuine full24 original artifact, verifies all 4 original B/cutoff cases and 32 source cells each (128 exact interval-cell trace infimum checks).
- Neither mathematical core selftest success nor the queued original-data workflow is a certificate that MG37's actual original-source trace barrier is above or below MG32. No original numerical Young-barrier value is claimed until the full accepted artifact is produced.

The underlying actual 470-source inverse, signed 51/56 odd cap, complete even/Weil/CC27/RH and independently accepted Fourier/domain identification remain OPEN.

---

# MG37 — Exact Young-parameter trace barrier in the original joint residual

October 20, 2026. Stacked on [MG36 PR #285](https://github.com/monocap-tech/weil-lab/pull/285). MG36's original source integral finished in its first Actions run #39491388570, but the independent audit failed solely on an exported full-matrix key mismatch. The actual calculation proved that **32/32 original [4,8] cells** preferred MG32 sourcewise Young to MG36's new covariance-error row-Gersh bound, for all tested original scalar/nonscalar B at k=12,16. Complete-source Gershgorin lower margins remain negative (~-19.35 scalar, ~-23.41 nonscalar). MG36 has corrected its schema, and its final accepted Actions proof is a strict prerequisite for this diagnostic.

## Answer a sharper structural question

Do NOT spend another costly 32-cell real-original Fourier integral on merely *guessing* a better Young parameter. The accepted MG36 source-error diagnostic **already provides exact rational data** sufficient to answer what the entire scalar-Young parameter family could achieve on upper TRACE.

For each original positive frequency cell of width `w` with genuine original pole-corrected source residual `q(xi)=v+d(xi-mid)+e(xi)`, `|e_i|<=rho_i`, the already proven directional-Young complete 24D Loewner **upper** has trace

```
f(t)=(1+t) P+(1+1/t) E,    t>0,
P=2w (sum_i v_i² +(w²/12)sum_i d_i²),
E=2w (sum_i rho_i)².
```

MG36 separately exports `f(t0)`, the accepted original `t0`, `w`, and `sum_i rho_i` for all 32 original [4,8] cells. Thus MG37 recovers `E` directly and `P=(f(t0)-(1+1/t0)E)/(1+t0)` with exact Fraction, and asserts `P>=0`. No source point is re-sampled, no inference about the original Fourier domain is added.

For positive `P,E`, the continuous best possible Young **trace** is exactly

```
inf_{t>0} f(t) = (sqrt(P)+sqrt(E))²
                = P+E+2sqrt(P E).
```

MG37 encloses the square root by *exact integer* `isqrt` on a known rational 10^-12 grid. No float eigenvalue or sampled trigonometric derivative enters. It also rationalizes a near-optimal t and evaluates its finite proposed upper trace from the exact Young formula, proving `inf <= proposal <= accepted old f(t0)`. This finite rational proposal is **not itself a new full original 24D matrix artifact**; the strict matrix spectral margin must be separately recomputed before any promotion.

## Frozen-assumptions whole-frequency trace barrier

MG35's PSD-monotone actual original omitted real-frequency covariance upper and MG32's accepted [0,4] direct source covariance are held fixed on the exact original rational response B. The MG36 independently verified *full complete-frequency upper TRACE* equals the sum of those two sectors and the accepted [4,8] measured upper.

The strongest trace achievable by *only tuning the Young parameter* (same source Taylor radii, original 32 frequency cells, same multiplier interval, same pole, same remainder) is bounded below by

```
F_min >= (accepted MG36 full trace - accepted MG36 band upper trace)
             +sum_32_cells [ P+E+2 lower_isqrt(P E) ].
```

This even grants **zero future 24D matrix-export rounding penalty**, making the barrier maximally favorable to the optimizer. Compare this rigorously with the independently accepted original MG32 [0,4] complete residual upper TRACE.

- If the barrier remains above MG32, no scalar Young t tuning can beat the older complete-frequency baseline on TRACE under these frozen premises. It does NOT prove the original true operator is negative or rule out a better fundamentally different matrix estimate.
- If the barrier falls below MG32, rigorously optimizing Young t warrants a full original 24D rerun with newly exported matrices and strict source positivity acceptance, not an automatic success claim.

**Prerequisite:** MG36 corrected run #39495457084 must finish successfully and publish its `mg36-true-original-direct-band-24D-full-residual` accepted artifact. MG37 will then require an independent exact-fraction CI replay of all four original 32-cell cases before being marked ready for review. No claim of numerical outcome in advance.

W-ODD-NEG, true all-470 original strong inverse, signed odd 51/56 cap, independently audited original Fourier/form/domain, complete even/Weil/CC27/RH remain OPEN.
