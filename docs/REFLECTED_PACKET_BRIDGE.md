# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-47 — THRESHOLD MELLIN AMPLITUDES ARE LAWFUL BOUNDARY RESIDUES, BUT ZERO MEAN AND UNIT GAIN DO NOT FORCE THEIR VANISHING.}
}
\`\`\`

At a prime-power threshold, localizing the endpoint source and Mellin
transforming gives the principal equation

\`\`\`math
\left(
\frac{\pi}{2\sin(\pi z)}
+
\varepsilon_u a_0
\right)
\widehat f_M(z)
=
H_f(z),
\`\`\`

so the admissible endpoint coefficients are the cutoff-independent residues

\`\`\`math
\mathfrak a_\beta(u)
=
\operatorname*{Res}_{z=-\beta}
\widehat f_M(z)
\`\`\`

at the RPB-46 indicial roots.

For a nonzero persistent source, the full amplitude vector is nonzero.  The
zero-mean condition is instead the ordinary Mellin value

\`\`\`math
\widehat f_M(1)=0,
\`\`\`

and does not annihilate those residues.

Via the neutral-resolvent isomorphism, each amplitude gives a boundary row on
the threshold-compatible unit-gain subspace,

\`\`\`math
\mathfrak T_{\beta,c}(v)
=
\mathfrak a_\beta
\left(
D A_{B,c}^{-1}\Phi_c^*v
\right).
\`\`\`

The existing Birman--Schwinger identity
\(\mathsf K_cv=v\) does not compute or annihilate this row.  Since the
unit-gain space is finite dimensional, the entire family of threshold Mellin
rows collapses to a finite boundary-transfer matrix.

## Next cursor

```text
RPB-48 / THRESHOLD BIRMAN--SCHWINGER BOUNDARY-TRANSFER MATRIX
```

The next pass should attempt to compute the threshold boundary-transfer rows
directly from the resolvent extremizer
\(h_v=A_{B,c}^{-1}\Phi_c^*v\): derive the boundary Mellin formula for the
background resolvent, express the first admissible amplitude row in selected
coordinates, and determine whether the resulting finite matrix has full column
rank on the unit-gain eigenspace or whether an additional resolvent boundary
symbol is genuinely missing.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
