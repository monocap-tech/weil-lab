# CC79 — quantitative acceptance windows for the collective join

Read [CC79 definitions](../docs/TERMINOLOGY_RPB108_JOIN_CORRELATION_BUDGET_CC79.md). Integration parent is CC78, 14dcfae9c91304f2fc8677586605f795f0d06c6e. Read-only source remains NF34, f353936b780a4d988ec242a647ab985404f5b69e. This consumer prepares the mixed-correlation acceptance test without duplicating a source integration producer.

## What the signed crosses must establish

The prior pair A and new diagonal c pass in each parity. To join them, the border b=n-g/kappa must satisfy b*A^-1b<c. This is the minimal sufficient fixed-family border estimate. Every passing matrix must also satisfy the following necessary covariance windows:

| Parity and pair coordinate | Necessary radius around kappa n_i, strict upper bound | Radius / Cauchy envelope, upper bound |
| --- | ---: | ---: |
| Even seed | 4.888e-30 | .136 |
| Even response | 1.287e-30 | .860 |
| Odd seed | 1.957e-26 | .398 |
| Odd response | 6.807e-28 | .150 |

The center is the actual signed native cross; the window is not centered at zero. The small even-seed and odd-response windows identify the most demanding coordinate cancellations relative to the available norm envelopes. Their exact outward rational values are in the certificate. Passing both coordinate windows is still insufficient: the prior off-diagonal A01 controls the orientation of the full acceptance ellipse.

## Precisely what the reduced packet cannot establish

The consumer constructs two signs of a PSD three-source Gram completion for each old source coordinate. It preserves the same positive old two-source block and the same new source-square diagonal. With alpha a rational lower bound for sqrt(Gamma22/Gammajj), the cross column is plus or minus alpha Gamma[:,j]. The remaining source diagonal gamma-alpha^2 Gammajj is nonnegative, proving both completions PSD.

Each completion's j-th cross magnitude exceeds the necessary covariance radius. For every fixed native center n_j, at least one sign has |g_j-kappa n_j| at least that magnitude and violates the corresponding principal minor. Thus the reduced norm-and-diagonal packet cannot certify the collective join uniformly over its admissible completions. This is a proof about that named reduced packet only. It neither rejects the actual arithmetic join nor claims that the complete Weil identities cannot imply it. The complete source construction can resolve the missing crosses by direct arithmetic certification.

The new exact controls use A=[[2,1],[1,2]], c=2s^2, b=s t(2,1). The border Schur value is 2s^2(1-t^2), crossing positive/null/negative at t=.99,1,1.01 for s=1 and 10^-18 while all diagonals remain positive. At the null control, the exact kernel proves that whole-physical-mass shifts .001,.1,2 have those exact positive ground levels. These are genuine matrix crossings and positive-level tests, not actual arithmetic countermodels.

## Next task and preserved results

NF35's useful deliverable is the signed native and complete source border with paid uncertainty, followed by the full three-by-three sufficient matrix sign in each parity. The ellipse criterion supplies the acceptance target. A pass gives six retained directions together with the entire F112; it still leaves 106 retained directions and the full collective coupling. A failed reduced-packet control is not evidence that the actual signed border fails.

CC74's Z4+F112 physical gap >3.1004e-36 and CC78's separate U2+F112 gap >1.6476e-22 remain preserved. A simultaneous six-direction certificate is not claimed. Whole-domain 53/50 positivity, full retained infinite-high sign, uniform all-cap leakage/frame, RH/F4/full transport and Lean remain open. Whole-domain anchor stays 21/20 with margin 1/(3*10^63); paused fronts and historical wording remain unchanged.

## Reproduction

Run scripts/certify_join_correlation_budget_cc79.py with the CC74 NF30 source certificate, CC73 NF29 parent certificate, and CC78 even and odd NF34 source certificates; specify --output. All four inputs are hash authenticated. Every root is computed by the existing outward rational square-root engine. Custody records the consumer replay, exact hashes and publication checks.
