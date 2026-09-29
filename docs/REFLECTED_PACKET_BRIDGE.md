# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** research/reflected-packet-bridge  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** monocap-tech/weil@research/reflected-packet-bridge through RPB-35.

## Current standing

~~~math
\boxed{
\textbf{RPB-60 — THE STANDARD ANALYTIC-PSEUDODIFFERENTIAL ROUTE DOES NOT CERTIFY INTERIOR ANALYTICITY FOR THE FINITE-DELAY WEIL OPERATOR.}
}
~~~

RPB-59 isolated logarithmic-order interior analyticity as the first promotion
blocker.

RPB-60 shows that the historical RPB-43 proof does not certify it.

The archimedean component is a diagonal logarithmic pseudodifferential
operator, but each prime translation

~~~math
(\tau_\ell h)(x)=h(x-\ell)
~~~

has kernel

~~~math
\delta(x-y-\ell),
~~~

singular on the shifted diagonal \(x-y=\ell\).

Therefore prime shifts are translation Fourier-integral operators with
off-diagonal canonical relation, not ordinary analytic pseudodifferential
lower-order terms.

The Fourier multiplier

~~~math
e^{-i\ell\xi}
~~~

also fails the decaying \(\xi\)-derivative bounds used by the standard
\(S^0_{1,0}\) pseudodifferential calculus.

Hence the full scalar multiplier

~~~math
\Psi_c(\xi)
=
m_\infty(\xi)
-
\sum_j2a_j\cos(\ell_j\xi)
~~~

cannot be inserted directly into the ordinary analytic-wavefront elliptic
theorem merely because

~~~math
|\Psi_c(\xi)|
\gtrsim\log|\xi|
~~~

at high frequency.

The correct local problem is an analytic-wavefront **delay-orbit propagation**
problem:

~~~math
(x,\xi)\in WF_A(h)
~~~

may be coupled to

~~~math
(x\pm\ell_j,\xi)\in WF_A(h).
~~~

This is structurally consistent with the finite-delay obstruction already seen
in RPB-36/37.

Consequences:

~~~text
RPB-43 FULL-SYMBOL ANALYTIC-ELLIPTIC SHORTCUT:
    WITHDRAWN

INTERIOR ANALYTICITY OF ARBITRARY FRIEDRICHS ZERO MODES:
    OPEN

RPB-57 FULL NONTHRESHOLD FRIEDRICHS EXCLUSION:
    CONDITIONAL / UNPROMOTED

RPB-58 FULL THRESHOLD FRIEDRICHS EXCLUSION:
    CONDITIONAL / UNPROMOTED

AZ-FIN-WEIL-NULL-EXTENSION:
    OPEN
~~~

The external source pin RPB-EXT-A1 itself remains valid for ordinary analytic
pseudodifferential operators; only its earlier specialization to the full
finite-delay operator is withdrawn.

## Next cursor

~~~text
RPB-61 / ANALYTIC-WAVEFRONT DELAY-ORBIT PROPAGATION
~~~

The next pass should derive the correct singularity-propagation relation for
the logarithmic archimedean operator coupled to finite translations and test
whether compact support/end-point zero regions forbid a closed or infinite
singular delay orbit.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved
branch-local statements, imported results, scope/no-go statements, or open
residue. Commit status is not canonical status. Promotion into the stable Weil
theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in notes/REFLECTED_PACKET_BRIDGE_0_20260928.md through notes/REFLECTED_PACKET_BRIDGE_60_20260929.md.
