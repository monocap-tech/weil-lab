# NF594 — analytic reduction of the finite checker and bounded kernel trials

Stacked on NF593 #624. New Lean proofs and kernel trials are pending.

## Verification and blockers

NF593 run 44146672054 initially queued amid extensive older workflow replays. At the final inspection its cache job 134263583689 had started but the periodic phase step failed; the source recovery job remained queued. No executed cached Lean table or 800-endpoint comparison can be claimed. The NF592 workflow on the NF593 head, run 44146670525 job 134263579147, independently passed the rational ball/rounding, analytic remainders, historical fee arithmetic and rounded exponential recurrence steps again. It reported only one remaining periodic phase cast diagnostic, and the original normalized complex source had two unknown constant-multiplication API diagnostics (the earlier sum and derivative issues are absent). NF594 replaces the cast tactic with explicit Rat.cast_le and uses the pinned Differentiable.const_mul. The new repairs have not yet been checked.

NF588 job 134253594663 completed with graph correction failure: the finite sum of CLMs directly into the closed source subtype lacked AddCommMonoid instance inference, the physical synthesis lacked the explicit basis expansion, and the corrected seed proof timed out. NF594 moves the sum into the ambient product and restricts the codomain to the original closed submodule by finite-sum membership; the physical proof expands the same original basis. The terminal corrected seed timeout may remain. No graph acceptance claimed.

## Analytic reduction of all 400 comparisons

The previously used circle majorant 10^400 was extremely loose. Expose the exact raw NF589 bound without changing the source or the old theorem:
M_raw = 400*10^143*2^13*3^283.
Exact live BigInt arithmetic verifies M_raw <= 10^285 and 10^325 <= 20^250. (The raw majorant itself does not suffice at degree 249.) With the already accepted canonical Cauchy coefficient estimate on radius 20, once the source disc assembly is accepted,
|v_n| <= 10^285*(1/20)^n <= 10^-40 for ALL n>=250.
The frozen ceilings at 250..399 are exactly 1 at scale 10^40. Thus 150 of the 400 finite coefficient inequalities can be discharged analytically; the original finite ceiling table, all 400 terms in the sums, infinite remainder budgets and numerical targets are unchanged. No truncation or substitution of the original source.

New Lean theorem candidates expose the raw bound, isolate the two exact natural number comparisons and casts, transfer the high-degree inequalities, and reduce the terminal collar bounds to only the first 250 rational interval budget checks. The cutoff proof and full-disc/source recurrence dependencies are compiler-pending.

## Kernel blocks

Split the reduced checker into five 50-order obligations [0,49], [50,99], [100,149], [150,199], [200,249]. Each block uses only the necessary cached prefix, not the full 400-order evaluation. A candidate soundness theorem uses NF593 cache/reference equality and joins the five true block Booleans into the reduced budget; analytic Cauchy bounds then pay the remaining 150 terms. Fresh exact BigInt audit of existing NF591 receipt endpoints passed all five blocks, strictly, and all 400 original inequalities; this is a data audit, not new interval reconstruction or execution of the Lean checker.

New focused workflow first attempts the cached executable and 800-endpoint comparison, then independently attempts a first-order kernel proof using decide +kernel (no native_decide) with bounded heartbeat/time budget and prints its axioms. Only if that succeeds does it attempt five separate 50-order kernel decisions, each with a timeout and axiom report. This is an experiment on the actual evaluator, not an assertion that kernel execution scales: proof performance remains unmeasured. No local Lean environment was available. The blocks are defined and connected, not yet proved true in Lean.

Original solve-box custody, canonical recurrence and full source disc assembly, checker proof, terminal correction, full signed Weil coercivity, W_ODD_NEG and RH remain open. No main merge.
