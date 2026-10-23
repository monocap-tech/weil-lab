# MG53 — Original 24D fixed-remainder direct-band repair ceiling

**Status:** Proposed structural diagnostic. No numerical claim is accepted until GitHub Actions independently replays the entire exact rational audit. Parent MG52 passed its original four-case proof-valid [4,8] same-cell multiplier cancellation and independent full24 Loewner replay in Actions #39813976498, but its PSD improvement was at most ~0.00975 trace on the four archived original source scenarios, far smaller than the inherited source certificate deficits.

## Precise mathematical question

The previous NF cycle rigorously improved the **new direct Fourier band [4,8]** while preserving all original source operators and frequency tails. Yet no original source contraction. Before refining individual cell error bounds again, MG53 asks:

**Can any further adjustment of ONLY the physical direct [4,8] covariance upper possibly establish original source 24D positivity, with the currently accepted MG52 response B and remaining-frequency source bound fixed?**

For each original 16/32-cell, k12/16 case, the independently accepted original complete 24D *valid* MG52 residual upper decomposes exactly as

```
U52 = U_[0,4] + U_[4,8] + U_rest,
```

where `U_[0,4]` and `U_[4,8]` are individually positive-semidefinite rational Loewner uppers for genuine original-source covariance `int R*R>=0`, and `U_rest` is the complete original |xi|>8 certified residual bound, including original seven-prime/digamma multiplier, physical pole correction, and entire original high tail.

Any **legitimate replacement upper** for direct [4,8] must itself dominate a PSD original source covariance, hence must be PSD. Therefore, with the specific `B` and `U_rest` fixed,

```
Hlo-(U_[0,4]+U_rest+U_new_valid)
    <= Hlo-(U_[0,4]+U_rest).
```

The right-hand side is the **optimistic ZERO direct [4,8] ceiling**, not a valid operator upper or a certificate. If even this optimistic ceiling is negative on an exact rational source vector, **no possible valid direct-[4,8]-only upper improvement** can make the fixed method's complete original source lower positive definite.

Stronger second diagnostic: even replacing BOTH direct original bands [0,4] and [4,8] by zero, the optimistic best-case source lower is

```
M_both_zero = Hlo-U_rest.
```

This is NEVER described as a valid source certificate; it is a mathematical **upper ceiling on source-lower positivity** for the fixed remainder and B, since all genuine direct physical covariance contributions are PSD.

## Exact acceptance protocol

Use original MG47 accepted MG43 rational negative source-certificate ray `v` as an independently fixed witness for every scenario. Compute exact original rational source charges

```
q_actual = vᵀ(Hlo-U52)v,
q_4to8 = vᵀ U_[4,8] v >= 0,
q_0to4 = vᵀ U_[0,4] v >= 0,

q_zero4to8 = q_actual+q_4to8,
q_zero_both = q_actual+q_4to8+q_0to4.
```

Do not infer that an archived MG43 witness is a true original operator negative mode. Only the tested conservative SOURCE certificate is classified, and even zero-band counterfactual classifications do not yield actual operator eigenvalues.

Check **exact rational PSD of each direct original 24x24 upper** and exact additivity of the full original upper and old source witnesses. Independently check rational sign witnesses of each hypothetical lower matrix. If q_zero4to8 or q_zero_both is negative, record the scope-restricted non-repair result precisely, without promoting it beyond the fixed response B and remainder.

## Research decision

- If the optimistic zero-[4,8] ceiling has a certified negative source ray in all cases, stop grinding direct same-cell frequency-radius refinements for the existing MG52 full-frequency architecture: changing only the direct [4,8] upper is mathematically insufficient.
- If the optimistic zero-[0,8] ceiling is still negative, even jointly perfecting both original measured direct covariances would not fix the inherited original missing-frequency/source moment/response obstruction.
- The useful next frontier is then to revisit the full original **remaining-frequency mass–first-moment coupling** or reconstruct a globally sharper original whole-source certificate around MG43, not to infer a negative true spectral mode.

No 470D strong inverse, signed odd 51/56, independent original Fourier/form/domain, complete even/Weil/CC27 or RH. All OPEN.
