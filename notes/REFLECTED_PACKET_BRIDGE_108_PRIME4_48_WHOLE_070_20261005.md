# RPB108: whole-domain positivity after prime-4 activation

Base: 71b325d0ebd41575d15cce71132003f37c43af22.
Definitions: docs/TERMINOLOGY_RPB108_PRIME4_48_WHOLE_070.md.

## Result

On the entire actual canonical supported logarithmic form domain at a=7/10,

Q(h)>=(1/524288000000000)||h||_2^2.

The 48-coordinate projection still suffices. Prime power 4 and the changed prime-2 adjacency are included in the actual matrix, sources and matching complement. This excludes fixed-aperture weak null modes and establishes corresponding full-source WD-T10 unit domination. Global endpoint exclusion and F4 remain open.

## Actual prime threshold and native matrix

Rational intervals certify log(4)<2a=7/5<log(5). Thus prime powers 2, 3 and 4 are active. The actual coefficient is Lambda(4)=log(2), not log(4). The native prime contribution for 4 is -2Lambda(4)/sqrt(4) times its physical correlation. The full matrix is freshly evaluated at this aperture with both pole terms and physical normalization sqrt((2n+1)/(2a)).

Here L=4a=14/5. Rational bounds log(16)<L<log(17) prove exp(L)<17 and exp(-L)<1/16. Hence L/(1-exp(-L))<(14/5)/(15/16)=224/75<3. Monotonicity of z/(1-exp(-z)) supplies kernel multiplier 3 throughout [0,L]. Native exponential order 160, 120 Bernoulli pairs, gamma order 12 and outward grid 10^-200 are retained. The new aperture is enabled only for degree 47. All 48 native and shifted pivots pass with raw physical margin 1/4194304000000; exact reflection parity and the negative diagonal control pass.

## Seven actual source panels

The normalized source constructor keeps the exact endpoint logarithm, both regular-difference terms, both pole moments and all actual prime translations. Its exact panels are:

| t interval | Active source translations |
| --- | --- |
| (0,1-ell_4) | +2,+3,+4 |
| (1-ell_4,1-ell_3) | +2,+3 |
| (1-ell_3,ell_2) | +2 |
| (ell_2,1-ell_2) | +2,-2 |
| (1-ell_2,ell_3) | -2 |
| (ell_3,ell_4) | -2,-3 |
| (ell_4,1) | -2,-3,-4 |

The central overlap is required because ell_2<1/2 after this threshold. Panel endpoints are exact logarithmic expressions; endpoint values do not affect the L2 source map. The source coefficient for either prime-4 translation is -log(2)/2. Panel-order and activation controls pass.

Source exponential order remains 60; Bernoulli pairs increase to 44 at this new aperture. The kernel remainder is 4(d/3)^90/[1-(d/3)^2]. The source exponential remainder coefficient 3/2 remains half the kernel bound. The pole exponent is (d/2)(t-1/2), whose absolute argument is at most d/4=7/20<log(2); this proves the existing Taylor remainder multiplier 2 directly even though d/2 now exceeds log(2). Older aperture guards and arithmetic are retained. Gamma order is 20; all midpoint polynomial rounding at grid 10^-40 is included in the source error. The actual source-map error is below 1.166e-26. All 7152 regular-factor identities for j=0..47 and k=0..148 agree with the original binomial sums.

On the normalized constant coordinate, omitting prime 4 changes the native/source pairing by log(2)(1-log(4)/d)>0.0067857. Using log(4)/2 instead of log(2)/2 produces the same excess magnitude. Both exceed twice the certified constant-row source error and are rejected by the independent coefficient controls.

## Joint prime-2/prime-4 complement bound

Let s=log(2), A2=log(2)/sqrt(2), A4=log(2)/2. Since 2s<2a<3s, the longest supported translation fibres have three points. On each such fibre A2 C_s+A4 C_2s is the weighted matrix

[[0,A2,A4],[A2,0,A2],[A4,A2,0]].

Its antisymmetric eigenvalue is -A4; its symmetric eigenvalues solve lambda^2-A4 lambda-2A2^2=0. The largest eigenvalue and operator norm are J24=(A4+sqrt(A4^2+8A2^2))/2, below 0.887767. On two-point fibres the norm is A2<J24; one-point fibres contribute zero. Below prime-4 activation, C_2s vanishes and the same J24 remains a conservative bound. Thus this is uniform for a in [1/2,7/10]. Prime 3 separately has compressed norm at most one because a<log(3), giving total prime loss A=J24+log(3)/sqrt(3). Bounding the two related prime powers jointly avoids the larger separate-norm penalty; neither term is omitted.

For k=48 and physical cutoff T=8, the existing integrated-Bessel mass bound is

rho=4a T[2a(22/7)T]^96/[(97!!)^2(1-q)], q=[2a(22/7)T]^2/(97*99)<1.

The pole loss is p=16a(a/2)^96/(48!)^2. Both majorants increase with a on this range. Using the pure archimedean floor -10 and high-frequency bound c=log(T)-1/(2T), independently proved in notes/REFLECTED_PACKET_BRIDGE_108_PRIME3_48_WHOLE_064_20261005.md, the actual physical bracket c-(10+c)rho-p-A exceeds 0.4829084523>12/25.

At independent logarithmic cutoff 7, the rational inequality (9/10)log(7)-(4/5)/7-A>0 supplies the high-band lower bound w/10, with w=log(e+|xi|). On the low band w<3, so the logarithmic bracket 1/10-(10+A+3/10)rho_log-p exceeds 0.09999997299>9/100. Physical inverse factor 25/12 and logarithmic coercivity therefore provide the lawful matching complement lift.

## Full Gram, corrected sign and whole-domain assembly

All 2304 native/source pairings pass, with maximum discrepancy below 1.527e-35. The full residual Gram projects away exactly degrees 0..47 and retains every log/log, smooth/smooth, log/smooth and mixed projection term on all seven panels. Its maximum entry width is below 8.869e-108. The actual Gram operator error delta=eta(2M+eta) is below 7.747e-26. Native/source hashes are recorded.

All 48 rational interval pivots of

Q_48-(25/12)Rhat_48-[(25/12)delta+1/5242880000000]I

are positive. Thus the actual lawful corrected form has lower margin tau=1/5242880000000. Its negative diagonal control is rejected. The lift squared norm is below 47.918<49, so use physical lift norm at most 7. For h=e+u, e in E_48 and u in the lawful complement,

Q(h)>=tau||e||_2^2+(12/25)||u+lift(e)||_2^2,
||h||_2^2<=2(1+7^2)||e||_2^2+2||u+lift(e)||_2^2.

Consequently Q(h)>=min(tau/100,6/25)||h||_2^2=(1/524288000000000)||h||_2^2. No physical spectral operator-domain membership is assumed.

## Validation and scope

The native matrix, rounded sources, complement, full Gram/whole-domain certificate and activation/coefficient controls reproduce byte-for-byte. Previous a=69/100 native matrix and sources reproduce unchanged under the narrow constructor extensions. All 7152 regular factors, source panels, pairings, input hashes, constructor guards, native/corrected negative diagonal controls and prime-4 omission/doubled-coefficient controls pass. No floating quantity enters a sign decision.

Next: larger apertures with their actual prime terms, source panels and matching complement, or independent global endpoint exclusion. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI standing are unchanged. These analytic/rational certificates are not Lean formalized.
