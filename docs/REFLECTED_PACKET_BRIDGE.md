# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-41 — THE CARLEMAN INDICATOR MATCHES THE MAXIMAL COLLAR EDGE EXACTLY, BUT PROVIDES NO INDEPENDENT SOURCE-SUPPORT CONTRADICTION.}
}
\`\`\`

Along \(z=iY\), the compact-source term and the finite-interval correction
carry the same source-edge exponential scale but cancel exactly into the true
exterior potential tail:

\`\`\`math
V(iY)\frac{\xi'}{\xi}(1/2+Y)
+
Y^2E_{+,a}(iY)
=
-
Y^2\int_a^\infty F_u(x)e^{-Yx}\,dx.
\`\`\`

The elementary collar-constant term then removes the constant plateau.  The
divisor-cleared numerator is invariant under movement of the artificial cutoff
inside that plateau:

\`\`\`math
\partial_aN_{+,a}=0.
\`\`\`

If \(a_{\max}\) is the maximal symmetric interval on which the screw potential
is constant, then

\`\`\`math
\limsup_{Y\to\infty}
\frac{
\log|N_+(iY)|-\log\xi(1/2+Y)
}{Y}
=
-a_{\max}.
\`\`\`

Thus the indicator records the true end of the plateau but does not determine
it from the compact-source support edge.

## Next cursor

```text
RPB-42 / MAXIMAL COLLAR FIRST-ACTIVATION GEOMETRY
```

The next pass should analyze the local geometry where the maximal constant
collar first fails: separate the analytic archimedean/pole pieces from the
moving prime-power kinks, identify the shifted-source activation sets
\(\log n+\operatorname{supp}u\), and determine whether the first activation
point is arithmetically constrained or simply another form of the existing
null-extension obstruction.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
