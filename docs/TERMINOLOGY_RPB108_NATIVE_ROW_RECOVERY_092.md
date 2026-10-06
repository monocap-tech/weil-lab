# RPB-108 native row recovery at 23/25

Definitions precede their use in the linked recovery note. This additive
registry records their exact checkpoint meaning; historical terminology is
unchanged.

- **Raw native entry:** the unnormalized rational interval computed by the
  existing native Legendre constructor, before the physical basis factor
  sqrt((2i+1)(2j+1))/(2a) is applied.
- **Completed-row count r:** every upper-triangle pair with smaller degree
  below r has been computed and copied symmetrically. Every even pair whose
  smaller degree is at least r remains uncomputed and is encoded as zero.
  Every odd reflection-parity pair is exactly zero throughout.
- **Native row checkpoint:** an intermediate encoding of those raw entries,
  in row-major lower-triangle order, with exact integer endpoints on grid
  10^-400 and a completed-row count. Even count 84 does not certify finite
  sign until the final constructor checks finish.
- **Constructor binding:** the aperture, dimension, approximation orders,
  interval precision, logarithm precision and SHA-256 hashes of the wrapper,
  core, exact polynomial arithmetic, kernel integrator, logarithm enclosure
  and codec. Recovery requires exact equality of the binding dictionary.
- **Atomic checkpoint replacement:** a complete deterministic gzip member is
  written to a temporary sibling and then replaces the prior checkpoint.
  Reading during computation sees a complete previous or subsequent member.
- **Actual row-recovery control:** comparison of a fresh computation through
  row two with a separate computation stopped at row one and resumed through
  row two, using the actual native constructor. It certifies equality of
  those intermediate intervals only.
- **Synthetic codec control:** a round-trip or invalid-state test on artificial
  rational entries. It certifies codec behavior only and supplies no native
  form or positivity witness.

No checkpoint is a replacement for the native entry-width, full and shifted
finite pivots, parity and negative controls; nor does finite native sign
replace a matching complete source residual Gram and corrected Schur sign.
The recovery note is
`notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_ROW_RECOVERY_092_20261006.md`.
