# Correlated endpoint-basis replay: fixed interval-model ceiling

Inputs are three accepted GitHub artifacts, pinned by run/source/archive
and exact JSON hashes: repaired 2D run 40260136876, complete mixed run
40267592408, and endpoint preflight run 40269077200. There is no new
frequency integration or change to the original source carrier.

## Preserve covariance before taking interval hulls

The mixed artifact uses r0=xcos+alpha*s, alpha=1.249793. The rational
double-endpoint representative is r1=xcos+a*u+b*s, with
a=1.884803, b=3.707850 and anchor f=u+t*s, g=u-s, t=4096/3013.
The exact coordinate shift is

    r1=r0+c0*f+c1*g,
    c0=(a+b-alpha)/(1+t), c1=a-c0.

Use its exact triangular congruence P, not an independently rounded new
interval for every matrix entry. Assemble the accepted original lowband
plus true physical pole interval matrix in (f,g,r0). Compact endpoints
OUTWARD to denominator 10^15. Diagonal lower endpoints are safe because
any diagonal increase stays PSD after congruence.

There are eight corners for the three original offdiagonal intervals.
For each corner h, transform the WHOLE matrix by P^T h P. This preserves
the covariance that would be lost by intervalizing each transformed entry.

## Joint negative-tail bound and positive high frequencies

The positive high-frequency form is discarded as a WHOLE PSD form.
It is not omitted while claiming bounds for the complete mixed entries.
The remaining original strict negative multiplier tail obeys, for real z,

    negative_tail(z) <= M2*(sum_i beta_i*|z_i|)^2.

Beta_f,beta_g come from the accepted reciprocal-power packet majorants;
beta_r comes from the rational double-endpoint preflight, including its
small 1/xi and 1/xi^2 leakage. Round betas and M2 upward to denominator
10^15.

The squared weighted l1 norm is the maximum of four rank-one quadratic
forms, up to an irrelevant common sign. Thus eight lowband corners times
four sign patterns give 32 matrices

    L = P^T h_corner P - M2*v_sign*v_sign^T.

For every such matrix the 2x2 anchor block is SPD. Compute its EXACT scalar
Schur with the full offdiagonal covariance, rather than a diagonal inverse
cap. If gamma is the minimum of the 32 scalar Schurs, every matrix
L-diag(0,0,gamma) is PSD by completion of the square. Convexity of the
lowband interval box and the pointwise maximum tail bound then give a
valid lower for the complete original form and its scalar physical Schur.
Real matrices control complex coefficients by separating real and
imaginary parts.

## Outcome and stopping rule

The correlated paid lower is approximately -0.00035526172288858027,
substantially tighter than the previous -0.1369083914046525 but still
INCONCLUSIVE about true positivity.

Crucially, set the entire negative-tail charge to ZERO while keeping
these lowband intervals. The minimum eight-corner scalar Schur remains
approximately -0.0002707543650415751. An exact interval-corner matrix
has a negative Schur. Subtracting any PSD negative-tail penalty cannot
make that corner positive.

Therefore this FIXED INTERVAL-BOX LOWER MODEL cannot certify PSD merely
by reducing negative-tail payments, including ideal zero payments.
The corner need not correspond to the actual operator: no original
negative witness or actual negative index is inferred. The bound describes
the information retained by these artifacts, not all correlations of the
original integral.

A further computation must earn new information: tighter lowband joint
enclosures, additional positive high-frequency covariance, or another
valid matched response construction. Do not rerun the same integration
only to sharpen tails, and do not move to another source dimension.

The next structural target remains the normalized 14D SI29 energy response
with its matched forcing and complete original J470 energy projection.
The existing SI11/SM17 supported-inverse alternative remains available
for a limited feasibility audit. No physical-to-energy-dual transport or
full remaining finite/infinite Schur is supplied here.

Inherited original analytic and domain assumptions are unchanged.
W-ODD-NEG, even/CC27/Weil and RH remain OPEN. No canonical acceptance
condition or closure status is changed.
