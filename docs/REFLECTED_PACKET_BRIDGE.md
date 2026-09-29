# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-39 — THE EXTERIOR TAILS HAVE DISJOINT CARLEMAN HALF-PLANES, AND THEIR CONTINUATION CARRIES AN UNCANCELLED ZETA DIVISOR.}
}
\`\`\`

For a hypothetical persistent screw-visible neutral mode, subtract the collar
constant from \(F_u=g*u\) and split the residual into left/right exterior
tails. Suzuki's unconditional growth estimate gives native one-sided
Fourier--Carleman domains

\`\`\`math
\Im z>\frac12,
\qquad
\Im z<-\frac12,
\`\`\`

with no common bilateral convergence strip.

The right tail has the exact representation

\`\`\`math
\mathcal C_+(z)
=
\frac{V(z)}{z^2}
\frac{\xi'}{\xi}\!\left(\frac12-iz\right)
-
E_+(z)
+
\frac{Ce^{iaz}}{iz},
\`\`\`

where \(V\) is the compact-source transform and \(E_+\) is entire.  The left
tail is the reflected analogue.

Meromorphic continuation across the separating strip therefore crosses the
zeta divisor.  By RPB-38, the compact source fails to cancel
\(\gg T\log T\) simple critical poles.

Multiplying by \(z^2\xi(1/2\mp iz)\) yields entire divisor-cleared numerators,
but their inherited order-one \(\xi\) growth means no Paley--Wiener/Jensen
contradiction has yet been obtained.

## Next cursor

```text
RPB-40 / DIVISOR-CLEARED CARLEMAN NUMERATOR GROWTH TEST
```

The next pass should study the entire divisor-cleared numerators \(N_\pm\):
determine their order/type, test for a lawful Cartwright or de Branges
normalization, and decide whether the interpolation values
\(N_+(z_\rho)=V(z_\rho)\xi'(\rho)\) produce a density contradiction or are
compatible with the inherited order-one growth.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
