# RPB108 — NF29: complete sources after a two-high retained response lift

2026-10-09 UTC. Aperture a=53/50. Phase Geometry parent is NF28,
`1b227864aa6398e59922fde470f371fb9b72dc11`. Coupled CC71 was read
without modification at `ae03e419ef9b975ee219806873c755b4d3149982`.
No integration or paused branch is modified.

Read the additive [NF29 definitions](../docs/TERMINOLOGY_RPB108_LIFTED_RESPONSE_NF29.md).

## Result

The complete fixed-lift source Gram is certified in both parities. The
odd two-direction coarse matrix passes; the even matrix remains
rigorously indefinite.

| Strict certified quantity | Even | Odd |
| --- | ---: | ---: |
| Unlifted NF28 residual square / native energy | (0.69827, 0.69829) | (0.80553, 0.80554) |
| Lifted residual square / native energy | (0.42957950, 0.42957952) | (0.19819722, 0.19819723) |
| Coarse high-floor budget | 0.207 | 0.207 |
| Removed native energy fraction | about 9.18% | about 20.56% |
| Lifted-response sufficient diagonal | $(-4.594600,-4.594599)\times10^{-37}$ | $(9.15055,9.15056)\times10^{-35}$ |
| Full two-direction sufficient determinant | $(-2.09759,-2.06666)\times10^{-72}$ | $(5.95540,5.95600)\times10^{-66}$ |
| Fixed-lift sufficient matrix | rejected | positive definite |

The odd result proves the original retained Schur restriction on
span(x_odd,w_odd) positive, with the entire original high space F
included. The lifting preserves both retained vectors, so this is not
merely finite-domain positivity. The sufficient scalar after eliminating
the response coordinate is greater than 6.5082e-32. This number is a
coordinate Schur lower bound, not a claimed physical whole-domain gap.

The even negative sufficient diagonal is already decisive for this
fixed family. Its native energy remains positive. It does not establish
an actual negative form direction, nor rule out retuning this lift,
using additional high modes, or a sharper inverse-response estimate.

Both selected high coordinates are suppressed below 2.15e-87 even and
2.324e-85 odd. Despite that tiny selected-shell residual, the even
complete source budget still fails. Thus selected-shell suppression
cannot stand in for a complete physical source-square bound.

The frozen high corrections are approximately
(1.0726124e-19,-5.6044381e-20) even and
(-1.1592372e-17,7.2290225e-18) odd. The machine-readable certificate
contains their exact rational values and all outward interval endpoints.

## Construction and scope

NF28 exposed a negative sufficient coarse score on the unlifted exact
NF27 retained response w. NF29 preserves that response's retained
component and adds a selected original high correction. In each parity,
H2 contains the first two high modes: 112/114 even, 113/115 odd.

With C2=Q(H2,H2) and k=Q(H2,w), freeze h using the exact rational
midpoint inverse of C2 and downward rounding to denominator 10^100.
Set w_h=w-h. This is a fixed native-energy-aware trial, not an actual
infinite-high minimizer. Its retained component remains exactly w,
and exactly orthogonal to the authenticated retained seed x.

The native energy Q(w_h,w_h) is obtained from the authenticated complete
original finite116 native entries, not inferred by approximate source
integration. The mixed energy is

\[
Q(v,w_h)=Q(v,w)-Q(v,h).
\]

Q(v,w) inherits NF26's paid retained coordinates, while Q(v,h) is
integrated from the complete reconstructed source and paired against
the tiny physical h. Its uniform source replacement error is paid as
eta_unit times (1001/1000) times ||h||. This avoids using unit-norm
approximate-source energy at the near-critical cancellation scale.

The producer separately reconstructs the complete projected sources
r_v=P_F L v and r_h=P_F L w_h. It integrates their signed 2-by-2 Gram
Gamma_h on the original thirteen cells, with the endpoint logarithm
explicit and all arch/prime/pole cross terms present. The native energy
Gram and complete residual Gram are both verified positive definite.

For the unchanged inherited high floor C>=kappa I, kappa=207/1000,

\[
S_{x,w}\ge U_h=Q((v,w_h),(v,w_h))-\Gamma_h/\kappa.
\]

A negative sufficient score is an estimator rejection on this fixed
lifted family, not an actual negative original Schur direction. The
selected lift does not exhaust all two-high choices, all larger high
corrections, or sharper inverse-response estimates.

## Proof arithmetic

The source uses the NF22 regular N=320 rational construction, NF26's
10^-500 outward rational grid and constant enclosures, exact endpoint
logarithmic moments, and the paid degree-40 pole remainder. Translated
prime polynomials are cached once per orientation and selected on all
thirteen original cells. No quadrature or source sampling is a proof
input. NF26's original v source-square enclosure overlaps the replay.

For each reconstructed residual, eta pays the complete source error
and retained midpoint projection radius. With reconstructed norm
upper bounds N_i, each Gram entry pays

\[
|\Gamma_{ij}-\widehat\Gamma_{ij}|
\le \eta_iN_j+\eta_jN_i+\eta_i\eta_j.
\]

Small measured H2 source coordinates are recorded separately. They do
not by themselves control the complete residual source or omitted modes.

## Independent verification and reproduction

The separate checker compares each lifted source's unsquared high
pairing against the unchanged original N720/K620 signed archive: e118
even and e117 odd, including all retained and H2 coefficients. It also
checks the finite energy by the expanded formula
Q(w,w)-2Q(w,h)+Q(h,h), and checks Q(v,h) by the independent decomposition
Q(p,h)-Q(y,h). The latter uses original native NF24 measured coordinates
for p and pays the much smaller product ||y|| ||h|| eta_unit.
Positive/zero/negative exact rational lift controls check the distinction
between a fixed-lift sufficient energy and the optimized Schur value.
Both original signed projection comparisons, both independently expanded
finite-energy comparisons, both mixed-energy decomposition comparisons,
and the separately rechecked sufficient matrix signs passed. Both proof
scripts also pass Python syntax compilation. The additional exact
rational norm checks and the odd 6.5082e-32 scalar threshold were checked
separately; no whole-domain conclusion is inferred from them.

Place the authenticated original NF24 native archives at the producer's
documented `nf24-inputs/Weil/` paths, then run from the repository root:

```sh
python3 scripts/certify_native_lifted_response_nf29_106.py --output /tmp/nf29.json
python3 scripts/check_native_lifted_response_nf29_106.py /tmp/nf29.json --output /tmp/nf29-validation.json
```

All seven producer inputs are SHA256 authenticated. Frozen rational
lift coefficients, native energies, signed complete source Gram entries,
paid errors and sufficient matrix signs are in the machine-readable
certificate. The independently labeled validation file authenticates
the resulting certificate and records its separate checks.

Whole-domain 53/50 positivity and the complete 55-direction retained
background in either parity remain open. The highest internally
certified whole-domain aperture remains 21/20. RH, F4 and Lean are not
claimed; historical wording and paused fronts remain unchanged.

## Next frontier

NF30 should enlarge the even response correction beyond H2 or sharpen
its high-response estimate, while preserving the newly successful odd
two-direction block. Neither directional success tests the other 54
background directions in its parity. CC71's 55 collective finite lifts
are useful read-only candidates for a complete-source matrix calculation;
their finite positivity does not supply the missing complete Gram.
The true inverse-weighted signed collective couplings and the full
retained Schur sign remain separate open obligations.
