# Weil-Lab — CP030
## Six scalar original Euler–Maclaurin finite-value certificates replace two complex coarse-box hypotheses

**Track:** independent CP### cross-projection compatibility, stacked on CP029 draft PR #851, CP028 #850, CP027 #849 and CP026 #848. Original IV/NF/PI proofs, acceptance counts and runner controls remain untouched.

**Precise status:** the mathematical implications are elementary and exact, but CP030 Lean source is an **UNCOMPILED CANDIDATE**. Its six concrete original source-value hypotheses are **UNPAID**. Python outward-cell manifest generation is external evidence, **not** kernel acceptance. The full 255+6 directed interval replay has not run in this CP030 turn. No source theorem or JSON assertion was smuggled into Lean as an axiom.

### 1. Exact original six-scalar proof interface

Define the TRUE original source quantities

- A(t) = zetaApproximant(1/2+i*t, 6, 256);
- F(t) = Re(exp(i*thetaStirling2_0(t)) * A(t));
- tLeft = 15005352/100000, tRight = 15005353/100000.

The new proposition FiniteScalarCells has exactly six original numerical claims:

| True original finite scalar | Left endpoint | Right endpoint |
|---|---|---|
| abs(real(A)) | ≤ 1/10000 | ≤ 1/10000 |
| abs(imag(A)) | ≤ 1/10000 | ≤ 1/10000 |
| finite rotated real F | ≤ −2/10^7 | ≥ 1/10^6 |

The prior EXTERNAL CP025/CP028 source intervals indicate approximately F(left)=−6.8174086701×10^-7, F(right)=+1.5519759813×10^-5 and original A norm bounds of comparable magnitude. These are not kernel facts.

For each endpoint, exact complex decomposition and the triangle inequality give

    norm(A) ≤ abs(real(A)) + abs(imag(A)) ≤ 2/10000 < 1/1000.

The signed thresholds are stronger than CP028's strict F(left)<−1/10^7 and F(right)>1/10^7. Hence the six actual source-value inequalities imply **both** CP028 finite boxes. The six scalars must still be proved from the original source; they are not automatically established by this conditional implication.

### 2. Genuine Lean source interface, not yet compiled

NEW cp011_zeta_v435/CP030FiniteComponentCells.lean imports only CP028CoarseFiniteBoxes and introduces four real original-source proof candidates and four #print axioms queries:

1. norm_of_coordinate_caps — purely elementary complex norm inequality;
2. left_coarse_of_scalar — turns three original left scalar bounds into CP028 FiniteLeftBox;
3. right_coarse_of_scalar — turns three original right scalar bounds into CP028 FiniteRightBox;
4. original_narrow_zero_of_scalar_cells — original narrow critical-line ζ-zero conditional on FiniteScalarCells, inheriting every original CP026/27/28 source/Lean obligation.

This candidate is *not* added to shared cp011_zeta_v435/lakefile.toml yet. That file is a source-scoped dependency of inherited CP013 and CP014 PR workflows, and changing it now would needlessly launch their audits. The parent CP026/27/28 modules themselves remain uncompiled. A genuine controlled Lean 4.35 build and four standard-axiom receipts are still required for CP030's conditional theorem.

### 3. Executable exact outward rational cell manifest

NEW scripts/cp030_original_finite_component_cell_manifest.py locks the CP025 10^55 integer-directed engine to Git blob e392ad4d5ded49f8314006335fa95ed15c7381de and the original Zeta commit c06b4e13d9c847e50a32c3d738271cbad62ae9f3.

With --replay it executes the original 255 Dirichlet terms, original pole and half terms, six Bernoulli corrections, and source theta-Stirling2 phase approximation. For each endpoint it rounds the complex A real part, A imaginary part and rotated finite real part OUTWARD to **exact integer pairs divided by 10^9**. Six exact Fraction comparisons check the new scalar thresholds, refusing a receipt on failure. It does not call an oracle for ζ/Gamma.

Cheap local syntax/exact controls passed for this new script; full CP025 source replay was **not run in this turn**. Source gate checks and real replay are available when checked out inside the full branch:

    python scripts/cp030_original_finite_component_cell_manifest.py --self-test --source-check
    python scripts/cp030_original_finite_component_cell_manifest.py --self-test --source-check --replay --receipt cp030-six-scalar-outward-cells-NOT-LEAN.json

The JSON will explicitly mark all six Lean source-membership facts, original narrow-zero, rank 53, global Weil positivity and RH as false. To obtain an actual Lean certificate, the next phase must verify each source finite expression's outward interval membership via trusted log/trig/Dirichlet/Bernoulli term-level bounds. **Never assert a generated JSON numeric value as a new Lean axiom.**

### 4. Certification and CI custody

CP030 changes precisely one new Lean conditional source candidate, one external source-aware interval script, and this document. It changes no historical source identity, no shared Lake registry, no ordinary CI workflow, no labels, and dispatches no heavy CI. The branch inherits CP029's read-only trigger audit: ordinary PR workflows were path-scoped and none previously depended on these three new paths. Recheck the head before any further CI submission.

**Still open:** CP029's 11 original pointwise Borwein Lean 4.35 proofs and strict axiom receipts; all six original CP030 finite scalar source proofs; actual CP026/27/28/30 chain compilation; source ordinal53/uniqueness; normalized original signed Weil↔spectral preservation, support-independent original positivity, and RH. The protected NF 692/968 kernel frontier does not advance from CP030.


### 5. Additional exact error-budget improvement (conditional)

If the four true source real/imaginary component inequalities hold, the proven elementary upper bound is norm(A) <= 2/10000, so the original published theta cap and the CP027 source-derived (but still uncompiled) remainder bound yield

    E(t) <= (12/150^4)*(2/10000) + 3/10^13
         = 1361/270000000000000
         ≈ 5.04074074074074e-12 < 1/10^11.

This rational equality and comparison were checked independently using Python Fraction arithmetic. They tighten CP028's conditional 6481/270000000000000 budget by approximately 4.76x; the rounded CP028 1e-10 ceiling is almost 20x larger. They **do not** establish the six original finite scalar inequalities or the pending CP027 original Lean theorem.

The source-only gate additionally pins the exact inherited CP028 coarse-box Git blob 5cc23f986d575cf94343a6afc19e9de2ee1ea536, rejecting drift before numerical receipt creation.
