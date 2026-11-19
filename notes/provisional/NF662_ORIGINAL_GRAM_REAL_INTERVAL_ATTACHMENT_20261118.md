# NF662 — complete original 15-source real Gram interval attachment

## Recovered exact repository state

- **NF658 repaired workflow 44434056814: SUCCESS** including its final clean axiom audit. The previous failure was only malformed heredoc newlines; it is now resolved in the isolated repaired workflow.
- **NF659 run 44430374282: SUCCESS**, all 225 integer transformed centers, 225 integer transformed radius bounds, exact 15 dominance margins, generic interval congruence and symmetric off-diagonal lemmas, standard axioms only.
- **NF661 run 44435792632:** the first stage `ActualZetaOriginalPhysicalGramCoercivityClosure` compiled successfully, including literal original physical source indices and quantitative surjective-basis coercivity theorem. The job as a whole failed in its second stage because the prior NF660 finite-dominance module retained a single unsolved multiplication-associativity goal at line 70. That specific goal is repaired in the NF662 branch with `simp [pow_two] <;> ring`. Fresh Lean acceptance of NF660 is still pending.
- NF660 initial run 44433932382 failed three elaboration goals; two were repaired in NF661 and the remaining third in NF662. Do not mark NF660 coercivity closed until the new compiler run passes.

## NF662 new source-independent real mathematics

`ActualZetaOriginalPhysicalGramRealIntervalTransport.lean` proposes:

1. A general theorem: symmetric real H and symmetric real center/radius C/E turn certified **lower-triangular** enclosures into **all** real entry enclosures.
2. Specialization to the genuine `neutralNF661PhysicalH` integral-defined 15-generator matrix, using already accepted NF606/NF661 physical symmetry.
3. Definitions of the actual real preconditioned Gram matrix `B=K H_I Kᵀ`, transformed real centers and propagated absolute-value radii.
4. A source-independent theorem that every actual transformed real entry lies in the propagated real ball using previously accepted `neutralNF659CongruenceEntry_bound`. It does not substitute the numerical centers for the original actual H.

All new proofs are pending compiler acceptance.

## Authentic physical entry bank

`PhysicalPilots.lean` defines the compact 64-digit rational ball directly by reading the existing NF658 certified K/C/E integer arrays. Pilot proofs attach:
- actual original oscillator H(0,0);
- actual original pole cross term H(241,0);
- actual original pole diagonal H(241,241);
- symmetric reversed upper pole cross entry H(0,241);
- exact full compact ball symmetry.

`scripts/emit_nf662_original_real_intervals.py` emits 15 bounded real-entry proof rows and a complete module:
- **120** physical lower-triangular compact contains theorems, each referring directly to its original NF658 accepted `nf658H*_Contains` result;
- **105** upper-triangular real contains theorems transported via original matrix and compact ball symmetry;
- **225** total genuine original real physical interval propositions, with no newly assumed real integrals;
- a terminal `nf662AllOriginalTransformedRealEnclosed` theorem connecting the original H-integral matrix through the accepted generic real double sum to all transformed real center/radius sums.

The CI workflow rehydrates pinned NF631/NF648/NF621 proof sources, independently regenerates NF657 compact data and NF658 original source intervals, builds pilot entries, builds rows 0/7/14, builds the complete real 225 entries, then audits standard axiom dependencies.

All NF662 newly generated modules and real-attachment theorems are **Lean pending**. A successful external generator or source inspection is not equivalent to a kernel PASS.

## Exact remaining endpoint after NF662

Even if all NF662 modules compile, there is still the nontrivial equality of its real transformed center/radius double sums with the **already Lean-certified NF659 integer arrays divided by S^3 (S=10^64)**. From that, use NF660's real diagonal dominance theorem, literal 15 margins and `m_int*10^60>S*kn`, explicit lower-unit-triangular preconditioner surjectivity, and Frobenius norm inequality to prove:

`∀ x : Fin 15 → ℝ, (10^-60 : ℝ)*∑ i,x i^2 ≤ ∑ i,∑ j, neutralNF661PhysicalH i j*x i*x j`.

This exact original 15-source physical theorem remains OPEN. Full 242 physical block, global signed Weil positivity, RH remain OPEN. Draft only, no main merge.
