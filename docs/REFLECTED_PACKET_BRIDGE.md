# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-46 — THE PRIME-THRESHOLD CARLEMAN EQUATION HAS GENUINE \(L^2\)-ADMISSIBLE LOG-OSCILLATORY CONORMAL MODES; LOCAL ENDPOINT ANALYSIS DOES NOT EXCLUDE STRICT PERSISTENCE.}
}
\`\`\`

At a prime-power threshold

\`\`\`math
2c=\log n_0,
\qquad
a_0=\Lambda(n_0)/\sqrt{n_0},
\`\`\`

the local singular operator is

\`\`\`math
\frac12\mathcal C_\delta+\varepsilon_u a_0 I,
\qquad
(\mathcal C_\delta f)(s)=\int_0^\delta\frac{f(r)}{s+r}\,dr.
\`\`\`

For a cutoff monomial \(s^\beta\),

\`\`\`math
\mathcal C_\delta(s^\beta)
=
-\frac{\pi}{\sin(\pi\beta)}s^\beta
+\text{analytic},
\`\`\`

so the exact indicial family is

\`\`\`math
\mathfrak m_{\varepsilon_u}(\beta)
=
-\frac{\pi}{2\sin(\pi\beta)}
+\varepsilon_u a_0.
\`\`\`

Writing

\`\`\`math
\cosh(\pi\tau_0)=\frac{\pi}{2a_0},
\`\`\`

the first \(L^2\)-admissible endpoint source exponents are

\`\`\`math
\beta=\frac12\pm i\tau_0
\`\`\`

for an even screw source and

\`\`\`math
\beta=\frac32\pm i\tau_0
\`\`\`

for an odd screw source.

Thus the exceptional threshold branch survives local Mellin analysis; what
remains is whether the actual global neutral mode realizes a nonzero amplitude
in one of these channels.

## Next cursor

```text
RPB-47 / GLOBAL THRESHOLD MELLIN-AMPLITUDE MATCHING
```

The next pass should return to the actual finite-dimensional screw-visible
endpoint nullspace: define a lawful threshold Mellin-amplitude map, reduce it
by parity and zero mean, and test whether the global interior neutral equation
or the selected Birman--Schwinger unit-gain relation forces the admissible
endpoint amplitude to vanish.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
