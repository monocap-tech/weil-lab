# Actual exterior coupling: stop the inherited scalar-floor strong-action estimate

A bounded continuation of draft PR #354. The source/deflation span stays at
its accepted 242 original dimensions. Reuse the existing four critical
witnesses as probes of the actual missing complementary coupling. This is a
method diagnostic, not another source-positivity or dimension campaign.
W-ODD-NEG and original operator realization/domain review remain OPEN.

## GitHub-first custody

Require successful run 40594831624 at
43a2c9e0053a51e9b2a7d9686cdda6724611d016, artifact 12776295683
`original-selected-signed-matrix`, archive SHA256
`89dca44de17d67862c58c1eb9b9bd0ea83dfa3bf7a74730cbbb3f9509052c006`.
Hash THIRTEEN exact retained parent JSONs, including the complete signed
matrix `33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa`.
Replay the accepted finite Schur certificate. Reuse that matrix; do not
recompute its 29,403 upper-triangle entries or any low-frequency quadrature.

Only the existing 968 critical mixed entries and their 4x4 target signed
Gram are refined, using the accepted closed kernel at 3072 bits / 384
Laplace terms. The same clean function tail is 2^-2420. All seven-prime and
true-pole physical cross-checks are retained. The fixed 90-second mixed
producer guard is unchanged. Native radii remain strictly positive rational
bounds; their optional Python float log conversion underflows at this
precision and does not mean zero error.

## Two different four-dimensional coordinate systems

Let P be the EXACT physical orthogonal projection onto J_selected, Q=I-P.
Use the accepted physical frame and exact rational Householder product to
write U=J_selected D Q_H. Its physical Gram is G=U*U and its complete signed
Gram is the accepted M=U*W U. Neither frame is asserted physically orthonormal.

For the existing critical functions F, define the actual physical residuals

    X=G^-1 U*F,    E=F-U X=Q F.

X is an exact defining REAL solve enclosed in Arb balls. It is never
replaced by a rounded projection candidate. The residual Gram
S=E*E is computed by original physical primitives, checked against #352's
physical quotient intervals, and verified positive after normalization.
Physical orthogonality is not signed-energy orthogonality; the coupling is
computed and retained.

Independently choose four exact DYADIC coordinate vectors P_phi inside the
SAME selected span, using the already accepted finite Schur factor and its
matched inverse-action candidate. They give Phi=U P_phi, with complete
signed-energy Gram H_phi=Phi*W Phi in [.99 I,1.01 I]. These are energy
coordinates, not physical unit vectors. They introduce no new original
witness functions or retained source directions. The residual probes E and
the weak source directions Phi are DIFFERENT four-tuples.

## Actual exterior form data, without a strong-action computation

With the newly refined Gamma=J_selected*W F and T=U*W F, compute

    Z=E*W Phi=(T-M X)* P_phi,
    C_E=E*W E=F*W F-T*X-X*T+X*M X.

All quantities use the COMPLETE original signed kernel. The calculation
retains the full 4x4 matrices, not isolated component bounds. The actual
positive exterior form compression obeys C_E>=mu S, where the inherited
GLOBAL exterior floor is

    mu=1/1000-epsilon_selected > .00098.

That inequality is also checked directly on these residual probes. It is
not an inverse compression of the entire indefinite operator W and is not
a transferred inverse estimate for the old 470-source complement.

## A certified obstruction to the current sufficient estimate

Let C_Q be the positive operator associated with the signed form restricted
to QH. This is the complement's own realization; it is NOT Q W^-1 Q.
The true infinite Schur correction is B* C_Q^-1 B. If B has the strong L2
realization Q W U, then C_Q>=mu I gives the sufficient matrix estimate

    B*B <= mu M.

For any EXACT coefficient vector y and e=E y in QH, the variational identity

    ||Q W phi||^2 >= 2 Re w(e,phi)-||e||^2

bounds strong action from below. Thus the weak form probes alone can
falsify that sufficient estimate, without computing complete strong action.
They do not presume its domain realization has already been audited.

Choose exact dyadic candidate columns Y_L2 for S^-1 Z and retain

    N_low=Z*Y_L2+Y_L2*Z-Y_L2*S Y_L2.

Three signed-energy directions satisfy
N_low[ii] > mu H_phi[ii]. The certified violation factors are approximately
1.52949, 2.98248 and 2.88922. The fourth factor is about .88858. Any compatible
L2 strong-action realization therefore FAILS this particular mu-only
sufficient matrix budget. More accurate integration, more precise strong
residuals, or testing more directions cannot make the same false inequality
true. This does not stop sharper exterior floors, operator/energy-resolved
inverse estimates, or the actual infinite Schur criterion.

## The same probes show why the inverse matters

Use exact dyadic candidate columns Y_C for C_E^-1 Z. The four-probe Galerkin
Schur correction G_E=Z*C_E^-1 Z has lower matrix

    G_low=Z*Y_C+Y_C*Z-Y_C*C_E Y_C.

For R_C=C_E Y_C-Z and a verified coefficient floor gamma_E for C_E,

    G_low <= G_E <= G_low+||R_C||_F^2/gamma_E I.

The native floor follows from the normalized physical residual Gram and
C_E>=mu S. The independent rational replay also proves positivity and a
coefficient floor by interval LDL in the ACTUAL tiny residual coordinates,
then independently recomposes the complete matched residual and inverse
remainder. No forcing is held fixed while an unmatched inverse is changed.

The four-probe correction has source-energy operator norm <.002
(native upper about .00191131). Its individual energy fractions are about
.00035369, .00068599, .00065646 and .00019605. These are actual FINITE-PROBE
inverse-action values, enclosed with a residual remainder, rather than an
isotropic 1/mu overpayment.

CRITICAL SCOPE: G_E is a Galerkin LOWER approximation to the full infinite
Schur correction. An upper bound on G_E is NOT an upper bound on that full
correction. The unprobed complement remains unbounded here. No negative
extension witness is found, but no positivity of an enlarged full source
space or of the infinite operator is inferred.

## Verification and stopping point

Local refinement took about 37 seconds, physical projection/coupling
analysis about 60 seconds, and exact rational replay about 22 seconds.
The analysis has a 150-second guard. The replay checks all 968 new raw
entries and clean analytic tail, recomposes the signed source-energy Gram
from the complete retained M and exact source vectors, independently proves
the 4x4 physical/exterior positive facts by interval LDL, and replays the
variational inequalities and four-probe inverse-action remainder.
Native physical projection and coupling enclosures are separately rebuilt
in GitHub CI. None of these arithmetic checks closes the inherited analytic
realization/domain review.

STOP the inherited mu-only strong-action sufficient estimate. Preserve the
accepted positive finite block and valid global exterior floor. The next
necessary work must strengthen complementary control (for example a sharper
floor or energy-resolved inverse response) and bound the WHOLE remaining
Schur correction above. Do not start another source/dimension campaign or
precision escalation to rescue an estimate already contradicted by exact
actual-coupling witnesses.
