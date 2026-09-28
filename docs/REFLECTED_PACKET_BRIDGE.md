# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-37 — THE ACTUAL NEUTRAL EDGE HAS A DENSE MULTI-PRIME DELAY ORBIT; SUPPORT-ORDER TRIANGULARIZATION DOES NOT CLOSE THE COLLAR PROBLEM.}
}
\`\`\`

The current unconditional compact-window positivity certificate gives
\(c_*>0.8\), so the active strict-right delay set already contains
\(\log2\) and \(\log3\). Their ratio is irrational, hence

\`\`\`math
\Gamma_{c_*}
=
\operatorname{span}_{\mathbb Z}\mathcal D_{c_*+}
\`\`\`

is dense in \(\mathbb R\).

Thus every interior delay orbit is dense and has arbitrarily small nonzero net
steps.  This rules out a finite support lattice or a monotone boundary-to-
interior triangularization.

Density still does not propagate zero because the Weil equation supplies a
weighted multi-delay relation plus a global archimedean field, not a scalar
transport law.

## Next cursor

```text
RPB-38 / PRIME-LOG DELAY SYMBOL SPECTRAL-SYNTHESIS TEST
```

The next pass should leave spatial support-order iteration and work in the
frequency/symbol picture: analyze the quasiperiodic prime-delay symbol, combine
it with the archimedean multiplier and pole term, and test whether compact
support / Paley--Wiener or Suzuki's Fourier--Carleman mean-periodic framework
yields an isolating spectral-synthesis relation.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
