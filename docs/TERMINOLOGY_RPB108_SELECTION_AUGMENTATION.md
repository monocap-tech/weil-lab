# RPB108 selection augmentation terminology

Registered 2026-10-06 before the companion theorem.

- `A`: fixed actual full native Riesz operator; augmenting the selection does not change A or the physical native form.
- `R:H->M`, `T:H->L`: old and disjoint added finite actual negative-coordinate maps, with original weights; `Rplus=(R,T)`. These are coordinate selections of the same complete actual analysis.
- `G=A+R*R`, `Gplus=G+T*T`: old and augmented effective covariances.
- `J=I+T G^-1 T*`, `B=R G^-1 T*`: finite Schur data, defined only when G is coercive. J is not the physical support inclusion.
- `D=I-RG^-1R*`, `Dplus=I-Rplus Gplus^-1 Rplus*`: finite source defects.
- `graph lift`: `u -> (u,B*u)` from ker D to ker Dplus. It differs from zero-padding unless the added actual samples vanish on the reconstructed physical vector.
- `blind kernel`: ker A intersect ker R at a nonnegative window. Finite augmentation can separate it but does not make the original prescribed G invertible.
- `e_s`, `eplus_s`: effective inverse energies of the same enlarged full-native residual, with different coercive selections.
- Same-vector transport here is finite-selection transport at one physical support (or comparison of gain functions for that same vector). It is not enlarged full-native null transport.
