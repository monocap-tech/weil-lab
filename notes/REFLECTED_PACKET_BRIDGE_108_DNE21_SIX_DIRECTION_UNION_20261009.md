# RPB108 — DNE21: six-direction mixed union with all high modes

Definitions: [DNE21 terminology](../docs/TERMINOLOGY_RPB108_DNE21_SIX_DIRECTION_UNION.md).
Parent DNE20:829189a69455067692b337282b1cf94a99f1f3ed.
Read-only Phase head:24aa3d5ff6e193f5865a3c9cdb9eeb61a6d29f1d (NF31).
Read-only Coupled head:433c32598895a6c23a4be303496939011c59017b (CC73).
Only the DNE branch is written.

## Result

The mixed union of the DNE18 and DNE20 retained planes is now certified:

    Q(h) >= 10^-35 ||h||^2,   h in Z6+F112,
    Z6=span(e0,e1,x_even,w_even,x_odd,w_odd).

All six retained mixtures and EVERY original high correction are included.
The exact retained Gram minors inherited and authenticated from DNE20
prove dimension six. An actual original null with retained component
in Z6 is excluded. There are106 retained dimensions outside this plane.

| Paid quantity | Even | Odd |
| --- | ---: | ---: |
| Rational congruence scales | (5,10^17,10^18) | (3,10^15,2*10^16) |
| Smallest positive scaled margin, approximately | 0.1396384522 | 0.0110793900 |
| Full physical gap, approximately | 1.3688702284e-35 | 1.0861080914e-32 |
| Certified physical gap guard | 1e-35 | 1e-32 |

The common reported guard is10^-35. These are physical norm bounds on
infinite-dimensional restrictions, not finite truncation scores.

## Missing mixed entries supplied by NF31

NF31 publishes the original retained source-coordinate intervals for
NF26's seed lift v and the successful response lift t. For even t use
NF30's expanded correction; for odd t use NF29's two-high correction.
The first coordinate is its pairing with e0 or e1. Enlarge each interval
by NF31's source_coordinate_reconstruction_error_bounds entry. This
pays only the appropriate small-correction physical source error, with
native coordinate uncertainty already present in the published interval.

The resulting central native pairings are approximately

    even: Q(e0,v)=-3.53107728e-21, Q(e0,t)=-1.39476067e-21;
    odd:  Q(e1,v)= 1.19644273e-18, Q(e1,t)= 1.16977665e-18.

The seed pairing intervals overlap DNE18's independently paid native
pairing ledger. The response pairings are new inputs from NF31; no raw
native matrix is invented or inferred from separate positivity results.

## Complete-source lower form

For T=(e_j,v,t), the true retained Schur form is

    S=Q_T-R* C^-1 R >= U_T=Q_T-Gamma_T/kappa,
    R=P_F L_original T, Gamma_T=R*R, C>=kappa I.

CC62 supplies the complete low source square P0 and low native energy.
NF29/NF30 supply the complete seed/response Gram and native energy,
including their SIGNED mixed entries. The new two raw source crosses
obey |Gamma_0i| <= sqrt(P0 Gamma_ii). Outward rational square-root bounds
therefore enclose the missing entries of U_T. No unknown true inverse
covariance is treated as a known signed source covariance.

Every matrix consistent with these intervals has positive fixed-rational
congruence margins. If D=diag(s_i), the proof yields

    U_T >= g diag(s_i^-2),
    g=min_i[s_i^2 U_ii_lower-sum_(j!=i) s_i s_j |U_ij|_upper]>0.

This is the JOINT sufficient form for all three retained coordinates
per parity. It does not splice together independent actual Schur entries.
The same entire F112 complement is eliminated throughout.

## Physical norm conversion

Write u=f+C^-1 Rz. Exact square completion gives

    Q(Tz+f)>=g sum_i |z_i|^2/s_i^2+kappa ||u||^2.

The low lift has norm1, the seed lift norm is conservatively bounded by
1.01, and the response lift norm is bounded from its exact retained and
high coefficient masses authenticated in DNE20. Complete source diagonal
bounds give b_i >= ||T_i||+||R_i||/kappa. Hence

    ||Tz+f|| <= sum_i b_i |z_i|+||u||,
    gap >= [sum_i s_i^2 b_i^2/g+1/kappa]^-1.

This weighted Cauchy estimate pays NONORTHOGONAL physical retained
coordinates and the exact full high completion. No numerical eigenvalue,
sampled endpoint, finite high inverse, or coordinate norm is a proof input.

## Custody and validation

The lossless encoded NF31 certificate is copied byte-exact from the
pinned Phase head. Its decoded SHA256 is
ee5c3ebab7fe2d015ff92145b5c69b72630d90cb6306530e8bd8769469e21557.
The consumer authenticates this and all five other inputs: existing
DNE18 CC62, DNE20 NF29/NF30, DNE20 gap certificate, and DNE18 gap
certificate. NF31's own input hashes are checked against the selected
lift certificates. Complete source/native producers and raw archives
are inherited dependencies, not freshly replayed here.

Primary160-digit and replay200-digit rational square-root enclosures
each pass28 explicitly counted assertions. A separate validator passes
805 rational checks, including interval nesting and stronger replay
margins/gaps. Three retained-coordinate controls cross a genuine full
matrix null while ALL two-coordinate restrictions stay positive. There
are256 nonorthogonal lifted/high-vector completion tests and three
whole-mass positive-ground-level controls. These algebraic controls are
not countermodels to complete original Weil identities. Both scripts
pass syntax compilation.

```sh
python3 scripts/certify_dne21_six_direction_union.py notes/data/RPB108_DNE21_NF31_INPUT_20261009.json.gz.b64 notes/data/RPB108_DNE18_CC62_INPUT_20261009.json notes/data/RPB108_DNE20_NF29_INPUT_20261009.json notes/data/RPB108_DNE20_NF30_INPUT_20261009.json notes/data/RPB108_DNE20_RESPONSE_PLANE_CERTIFICATE_20261009.json notes/data/RPB108_DNE18_MIXED_CERTIFICATE_20261009.json --output /tmp/dne21.json
```

Repeat with `--digits 200` for the replay, then run
scripts/validate_dne21_union_controls.py with the primary, replay and
validation output paths.

## Remaining obligation

This closes the missing mixed union flagged in DNE18/DNE20. It does not
close the complete112-dimensional retained Schur matrix. NF31's finite
remaining-background positivity and reaction are useful but cannot be
subtracted separately from this infinite-high restricted gap. The
remaining complete source Gram and its signed coupling to the selected
family still require a justified joint treatment or sharper response bound.

Whole1.06 positivity, all-cap continuation, global actual null exclusion,
RH/F4, full transport and Lean closure remain open. The prior restrictions
and DNE19 strategy boundary remain valid. Historical wording and all
other branches are untouched.
