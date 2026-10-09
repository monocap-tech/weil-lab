# RPB108 — DNE25: paid native energy budgets for the complete remainder

Definitions precede use in [DNE25 terminology](../docs/TERMINOLOGY_RPB108_DNE25_SOURCE_BUDGET.md).
Only research/rpb108-direct-null-exclusion is written.
Parent DNE24: 2566cf2c805e8821f79d7aba1ae3d625e92cd37d.
Read-only Phase NF34: f353936b780a4d988ec242a647ab985404f5b69e.
Read-only Coupled CC78: 14dcfae9c91304f2fc8677586605f795f0d06c6e.

## Result

DNE23's complete four-column source in each parity has a certified
strict contraction relative to its ORIGINAL NATIVE ENERGY, with paid
credits c=0.00145 even and c=0.00625 odd. These credits give a concrete
sufficient complete-source test on the remaining 52 columns per parity:

    c B_Y-Gamma_Y > 0,

after native energy orthogonalization against the tested frame. If this
single collective inequality passes in both parities, the original form
is positive on the full aperture 53/50, including every high vector.
No separate signed source crosses between T and Y are then required;
the coherent Gram bound pays them together.

The remaining inequality is NOT certified here. DNE25 certifies the
credits and the sufficiency argument, not the complete remainder Gram,
native orthogonalization or whole-domain sign. The 104 outstanding
retained dimensions remain outstanding.

| Paid quantity | Even | Odd |
| --- | ---: | ---: |
| Complete tested source ratio upper, relative to A | 0.43855 | 0.43375 |
| Certified remainder source budget c | 0.00145 | 0.00625 |
| Largest budget from this row comparison, approximately | 0.00145985135 | 0.00625267610 |
| Alternate trace-comparison budget, approximately | 0.00124288900 | 0.00359643017 |
| Frozen rational remainder ratio allowance r | 0.000725 | 0.003125 |
| Frozen native mixed dual norm allowance epsilon | 29/35200 | 5/1408 |

These are energy-normalized source bounds. They cannot be compared
directly with physical gaps or with a ratio from a different lifted
frame. The much smaller physical DNE23 gap is not used in this criterion.

## Quantitative contraction from the already paid frame

Let A be the original native energy of T=(low,v,t,u), and Gamma_T its
complete original F112 source Gram. DNE23's coherent low-source proof
establishes

    A-Gamma_T/kappa >= L,  kappa=11/25,

where the rational scaling D=diag(1,s1,s2,s3) gives
D L D=diag(alpha,g,g,g)>0. This is a paid coarse SOURCE matrix bound,
not merely a lower bound for the true inverse Schur form. The distinction
is needed to obtain the source contraction below.

DNE25 assembles every entry of the scaled original native matrix
A'=D A D from authenticated intervals: the original low diagonal, three
paid original low/lift pairings, and the complete NF32 native 3-by-3
matrix. No eigenvector identity or sampled energy is used.

For the exact rational mu=c/kappa, it checks four strictly positive
Gershgorin margins for

    diag(alpha,g,g,g)-mu A'.

Thus L>=mu A, and

    Gamma_T <= kappa(A-L) <= (kappa-c)A.

The uncomputed low/other SOURCE crosses have already been paid by the
DNE23 coherent bound. This new comparison needs no raw low-source
covariance guesses. The displayed maximal row budget is kappa divided
by the maximum of the four paid relative row sums. The reported rational
credits lie strictly below it. The trace alternative uses
kappa/trace((D L D)^-1 A') and is weaker in both parities.

## The exact remaining source test

Let W be the exact remaining frame from DNE24. A>0 is already certified.
Define using only the exact ORIGINAL FINITE native pairings

    P=Q(T,W), K0=A^-1 P, Y=W-T K0,
    Q(T,Y)=0, B_Y=Q(W,W)-P*A^-1 P.

This is a change of the finite trial frame. It also changes its retained
components by adding Z8 components, so it does not leave an orthogonal
physical splitting. Nevertheless its projection to E/Z8 is exactly W;
T and Y retain full rank 56 per parity, and adding F112 gives the whole
original form domain. No coordinate basis is treated as orthonormal.

The complete source R_Y is P_F L_original Y, with all endpoint logarithms,
signed pole terms, clipped prime translations and every cross term.
If c B_Y-Gamma_Y>0, then B_Y>0 automatically. Finite dimensionality
gives a ratio r<c with Gamma_Y<=r B_Y. The two source maps satisfy

    ||R z+R_Y a||
    <= sqrt(kappa-c) sqrt(z*A z)+sqrt(r) sqrt(a*B_Y a),

and therefore

    ||R z+R_Y a||^2
    <= (kappa-c+r)(z*A z+a*B_Y a).

The total normalized source ratio is strictly below kappa. Completing
the original infinite high square with C>=kappa I then proves positivity
on T+Y+F112, which is the whole aperture domain. Bounded finite-column
physical masses also convert this to a positive physical gap, but no
numerical gap is claimed without the remaining inputs.

This is a sufficient estimate, not a necessary condition for the true
inverse response or actual-null exclusion. The worst coherent source
alignment saturates the sum of the two marginal energy-normalized
ratios. The real original source crosses may permit a much less
restrictive signed matrix test. DNE24's exact unit-response criterion
remains valid regardless of whether this scalar budget succeeds.

## Implementable frozen rational version

The exact K0 generally has real native entries; it is not a frozen
rational source trial. A producer can instead choose a rational map
hatK0 first and set hatY=W-T hatK0, then certify its ORIGINAL native
energy and complete source. It must pay the remaining native border
E=Q(T,hatY), rather than set it to zero by approximation.

With hatB>0, suppose

    hatGamma<=r hatB,
    ||A^-1/2 E hatB^-1/2||<=epsilon,
    r+kappa epsilon<c.

The original native quadratic is at least (1-epsilon) times the sum
of its two positive diagonal energies. The coherent source payment is
at most (kappa-c+r)/kappa times that sum. Hence the condensed form has
relative energy margin at least

    (c-r)/kappa-epsilon > 0.

The published conservative allocation r=c/2 and epsilon=c/(4 kappa)
leaves margin c/(4 kappa)>0. Thus the rational version does not require
an exact vanishing native border or an actual infinite inverse. It DOES
require the full collective native dual-norm and source-Gram estimates.
It is not a collection of 52 independent diagonal tests.

To form Y or hatY, source producers may combine interval-certified
complete sources of finite polynomial columns with a paid finite native
inverse approximation. The native inverse uncertainty, all mixed finite
energy, and complete source error must be included. Knowing just the
existing successful witnesses or their selected shell is insufficient.
These remaining operations are not performed in DNE25.

## Crossing controls and validation

Two fresh exact consumers give byte-identical certificates and each pass
54 explicitly counted assertions. The separate validator passes 624
rational checks. It independently forms the interval matrix L-mu A
before checking its margins; exact weighted Young tests validate the
same comparison without numerical eigenvalues. Python syntax checks pass.

The coherent source controls use original finite matrices

    [[1,0,3/5],[0,1,s],[3/5,s,1]],

whose native retained energies are orthogonal and whose high block is
one. At s=3/5,4/5,1 their full sign crosses positive, null and negative.
The total source ratios are 18/25,1,34/25. Equality of the source budget
really permits a null: (3/5,4/5,-1) is an exact original null at s=4/5.
The signed source Gram is rank one and its mixed entry is paid.

The same marginal source norms with orthogonal sources instead give a
positive diagonal Schur matrix. This checks why the criterion is sharp
for arbitrary coherent alignment but need not be necessary for a given
original source. The controls also test nonorthogonal coordinate scaling,
441 high-square identities, 147 coherent Cauchy tests, and positive ground levels produced by
adding lambda times the WHOLE physical mass. Subtracting lambda only
from the retained block misses those shifted nulls. These are abstract
matrix controls, not countermodels to the complete Weil identities.

## Current heads and preserved scope

NF34 and CC78 improve the complete sources and physical gaps on the same
NF32 retained probes via a changed expanded high lift. These probes are
already within DNE23's retained Z8. Their other frame's source ratios
cannot be inserted into the DNE25 orthogonalized remainder budget.
DNE25 does not assume their missing mixed borders pass and writes neither
source branch. Their certificates and all prior DNE results are preserved.

The remaining source budget, full 1.06 positivity, exact unit-response
exclusion, all-aperture continuation, global null exclusion, RH/F4,
full transport and Lean remain open. No original complete-source producer
or infinite inverse is rerun. The new computational result is the tested
frame's contraction credit; the whole-domain theorem is conditional.

## Reproduction

From the repository root run:

```sh
python3 scripts/certify_dne25_source_budget.py notes/data/RPB108_DNE23_EIGHT_DIRECTION_CERTIFICATE_20261009.json notes/data/RPB108_DNE18_CC62_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_EVEN_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_ODD_INPUT_20261009.json notes/data/RPB108_DNE24_NULL_REDUCTION_CERTIFICATE_20261009.json --output /tmp/dne25.json
```

Run again for a separate replay output. The validator takes certificate,
replay and validation output as positional arguments. All five inputs
are SHA256 authenticated; custody retains output and script hashes.
