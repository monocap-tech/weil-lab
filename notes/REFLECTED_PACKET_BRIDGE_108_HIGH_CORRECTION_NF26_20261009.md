# RPB108 — NF26: additional high corrections close the fixed directional source test

Date: 2026-10-09 UTC. Aperture a=53/50. Independent Phase Geometry
continues NF25 at `493650e71100c62862b682d0579b2240e8c1d002`.
Coupled was recovered read-only through CC66 at
`795aa8849d07d99c7da880ca201dfda8aa011623`. No Coupled or paused branch
is modified. This tests new Phase trial polynomials; it does not evaluate
or relabel CC65's different frozen trial polynomials.

Read the additive [NF26 definitions](../docs/TERMINOLOGY_RPB108_HIGH_CORRECTION_NF26.md).

## Result and scope

NF26 freezes additional rational high corrections for NF24's two
near-critical retained seeds, reconstructs each complete corrected
physical source, and pays all original-source approximation errors.
The strict directional source test is evaluated using the unchanged
original high floor kappa=207/1000.

| Certified quantity | Even | Odd |
| --- | ---: | ---: |
| Complete residual square / (kappa corrected energy) | **(0.9612, 0.9619)** | **(0.7612, 0.7613)** |
| Original directional Schur value, strict lower bound | $>3.32\times10^{-36}$ | $>7.56\times10^{-32}$ |

The corresponding strict original energy and source-square brackets are:

| Physical quantity | Even | Odd |
| --- | ---: | ---: |
| Q(v,v) | $(8.7267,8.7271)\times10^{-35}$ | $(3.16796,3.16798)\times10^{-31}$ |
| Complete residual square | $(1.7364,1.7377)\times10^{-35}$ | $(4.9918,4.9920)\times10^{-32}$ |

Both upper ratios are strictly below one after physical error payment.
Both original retained directions therefore pass. Exact reflection parity
makes their mixed Schur term zero, certifying their two-dimensional
Schur restriction.

The original retained direction x is unchanged. A positive score certifies
its original Schur value, including the true infinite high response.
It does not compute that inverse response or certify the collective
retained Schur matrix. Couplings to the other retained directions remain
outside this certificate.

NF25's failure was scoped to the original target and the two measured
high sources. NF26 supplies additional original source information by
using many more high modes in a single fixed polynomial correction.

## 1. Frozen trial polynomials

Let p be the unchanged authenticated NF24 compensated target. Its retained
component is x, and its high component lies in the original measured H2.
Set v=p-y, where y is frozen before proof evaluation with rational
coefficient denominator 10^80.

- Even: 33 modes e116,e118,...,e180.
- Odd: 32 modes e117,e119,...,e179.

For each mode the selected coefficient is the downward rational rounding
of one quarter of NF24's diagnostic projection of Lp onto that mode.
Those noncertifying diagnostic values serve only to choose y. The exact
coefficients in the [trial ledger](data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json)
are the proof inputs; no numerical quadrature enclosure is assumed.
No coefficient of the retained x or of NF24's H2 compensation is changed.

The correction norm is at most approximately 1.037e-18 even and 5.395e-17
odd. The very small size is appropriate to the near-critical energy scale;
all energy and source errors are compared against that scale explicitly.
No omitted high-mode coordinate is discarded from the final source norm.

## 2. The original directional Schur argument

Let F=E112-perp and C be the original closed coercive high form on F.
The established original bound C>=kappa I implies inverse-form order,
as used in [CC59](https://github.com/monocap-tech/weil-lab/blob/795aa8849d07d99c7da880ca201dfda8aa011623/notes/REFLECTED_PACKET_BRIDGE_108_CORRELATED_HIGH_FLOOR_CC59_20261009.md).
For the corrected polynomial v, let r_v=P_F L_a v. Completing the square
in the original high form gives the Schur value on the retained x:

\[
S(x)=Q(v,v)-\langle r_v,C^{-1}r_v\rangle
\ge Q(v,v)-\frac{\|r_v\|_2^2}{\kappa}.
\]

The left side is independent of the chosen finite high correction.
Every object uses the original signed Weil form. The right side is the
certified sufficient score, not an approximation to the full inverse.
For opposite-parity retained seeds, the mixed Schur term is exactly zero
by reflection symmetry. Successful directional scores therefore certify
their two-dimensional Schur restriction; this is still smaller than the
complete retained space.

## 3. Energy at the original cancellation scale

The authenticated NF24 q=Q(p,p) is inherited unchanged. It is NOT inferred
by pairing an approximate unit-norm source with p. Instead compute

\[
Q(v,v)=q-2Q(p,y)+Q(y,y).
\]

The complete approximate sources of p and y are integrated against y.
Their approximation errors in these pairings are bounded by
eta_unit (1001/1000)||y|| and eta_unit ||y||^2 respectively. The small
norm of y makes these errors negligible at the native energy scale.
The transpose pairing Q(y,p) is independently computed and overlaps the
paid Q(p,y) enclosure, checking original bilinear symmetry across all
source sectors and cells.

## 4. Complete source reconstruction and paid projection

The producer applies the same exact endpoint decomposition as NF22/NF25
to arbitrary polynomial inputs:

\[
L_{arch}f=c f-\tfrac12 f\log(a^2-x^2)+S_f
-\int_{-a}^a r(|x-y|)f(y)\,dy.
\]

Only the regular kernel is replaced by the N=320 rational construction.
Both endpoint logarithms and their squared moments remain explicit.
All six prime powers 2,3,4,5,7,8, both orientations, signed poles and all
cross terms are integrated over the original thirteen translation cells.
Exact polynomial, log and log-square moments are used, with algebraic
continuous endpoint limits. No quadrature error or sampling maximum
enters the proof.

The runtime outward rational grid is strengthened to 10^-500 for the
higher polynomial degrees. Rational atanh series use 800 terms with paid
remainders. Machin arctangents use 350 terms. The Euler-gamma enclosure
uses the harmonic formula at m=400, Bernoulli corrections through B400,
and the next B402 remainder. These changes affect arithmetic precision
and constant enclosures; historical producer files remain unchanged.

Let

\[
\epsilon=4(106/125)^{320}/(1-106/125),\quad
R40=2(a/2)^{41}/41!,\quad
\eta_{unit}=2a\epsilon+8R40.
\]

NF24's degree-independent error theorem controls the regular arch source.
The degree-40 pole exponentials have error factor 4a exp(a/2)<8. A
positive-series bound proves exp(a/2)<7/4 and 7a<8. The positive Rodrigues
first-moment series and its entire remaining tail are enclosed directly.

The retained projection of Lp uses the authenticated native coordinate
midpoints, paying its physical coordinate radius delta_p. The retained
projection of the approximate Ly is computed by exact moments; its fixed
rational midpoint rounding costs delta_y. Orthogonal projection contracts
the Ly source error. Therefore, with m_p=1001/1000 and m_y>=||y||,

\[
\|r_v-\widehat r_v\|_2\le
\eta=m_p\eta_{unit}+\delta_p+m_y\eta_{unit}+\delta_y.
\]

The full original source-square upper bound is
(sqrt(approximant_square_upper)+eta)^2. The lower bound uses the analogous
nonnegative lower square root minus eta. All roots are enclosed by exact
integer square-root arithmetic. The certificate retains the complete
rational moment source-square enclosure, both mixed energy enclosures, the original corrected
energy, all 56 retained correction coordinates per parity, and the
physical error payment.

## 5. Replay and publication artifacts

A complete first run is followed by a strengthened replay. All common
energy and source-square intervals agree exactly. Six independent
unsquared source pairings overlap original native intervals after paid
errors: p against its two H2 modes and against NF24's independently
produced e118 even/e117 odd projection. Both transpose energy checks pass.
The retained target and NF24 projection-certificate bytes are SHA-256
authenticated before proof evaluation.

- [Complete rational producer](../scripts/certify_native_high_correction_nf26_106.py).
- [Frozen high corrections](data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json).
- [Paid original energy and complete residual certificate](data/RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json).
- [Replay, strict decimal brackets and file custody](data/RPB108_NF26_HIGH_CORRECTION_VALIDATION_20261009.json).

Existing NF17, NF22 and NF25 helper scripts are unchanged. Reproduce from
the repository alone:

```bash
python scripts/certify_native_high_correction_nf26_106.py \
  notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json \
  notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json \
  notes/data/RPB108_NF24_COMPENSATED_SOURCE_CERTIFICATE_20261009.json \
  --output certificate.json
```

The diagnostic file used to select coefficients is unnecessary for replay:
all selected rational coefficients are already frozen and published.

## 6. NF27 frontier and claim boundary

The next task is collective assembly: control the original Schur couplings
between these near-critical retained directions and the remaining retained
space, with a justified stable retained complement and every residual
source contribution paid. Directional success does not automatically
control those mixed terms. A source-aware retained decomposition can
reduce the remaining work, but must preserve the original form and mass.

The full collective residual Gram and whole-domain sign at 1.06 remain
open. The highest internally certified whole-domain aperture remains
1.05. RH, F4, cap-uniform leakage, global null exclusion and Lean closure
are not claimed. Coupled's CC66 estimator controls remain intact and
read-only; paused fronts are not restarted.
