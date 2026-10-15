# RPB108 RC288 — new-reference three-source covariance reconstruction

**Parent:** RC287 `7bad1336df47036872705b5f1db65a388f8f1fbd`.
**Aperture:** B=11/10.
**Reference:** reduced rank 317, 122 even +195 odd, with whole-domain
certified positive physical D floors >0.005.

## Scope

Reconstruct **new rank-317** full 3x3 original-source inverse-residual
covariance envelopes for even P0/P2/P4 and odd P1/P3/P5.
No old RC280 inverse covariance or positive pivot is transferred.
RC280 rational trial polynomials, stored RC279 original-source actions
through degree 2048, and RC274 P0/P1 residue intervals are reused
because their polynomials lie entirely within the reduced projection.

The exact source residual and variational center are unchanged on the
trial family, but its *inverse-energy* is recertified. Write
N_new=D^-1 G_new, and the RC283 lower comparison W_new:

    G_new >= W_new
    w_n=1                          (n<first omitted parity degree)
    w_n=1-lambda/(H_n+s_lower)     (otherwise).

For rank317, the first omitted degrees are 244 even, 391 odd. Every
source-output coefficient through degree 2048 is reweighted with
1/w_n, using downward-rounded rational lower weights. The complete
infinite tails from RC274 and RC279, plus original prime/endpoint and
arithmetic global D-fault bounds, are paid by each parity's respective
tail weight and the new global reference floor.

For the three original source trials, reconstruct each finite
center residual polynomial, and construct a **joint** 3x3 Gram bound

    Gram_model_ij =
       sum_n physical_mass_n (H_n+s_upper)
             model_i(n)*model_j(n)/w_n.

Use outward rational interval enclosure and a Loewner Gershgorin
radius for interval error; there is no independence assumption for
model cross terms. Inherited four correlated underlying source
errors are charged via their rank-one quadratic forms and the
original response coefficients, plus finite interval radii.

For matrix Young parameter theta>0, get a full covariance upper
matrix S_new(theta). The new native gate lower matrix is

    Gate_lower(theta)
        = Mass_3 - lambda (Center_mid + S_new(theta)
                            + Center_interval_radius * I).

No new original Weil action is performed. A positive leading block
is accepted only by exact rational Schur pivots on the **new**
gate lower matrix.

## New joint positivity certificate

The complete rational 3x3 covariance replay has returned **a new
positive two-direction even block** (P0,P4) and **one positive odd
direction** (P1), under the *rank-317 reduced reference*. This does
not import RC280's former old-reference positive pivots.

| New reference | Native subblock certified strictly positive | Still unresolved among six |
| --- | --- | --- |
| Even, 122 channels | **P0,P4 jointly** | Coupling to P2 and rest |
| Odd, 195 channels | **P1** | P3,P5 and rest |
| Combined, 317 channels | **3-dimensional positive principal block** | **314-dimensional Schur complement** |

The new full 3x3 **gate lower** has a negative Gershgorin floor in
both parities (about -0.004653 even and -0.003979 odd), so this
calculation does **not** certify full three-mode positivity.
The checker certifies the even 2x2 principal block by exact
Schur pivots of the **new** gate; odd P1 likewise passes.
The negative full-gate lower envelopes are **not negative original
operator witnesses**.

The earlier RC285 P0/P1 positive pivots and RC286 whole-range
cross-column payments remain independently valid. RC286's P0/P1
cross-payment inequality **cannot automatically be promoted** to
the new joint P0,P4 block. Before eliminating three pivots from the
317-channel auxiliary form, its complete new joint cross-columns
must be paid.

The improved count is a certified positive principal subspace,
**not a reduction of the original nonpositive-index upper bound**.

## Limits

The RC285 P0/P1 individually positive source pivots and RC286
whole-range cross payments stay certified independently, regardless
of the success or failure of this distinct three-source trial family.
A nonpositive lower matrix from this pass is **inconclusive** about
actual source or Weil-form negativity. It does not invalidate
those earlier source tests. The rank-317 remaining 315-dimensional
principal Schur positivity, Stage I, F4, RH and Lean are OPEN.

## Audit

Input blob pins: RC129, RC274, RC278, RC279, RC280, RC283, RC287.
The validator checks exact RC280 trial reconstruction, native
rank-317 cutoffs, original-action profile degree coverage,
separate global fault payments, all 2049 coefficient weights and
a 3x3 correlated covariance envelope. Both generation and reverse
replay must match the same materialized JSON.

```bash
python scripts/validate_rpb108_rc288_new_six_mode_covariance.py --output certificates/rpb108_rc288_new_six_mode_covariance.json
python scripts/validate_rpb108_rc288_new_six_mode_covariance.py --output certificates/rpb108_rc288_new_six_mode_covariance.json --replay
```

Next: identify whether a new 3x3 positive block is obtained; if not,
concentrate RC289 on joint trial selection and RC280's improved
correlated prime jump-tail covariance, not a global scalar
transfer factor.
