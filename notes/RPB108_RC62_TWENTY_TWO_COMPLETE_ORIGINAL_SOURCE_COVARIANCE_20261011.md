# RPB108 RC62 — complete 22-feature original-source covariance

RC62 evaluates the complete signed nominal physical covariance of the original source on all 22 fixed native trial responses at cap B=11/10. Every archimedean, prime and signed-pole correlation is included, together with the native target q. The covariance is transported into a whole-matrix upper bound for the actual canonical original source, and it sharpens the actual Weil head through the original-source cancellation identity.

The new bounds resolve the two individual feature signs left open in RC61. **Every one of the 22 individual native feature directions has positive actual original Weil value.** This does not establish positivity of arbitrary linear combinations.

| Feature degree | New actual Weil quadratic lower | Upper |
|---|---:|---:|
| 8 | 0.0288869015 | 0.0389647975 |
| 11 | 0.0272698612 | 0.0362647210 |

These are outward decimal summaries of the exact rational intervals. The other 20 individual signs remain certified positive.

## Source definitions and scope

Write R22 for the actual canonical native Riesz representatives, V22 for their fixed 32-mode trials, and E22=R22-V22. Let K be the complete bounded physical remainder, including the archimedean remainder, all seven active prime-power translations, and the signed pole term.

The evaluated nominal physical source is

\[
F_{+,\rm nom}=q_{22}+K_{\rm nom}iV_{22}.
\]

The corresponding actual trial source is q22+K iV22. The actual canonical original source is

\[
\Sigma_+=i^*(q_{22}+K iR_{22})=R_{22}+\sigma.
\]

The certificate does not identify the nominal physical covariance with the actual canonical covariance. It pays the actual operator correction and the actual Riesz errors explicitly. These three source maps have distinct roles throughout the computation.

For the actual rank-22 native projection Pi22, the projected original and remainder sources agree:

\[
(I-\Pi_{22})\Sigma_+=(I-\Pi_{22})\sigma.
\]

RC62 does not yet evaluate that projected residual.

## Exact signed covariance assembly

The endpoint-log representation of q+K_arch,nom iV is constructed with the degree-192 kernels and exact Chebyshev conversion. The generalized residual builder has auxiliary Legendre targets; those targets are removed exactly before the native q is added. This avoids silently substituting a Legendre target for a Chebyshev target.

For F0=q+K_arch,nom iV, P=K_prime iV and O=K_pole iV, the full nominal physical source is F0+P+O. Its covariance contains all six terms:

\[
U_+=F_0^*F_0+P^*P+O^*O
+F_0^*P+P^*F_0
+F_0^*O+O^*F_0
+P^*O+O^*P.
\]

The pole signs are retained in both mixed terms. Combining the sources before bounding their norm preserves cancellation between components.

The prime source has 14 oriented translations from the complete active set 2,3,4,5,7,8,9. Its support changes across 15 physical segments. Polynomial/log primitive families integrate every archimedean-prime mixed term on those actual segments. Separate exponential moments evaluate the mixed pole terms, and the even/odd pole test-function norms evaluate the pole self-covariance.

All 253 nominal upper-triangle source entries are enclosed, including 121 exact opposite-parity zeros. Rational entry endpoints use denominator 10^20. Diagonal row-sum transport of the entry uncertainties yields the certified nominal physical Loewner upper Uplus_up. Exact rational LDL checks its positivity.

## Actual canonical source transport

Let delta_S be the certified correction from the old nominal bounded archimedean kernel to the actual one. It includes the corrected constant shift/radius and both kernel remainders. Let T be the physical trial Gram, Ep_up the actual physical Riesz-error Gram upper, and k_even,k_odd the complete physical operator norm bounds on the two parity sectors.

With D_k the parity diagonal matrix and u=1/32, the actual physical source-error Gram is bounded by

\[
B_S=(1+u)D_k E_{p,\rm up}D_k
+(1+u^{-1})\delta_S^2T.
\]

The inherited canonical embedding factor rho=252/257 then gives, with t=1/16,

\[
\Sigma_+^*\Sigma_+
\preceq\rho\left((1+t)U_{+,\rm up}+(1+t^{-1})B_S\right).
\]

This upper matrix is rounded outward to denominator 10^24 with exact diagonal row-sum allowances. A rational PSD bisection compares it with the physical native Gram. RC59's actual canonical lower bound M22>=0.3 P22 converts that comparison into a uniform actual-native-metric source bound. The accepted bound is a whole-matrix inequality for all complex coefficient vectors, not a collection of diagonal estimates.

The resulting conservative unprojected bound is

\[
\Sigma_+^*\Sigma_+\preceq\frac{8414545}{65536}M_{22}
\quad(128.395768\,M_{22}\text{ after outward decimal rounding}).
\]

This is an unprojected source upper bound on the enlarged 22-feature map. It does not meet or test the much smaller projected-source budget. The stored nominal covariance and actual upper matrix provide the data needed for the next projection calculation.

## Original-source cancellation in the actual head

Let Qtrial be the actual original Weil form on V22, already enclosed in RC61. With Fplus_trial=q+K iV, the exact identity is

\[
Q(R_{22})=Q(V_{22})
+(iE_{22})^*F_{+,\rm trial}+F_{+,\rm trial}^*(iE_{22})
-E_{22}^*E_{22}+(iE_{22})^*K(iE_{22}).
\]

The negative canonical error Gram keeps its sign. The new nominal source covariance bounds each trial-source norm after paying delta_S times the physical trial norm. These source norms replace the cruder separate component norm estimates used in RC61's head transport. Every resulting actual head entry is intersected with its previous enclosure and rounded outward rationally.

This entry refinement does not certify a uniform positive head floor. A whole-matrix lower bound must retain the source and error correlations, especially in weak combinations of the low features.

## Independent replay

Generation and replay use different evaluations for the principal integrations:

- Full nine-term logarithmic covariance versus five-term reflection reduction for the q-plus-archimedean source.
- Prime polynomial primitives on physical segments versus affine integration on [0,1].
- Direct three-log archimedean-prime integration versus the globally reflected two-log identity across the complete symmetric partition.
- Direct and reflected exponential/log moments for the archimedean-pole terms, with separately paid Taylor tails.
- Closed exponential primitives versus degree-100 Taylor integration for the prime-pole moments.

Replay verifies every stored nominal enclosure and then exactly rebuilds the signed assembly, rounding allowances, actual canonical transport, rational PSD source bound and actual head cancellation.

Generation and independent replay pass.

From the repository root:

```sh
python scripts/validate_rpb108_rc62_twenty_two_original_source_covariance.py > certificates/rpb108_rc62_twenty_two_original_source_covariance.json
python scripts/validate_rpb108_rc62_twenty_two_original_source_covariance.py --replay certificates/rpb108_rc62_twenty_two_original_source_covariance.json
```

## Remaining frontier

The next checks are a correlated whole-matrix original-head lower bound and the actual canonical projected-source residual on the 22-feature space. The unprojected bound supplied here does not establish the revised projected-source threshold. The existing low-eight floor and RC59 inverse enclosure remain available.

No 22-feature complement floor, whole-aperture positivity, aperture extension, RH, or F4 completion is claimed. The inherited complementary floor still belongs to the 1250-feature complement.
