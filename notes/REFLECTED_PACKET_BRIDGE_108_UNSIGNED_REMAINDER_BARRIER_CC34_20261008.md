# RPB108 CC34: critical lifts cannot have vanishing unsigned remainder energy

Date: 2026-10-08 UTC. Parent: 80644d007765195afccbed606d1128965f165d06.
Definitions: [unsigned remainder barrier](../docs/TERMINOLOGY_RPB108_UNSIGNED_REMAINDER_BARRIER.md).
This is a native analytic obstruction to a specific estimator, not an
arithmetic leakage bound or a countermodel to the full Weil identities.

## Exact native result

Let h be any exact old critical lift, normalized by ||Ph||=1. Testing
its old equation with h itself gives

    <C_t h,h>_D=delta-||h||_D^2.                         (1)

The same supported vector and diagonal form are used on D_s and D_t.
For delta<1/U_B^2, the right side is negative, and consequently

    V_B(h)>=||h||_D^2-delta>=1/U_B^2-delta.             (2)

Here V_B keeps all native terms: the absolute archimedean remainder
diagonal, the absolute contributions from both shifts for each active
prime power, and the absolute cross-paired pole contributions. Triangle
inequality proves its lower bound by the absolute value of (1).
CC33's component norm estimates also give V_B(h)<=r_B||h||_2^2,
with r_B as defined there. Therefore, when r_B>0,

    ||h||_2^2>=(1/U_B^2-delta)/r_B.                    (3)

If r_B=0, such a critical lift with delta<1/U_B^2 is impossible outright.
For delta<=1/(2U_B^2), physical mass is at least 1/(2r_BU_B^2).
Thus any hypothetical near-zero-defect sequence cannot escape by
making its normalized physical mass vanish. No additional regularity,
source compactness, height moment, Lindelof estimate or aperture change
is used. These are uniform cap statements, conditional on the existence
of the stated critical lifts, not an assertion that such a sequence exists.

The vector version identifies where the large remainder sits. Project
the exact old equation canonically:

    Pi C_t h=-h+delta Pi M_t h.

Since ||M_t h||<=U_B and ||h||_D>=1/U_B,

    ||Pi C_t h||_D>=1/U_B-delta U_B.                   (4)

In particular the complete canonical remainder cannot be small on
critical lifts. Its interior component must cancel the leading identity.
The outward component q=(I-Pi)C_t h is not bounded below by (2)-(4).

## Precisely which proposed route fails

A proposed uniform estimate V_B(h)<=K_B omega(delta), with finite K_B
and bounded omega tending to zero, is incompatible with any actual
sequence of critical lifts having delta->0: (2) has positive limiting
lower bound. The same statement holds for a vanishing bound on the
full remainder norm or its canonical interior component by (4).
Componentwise absolute value or Cauchy-Schwarz estimates that require
one of these quantities to vanish therefore cannot deliver the desired
outward suppression in a nonvacuous near-critical regime.

This does NOT prove that every use of absolute estimates fails. A new
bound that estimates the projected outward component directly may be
smaller than the full unsigned envelope. Nor does the failure prove
that the complete original Weil identities cannot imply RH or the
desired bound. The required directional cancellation remains unproved:

    ||M_t^-1/2 (I-Pi)C_t h||^2
        <=b_B lambda omega_B(delta), omega_B(delta)->0. (5)

CC33 transfers (5), with its O_B(delta) norm correction, to the true
forced row. CC31 supplies the cap-uniform finite critical rank needed
to pass scalar row bounds to collective covariance. Equation (2) is
not evidence for (5); it rules out replacing (5) by smallness of all
native remainder terms. Signed arithmetic cancellation after projection
and complete positive-inverse normalization is still essential.

## Controls: identical interior energy, different outward behavior

Take the exact finite source form P=I, N=(u,v), old domain span e_1,
h=e_1, lambda=u^2 and delta=1-u^2. Then C=-N*N and

    Pi Ch=-u^2 e_1, q=-uv e_2, V(h)=u^2,
    det Q_t=delta-v^2.

With v=0, the full remainder energy tends to one but q=0; the enlarged
form stays positive for every delta>0. With v=1/4, precisely the same
old equation and envelope hold, yet q^2=u^2/16 tends to 1/16 and the
enlarged form crosses when delta<1/16. Both have rank-one compact C.
Thus the unsigned diagonal information neither upper-controls leakage
by a vanishing modulus nor forces leakage to be nonzero. These finite
source controls are not actual Weil arithmetic divisors or EF models.

The inherited genuine differential crossing and full positive-level
mass-channel controls are replayed through CC33. No finite control is
substituted for actual arithmetic critical-vector data.

## Validation and standing

The validator adds 72 exact rational checks and replays CC33's 25,657,
for 25,729 passing checks. Checks verify the two contrasting controls,
the crossing threshold, diagonal/interior identities and the failure
of full remainder smallness to distinguish the controls. Native infinite-domain
claims (1)-(4) are analytic deductions, not computed zeta covariance
or Lean certificates.

Original whole-domain positivity remains certified through 21/20,
even0/odd0, physical margin 1/(3*10^63). RH/F4, arithmetic outward
suppression, retained attachment, reusable continuation and Lean
closure remain open. IP1-IP4 are preserved. Other fronts remain paused.
