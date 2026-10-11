# RC82: direct Riesz-error attachment to the original source

Date: 2026-10-11. RPB108 route consolidation. Status: PASS.

RC82 attaches RC81's direct 64-dimensional Riesz-error certificate to the existing original source residual calculation. It tightens the projected transfer covariance and the final rank-38 residual upper, while preserving the original source identity, the nominal 64-mode trial vectors, and the 22-input scope.

| Quantity | Certified result |
| --- | --- |
| Actual canonical target projection rank | 38 |
| Existing source input count | 22 |
| New uniform residual upper relative to actual canonical input Gram | 2061/4096 = 0.503173828125 |
| Even factor; residual Young parameter | 2061/4096; 1/4 |
| Odd factor; residual Young parameter | 471/1024; 5/16 |
| Prior RC79 factor | 417/512 = 0.814453125 |
| Fractional decrease of certified scalar upper bound | 425/1112, approximately 38.21942% |
| Even nominal enclosure relative to actual input Gram lower: upper | 1291/4096 = 0.315185546875 |
| Even transfer enclosure relative to actual input Gram lower: upper | 25/1024 = 0.0244140625 |
| Odd nominal enclosure relative to actual input Gram lower: upper | 1187/4096 = 0.289794921875 |
| Odd transfer enclosure relative to actual input Gram lower: upper | 53/2048 = 0.02587890625 |

These are certified upper-enclosure comparisons, not measurements of actual residual energies. The required scalar source budget remains uncertified.

## Unchanged original source and nominal residual

The original complete physical source remains F=q+K iR_22. Its nominal approximation uses RC67's physical 64-mode trials V_64 and RC68's nominal operator. RC71 supplies the physical polynomial-subtraction residual Gram upper W for polynomial degree less than 38. RC79 applies the actual canonical adjoint tail map B_38=(I-Pi_38)i*, with ||B_38||<=tau from RC78, and obtains the canonical nominal residual enclosure

N=tau^2 W.

RC82 reconstructs this matrix from RC71 and verifies exact equality with RC79's saved N. No nominal residual entries, physical trial coefficients, operator norm constants, or actual head definitions change in this attachment. The polynomial Riesz images belong exactly to the actual rank-38 head, so subtraction introduces no extra Riesz approximation error.

## Attach the new physical Riesz-error matrix

RC81 directly certifies the physical Riesz-error Gram upper E_phys,new for the same V_64, with an exact Loewner improvement over RC67's E_phys,old. RC82 checks both positivity and E_phys,old-E_phys,new>=0.

Keep rho=252/257, RC79's parity projected arch/prime/pole bounds k_p expressed in units of sqrt(rho), its tail/global ratio s=tau^2/rho, RC68's source operator approximation error delta, and the exact trial physical Gram T. With source-transfer Young parameter nu=1/65536, form the outward-rounded matrix

E_eq=(1+nu) D_k E_phys,new D_k+(1+1/nu)*delta^2*s*T.

The projected canonical transfer enclosure is E_can=rho E_eq. The same actual source decomposition and parity-preserving correlated transport as RC79 justify this covariance upper. The stronger direct error matrix changes only the Riesz-error part of the transfer. No additional canonical tail factor is applied to the already projected prime bound.

Exact rational PSD checks prove E_eq,RC79-E_eq>=0. Keeping RC79's residual Young parameters also proves that the whole residual upper matrix improves in Loewner order.

For parity parameters t_p>0, the final outward-rounded matrix is

A(t)=(1+t_p)N+(1+1/t_p)E_can.

A finite exact search selects t_even=1/4 and t_odd=5/16. Exact PSD comparisons against RC67's actual canonical input Gram lower establish

Gamma_38 <= (2061/4096) M_22.

The displayed 38.21942% decrease compares scalar upper bounds. It is not a measured decrease of the fixed actual source residual.

## What still limits this method

The separate component upper comparisons in the table use the actual input Gram lower to certify valid uniform upper bounds. They show the retained nominal enclosure is the larger component in this certificate. They do not quantify a decomposition of the actual residual or assert that the two components are orthogonal.

RC80's fixed nominal-allowance boundary still applies because N is unchanged. In the physical Legendre degree-20 input direction, any positive-Young upper enclosure retaining N has a relative factor at least approximately 0.03557598215037, even if the transfer enclosure is set to zero. This exceeds RC63's inherited scalar source-budget ceiling by more than two billion times. RC82 independently checks the exact directional comparison and stores it in the certificate.

That is a limitation of retaining this nominal upper enclosure, not an actual leakage lower bound. RC63's ceiling uses its weak head bound and the inherited 1250-feature complement floor; RC82 does not assert a floor for the rank-38 complement. Further Riesz-error reduction alone cannot certify that ceiling while N is retained. The next quantitative frontier is a tighter nominal source projection or a source-specific canonical covariance that preserves information discarded by the current physical-norm transport and positive Young split.

## Independent validation and provenance

Generation computes the trial physical Gram by matrix contraction and forms the final covariance in units of rho. Independent replay reconstructs T by direct physical mass sums, forms the transfer by exact diagonal congruence, and assembles the final residual directly from N and E_can. Replay checks every final parity comparison after inverse Chebyshev-to-Legendre congruence. All acceptance conditions are rational PSD comparisons, exact equalities, or rational directional inequalities.

Generation and independent replay passed. Input order: RC81, RC79, RC67, RC68, RC71, RC59, RC70, RC80, RC63. The JSON records all nine SHA-256 hashes and checks the inherited direct-error, source, trial, head, boundary, and weak-floor provenance links.

- scripts/validate_rpb108_rc82_direct_error_source_attachment.py
- certificates/rpb108_rc82_direct_error_source_attachment.json
- notes/RPB108_RC82_DIRECT_ERROR_SOURCE_ATTACHMENT_20261011.md

Replay with default repository paths:

`python scripts/validate_rpb108_rc82_direct_error_source_attachment.py --replay certificates/rpb108_rc82_direct_error_source_attachment.json`

The source input count remains 22 and the actual target head remains rank 38. The required scalar source budget, any actual rank-38 budget failure, a 38-input covariance, and an enlarged Weil floor remain unresolved. No whole-aperture positivity extension, RH, F4, or Lean formalization is claimed.
