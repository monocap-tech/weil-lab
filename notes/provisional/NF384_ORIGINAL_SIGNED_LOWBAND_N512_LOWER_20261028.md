# NF384 — Original n512 signed response forces a nonzero low-band norm

**Standing:** exact-rational original-data source-reuse reduction, conditional on inherited original strong-domain realization. `W-ODD-NEG`, even, whole Weil, RH **OPEN**. Previous NF383 PR #368; no original n513 result.

## Original data

The *unchanged* certified NF380 complete signed seven-prime/arch/pole original n512 native report has SHA256 `9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b`. It records positive `b=Wodd(u4,q_perp)≈1.375270261268512e-13` and `g=||q_perp||²≈1.085542249619544`, with 16 physical and 32 signed native overlap checks. Here `q_perp=(I-P_(J242+F4))v512`.

The *unchanged* NF375 cutoff report has Git blob SHA1 `03c709571046d3f09307614aaded9749f5a15ba1`, original source SHA256 `abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770`, and native source SHA256 `a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559`. It contains five accepted **high-frequency norm upper bounds** for the identical original matched NF370 fourth trial `u4=f_(Te4)-w4`, with lowband still uncomputed.

## Exact Hilbert estimate

Assuming the inherited signed strong-domain/continuum identity, define `l_L=P_I F^-1[1_(|xi|<=L) m(xi) u4hat]`, `h_L=P_I F^-1[1_(|xi|>L) m(xi) u4hat]`. For all `j∈J242`, the original odd pole lies in J242 and `q_perp⊥J242`, so

`|b|=|<l_L+h_L-j,q_perp>| <= (||l_L-j||+||h_L||)*sqrt(g)`.

Consequently for the **actual original signed lowband residual norm** `H4(L;j)=||l_L-j||`,

`H4(L;j) >= max(0, |b|/sqrt(g)-high4(L))`.

Here `high4(L)` is the accepted NF375 original high-frequency Fourier bound. The test avoids square-root rounding: for proposed strict lower `L0>=0`, check the exact `b_lower² > g_upper*(high4+L0)²`.

## Replayed original threshold comparisons

| Cutoff | Strict H4 lower for every j in J242 | NF375 unmeasured future H4 upper target |
|---|---:|---:|
| 2^20 | No nonzero lower from this witness | 1.5e-13 |
| 2^21 | >2.1e-15 | <2.0e-13 |
| 2^22 | >3.85e-14 | <2.5e-13 |
| 2^23 | >6.46e-14 | <2.7e-13 |
| 2^24 | >8.34e-14 | <2.8e-13 |

All four positive comparisons passed independently by exact BigInt rational inequalities on the original native NF380 and NF375 GitHub file contents. A pinned stdlib Fraction replay is committed at `scripts/local_replay/nf384_original_lowband_n512_lower.py` with dedicated CI. **Remote CI not yet claimed green.** This one-witness test does **not** exclude any of the five NF375 future upper targets; a certified lower below a target cannot certify its upper.

## Stop and next

The n513 native action #40820718599 and independent NF381/382/383 workflow checks remained queued when inspected; no new original signed n513 measurement or low-band upper is claimed. The original **lowband lower** is real scoped information (assuming inherited source-domain identification), not a numerical integration or a sign theorem. The next useful test is an actual correlated original J242-subtracted signed lowband **upper** / complete form-dual upper for the same four NF370 directions, rather than another harmonic witness scan.

The 49 historic NF356–364 files, all original sources, 30,371 archived signed cells and existing source hashes are unchanged. No main merge, no RH promotion.
