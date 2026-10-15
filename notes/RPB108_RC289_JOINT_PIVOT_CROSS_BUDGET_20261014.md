# RC289 — joint three-pivot cross payment; center geometry is the bottleneck

**Parent:** RC288 `b96d942b60a725646fe71e53c2fa7980ac33b3d2`.
**Aperture:** B=11/10.
**Reference:** certified globally positive reduced rank 317 (even 122, odd 195).
No new original Weil action or independently revalidated analytic premise.

## The exact whole-range coupling theorem

RC288 certifies the new same-reference positive 2x2 even gate on
P0,P4 and 1x1 odd gate on P1. Partition the *actual* rank-317 native
auxiliary matrix into pivot coordinates A and the remaining R:

    K = [[Gamma, C],[C*, F]],   Gamma >= Gamma_lo > 0.

Rank(R)=120 even + 194 odd = **314**. Even 2x2 and odd 1x1
blocks are treated with their full correlated covariance. RC288's
positive Gamma_lo is specific to the **new** reduced reference,
and its complete inverse-residual covariance S_new is not RC280's
old-reference covariance.

Write the actual correlated source response for each pivot as

    G_new^-1 P_i = Z_i + X_i,

where Z_i is RC280's exact 65-coefficient rational trial polynomial
(whose source/action identity was proved by RC287), and X_i is the
new-reference inverse of the unchanged actual source residual.

The precise trial mass Gram projected onto *all* remaining reference
degrees is

    (A_Z)_ij = sum_{n in R} m_n (Z_i)_n (Z_j)_n,
    m_n = 2B/(2n+1).

The new-reference physical inequality G_new >= D on the retained
projection yields the complete *correlated* physical projection
bound

    [<P_R X_i,P_R X_j>_physical] <= S_new/d_R,
    d_R = H_(first remaining degree)+s_lower,

with first remaining degree 2 (even) and 3 (odd). No extra residual
independence, pointwise source error assumption, or missing infinite
tail is introduced.

For any positive rational theta, using inverse Loewner order and
matrix Young/Cauchy on the full selected source family gives

    C* Gamma_actual^-1 C
      <= lambda^2 [
          (1+theta) tr(Gamma_lo^-1 A_Z)
          +(1+1/theta) tr(Gamma_lo^-1 S_new)/d_R
         ] Mass_R.

This **covers all 314 cross columns**, not just a finite sampled
subset, and preserves RC288's complete selected 2x2 correlation.

## Exact rational result

| Sector | Pivots | Remaining | Young theta | Certified cross payment |
| --- | --- | ---: | ---: | ---: |
| Even | P0,P4 | 120 | 7 | **< 160 Mass_R** |
| Odd | P1 | 194 | 9/4 | **< 3 Mass_R** |

The exact rational certificates and source blob pins are stored in
`certificates/rpb108_rc289_joint_pivot_cross_budget.json`.
The bounds are rigorous but **far too large to establish Schur
positivity**. The remaining 314-dimensional principal response F
has not been evaluated or lower bounded sufficiently, and Stage I
remains open.

This is a *negative numerical diagnostic* for the present coarse
norm method, not a proof of any actual negative Weil direction.

## Structural bottleneck: not all uncertainty is residual error

In the even sector, RC288's new 2x2 positive lower matrix is quite
close to singular. The physical P0/P4 trial-center projection Gram,
weighted by Gamma_lo^-1, contributes

    lambda^2 tr(Gamma_lo^-1 A_Z) ~ 2.35.

**This term alone exceeds one Mass_R** in the *present upper-bound
strategy*, even if the entire residual covariance S_new could be
made zero. Merely increasing precision on existing residual
calculations therefore cannot bring this particular nonnegative-sum
bound below one. This observation is about the **bound**, not a lower
bound on the actual C*Gamma^-1 C (center and residual may cancel).

The even optimized payment is roughly 158, dominated by
Gamma_lo^-1 amplification of correlated residual uncertainty.

In the odd sector, the corresponding center-only bound is about
0.266, below one, but the present residual contribution is too
large. Using theta=1, a sufficient *method-specific* condition for
a subunit odd payment is

    tr(Gamma_lo^-1 S_new)/d_R
       < 1/(2 lambda^2) - tr(Gamma_lo^-1 A_Z).

The right side is positive but the current covariance payment
exceeds it by more than a factor of five. A sharper projected
inverse-residual bound might attain it; this is not an actual
negative-eigenvalue inference.

## What remains usable

RC285's positive P0/P1 source directions and RC286's **subunit
single-source** cross envelopes are still valid in rank 317:

    even P0 cross < (4/5) Mass_R,
    odd  P1 cross < (3/4) Mass_R,

against their appropriate respective 121/194-dimensional remaining
subspaces. These remain *separate partitions*. In particular the
RC286 even P0 result does not pay the enlarged even P0/P4 joint
Schur cross block. The poor new joint estimate cannot invalidate
the previously valid single-source estimate.

## Next checkpoint RC290

**Even:** improve the correlated trial-center geometry and the
conditioning of the 2x2 positive source gate simultaneously, or
use directional rather than Hilbert-Schmidt estimates that can
certify center/residual cancellations. Mere smaller residual
roundoff will not fix the current center-only mass charge.

**Odd:** first target a stronger projected residual covariance
for P1, using degree-level cancellations or an optimized rational
trial. The current 1x1 pivot and RC286 cross result provide an
independent baseline.

Any new certificate must preserve entire original prime-jump,
archimedean and endpoint tails, and audit the new augmented
reference. The original nonpositive-index ceiling is unchanged.

## Replay

```bash
python scripts/validate_rpb108_rc289_joint_pivot_cross_budget.py --output certificates/rpb108_rc289_joint_pivot_cross_budget.json
python scripts/validate_rpb108_rc289_joint_pivot_cross_budget.py --output certificates/rpb108_rc289_joint_pivot_cross_budget.json --replay
```

This replays algebra and rational bounds against immutable RC129,
RC280, RC283, RC286 and RC288 source blobs. It does not
independently prove their analytic estimates. Stage I, global F4,
RH and Lean remain OPEN.
