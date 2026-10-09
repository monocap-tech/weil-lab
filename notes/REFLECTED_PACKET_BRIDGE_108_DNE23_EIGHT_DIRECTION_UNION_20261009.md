# RPB108 — DNE23: coherent eight-direction union with all high modes

Definitions: [DNE23 terminology](../docs/TERMINOLOGY_RPB108_DNE23_EIGHT_DIRECTION_UNION.md).
Parent DNE22:a88bc029b48a1de345816605d29ca4d3ba0c08f9.
Read-only Phase NF33:6aea8f9a887db70fc56bfa6de6af691d9a8997f6.
Read-only Coupled CC76:938913512b851edfe14eb41fec23b5a7c472351c.
Only research/rpb108-direct-null-exclusion is written.

## Result

The missing mixed union from DNE21/DNE22 now passes. The original form
at a=53/50 satisfies

    Q(h) >= 10^-36 ||h||^2,  h in Z8+F112,
    Z8=span(e0,e1,x_even,w_even,u_even,x_odd,w_odd,u_odd).

Every combination of all EIGHT retained directions and every original
infinite high correction is included. An actual original null whose
retained component lies in Z8 is excluded. There are104 retained
dimensions outside the certified plane. The lower common gap reflects
the larger mixed restriction; all prior restricted gaps stay valid.

| Certified quantity | Even | Odd |
| --- | ---: | ---: |
| Fresh original low/probe pairing, approximately | -1.11768629e-22 | -7.73691316e-20 |
| Joint low-coordinate lower bound alpha | >0.00292338 | >0.00684561 |
| Full physical gap | >1.97e-36 | >1.48e-32 |
| Reported physical gap guard | 1e-36 | 1e-32 |

These are outward computational certificates combined with inherited
analytic source and closed-form high-inverse theorems, not Lean proofs,
actual inverse evaluations, whole-aperture positivity or RH.

## Fresh original unsquared pairings

The low mode's entire original source is reconstructed using the exact
endpoint logarithm, singular harmonic action, regular kernel Taylor
polynomial and signed pole. All six prime powers2,3,4,5,7,8 and both
orientations are included on the seven positive-half cells. Reflection
parity doubles these integrals. No numerical quadrature, sampled endpoint,
eigenvector equation or raw-native entry guess is used.

The fixed probe's exact NF32 rational coefficients are expanded in the
normalized physical Legendre basis. Each source/probe integral uses
outward polynomial and endpoint-log primitives. The complete low-mode
diagonal is also freshly evaluated and overlaps the independent CC62
original native low energy interval in both parities.

The literal frozen DNE16 source engine is copied byte-exact. The wrapper
executes its prefix through the make_u definition, then performs the new
unsquared experiment; the old three-source DNE16 experiment is not run.
Targets, probe and low native input hashes are authenticated before use.

For regular order N, the inherited analytic bound is

    delta_N=(550/19)(106/125)^N,
    low_source_error <= 2a delta_N+3e-99.

The pole64 tail is included in the second term. Constants, normalized
basis and polynomial arithmetic are enclosed by directed Decimal
intervals. Pairing the source error with the exact probe pays the physical
probe norm bound1.001. The primary600-digit/N360 source error is below
1.025e-24; replay620-digit/N400 lowers it below1.401e-27. The entire
replay pairing intervals nest inside the primary intervals, and both
diagonal checks overlap CC62. The approximate central values are display
only; all exact endpoints are preserved.

## The source crosses are paid together

Let T3=(v,t,u), with NF30 even and NF29 odd response lifts. NF32's
complete original source Gram Gamma3 and native energy give

    V=Q(T3,T3)-Gamma3/kappa, kappa=11/25.

DNE22 already certifies V>0. A NEW paid rational congruence/Gershgorin
test also establishes V-Gamma3>0 in each parity. Thus Gamma3<=V on
this complete three-column family.

Let r0=P_F L e_j and g0=<r0,P_F L T3>. Source Cauchy-Schwarz now gives

    |g0 z|^2 <= P0 z*Gamma3 z <= P0 z*V z.

This is the arithmetic correlation that avoids treating the three
unknown low-source crosses as independent worst-case numbers. No actual
source-cross sign is assumed. The Gram domination is certified on the
specific family, not asserted globally or uniformly across aperture caps.

For the native low row p, use NF31's first two paid coordinates and
the fresh third pairing. The prior congruence V>=g diag(s_i^-2) implies

    ||p||_(V^-1)^2 <= sum_i s_i^2 |p_i|_upper^2/g.

Both native and source rows are therefore measured in the SAME V norm:
|[p-g0/kappa]z|<=M sqrt(z*V z), where
M=sqrt(native_dual_upper)+sqrt(P0_upper)/kappa is enclosed outward.
Let A=Q(e_j,e_j)_lower-P0_upper/kappa. Young's inequality with theta=1/10
gives the complete joint lower form

    U4 >= diag(alpha,theta V),
    alpha=A-M^2/(1-theta)>0.

This is a bound for the single complete four-column source matrix.
It does not splice independently condensed actual Schur entries, and
does not replace a signed raw covariance by a true inverse covariance.

## Physical norm and all high vectors

For T4=(e_j,v,t,u), original high square completion at C>=kappa I yields
an energy lower bound alpha|z0|^2+theta g sum_(i>0)|zi|^2/si^2 plus
kappa times the squared completed high norm. The physical column bound
b_i>=||T_i||+||P_F L T_i||/kappa uses the paid low, seed, response and
probe masses; no retained coordinate is assumed orthonormal.

Weighted Cauchy supplies

    physical_gap >= [b0^2/alpha+sum_(i>0) si^2 bi^2/(theta g)+1/kappa]^-1.

The resulting full-high bounds are approximately1.9703025864e-36 even
and1.4899264855e-32 odd. Exact reflection parity gives the common10^-36
guard and includes arbitrary combinations across both parities.

## Validation, reproduction and custody

There are four fresh outward unsquared source runs: two parities at each
precision/order. Both joint consumers pass19 explicitly counted assertions.
The separate validator passes2628 rational checks: pairing nesting and
original diagonal overlaps, joint replay bounds,648 coherent-source
retained tests,1296 nonorthogonal physical/high-completion tests, three
genuine positive/null/negative crossings and three whole-mass positive
ground-level controls. These controls are not actual Weil countermodels.
The four scripts, including the frozen engine, pass syntax compilation.

NF31, CC62, NF32 and DNE22 full source/native certificates are authenticated
inherited inputs. Their original expensive complete-source producers
are not rerun here. The new low/probe pairing producers ARE freshly run,
including the original signed physical source and paid analytic tails.
All source and output hashes are retained in custody.

```sh
python3 scripts/certify_dne23_low_probe_pairing.py even notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64 notes/data/RPB108_DNE22_NF32_TRIAL_20261009.json notes/data/RPB108_DNE18_CC62_INPUT_20261009.json --output /tmp/dne23_even.json
```

Run the odd analogue. For replay set DNE16_PRECISION=620 and
DNE16_ORDER=400. These environment names belong to the frozen source
engine; primary defaults are600/360. The joint consumer takes the
existing DNE21 encoded NF31 input, DNE18 CC62 input, DNE22 even/odd NF32
inputs, DNE22 certificate, and the two new pairing files, then --output.
Its replay uses `--digits 200` and the replay pairings.
The validator takes both joint outputs, the two primary pairings, the
two replay pairings and a validation output path.

## Remaining obligation

This closes the eight-direction mixed union flagged in DNE22. The
complete remaining background source Gram and collective sign are still
missing. CC76 provides an exact shared finite lift on all remaining
directions; NF33 provides complete sources of its selected witnesses.
Tiny selected-shell coordinates and finite graph positivity do not
bound its complete residual source or establish its collective sign.
DNE22's unchanged raw-background loading rejection remains valid.

Whole1.06 positivity, complete retained infinite-high Schur sign,
all-aperture continuation, global actual null exclusion, RH/F4,
full transport and Lean remain open. Historical text and all other
branches are untouched.
