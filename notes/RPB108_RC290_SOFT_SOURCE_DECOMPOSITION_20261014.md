# RC290 — exact soft mixed source behind rank-317 even cross amplification

Parent: canonical RC289 at `765e64555d2a1012f1eb1898c1af5269ce66a7d0`.
Original Weil form unchanged, aperture B=11/10.

## Identifying the actual *certificate* bottleneck

The new-reference RC288/289 even positive source block is on P0,P4,
with **exact rational** positive Loewner lower matrix

    Gamma_lo = [[a,b],[b,c]],  a>0, ac-b²>0.

Its positive source directions can be congruence-diagonalized without
an eigensolver, by setting

    t=b/a,
    v_soft=P4-t P0,
    delta=c-b²/a>0.

For the change-of-basis columns T=[P0, v_soft] in the old P0,P4
coordinates, exact rational multiplication gives

    T* Gamma_lo T = diag(a, delta).

The new **soft positive direction** is approximately

    v_soft = P4 - 0.823238958176 P0.

This coefficient comes from the certified *lower gate*, **not
necessarily the exact physical orthogonalizer of the actual gate**.
The exact value t is retained in the JSON certificate.

The soft Schur margin is about **0.00002787419406**, while the hard
margin a is about **0.00518134700932**. Their ratio exceeds **180**.
This is why bounding the source covariance through the *inverse of
the entire positive pivot matrix* magnifies some uncertainty enormously.

## Exactly which error concentrates on the soft source?

Let A denote RC289's exact Gram of rational trial-polynomial centers
after physical projection onto the 120 **remaining even** Legendre
directions. Let S denote the newly paid, correlated inverse residual
Gram from RC288, and d_R its rigorous even native D weight floor.

For each M in {A,S}, under the source congruence

    M' = T* M T,

its soft diagonal is

    M_soft = M_44 - 2t M_04 + t² M_00.

Consequently, the full trace identities split *exactly*:

    tr(Gamma_lo^-1 A)
       = A_00/a + A_soft/delta,

    tr(Gamma_lo^-1 S)/d_R
       = S_00/(a d_R) + S_soft/(delta d_R).

The validator checks all identities with exact Fractions, including
the original RC289 trace upper ceilings and transformed matrix
symmetry.

| Weighted contribution | Hard P0 share | Soft P4-tP0 share |
| --- | ---: | ---: |
| Trial-center trace | ~7.42% | **>90%** (about 92.58%) |
| Inverse-residual covariance trace | ~0.72% | **>99%** (about 99.28%) |

The soft covariance concentration is the primary **source-level
optimization target**.

These percentages describe the *certificate's positive matrix
traces*. They are not percentages of the actual original Weil
operator spectrum or a physical energy distribution, and do not
imply that any actual original eigenvalue is negative.

## Why this changes the next computation

RC289 already showed that the existing variance-only whole-range
cross-payment cannot become mass-subunit by merely adjusting the
Young parameter. RC290 isolates the particular correlated
combination responsible for that failure.

A basis relabeling **alone** does not improve the full trace:
the transformation is an exact identity. What helps would be
obtaining a **new, tighter signed projection** of the actual
inverse response for

    P4 - tP0

onto the other 120 even retained source modes, ideally by paying
correlations between the actual rational trial center and the
residual response rather than adding their nonnegative norms.

The old rank-371 covariance must not be carried over. The new
rank-317 positive P0/P4 block and the independently subunit
RC286 single-source P0/P1 cross bounds remain valid.

The remaining 314-dimensional principal Schur gate, complete
Stage I, global F4, RH, and Lean obligations remain OPEN.

## Next RC291

Try a signed, degree-localized interval enclosure of
`U_R^* G_new^-1 (P4-tP0)`, preserving complete original arithmetic
source errors and infinite tails. Compare whether a short
Chebyshev/resolvent correction to this soft source can pay its
cross column more sharply than the full inverse-energy Gram.

Do not claim that the above soft coordinate is a negative or zero
mode. It is a strictly positive mode of the **certified lower
pivot matrix** with a small quantitative margin.

## Reproduce

```bash
python scripts/validate_rpb108_rc290_soft_source_decomposition.py --output certificates/rpb108_rc290_soft_source_decomposition.json
python scripts/validate_rpb108_rc290_soft_source_decomposition.py --output certificates/rpb108_rc290_soft_source_decomposition.json --replay
```

Actions checks exact rational identities, immutable RC288 and RC289
Git blob pins and stored JSON; it is not independent rederivation
of the inherited analytic inputs.
