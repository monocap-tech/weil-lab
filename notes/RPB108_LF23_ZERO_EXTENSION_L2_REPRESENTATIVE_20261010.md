# RPB108 LF23: closed cap and physical L2 candidate representative

Submit closed-cap candidate L2 membership by equality of the restricted
volume measures on (-B,B) and [-B,B]. The endpoints are null, including
the degenerate cap B=0. This does not assert convergence of the improper
tail integral at zero distance.

Define the actual candidate zero extension as the closed-cap indicator
times the endpoint formula. Its full-line MemLp 2 membership follows from
the closed-cap result and the indicator/restricted-measure equivalence.
Construct a RealComplexL2 representative with toLp, and retain its exact
almost-everywhere equality with the zero-extended formula. The zero
extension is pointwise zero outside the cap.

These results derive membership from trial measurability, a pointwise
bound and an explicit Lipschitz modulus. Weak metric attachment and
spectral source identity are not assumptions or conclusions. Splitting
the original zero-extended jump operator, mixture exchange and physical
limit attachment still require proof.

LF19 run 38102835917, job 114363069856, compiled EndpointMeasurable.
It then failed at the EndpointLog convenience name already replaced by
LF20. Checked modules now include LF05 through LF10, LF12 and LF19;
complete-root validation remains LF01 through LF04. LF22 run 38103549861
is in progress at submission. LF13/LF20/LF21/LF22 and these LF23 results
await cumulative CI. No local Lean executable is available. Targeted CI
and root imports include the new module. No hand-written sorry, admit or
project axiom is introduced. Research refs remain unchanged. No aperture,
F4 or RH claim is made.
