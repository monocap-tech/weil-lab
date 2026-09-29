# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-48 — THE THRESHOLD BOUNDARY MATRIX IS THE ENDPOINT MELLIN TRACE OF THE BACKGROUND RESOLVENT; BIRMAN--SCHWINGER GRAM DATA DO NOT DETERMINE IT.}
}
\`\`\`

Choose selected basis vectors \(e_j\), forcing columns
\(g_j=\Phi_c^*e_j\), and resolvent columns
\(h_j=A_{B,c}^{-1}g_j\).  Then every admissible threshold boundary row is

\`\`\`math
(\mathbf B_c)_{\ell j}
=
\mathfrak a_{\beta_\ell}(Dh_j)
=
\mathfrak a_{\beta_\ell}
\left(
D A_{B,c}^{-1}\Phi_c^*e_j
\right).
\`\`\`

Thus the finite boundary matrix is exact once the endpoint Mellin symbol of
the background resolvent is known.

The Birman--Schwinger matrix stores only

\`\`\`math
(\mathsf K_c)_{kj}
=
\langle h_j,g_k\rangle,
\`\`\`

and does not determine these endpoint conormal residues.  An abstract
finite-rank perturbation model shows that identical compressed Gram data can
coexist with different boundary rows.

Also, full rank of the **allowed amplitude** matrix is not an exclusion
criterion: a nonzero persistent threshold mode must carry a nonzero admissible
amplitude.  The actual persistence obstruction is the complementary boundary
defect consisting of forbidden Mellin channels plus the analytic exterior
remainder.

## Next cursor

```text
RPB-49 / BACKGROUND RESOLVENT ENDPOINT PARAMETRIX
```

The next pass should attack the missing endpoint symbol of the actual
background resolvent: put \(A_{B,c}\) into endpoint coordinates, separate the
universal logarithmic-Laplacian singular kernel from bounded prime/fixed-rank
terms, construct the local Mellin/Wiener--Hopf parametrix, and determine the
coefficient map from selected analytic forcing to both admissible and forbidden
boundary channels.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
