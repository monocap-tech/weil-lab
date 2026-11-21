# Weil-Lab — IV029
## Original signed correlation: the exact graph-arrow / source-argument dictionary

**Certification boundary:** This is an independent arithmetic and complex-algebra compatibility check, NOT a new Lean theorem. The existing original Phase IV IV009 repair is still queued at the latest API inspection. The IV018–IV024 checked workflows also remain queued/pending. Existing IV017–IV023 Schwartz/coercivity declarations remain source-only candidates until the true pinned Mathlib/Lean source and standard-axiom builds pass. Phase III NF### original physical numerical certification remains separate and untouched.

**Branch:** research/iv026-single-lane-iv009-kernel-recovery (IV029 committed here to avoid creating another branch/PR and adding further automatic workflow fan-out).

### 1. Exact source, not a guessed convention

The original Lean source ActualZetaCorrelationTransform.lean defines, literally,

    neutralWindowCorrelation a first second τ =
      ∫ x, window(second,x) * conj(window(first,x-τ)).

Under actual source support conditions, IV011 proves

    C(first,second;τ) = ∫ x, second(x) * conj(first(x-τ)).

Therefore the original source is **antilinear in its first argument, linear in its second argument**, with the conjugation on the shifted first input. A test can enter the correlation when

    x ∈ supp(second) ∩ (supp(first)+τ).

The independently constructed IV024 prime graph uses an oriented arrow

    from -> to at τ  iff  I_from ∩ (I_to+τ) is nonempty.

Consequently the exact interface is

    G(from,to;τ) = possible support for C(first=to,second=from;τ).

This is an **argument-order reversal**. The from cell is the SECOND Lean source argument; the to cell is the FIRST. It does not contradict IV027's corrected signed interval classifier; it explains precisely how the graph is to be consumed by the source pairing. Reading the arrow as (first,second) instead would reverse the n9 source entries even if the graph labels themselves are correct.

### 2. Original old-collar signed n9 entries

The fixed actual original old collars have centers -1099/1000 and +1099/1000 with radii1/1000. The rigorous rational 96-term log(9) enclosure lies strictly inside the overlap band for the two geometrically possible samples.

| True object | +log(9) sample | -log(9) sample |
|---|---|---|
| Graph arrow (from -> to) | old_right -> old_left | old_left -> old_right |
| Source C(first,second) | C(old_left,old_right) | C(old_right,old_left) |

The reverse-sign same-ordered pairs are strictly CLEAR. No other source-pair signed prime-power overlap is present among all four cells at the genuine active n in {2,3,4,5,7,8,9}. There are exactly 4 × 4 × 7 × 2 = **224** source-input and signed-prime cases.

**Caution:** An OVERLAP means the corresponding correlation can be nonzero for some supported tests; it does NOT mean any particular test has a nonzero actual integral, nor does it determine an eigenvalue or a sign of the full Weil form. The source n9 term is retained; it is not asserted nonzero for every test.

### 3. Complex structure and signed adjunction

For the authentic Schwartz physical correlation, change variable x -> x+τ and use complex conjugation to obtain the purely formal source identities

    C(α s, β t;τ) = conj(α) β C(s,t;τ);
    C(s,t;τ) = conj(C(t,s;-τ));
    C(f,f;τ) + C(f,f;-τ) is real.

Here the two signs are essential. In particular, C(s,t;τ) is generally NOT C(t,s;τ). A future independent arithmetic or spectral construction needs an explicit pairing and sign dictionary preserving these rules. Merely identifying the undirected support interaction graph would forget the conjugation and orientation.

The actual original von Mangoldt contribution uses BOTH +log n and -log n with real coefficients Λ(n)/sqrt(n); the diagonal two-sign component is therefore real when its full source sum/dictionary has been correctly established. IV029 does **not** prove the infinite original source prime sum or signed Gamma/pole transport from scratch. Those remain the existing IV011–IV023 formal and compiler obligations.

### 4. Executable independent tests and negative controls

New script: scripts/iv029_original_correlation_argument_order_audit.py.

The test imports the corrected IV024 source geometry, reconstructs the full 224-sample directed source dictionary by SWAPPING the graph arrow endpoints, and insists the only two old n9 source entries have the correct signs. The opposite signs must be provably separated, and both endpoints of the rigorous exact log9 enclosure must preserve the same overlap classification.

For an independent test of the **complex-algebra convention only**, it computes exact rational integrals of finite piecewise-constant test functions with rational complex coefficients on the four cells. It checks conjugate-linear first slot, linear second slot, C(s,t;τ)=conj(C(t,s;-τ)), and reality of diagonal ± samples. An intentionally wrong no-swap interface and the false same-sign input symmetry are separately rejected.

The piecewise-constant functions used for the algebraic test are **NOT Schwartz functions**. These computations validate the proposed algebraic interface and expose wrong conventions; they are not a Lean proof of Schwartz preservation or positive Weil coercivity. A locally reconstructed exact Fraction implementation of the same 224-sample/directed-pair checks passed before commit; actual CI execution of the newly committed source is NOT claimed.

### 5. Falsifiable cross-projection gate

The original arithmetic graph is an independent object **relative to the source Weil-form implementation**, but it is NOT an independently constructed spectral Hamiltonian. For a genuine external projection to be compatible, specify independently:

1. A Hilbert or sesquilinear target H with explicit convention (which argument is conjugate-linear);
2. a densely defined operator A and common source test domain D;
3. a map T:D→Dom(A), with actual proven linearity, injectivity/density if claimed, normalization and extension admissibility;
4. the exact equation W_original(f,g)=⟨Tf,A Tg⟩_H for all permitted pairs, with the full original signed Gamma, BOTH poles, and genuine ±log prime terms;
5. a source-bound assignment of each oriented graph interaction to a target coupling preserving the graph-to-source argument swap and τ→-τ adjunction.

**Falsification:** exhibit a permitted source test where a target pairing differs from W_original, an active shifted support entry mapped with the wrong source input or τ-sign, a failure of conjugation or phase covariance, or a missing full Gamma/pole correction. The graph alone does not determine the full pairing.

**Intrinsic vs coordinate/estimate-dependent:** True original correlation values and their sesquilinearity are properties of the fixed original pairing; the oriented overlap graph and support width depend on the chosen physical support (not on its cell-label permutation); the rough 1/16 margin and Schwartz cutoff choices remain auxiliary and not optimal spectral invariants.

### 6. Verification disposition and next IV030

No new Lean theorem or kernel receipt was produced here. At the latest inspection the repaired IV009 run 44850887402 remained QUEUED, and the other original IV018–IV024 checked runs remained queued/pending. The existing IV025 generated-manifest-order fixes, IV027 graph sign correction and IV028 diagnostic-parser repair are preserved on this recovery branch; the earlier individual stacked PR heads have not yet received their backports.

**IV030 priority:** recover a genuine successful IV009 Lean compiler/standard-axiom run or first actual new source diagnostic; integrate the source fixes with controlled workflow fan-out when repository capacity permits. Keep the independent cross-projection conjecture falsifiable and distinguish graph geometry, complex pairing and full Weil-form transport.

No global Weil positivity, RH, or external spectral equivalence is asserted.
