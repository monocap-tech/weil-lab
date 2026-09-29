# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-49 — THE LOGARITHMIC ENDPOINT PRINCIPAL SYMBOL KILLS EVERY THRESHOLD MELLIN AMPLITUDE; NO NONZERO SCREW-CORE NEUTRAL MODE ADMITS A STRICT NULL EXTENSION.}
}
\`\`\`

The one-dimensional logarithmic endpoint normal form is

\`\`\`math
\mathcal N_{\log}H(t)
=
2tH(t)
-
\int^t H(w)\,dw,
\qquad
t=\log(1/s),
\`\`\`

with generic homogeneous boundary scale \(H(t)\sim t^{-1/2}\).  Screw-core
regularity \(h\in H_0^1\) lies strictly below every finite inverse-logarithmic
boundary layer.

More decisively, any noninteger conormal physical component

\`\`\`math
h(c-s)\sim b\,s^\lambda
\`\`\`

produces under the archimedean logarithmic principal part an unavoidable

\`\`\`math
b\,s^\lambda\log(1/s)
\`\`\`

term.  At the endpoint, the active prime translations, pole/evaluation row,
and smoother archimedean remainder cannot produce the same extra logarithm at
that noninteger exponent.

A nonzero RPB-46 threshold Mellin amplitude of \(u=Dh\) gives exactly such a
noninteger conormal component of \(h\).  Hence every lawful threshold amplitude
must vanish.  RPB-47, however, proved that every nonzero threshold-persistent
source must have a nonzero full threshold amplitude vector.

Therefore the threshold persistence branch is empty.  Combined with RPB-45's
nonthreshold exclusion,

\`\`\`math
0\ne u\in\ker G_c
\Longrightarrow
G_aJ_{c,a}u\ne0
\qquad
(a>c)
\`\`\`

on the screw-visible/core neutral subspace.

This remains branch-local experimental standing.  The effect on the full
Friedrichs nullspace and the canonical null-extension interface still requires
the multiplicity/core-lift audit.

## Next cursor

```text
RPB-50 / NULL-EXTENSION DISCHARGE AND NEUTRAL-PLATEAU COLLAPSE AUDIT
```

The next pass should audit the consequences of the core strict-null-extension
exclusion against the earlier neutral branch: determine whether one nonzero
core leakage direction collapses every positive-length neutral plateau, map the
result through the neutral-resolvent/screw-visible identifications, decide the
exact status of \`AZ-FIN-WEIL-NULL-EXTENSION\`, and isolate any remaining
Friedrichs multiplicity or selected-custody caveat without promoting beyond the
proved scope.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
