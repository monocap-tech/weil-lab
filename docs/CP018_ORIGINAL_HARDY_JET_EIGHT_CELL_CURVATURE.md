# Weil-Lab — CP018
## Original Hardy-`Z` analytic derivative jets and an exact eight-cell curvature certificate interface

**Track:** independent CP### cross-projection investigation, stacked on CP017 PR #838 → CP016 #837 → CP015 #836 → CP014 #831 → CP013 #829 → CP012 #827 → CP011 #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. The original IV### Phase IV signed Weil support-extension/Lean compiler and NF### Phase III original numerical source enclosure custody remain UNCHANGED. Separate PI### pole/prime/Gamma spectral interface remains independent.

**Honest status:** four actual primary-source Git blob SHAs verified; independent exact rational eight-cell arithmetic checked; original analytic second-derivative expression derived by ordinary calculus and independently NUMERICALLY cross-checked against Hardy-`Z` direct differentiation; two NEW original-v4.35 Lean SOURCE PROOF CANDIDATES committed; NO new accepted Lean 4.35 .olean/axiom receipt; NO validated source ζ derivative interval enclosure, NO uniform Hardy-`Z` third derivative bound, NO rigorous original Hardy-`Z` first derivative anchor, NO CP010 narrow 53rd zero kernel existence proof, NO original signed Weil ↔ complete spectral form equality, and NO global Weil positivity or RH claim.

## 1. A specific source limitation: the original Hardy-Z bound controls values, NOT derivatives

Directly read source `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`, `Zeta/Zeros/HardyZ.lean` (Git blob `9975442b0c14011c35f4624197d0bf26169c7665`).

Its original definition is
```lean
noncomputable def Zeta.hardyZ (t : ℝ) : ℝ :=
  (Complex.exp (Complex.I * (riemannSiegelTheta t : ℂ)) *
    riemannZeta (1 / 2 + Complex.I * t)).re
```
The source proves `riemannSiegelTheta_eq_im_logGamma` for (t\ge0), `continuousOn_hardyZ`, `hardyZ_eq_zero_iff_riemannZeta`, `abs_hardyZ_sub_re_le`, and `abs_hardyZRemainderEM_le`. The LAST is a uniform (for its stated source parameters) **VALUE** approximation:
[
|Z(t)-\widetilde Z_{M,N}(t)|\le\mathcal E_{M,N}(t).
]
It **does not prove** (|Z'(t)-\widetilde Z'_{M,N}(t)|\le mathcal E_{M,N}(t)), or a (Z'') or (Z''') enclosure. Differentiating the absolute error inequality would be INVALID. Even a function satisfying a tiny value error (r(t)=\varepsilon\sin(K(t-a))) has (|r(t)|\le\varepsilon) but (r'(a)=\varepsilon K), arbitrarily large as (K\to\infty). A similarly constructed smooth remainder has arbitrarily large higher derivatives. This is a source-level **proof obligation**, not a solver/compiler optimization.

The original source `Zeta/Gamma/LogGammaBranch.lean` (Git blob `f544c4682969d8cefe0b8f489f6ddbaafaba45d5`) DOES provide `Complex.hasDerivAt_logGamma`, the derivative of the genuine holomorphic `logGamma` branch on the right half-plane in terms of `Complex.digamma`. It also provides the exact phase-`logGamma` relation. These support deriving derivative *FORMULAE*, but not automatic rigorous NUMERICAL ENCLOSURES of the ζ derivative, digamma derivative or their original error terms.

## 2. Mathematical source-exact analytic jets: phase, ζ and ζ' MUST remain correlated

Put (s(t)=\tfrac12+it, w(t)=\tfrac14+\tfrac i2t, \theta(t)=\operatorname{riemannSiegelTheta}(t)), and (E(t)=e^{i\theta(t)}). For positive (t), original `riemannSiegelTheta_eq_im_logGamma` states
[
\theta(t)=\Im\log\Gamma(w(t))-\frac t2\log\pi.
]
Ordinary chain rule applied to the original holomorphic `logGamma` gives
[
\boxed{\theta'(t)=\tfrac12\Re\psi(w(t))-\tfrac12\log\pi},
\qquad
\boxed{\theta''(t)=-\tfrac14\Im\psi'(w(t))},
]
where (psi=\operatorname{digamma}=\Gamma'/\Gamma) and (\psi'=\operatorname{deriv}\psi).

Write (u(t)=\zeta(s(t))), (zeta_1(t)=\zeta'(s(t))), (zeta_2(t)=\zeta''(s(t))), where ζ' and ζ'' denote derivatives with respect to COMPLEX (s), not the real Hardy-`Z` variable. Since (s'(t)=i), the exact source mathematical jets are:

[
\boxed{Z'(t)=\Re\left(E(t)\,i\,[\theta'(t)u(t)+\zeta_1(t)]\right)}
]
and
[
\boxed{
Z''(t)=\Re\left(
E(t)\left[
-\theta'(t)^2u(t)
-2\theta'(t)\zeta_1(t)
-\zeta_2(t)
+i\theta''(t)u(t)
\right]\right)}.
]

**Cancellation is essential.** An independent norm bound on all four summands generally overestimates (|Z''|), missing the phase/zeta cancellation that numerically keeps the true result below 4. The proper verified enclosure should evaluate the entire complex bracket and its final rotated REAL part, with source-certified complex balls and correlated quantities.

The original true Lean declarations do NOT yet contain a new accepted theorem `deriv (deriv Zeta.hardyZ) t = sourceSecondJet t`; CP018 leaves that as an EXPLICIT missing source-to-jet derivative identity. No value-error remainder is illegitimately differentiated.

`cp011_zeta_v435/CP018HardyJet.lean` defines `thetaPrimeJet`, `thetaSecondJet`, `sourceFirstJet`, and `sourceSecondJet` using the original exact functions `riemannSiegelTheta`, `riemannZeta`, `Complex.digamma`, `deriv riemannZeta`, and `deriv (deriv riemannZeta)`. The two conditional formal theorem targets are:

- `uniform_curvature_of_eight_source_jet_boxes`: if the actual source derivative equals this second jet ON the full interval, and eight whole-cell analytic interval boxes each rigorously bound the jet by 4, then the original Hardy-`Z` has (|Z''|\le4) universally.
- `genuine_anchor_of_first_jet_certificate`: if (Z'(a)=\texttt{sourceFirstJet}(a)) and a validated source numerical enclosure proves that jet (\ge12/5), then the CP017 anchor follows.

Both are **conditional** source formal candidates and are NOT new accepted numerical derivative results.

## 3. Eight-cell rigorous finite-reduction option with a third derivative bound

An alternative, more finite target replaces the **UNIFORM second-derivative** interval enclosure by EIGHT exact-rational point enclosures plus a **UNIFORM third-derivative** bound. This is a formal sufficiency alternative; it is NOT automatically a cheaper analytical certification. It adds one derivative and therefore might prove harder.

Let
[
a=149500/1000=149.5,\quad b=15005353/100000=150.05353,\quad
\Delta=b-a=55353/100000=0.55353.
]
Partition ([a,b]) into eight closed subintervals (I_j=[a+j\Delta/8, a+(j+1)\Delta/8]), (j=0,\ldots,7), with exact midpoint
[
\boxed{c_j=a+\frac{2j+1}{16}\Delta},\quad
\forall t\in I_j:\quad |t-c_j|\le\Delta/16.
]
The eight centers are **exact fractions**, not reconstituted original private batch-row endpoints.

Sufficient genuine analytic obligations are
[
\boxed{|Z''(c_j)|\le7/2\quad(j=0,\ldots,7)}
\quad\text{and}\quad
\boxed{|Z'''(t)|\le12\quad\forall t\in[a,b]}
]
plus the necessary source real differentiability of (Z''). Then for every (tin[a,b]), the mean-value theorem gives
[
|Z''(t)|
\le |Z''(c_j)|+12|t-c_j|
\le\frac72+12\frac{\Delta}{16}
=\boxed{\frac{1566059}{400000}=3.9151475<4}.
]
The strict arithmetic margin is
[
\boxed{4-\frac{1566059}{400000}
=\frac{33941}{400000}=0.0848525}.
]
This is fully exact rational algebra. It leaves mathematical slack for numerical interval certificates, but NO source derivative bound has yet been certified.

The eight centers (c_j) and high-precision *NONRIGOROUS* independent direct Hardy-`Z` derivative samples are:

| j | Exact center | Decimal center | Exploratory (Z''(c_j)) |
|---:|---:|---:|---:|
| 0 | 239255353/1600000 | 149.534595625 | +0.106931643856299 |
| 1 | 239366059/1600000 | 149.603786875 | −0.378772551065931 |
| 2 | 47895353/320000 | 149.672978125 | −0.856943019546586 |
| 3 | 239587471/1600000 | 149.742169375 | −1.321328978765288 |
| 4 | 239698177/1600000 | 149.811360625 | −1.765845664303697 |
| 5 | 239808883/1600000 | 149.880551875 | −2.184649892907262 |
| 6 | 239919589/1600000 | 149.949743125 | −2.572212831143788 |
| 7 | 48006059/320000 | 150.018934375 | −2.923389079319170 |

Numerically (max_j |Z''(c_j)|\approx2.92339<3.5), (Z'(149.5)\approx2.442738>2.4), and an independent 81-point screen of (Z''') on ([a,b]) finds (max |Z'''|\approx7.04<12). **None of these finite samples proves any of the universally quantified analytical statements, and they must never be entered into Lean as a theorem or axiom without actual enclosure/error proofs.**

Two independently computed numerical routes agree pointwise for the eight `Z''` center samples: direct `mpmath.diff(mpmath.siegelz)` and the ORIGINAL phase–zeta complex derivative formula using `mpmath.loggamma`, `mpmath.digamma`, `mpmath.polygamma` and `mpmath.zeta` derivatives. This is a consistency check, NOT a certified source integral or ball.

## 4. Actual NEW source Lean theorem scope

New `cp011_zeta_v435/CP018EightCell.lean`, original external Lean 4.35 source candidate:

1. `center_mem_interval`: exact first/last rational bounds for each finite center.
2. `eight_center_cover`: exact `∀t∈[a,b], ∃j∈Fin8, |t-c_j|≤\Delta/16`, explicit interval arithmetic.
3. `exact_eight_cell_curvature_margin`: exact result `1566059/400000<4`.
4. `eight_midpoints_and_third_derivative_imply_curvature`: universal `|f''|≤4` for any real function with explicit whole-interval (f'') smoothness, `|f'''|≤12), and 8 midpoint `|f''(c_j)|≤7/2) certificates. Reuses ORIGINAL Mathlib v4.35 `Convex.norm_image_sub_le_of_norm_deriv_le`.
5. `original_hardyZ_strictMono_of_eight_midpoint_certificate`: if genuine original Hardy-`Z` derivative anchor (Z'(a)\ge12/5), derivative smoothness, genuine 8 midpoint enclosures, and whole-interval `|Z'''|≤12) all hold, derive CP017 original Hardy-`Z` strict monotonicity.

These are SOURCE CANDIDATES. The first three use exact arithmetic and are straightforward mathematically; all five still require REAL Lean compilation. The last two absolutely preserve their missing original analytic premises in the type signatures.

New `cp011_zeta_v435/CP018HardyJet.lean` exposes formal first/second phase–zeta jets and the two additional conditional source numerical box and derivative-identity transfers. No source value-bound differentiation appears.

The target hierarchy is now explicit:

```
Original Hardy-Z phase/ζ derivative identities                UNPROVED NEW LEAN
  ├── honest direct complex 8-cell Z'' interval boxes <=4     OPEN, OR
  └── 8 rigorous point |Z''|<=7/2 + uniform |Z'''|<=12        OPEN
Actual original Z'(149.5)>=12/5                                OPEN
       ↓ exact CP017 curvature budget & strict monotonicity  NEW LEAN SOURCE CANDIDATE
Genuine new original Zeta root t∈(150.05352,150.05353)        OPEN
       ↓ CP016 original complete source rank theorem         NEW LEAN SOURCE CANDIDATE
Numerically refined root t is source ordinal #53              CONDITIONAL ONLY
       ↓ signed Weil Pole−Prime+Gamma 3×3 spectral dictionary INDEPENDENT OPEN
RH / global signed Weil positivity                             OPEN
```

## 5. Original immutable provenance, exact preflight and strict kernel custody

Directly re-fetched and verified all 4 original primary-source Git blob hashes:

| Original source | Immutable source Git blob | Genuine available declaration |
|---|---|---|
| `smmercuri/zeta@c06b4e13...` `Zeta/Zeros/HardyZ.lean` | `9975442b0c14011c35f4624197d0bf26169c7665` | genuine HardyZ/phase and VALUE-error bound, NOT derivative error |
| original `Zeta/Gamma/LogGammaBranch.lean` | `f544c4682969d8cefe0b8f489f6ddbaafaba45d5` | genuine `hasDerivAt_logGamma` with `digamma` |
| original `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` | `c2b1da101a580cc91cfb0a43d72d5839fd97265c` | genuine `N_gramPoint_eq`, bounded-height simplicity |
| `mathlib4@v4.35.0` `Mathlib/Analysis/Calculus/MeanValue.lean` | `7004c9f6d2bf12928f02be9ee35a814aed17e254` | genuine mean value/Lipschitz transfer theorem |

`scripts/cp018_hardy_jet_eight_cell_preflight.py` verifies exact stdlib `Fraction` tiling and radius, explicit failed-bound controls (center cap 15/4 or third cap 15 lose the result), all four original source blob SHAs and actual theorem names, CP018 Lean theorem/source-premise signatures, optional high precision `--numeric-screen` cross-check of the two analytic formulas. The optional numerical screen prints NONRIGOROUS and does not run automatically in kernel CI. The source-only receipt is `CP018_FOUR_ORIGINAL_SOURCE_SHA_AND_EIGHT_CELL_EXACT_LOGIC_PASS_NOT_LEAN`.

`scripts/cp018_hardy_eight_cell_lean_axiom_audit.py` is FAIL-CLOSED: requires **11 actual** original external compiled `.olean` files (two new CP018 modules plus 9 CP013–017 prerequisite modules), actual `#print axioms` output for all **SEVEN** new theorems, and standard `propext, Classical.choice, Quot.sound` only. It also actively verifies no missing source analytical hypotheses were silently removed. Even on true compiler success, the receipt is `CP018_ORIGINAL_HARDY_8CELL_AND_COMPLEX_JET_CONDITIONAL_KERNEL_PASS_ONLY`, explicitly stating the source differentiated jet equality, eight real interval certificates, third-derivative bound, anchor, narrow root existence and original signed Weil/spectral dictionary remain UNPROVED.

Two new **opt-in only** workflows protect the currently congested NF###/IV### queues:
- `.github/workflows/cp018-hardy-eight-cell-original-source-opt-in.yml`: label `cp018-jet-source` or eligible manual dispatch, exact fractions/source Git SHA; NOT kernel.
- `.github/workflows/cp018-hardy-eight-cell-v435-lean-kernel-opt-in.yml`: label `cp018-jet-lean` or eligible manual dispatch, genuine original Zeta 4.35 build + kernel standard-axiom audit; not automatically enqueued on ordinary PR/push events.

At CP018 PR creation, no new actual source preflight or original Lean compiler workflow is assumed run. This distinction is deliberate: only real compilation can elevate a new theorem.

## 6. CP019: genuinely certify an ORIGINAL derivative jet, not merely repeat numerical screening

The next exact obligation is to derive derivative-specific error bounds for the original `Zeta.hardyZ` formula. Candidate routes:

- Prove in Lean the actual source phase-derivative identities from `riemannSiegelTheta_eq_im_logGamma` and `hasDerivAt_logGamma`; obtain corresponding ζ first and second derivative identities from original holomorphic `riemannZeta`. Include real/complex chain rules, confirm branch and no-pole hypotheses on the full interval.
- Produce validated `ζ(s),ζ'(s),ζ''(s),\psi(w),\psi'(w),e^{iθ(t)}` **complex balls on EACH of the eight full intervals** and combine with rigorous cancellation-aware interval evaluation of `sourceSecondJet`. This may close `|Z''|≤4` with no global third derivative theorem if the interval precision is sufficient.
- Alternatively rigorously certify eight rational center values `|Z''(c_j)|≤7/2` and a universal `|Z'''|≤12`; then the CP018 exact midpoint/MVT sufficiency theorem closes the global curvature cap.
- Independently produce the original derivative anchor `Z'(149.5)≥12/5`, and a new authentic Lean kernel zero-existence proof for `(150.05352,150.05353)`. The original `abs_hardyZRemainderEM_le` value bound can help certify root signs, but NOT derivative estimates without a separate analytic argument.
- Check and repair the actual CP013–CP018 original Lean source builds when the independent compiler capacity is available; do not convert QUEUED workflows into imaginary PASS receipts.

**Preservation law:** source original true zero rank, phase/ζ derivative identity, and signed Weil/zero-side normalization cannot be inferred from high-precision numerical checks alone. Every approximation/change of coordinate must explicitly transport its **error, phase and derivative information**. The old original value-only error theorem does not transport derivative information.

**No global Weil positivity or RH claim.**
