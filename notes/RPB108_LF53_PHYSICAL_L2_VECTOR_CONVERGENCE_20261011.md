# RPB108 — LF53: physical L2 vector convergence

## Submitted theorems

Establish full-line MemLp 2 membership of cutoff spatial actions extended by zero from the closed cap. The cap's two endpoints are null, so checked interior membership transports to the closed cap, then indicator membership gives whole-line membership.

Transport the submitted cap L2 error limit to the whole physical line. The difference of zero extensions is the indicator of the difference, and the indicator seminorm equals the restricted-measure seminorm. Again, endpoints are null. Finally use the pinned Mathlib toLp convergence equivalence to derive convergence of the actual physical L2 vectors to the existing neutralLogMetricEndpointCandidateL2 representative. No new definitions or convergence hypotheses are introduced.

## Validation boundary

LF52 commit 1dac873bdc97222ef758cc2dbb9607bf7be90b92 run 38167440619, job 114552824036, was still building the targeted chain during LF53 preparation. LF52 repairs LF51's missing ENNReal scope and submits time-action L2 transfer. LF50 remains the latest full-root success. LF52–LF53 await cumulative CI; no local Lean executable is available. The toLp and indicator seminorm APIs were read at pinned Mathlib revision 5ed2965256430c3649e86755f9576b54eca72435.

## Remaining

Validate convergence, derive physical L2 test pairings, and identify the spectral source. Full-line convergence here concerns the cap-supported source representatives, not convergence of the untruncated exterior action on the entire line. No aperture positivity, F4 closure, or RH claim.
