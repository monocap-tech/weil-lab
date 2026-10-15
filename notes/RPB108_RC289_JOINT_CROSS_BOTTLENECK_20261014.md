# RC289 — full three-pivot cross-column payment and variance bottleneck

**Parent:** RC288 at `b96d942b60a725646fe71e53c2fa7980ac33b3d2`.
Aperture B=11/10. The native RC283 reduced rank-317 reference has
122 even and 195 odd source channels. Original Weil action unchanged.

## Result: rigorously paid, but not small, three-pivot coupling

RC288 certified the **joint even P0,P4** principal block and the
**odd P1** principal pivot using *new-reference* 3x3 inverse-residual
covariances. RC289 certifies all of their cross columns against every
one of the remaining **120 even + 194 odd = 314** Legendre channels.

| New-reference native block | Remaining channels | Rigorous upper bound |
| --- | ---: | ---: |
| Even `P0,P4` (2x2 SPD) | 120 | `C*Gamma^-1 C < 159 Mass_R` |
| Odd `P1` (1x1 positive) | 194 | `C*Gamma^-1 C < 3 Mass_R` |

The actual reported bounds, rounded upward to 20 decimal places, are
approximately **158.0755051** and **2.8416946**, respectively.
They are extremely conservative upper envelopes, not measured actual
couplings. They do *not* establish any negative direction, and
are too large to prove the remaining Schur positivity.

### Exact matrix inequality

In one parity, write the native auxiliary matrix as

    K = [[Gamma, C], [C*, F]].

The positive pivot set A is `{P0,P4}` even or `{P1}` odd.
RC288 certifies an exact rational Loewner lower matrix
`Gamma >= Gamma_lo > 0`; its entire 3x3 residual covariance upper
is `S`, and the appropriate principal restriction is `S_A`.

All selected RC280 rational trial polynomials `Z_i` have degree <=64
and are exactly the same trial polynomials in the rank-317 reference.
Define their **complete retained-rest physical projection Gram**

    (GZ)_ij = sum_(n in R) m_n (Z_i)_n (Z_j)_n,
    m_n=2B/(2n+1).

The true response is `G_new^-1 P_i=Z_i+X_i`. For every linear
combination of pivots, the inherited full source error covariance and
RC283's whole-domain positive reference lower form imply

    Gram_Physical(P_R X) <= S_A/d_R,

where `d_R=H_2+s_lower` even or `H_3+s_lower` odd. This pays **all**
remaining channels simultaneously; it does not assume independent
residuals, diagonalize a noncommuting inverse, or ignore cross terms.
For every `theta>0`, the exact matrix Young inequality gives

    C*Gamma^-1 C <= lambda^2 [
       (1+theta) tr(Gamma_lo^-1 GZ)
       +(1+1/theta) tr(Gamma_lo^-1 S_A)/d_R
    ] Mass_R.

The validator checks the selected 2x2 / 1x1 Loewner pivot lower
matrix is SPD, the selected residual covariance is SPD, all 65
original trial coefficients, the complete reduced reference Legendre
ranks, exact mass normalization and the RC129 D offset.

RC289 takes `theta=7` even and `theta=2` odd and rounds all
certificate results outward with exact rational arithmetic.

## Why merely optimizing Young cannot rescue this estimate

Set `A=tr(Gamma_lo^-1 GZ)` and
`Q=tr(Gamma_lo^-1 S_A)/d_R`, both strictly positive. Then the
*current envelope formula*, independent of the actual unknown
cross-column values, obeys

    Envelope(theta)
      = lambda^2 [(1+theta) A+(1+1/theta) Q]
      > lambda^2 Q.

The validator certifies strict rational floors

    lambda_even^2 Q_even > 120,
    lambda_odd^2  Q_odd  > 1.

Consequently **no choice of theta** within this variance-only
energy-projection majorant can produce a subunit Mass bound.
This is a no-go result for the *present sufficient estimate*, not
for the actual operators, residuals, or the prospect of obtaining
a different, directional/correlated bound.

In particular, the positive even block is relatively ill-conditioned:
charging its soft linear combination by full inverse-residual energy
and one global `d_R` produces most of the cost.

The **separate RC286 single-pivot** cross certificates in the *same
rank-317 reference*, even P0 <4/5 Mass_R and odd P1 <3/4 Mass_R,
remain valid and strictly tighter. One may not attribute those
single-pivot payments to RC288's enlarged even two-pivot block,
and the new block cannot be eliminated at the old price.

## Mathematical/implementation custody

The entire calculation is exact Fractions against immutable SHA1 Git
blobs from RC129, RC280, RC283, RC288 and RC286. The validator checks
positive pivot Loewner matrices and complete covariance matrices
before paying trace bounds; all 314 cross columns are covered through
physical projection and matrix Young. No new original Weil arithmetic,
inverse-response solve, or proof of `F-C*Gamma^-1 C>0` is asserted.

The original nonpositive-index census remains unchanged. Stage I,
F4, RH and Lean are OPEN.

## RC290 cursor

Compute the *projected inverse response covariance* specifically on
the retained rest of the rank-317 reference—especially the soft even
`P0,P4` direction—rather than paying its entire residual energy
with the weakest common physical D weight. Preserve the source
correlations and original/infinite tails. Compare a smaller or rotated
positive pivot block against the independent RC286 single-pivot
route; advance to the 314-dimensional Schur principal form only
when the new block-to-rest payment is adequate.

## Reproduce

```bash
python scripts/validate_rpb108_rc289_joint_cross_bottleneck.py --output certificates/rpb108_rc289_joint_cross_bottleneck.json
python scripts/validate_rpb108_rc289_joint_cross_bottleneck.py --output certificates/rpb108_rc289_joint_cross_bottleneck.json --replay
```
