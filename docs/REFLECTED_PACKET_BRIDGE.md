# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-42 — MAXIMAL COLLAR FIRST ACTIVATION MUST OCCUR AT A PRIME-POWER SHIFT OF SOURCE ANALYTIC SINGULAR SUPPORT.}
}
\`\`\`

Using Suzuki's explicit positive-half screw formula,

\`\`\`math
g(t)
=
g_{\rm an}(t)
+
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+,
\qquad t>0,
\`\`\`

the non-prime part is real analytic away from \(t=0\), while each prime-ramp
convolution satisfies

\`\`\`math
P_{n,u}''(x)
=
\frac{\Lambda(n)}{\sqrt n}
u(x-\log n).
\`\`\`

Hence if no translated analytic singularity of \(u\) meets a neighborhood of
the maximal collar edge, the full potential is analytic there and its constant
value analytically continues past that edge. Therefore

\`\`\`math
a_{\max}
\in
\bigcup_{n=p^m}
\left(
\log n+\operatorname{singsupp}_{\omega}u
\right).
\`\`\`

Equivalently, for some prime power and source analytic singularity,

\`\`\`math
a_{\max}=\log n+y,
\qquad
e^{a_{\max}-c}\le n\le e^{a_{\max}+c}.
\`\`\`

This localizes first activation but does not force \(y\) to be a support
endpoint; parity and zero mean do not supply a further exclusion.

## Next cursor

```text
RPB-43 / ANALYTIC-SINGULAR-SUPPORT PROPAGATION UNDER PRIME DELAYS
```

The next pass should test whether the interior neutral equation propagates
analytic singularities along the active prime-log delay graph strongly enough
to force endpoint ownership, dense analytic singular support, incompatibility
with compact support, or else a sharp no-go showing that analytic-wavefront
propagation does not improve the current null-extension interface.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
