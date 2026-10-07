# RPB108: mixed sharp-height compensation

Additive definitions, 2026-10-07. Retain original actual paired/copy source coordinates and their normalization weights. For supported canonical f,g define the finite sesquilinear head

    B_T(f,g)=sum_(|theta_q|<=T) |theta_q|
                 [p_q(f) overline(p_q(g))-n_q(f) overline(n_q(g))].

The convention is linear in the first variable. B_T(f,f)=S_f(T). Every original multiplicity/copy weight remains in this sum. This is a finite head, not an unregularized infinite first-height pairing.

Write eta=2/pi. For actual contact kernel K and the NF48 actual-row projection C_X, a smooth core v has kernel correction k=C_X v and energy representative e=R_X v=v-k. Mixed height compensation means the limits of B_T(k,k), B_T(e,e) and B_T(k,e), divided by log T, are respectively eta|kappa_R(k)|^2, eta|kappa_R(k)|^2 and -eta|kappa_R(k)|^2. The unweighted native pairing Q(k,e)=0 is a different equation.

A regularity-preserving kernel projection would be a bounded projection P:D_a->K with P(v) in global H1 for every smooth compact v. The theorem below excludes such a projection when K is nonzero. No endpoint-exclusion criterion or altered source dictionary is introduced.
