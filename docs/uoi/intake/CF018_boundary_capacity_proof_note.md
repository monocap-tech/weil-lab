# Weil-Lab CF018 — Optimal logarithmic packet capacity and arithmetic decoupling

Date: 2026-11-21. Mode: local analytic/proof-preparation; **no CI, GitHub writes, or Lean certification**. Original HD/A kernel-passed frontier remains **692/968**.

## Original carrier and exact source links

Use the real Fourier transform `Ff(ξ)=∫e^{-2πixξ}f(x)dx`, the Mathlib normalization, and

`w(ξ)=log(exp(1)+|ξ|)`, `||f||log²=∫w(ξ)|Ff(ξ)|²dξ`.

Pinned read-only source inspection on `research/iv023-original-four-cell-schwartz-partition-and-prime-transfer`:

- `WeilDefect/Arithmetic/LogarithmicForm.lean` blob `ae932d4f3f7e4d6d06dbd778a5708927172238dc`: exact `logarithmicFourierWeight`.
- `WeilDefect/Morphology/NeutralLogHilbertCarrier.lean` blob `679d58b8f0cfa6b4f7d28c48ce844a41cdce2844`: carrier norm equals physical Fourier logarithmic energy.
- `WeilDefect/Arithmetic/ActualZetaNativeFormOperator.lean` blob `93beff3a82207f44fd5a431987c39f1aeb7e0092`: Gårding inequality `||f||log² <= Q_c(f) + M_c||f||²` with `M_c=neutralActualZetaNativeLogError(c)+neutralPhysicalPoleEnergyConstant(c)`.
- `WeilDefect/Morphology/NeutralLogPoleSourceAttachment.lean` blob `331ad94a02336a124eb6c17e3ee94480694a8c5c`: pole uses two Hermitian **cross moments**, not a sum of positive squares.

Use CF017's exact mixed discrepancy `D_c(f,v)`, without changing the original prime weights or source identities. For support `[-c,c]` let `S_c=∑_{log n<2c}Λ(n)/√n`.

## Theorem CF018-A — exact local Fourier-capacity bound

For any `v∈L²(R)` supported in an interval of measure/length at most `ell`, and any `0<R<1/(2ell)`, `||Fv||²_{L²(-R,R)} <= 2Rell ||v||²_2` by Cauchy–Schwarz in the physical variable and Plancherel. Hence, whenever `v` has finite logarithmic energy,

`||v||log² >= (1-2Rell) log(e+R) ||v||²_2`.

Taking `R=1/(4ell)` gives

`||v||²_2 <= [2/log(e+1/(4ell))] ||v||log²`.

For `L=log(1/ell)>=2`, the choice `R=1/(2ell L)` also gives the explicit lower bound

`||v||log² >= [L-log(2L)-1] ||v||²_2`, which has optimal leading coefficient 1.

No pointwise boundary trace, derivative, positivity of Weil Q, or RH hypothesis is used.

## Theorem CF018-B — optimal arithmetic mixed-form decoupling

CF017 established, for every support interval `I` of width `ell`, `supp(v)⊂I`, and `f∈D_c`,

`|D_c(f,v)| <= [ S_c (sqrt(2)*ell^(1/4) + 1/sqrt(log(e+ell^(-1/2)))) + sqrt(ell*(e^(2c)-1)) ] ||f||log ||v||_2`.

Combining with CF018-A yields

`|D_c(f,v)| <= A_c(ell) ||f||log ||v||log`, where

`A_c(ell) = sqrt(2/log(e+1/(4ell))) * [ S_c*(sqrt(2)*ell^(1/4) + 1/sqrt(log(e+ell^(-1/2)))) + sqrt(ell*(e^(2c)-1)) ]`.

As `ell↓0`, `A_c(ell) = O_c(1/log(1/ell))`. This is **not uniform in c** and does not by itself exclude a null vector. It is valid for arbitrary complex phases, with no graph-only approximation.

## Proposition CF018-C — the logarithmic rate is sharp in general

Fix `c=0.4`, `a=log 2`, and `0<ell<min(c,2c-a,a)`. Then the sole active prime power is `n=2` and `κ=log(2)/sqrt(2)`.

Let

`v_ell(x)=ell^(-1/2) 1_(c-ell,c)(x)`, and

`f_ell(x)=ell^(-1/2) 1_(c-a-ell,c-a)(x)`.

Both have L² norm 1, log energy finite, and the same log norm. A direct triangular-correlation computation gives

`D_c(f_ell,v_ell) = κ/2 - (8 sqrt(2)/ell) sinh²(ell/4) -> κ/2`.

Their Fourier energies have exact integral expression

`||v_ell||log² = ∫_R log(e+|z|/ell) [sin(πz)/(πz)]² dz`.

Subtracting `L=log(1/ell)` and applying dominated convergence gives

`||v_ell||log² = L + K + o(1)`, with `K=∫_R log|z| sinc²(πz) dz` finite.

In fact, the Mellin identity

`∫_R |z|^s sinc²(πz) dz = (2π)^(-s)/(Γ(2-s) cos(πs/2))`

for `-1<s<1` gives `K=1-γ-log(2π)≈-1.41509273`.

Therefore the normalized discrepancy satisfies the exact asymptotic limit

`lim_(ell↓0) L * |D_c(f_ell,v_ell)| / (||f_ell||log ||v_ell||log) = κ/2 = log(2)/(2sqrt(2))>0`.

Thus an `o(1/log(1/ell))` uniform mixed-discrepancy bound is impossible on the original logarithmic carrier, even in the first prime-active window. This is a structural negative control, not an RH counterexample.

## Corollary CF018-D — native narrow-packet logarithmic coercivity

Let `M_c⁺=max(0,M_c)` with `M_c` the **original full-form** Gårding error above. If `v∈D_c` is supported in an interval of width `ell`, then

`Q_c(v) >= (1-2 M_c⁺/log(e+1/(4ell))) ||v||log²`.

In particular, whenever `log(e+1/(4ell)) >= 4M_c⁺`,

`Q_c(v) >= (1/2) ||v||log²`.

This is stronger than previously established `Q_c(v)>=const*||v||²`. The admissible width may be extremely small because `M_c` need not be sharp.

## Corollary CF018-E — quantitative neutral-boundary dichotomy

Suppose `Q_c>=0` on the original domain and `k∈ker Q_c`. For any lawful decomposition `k=u+v` with `u,v∈D_c` and `supp(v)` contained in an interval of width `ell` satisfying the preceding coercivity condition, let `B_ref = B_Gamma + B_positive_reference`; the exact original complex mixed identity is `B_W = B_ref - 2D_c`. Then

`-Re B_ref(u,v) >= (1/2)||v||log² - 2 A_c(ell) ||u||log||v||log`.

Therefore either

(A) `||v||log < 8 A_c(ell)||u||log`, i.e., the collar packet has *very little* log energy relative to the interior,

or

(B) `-Re B_ref(u,v) >= (1/4)||v||log²`, i.e., the archimedean-plus-positive-reference interaction supplies significant negative mixed energy.

The dichotomy is **necessary**, not contact exclusion. To progress, prove an independent endpoint lower/upper comparison for `B_ref(u,v)` strong enough to rule out branch (B), and an observability/lower bound on a genuine neutral mode to rule out branch (A). Both are open.

## Local tests

Run `python /mnt/data/cf018_boundary_capacity_validation.py`. The script independently quadratures the exact one-prime triangle correlation, verifies the explicit capacity inequalities on normalized rectangles, calculates an exploratory finite-cutoff Fourier energy with a proven positive-tail upper bound, and checks the mixed bound numerically. It does not claim rigorous interval rounding certification or Lean kernel acceptance.

## Formal and CI plan

Highest-value immediate Lean obligations, *after a permitted base lineage is selected*, are (1) local Fourier-mass bound, (2) exact normalized mixed-discrepancy bound, (3) Gårding-based coercivity, and (4) the neutral-boundary dichotomy. Keep the step-function sharpness analysis separate, with density support if needed.

Source-identity audit must preserve the original support-right-limit convention `log n < 2c`, Hermitian complex polarization, cross-pole normalization, and physical/canonical Fourier units. Required verification: local `lake env lean` on a single module, `lake build` for the targeted import graph, `#print axioms` with only allowed foundational axioms, no `sorry` or unstated hypotheses, independent mathematical and Python tests.

GitHub submissions/actions: **NONE in this CF018 pass**. The earlier NF753 vs NF756 branch-lineage divergence remains unresolved; before creating a CF PR, verify full workflow source-scoping, branch ancestry and expected PR fan-out. Do not start heavy CI, do not alter NF750–NF753 source/certificates/receipts, and do not promote 692/968.