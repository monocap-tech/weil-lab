# RPB108 — RC205: signed trial-error transport into the six-source inverse

Parent RC204, commit e2f28614ebf037efa7db567afc57d2ddb103665a. Aperture B=11/10; supported canonical operator M=D^-1 L and D-energy norm are unchanged. Response sources remain P0,P2,f0,psi0,w14,v10; raw trial directions remain P0,P2,f0,psi0,w14,q185,v10,q202. The least-residual coefficient matrix, complete nominal residual Grams, actual source Grams and all signed analytic tails are inherited verbatim from RC203.

## Result

RC204's exact fixed-trial bound E <= (473/200000) G_lower is now transported through the actual inverse Loewner enclosure. The exact certified six-source relative inverse width improves from 0.743003 to **0.720712** (90089/125000), a reduction of 22291/743003, approximately 3.00%.

| Same-family certified measurement | RC203 | RC205 |
| --- | ---: | ---: |
| Inverse width relative to G_lower | 0.743003 | 0.720712 |
| Width / half-Gram threshold | 1.486006 | 1.441424 |
| Threshold minus width | -0.243003 | -0.220712 |
| Uniform squared trial-action-error factor | 0.002504 | 0.002365 |
| Selected variational width | 0.452039 | 0.466716 |
| Half-Gram gate | Failed | Failed |

The selected variational width increases because parameters optimize the complete inverse width, rather than the variational component alone. No actual physical error, nominal residual Gram or source data is claimed to shrink. The remaining deficit concerns this sufficient enclosure; it is not a lower bound on the true inverse uncertainty.

## Lawful transport

Let U=Yx, with exactly RC203's selected least-residual Y. RC204 proves that the actual action error of these fixed trials has Gram at most E=(473/200000)G_lower. Rebuild all 128 sign controls and their 768 positive integer leading principal minors before using E. The bound is not transferred to a different trial map.

Recover the unpaid variational endpoints B_lower, B_upper by adding/subtracting RC203's stored payment. Reconstruct that payment exactly as a consistency check. Let G_U be the upper trial-source Gram; let U_tail and R_tail be the unchanged complete source and residual tail Grams. For positive theta and t, set

    P = theta G_U + E/(4 theta) + t U_tail + R_tail/(4 t),
    C_lower = B_lower - P,   C_upper = B_upper + P.

For positive tau and optional 0 < sigma <= 1, use the original Young inequalities

    R_upper = (1+tau) N_upper + (1+1/tau) E,
    R_lower = (1-sigma) N_lower - (1/sigma-1) E.

Sigma=0 uses the independently valid zero residual lower. Only PSD residual lower candidates are accepted. With RC121's unchanged coercivity a=32125/230953, the inverse bounds are C_lower+R_lower/2 and C_upper+R_upper/a. Independently certified RC203 inverse endpoints remain available. Every selected lower, endpoint gap, relative-width domination and half-Gram acceptance test uses exact rational PSD elimination.

The selected exact parameters are theta=7224189351/10^12, t=2398534523191/10^12, tau=132043107987/(5*10^11), sigma=0, with refined lower and upper endpoints. Powell and SLSQP are proposal mechanisms only. Replay reads stored rational proposals and does not run numerical optimization. The millionth-grid width is accepted, while its immediately preceding grid value is rejected by the sufficient matrix test.

## Custody and verification

Both input certificates and all five imported validator modules are pinned by immutable Git blob hashes. RC203's blob is 5d321b659367ba459682b557b12ef63451f63e49. RC121's blob is 089664ca7eb9139fec1ba0f58b4cfbf25902f51a. The verifier rejects mismatched data or helper code before accepting the enclosure. The RC203 analytic ancestry is reused as a certified premise; this turn does not rerun the 65534-degree physical reconstruction.

Run:

```bash
python scripts/validate_rpb108_rc205_signed_error_inverse.py --output certificates/rpb108_rc205_signed_error_inverse.json
python scripts/validate_rpb108_rc205_signed_error_inverse.py --replay --output certificates/rpb108_rc205_signed_error_inverse.json
```

Exact replay reverses sign controls, proposal order and lower-residual parameter order, and requires equality of the entire certificate. Input-integrity and nonpositive-parameter rejection are also checked. No Lean validation is claimed.

## RC206 cursor and evidence boundary

The six-source half-Gram gate remains open. Refine the variational cross/source-residual enclosure and signed tail payments, or enrich the residual trial only with its complete action and new error proof. The scalar signed bound is specific to the fixed RC203 Y. It must be recertified if Y changes. Native z_b6/t10 action coverage, odd-parity/source-range coverage, original augmentation and Stage I acceptance remain open. RH, F4 and Stage I closure are unclaimed. The accepted five-source result and other research branches are preserved.
