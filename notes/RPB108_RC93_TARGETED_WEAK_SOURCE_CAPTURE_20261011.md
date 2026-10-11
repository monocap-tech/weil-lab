# RPB108 RC93 — Targeted weak-source capture

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC92, commit `419256f6878f3f74a19d0c136e679f831948f047`.

RC93 improves the complete original-source coupling upper on each known weak span. It contracts signed source and residual intervals onto the fixed RC63 combinations before applying interval row bounds, and subtracts a physical polynomial of degree below 64 using existing RC83 source pairings. No new integrations or dense 64-feature Weil-head evaluation are required.

Both resulting 2×2 coupling uppers improve the RC91 uppers in the whole Loewner order. The four directional coupling uppers decrease by approximately 45–76%. Both corrected weak Schur blocks remain unresolved. A new exact obstruction shows that every positive scalar Young weighting of these fixed nominal/transfer enclosure components fails all four directional Schur tests, even against the RC92 head upper endpoints. This is a limit of this enclosure family, not an actual leakage lower or a negative actual Schur result.

## Physical capture without dense head evaluation

Write F_nom=q+K_nom V64 for the unchanged complete original physical source on the RC67 trials. RC83 encloses <P_n,F_nom> for n<64, including the archimedean source, all prime translations, the signed pole and their correlations. Let H_c be their centers, r_H their radii, and m_n=2.2/(2n+1) the exact physical Legendre masses.

After contracting the 22 native source inputs onto two fixed weak vectors in each parity, choose the physical subtraction coefficients c_n=H_c,n/m_n. The residual Gram center is

    W_c = U_c − H_c^T diag(1/m_n) H_c.

The actual nominal residual is F_nom−sum_n c_n P_n. Because these subtraction coefficients are fixed rational centers, the pairing error enters linearly: entry (i,j) pays

    r_U,ij + sum_n (|H_c,ni| r_H,nj + |H_c,nj| r_H,ni)/m_n.

There is no unpaid quadratic pairing error. Symmetric weighted row bounds then give a physical residual Gram upper. Unlike RC71, the interval contraction occurs before the 22-input row inflation. All signed covariance centers are retained.

The canonical image i* of every subtracted physical polynomial lies exactly in the actual Riesz head H64=i*P_<64. Consequently this residual controls the actual projection complement. H64 is nested inside H1250, so its coupling upper also bounds the rank-1250 coupling. Evaluating the original Weil restriction to H64 is unnecessary for this source-side argument.

This is a coupling result on four specified inputs, not a positivity certificate for an enlarged head. No rank-64 Weil complement floor is claimed.

## Rank-64 canonical tail bound

A canonical vector orthogonal to H64 has a physical embedding orthogonal to all Legendre polynomials of degree below 64. The Fourier plane-wave remainder gives, at each rational cut L,

    theta64(L) <= 4 B L (2 pi B L)^128 /
                  ((129!!)² [1−(2 pi B L)²/131²]),

with B=1.10. Theta is rounded upward and capped at 1. A lower staircase for log(e+|xi|), with frequency steps 1/50, sums the guaranteed high-frequency energy. All infinite Legendre tails are included. The rational logarithms are checked by an independent positive atanh series in replay, and the double factorial by its factorial identity.

The staircase closes after 360 layers at L=7.2 and proves a canonical-complement embedding norm upper of approximately 0.6613593207, improving the rank-38 value 0.7155746334. The exact norm upper, energy lower, e/pi enclosures and every frequency layer are saved in the certificate.

The inherited archimedean polynomial remainder, full prime norm and projected pole estimates each contain one complement embedding factor. The same degree-below-38 subtractions also lie in H64. Thus their factors may be multiplied by tau64/tau38, with no second tail factor. RC93 retains the inherited physical source and operator approximation errors.

## Weak Riesz-error transfer before row bounds

The RC81 residual intervals are expressed on Legendre targets. If C is the native Chebyshev-to-Legendre map and W the two-column fixed weak basis, the correct target coefficients are C W. RC93 contracts the full signed residual interval matrix by these coefficients before the row bound, rather than contracting its already inflated native upper.

Let E_p be the resulting actual physical Riesz-error Gram upper and T the weak physical trial Gram. With nu=1/65536, delta_L the RC81 operator-correction norm and delta_K the RC68 source-approximation error, the physical Riesz error is transported exactly as in RC81. The projected source transfer upper is

    E64 = rho (1+nu) k64² E_p
          + (1+1/nu) delta_K² tau64² T,

where rho=252/257 and k64 is the inherited projected remainder factor, divided by sqrt(rho), scaled by tau64/tau38. The nominal projected residual upper is N64=tau64² W_upper.

Weighted interval scales (100,1) and (80,1) retain the disparate weak-mode magnitudes. The resulting 2×2 uppers are checked by exact PSD tests; no floating eigenvalue is accepted.

## Results and the decisive enclosure obstruction

For each parity, RC93 tests a rational positive Young grid and minimizes the coupling upper relative to the unchanged RC92 full weak-head lower. The accepted matrices are

    A(t)=(1+t)N64+(1+1/t)E64.

The selected parameters are 7/16 for even and 1/4 for odd. Each matrix is an actual rank-64 coupling upper and, by nesting, a rank-1250 coupling upper. Each improves its RC91 weak block in the whole Loewner order.

| Direction | New coupling squared upper | Reduction from RC91 | Family lower / (alpha × head upper) |
| --- | ---: | ---: | ---: |
| even weak_0 | 4.18941564e-18 | 76.033% | 1.746421 |
| even weak_1 | 2.49256818e-14 | 45.356% | 1.112704 |
| odd weak_0 | 8.88016046e-17 | 73.612% | 1.000524 |
| odd weak_1 | 1.20804501e-12 | 62.979% | 1.970642 |

Here alpha=247/2500 is the inherited rank-1250 Weil complement floor. The last column is an exact sufficient-method obstruction, displayed approximately. For a fixed direction let n=N64,ii and e=E64,ii. Every t>0 satisfies

    A(t)_ii >= n+e+2 sqrt(n e).

A downward rational square root certifies a lower endpoint for this expression. On each of the four directions that endpoint exceeds alpha times the RC92 actual head upper. Thus no positive scalar Young weighting of these fixed enclosure components can make even that directional corrected Schur value positive, regardless of further head precision within RC92's enclosure.

This lower endpoint belongs to an upper-enclosure family. It is not a lower bound on the actual rank-64 or rank-1250 coupling. An alternative signed source/transfer correlation estimate, better nominal source capture, or a different projection can change the family.

The whole corrected weak lower Q_W,lower−A(t)/alpha is not positive in either parity. Actual corrected-block negativity is not proved.

## Next mathematical obligation

The transfer-only hypothetical comparison Q_W,lower−E64/alpha is positive definite in both parities. This is a diagnostic for zero nominal residual; the nominal residual is not zero and no positivity certificate follows from the diagnostic. It shows that the current transferred Riesz-error allowance alone does not force failure of the weak-block test.

The next useful theorem should control the nominal source beyond the degree-63 physical capture, or retain signed nominal/transfer correlations rather than apply a norm-only Young attachment. The original prime support boundaries and archimedean endpoint structure are concrete candidates for a source-tail theorem. Merely optimizing Young parameters cannot solve the fixed-family obstruction certified here.

Any eventual weak-block success still needs complete weak-mode coverage for H1250, corrected strong-block positivity and weak/strong cross-block inverse control. The four fixed RC63 directions are not assumed exhaustive. Global first-contact exclusion remains an independent alternative.

## Verification and deliverables

Inputs, in order: RC92, RC91, RC63, RC59, RC67, RC68, RC81, RC83 and RC89. SHA-256 digests and relevant native/source/trial/precision crosslinks are checked. Source pairings and trials use the same 64-mode basis. Exact physical masses and inherited e/pi enclosures are checked.

Generation and independent replay agree exactly. Replay uses symmetric triangular interval centers in place of full ordered contractions, column-first trial bilinear sums, factorial Fourier tails, rational logarithm series and a telescoping staircase identity. Both whole-block improvement tests, all four family obstructions and all exact PSD acceptance checks pass.

- `scripts/validate_rpb108_rc93_targeted_weak_source_capture.py`
- `certificates/rpb108_rc93_targeted_weak_source_capture.json`
- `notes/RPB108_RC93_TARGETED_WEAK_SOURCE_CAPTURE_20261011.md`

No Lean files or other research fronts are changed. No complete-head positivity, RH or Global/F4 claim is made.
