# RPB108 — DNE42 encloses the full-packet uniform-floor target

Parent: DNE41, `bae3aa15f5db9beb87feeddf36c33b6d03f9534a`, on `research/rpb108-direct-null-exclusion`.
Terminology was registered before computation in `docs/TERMINOLOGY_RPB108_DNE42_UNIFORM_FLOOR_TARGET.md`.

DNE42 proves a sharp sufficient target for the three unresolved comparison directions in the existing 72-column source packet. It does not improve the original infinite high lower bound. Actual original positivity remains 69 retained directions plus the entire infinite F112, with the DNE41 physical guard 1e-39; 43 retained dimensions remain uncovered.

## Certified targets

For each parity let N36 be the authenticated original native matrix and G36 the paid complete original projected-source Gram. The native matrix is strictly positive. The basis invariant threshold rho=max(v*G36 v/v*N36 v) is enclosed by an exact rational trial below and a paid rational congruence of u N36-G36 above. All 36 columns and all mixed correlations are retained.

| Parity | Certified lower endpoint (decimal display) | Certified upper endpoint (exact decimal) | Bracket width, upper bound |
|---|---:|---:|---:|
| Even | 0.6024009488966369 | 0.60240095 | 1e-8 |
| Odd | 0.5954841534052450 | 0.59548416 | 1e-8 |

The lower endpoints in the JSON certificates are exact rational numbers; displayed decimals are rounded. Both upper endpoints are exact rationals. At each upper endpoint, the entire 36-dimensional comparison is strictly positive. Consequently the single rational target **603/1000** is sufficient in both parities, by positivity of N36 and monotonicity. If this were independently established as a lower bound for the original infinite high restriction, all 72 computed retained directions, together with F112, would be positive. Forty retained dimensions outside the computed packet would still remain open.

The established original high floor is **289/500=0.578**. The necessary increases for this full-packet scalar route exceed approximately 0.0244009488966369 even and 0.0174841534052450 odd. DNE39's stronger unrounded weight floor 0.578251243732 also remains below both thresholds. A new high estimate is required; changing coordinates cannot alter these generalized Rayleigh thresholds.

## Exact sign and physical payments

The inherited DNE40 exact failure trial is reused. Outward native and source quadratic intervals q and g satisfy q_lower>0. The exact lower target is g_lower/q_upper. The candidate upper target is its ceiling on the rational 1e-8 grid. A decimal LDL calculation selects a rational triangular congruence U; an outward interval computation proves every Gershgorin margin of U*(u N36-G36)U strictly positive. Decimal calculations are proposals only.

The independent verifier uses exact Fraction endpoint arithmetic, rather than the producer's outward 120-digit interval grid. It audits the inherited native positivity certificate, input hashes and source-audit linkage, all full comparison entries, every congruence entry, each Gershgorin margin, trial energy enclosures, target widths, and monotonicity inputs. It also authenticates the DNE41 passing audit and preserves its actual rank 69.

The conditional physical bounds at the respective upper targets are approximately 1.964757440e-44 even and 2.719320052e-39 odd. These are conditional bounds, not new actual guards. They use the original packet's exact physical masses M, the paid upper source trace T, and d=min_margin/||U||_F^2 through min{(d/u)/(4(M+T/u^2)),u/2}. Source trace bounds are checked by enclosure because outward rounding may enlarge them.

## Directional response alternative and coupling

The scalar target is sufficient but not necessary for actual original positivity. With k=289/500 and actual infinite high operator L_F, define the response credit C=G36/k-Z*L P_F L_F^{-1}P_F L Z. The established high floor implies C is positive semidefinite. The true finite Schur matrix is H/k+C, where H=k N36-G36. No value of C is computed in DNE42.

In the exact DNE41 basis (B,D), B has dimensions 34 even and 35 odd, and D has dimensions 2 even and 1 odd. Set A=B*(H/k+C)B, E=B*(H/k+C)D and F=D*(H/k+C)D. A is positive because B*H B is positive and C is positive semidefinite. Closing the computed packet is therefore equivalent to positivity of F-E*A^{-1}E. A future directional response estimate must pay this coupling; a positive correction on the D block alone is insufficient without control of the mixed block. This formula identifies the remaining small gate but does not discharge it.

## Validation and next obligation

The independent audit passes **15,907 exact rational checks**. Both new scripts pass syntax compilation. No source integration or high-floor audit is repeated. Existing source payments, retained rank, and high positivity are inherited through authenticated passing audits; their historical check counts are not counted as new checks.

The next substantive obligation is to establish additional original high information: either the sufficient common floor 603/1000 or a paid directional inverse-response bound closing the coupled 2-even/1-odd gate. The other forty retained source directions also remain to be covered. Actual inverse evaluation, whole a=53/50 positivity, first-contact exclusion, RH and Lean remain open.

Reproduce by running `scripts/certify_dne42_uniform_floor_target.py PARITY --output CERTIFICATE.json` for both parities, followed by `scripts/validate_dne42_uniform_floor_target.py EVEN_CERTIFICATE ODD_CERTIFICATE --output VALIDATION.json`. Require PASS before publication.
