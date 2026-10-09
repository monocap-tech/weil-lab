# RPB108 — DNE20: physical response-plane positivity with all high modes

Definitions: [DNE20 terminology](../docs/TERMINOLOGY_RPB108_DNE20_RESPONSE_PLANE.md).
Parent DNE19: 2986f3d75697bfc7f6da14bd351deb1b54b6adec.
Read-only Phase head: 2c64055c00350a7b91ead62453b085cd3408da66 (NF30).
Read-only Coupled head: 433c32598895a6c23a4be303496939011c59017b (CC73).
Only research/rpb108-direct-null-exclusion is written.

## Result

For the original form at a=53/50, the four-dimensional retained response
plane Z4=span(x_even,w_even,x_odd,w_odd), together with the ENTIRE F112
high complement, satisfies

    Q(h) >= (4/10^35) ||h||^2,   h in Z4+F112.

Every retained mixture in that plane and every high correction are
included. An actual original null whose retained component lies in Z4
is excluded. The proof uses the DNE17 high floor kappa=11/25 and
authenticated complete signed source/native intervals from NF29/NF30.

The stronger floor also repairs the even NF29 two-high response block:
its determinant is positive. Thus the expanded NF30 correction is not
needed to make THIS restricted plane positive at the new floor, though
it improves the bound substantially.

| Lift family | Even full physical gap, strict lower | Odd full physical gap, strict lower |
| --- | ---: | ---: |
| NF29 two-high response at floor0.44 | 1.30e-35 | 2.02e-31 |
| NF30 expanded even response at floor0.44 | 4.76e-35 | unchanged NF29 odd |
| NF30 even / NF29 odd at old floor0.207 | 3.10e-36 | 6.50e-32 |

The selected common bound before rounding down is approximately
4.7669147828e-35. The certified rational guard is 4e-35. Shortened
display numbers are not proof inputs.

## Paid collective sign and physical mass

Within each parity let T=(v,t), retained(T)=(x,w), R=P_F L_original T.
The inherited complete source Gram is Gamma=R*R and native lift energy
is Q2. Since the entire high form C>=kappa I,

    S=Q2-R*C^-1 R >= U=Q2-Gamma/kappa.

Outward rational intervals enclose ALL entries of U, including the
signed mixed term. If A,D are lower diagonal bounds and B is an upper
bound on the absolute mixed entry, AD-B^2 is a determinant lower bound.
All three new-floor blocks pass this joint test. No diagonal-only
inference, truncated high inverse, or sign identification of the true
inverse covariance is used.

For even NF29 the paid diagonal lower bounds are approximately
4.7776683793e-35 and1.0119710613e-38. Its mixed absolute upper bound is
5.9294916679e-37 and determinant lower bound1.3189749966e-73.
This settles the previously failed restricted estimator after changing
the high floor; NF29/CC73's historical old-floor rejection stays correct.

The retained mass is M=diag(mx,mw), checked directly from exact rational
coefficients. mx>0, mw>0, and x*w=0. The retained response masses are
approximately1.47672048e-11 even and3.12544958e-10 odd. Treating them as
unit coordinate masses would lose the physical meaning of the result.

The inverse-trace estimate for the generalized physical matrix gives

    mu >= det(U)_lower/(U11_upper mx+U00_upper mw).

All inverse uncertainty is covered by these outward bounds. The chosen
high-lift norm for the seed is conservatively bounded by twice the exact
NF24 H2 compensation square plus twice NF26's high-correction norm bound
squared. For the response, the two NF29 high coefficients give its exact
high mass. NF30 adds a correction supported on disjoint higher modes,
so its squared mass adds exactly. NF29's published lifted mass is checked
against the exact retained and high coefficient masses.

Because M is diagonal, complete source diagonals and lift masses bound

    eta^2=trace(Gamma M^-1)_upper/kappa^2,
    xi^2=trace(H*H M^-1)_upper.

These trace estimates cover all unknown mixed operator norms. With
u=f+C^-1 Rz and Tz=z+Hz, the exact form completion and physical inequality
are

    Q(Tz+f)=S(z)+Q_C(u),
    ||Tz+f||^2 <= (1+4eta^2+4xi^2)||z||^2+2||u||^2.

Thus g=min(mu/(1+4eta^2+4xi^2),kappa/2) is a physical gap on the whole
restriction, not merely a coordinate Schur score. Exact reflection
parity combines the even and odd bounds. This uses the inherited closed
high-form/inverse framework and does not assume RH or an old whole-domain gap.

## Authentication and controls

NF27, NF29, NF30 and NF30's selected correction are copied byte-exact
from the pinned Phase head. Existing DNE15 targets and DNE18 NF26 native
source input are consumed without change. The producer authenticates all
six decoded input SHA-256 values, rechecks exact retained independence,
orthogonality, physical masses, source Gram positivity, native Gram
positivity, and every mixed sufficient sign and gap comparison.

DNE20 is a fresh exact rational CONSUMER of inherited complete-source
certificates. It does not rerun their original expensive source producers
or the raw native archives, and is not a new formal Lean proof. NF30's
trial hash is checked against the actual fixed coefficient artifact.

The new-floor consumer passes52 explicitly counted assertions. The
old-floor control passes49 and reproduces NF29's failed even block and
the NF30/odd successes. A separate validator passes290 rational checks:
three near-critical two-direction determinant crossings,64 nonorthonormal
lift/high-vector tests,9 exact high-response minimizers, three whole-mass
positive-ground-level controls, and the old/new floor comparisons. A
union countercontrol checks that positive restrictions alone cannot be
reported as positivity of their combined span. These algebraic controls
are not original Weil countermodels.

```sh
python3 scripts/certify_dne20_response_plane.py notes/data/RPB108_DNE20_NF27_INPUT_20261009.json notes/data/RPB108_DNE20_NF29_INPUT_20261009.json notes/data/RPB108_DNE20_NF30_INPUT_20261009.json notes/data/RPB108_DNE20_NF30_TRIAL_20261009.json notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64 notes/data/RPB108_DNE18_NF26_INPUT_20261009.json --output /tmp/dne20.json
```

Repeat with `--floor 207/1000` to produce the
old-floor control, then run scripts/validate_dne20_physical_controls.py
with the new output, old output and a validation output path.

## Scope and next assembly

DNE18's retained plane span(e0,e1,x_even,x_odd)+F112 remains positive
with physical gap10^-35. DNE20 certifies a different retained plane.
Exact rational Gram minors verify that adding e0,e1 to Z4 gives six
independent retained directions. Their UNION SPAN IS NOT certified:
the missing low/response couplings must still be paid. No subtraction
of uncovered dimensions across these separate results is valid.

DNE20 itself leaves108 retained dimensions outside Z4. Whole1.06,
the full retained infinite-high Schur matrix, all-cap critical control,
global actual null exclusion, RH/F4, full transport and Lean remain open.
DNE19's raw-background strategy boundary remains correct: changed high
lifts alter the sufficient source matrix and evade that specific barrier.

The next step is either the low/response mixed assembly for the six
directions, or the genuinely collective remaining background complete
source calculation. CC71's frozen finite lifts remain useful inputs but
cannot replace that complete residual Gram. Historical wording and all
other branches are untouched.
