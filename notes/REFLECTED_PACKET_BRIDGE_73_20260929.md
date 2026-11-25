# RPB-73 — WD-T40 carrier proof-term elaboration audit

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **PROOF-TERM STATIC PASS / ALL CARRIER PROOF BODIES REDUCED TO DIRECT TARGET-EXPLICIT TERMS OR ONE STANDARD SUPPORT CONTRADICTION / NO METAVARIABLE HOLES, SIMPA DEPENDENCE, OR REWRITE-DRIVEN PROOF STATE REMAINS / NO STATIC PROOF-TERM BLOCKER FOUND / BUILD CERTIFICATION STILL INFRASTRUCTURE-BLOCKED / F-2 REMAINS CLOSED**

## 0. Objective

RPB-71 closed declaration/API-shape risk and RPB-72 closed the implicit typeclass graph.

RPB-73 audits the remaining theorem bodies and parser/elaboration-sensitive proof syntax in the F-1 carrier.

Because no Lean process is available, this is a static elaboration-risk audit rather than a compiler certificate.

## 1. Adapter theorem

The adapter theorem now states its definitional target explicitly:

~~~lean
change d.interface.kExt = d.h_memLp.toLp d.h
exact d.kExt_eq_toLp
~~~

This avoids simplifier or unfolding heuristics.

Disposition: PASS.

## 2. Nonzero transfer

The nonzero transfer now uses equality composition directly:

~~~lean
intro hzero
exact d.interface.kExt_ne ((interface_kExt_eq_l2Mode d).trans hzero)
~~~

Types:

~~~text
interface_kExt_eq_l2Mode d : d.interface.kExt = d.l2Mode
hzero                         : d.l2Mode = 0
kExt_ne                       : d.interface.kExt ≠ 0
~~~

The equality chain therefore lands exactly in the contradiction expected by `kExt_ne`.

No `apply`, `rw`, or simplifier state remains.

Disposition: PASS.

## 3. Support contradiction

The representative theorem is:

~~~lean
by_contra hne
exact hx (d.support_subset hne)
~~~

Pinned mathlib defines:

~~~text
Function.support h = {x | h x ≠ 0}.
~~~

Thus `hne` is definitionally the membership witness required by `support_subset`.

`by_contra` is ordinary Lean tactic syntax and introduces no project-specific elaboration premise.

Disposition: PASS.

## 4. Fourier compatibility proof

The Fourier theorem uses one explicit `change` and then the pinned theorem directly:

~~~lean
change
  𝓕 (d.l2Mode : RealComplexTempered) =
    ((𝓕 d.l2Mode : RealComplexL2) : RealComplexTempered)
exact MeasureTheory.Lp.fourier_toTemperedDistribution_eq d.l2Mode
~~~

RPB-71 already verified the theorem signature and RPB-72 verified every implicit instance.

No rewrite or coercion search beyond the explicitly displayed casts remains in the proof body.

Disposition: PASS.

## 5. Residual-vanishing monotonicity proof

The proof is now a direct theorem application:

~~~lean
exact Distribution.IsVanishingOn.mono
  (s₁ := Set.Ioo (-d.a) d.a)
  (s₂ := Set.Ioo (-c) c)
  (fun _ hx =>
    ⟨lt_trans (neg_lt_neg d.strict) hx.1,
      lt_trans hx.2 d.strict⟩)
  d.residual_vanishes
~~~

Pinned mathlib states `IsVanishingOn.mono` with arguments:

~~~text
hs : s₂ ⊆ s₁
hf : IsVanishingOn f s₁
~~~

and conclusion `IsVanishingOn f s₂`.

The interval inclusion direction is correct:

~~~text
c < a
=> -a < -c
=> (-c,c) ⊆ (-a,a).
~~~

Disposition: PASS.

## 6. Parser-sensitive syntax scan

The carrier source now contains:

~~~text
metavariable proof holes `?_`:     none
`simpa`:                           none
`rw [...]`:                        none
project-specific tactics:          none
ordinary `by_contra`:              one
explicit `change`:                 two
Fourier notation `𝓕`:              pinned/opened by FourierTransform scope
~~~

No unbalanced or unsupported notation was identified.

## 7. Source hardening accumulated through RPB-71–73

The F-1 source now uses:

1. explicit `volume` in the L2 abbreviation;
2. explicit adapter target via `change`;
3. equality composition for nonzero transfer;
4. explicit Fourier coercions before the pinned theorem;
5. explicit `s₁`/`s₂` in residual monotonicity;
6. direct theorem application instead of tactic-state `apply` for residual vanishing.

These edits reduce elaboration freedom without changing mathematical content.

## 8. Static audit matrix

~~~text
DECLARATION/API SHAPES:        PASS  [RPB-71]
TYPECLASS GRAPH:               PASS  [RPB-72]
ADAPTER PROOF TERM:            PASS
NONZERO TRANSFER PROOF TERM:   PASS
SUPPORT CONTRADICTION:         PASS
FOURIER COMPATIBILITY TERM:    PASS
RESIDUAL MONOTONICITY TERM:    PASS
PARSER/NOTATION SCAN:          PASS
~~~

No identified static elaboration blocker remains.

## 9. Remaining uncertainty

The only unresolved F-1 question is actual Lean elaboration/build execution.

Static inspection cannot certify:

- parser behavior in the exact toolchain executable;
- instance search runtime behavior;
- kernel checking;
- hidden import/reducibility behavior exposed only during compilation.

Those require a functioning Lean process.

## 10. RPB-73 determination

~~~math
\boxed{
\textbf{RPB-73 — F-1 HAS PASSED DECLARATION, TYPECLASS, AND PROOF-TERM STATIC AUDITS; NO STATIC SOURCE BLOCKER REMAINS.}
}
~~~

Current state:

~~~text
F-1  SOURCE IMPLEMENTED
     STATIC API PASS
     TYPECLASS STATIC PASS
     PROOF-TERM STATIC PASS
     BUILD CERTIFICATION INFRASTRUCTURE-BLOCKED

F-2  NOT STARTED
~~~

WD-T40 remains LEAN-BLOCKED.

## Next cursor

~~~text
RPB-74 / WD-T40 F-1 STATIC CLOSURE AND BUILD HANDOFF
~~~

The next pass should freeze the audited F-1 source, ensure the deterministic build handoff captures the exact module and trust checks, and classify F-1 as statically exhausted pending a real Lean runner. Do not start F-2.