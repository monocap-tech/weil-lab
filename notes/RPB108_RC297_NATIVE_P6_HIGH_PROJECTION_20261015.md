# RC297 — complete original P6 output and rank-317 augmentation

**Parent:** RC296 at `b48fc40439ba8ecfbbfa9dad04a0f26578ee6553`.
**Carrier:** original Connes–Weil physical aperture B=11/10.
**Positive reference:** rank 317 (122 even + 195 odd).
Stage I, global F4, RH and Lean remain OPEN.

## Result sought

RC296 introduced a fourth actual original Weil input-action column
`P6`, independently of the previously certified P0/P2/P4 columns.
Its first 65 D-normalized original output coefficients and global
omitted-output error were constructed using generic signed
regular/pole/prime/endpoint source formulas.

RC297 extends that **same original input** through degree 2048.
Use the previously certified generic RC279/RC273 original
prime-jump and analytic endpoint projection method with the
RC296 P6 low-mode original data and exactly pinned RC43 prime
arithmetic. All 65 preexisting coefficients must reproduce RC296
without modification. The actual finite source output through 2048
is materialized in the JSON certificate; odd coefficients vanish
by parity.

The generic continuation's complete global D-norm uncertainty pays
the inherited finite original-action rounding, regular kernel,
pole Taylor, active-prime arithmetic uncertainty, new high-degree
projection rounding, and the original regular omitted high output.
The separate model D-energy tail beyond degree 2048 pays all
remaining prime and endpoint outputs. No omitted output is set
to zero. All inherited analytic formulas, including their
degree-six applicability, remain proof assumptions imported through
the pinned source code and mathematical certificates rather than
fresh independent peer review.

## Correct physical augmentation

For the preferred rank-317 reference let

    G_new=G_original+lambda P_low,
    N_new=D^-1 G_new.

Since P6 is among the retained even Legendre inputs (the even
reference retains degrees 0 through 242), its augmented
D-normalized action differs from the original action only at
the physical output degree n=6:

    N_new P6 = N_original P6
               + [lambda/(H6+s)] P6.

The interval of possible s is the exact RC129 pinned moment
interval. The validator constructs an outward-rounded rational
center and radius for lambda/(H6+s). It pays the extra single
coefficient's uncertainty in the *D*-norm:

    delta_aug <= sqrt(m6*(H6+s_upper)) * radius.

The total new global D-error norm is conservatively increased by
this amount. The original infinite high-output tail remains
unchanged, because the augmentation is finitely supported at
degree 6. This distinction is essential: the rank-317
augmentation cannot be silently attached to all source/output
coordinates, nor to the inverse itself.

The certificate contains the original 0–2048 output profile,
its complete prime/endpoint proof metadata, and the
single-coordinate augmented patch with its full uncertainty.

## What is not claimed

We now have complete high-output, paid original-action columns
for the four specific even inputs P0,P2,P4,P6, contingent upon
their inherited analytic formulas.

We have **not** evaluated the original operator on arbitrary
inputs, run a full Chebyshev inverse recurrence, or solved the
four-column Galerkin residual problem. No new source positivity,
signed cross-cancellation, original Weil-form positivity, or
314-dimensional remaining Schur positivity is certified here.

**RC298:** construct actual inverse seeds in span{P0,P2,P4,P6},
using all original columns and rigorous residual/covariance
payments. Test against the RC292 signed-source tolerance and
RC295's finite-output dual constraints; the RC295 no-go applies
to the former three-column span, not automatically the larger
four-column space.

## Reproduction

```bash
python scripts/validate_rpb108_rc297_native_p6_high_projection.py --output certificates/rpb108_rc297_native_p6_high_projection.json
python scripts/validate_rpb108_rc297_native_p6_high_projection.py --output certificates/rpb108_rc297_native_p6_high_projection.json --replay
```

GitHub Actions replays exact rational projection and input
custody. Successful execution does not independently establish
all imported original Weil arithmetic and analytic assumptions.
