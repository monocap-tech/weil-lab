# NF659 — complete original physical compact interval custody; exact transform gate architecture

## Latest actual compiler verification

Recovered NF658 run **44426966066**, job **135234186938**, completed with failure only at the final four-case transformed integer pilot. Stages which completed **SUCCESS**:
- Original physical H symmetry and fifteen stored integer witness conditions, including exact positive margin bound.
- First real and pole widened rows.
- **All 120 genuine original 15-source physical H entry containments in the 64-digit compact balls**, via the already Lean-certified NF655 original 2600-digit enclosures. The first and pole row and the complete module all built.
- Generic physical quadratic cross-term inequality and interval bilinear lower bound.

The failed pilot is **not a failed interval** or a mathematical counterexample. The log reports exactly:
`TransformPilot.lean:28:2: Tactic decide proved that the proposition nf658TransformedCenter 0 0 = <old 180-digit decimal> is false`.
The pole center and pole radius passed with standard axioms. Actual independent arithmetic computed first-center literal with **192 digits**, which was already corrected on NF658 PR #681 head `fbb7ba7c406cfe80c0b55f9075097e839ba58393`; that corrected run **44427400456 remained queued at final NF659 inspection**. The older failed run did not build the last audit step. Do not claim that final transformed pilot is Lean PASS.

## New mathematical/formal decomposition

1. `ActualZetaOriginalPhysicalGramCongruenceInterval.lean` supplies a generic theorem: for any real entries (H_{pq}) with (|H_{pq}-C_{pq}|\le E_{pq}), and arbitrary fixed real (K),
[
 left|\sum_{p,q}K_{ip}K_{jq}H_{pq}
      -\sum_{p,q}K_{ip}K_{jq}C_{pq}\right|
 \le \sum_{p,q}|K_{ip}K_{jq}|E_{pq}.
]
This is an actual candidate proof using only triangle inequalities, `Finset.abs_sum_le_sum_abs`, and componentwise inequalities. No positivity assumption. **Lean pending**.

2. `ActualZetaOriginalPhysicalGramDiagonalDominance.lean` proves candidate uniform nonnegativity of the off-diagonal pair energy (sum_{i\ne j}(|b_{ij}|(y_i^2+y_j^2)+2b_{ij}y_iy_j)\ge0), and the exact symmetric row/column absolute payment exchange. Both are intended as sublemmas of the Gershgorin coercivity proof. **Lean pending**.

3. `scripts/emit_nf659_gram_transformed_gates.py` computes **all 225 transformed center values and 225 transformed radius bounds**, directly as four-index integer sums from original compact witness (K,C,E), **no interpolated eigenvalues or new numerical solver**. It checks all 225 symmetry/equivalent moment pairs, recomputes all 15 dominance margins, and independently checks the exact Frobenius norm of (K) and the original (10^{-60}) integer gate. It emits 15 bounded row proof modules, each with 30 literal kernel checks; a ComputedData module with 15 complete row margins, nonnegative margins, symmetry, Frobenius norm and exact conservative coercivity gate; a terminal import module. **External in-session Python preflight PASS** on actual compact witness `/mnt/data/nf657_compact_congruence.json`; 17 emitted modules (450 center/radius proof targets). Actual transformed four sample decimals match original preflight, including the corrected 192-digit oscillator first center. These are proof proposals only, not yet Lean PASS.

4. A single focused workflow first builds generic theorems, the repaired NF658 pilot and computed arrays, three representative transformed rows (0,7,14), then the complete set of 450. It audits named standard axiom dependencies. The actual 120 source-data archive and old NF648/655 proof artifact pins remain unchanged.

## Remaining formal target

Once compiled, use the genuine physical compact entry enclosures and generic finite double-sum theorem to conclude the real congruence (B=K H_I K^\mathsf T) is contained in all 225 integer-computed transformed balls. From fifteen strictly positive certified row dominance margins, derive (y^\mathsf TB y\ge (m/S^3)\|y\|_2^2). Because the rational integer preconditioner (K) is unit lower triangular, it is invertible; use (x=K^\mathsf T y) and the exact Frobenius bound to conclude (x^\mathsf TH_Ix\ge10^{-60}\|x\|_2^2). The full coercivity bridge is not yet implemented as a kernel theorem; **OPEN**.

No main merge, no claim on the full 242-generator physical H, entire signed Weil positivity or RH.
