# RPB-99 — WD-T40 F-4 Gaussian-admissibility bridge build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **GAUSSIAN-ADMISSIBILITY INTERFACE BUILD-CERTIFIED / FIRST EXACT BUILD ATTEMPT GREEN / REPOSITORY-WIDE TRUST SCAN PASSED / ONE NONBLOCKING DEFPROP LINTER WARNING / ACTUAL CUTOFF-GROWTH DISCHARGE STILL OPEN / LOGARITHMIC COERCIVITY NOT STARTED**

## 0. Objective

RPB-98 typed the noncompact moving-Gaussian domain seam explicitly as

~~~lean
RightLimitWeilGaussianAdmissibilityBridge
~~~

without importing any coercivity estimate.

RPB-99 performs only the pinned build certification of that interface.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb99-gaussian-admissibility
~~~

Draft validation PR:

~~~text
#14  Validate RPB-99 Gaussian admissibility bridge
~~~

The validation-only workflow targets exactly:

~~~text
WeilDefect.Morphology.NeutralGaussianAdmissibility
~~~

and is not merged into the research branch.

## 2. Successful build evidence

The first exact validation attempt succeeded:

~~~text
run: 36776782079
job: 110096581102
validation head: 1a22b9ae140d8d56008689113015599b400f2955
~~~

Lean reported:

~~~text
Built WeilDefect.Morphology.NeutralFourierCarrier
Built WeilDefect.Morphology.NeutralWeilMultiplier
Built WeilDefect.Morphology.NeutralWeilResidualCarrier
Built WeilDefect.Morphology.NeutralGaussianSupportGap
Built WeilDefect.Morphology.NeutralGaussianTail
Built WeilDefect.Morphology.NeutralGaussianPairing
Built WeilDefect.Morphology.NeutralGaussianAdmissibility
Build completed successfully (8940 jobs).
~~~

The repository-wide rejection gate for top-level \`axiom\`, \`sorry\`, and
\`admit\` also passed.

No compiler repair was required.

## 3. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralGaussianAdmissibility.lean
~~~

Certified Git blob:

~~~text
a2477a3984957c1754895b533d0b1f2a12f5b4df
~~~

The certificate covers:

~~~lean
RightLimitWeilGaussianAdmissibilityBridge
movingGaussianResidualPairing_eq_weakLeft
gaussianWeakRealization
toCompactWeak
~~~

Thus Lean accepts the exact domain-bridge species:

- existing compact-test EXT-4 realization;
- Schwartz representative of the actual moving Gaussian mode;
- genuine residual pairing integrability;
- genuine pole pairing integrability;
- extended weak identity for that Gaussian mode.

## 4. Linter note

Lean emitted one nonblocking style warning:

~~~text
Definition toCompactWeak is a proposition; use theorem instead of def
~~~

This does not affect kernel checking or semantic content.

RPB-99 leaves the certified source unchanged rather than making a
non-load-bearing stylistic mutation during the build gate.

## 5. What is and is not certified

Certified:

~~~text
Gaussian-admissibility interface TYPE:
    BUILD-CERTIFIED

downstream extraction theorem:
    BUILD-CERTIFIED
~~~

Not certified:

~~~text
existence of an instance of that interface from existing F-2/F-3 fields:
    OPEN
~~~

In particular, RPB-99 does not prove:

- that the moving filtered mode is Schwartz from the current carrier fields;
- cutoff convergence from compactly supported Schwartz tests;
- a whole-line exponential-growth bound for the explicit pole function;
- passage of the compact-test EXT-4 identity to the Gaussian test.

Those are the actual mathematical/domain obligations in the next pass.

## 6. F-4 standing

~~~text
Gaussian-admissibility bridge interface:
    BUILD-CERTIFIED

Gaussian-admissibility cutoff/growth discharge:
    OPEN

logarithmic Gaussian coercivity:
    NOT STARTED

F-5 strip holomorphy:
    CLOSED
~~~

## 7. RPB-99 determination

~~~math
\boxed{
\textbf{RPB-99 — THE F-4 GAUSSIAN-ADMISSIBILITY DOMAIN INTERFACE IS BUILD-CERTIFIED, BUT ITS CUTOFF/GROWTH DISCHARGE REMAINS THE SOLE PRE-COERCIVITY OBLIGATION.}
}
~~~

## Next cursor

~~~text
RPB-100 / WD-T40 F-4 GAUSSIAN-ADMISSIBILITY CUTOFF/GROWTH DISCHARGE
~~~

The next pass should determine and implement the minimal lawful discharge of
the certified interface from the existing carrier plus any explicitly needed
pole-growth data.

Do not begin logarithmic coercivity until that discharge is closed.
