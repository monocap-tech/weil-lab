# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-40 — DIVISOR-CLEARED CARLEMAN NUMERATORS ARE ORDER-ONE MAXIMAL TYPE; CARTWRIGHT/UNCONDITIONAL DE BRANGES CLOSURE FAILS.}
}
\`\`\`

For the nonzero right/left exterior tails,

\`\`\`math
N_\pm(z)
=
z^2
\xi\!\left(\frac12\mp iz\right)
\mathcal C_\pm^{\rm mer}(z)
\`\`\`

are entire of order one and infinite/maximal type.  Finite exponential type
would force the corresponding one-sided Laplace transform to decay faster than
every exponential, which by the Laplace support theorem would make the tail
vanish identically; RPB-11 excludes that for a nonzero compact neutral mode.

Hence \(N_\pm\) are not Cartwright, and \(T\log T\)-scale zeta interpolation is
compatible with their growth. The natural \(\xi\)-based Hermite--Biehler/de
Branges normalization is RH-conditional, while dividing by \(\xi\) restores
the uncancelled divisor and loses entire structure.

The surviving datum is the subleading vertical indicator:

\`\`\`math
\limsup_{Y\to\infty}
\frac{
\log|N_+(iY)|
-
\log\xi(1/2+Y)
}{Y}
=
-b_+,
\`\`\`

where \(b_+\) is the first support point of the right exterior tail.

## Next cursor

```text
RPB-41 / CARLEMAN INDICATOR SUPPORT-EDGE MATCHING
```

The next pass should compute the same vertical indicator from the explicit
identity for \(N_+\), using the Paley--Wiener support indicators of the compact
source and finite-interval correction, and test whether the tail onset \(b_+\)
is forced to equal the collar edge \(a\), a source-support endpoint, or another
rigid value.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
