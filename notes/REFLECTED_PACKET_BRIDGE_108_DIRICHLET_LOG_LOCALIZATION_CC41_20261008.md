# RPB108 CC41: actual null operator domain and quantitative critical localization

Date: 2026-10-08 UTC. Parent: 2fe4cdeec21bbf559daeec1f139209bcb2c7f879.
Definitions: [supported logarithmic operator](../docs/TERMINOLOGY_RPB108_DIRICHLET_LOG_LOCALIZATION.md).
Result class: analytic consequence of the complete native bounded remainder;
neither null exclusion nor a defect-relative outward estimate.

## Actual supported operator, with a precise domain distinction

The closed positive form E_log on physical L2[-s,s] defines A_s>=I with
form domain D_s. Its density and closedness follow from the inherited
smooth core and complete logarithmic carrier. R_s is bounded selfadjoint,
with ||R_s||<=r_B. The bounded form perturbation has the physical
selfadjoint realization L_s=A_s+R_s, Dom L_s=Dom A_s.

This uses the ACTUAL archimedean remainder, every active prime translation
and both signed poles. It does not represent full Q by a bounded L2
operator. Nor does it identify A_s with the unrestricted logarithmic
Fourier multiplier applied to a zero extension: the latter can have
additional exterior/boundary distribution behavior. This domain result
is not the earlier spectral source attachment or Green reconstruction.

For an actual nonnegative-contact null, mixed nullity Q_s(h,k)=0 on ALL
supported k in D_s gives

    E_log(h,k)=-<R_s h,k>_2.

The right side is a bounded physical L2 functional. By the definition
of the form-associated operator this proves

    h in Dom A_s, A_s h=-R_s h, L_s h=0,
    ||A_s h||_2<=r_B||h||_2.                           (1)

This sharpens the distributional native null equation only to the
SUPPORTED operator domain. No H1 regularity, pointwise derivative,
global Fourier log-squared norm or nonzero boundary trace follows here.
The concurrent contact report's caution about inferring an unrestricted
physical multiplier domain is preserved with this explicit distinction.

## Quantitative localization for genuine near-critical lifts

Let ||Ph||=1 and Q_s(h,k)=delta<Ph,Pk> on D_s. If M_s is the canonical
positive form operator, set w=M_s h and v=h-delta w. The supported
generalized equation becomes

    E_log(v,k)=-<R_s h,k>_2 for all k in D_s.

Therefore, without assuming h itself has physical operator regularity,

    v in Dom A_s, A_s v=-R_s h,
    ||h-v||_D<=delta U_B,
    ||A_s v||_2<=r_B/c_B.                              (2)

Here ||M_s h||_D<=U_B follows from the COMPLETE P normalization and
M_s<=U_B^2 I, and ||h||_2<=||h||_D<=1/c_B. No bounded physical
representation of the positive source M_s is assumed. Its defect term
is paid in the canonical norm rather than silently promoted to L2.

Let F_(s,Lambda)=1_(Lambda,infinity)(A_s), Lambda>=1. Spectral calculus
on v gives

    ||F_(s,Lambda)v||_D<=r_B/(c_B sqrt(Lambda)),
    ||F_(s,Lambda)v||_2<=r_B/(c_B Lambda).

The spectral projection contracts D_s because it commutes with A_s.
Combining with (2),

    ||F_(s,Lambda)h||_D
        <=r_B/(c_B sqrt(Lambda))+delta U_B.             (3)

This is an explicit cap-uniform spectral localization estimate for
actual critical lifts. It has no inverse old defect. A fixed Lambda
still gives an absolute floor; (3) is not outward suppression. In
particular converting its spectral cutoff into a growing numerical
basis does not supply the missing signed prime/pole correlation.
The A_s spectrum itself and its projections are not evaluated here.

For an actual null the stronger mass-relative version of (1) gives

    ||F_(s,Lambda)h||_D^2 <=r_B^2||h||_2^2/Lambda,
    ||F_(s,Lambda)h||_2^2 <=r_B^2||h||_2^2/Lambda^2.     (4)

Thus a null cannot live wholly above Lambda>r_B. This constrains its
spectral distribution; it does not eliminate a low-spectrum null.
CC37 supplies r_B=20 on caps through21/20; the general cap remainder
envelope applies beyond that, with the separately proved IP8 extension
available at53/50. No new numerical defect or source constant is assigned.

## Controls and limits

Take physical A=diag(1,4), n=(3/5,8/5), R=-n*n, P=A^1/2 and N=n*.
Then Q=A+R is nonnegative and h=(3/5,2/5) is a genuine null with
||Ph||=1. It satisfies Ah=-Rh while retaining nonzero spectral mass
in the eigenvalue4 direction. This verifies that operator-domain
membership and the tail estimates are compatible with actual contact
in a source model. They are not an exclusion theorem.

The vector (2,-3) has ORIGINAL physical eigenvalue52/25>0 and becomes
null after subtraction of the FULL physical level52/25. It also has
the same supported operator-domain property; its equation is
A h=(mu I-R)h, with norm bound (r_B+mu)||h||_2. Thus the domain property
does not distinguish an original null from the positive-level control.
These finite source controls are not actual Weil arithmetic countermodels.

CC39's generic recurrence vectors escape by canonical-normalized
physical mass tending to zero and are eventually positive. Equations
(2)-(4) address selected critical or null vectors instead, but give no
contradictory arithmetic sign. The contact parity thresholds and the
separate zero-moment channel remain open; neither is removed by localization.

The restored workspace runs 16 new exact finite-model checks. Earlier
25,993-check chains are not replayed in this pass and are not added to
that count. Infinite-domain assertions above are analytic form and
spectral arguments, not Lean or numerical zeta eigenvector evaluations.
NF13's independently certified native E32 and NF10's F112 complement at
53/50 are preserved read-only; their mixed whole-domain sign is still pending.
The whole-domain anchor stays21/20, even0/odd0, physical margin1/(3*10^63).
RH/F4, retained attachment, critical outward suppression and Lean closure
remain open.
