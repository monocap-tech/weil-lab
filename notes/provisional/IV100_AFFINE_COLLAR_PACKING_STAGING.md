# IV100 — Affine carrier packing (inactive staging)

Base: IV099 candidate 5c2dbff19447bee07921a66d617b8f6b8b1f870a; IV099 native receipts are pending. No active workflow and no PR in this staging gate.

11 source candidates: affine compact support, chain rule, exact Lebesgue Jacobian, mass and derivative energy scaling, uniform scaled energy budget, positive mass, and exact rational cell geometry. Given a>0, the same IV097 plateau has m(a,b)=m0/a, e(a,b)=a e0, hence e/m <= 16000000 a^2. For k>0, index i<k, use a=k and shift b=1099/1000 - k*(1099/1000-3/4000) - (2i+1)*(3/4000). Nonzero support lies strictly inside the ith cell of the original right plateau interval. Pairwise strict cells disjoint, with zero function and derivative at boundaries. Candidate geometry proves containment and nonoverlap. 

Next source obligations: instantiate Fin k family, original collar closure, function and derivative disjointness, apply IV099 receiver for arbitrary coefficients, choose cutoff N>=8945*k to guarantee 1/5 margin and prove nondegeneracy. C=16000000*k^2. This is a proposed arbitrary finite rank within a previously positive restricted collar, not a global complement or RH proof. No uniform fixed cutoff as k grows. Native checks not yet run. No adoption or merge.

Central ledger #935.
