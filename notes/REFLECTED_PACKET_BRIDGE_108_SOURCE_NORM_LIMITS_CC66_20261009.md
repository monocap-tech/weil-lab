# CC66: why the complete trial source alone does not guarantee correlation credit

Read [definitions](../docs/TERMINOLOGY_RPB108_SOURCE_NORM_LIMITS_CC66.md) first.

## Recovered standing and the question tested

Integration remains CC65 b0406fddfa42e6a75da9a40efe2a0ddbe007a6ed.
Read-only Phase Geometry remains NF24
b7fa4461ab4cca2ebc9383ae4b9407c03a580826. No new original arithmetic
producer certificate was available at recovery. CC65's original omitted
source-square budgets remain untested.

The tested question is narrower: would a complete trial source, even as
an exact physical vector rather than just its norm, guarantee that the
CC64 correlation credit is positive once the finite observed rows and
scalar high floor are known? The answer is NO for those reduced data.
This is not a claim that all current source information or the complete
original Weil identities cannot establish the requested bounds.

## Exact cancellation of the unmeasured correlation

Write the high space as H2 plus one observed mode J and one omitted mode U.
Fix C2>kappa I, the observed mixed row k, measured trial-source u, observed
trial-source coordinate v, and nonzero omitted trial-source coordinate w.
The entire source r=(u,v,w) is FIXED. Define

    z_obs=(C2-kappa I)u+k* v,
    ell=-z_obs*/w,
    K_t=[k;t ell],
    D_t=kappa I+K_t(C2-kappa I)^-1 K_t*,
    C_t=[[C2,K_t*],[K_t,D_t]].

Every C_t>=kappa I by square completion. The corrected correlation is

    zbar_t=(1-t) z_obs.

At t=1 it vanishes exactly even though r is unchanged and nonzero.
Indeed the least completion gives

    C_1 r=kappa r,
    <r,C_1^-1 r>=||r||²/kappa,
    correlation credit=0.

The observed finite block remains fixed: C2, k and the J diagonal
kappa+k(C2-kappa I)^-1 k* are independent of t. Changes occur in omitted
high source rows and their high form, not in the complete trial source.
Thus no strictly positive credit lower bound follows from this reduced
packet in general. The coarse majorant is attained, not merely approached.

Fixing the entire original source action on all measured high functions
would rule out this freedom; so would additional original arithmetic
restrictions. That is precisely why complete G*G and G*r are useful
new inputs. A full source norm by itself does not supply their phase
correlation. This does not prove that the three-source Gram is a uniquely
necessary route: a certified form-dual or stronger operator estimate
could also resolve the response.

## Same complete source, same finite block, three full signs

The [exact Fraction validator](../scripts/validate_source_norm_limits_cc66.py)
uses C2=diag(3,4), k=(1/3,1/5), kappa=207/1000,
u=(1/1000,-1/500), v=1 and w=1/2. It fixes the retained energy q to the
exact reaction at t=0 and forms the ORIGINAL unshifted full matrices

    Q_t=[[q,r*],[r,C_t]].

At t=-1 the original full form is strictly positive. At t=0 its Schur
complement is zero and the full matrix has a genuine null. At t=1 the
Schur complement is strictly negative. Their complete retained source
column (q,r), complete trial-source norm, measured C2, whole finite native
block on retained+H2+J and exact high floor are identical.
The true response differs because the unmeasured high source geometry differs.

Every response is evaluated exactly and equals the CC64 majorant for its
own complete high-source data. At the cancellation completion the coarse
majorant is exactly attained. None of these matrices is identified with
the actual NF24 arithmetic; they are estimator controls only.

## Near-critical and positive-level checks

Two additional exact scale families epsilon=1e-18 and1e-16 replace
r by epsilon r and q by epsilon² q. Each retains the same fixed-source
and fixed-observed-block property across its three signs. The source
square / original retained energy ratio is unchanged. This shows that
the insufficiency does not disappear merely because the positive trial
energy is extremely small. The general construction works for every
nonzero epsilon, so there is no scale threshold asserted here.

Three matrices Q0+mu I on the WHOLE physical mass have genuine positive
ground levels mu=1e-40,1/100,1/20. The original matrices have no null;
subtracting the whole level produces Q0's null. Subtracting that level
only on the retained block does not create this null. These controls
prevent positive eigenlevels from being mislabeled as contact.

[Validation](data/RPB108_SOURCE_NORM_LIMITS_CC66_VALIDATION_20261009.json)
passes three fixed-source crossings, six scaled crossings, three genuine
positive ground levels, exact high-floor square completion, fixed finite
block checks and attained inverse responses.

## Concrete arithmetic consequence and scope

If a rigorous complete source norm passes P<kappa Q(p), it already
certifies the directional sign. If it fails, computing P more accurately
cannot itself establish a positive CC64 credit. The added source-aligned
information must bound

    zbar*V^-1 zbar > P-kappa Q(p)

with all enclosure errors paid. Alternatively, one can directly certify
a rational combined source as in CC65 or improve the true high response
through a stronger arithmetic operator estimate.

CC65 has published such a combined polynomial and a strict omitted-source
budget for each parity. Its observed gain is certified; the remaining
complete omitted-source norm is still unbounded. No native failure,
success, source-phase cancellation, actual null, or crossing is inferred
from the abstract controls or from NF24's numerical diagnostics.

This milestone precisely limits a REDUCED directional input set. It
does not prove nonimplication from all finite native records, from all
Weil identities, or from future complete three-source arithmetic.
Original whole-domain anchor21/20 and CC62 E2+F112 gap1/100 remain.
Whole53/50 positivity, cap-uniform leakage, defect-relative collective
critical frame, actual null exclusion, RH/F4, transport and Lean remain
open. Historical wording and paused fronts are preserved.
