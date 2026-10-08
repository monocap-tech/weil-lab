# RPB108 CC35: exact native pole correlation and transverse obstruction

Date: 2026-10-08 UTC. Parent: 40cab3ca85b3d709d130a1fc397f3949aee1dce3.
Definitions: [parity pole correlation](../docs/TERMINOLOGY_RPB108_PARITY_POLE_CORRELATION.md).
Scope: a concrete native correlation test, not its certification.

## The actual pole direction

CC27's full Hermitian pole kernel is

    exp((x-y)/2)+exp(-(x-y)/2)
       =2 cosh(x/2)cosh(y/2)-2 sinh(x/2)sinh(y/2).

Thus its physical operator is 2|cosh><cosh|-2|sinh><sinh|.
This sign is important: the odd pole is negative. No replacement by
two positive squares is made. For a lift of definite parity, the
opposite moment vanishes, leaving exactly

    C_pole,t h=sigma a ell,
    q=q_0+sigma a v.                                    (1)

The definitions above fix all factors of two in normalized Q. The
canonical projection is performed after the native operators act;
v is not the physical exterior restriction of g. This pass applies
to any exact critical lift of definite parity. It makes no assertion
that arbitrary complex lifts have a single pole direction; they have
up to two, and require the corresponding full Gram projection.

## Two necessary and sufficient correlation tests

In the complete positive-inverse metric, decompose q_0=z v+q_perp.
For v nonzero, exact orthogonality gives

    ||M_t^-1/2 q||^2
       =||q_perp||_*^2+||v||_*^2 |z+sigma a|^2.          (2)

No omitted complement, finite packet inverse or assumed commutation
between M_t and Pi occurs. A scalar target bound b_B lambda omega(delta)
on the left is equivalent to the bound on the SUM on the right.
It implies each term separately is at most that budget. Conversely,
separate budgets b_perp lambda omega and b_pole lambda omega imply
the target with b_B=b_perp+b_pole. If v=0, q=q_0 and only the whole
q_0 bound remains; no division by zero or pole normalization is used.

This identifies precisely the correlation a pole-cancellation argument
would have to supply. It must simultaneously suppress the full
archimedean-plus-prime transverse forcing and make its longitudinal
coefficient z cancel sigma a in the complete dual geometry. Merely
matching the pole moment or longitudinal phase cannot address the
first term. Merely bounding individual component norms can destroy
the cancellation in the second term.

Equation (2) is an identity, not an estimate of adaptive zeta lifts.
Neither term is currently bounded by a vanishing defect modulus.
Through CC33 the true forced row differs in norm by at most
(U_B/c_B)delta; through CC31 a proved scalar bound would control the
collective finite critical cluster. These dependencies are unchanged.
CC34's interior/unsigned lower bound does not upper-bound either term.

## Metric, phase and transverse controls

Take an exact two-coordinate dual control

    M=[[1,b],[b,1]], |b|<1, v=(0,1), q_0=(x,z_0).

The positive-inverse longitudinal coefficient is z=z_0-bx,
not z_0, and the transverse energy is x^2. For sigma=+1,

    ||q_0+a v||_*^2=x^2+(z_0-bx+a)^2/(1-b^2).           (3)

When q_0=-a v, the total forcing vanishes even though both component
energies equal a^2/(1-b^2). Reversing its phase to q_0=+a v gives
four times this energy, with identical individual component norms.
For x=1/4 and z_0=bx-a, the longitudinal mismatch is exactly zero,
yet the total forcing energy is 1/16. This transverse leakage cannot
be removed by any pole phase adjustment. Both signs sigma are checked.

These are exact dual decomposition controls, not native Weil source
identities or an arithmetic countermodel. Genuine differential crossing
and full positive-level controls are replayed through CC34's chain;
their complete mass channel is retained. No new physical aperture or
actual arithmetic covariance calculation is claimed.

## Standing and concurrent handoff

IP5 supplies an absolute small-step modulus from compact remainder
and support continuity. It explicitly does not supply a fixed-step
defect modulus. Equation (2) does not promote that modulus into either
of its two missing defect-dependent estimates. IP1-IP5 are preserved
as read-only dependencies; no independent investigation is restarted.

The validator adds 144 exact rational checks to CC34's 25,729, for
25,873 passing checks. The actual pole rank and signs follow from
the native kernel analytically; the numerical checks concern the
noncommuting metric and cancellation controls. No Lean proof is added.

Original positivity remains certified through21/20, even0/odd0,
physical margin1/(3*10^63). Arithmetic outward suppression, RH/F4,
retained attachment, reusable continuation and Lean closure remain
open. No logical nonimplication from complete Weil arithmetic is proved.
