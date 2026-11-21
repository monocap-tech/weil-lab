# Weil-Lab — CP034: first genuine original Zeta compiler diagnostics and narrow correction

**Status:** actual Lean v4.35 kernel proof **PENDING** until a new real run passes. CP034 is a narrowly scoped compiler repair stacked on CP033 draft #855, then CP032 #854. The original NF/IV/PI source and protected numerical frontier are preserved.

## Observed two distinct original compiler obstructions

The immutable original-Zeta compiler is no longer hypothetical.

- Run 44913102413 failed at the compiler's very first import: `unknown module prefix 'Zeta'`. That was an insufficient Lake dependency build, **not a source theorem error**.
- CP033 repaired the environment by adding the CP032 module as a **temporary runner-local Lake lean_lib** and calling `lake build CP032OriginalTermSplit`, with pinned original Lean v4.35, original Zeta source SHA `c06b4e13d9c847e50a32c3d738271cbad62ae9f3`, and restored Mathlib cache. Runs 44913303488 and 44913320139 reached the actual original source proof elaborator.
- The first genuine source failure in run 44913320139 was: `CP032OriginalTermSplit.lean:36:37: unexpected token '!'; expected ')', ',' or ':'`. The next error was `line 47: Tactic rfl failed`, for the original source approximant decomposition. Because the malformed Bernoulli term contaminated the source definition, the failed build's `#print axioms` transcript explicitly included `sorryAx` for the decomposition theorem. **It was NOT a certified proof.**
- The remaining generic finite-sum interval theorem, original n=1 Dirichlet identity, and exact n=1 real/imag scalar cells emitted standard-only axiom reports in that same FAILED build transcript. The overall module failed and produced no accepted strict four-theorem kernel receipt. Those individual `#print` reports do not constitute independent accepted kernel certificates without the audit.

## Precise CP034 source repair

The original published Euler-Maclaurin `zetaApproximant` uses Bernoulli coefficient `B_(2k)/(2k)!`. The reparsed source spells its denominator as `Nat.factorial (2*k)` explicitly, avoiding a Lean 4.35 notation/parser failure while preserving the original factorial expression and source identity. All four proof candidates are unchanged except that single mathematical normalization / source comment. The exact source Git blob is frozen to `75024762ea2f9fff12f1d6205af652ce9d21f747`.

If the second `rfl` error persists after the denominator syntax repair, that is a genuine remaining source-identity obligation: DO NOT hide it with `sorry` or a trusted Python receipt. Repair the first actual compiler diagnostic in a new isolated change instead.

## Exact strict axiom audit correction

The CP033 receipt parser incorrectly assumed `#print axioms` lines have no Lean `info: file:line:column:` prefix and no line wrapping. The actual run showed both prefix and multiple lines. CP034 changes the parser to recognize exactly the four expected original theorem names with unique axiom reports, tolerate prefix/wrap, and still prohibit all nonstandard axioms (especially `sorryAx`). It adds a cheap synthetic four-positive/four-negative parser test to the source-only stage. **A source-only parser test is NOT kernel acceptance.**

The only acceptable kernel receipt requires the original v4.35 .olean, nonempty real build and axiom logs without errors, exactly four genuine theorem dependencies, and only `propext`, `Classical.choice` and `Quot.sound` or no axioms.

## Controlled CI / next payment

CP034 modifies the original source module, one strict gate and its own narrowly path-scoped one-leaf workflow, plus this document. No change to shared Lake registry or upstream Zeta/Mathlib, no numerical JSON axioms, no NF/IV modifications. The PR event can run only the CP033 single leaf plus any preexisting **exact source-dependent** filters; source-scoped 37-workflow inventory was checked in CP032/33.

A passing run would establish the exact 263-term original decomposition, generic finite-sum interval transport and n=1 complex term identity + its two exact scalar cells at both heights. These are STILL NOT the other 524 complex term bounds, theta phase bounds, CP029 Borwein 11-pointwise kernel receipts, CP026–28/30 full Lean chain, unconditional narrow ζ zero, ordinal 53, normalized signed Weil/spectral equivalence, global Weil positivity, or RH. No NF gate promotion is authorized.
