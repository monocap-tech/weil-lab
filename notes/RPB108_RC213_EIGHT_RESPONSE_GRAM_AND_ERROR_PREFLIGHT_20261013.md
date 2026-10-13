# RPB108 — RC213: eight-response Gram and canonical error preflight

Parent RC212, commit 39cec66481545e1996a8f160797175e76e9f0e78. Aperture 11/10 and M=D^-1 L remain fixed. The expanded source order is P0,psi0,f0,w14,v10,z_b6,t10,P2: all seven native sources plus auxiliary P2. The accepted six-source inverse width 0.436100 and margin +0.063900 remain intact.

## Result

The full eight-response D-Gram is certified strictly positive. All finite source and infinite analytic tails are paid. Complete canonical-action error norm bounds for all eight columns and all 64 source/action and action/action absolute error payments are attached.

A first all-mixture envelope formed from separate marginal column errors has exact worst signed factor approximately 304.0384749488951 against the certified rational Gram lower. The outward-rounded factor is

    12161539/40000 = 304.038475.

Its half-Gram **action-error** sufficient test is rejected. This factor is not an inverse enclosure width, is not comparable with the six-source width 0.436100, and is not a lower bound on the actual physical action error. The expanded inverse has not been evaluated. Failure of this error preflight does not prove that the inverse gate cannot pass.

The result identifies a useful next target: correlated common/difference canonical-action bounds, especially z_b6-v10, before relying on the initial independent z/t column errors in a nearly cancelling source family.

## Source Gram construction

RC136 supplies the native seven-source finite-prefix Gram entry intervals through degree 16382 and full Gram upper entry intervals with analytic tails. P2 has only its degree-2 coefficient. Therefore its new mixed source rows have no omitted tail.

The P2/f0 pairing is exactly 2B/6. P2 has zero pairing with P0 and psi0. Its pairings with w14,v10,z_b6,t10 are

    (2B/5)(s+3/2) times the exact native degree-2 coefficient.

The native w/v centers come from their pinned materialized carrier; native z/t centers come from RC211/RC212's reproduced historical source prefixes. The actual s interval and P2 diagonal D-energy are retained. Directed entry enclosures are converted to Loewner endpoints with paid symmetric interval widths. The finite-prefix lower is PSD; the complete upper pays all native analytic tails.

For exact controls, construct an entrywise floor on a 10^50 grid and subtract 8 grid units from each diagonal. The lower-to-floor defect has diagonal at least 8 grid units and every off-diagonal magnitude below one grid unit, so it is strictly diagonally dominant and positive definite. The floor itself is PSD and exactly invertible, certifying eight-source independence. It is a conservative smaller Gram lower, not an optimistic rounding.

## Signed marginal error envelope

Let epsilon_i be the eight pinned complete canonical column norm bounds. For every real response coefficient c,

    ||sum_i c_i error_i||_D <= sum_i epsilon_i |c_i|
      = max_sign (sign*epsilon)^T c.

Simultaneous sign reversal is redundant. Enumerate 128 signed vectors z_sigma, fixing the first sign positive. With the positive rational floor G_F, the exact rank-one factor is

    q_sigma=z_sigma^T G_F^-1 z_sigma.

The maximum is rounded upward onto a millionth grid. The exact criterion q_sigma<=beta proves z_sigma z_sigma^T<=beta G_F for every sign, supplying a complete all-mixture upper. Real actions/trials and separate real/imaginary decomposition extend the bound to complex mixtures.

The worst mask is 10. Its exact rational witness x=G_F^-1 z has strictly negative value on (1/2)G_F-z z^T; this rejects that signed-rank-one sufficient control against this lower. It does not show that the true error map has that adverse alignment, or that a sharper correlated error certificate is impossible. No error orthogonality or independence is assumed.

## Pairing-error interface

For complete canonical error epsilon_j and source norm upper n_i, record

    |<S_i,V_j>-<S_i,M S_j>| <= n_i epsilon_j.

The full-domain norm bound ||M||<=2 also gives

    |<V_i,V_j>-<M S_i,M S_j>|
      <= 2 n_i epsilon_j + 2 n_j epsilon_i + epsilon_i epsilon_j.

All 64 entries of both absolute payment matrices are supplied. These are error payments for future mixed-row enclosures. Nominal pairing centers, represented residual matrices and inverse endpoints are not fabricated or inferred from this interface.

## Verification

Seven certificate input blobs and two helper blobs match the live repository tree. Normal verification and reversed sign-order replay pass and reproduce the whole certificate. All 128 exact rank-one controls are computed; conservative floor domination, source positivity/invertibility and the exact failed half-Gram witness are checked. A mismatched input Git pin is rejected.

```bash
python scripts/validate_rpb108_rc213_eight_source_error_interface.py --output certificates/rpb108_rc213_eight_source_error_interface.json
python scripts/validate_rpb108_rc213_eight_source_error_interface.py --replay --output certificates/rpb108_rc213_eight_source_error_interface.json
```

## RC214 cursor and boundaries

Certify shared canonical actions for the common/difference directions instead of applying independent marginal errors to nearly cancelling native columns. Retain all regular-input, endpoint and source/output tails in those combined directions. Then assemble the enlarged nominal mixed/action/residual rows and independently test the expanded inverse. Its accepted result cannot be inferred from either an action-error test or RC210's smaller-family inverse gate.

The six-source acceptance remains preserved. Expanded inverse acceptance, odd/source-range and original augmentation remain open. Stage I, original Weil positivity, RH, F4 and Lean closure are unclaimed. Historical files and other heads are unchanged.
