# RPB108 DNE13 — Compensated constant source diagnostic

At a=53/50 use normalized physical Legendre modes e_n and original signed Weil source L_Q.

- Two-mode constant trial: w=e0-c112 e112-c114 e114, where the numerical candidate c solves the 2x2 native high block equation. This candidate is not authenticated interval data.
- Frozen rational trial: wbar=e0+(7094302/10^9)e112-(5131477/10^9)e114. The coefficients are exact; their adequacy and source integrals are not certified by a floating calculation.
- Complete retained projection: P_E projects onto span{e0,e2,...,e110}. P_F=I-P_E. It removes 56 even modes, not merely e0.
- Physical residual square: P(w)=||P_F L_Q w||_2^2. It includes all archimedean/prime/pole correlations and any remaining high trial pairings.
- Scalar residual budget: kappa Q(w,w), with inherited ORIGINAL signed F112 lower floor kappa=207/1000. P(w)<kappa Q(w,w) is a sufficient scalar Schur certificate for the low line represented by w; it is not an all-E112 matrix certificate.

Numerical integration orders are convergence diagnostics, never outward interval bounds. Source-level cancellation and full retained projection are computed explicitly.
