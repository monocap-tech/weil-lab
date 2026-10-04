# Terminology: RPB108 explicit theta/count constants

Additive register; historical wording remains unchanged.

| Term | Definition | Scope |
| --- | --- | --- |
| Explicit actual theta decay | abs(evenKernel(0,t)-1)<=4 exp(-3t) for t>=1 | Analytic proof using pinned exact kernel series |
| Explicit raw-copy dyadic constant | A=864 in band count <=A(n+2)2^n | Analytic specialization of the existing theta/Jensen chain; not Lean-certified |
| Numerical fixed-packet tail envelope | 6912 a exp(a)||h'||^2(2N+6)2^-N | Signed cutoff error; finite data still required |
