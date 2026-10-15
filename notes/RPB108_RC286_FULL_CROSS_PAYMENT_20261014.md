# RC286 — all remaining P0/P1 cross columns paid in reduced references

Parent RC285 `be65d328ef63d6ac8ddf990d30af7d07c6ad94c8`.
Aperture B=11/10. The original Weil form, source responses and
positive projection references are unchanged.

## Result

RC285 certified strictly positive native source pivots P0 (even) and
P1 (odd) in each of the rank-301, rank-317 and rank-334 references.
RC286 proves **whole remaining-range Schur cross-payment inequalities**
for those newly certified pivots, without solving for each remaining
response separately.

For the preferred **rank-317** reference:

| Parity | Pivot | Remaining coordinates | Native Mass upper for Schur cross payment |
| --- | --- | ---: | ---: |
| Even | P0 | 121 | **< 4/5** |
| Odd | P1 | 194 | **< 3/4** |
| Combined | two independent parity pivots | **315** | parity-specific bounds |

These are valid conservative inequalities, not exact measurements of
the cross covariance. The rank-334 reference additionally has cross
payments < 3/4 even and < 2/3 odd. The minimal rank-301 bounds are
approximately 2.8968 even and 1.2118 odd, so do not cross one under
the current estimates.

## Proof contract

Fix one reflection parity and one RC283 positive reference. Write the
original physical Weil form `G0`, its positive augmented form
`G=G0+lambda P_ret` and its auxiliary native matrix

    K = Mass - lambda U* G^-1 U
      = [[gamma_actual, C],
         [C*, F]].

The existing RC285 arithmetic proves `gamma_actual>=gamma>0`, and
for the actual RC278 trial Z in this **same** reduced reference, the
complete actual residual e satisfies

    X=G^-1 D e,
    G^-1 P_base = Z+X,
    <X,G X> = <e,N^-1 e>_D <= q.

The trial has degree <=64 and is wholly within every new retained
projection. All original Weil output tails and arithmetic defects
already enter q through RC285.

On the retained source span, the exact physical form inequality is

    G >= W = D_(retained) + (D-lambda)_(outside).

Thus, for the remaining retained span R and its physical projection,

    ||P_R X||^2_physical <= q/d_R,

where `d_R` is the rigorous lower bound for `H_n+s` at its first
remaining Legendre degree, n=2 even or n=3 odd. RC129 supplies the
exact common interval for s. This is a whole-span consequence of
inverse energy, without assuming independence of residual entries.

Let `m_j=2B/(2j+1)` be the physical Legendre mass and
`z_j` the *actual* rational trial coefficients. Define

    A = sum_(j in R) m_j z_j^2,
    Q = q/d_R.

The entire cross-column operator C obeys

    C* gamma_actual^-1 C
      <= (lambda^2/gamma) [(1+theta)A+(1+1/theta)Q] Mass_R,

for any theta>0. The exact validator takes theta=3, pays each trial
coefficient with outward rational rounding, rounds d_R downward and
the residual energy upward, then checks the displayed strict
rational bounds.

Odd/even cross terms vanish by reflection parity, so both sectors
are treated jointly as a block-diagonal assertion across **all**
315 remaining coordinates.

## Limitations

We have **not** evaluated the remaining principal form F, let alone
certified `F-C*gamma_actual^-1 C>0`. A cross payment smaller than
one physical Mass does not imply positivity: F may be nonpositive,
small or strongly coupled internally. The validator includes a
separate exact 2x2 indefinite matrix control exhibiting this.

Unlike RC280, no additional positive same-parity P2/P4 or P3/P5
pivot is claimed under the new reference. They still require fresh
mixed original-source action / covariance certification.

RC286 is a new collective coupling certificate. It does not change
the original nonpositive-index census or close Stage I, global F4,
RH or Lean.

## Reproduction

```bash
python scripts/validate_rpb108_rc286_full_cross_payment.py --output certificates/rpb108_rc286_full_cross_payment.json
python scripts/validate_rpb108_rc286_full_cross_payment.py --output certificates/rpb108_rc286_full_cross_payment.json --replay
```

GitHub Actions checks exact rational replay of the pinned previous
certificates; it does not independently reproduce their original
arithmetic actions or underlying analytic inequalities.

**RC287:** establish a lower bound for the remaining rank-317 principal
matrix F, or build three-mode same-parity covariance for the new
rank-317 reference without transferring old-reference pivots.
