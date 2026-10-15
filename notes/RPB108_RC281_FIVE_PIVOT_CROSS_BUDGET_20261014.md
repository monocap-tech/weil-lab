# RPB108 RC281 — full five-pivot cross-column covariance budget

Starting head: `e0a6cfe6e639a112111804a29fb9ac8e1aabe427` (RC280 plus the Actions merge).
Aperture B=11/10. Reference: the unchanged RC278 rank-371 exact physical Legendre
projection augmentation. **No new original action, auxiliary inverse solve,
or positivity assertion for the remaining 366-dimensional Schur complement.**

## Result

RC280's certified positive five-mode block consists of even P0,P4 and odd
P1,P3,P5. RC281 gives one *complete* rigorous cross-column Schur payment
against **every one** of the remaining 140 even and 226 odd native coordinates.
It preserves correlated pivot noise instead of charging each source and
remaining coordinate independently.

| Actual coupled cross payment | Even | Odd |
| --- | ---: | ---: |
| Positive pivot block | P0,P4 | P1,P3,P5 |
| Remaining coordinates | 140 | 226 |
| First remaining degree | 2 | 7 |
| Safe physical D weight | 5 | 6 |
| Weighted trial-center trace ceiling | 1/550 | 1/800 |
| Weighted inverse-residual trace / D ceiling | 3/200 | 41/200 |
| Young parameter | 3 | 13 |
| **Schur cross payment** | **< 3 Mass_R** | **< 26 Mass_R** |

These are deliberately conservative **matrix bounds**, not an actual norm
measurement of the original operator or a positive lower bound for the
remaining principal form. In particular the coefficients 3 and 26 may be
far too large to close positivity.

## Exact interface

Let G be the *actual* positive RC278 physical augmented form; N=D^-1 G its
D-Riesz operator. The retained native polynomial synthesis maps are U_A for
the certified pivot set A and U_R for all remaining reference degrees R.
The native auxiliary gate has blocks Gamma, C, F, with

    C = -lambda U_A* G^-1 U_R,

because the auxiliary physical mass Gram has zero off-diagonal entries
between disjoint Legendre modes. RC280 certifies Gamma >= Gamma_lo > 0.
No same-parity coupling is discarded.

For each pivot source u_i, RC280's exact rational trial Z_i and actual
residual e_i satisfy

    e_i = D^-1 u_i - N Z_i,
    G^-1 u_i = Z_i + N^-1 e_i.

Let X_i=N^-1 e_i. Then C has an **exact finite center** determined by the
coefficients of Z_i on R (all degree <=64) and an unknown projected
remainder determined by the coefficients of X_i on R.

RC280 certifies the full *correlated* inverse-residual Gram

    [<e_i,N^-1 e_j>_D]_A <= S_A

in Loewner order. RC278's complete physical lower form is

    G >= D_{P_ret} + (D-C_b)_{Q_ret}.

Every remaining reference mode is in P_ret, so for all pivot combinations
a, its physical projection obeys

    ||P_R sum_i a_i X_i||^2
      <= <sum_i a_i e_i, N^-1 sum_i a_i e_i>_D / d_R
      <= a* S_A a / d_R,

where d_R <= H_n+s for all n in R. RC129's exact s interval certifies the
chosen d_R=5 for even R (first degree 2) and d_R=6 for odd R
(first degree 7). This is an actual common-domain inverse inequality and
uses **no identification** of the canonical operator M with N.

Let M_R=diag(m_n:n in R) with m_n=2B/(2n+1). Define the exact
pivot-trial physical Gram

    (G_Z)_{ij} = sum_{n in R} m_n (Z_i)_n (Z_j)_n.

For any rational theta>0, applying matrix Young **before** a Hilbert–Schmidt
trace gives a complete bound for the *true* cross block:

    C* Gamma^-1 C <= lambda^2 [
       (1+theta) tr(Gamma_lo^-1 G_Z)
       +(1+1/theta) tr(Gamma_lo^-1 S_A)/d_R ] M_R.

The proof uses inverse Loewner order Gamma^-1<=Gamma_lo^-1,
Cauchy–Schwarz for the full synthesis map U_R, and the physical projection
bound above. All 366 remaining modes are covered simultaneously. Neither
entrywise error independence nor diagonality of Gamma is assumed.

The exact fraction validator checks the full selected 2x2 / 3x3 pivot
matrices, the full correlated RC280 residual covariance, all coefficients
of the selected trial polynomials, the native Legendre masses, the RC129
D offset and the RC278/RC280 immutable blobs. It chooses theta=3 even,
13 odd, verifies the strict trace ceilings in the table, and obtains

    C_even* Gamma_even^-1 C_even < 3 M_R_even,
    C_odd*  Gamma_odd^-1  C_odd  < 26 M_R_odd.

These inequalities include the enlarged block-to-rest correlations that
RC280 had expressly left unaccounted for.

## What is and is not closed

**Closed:** a valid conservative full 5-by-366 cross-column Schur payment,
as a mass-Loewner upper bound, with selected-source covariances preserved.
This is an upper envelope; it is not a calculation of individual cross
entries or their exact covariance. The rank-371 reference and five positive
pivots are unchanged.

**Still open:** evaluating or uniformly bounding the 366-dimensional
remaining principal form F strongly enough to prove

    F - C* Gamma^-1 C > 0.

The current cross-payment constants are large. RC282 should either improve
these via source-specific projected inverse responses/critical-eigenvector
alignment, or construct a matching positive principal-block lower bound.
The results do not automatically improve the independent original
nonpositive-index census (301). The complete Stage I, global/F4, RH and Lean
obligations remain open.

## Reproduction

```bash
python scripts/validate_rpb108_rc281_five_pivot_cross_budget.py --output certificates/rpb108_rc281_five_pivot_cross_budget.json
python scripts/validate_rpb108_rc281_five_pivot_cross_budget.py --output certificates/rpb108_rc281_five_pivot_cross_budget.json --replay
```

The RC281 check reuses RC280's separately replayed finite/infinite source
certificates and checks their exact Git blobs; it does not recalculate their
expensive 2048-degree prime steps or supply independent peer review.
