# RPB108 — RC207: exact obstruction to parameter-only fixed-trial closure

Parent RC206, commit a23209ae4334772f81c35ad1838103749aa27d8e. The actual supported operator M=D^-1 L, aperture 11/10, six-source response family and RC203's eight-trial least-residual map Y remain unchanged.

## Result and scope

For the fixed RC203 carriers and the RC205/RC206 scalar Young payment formulas, every candidate in the certified parameter family has relative inverse enclosure width at least

    10249/15625 = 0.655936 > 0.5.

The result covers every positive triangle weight, every convex mixture with the RC204 scalar signed bound, every positive action/tail/residual Young parameter, and every allowed residual-lower sigma in [0,1]. It also covers combinations with all stored RC201/RC203 trial endpoints, selected RC205/RC206 endpoints and the structural endpoints. A single exact rational response probe rejects all 64 endpoint-pair families.

**This is a barrier for an enclosure method, not for the actual inverse or Weil positivity.** It does not rule out sharper physical estimates, directly bounded cross tails, other error majorants not in the stated family, or changed trials. No new inverse-width upper is claimed. RC206's certified upper remains 0.672096 and the six-source acceptance gate remains open.

## Exact probe and parameter-independent lower bounds

Use the rational response vector

    x=(1619/500000, -14633/1000000, 160653/1000000,
       -1, -569149/1000000, 596627/1000000).

Let g=x^T G_lower x>0. For the eight raw trial error bounds epsilon_i and positive weights w_i, weighted Cauchy gives

    x^T E_triangle(w) x
      = (sum_i epsilon_i/w_i) sum_i epsilon_i w_i (Yx)_i^2
      >= (sum_i epsilon_i |(Yx)_i|)^2 = e_triangle.

The RC204 scalar signed envelope has exact probe value e_signed=(473/200000)g. Every convex mixture therefore has probe energy at least e=min(e_triangle,e_signed), independent of weights and mixing coefficient. This is a lower bound on the chosen error **majorant**, not on the actual physical action error.

Write u=x^T G_U x, n=x^T N_upper x, n_low=x^T N_lower x, t_u=x^T U_tail x and t_r=x^T R_tail x, all nonnegative. The unpaid variational endpoints B_lower/B_upper are recovered exactly by reconstructing and removing RC203's stored original payment.

For any positive action theta and tail parameter t, the variational payment obeys

    x^T P x >= sqrt(u e) + sqrt(t_u t_r) = p_min.

For any positive residual parameter tau and RC121 coercivity a,

    x^T R_upper x / a
      >= (n+e+2 sqrt(n e))/a = r_min.

For every allowed sigma, including the zero lower, x^T R_lower x <= n_low. Consequently, every fully refined inverse lower endpoint has probe value at most

    x^T B_lower x - p_min + n_low/2,

and every fully refined inverse upper endpoint has probe value at least

    x^T B_upper x + p_min + r_min.

These estimates enlarge the allowed parameter search, so the rejection does not depend on numerical optimizer behavior. All historical and structural endpoint probe values are also computed. The largest allowed lower ceiling and smallest allowed upper floor give a gap greater than 0.655936 g, hence greater than g/2. Thus the half-Gram gate matrix has a strictly negative value on this same x throughout the stated family.

## Arithmetic verification

Three square-root lower bounds are computed by exact integer square root on a 10^30 grid. Each rational lower r is checked by r^2<=z<(r+10^-30)^2. Using a square-root lower makes the payment lower conservative; it yields a larger, conservative inverse-lower ceiling and a smaller, conservative inverse-upper floor.

The final normalized gap is rounded downward on a millionth grid. It remains strictly above 1/2 by 0.155936. Five certificate inputs and seven helper modules are bound by immutable Git blob hashes. Source/trial carriers and the physical reconstruction remain inherited certified premises. The comparison does not assert that the current best upper is mathematically optimal.

Normal verification and reversed-order replay pass and require identical certificates. Replay reverses response-coordinate, raw-trial and historical-family evaluation orders. Negative controls reject a zero-energy probe, mismatched Git input pin and negative square-root energy.

```bash
python scripts/validate_rpb108_rc207_fixed_trial_payment_barrier.py --output certificates/rpb108_rc207_fixed_trial_payment_barrier.json
python scripts/validate_rpb108_rc207_fixed_trial_payment_barrier.py --replay --output certificates/rpb108_rc207_fixed_trial_payment_barrier.json
```

## RC208 cursor

Stop parameter-only passes within this fixed payment scheme. Improve complete action error data, nominal residual/source-residual estimates, or direct correlated cross-tail bounds; alternatively enrich Y with a fully certified action and new error proof. A different method or new carrier data is required to clear the half-Gram gate. This certificate identifies a necessary method change rather than predicting how many turns closure will take.

The best certified six-source upper remains 0.672096. Native z_b6/t10 coverage, odd-parity/source-range and original augmentation remain open. Stage I, RH, F4 and Lean closure are unclaimed. No historical or other branch is altered.
