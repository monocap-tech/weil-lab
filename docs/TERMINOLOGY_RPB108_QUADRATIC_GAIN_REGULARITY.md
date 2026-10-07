# RPB108 quadratic gain regularity terminology

Registered for the global/F4 lane, 2026-10-06, before the companion theorem.

- `c`: hypothetical actual nonnegative null support; `K_c`: its full native kernel, not a selected-background kernel.
- `b`: fixed larger support with coercive effective covariance and no newly activated prime between `2c` and `2b`.
- `R_t,G_t,C_t`: the fixed finite actual selection, effective covariance and reduced signed compensator of the fresh fixed packet, restricted to support `t`.
- `Lambda(t)=R_t G_t^{-1} R_t* = C_t* C_t`: finite response covariance. This is distinct from the positive coefficient subspace `L_t` and the source defect `D(t)=I-Lambda(t)`.
- `s=t-c`, `Ih`: unchanged physical zero extension into support `t`; no dilation is used.
- `e_s(h)`: effective inverse energy of the enlarged full mixed residual, equal to the gain excess for the unchanged coefficient `u=-R_c h`.
- `E_1`: coefficients in `ker D(c)` whose reconstructed actual null vector is globally `H^1(R)`.
- Quadratic gain bound: `e_s(h)=O(s^2)` as `s` decreases to zero, with a constant allowed to depend on `h`. It is not implied by continuity or strict Loewner order.
- `F_h(s)`: signed real translation boundary flux with the orientation in EXACT_TRANSLATION_BOUNDARY_FLUX; a large negative flux is the missing cancellation, not a large positive flux.

All assertions about a nonzero null vector are conditional; no actual contact existence is asserted. Fresh actual packet construction does not identify a prescribed historical packet.
