# RPB108 LF22: physical cap endpoint and complete candidate L2

Submit five actual function membership results on (-B,B), for B>=0:
the left tail at distance B-x, the right tail at B+x, their exterior sum,
the exterior product with a bounded measurable trial, and the complete
endpoint candidate for a bounded measurable trial with an explicit
Lipschitz modulus on [-B,B].

Translation and reflection preserve real volume. Restrict these maps to
preimages of (0,2B], compose the LF21 actual tail L2 theorem, and restrict
to the cap interior. Both exterior contributions are retained. A pointwise
trial bound controls the complex exterior product by M times the positive
exterior source. The finite-cap internal jump integral has norm <=2*B*L
by LF10 and is measurable by LF19, hence belongs to L2 on the finite cap.
Adding these three actual terms yields the complete candidate membership.

The theorem assumes trial measurability, a pointwise bound and a modulus;
it does not assume candidate or exterior L2 membership. This is still
function membership, not weak source attachment, an operator-domain
identification or equality with the spectral source. Closed-cap null-
endpoint transport and full-line zero extension remain separate steps.

At submission LF19 run 38102835917 was in progress, and LF21 run
38103400561 was pending. The checked module boundary remains LF05 through
LF10 plus LF12; complete-root validation remains LF01 through LF04.
LF13/LF19/LF20/LF21 and these LF22 statements await cumulative CI.
No local Lean executable is available. Targeted CI and root imports include
the new module. No hand-written sorry, admit or project axiom is introduced.
Research refs remain unchanged. No aperture, F4 or RH claim is made.
