# RPB-108 native finite margin terminology

- **Native finite margin:** a certified lower bound on the actual native form restricted to the physical orthonormal Legendre span of degrees 0 through 83 at aperture 81/100. It concerns that finite span, not all of D_a.
- **Stored interval matrix:** the unchanged 2026-10-05 native matrix certificate, pinned by Git blob SHA 513b970b3d7d521c6d9f8b8f6551d550c99584d7.
- **Shifted pivot certificate:** strictly positive lower endpoints from outward rational interval elimination applied to Q_84-tau I, separately on exact reflection parity blocks.
- **Uncertified shift:** a shift for which this interval elimination fails to certify positive pivots. It does not imply that the true shifted matrix is indefinite.
- **Whole-domain bound:** the existing bound on all of D_(81/100), obtained using the full corrected Schur construction. This pass does not update it.

The new finite margin is 10^(-18); the previous finite margin was 10^(-28).
Historical packet attachment, F4, FULL TRANSPORT CLOSED, and RH closure remain open.
