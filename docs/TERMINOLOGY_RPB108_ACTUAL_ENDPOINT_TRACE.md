# RPB108: actual averaged endpoint traces

Date: 2026-10-07 UTC. Additive definitions.

Use the full-native K_a, exact q_h and strip coordinates from ENDPOINT_STRIP_MATCHING.

- H_R(L)=exp(L) integral_0^(exp(-L)) h(a-v)dv; J_R(L)=J_R(exp(-L)). Left versions use h(-a+v).
- The **averaged right endpoint trace** is kappa_R(h)=lim_(L->infinity) sqrt(L)H_R(L), whose existence on actual K is proved in the linked note. It is a linear functional on K.
- The **scaled right profile** is sqrt(L_epsilon)h(a-epsilon t), 0<t<1. Its proved trace is in L2(0,1), not a claimed pointwise normalized trace at every t approaching the edge.
- K_reg=K_a intersect global H1. The **rough quotient** is K_a/K_reg, not a quotient of the general divisor or physical carrier.
- kappa_R^*kappa_R denotes the Hermitian rank-at-most-one form (h,u)->kappa_R(h)conj(kappa_R(u)).

These traces are neither the unrenormalized improper inverse moment nor the historical retained packet coordinates. A trace may vanish on nonzero regular vectors in a higher-dimensional actual kernel.
