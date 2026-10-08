# RPB108 NF60: pole matching does not rescue fixed-width global smearing

Date: 2026-10-08 UTC. Recovered shared head c862cf867ea30d6e8a192d424ffa259038b25884, including the concurrent prime-8/a=1.05 audit. Definitions: [smearing edge](../docs/TERMINOLOGY_RPB108_SMEARING_EDGE.md).

## Outcome

The fixed-width global smearing route is stopped as an active global closure candidate. Two actual-carrier tests dispose of the repairs suggested by NF59:

1. Pole matching with the ORIGINAL frozen prime dictionary is unconditionally negative on large-window smooth opposite-sign packets, by the already adopted classical PNT.
2. Adding the prime halo removes that edge mismatch, but even under RH its comparison form is negative on long packets in low-frequency gaps. Therefore positive lower bounds plus successful original sign transfer at every aperture cannot be achieved with one fixed nonzero width by this repair either.

No ORIGINAL negative Weil vector is constructed. Adaptive widths remain unexcluded but have no proved all-window lower-bound mechanism here. NF57/NF58 remain valid approximation and conditional sign-transfer results. This audit closes this specific candidate as a failure; it does not shorten the original source-gain proof graph.

## 1. Pole-matched frozen primes: the missing edge contribution

Fix 0<delta<=exp(-4), b=1/8, and a smooth real nonnegative psi supported in [-b,b], positive on its interior. For R>b set

    h_R(x)=psi(x-R)-psi(x+R), a_R=R+b,
    J=integral exp(u/2)C_psi(u)du>0,
    phi_delta(u)=average_(|v|<=delta) C_psi(u+v),
    H_delta=integral_(2b)^infinity exp(u/2)phi_delta(u)du.

The packets are smooth actual physical vectors in D_(a_R), of constant mass. H_delta>0: averaging spreads the positive correlation past its original endpoint 2b. For example phi_delta is positive on (2b,2b+delta/2), because averaging samples values u+v strictly inside (-2b,2b).

The whole averaged cross integral is alpha_delta J. The FROZEN actual cutoff log n<=2a_R, however, keeps only the part with displacement u=log n-2R<=2b. The weighted PNT limit from NF59 therefore gives cross-prime coefficient

    +2exp(R)(alpha_delta J-H_delta)+o(exp(R)).

The sign is positive because the two physical bumps have opposite signs. The pole-matched cross pole contributes -2alpha_delta exp(R)J+O(exp(-R)). Archimedean cross terms decay, and all self terms are fixed. Consequently

    Q_frozen-matched(h_R)/exp(R) -> -2H_delta<0.              (1)

The PNT test is truncated at one displacement endpoint. This is lawful: the limiting measure exp(u/2)du has no atom there; approximate the bounded piecewise smooth test from above and below. The single prime-power endpoint atom also tends to zero in the normalized measure, using Lambda(n)<=log n. No shrinking-interval PNT assertion is made.

The ORIGINAL unsmeared cutoff has no edge loss: C_psi(u)=0 for u>2b. Its leading pole and prime terms still cancel, leaving the ORIGINAL value divided by exp(R) tending to zero with no sign conclusion. Equation (1) is a comparison defect, not an actual zero or original negative vector.

## 2. Including the prime halo: correct main term, wrong global sign

Include the additional primes up to log n<=2a+delta, so every possible averaged correlation is included, and retain the pole factor alpha_delta. Let Q_halo denote this comparison. The preceding edge term disappears. That does not prove positivity.

For a smooth supported vector, Q_halo is obtained by box-averaging the ENTIRE physical Weil distribution and then restoring the unchanged archimedean form. Box-averaging the pole multiplies it by alpha_delta exactly. The halo makes the averaged prime part complete. In physical Fourier frequency xi the box multiplier is

    sigma_delta(xi)=sinc(2pi xi delta).

Under the CONDITIONAL hypothesis RH, the actual literal formula therefore gives

    Q_halo(h)
      =sum_rho nu_rho sigma_delta(theta_rho)|hhat(theta_rho)|²
         +integral m0(xi)[1-sigma_delta(xi)]|hhat(xi)|²dxi.    (2)

Here theta_rho are real physical frequencies and nu_rho the ORIGINAL positive multiplicity weights under that hypothesis. The signed sinc factors are not discarded. Equation (2) is an identity for the MODIFIED comparison form, not its declaration as an actual source analysis. It follows by applying the linear explicit formula to the averaged smooth compact correlation. No test is presumed null.

The unchanged actual m0 is continuous and m0(0)<0. Choose a NONZERO omega in a small open interval where m0<0, outside the locally finite actual critical ordinate set. For any fixed nonzero delta,

    1-sigma_delta(omega)>0.

Use the existing actual long-gap packets from LOCALIZATION_CEILING_AUDIT:

    h_L(x)=L^(-1/2)eta(x/L)exp(2pi i omega x), ||h_L||_2=1,

with eta smooth compact and normalized. Under RH, their original positive discrete zero sum tends to zero. Since |sigma_delta|<=1, the absolute value of the first sum in (2) tends to zero as well. This uses the same actual quartic divisor summability and Schwartz decay proof; multiplicity copies retain their weights.

The continuous term in (2) tends to

    m0(omega)[1-sigma_delta(omega)]<0.                     (3)

Fourier rescaling concentrates their mass at omega. Dominated convergence is justified by the logarithmic envelope and the Schwartz density of eta. Thus even in the globally positive ORIGINAL RH case, Q_halo has negative physical vectors at sufficiently large supports.

This is a conditional actual-source control, not an assumption of RH as an unconditional theorem. Its implication for the proposed CLOSURE ROUTE is decisive: if fixed-width halo lower bounds and their sign transfers succeeded at every aperture, the original form would be globally positive and hence RH by the standing Weil criterion. Under that consequence, (3) contradicts the asserted halo positivity. The conjunction of those proposed premises is therefore impossible. Halo positivity by itself is not claimed to imply RH.

## 3. What remains lawful and what is stopped

At a FIXED aperture, the full-halo error budget uses S_(a+delta/2), not S_a, because the extra prime powers were added. On bounded-level original eigenvectors its physical error is at most

    S_(a+delta/2)[(32/3)delta+2L_(a,M,k)²(2/log(1/delta))^(2k)]
       +(alpha_delta-1)4a exp(a).

The original eigenvector moments use the ORIGINAL equation and original dictionary. The last term retains the changed signed pole explicitly. This follows from NF57/NF58 and the physical pole bound; it does not prove a halo lower bound or assign a modified source dictionary.

The fixed-width prime-only, frozen pole-matched, and halo pole-matched variants are now stopped as global positivity candidates. We will not extend their generic moment or approximation machinery as the default continuation. Widths chosen separately at each aperture are not excluded, but this audit supplies no independent arithmetic sign estimate for them.

The original source-gain target from NF55 remains the missing theorem. A future advance must estimate that actual full-range gain or prove a genuinely independent arithmetic relation that controls it. Neither matching the prime main term nor preserving a generic operator domain supplies that relation.

## Validation and standing

The companion finite controls check shifted support past the cutoff, strict edge-loss signs, restoring the omitted halo term, and a low-gap signed-continuous control. They do not certify the PNT limit, RH, the literal formula, or a numerical negative aperture. Those arguments are analytic and unformalized in Lean.

The shared prime-8/a=1.05 audit, existing aperture-one certificate and all original source/pole custody are preserved. No original negative vector, improved positivity interval, actual gain upper bound, global exclusion, F4 or full transport is claimed.
