# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-43 — CORE-NEUTRAL ANALYTIC SINGULAR SUPPORT IS ENDPOINT-ONLY; MAXIMAL COLLAR ACTIVATION IS DISCRETE AND ENDPOINT-ARITHMETIC.}
}
\`\`\`

The full translation-invariant compact-window Weil symbol is analytic and
elliptic at high frequency.  Since the pole/evaluation term has analytic
finite-dimensional range, analytic elliptic regularity gives

\`\`\`math
h,u\in C^\omega(-c,c),
\qquad
u=Dh.
\`\`\`

For the zero-extended nonzero source,

\`\`\`math
\operatorname{singsupp}_{\omega}u
=
\{-c,c\}.
\`\`\`

Therefore RPB-42's first-activation set collapses to the discrete endpoint
spectrum

\`\`\`math
a_{\max}
\in
\{c+\log n,\ \log n-c:n=p^m\}.
\`\`\`

An unpaired endpoint activation cannot be crossed by a constant plateau.  The
only possible crossing mechanism is a paired right-exit/left-entry collision,

\`\`\`math
e^{2c}=m/n,
\`\`\`

together with a weighted analytic endpoint-germ matching condition.  In the
nonresonant case,

\`\`\`math
a_{\max}
=
\min\{c+\log2,\ \log n_+(c)-c\}.
\`\`\`

## Next cursor

```text
RPB-44 / PAIRED ENDPOINT COLLISION RESONANCE AND GERM MATCHING
```

The next pass should analyze the resonant branch
\(e^{2c}=m/n\) for prime powers \(m,n\): use parity to derive the exact
endpoint-germ matching relation, test whether the von Mangoldt weights can
satisfy it, and determine whether crossing one collision forces a further
collision ladder compatible with a finite maximal collar.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
