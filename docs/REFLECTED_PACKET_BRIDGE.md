# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** research/reflected-packet-bridge  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** monocap-tech/weil@research/reflected-packet-bridge through RPB-35.

## Current standing

~~~math
\boxed{
\textbf{RPB-51 — SUZUKI'S GENERALIZED ZERO EIGENSPACE LIVES IN THE COMPLETED SCREW SPACE; §8.5 DOES NOT CLOSE THE ORDINARY \(L^2\) CORE-LIFT DEFECT.}
}
~~~

RPB-51 corrects the source interpretation used in RPB-33.

Suzuki first has the ordinary core map

~~~math
D:H_0^1(-a,a)\overset{\sim}{\longrightarrow}L_0^2(-a,a),
~~~

but then extends it to a unitary map between form completions

~~~math
\bar D:
\mathcal H(T_a)
\overset{\sim}{\longrightarrow}
\mathcal H(S_a),
~~~

and explicitly notes

~~~math
\mathcal H(S_a)\not\subset L^2(-a,a).
~~~

His §8.5 generalized problem is

~~~math
G_au=\lambda K_au,
\qquad
u\in\mathcal H(S_a).
~~~

Therefore the exceptional zero generalized eigenspace belongs to the completed
space.  Define

~~~math
\mathcal N_a^S
=
\{u\in\mathcal H(S_a):G_au=0\}.
~~~

The source supports the completed-space correspondence

~~~math
\ker A_a
\longleftrightarrow
\mathcal N_a^S,
~~~

not the stronger ordinary-carrier identification

~~~math
\ker A_a
\stackrel{?}{\longleftrightarrow}
\ker_{L^2}G_a.
~~~

The exact ordinary core statement from RPB-32 remains

~~~math
\boxed{
D^{-1}(\ker_{L^2}G_a)
=
\ker A_a\cap H_0^1(-a,a).
}
~~~

Accordingly, RPB-33's source-based conclusion that the actual neutral edge
necessarily has a nonzero ordinary \(L^2\) screw-kernel direction is withdrawn.
Historical RPB notes remain immutable; RPB-51 is the additive correction.

The RPB-34 through RPB-50 leakage/null-extension mechanism remains valid
**conditionally on an explicitly supplied nonzero**
\(u\in\ker_{L^2}G_c\).  What is no longer established is the bridge from an
arbitrary Friedrichs neutral edge to such a core vector.

Current branch-local status:

~~~text
CORE-RESTRICTED NULL-EXTENSION EXCLUSION: PROVED CONDITIONALLY
CORE-RESTRICTED PLATEAU COLLAPSE: PROVED CONDITIONALLY
ACTUAL-EDGE L2 SCREW-CORE EXISTENCE: OPEN
ACTUAL-EDGE PLATEAU COLLAPSE VIA THIS ROUTE: OPEN
FULL AZ-FIN-WEIL-NULL-EXTENSION: OPEN
~~~

## Next cursor

~~~text
RPB-52 / COMPLETED-TO-L2 SCREW CORE-LIFT TEST
~~~

The next pass should test whether a completed generalized zero mode

~~~math
u\in\mathcal N_c^S
~~~

is forced into the ordinary carrier

~~~math
L_0^2(-c,c).
~~~

Priority is zero-eigenvalue regularization of the completed kernel equation,
not another multiplicity count.  If no lift exists, the quotient between the
completed zero space and the ordinary \(L^2\) screw kernel is the exact
remaining object.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in notes/REFLECTED_PACKET_BRIDGE_0_20260928.md through notes/REFLECTED_PACKET_BRIDGE_51_20260928.md.
