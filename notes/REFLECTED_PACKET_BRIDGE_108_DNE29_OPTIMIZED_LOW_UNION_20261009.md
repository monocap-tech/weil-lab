# RPB108 — DNE29: certify the missing low border of the optimized NF38 lifts

Read [DNE29 terminology](../docs/TERMINOLOGY_RPB108_DNE29_OPTIMIZED_LOW_UNION.md) before the definitions below.
Parent DNE28: 7e31f02323e7cb314bddfae03bfbe0b3829f8345.
Read-only Phase NF41: 4d2a5d7d3857854677a223ca38d03b13358f40e9.
Read-only Coupled CC79: dd93e5cc7d003d44cdc240c5710f4c253dc1346f.
Only research/rpb108-direct-null-exclusion is written.

## Result

DNE26 certified NF38's selected three-column packet at the original high floor kappa=11/25, but left its low-mode union untested. DNE29 closes that specific missing border with six fresh original signed native pairings. Both complete four-column frames pass with all original infinite high vectors included.

| Paid quantity | Even | Odd |
| --- | ---: | ---: |
| Frozen source Young parameter tau | 66/125 = 0.528 | 211/500 = 0.422 |
| Credit on DNE23's frame, paid in DNE28 | 0.032 | 0.082 |
| Credit c on optimized T4 | 11/100 = 0.11 | 7/50 = 0.14 |
| Credit ratio between these frames | 3.4375 | >1.7073 |
| Scaled physical coarse diagonal ell | (0.001,0.25,0.1,0.5) | (0.01,0.12,0.2,0.02) |
| Full-high physical gap, strict lower | >2.49999e-35 | >1.19999e-31 |

The same retained restriction Z8+F112 now has the common guard

    Q(h)>=2.4*10^-35 ||h||^2.

This improves DNE28's common guard 1.9*10^-35. The retained span is unchanged: eight directions remain jointly certified, with 104 outside their span. The larger source credits apply to the optimized polynomial frame and its corresponding native energy orthogonal remainder. They are not simply assigned to DNE28's old remainder coordinates.

## Exact frozen polynomial reconstruction

NF41 records the full coefficients of NF38's frozen joined base columns B. The imported excerpts preserve those indices and coefficients exactly; custody records their source paths, pinned Phase commit and complete source-file hashes.

For each parity, reconstruct

    T3_i=B_i-z0 C_(0,i)-z1 C_(1,i)

using the selected joint rational functionals and the two exact high corrections in the authenticated NF38 packet/trial. Merged coefficients remain rational. The base witness polynomial exactly matches NF38's authenticated merged trial polynomial. Independent validation checks every selected coefficient against the same exact formula and verifies all retained coefficients against the original NF24 seed, NF27 response and NF32 probe records.

The two corrections are physically orthogonal and supported in F112. The same retained components therefore still span Z8. The selected columns have degree at most 180 even and 179 odd. All complete selected polynomials and exact physical masses are preserved in deterministic gzip/base64 imports, with decoded hashes paid by the consumers.

## Six fresh original low-energy pairings

The old low row cannot be reused after changing high lifts. Reconstruct the original source of e0 or e1 using the frozen DNE16/DNE23 source engine. The only change to its prefix is extending available normalized Legendre bases from degrees below 116 to degrees below 181. The original source formula is unchanged.

The complete action includes the singular harmonic polynomial, regular archimedean convolution, exact endpoint logarithms, all six prime powers {2,3,4,5,7,8} in both translation orientations and the correctly signed pole. Seven positive half-interval panels account for all thirteen original translation cells by reflection parity. No quadrature, sampled transform or discarded endpoint strip is used.

Pair this original low source with each complete optimized selected polynomial. The exact polynomial/log moment integration gives the native row, with source operator error

    eta_N=2a*(550/19)*(106/125)^N+3*10^-99

multiplied by the outward norm of that selected column. The primary uses N=360 and 600 directed Decimal digits; the replay uses N=400 and 620 digits. All six pairings agree within their paid intervals.

| Fresh native low pairing, approximate center | Even | Odd |
| --- | ---: | ---: |
| Seed column | -3.46489e-22 | +1.338067e-18 |
| Response column | -1.580254e-21 | +1.154537e-18 |
| Probe column | +6.517227e-14 | +4.475769e-14 |

These displays are not certificate endpoints; the JSON files retain exact interval endpoints. In particular the changed probe's low pairing is positive and substantially different from DNE23's old probe pairing. Paying it matters in the scaled mixed matrix.

For an independent original symmetry check, reverse the action: reconstruct each full optimized polynomial's original source, including its harmonic polynomial and translated prime action, and pair with e0/e1. The reverse runs use N=400 and 620 digits. Their six original intervals overlap the primary and replay low-source intervals. Every run also reconstructs the original low diagonal and checks overlap with CC62. The smooth source error is paid in both orientations.

## Complete optimized four-column source comparison

The optimized Q3 and Gamma3 are NF38's already certified complete selected native and projected source matrices. Their expensive full source Gram producers are not rerun. The six new pairings supply the missing native row of Q4; CC62 supplies its low diagonal and complete low source-square bound P0.

DNE28's coherent source Young argument applies to these actual selected columns:

    Gamma4<=D_tau=diag((1+1/tau)P0,(1+tau)Gamma3).

This pays all three uncomputed low-source Gram crosses together. It does not claim those crosses vanish. The signed low native row and complete signed three-column source/native blocks enter the matrix test

    S[(kappa-c)Q4-D_tau]S>0.

The rational choices in the result table pass all four outward interval LDL pivots in each parity. Thus Gamma4<(kappa-c)Q4 is a fully paid four-column source contraction for this optimized frame. It is not DNE26's three-column credit spliced with an independent low-mode certificate.

A separate native comparison pays S Q4 S>q I, with q=1/25 even and 7/50 odd. A separate physical comparison pays

    S[Q4-D_tau/kappa]S>diag(ell).

Their four outward pivots are also strictly positive. Candidate tau, c and ell values were selected using midpoint diagnostics and frozen before exact verification. Neither maximal credits nor optimal high corrections are claimed.

## Physical mass and infinite high completion

Compute each selected polynomial's physical norm from its exact rational normalized Legendre coefficient mass, rather than a triangle estimate over its separate corrections. Outward roots at 160 digits in the primary and 200 digits in the replay bound these norms.

For each optimized finite column i, its inverse-completed physical norm is bounded by

    b_i<=norm(T4_i)+sqrt(Gamma4_(i,i))/kappa.

The low-column bound is inherited from DNE28; the other source diagonal bounds come from the complete NF38 selected source Gram. With C>=kappa I and the paid physical diagonal ell, square completion and weighted Cauchy yield

    physical_gap >= [sum_i (s_i b_i)^2/ell_i+1/kappa]^-1.

This gives the displayed bounds and the common 2.4*10^-35 guard. Both parity bounds exceed DNE28's corresponding bounds. The higher precision replay is no weaker. The nonorthogonal frame mass and every original high vector are included. The actual infinite inverse is not evaluated.

## Remaining-frame interface

DNE25's complete source transport criterion can now use c=0.11 even and c=0.14 odd after defining the optimized remainder

    Y=W-T4 Q4^-1 Q(T4,W).

The strict complete test c B_Y-Gamma_Y>0 would suffice for whole 1.06 positivity. Alternatively a frozen rational approximation can pay r+kappa epsilon<c with its original native border errors. These are conditional criteria. The optimized energy orthogonalization, remaining native border and complete remaining source Gram are still uncomputed. Historical DNE23/DNE28 frame results remain valid separately.

DNE24's exact null reduction and 52-per-parity remaining dimension bounds are unchanged because the retained span and eliminated subspace Z8+F112 are unchanged. No new retained direction or whole-aperture positivity claim is made.

## Verification and custody

Primary and replay matrix consumers use outward rational interval grids of 80 and 100 digits, respectively, and each pass 41 explicitly counted certificate assertions, with additional interval overlap, root and division guards. They use different freshly integrated low rows and different outward mass-root precisions. Source replay boxes lie inside the primary boxes; credits and physical diagonals are identical.

The independent validator imports no producer code. It reconstructs the exact selected coefficients, checks the original retained components, verifies source-error payments and forward/replay/reverse symmetry overlaps, independently rebuilds signed matrix boxes and tests every symmetric box vertex. The six four-by-four boxes each have 1024 vertices, and every vertex has four positive exact leading determinants. Convexity pays all interior matrices without an independence assumption on their errors.

Validation passes 26,508 rational checks, including 24,576 vertex leading-minor checks and 486 nonorthogonal physical completion controls. Three genuine positive/null/negative full-block crossings and three whole-physical-mass positive-level controls pass. These abstract controls are not original Weil countermodels. Syntax checks pass. Encoded imports reproduce exact selected-column bytes and the primary consumer output.

The source engine and all inherited packet inputs are pinned by SHA256. Imported NF41 coefficient excerpts are verified against the original Phase files. No actual inverse reaction, complete 104-dimensional source Gram, whole 1.06 positivity, all-aperture transport, RH/F4 or Lean closure is claimed. This is outward computational certification combined with inherited original-source, high-floor and closed-form arguments.

Phase remains NF41 and Coupled remains CC79 at the pinned read heads. The optimized polynomial coefficients are imported as data; NF41's abstract inverse-coupling model is not used as an actual Weil response estimate. Both source branches remain read only. Earlier documents are preserved additively.

## Reproduction

The repository validation manifest lists the exact inherited/imported input paths. From the repository root, the consumer can be invoked from Python as follows:

```python
import sys, json
sys.path.insert(0, 'scripts')
from pathlib import Path
from certify_dne29_optimized_low_union import run
m=json.loads(Path('notes/data/RPB108_DNE29_VALIDATION_MANIFEST_20261009.json').read_text())
primary=run(m['consumer_inputs'],80,160,False)
Path('/tmp/dne29.json').write_text(json.dumps(primary,indent=2)+'\n')
replay_inputs=m['consumer_inputs'][:8]+m['extra_inputs'][6:8]
replay=run(replay_inputs,100,200,True)
Path('/tmp/dne29_replay.json').write_text(json.dumps(replay,indent=2)+'\n')
```

Then run the independent validator with that manifest, primary, replay and an output path. The original low-row producer accepts parity, the DNE15 encoded target archive, the DNE29 encoded selected columns, CC62 low input, scripts/dne23_dne16_source_input.py and --output. Replay with DNE16_PRECISION=620 DNE16_ORDER=400; add --reverse for the independent selected-source action. Custody preserves all artifact and decoded import hashes.
