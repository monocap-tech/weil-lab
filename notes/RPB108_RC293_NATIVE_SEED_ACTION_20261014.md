# RC293 — native signed-response seed action on the reduced rank-317 reference

Parent: canonical RC292 `1d2047d294698b24f65ea3c3b3e248c3b038922c`.
Aperture B=11/10; parity even; physical retained projection degrees
0,2,...,242; 120 remaining source directions after positive P0,P4.

## What is actually computed

RC292 supplied exact **conditional** signed-inverse acceptance thresholds
for hard source `v_h=P0` and soft source `v_s=P4-tP0`, but did not
execute any inverse recurrence. RC293 makes the first *certified native
action recomposition* on two explicit rational Galerkin seeds in the
physical source span `span{P0,P4}`, using previously completed RC279
original P0/P4 action profiles.

The two trial seeds are

    Yhat_h = 0.10134998 P0 - 0.00386594 P4
    Yhat_s = -0.08384303 P0 + 0.10042994 P4.

These coefficients are fixed rational approximations to finite
D-weighted least-squares fits. They are *not* the true inverse solutions,
and their origin supplies no mathematical validity; all certification
comes from directly checking the resulting native residual.

The actual reference operator is

    N_new = D^-1 (G0+lambda P_317),     b=D^-1 v.

On P0 and P4 the exact projection augmentation is known:

    N_new P_j = N_original P_j
                  + lambda/(H_j+s) P_j,      j in {0,4}.

RC279's stored original P0/P4 D-normalized action coefficients, each
through degree 2048, are pinned and recomposed linearly. The model
residual is calculated in the physical D norm, using RC129's
s_lower<=s<=s_upper, the actual rational augmentation, and upward
rounded Legendre mass and D weights. Source and augmentation inverse
weight rounding at n=0,4 is charged separately.

RC279's complete **infinite original-output tail** is included in
the D-residual via Minkowski using the actual seed coefficients;
the full original prime/archimedean/endpoint global D-norm faults
are likewise included. None of these uncertainties is set to zero.

The result is a full-domain **upper bound** on the actual residual
`||b-N_new Yhat||_D²` for these two particular seeds.

## What the initial test can and cannot settle

Each seed lies exactly in the positive pivot source span, so its
*approximate* signed projection onto all 120 other even retained
Legendre directions is zero. This trivially passes the projection
budget required by RC292.

The decisive issue is its **actual paid residual**. Both seeds are
deliberately checked against RC292's strict residual-square tolerances,
and both fail by a large margin. Thus no actual signed inverse-response
or even joint cross-payment is certified. A residual **upper bound**
above threshold does not prove that the actual residual exceeds the
threshold or that every source-span approximation is impossible.

This is a bona fide calculation for a limited certified native action
oracle, not execution of RC292's full 1000+-step Chebyshev inverse
polynomial. RC279's action profiles were computed previously: no new
original Weil prime evaluation is claimed.

## New engineering boundary

The remaining implementation task is an operator-action evaluator that
accepts **arbitrary recurrence polynomials**, not just the available
P0/P4 columns. Its native source-action primitive must calculate
exact endpoint, archimedean and prime outputs with certified complete
infinite tails and D-norm arithmetic defects, preserving the
rank-317 augmentation at every step. Merely applying a finite
2049x2049 matrix assembled from two action columns does not
certify this operator's infinite-dimensional recurrence.

Next RC294: construct and test a linear native-action contract for
larger rational Legendre polynomial inputs and pay original source
errors on every evaluated recurrence step. Test the RC292 strict signed
rest-projection and residual budgets only after these genuinely
executed actions are certified.

## Audit and replay

Input immutable Git blobs RC129, RC279 (actual original native
source actions), RC283 (new positive reference), RC290 (soft rational
coefficient), and RC292 (exact signed-action acceptance contract).
Generation and reversed input-order replay must reproduce the entire
exact rational JSON. GitHub Actions replay is a reproducibility check
rather than independent proof of historical source estimates.

```bash
python scripts/validate_rpb108_rc293_native_seed_action.py --output certificates/rpb108_rc293_native_seed_action.json
python scripts/validate_rpb108_rc293_native_seed_action.py --output certificates/rpb108_rc293_native_seed_action.json --replay
```

The rank-317 314-dimensional Schur principal gate, Stage I, global F4,
RH and Lean remain **OPEN**.
