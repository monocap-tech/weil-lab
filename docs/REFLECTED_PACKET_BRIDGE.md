# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-44 — PAIRED PRIME-ENDPOINT RESONANCES CANNOT SATISFY THE REQUIRED WEIGHT MATCHING; ALL LATER PRIME ACTIVATIONS ARE UNCROSSABLE.}
}
\`\`\`

At a paired endpoint collision

\`\`\`math
c+\log n
=
\log m-c,
\`\`\`

parity and analytic germ matching force

\`\`\`math
\frac{\Lambda(n)}{\sqrt n}
=
\frac{\Lambda(m)}{\sqrt m}.
\`\`\`

For prime powers this equality implies \(m=n\): distinct underlying primes
would make \(\log p/\log q\) algebraic, contradicting Gel'fond--Schneider,
while the same prime forces equal exponents.

But the collision equation then gives

\`\`\`math
e^{2c}=m/n=1,
\`\`\`

hence \(c=0\), impossible in the live branch.

Thus no prime-power endpoint activation strictly above \(c\) can be crossed.
Conditional on the existence of any strict collar,

\`\`\`math
a_{\max}
=
\min\{c+\log2,\ \log n_+(c)-c\},
\`\`\`

where \(n_+(c)\) is the first prime power with \(\log n>2c\).

The remaining uncertainty is now entirely the initial crossing of the original
support boundary \(x=c\), where the non-prime screw kernel itself meets
separation \(t=0\).

## Next cursor

```text
RPB-45 / BASE-ENDPOINT t=0 SCREW-SINGULARITY MATCHING
```

The next pass should return to the original support boundary \(x=c\):
derive the local \(t\downarrow0\) singular expansion of Suzuki's non-prime
screw kernel, convolve it with the analytic endpoint germ of the source,
include any equality-threshold prime event, and decide whether the endpoint
constant germ can extend even infinitesimally outside the support.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
