# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-45 — THE BASE }t=0\textbf{ SCREW SINGULARITY EXCLUDES ALL NONTHRESHOLD STRICT COLLARS; ONLY PRIME-POWER THRESHOLD CARLEMAN MATCHING SURVIVES.}
}
\`\`\`

Suzuki's small-\(t\) expansion gives

\`\`\`math
g''(t)
=
\frac1{2t}
+
O(1)
\qquad
(t\downarrow0).
\`\`\`

At the right support edge \(x=c+s\), this produces the endpoint Stieltjes
transform

\`\`\`math
\frac12
\int_0^{2c}
\frac{u(c-r)}{s+r}\,dr.
\`\`\`

If \(2c\) is not a prime-power logarithm, every other local term is analytic
through \(s=0\).  A strict collar would then force this Cauchy transform to
extend holomorphically through the endpoint of its cut, and the Plemelj jump
would force the endpoint source to vanish.  Interior analyticity then gives
\(u\equiv0\), contradiction.

Therefore strict persistence is possible only at a threshold

\`\`\`math
2c=\log n_0.
\`\`\`

At such a threshold, parity reduces the equality-threshold prime contribution
to the exact endpoint equation

\`\`\`math
\frac12
\int_0^{2c}
\frac{f(r)}{s+r}\,dr
+
\varepsilon_u
\frac{\Lambda(n_0)}{\sqrt{n_0}}
f(s)
+
A(s)
=
0,
\`\`\`

with \(f(s)=u(c-s)\) and \(A\) analytic.  This is the only surviving
base-crossing mechanism.

## Next cursor

```text
RPB-46 / THRESHOLD CARLEMAN-MELLIN ENDPOINT REALIZATION
```

The next pass should analyze the threshold singular integral equation itself:
identify the endpoint Carleman/Mellin operator, determine the parity-dependent
spectrum and actual \(L^2\) endpoint germs, and test whether any such germ is
compatible with the global neutral mode and zero-mean normalization.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
