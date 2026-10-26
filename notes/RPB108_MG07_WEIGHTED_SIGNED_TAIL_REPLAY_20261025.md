# GitHub-first weighted signed-tail acceptance

This focused replay consumes the accepted original 7168-cell artifact from
run 40251400717, artifact 12620838774, source commit
bf56f5ca1a17305671f58c8a5b785898a1843d55. The workflow checks run success,
source identity, artifact identity, archive SHA-256 and exact JSON SHA-256.
It fails closed if the artifact expires or any identity changes.

The repository's original SI10 cover is recomputed. Its 107 clusters contain
973 unresolved leaves; 94 clusters begin at or above 12, none straddles 12.
Their certified two-sided mass is 502297951/32000000. Retaining each left
endpoint proves the exact-rational inequality

    S = sum_(a_j >= 12) M_j/a_j^2 < 423/25000 = 0.01692.

For the original accepted packet estimates |hhat(xi)| <= beta/|xi|,
negative high-frequency action is <= beta^2 S. The lowband and physical-pole
Fractions are preserved from the accepted artifact; no low-frequency
quadrature is rerun. This gives strict original signed-action lower bounds
25772.048 (direct ray) and 1691.180 (second ray). Both displayed lower bounds
are downward truncations. Mass already includes the reflected frequencies;
no extra factor of two is used.

This accepts only an exact rational composition. SI06 exterior positivity,
the SI10 cover's analytic inequalities, original Fourier normalization,
physical pole realization and source/domain assumptions are inherited.
No whole-original signed odd positivity, even criterion, CC27, Weil or RH
closure follows. The separate accepted signed 2D workflow remains stronger
in subspace scope; this replay supplies custody for the sharper two-ray
numbers without repeating its expensive low-frequency integration.

The canonical active obligation and acceptance conditions are unchanged.
