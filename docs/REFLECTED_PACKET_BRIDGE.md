# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

\`\`\`math
\boxed{
\textbf{RPB-38 — PRIME-LOG SYMBOL NONDEGENERACY DOES NOT CLOSE THE COMPRESSED COLLAR PROBLEM; THE COMPACT SOURCE RETAINS THE ZETA SPECTRUM.}
}
\`\`\`

The strict-right scalar symbol

\`\`\`math
\Psi_{c_*+}(\xi)
=
\Re\psi\!\left(\frac14+\frac{i\xi}{2}\right)
-\log\pi
-
\sum_{\log n\le2c_*}
\frac{2\Lambda(n)}{\sqrt n}\cos(\xi\log n)
\`\`\`

is real analytic and tends to \(+\infty\), so it has only finitely many real
zeros.

But the compact-window neutral mode is a kernel vector of a compressed
operator, not a whole-line multiplier kernel.  Its Fourier transform is
therefore not localized to the real zero set of \(\Psi_{c_*+}\).

Conversely, a nonzero compact screw source cannot cancel the zeta spectrum:
its entire transform has only \(O(T)\) zeros, while there are
\(\gg T\log T\) distinct simple critical-line zeta ordinates.  Hence
\(\gg T\log T\) critical spectral coefficients survive.

The remaining frequency-side problem is a spatial-gap/Fourier--Carleman
factorization of the left and right exterior tails.

## Next cursor

```text
RPB-39 / EXTERIOR-TAIL FOURIER-CARLEMAN FACTORIZATION
```

The next pass should type the exterior tails
\(q=\mathcal W^{\rm ext}_{c_*+}h\) precisely, determine their half-plane
Fourier--Carleman growth classes, derive the exact left/right boundary-value
identity with the completed Weil symbol and finite pole row, and test whether a
Wiener--Hopf factorization or index calculation rules out a nonzero
Paley--Wiener numerator.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
