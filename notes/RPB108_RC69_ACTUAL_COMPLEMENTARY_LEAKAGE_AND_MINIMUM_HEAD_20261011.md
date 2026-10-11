# RPB108 RC69 — actual complementary leakage and minimum head

RC69 certifies actual source leakage outside the consecutive native projection. The inherited scalar Schur source-budget ceiling fails for every native head with 22 through 37 features. Therefore at least 38 consecutive native features are necessary for that budget. This is a lower bound on the required consecutive head count, not a claim that 38 features suffice.

The older fixed source budget 1/64000000 also fails for heads 22 through 35. Together with RC58's failure for heads 8 through 21, at least 36 consecutive features are necessary for that older budget.

Unlike a large upper bound, these are actual directional lower witnesses. They concern the actual canonical source and orthogonal projection, with all nominal trial errors paid.

## Exact complementary witnesses

RC69 uses the two fixed rational low-eight source directions recorded in RC56, padded into the 22-feature coefficient space. Their nominal original source is evaluated on RC67's enriched 64-mode trials with the complete original archimedean, full paired-prime, and signed-pole source conventions of RC68.

For a physical Legendre polynomial P_n and any native physical target q_j of degree j<n, exact integration gives <P_n,q_j>_phys=0. The canonical Riesz identity then gives

\[
\langle P_n,R_j\rangle_{\mathrm{can}}=0.
\]

Thus P_n is canonically orthogonal to every consecutive actual native head of size N<=n. This orthogonality uses the actual representatives; it does not rely on the accuracy of finite Riesz trials.

The implementation evaluates individual tests of degrees 22 through 63. It then forms same-parity combinations supported on degrees d,d+2,...,63. Their exact rational coefficients are the nominal source-pairing midpoints divided by physical Legendre masses. Those finite rational vectors, their interval pairings, and their norms are stored in the certificate. Every such combination remains canonically orthogonal to heads N<=d.

## Actual pairing and lower bound

Let v be one fixed source input, z an exact complementary test, and Sigma_plus(v) the actual original canonical source. RC68 supplies the nominal source approximation error delta. RC66 supplies the complete physical parity operator norm upper bound k_p. RC67 supplies the correlated physical Riesz error bound e_v and physical trial norm t_v. The actual physical source transfer is bounded by

\[
\epsilon_v\le k_p\sqrt{e_v}+\delta\sqrt{t_v}.
\]

A nominal physical pairing enclosure [b_-,b_+] therefore gives the actual canonical source pairing enclosure

\[
\langle z,\Sigma_+(v)\rangle_{\mathrm{can}}
\in[b_- -\|z\|_{\mathrm{phys}}\epsilon_v,
      b_+ +\|z\|_{\mathrm{phys}}\epsilon_v].
\]

The native target part is orthogonal to z, so this is also the sigma pairing. Because z is orthogonal to the actual head, the pairing equals that of the actual projected source residual.

The canonical test norm upper is computed with the recentered 64-mode metric and its certified mass-relative error. The actual source input norm upper is the minimum of the physical embedding bound and RC57's actual low-eight canonical Gram upper. Let D be the distance of the actual pairing interval from zero. Canonical Cauchy-Schwarz gives

\[
\frac{\|(I-\Pi_N)\Sigma_+(v)\|_{\mathrm{can}}^2}
     {\|R(v)\|_{\mathrm{can}}^2}
\ge \frac{D^2}{Z_{\mathrm{up}}M_{v,\mathrm{up}}}.
\]

This directional inequality disproves a proposed uniform Gram upper budget when its right side exceeds that budget. It is not a Loewner lower bound on the entire source Gram.

## Certified odd combinations

All rows below use the same exact low-eight odd source direction. Each test is supported on the indicated odd degrees through 63.

| Minimum test degree | Applies to consecutive heads | Actual directional residual lower | Ratio to RC63 ceiling |
|---|---|---:|---:|
| 23 | 22–23 | approximately 1.44781433e-7 | approximately 8474.41 |
| 33 | 22–33 | approximately 4.19209007e-8 | approximately 2453.73 |
| 35 | 22–35 | approximately 2.92816251e-8 | approximately 1713.93 |
| 37 | 22–37 | approximately 2.99365175e-9 | approximately 175.23 |

The exact fractions in the certificate, rather than the displayed decimal approximations, establish all comparisons. The degree-37 combination exceeds the ceiling approximately 1.7084534755e-11 by more than 175 times. The degree-35 combination exceeds the older fixed budget 1.5625e-8. The degree-23 combination supplies the strongest lower witness, including for the actual rank-22 projection.

The evaluated tests with minimum degree 39 and higher do not give a positive lower bound after transfer allowances. A zero certified lower bound means these estimates do not resolve that test; it does not mean actual leakage is zero.

## Independent replay

Generation uses the full three-log archimedean pairing, physical prime polynomial primitives, and Taylor pole moments with explicit uniform tails. Replay uses the reflected two-log pairing, affine prime integration on each support segment, and closed exponential primitives. It independently verifies every exact polynomial moment orthogonality relation, all square-root upper conditions, and the combined-test Cauchy-Schwarz ratios. The resulting certificate is reproduced exactly.

## Evidence boundary

The ceiling is the requirement of the inherited scalar sufficient Schur method with its 1250-complement floor and RC63's head-floor ceiling. It is not a necessary condition for positivity by every possible method. No rank-22 or rank-37 complement floor is asserted.

The dimension bound applies to the consecutive native feature family, not arbitrary subspaces of that dimension. It does not prove source-budget failure at 38 or 1250 features. No negative Weil direction, aperture positivity obstruction, full 1250 projection, new aperture positivity, RH, or F4 conclusion follows.

The certified rank-22 residual upper bound remains RC68's 471/32. RC69 supplies a separate actual lower witness and shows that refining a rank-22 upper estimate alone cannot certify the inherited scalar budget. A larger consecutive projection or a different positivity criterion is required for this route to advance.

## Added artifacts

- `scripts/validate_rpb108_rc69_enriched_complementary_leakage.py`
- `certificates/rpb108_rc69_enriched_complementary_leakage.json`
- This report.

Historical milestone artifacts remain unchanged.
