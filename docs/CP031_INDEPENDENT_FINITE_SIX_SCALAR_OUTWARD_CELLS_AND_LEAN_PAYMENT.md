# Weil-Lab — CP031
## Independent outward-rational six-scalar reproduction and precise original-source Lean payment map

**Branch:** research/cp031-independent-six-scalar-replay, stacked only on CP030 draft PR #852 (then CP029 #851, CP028 #850, CP027 #849, CP026 #848). No changes to NF/IV/PI source, acceptance records, toolchains, Lake registry or GitHub Actions workflows.

**What was actually accomplished:** a separately coded original Euler–Maclaurin finite-expression **reconstruction** produced six exterior rational interval cells, all with denominator 10^9, at BOTH exact rational centers. Integer fixed-point scales 10^50 and 10^55 gave the SAME six final interval pairs. This is robust external numerical evidence; it is NOT a run of the pinned original CP025 Git-blob engine, is NOT a newly established correspondence to every original Lean source definition, and is NOT a Lean kernel certificate. There is no proof of RH, global signed Weil positivity, or zero ordinal 53.

### 1. Original numerical quantities and external cells

With s(t)=1/2+it and the original source-oriented finite approximation
A(t)=zetaApproximant(s(t),6,256), let
F(t)=Re(exp(i*thetaStirling2_0(t))*A(t)).
The two exact centers are tL=15005352/100000 and tR=15005353/100000.

The independent exact-rational reconstruction produced, with outward bounds displayed as INTEGER PAIRS DIVIDED BY 10^9:

| Scalar | tL | tR |
|---|---:|---:|
| Re A | [-516, -515] | [11733, 11734] |
| Im A | [-447, -446] | [10158, 10159] |
| F | [-682, -681] | [15519, 15520] |

This directly satisfies CP030's six proposed **original source numerical** threshold *comparisons*:
- both |Re A| and |Im A| ≤ 10^-4, independently at each endpoint;
- F(tL) ≤ −2×10^-7;
- F(tR) ≥ 10^-6.

The cells contain strictly more detail than the six contract thresholds. No Boolean, interval endpoint, or fractional source value from this external calculation is introduced into Lean as a fact.

### 2. Independent arithmetic, no transcendental oracle

NEW \`scripts/cp031_independent_original_six_scalar_interval_crosscheck.py\` reconstructs the original M6,N256 published expression with 255 Dirichlet terms, pole, half-term, and six Bernoulli/Pochhammer terms. It separately evaluates the source-oriented theta Stirling-two phase. It uses:
- exact Python integers and Fraction throughout arithmetic;
- 10^55 fixed-rational outward intervals (a local second pass at 10^50 generated identical 10^-9 cells);
- an exact Machin pi identity with bounded rational alternating arctangent tails;
- rational atanh logarithm expansion with explicit positive tails;
- real sin/cos Taylor evaluation with Lagrange error bounds, restricted to exact checked reduced arguments in [-4,4];
- integer square roots bounding n^(-1/2) exactly;
- exact directed floor/ceil for all six final 10^9 cells.

The only Python floating operation chooses an *integer* multiple of 2π for argument reduction. It does not supply any value enclosure; the reduced argument is then required to satisfy the exact integer-domain check.

**Numerical trust boundary:** this local independently coded implementation was executed in the analysis runtime and produced all six cells. The committed GitHub script contains the same arithmetic algorithm as a reproducibility candidate, but no GitHub CI or Lean run is reported. Its output is not the same as source-kernel checking.

### 3. Newly sharpened rational error and sign margins — conditional

From the six component cells, elementary complex norm bounds give

    ||A(tL)|| ≤ (516+447)/10^9 = 963/10^9,
    ||A(tR)|| ≤ (11734+10159)/10^9 = 21893/10^9.

Using the original published theta error ≤12/t^4 (for these t>150), PLUS the source-derived but STILL UNCOMPILED CP027 cap |R|≤3/10^13, yields exact conditional budgets

    E_L ≤ (12/150^4)*(963/10^9)+3/10^13
        = 6053/18750000000000000 ≈ 3.2282667×10^-13;

    E_R ≤ (12/150^4)*(21893/10^9)+3/10^13
        = 138197/168750000000000000 ≈ 8.1894519×10^-13.

Meanwhile F(tL) ≤ −681/10^9 and F(tR) ≥15519/10^9. Thus, IF the corresponding exact source expressions are proved to lie within these cells and the error bounds are kernel-certified, BOTH original finite signs are separated from zero by large margins. This is a sufficient condition; its converse is neither required nor proved.

### 4. Remaining exact Lean proof duties

The next genuinely valuable source proof has no use for a 55-digit imported axiom:
1. In the frozen original Zeta v4.35 environment, prove rational outward enclosures for the actual original finite Dirichlet terms \`n ^ (-(1/2+it))\` across n=1,…,255 via verified n^(-1/2), log(n), sin(t log n), cos(t log n).
2. Prove rational outward cells for the pole term, half term, each of the six Bernoulli correction terms, and theta-Stirling-two phase, with an explicit identity to the original Lean \`zetaApproximant\` and \`thetaStirling2_0\` expressions.
3. Sum all source-term cells inside Lean using exact real inequalities; obtain actual original Re A, Im A, and rotated F memberships at the two rational heights.
4. Pay the six source cell membership theorems, then apply CP030's **conditional** scalar bridge; separately obtain original CP029 Borwein Lean v4.35 compilation with 11 strict standard-axiom receipts and compile CP026–28.
5. Only after the entire chain is kernel-accepted can existence of an original critical-line ζ zero inside (150.05352,150.05353) be called unconditional. The zero's source ordinal 53, uniqueness, full normalized signed Weil ↔ spectral equivalence, global Weil positivity, and RH remain separate, open tasks.

The exact numbers in the JSON are **targets for kernel proofs**, not trusted premises. A compiler pass of a conditional lemma alone does NOT establish those memberships.

### 5. Controlled repository/CI gate

CP031 adds one independent external arithmetic script, one JSON record labeled NOT LEAN, and this documentation. It changes no \`lakefile.toml\`, workflow file, original Zeta or signed Weil source. The CP029 branch's existing source-scoped trigger audit and manual/label-only kernel workflow policy remain in force. No heavy CI triggered or requested by CP031.

**Acceptance and guardrails:** Original NF certified frontier remains 692/968; no new CP source theorem is called LEAN PASS. CP031 numerical cells are external evidence only; actual CP025 pinned replay and independent source-level interval memberships await genuine execution/proofs.
