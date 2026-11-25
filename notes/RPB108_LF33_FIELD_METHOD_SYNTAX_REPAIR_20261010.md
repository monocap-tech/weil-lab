# RPB108 LF33 — Field-method syntax repair

## Change

Repair seven field-method applications split immediately after the dot: six
indicator-integrability calls in TrialJump and one constant multiplication in
PoissonMixture. Keep each dot adjacent to its method identifier. The Lean
parser rejects a newline after the dot before its field name. No theorem,
definition or premise changes.

## Validation evidence

LF30 run 38107903216 job 114378203312 and LF32 run 38108592402 job
114379468459 failed in TrialJump on invalid field notation at lines 61 and 82;
those parse failures stopped the relevant proof bodies and downstream modules.
The partition and zero-extension helper declarations produced no diagnostics,
but TrialJump as a module did not compile. Downstream PoissonAction,
PoissonMixture and TruncatedJump remain unchecked. LF33 repairs the repeated
syntax pattern in all affected source locations.

LF28 is the latest complete-root success: commit
`7c658587c3c4f79123de957356b69d7306384140`, run 38107491130,
job 114375973158, including unfinished-declaration rejection. LF33 is
submitted for fresh cumulative kernel checking. No unfinished proof or
project axiom is introduced.

## Next cursor

Resolve subsequent diagnostics, then remove time cutoffs and prove physical
weak/spectral attachment. Numerical enclosures and concrete matrices remain
separate. No new aperture positivity, F4 or RH is claimed.
