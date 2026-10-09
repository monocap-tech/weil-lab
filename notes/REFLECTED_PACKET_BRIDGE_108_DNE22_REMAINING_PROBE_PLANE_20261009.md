# RPB108 — DNE22: complete remaining-probe restriction and collective boundary

Definitions: [DNE22 terminology](../docs/TERMINOLOGY_RPB108_DNE22_REMAINING_PROBE_PLANE.md).
Parent DNE21:7542382bcf8cfada44722c9bb832031664ff7c4a.
Read-only Phase NF32:a2e155a631a3a719c2f53ab629c501d0fe105747.
Read-only Coupled CC74:9ed50ac8b568cb9c5a986abd6d6a3a28aac3c9ed.
Only research/rpb108-direct-null-exclusion is modified.

## Result

At a=53/50, the NEW six-dimensional retained probe plane satisfies

    Q(h) >= 10^-35 ||h||^2,  h in Zprobe+F112,
    Zprobe=span(x_even,w_even,u_even,x_odd,w_odd,u_odd).

All retained mixtures in that plane and EVERY original high correction
are included. An actual original null whose retained component lies in
Zprobe is excluded. This is a complete mixed source test, not a collection
of positive diagonal probes or a finite high truncation.

| Certified strict bound | Even | Odd |
| --- | ---: | ---: |
| New probe-plane full physical gap | >1.97e-35 | >1.48e-31 |
| Remaining full-background loading at floor0.44 | >1.35294 | >1.27739 |
| Necessary scalar floor from that remaining high row | >0.59529 | >0.56205 |

The new-floor source test passes on the explicit NF32 probes although
NF32's historical floor0.207 tests correctly rejected them. The entire
unchanged remaining background still defeats the scalar-floor estimator,
even after DNE17's improvement to0.44. Both findings are original
arithmetic consequences of authenticated producer certificates.

## Joint probe-plane sign and physical norm

NF32 supplies the complete original native3-by-3 energy and full
projected3-by-3 source Gram of (v,t,u), including every signed cross.
The selected response lift is NF30 even and NF29 odd. For the original
entire high form C>=kappa I, kappa=11/25,

    S=Q(T,T)-R*C^-1 R >= U=Q(T,T)-Gamma/kappa.

Every interval entry is recomputed with exact Fractions. Fixed rational
congruence scales are (10^17,10^18,10^11) even and
(10^15,2*10^16,10^9) odd. Positive Gershgorin margins certify ALL three
coordinates jointly. The smallest margins are approximately0.2009905671
even and0.1519874194 odd. No sign is assigned to unknown inverse covariance.

Exact rational coefficients independently verify nonzero physical masses
and mutual orthogonality of x,w,u. The source trial hash agrees with
the actual frozen coefficients. DNE20's retained/lift masses are preserved.
The seed lift has norm at most1.01; the response lift mass is paid exactly
from retained/high coefficients; u is an unlifted retained polynomial.

Let D=diag(s_i), g be the positive scaled margin and
b_i >= ||T_i||+||P_F L T_i||/kappa. Exact high square completion and
weighted Cauchy give

    Q(Tz+f)>=g sum_i |z_i|^2/s_i^2+kappa ||f+C^-1 Rz||^2,
    physical_gap >= [sum_i s_i^2 b_i^2/g+1/kappa]^-1.

The resulting bounds are approximately1.9703025864e-35 even and
1.4899264855e-31 odd. Reflection parity supplies the common10^-35 guard.
Every source tail and original mixed convention is inherited from the
authenticated COMPLETE NF32 source certificate, not dropped by this consumer.

## Full remaining-background estimator remains obstructed

CC74 authenticates a single original high-source row on NF31's COMPLETE
54-dimensional remaining background, with its original finite inverse
uncertainty paid. The loading interval was normalized by207/1000.
Keeping the same original native background and row while replacing
the floor by11/25 scales that interval exactly by207/440.

The resulting lower bounds exceed1.35294 even and1.27739 odd. Therefore
the complete unchanged matrix A_T-G*G/kappa cannot be positive definite,
regardless of other uncomputed source rows. A basis change or additional
source precision cannot repair this specified test at the fixed floor.

This is NOT a negative original Weil vector, an actual Schur sign, a
full-Weil nonimplication claim, or a rejection of new high lifts. The
single-row necessary floors0.59529/0.56205 are estimator targets, not
upper bounds on the actual high spectral floor or sufficient full gates.
DNE19's fixed-budget raw-background result concerns its own named family.

## Custody and controls

NF32's two complete source certificates and frozen probe artifact are
copied byte-exact from the pinned Phase head. CC74's native loading
certificate is copied byte-exact from the pinned Coupled head. All four,
the existing DNE20 physical certificate, NF24 seeds and NF27 responses
are SHA256 authenticated before computation. Complete source producers
and raw native archives are inherited dependencies and are NOT replayed here.

Primary160-digit and replay200-digit rational square-root calculations
each pass34 explicitly counted assertions. The separate validator passes
405 checks, including closed-form Sylvester positivity at ALL64 interval
vertices in EACH parity. These vertices exhaust the interval box; the
positive cone is convex. They independently corroborate the all-interval
Gershgorin proof rather than substituting random sampling for it.

Three genuine joint positive/null/negative crossings and three whole-mass
positive-ground-level controls pass. A positive actual block with diagonal
high couplings(1/2,4/5) verifies that a passing probe, failing collective
floor estimate, and positive actual form can coexist. These algebraic
controls are not countermodels to complete original Weil identities.
Both scripts pass syntax compilation.

```sh
python3 scripts/certify_dne22_remaining_probe_plane.py notes/data/RPB108_DNE22_NF32_EVEN_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_ODD_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_TRIAL_20261009.json notes/data/RPB108_DNE22_CC74_LOADING_INPUT_20261009.json notes/data/RPB108_DNE20_RESPONSE_PLANE_CERTIFICATE_20261009.json DECODED_NF24_TARGETS.json notes/data/RPB108_DNE20_NF27_INPUT_20261009.json --output /tmp/dne22.json
```

The decoded target is the exact JSON obtained from the existing DNE15
base64/gzip target artifact; its hash is authenticated. Repeat with
`--digits 200`, then run scripts/validate_dne22_probe_controls.py on
the two outputs and a validation output path.

## Board state and next obligation

DNE21's low/seed/response restriction remains positive. DNE22's
seed/response/probe restriction is a DIFFERENT six-dimensional plane.
Exact positive4-by-4 physical Gram determinants show that the combined
retained span has dimension eight. Its MIXED SIGN IS STILL OPEN:
the original low/probe native pairings and a justified common source
cross bound must be paid before adjoining e0,e1 to the new probe plane.

There are106 retained dimensions outside EACH certified six-dimensional
plane. The separate restrictions cannot be counted as a certified
eight-dimensional restriction or as whole-domain progress by dimension
subtraction alone. The full unlifted background strategy needs changed
joint high lifts, a stronger justified floor, or sharper response control.

Whole1.06 positivity, complete retained infinite-high Schur sign,
all-aperture continuation, global actual null exclusion, RH/F4,
full transport and Lean remain open. Historical wording and all other
branches are untouched.
