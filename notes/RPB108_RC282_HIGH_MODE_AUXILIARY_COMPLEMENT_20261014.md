# RC282 — protected high-degree auxiliary block and buffered Schur options

Branch: `research/rpb108-route-consolidation`. Parent `558a136277e0ddd4a1d12f6bca58228f42ee43c4` (RC281).

**Result:** A whole-range Loewner inequality in RC278's *unchanged rank-371
physical projection reference* certifies **70 native high auxiliary coordinates
jointly positive** (26 even, 44 odd) without another original Weil action or
inverse solve. This is a high-*principal-block* certificate. It does **not**
establish simultaneous positivity with the five RC280 pivots, nor any
low/high Schur positivity. The preexisting original nonpositive-index ceiling
301 is recovered, not improved.

## Exact whole-domain comparison

For either reflection parity, write `P` for RC278's retained physical
Legendre projection, `D P_n=(H_n+s)P_n` (with the exact common RC129
interval for `s`), and `lambda=C_b`, RC277's certified complete negative
physical allowance. The actual physical original form satisfies

    G0 >= D - lambda I.

For the unchanged RC278 reference `G=G0+lambda P`, RC278 proves the
full-domain bound

    G >= W := D_P + (D-lambda)_(I-P) > 0.

Inverting in the Loewner order is legitimate even though `G` is not
diagonal or commuting with `W`. The native auxiliary response on the
retained Legendre basis `U` satisfies

    T = U* G^-1 U <= U* W^-1 U
      = diag(m_n/(H_n+s)),     m_n=2B/(2n+1).

For any subset `J` of retained degrees, the actual native gate
`K=Mass-lambda T` has the positive lower bound

    K_J >= diag(m_n*(1-lambda/(H_n+s)) : n in J).

Using the exact *lower* endpoint for the same actual `s`, this implies
`K_J >= beta_J Mass_J` whenever `beta_J>0`. The inequality is
uniform over **all** linear combinations in `J`, not just positive
diagonal entries. It retains every original source coupling through inverse
operator order.

## Exact certificate and floor-versus-dimension tradeoff

| Requested guaranteed Mass-normalized floor | First even / odd protected degree | Joint protected rank | Remaining low rank |
| --- | --- | ---: | ---: |
| >0 | 232 / 371 | **70** (26+44) | **301** (116+185) |
| >0.001 | 234 / 375 | 67 | 304 |
| >0.002 | 236 / 379 | 64 | 307 |
| >0.005 | 244 / 391 | **54** (20+34) | **317** (122+195) |
| >0.01 | 256 / 413 | 37 | 334 |

Every cutoff is the **first matching parity Legendre degree** satisfying
`1-lambda/(H_n+s_lower)>threshold`, and its immediate retained predecessor
fails that same strict threshold. Each minimum floor is calculated with exact
fractions and rounded **downward** to 18 decimal places. RC282's JSON stores
the floor for each parity and threshold, not only these totals.

The unbuffered rank-70 high block is theoretically the largest block this
diagonal lower-bound criterion certifies on the supplied fixed reference;
its minimum native floor is small (approximately 3.334e-4 even and
6.217e-5 odd). The buffered 54-coordinate option instead certifies a common
Mass-normalized floor **greater than 0.005**, allowing a high-principal-block
inverse norm **less than 200** in that metric. The exact high-block inverse
here is an inverse of the auxiliary gate's principal block; it is *not*
the inverse of the original Weil form.

## The remaining coupling obligation

Partition the **actual** native auxiliary gate by low degrees `L` and
protected high degrees `J`:

    K = [[K_LL, C_LJ],
         [C_LJ*, K_JJ]],     K_JJ >= beta_J Mass_J > 0.

Then original positivity is equivalent to

    K_LL - C_LJ K_JJ^-1 C_LJ* > 0.

Neither `K_LL` nor the low/high cross block is evaluated here. The selected
RC280/RC281 five positive pivots all lie in the low principal restriction
for every displayed cutoff, but they **cannot simply be subtracted** from
the 301- or 317-dimensional low Schur problem: eliminating the protected
high block subtracts another nonnegative term, and a formerly positive
pivot may fail after that correction. A 2x2 exact indefinite control with
both diagonal restrictions positive enforces this distinction.

Thus RC282 supplies a **usable positive block in exactly the same native
rank-371 auxiliary metric**, with explicit conditioning choices. This is more
constructive than an independent canonical eigenvalue census, but does not
strengthen the existing global nonpositive-index upper bound of 301.

**Next RC283:** bound the low/high cross response jointly and then obtain a
lower bound for the low principal Schur form. Use either the rank-70
unbuffered route or the rank-54 buffer-`0.005` route, depending on the
cross-bound conditioning; preserve all same-parity couplings.

## Replay

```bash
python scripts/validate_rpb108_rc282_high_mode_auxiliary_complement.py --output certificates/rpb108_rc282_high_mode_auxiliary_complement.json
python scripts/validate_rpb108_rc282_high_mode_auxiliary_complement.py --output certificates/rpb108_rc282_high_mode_auxiliary_complement.json --replay
```

The validator checks exact Git blob ancestry, RC129's `s` interval,
the RC278 reference parameter equality, the two RC280 and RC281 scope
flags, exact moment ranks, rational threshold ordering, and a separate
noncommuting inverse-order matrix control. Earlier certified arithmetic
estimates are imported by pinned certificates rather than rederived.
Stage I, F4, RH, and Lean remain open.
