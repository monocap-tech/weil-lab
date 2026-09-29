# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** research/reflected-packet-bridge  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** monocap-tech/weil@research/reflected-packet-bridge through RPB-35.

## Current standing

~~~math
\boxed{
\textbf{RPB-55 — CURRENT BOUNDARY REGULARITY DOES NOT PRODUCE A UNIVERSAL OPTIMAL LOG TRACE COEFFICIENT, AND VANISHING OF SUCH A COEFFICIENT DOES NOT FORCE SCREW-CORE MEMBERSHIP.}
}
~~~

RPB-54 excluded every mode carrying a nonzero optimal logarithmic boundary
amplitude.  RPB-55 audits whether that amplitude exists for every Friedrichs
zero mode.

The current sharp pure-logarithmic boundary theorem gives the envelope

~~~math
|u(x)|
\le
C\ell^{1/2}(d(x,\partial\Omega))
~~~

for bounded weak solutions with bounded forcing.  It does not assert existence
of a boundary quotient limit

~~~math
u/\ell^{1/2}\to b.
~~~

Matching lower bounds are known for special positive/Hopf classes, such as the
torsion function and nonnegative supersolutions, but not for arbitrary
sign-changing zero modes.

For the actual compact-window Weil operator, RPB-31 only gives logarithmic
operator-domain regularity.  Current inputs do not yet prove that every
Friedrichs zero mode falls into the bounded-solution/bounded-forcing class of
the optimal boundary theorem.

Therefore the boundary-untyped residue remains real at the present theorem
level.

Moreover, even if an optimal coefficient exists and vanishes,

~~~math
h=o(\ell^{1/2}),
~~~

this does not imply

~~~math
h\in H_0^1.
~~~

For example,

~~~math
h(c-r)=\ell(r)=\frac1{\log(1/r)}
~~~

is log-flat relative to \(\ell^{1/2}\), while its derivative is not square
integrable near the endpoint.

The more robust boundary object is the cumulative boundary mass

~~~math
M_+(s;h)
=
\int_s^\delta
\frac{h(c-r)}{r}\,dr,
~~~

and similarly \(M_-\) at the left endpoint.

This recovers the RPB-54 amplitude leak as

~~~math
h(c-r)\sim b\ell^{1/2}(r)
\Longrightarrow
M_+(s;h)\sim2b\sqrt{\log(1/s)},
~~~

but also detects slower log-flat leakage:

~~~math
h(c-r)\sim\frac{b}{\log(1/r)}
\Longrightarrow
M_+(s;h)\sim b\log\log(1/s).
~~~

Thus a scalar trace coefficient is not the fundamental null-extension datum.
The remaining thin residue is the class in which cumulative boundary mass
stays bounded by cancellation.

Current branch-local partition:

~~~text
CORE ZERO MODE:
    excluded conditionally by RPB-34–49

NONCORE MODE WITH NONZERO OPTIMAL LOG AMPLITUDE:
    excluded by RPB-54

BOUNDARY-UNTYPED OR LOG-FLAT MODE WITH UNBOUNDED CUMULATIVE MASS:
    candidate direct-leak class

BOUNDED CUMULATIVE-MASS CANCELLATION RESIDUE:
    OPEN
~~~

## Next cursor

~~~text
RPB-56 / CUMULATIVE BOUNDARY-MASS LEAKAGE AND CANCELLATION TEST
~~~

The next pass should derive the exterior Weil output directly in terms of
\(M_\pm\), without assuming a pointwise trace coefficient, and determine
whether every unbounded cumulative mass dominates the remaining actual-Weil
terms.  The residual bounded-mass class should then be tested against the
interior zero equation.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved
branch-local statements, imported results, scope/no-go statements, or open
residue. Commit status is not canonical status. Promotion into the stable Weil
theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in notes/REFLECTED_PACKET_BRIDGE_0_20260928.md through notes/REFLECTED_PACKET_BRIDGE_55_20260928.md.
