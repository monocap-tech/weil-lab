# RPB108 DNE47: shell-route limit and a finite residual-response gate

Parent DNE46: `61b896309a4c426a9259290b92dbd039a26f96ef`.
Branch `research/rpb108-direct-null-exclusion`. Definitions were registered
before load-bearing computation in
`docs/TERMINOLOGY_RPB108_DNE47_RESPONSE_TRIAL_GATE.md`. Historical certificates
are unchanged.

DNE47 proves that further refinement of the current positive-region shell
route cannot close the remaining even packet direction. It constructs and
certifies three exact physical high trial vectors for a stronger residual
response criterion. **Their original high source correlations have not
been computed.** The actual positivity state remains DNE46's 87 retained
directions plus the infinite high space at floor 647/1000.

## 1. A route-wide ceiling, not just one fixed arch input

DNE45 bounded the fixed old arch input route. DNE46 improved that input and
closed two additional directions. DNE47 now bounds the whole stated shell
mechanism at fixed cutoff 112: b(T)=log T-7/(216 T^2), nonnegative shell
and pole payments, positive-region top cutoff (2 a pi T)^2<112*113, and a
valid global prime norm upper beta.

An independent Machin interval proves pi>314159/100000. Exact arithmetic
proves

    (2*(53/50)*(314159/100000)*(169/10))^2 > 112*113.

Thus every admissible top cutoff has T<169/10. Regardless of its partition,
its certified arch input cannot exceed b(T)<log(169/10), since all its
shell and pole losses are nonnegative. DNE45's authenticated Rayleigh
certificate gives ||P||>2.15889502, so every valid beta exceeds this value.
The best lower floor this route can furnish is consequently strictly below

    log(169/10)_upper - 2.15889502
      = approximately 0.6684186019290278.

The saved exact rational upper is strictly below DNE45's exact lower bound
0.7463624055881617... for the full even packet's scalar threshold. Therefore
neither a finer partition, a top cutoff nearer the positive-region boundary,
a sharper mass envelope under these same rules, nor a better global prime
norm bound can make the full 44-column even comparison positive.

This excludes only the registered fixed-F112 shell/global-norm route.
It does not bound the true high floor from above and does not exclude a
stronger arch estimate outside this mechanism, a correlated/restricted
prime estimate, a different retained cutoff, or inverse-response control.

## 2. Three exact physical high trial vectors

Materialize the authenticated DNE44 even packet Z=(T4*S,X[0:40]). For each
of its three nonconstant tested columns, discard exactly the physical
Legendre coefficients of degrees below 112 and divide the remaining
coefficients by a rational upper bound for their physical norm. These
vectors lie exactly in F112, remain supported polynomials of degree at
most 180, and each has physical norm strictly below one.

The saved exact 3x3 physical Gram has an independently audited rational
positive congruence certificate. Thus the vectors form a genuine
three-dimensional high trial space, rather than three approximate
projections with unknown rank. The certificate preserves exact physical
coefficients, parent column identities, discarded/retained degree boundary,
rational normalizations, exact masses, and the input packet hash.

This certifies geometry only. It does not certify the original native
energy of these new high vectors, their action Grams, or any inverse
response improvement.

## 3. The response calculation that would use this frame

On the original polynomial source-action domain, let L=L_F112>=kI,
k=647/1000; let f=P_F112 L_original Z be the 44 original high source
columns. Use Y for the three high trial columns. Required matrices are:

| Matrix | Size | Meaning | DNE47 standing |
| --- | --- | --- | --- |
| N | 44x44 | Original native packet energy | Already certified |
| G | 44x44 | f* f | Already certified |
| M | 44x3 | f* Y = Z* L_original Y | New original native pairings required |
| A | 3x3 | Y* L Y | New original native pairings required |
| B | 44x3 | f* (L Y) | New projected source correlations required |
| D | 3x3 | (L Y)* (L Y) | New projected source correlations required |

Since Y lies in F112, L Y means the compressed high action P_F112
L_original Y. Its full projected source norm must subtract all 56 same-parity
retained coordinates and pay the complete original analytic source error.
M and A can be evaluated from the three new original source actions against
Z and Y, with all errors paid; they are not inferred from an unmeasured
native block. Directly integrate Y's actions rather than subtracting two
large scaled actions with independently paid errors.

For any exact rational J of size 3x44, set v=YJ and residual r=f-LYJ.
The full matrix identity is

    f* L^(-1) f = M J + J* M* - J* A J + r* L^(-1) r.

Use the established entire infinite high lower floor on the residual:

    r* L^(-1) r <= (G - B J - J* B* + J* D J)/k.

No evaluation of the true inverse is needed for this sufficient upper.
Define E=B-kM and W=D-kA. Then the response credit relative to G/k is
bounded below by

    C_J = (E J + J* E* - J* W J)/k.

Accordingly the load-bearing finite positivity gate is the complete
44x44 interval inequality

    k N - G + E J + J* E* - J* W J > 0.

Every mixed entry must be paid. If W>0, an ideal candidate is J=W^(-1)E*,
with rank-at-most-three credit E W^(-1) E*/k. In computation J can be
proposed numerically and frozen rationally; the final inequality is checked
with exact interval arithmetic. No ideal-inverse identity is substituted
for a paid candidate certificate. If W is singular, the arbitrary-J
criterion still applies; strict W positivity is only needed for that
particular optimizer formula.

This is a finite trial approximation to the ORIGINAL high inverse. It
can improve the response estimate without raising the scalar high floor.
Whether this particular trial space supplies enough credit remains open.

## 4. Cost and countercontrols

The minimal projected source extension for all three trials adds only
44*3+3*4/2 = **138** upper-triangle source correlations to the existing
44-column even Gram. It also requires complete retained projections of
the new actions and their native pairings against Z and Y. These quantities
have not been integrated in DNE47. No old source entry needs reintegration.
For comparison, adding the 12 missing even retained packet columns alone
would require 44*12+12*13/2=606 new upper-triangle source correlations.
These are entry counts, not a promised runtime ratio; polynomial and
native-moment work also matters.

The independent audit verifies the residual identity and credit expansion
in exact rational commuting and noncommuting matrix controls. With k=1,
L=diag(2,5), f=I and Y=e2, the optimized trial gives credit diag(0,4/5).
For N=diag(2,1/2), the old sufficient budget has a negative second direction,
while the corrected budget is diag(1,3/10)>0. For N=diag(2,1/10), the
corrected second direction stays negative. For
N=[[2,1],[1,7/10]], the corrected bottom diagonal is positive but the
full determinant is negative: paying the last direction's diagonal alone
would miss the mixed obstruction. These are algebraic countercontrols,
not original Weil examples or new original positivity claims.

## 5. Validation and current state

The independent audit passes **87 new exact rational checks**. It uses a
longer rational logarithm series, reconstructs Machin's pi interval,
authenticates the inherited passing audits, verifies the route ceiling,
reconstructs all high trial coefficients and masses, pays the physical Gram
congruence, and executes the residual/positive/crossing/mixed controls.
Inherited high and source checks are not counted as newly executed.

Reproduce from the repository root:

```sh
python scripts/certify_dne47_response_trial_gate.py --output notes/data/RPB108_DNE47_RESPONSE_TRIAL_GATE_20261010.json
python scripts/validate_dne47_response_trial_gate.py notes/data/RPB108_DNE47_RESPONSE_TRIAL_GATE_20261010.json --output notes/data/RPB108_DNE47_RESPONSE_TRIAL_VALIDATION_20261010.json
```

**Standing unchanged:** 87 retained directions (43 even,44 odd), original
infinite high floor .647, common physical guard 1e-37, and 25 uncovered
retained dimensions: 24 outside the computed packet and one inside its
even sector. Next response computation has an explicit three-column input
and full mixed-entry gate. No new original source integration, actual
high inverse evaluation, whole-aperture positivity, first-contact exclusion,
RH, or Lean closure is claimed.
