# RPB108 NF24 — Compensated original sources and exact remaining projections

Date: 2026-10-09 UTC. Independent Phase Geometry branch
`research/rpb108-phase-geometry-localization`. Recovered NF23 parent
`612dd2696f8f9b423d1c898aaeda2b046fd93af0`. Coupled, DNE and paused
branches receive no writes. Definitions are registered in the additive
[NF24 terminology](../docs/TERMINOLOGY_RPB108_COMPENSATED_SOURCE_TARGET_NF24.md).

**New certified results:** NF18's two exact rational near-critical vectors
are authenticated and compensated against the original measured H2 block.
Their finite energies remain strictly positive. NF22's regular-kernel
error extends to every supported polynomial without a degree multiplier.
Two new complete original native source projections prove that the
compensated physical residuals remain strictly nonzero.

**Not certified:** the complete residual source squares, failure or success
of the directional scalar-floor test, the full residual Gram, the true
high inverse response, or whole-domain positivity at 1.06.

## 1. Exact custody and explicit compensated source targets

The NF17 full E112, NF18 first exterior, NF19 second exterior and NF18
rational witness artifacts were retrieved and authenticated against the
immutable SHA256 values in their repository manifests:

- E112: `f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81`.
- First exterior: `da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee`.
- Second exterior: `0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad`.
- NF18 rational witnesses: `b3e23133db4562c1b28816e922f9c085899818399dcfcee74a323b4f6da10d5c`.

For either retained rational vector x, let t=Q(x,H2), C2=Q(H2,H2).
Enclose -C2^-1 t using all original native channels. Freeze a rational
coefficient vector lambda with denominator 10^80 inside the neighborhood
of this exact minimizer, and define p=x+lambda.H2. This creates an explicit
reproducible target; it is not asserted to be the exact minimizer.

| Certified finite quantity (approximate displays) | Even p | Odd p |
| --- | ---: | ---: |
| H2 degrees | 112,114 | 113,115 |
| Frozen lambda first | +3.6210589043e-19 | -4.4366024662e-17 |
| Frozen lambda second | -2.0723257978e-19 | +2.9802961418e-17 |
| Q(p,p), strictly positive | 9.25563570359728e-35 | 3.30701999543587e-31 |
| Removed fraction of NF18 old energy | 0.00547158443858 | 0.02504673001089 |
| Complete low source projection square | 1.57182825899193e-37 | 2.44998102299820e-33 |
| Measured H2 source projection square | <1e-150 | <1e-150 |

The complete 56 low source coordinates and the two measured high source
coordinates are enclosed with exact rational arithmetic on a 10^-180
grid. ||p||²<1001/1000 is also certified. The tiny H2 pairings are retained;
they are not replaced by exact zero. The exact T/P2 identity for the true
minimizer remains NF21's identity, not a silently altered identity for p.

## 2. Degree-independent arch source error — a new uniform lift

For a supported polynomial p, the original arch source can be written

\[
L_{arch}p(x)=c p(x)-\tfrac12p(x)\log(a^2-x^2)
 +S_p(x)-\int_{-a}^{a}r(|x-y|)p(y)\,dy,
\]

where c=-gamma-log(2pi) and

\[
S_p(x)=\tfrac12\int_{-a}^{a}
\frac{p(x)-p(y)}{|x-y|}\,dy.
\]

For a monomial x^m, this removable-singularity integral is exactly

\[
S_{x^m}(x)=H_m x^m
 -\sum_{\substack{1\le j<m\\j\;odd}}
 \frac{a^{j+1}}{j+1}x^{m-1-j}.
\]

The formula follows by factoring p(x)-p(y) on the two sides of x.
The regular inside-support p(x) term cancels the regular boundary primitive
term. Consequently, after replacing r by NF22's rational r_N,

\[
(L_{arch}-L_{arch,N})p(x)
=-\int_{-a}^{a}(r-r_N)(|x-y|)p(y)\,dy.
\]

Cauchy-Schwarz in y and integration in x, or the integral Schur test,
therefore gives the uniform physical operator ERROR bound

\[
\boxed{\|(L_{arch}-L_{arch,320})p\|_2
 \le 2a\epsilon\|p\|_2,
\qquad
2a\epsilon<7\times10^{-22}.}
\]

Here epsilon=4(106/125)^320/(1-106/125), inherited from NF22's complex
Cauchy certificate. The exact coefficient is approximately
6.811221229467675e-22. No derivative norm or polynomial-degree factor
occurs. The singular logarithm remains exact; this asserts boundedness
of the approximation ERROR, not boundedness of the original arch operator.

For the frozen p, the paid arch L2 error is at most
(1001/1000)*2a*epsilon. Orthogonal residual projection does not increase it.
If the reconstructed residual source square is below the following
conservative rational budgets, its true square is below kappa Q(p,p),
with kappa=207/1000:

| Sufficient approximant-square budget (approximate display) | Even | Odd |
| --- | ---: | ---: |
| (sqrt(kappa*energy_lower)-source_error)^2 | 1.91531977041784e-35 | 6.84549571324431e-32 |
| Arch error / threshold L2 norm, upper | 0.000155766 | 0.000002606 |

The exact budgets are in the target ledger. The reconstruction error
uses less than 0.1% of either squared sufficient threshold. The missing
issue is therefore the actual residual source size, rather than inability
to reconstruct a high-degree source accurately enough.

## 3. New original native residual projections — rigorous lower bounds

Compute 116 new full original native pairings against e117 and e118,
including all arch, six-prime/both-orientation and signed-pole channels.
The rational kernel-moment arithmetic retains N=720, K=620 and grid
10^-280. These are source coordinates against normalized physical high
modes, not an enlargement of the positivity certificate.

The pole first moments use an independent exact positive-series formula
derived from Rodrigues' formula and integration by parts:

\[
\int_{-a}^{a}e^{x/2}P_n(x/a)dx
=2a\sum_{k\ge0}\frac{(a/2)^{n+2k}}
 {2^k k!\,(2n+2k+1)!!}.
\]

Terms through k=80 are retained and the remaining positive tail is bounded
by twice the next term; subsequent ratios are below 1/2. Six independent
old diagonal pole intervals (degrees 0,1,10,11,110,111) overlap the new
series enclosures. Original signed pole conventions are unchanged.

For r_p=P_F112 L_a p, physical Bessel gives
|Q(p,e_j)|² <= ||r_p||². Exact interval evaluation of the frozen targets
proves

\[
\boxed{\|r_{p_e}\|_2^2>2.6325\times10^{-36}
 >0.0284\,Q(p_e,p_e),}
\]

\[
\boxed{\|r_{p_o}\|_2^2>9.8878\times10^{-33}
 >0.0298\,Q(p_o,p_o).}
\]

The observed coordinates are approximately +1.62250872406683e-18 on
e118 and +9.94375426729619e-17 on e117. Strict measured square/energy
brackets are (0.0284,0.0285) even and (0.0298,0.0300) odd.
This certifies a genuine residual after H2 compensation. Each lower bound
is below 0.207, so neither alone rejects the coarse sufficient gate.

## 4. Independent complete residual diagnostics — NOT certificates

A 90-digit Decimal computation evaluates the original regular kernel
directly, the exact singular polynomial, endpoint logarithms, all original
prime cells and signed poles. It subtracts all low source coordinates
before squaring. Gaussian integration uses two independent order pairs:

| Numerical residual-square / Q(p,p) | Inner96 / outer64 | Inner128 / outer96 |
| --- | ---: | ---: |
| Even | 0.3500748152404 | 0.3500748152399 |
| Odd | 0.2802820445030 | 0.2802820445025 |

These exceed the coarse kappa=0.207 threshold by factors about1.691 and
1.354. Numerical Pythagoras (full source square minus residual square)
agrees with the exact low projection ledger to relative discrepancies
below 1.6e-13 at the larger order. The two certified new source coordinates
also agree with separately integrated high projections.

No rigorous quadrature remainder is established here. The apparent failure
of the coarse residual source-square gate is **not** promoted to a theorem.
Even a rigorous failure would reject only that scalar sufficient estimator,
not the genuine C^-1 response, a whole-domain sign, or RH.

## 5. Reproduction, interface and next frontier

- [Authenticated target/energy/error producer](../scripts/certify_native_compensated_witness_nf24_106.py).
- [New native projection producer](../scripts/build_native_residual_projection_nf24_106.py).
- [Exact projection/Bessel validator](../scripts/validate_native_residual_projection_nf24_106.py).
- [Non-certifying complete source diagnostic](../scripts/diagnose_native_compensated_source_nf24_106.py).
- [Exact target and coordinate ledger](data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json).
- [Deterministic compressed/base64 full native projection source](data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64).
- [Certificate and separately labeled numerical diagnostics](data/RPB108_NF24_COMPENSATED_SOURCE_CERTIFICATE_20261009.json).

Target producer, fresh native source producer and exact validator all ran
locally and passed; native source bytes are deterministic and hash-checked
in the certificate. Original input artifacts are unchanged. The validator
accepts either raw JSON or the published .json.gz.b64 source. No Lean or
GitHub Actions run is claimed.

**NF25:** rigorously enclose the compensated directional residual norms or
produce a sufficient weighted/correlated high-response bound. The degree-free
error lift makes the source reconstruction precision adequate. If an exact
residual lower bound confirms the numerical scalar-floor obstruction,
record that scoped rejection and pursue source-aligned response, including
CC59's read-only sharper correlated interface. Do not build the full physical
P2 matrix on the unsupported assumption that its coarse sign must pass.

Highest internally certified whole aperture remains 1.05. Whole 1.06,
full source/residual Gram, true infinite inverse, RH, F4, transport and
Lean closure remain open.
