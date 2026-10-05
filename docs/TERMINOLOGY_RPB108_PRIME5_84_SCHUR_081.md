# RPB108 actual prime-5 84-source residual Gram and corrected form

- Aperture a=81/100, physical basis phi_n(x)=sqrt((2n+1)/(2a)) P_n(x/a), n=0..83. E84 is their span and P84 is the matching physical orthogonal projection. Q84 is the complete actual native restriction in that basis.
- S84 is the actual residual source map, with columns (1-P84) A phi_n. Shat84 is its certified polynomial/endpoint-log surrogate. `R84=S84^*S84` and `Rhat84=Shat84^*Shat84`; the latter includes every endpoint-log/log, endpoint-log/smooth and smooth/smooth term and subtracts the complete matching projection.
- eta bounds ||S84-Shat84||. M bounds ||Shat84|| through the upper enclosed Gram trace. delta=eta(2M+eta) bounds ||R84-Rhat84||; orthogonal projection does not increase the source error.
- c=51/100 is the actual physical complement lower bound; beta=100/51 is its inverse energy factor. The sufficient corrected form is K84=Q84-beta R84. Interval certification tests Q84-beta Rhat84-beta delta I-tau I with tau>0. A positive result bounds K84 below by tau I. A negative direction of this sufficient estimator alone is not a negative witness for the full physical form.
- The energy-orthogonal complement lift has squared norm bounded by beta^2(trace_upper(Rhat84)+delta). Any certified integer L strictly above that square root gives the whole-domain bound min(tau/[2(1+L^2)],c/2).
- Nine actual panels retain prime powers 2,3,4,5, both translation orientations, both pole moments, endpoint logarithms and regular differences. The existing source coefficient grid is 10^-60; complete Gram moments use outward grid 10^-600 and logarithm series 500.
- Exact integer Hankel integration forms centers sum u_i v_j(l_{i+j}+h_{i+j}) and radii sum |u_i v_j|(h_{i+j}-l_{i+j}). Carry-free arbitrary-precision integer packing evaluates the convolution windows exactly; division by twice the moment grid and coefficient denominators gives outward intervals.

The complete actual corrected form at a=81/100 is positive with physical margin 1/100000000000000000000000000000. The full-domain physical quadratic form satisfies Q(h)>=1/20200000000000000000000000000000 ||h||_2^2. This closes the matching 84-coordinate sign problem, excludes fixed-aperture weak null modes and establishes fixed-aperture full-source unit domination.

Gram endpoints use lossless finite-decimal strings on the outward grid, with exact rational round-trip verification for all 14,112 endpoints per run.

These are rational/outward interval analytic certificates, not Lean proofs. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms and CI are unchanged.
