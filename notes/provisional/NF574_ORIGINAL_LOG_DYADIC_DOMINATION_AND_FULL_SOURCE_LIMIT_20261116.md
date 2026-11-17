# NF574 — actual original endpoint-log dyadic domination and full-source limit interface

Stacked on NF573 #605. All new proofs are candidates, not newly Lean-certified. NF568–NF573 checks inspected remained queued; no new compiler diagnostics.

Recovered the actual NF524/NF528 historical endpoint-log target:
ell_U(x)=sgn(x) 1_{B-delta<|x|<B} U(|x|)/2 log(B/(B-|x|)), B=11/10, delta=1/500.
The source is the frozen NF494 U400 (SHA256 39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181). NF528 uses positive-collar affine compression about c=B-delta/2, odd reflection and even compact mollification. The prior analytic notes claim source strip decay C(1+log(2+t))/(1+t) for the endpoint and a uniform 8C for its seeds, with C=10^-4, and H^(1/4) convergence. These analytic source estimates and their formal proof are NOT replayed or verified anew here.

New ActualZetaOriginalLogDyadicEnvelope.lean defines the actual divisor index n(q)=Nat.log 2 (floor(|Im rho_q|)+1) and W(q)=(n(q)+2)^2 4^(-n(q)). Uses existing actual multiplicity-preserving count #D_n <= A(n+2)2^n to implement summability: band sum <= A(n+2)^3 2^(-n). The literal strip envelope squared is <=4 W(q). No quartic or stronger smooth-source decay is substituted for the logarithmic endpoint.

New ActualZetaOriginalLogDyadicGraphLimit.lean implements dominated convergence of both literal l² source components using Mathlib Tannery and lp.hasSum_norm, followed by product/subtype convergence in the genuine complete source domain. For any actual log carrier k and g_i converging in that carrier norm, if both exact unnormalized source families for k and every g_i have a common squared dyadic majorant, constructs graph lifts retaining k, g_i exactly and proves full graph convergence. Difference squared domination uses 4 times the common bound. No graph membership of k is assumed.

New ActualZetaOriginalLogStripGraphLimit.lean converts the historical raw strip envelope into the needed common squared source majorant for both actual P/N samples. Uses open-strip zero and conjugate ordinate, same height, and exact raw sqrt(2) normalization. The theorem at B=11/10 requires a common finite constant M and convergence in the genuine log carrier, then produces same-vector graph membership and convergence. It does not use Gram positivity or exact moment matching.

Still open in Lean: define and admit the genuine nonsmooth U400 source ell_U in the log carrier (without requiring H¹); source M0/M1 endpoint-log estimates; formal compression/mollification strip bound and genuine log-norm convergence; all NF574 new compilation. The earlier NF528 argument is an analytic proof plan, not a completed formal source certificate. Once inputs and NF574 pass, NF573 can preserve the full graph convergence under the exact canonical moment correction. Other remaining NF527 full coercivity, NF539 identification, W_ODD_NEG and RH are not discharged. One focused CI job; do not treat pending dependencies as certified.
