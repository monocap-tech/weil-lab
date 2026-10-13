# RPB108 — RC206: direction-sensitive trial-error inverse payments

Parent RC205, commit 3a6ecc1f075a19a1b8ae89c5bbf87de4d3ed785a. Aperture 11/10, actual supported M=D^-1 L, response sources P0,P2,f0,psi0,w14,v10, and raw trial directions P0,P2,f0,psi0,w14,q185,v10,q202 are unchanged. The selected least-residual coefficient map Y and complete nominal residual/source/tail data remain exactly RC203's data.

## Result

The exact relative six-source inverse width improves from **0.720712 to 0.672096** (21003/31250). The relative reduction is 6077/90089, approximately **6.75%**. The exact half-Gram gate remains failed; its threshold is 0.5.

| Same-family certified quantity | RC205 | RC206 |
| --- | ---: | ---: |
| Six-source inverse width | 0.720712 | 0.672096 |
| Width / half-Gram threshold | 1.441424 | 1.344192 |
| Threshold minus width | -0.220712 | -0.172096 |
| Selected variational width | 0.466716 | 0.350796 |
| Selected uniform action-error Gram factor | 0.002365 | 0.003252 |
| Half-Gram acceptance | Failed | Failed |

The selected action-error Gram factor becomes worse as a uniform scalar bound, while its directional shape yields smaller inverse payments. No ordering between the old and new error Grams is asserted. In particular, uniform scalar error reduction is not a necessary condition for same-family inverse-width progress. Neither the true physical error nor the unchanged nominal residual Gram is claimed to decrease.

## Exact error-envelope construction

For positive rational weights w_i and the eight inherited individual error norms epsilon_i, let C=sum_i epsilon_i/w_i and H=diag(C epsilon_i w_i). The exact PSD test H-epsilon epsilon^T >= 0 verifies the diagonal Cauchy majorant. For every real response vector x,

    ||error(Yx)|| <= sum_i epsilon_i |(Yx)_i|,
    (sum_i epsilon_i |(Yx)_i|)^2 <= x^T Y^T H Y x.

The diagonal majorant applies to absolute values, so it bounds every signed mixture; no orthogonality or independent errors are assumed. The real error maps and real/imaginary splitting extend the same Gram bound to complex response vectors.

Independently rebuild RC204's 128 fixed-trial signed controls and 768 positive integer minors. Its signed majorant is E_signed=(473/200000)G_lower. Thus for 0<=lambda<=1,

    E = lambda Y^T H Y + (1-lambda) E_signed

is a lawful bound for the same fixed-trial error. Joint proposal optimization varies the eight positive weights, lambda and the three positive Young parameters. The selected exact lambda is **1**: the best certified candidate uses the directional triangle majorant alone. The signed-bound candidate and RC205's independently certified inverse endpoints remain available.

Transport E using RC205's unchanged formulas for variational action/tail payments and actual residual lower/upper bounds. Reconstruct RC203's original payment exactly before removing it to expose the unpaid base endpoints. Keep both complete signed source and residual tails and RC121 coercivity a=32125/230953. Accept only PSD lower endpoints, PSD inverse gaps and exact relative-width domination matrices. The millionth-grid width is accepted; the preceding grid value fails that sufficient test.

The selected positive rational parameters are:

- action theta = 3486532239/(5*10^11),
- tail theta = 102479115163/(125*10^9),
- upper residual tau = 63648974681/(250*10^9),
- lower residual sigma = 0, using the independently valid zero lower.

Both selected inverse endpoints are refined. The certificate stores all eight rational weights and the resulting action-error Gram, variational endpoints, residual bounds and inverse bounds.

## Verification and custody

RC203, RC121 and RC205 certificates are pinned by immutable Git blob hashes, along with all six imported validator modules. RC205 certificate blob is 460cad6cf77581db35662204d319ab30c9c1c2c7. The entire source family, trial map and carrier data are inherited as certified premises; the physical 65534-degree reconstruction is not rerun here.

Powell/SLSQP generate proposals only. The selected enclosure is verified independently by exact rational PSD elimination. Replay uses stored rational proposals, reverses signed controls, proposal order and residual-lower search order, and requires exact equality of the whole certificate. Negative controls reject a mismatched input Git pin, zero triangle weight and convex mixing coefficients outside [0,1].

```bash
python scripts/validate_rpb108_rc206_directional_error_inverse.py --output certificates/rpb108_rc206_directional_error_inverse.json
python scripts/validate_rpb108_rc206_directional_error_inverse.py --replay --output certificates/rpb108_rc206_directional_error_inverse.json
```

## RC207 cursor and evidence boundary

The gate remains open by a sufficient-enclosure deficit of 0.172096 G_lower. This is not a lower bound on actual inverse uncertainty, and no iteration-count or completion-time claim follows. Next, tighten the source-residual cross-tail/nominal residual enclosure or enrich the trial with its complete canonical action and a newly paid error bound. A changed Y requires recertifying its fixed-trial signed envelope.

Native z_b6/t10 full action coverage, odd-parity/source-range and original augmentation acceptance remain open. Stage I, original Weil positivity, RH, F4 and Lean closure are unclaimed. This is an add-only RC continuation; historical/source/LF branches remain untouched.
