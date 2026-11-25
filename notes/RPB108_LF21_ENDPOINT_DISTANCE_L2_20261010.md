# RPB108 LF21: actual endpoint-tail L2 on finite distance intervals

Submit four statements: a power majorant for log(d)^2 for every d>0,
integrability of the squared logarithm on (0,D], log in MemLp 2 on that
interval, and the actual endpoint tail in MemLp 2 there.

The explicit majorant is 16*(d^(-1/2)+d^(1/2)). Apply log(u)<=u-1 at
u=d^(-1/4) below distance one and at u=d^(1/4) above it, then square.
Both powers have exponent greater than -1, so their endpoint integrals
converge. The actual tail is measurable by LF19 and bounded by
C+abs(log(d)) by LF13/LF20; domination gives its L2 membership without
assuming tail L2 membership as an input.

This is membership in the distance variable under volume restricted to
(0,D]. The left and right physical cap endpoints still require translation
and reflection transport, followed by construction of the complete complex
candidate in L2. Mixture exchange, weak attachment, zero-extension splitting
and identification with the spectral source remain open.

Validation at submission: LF18 compiled EndpointBounds, extending checked
modules to LF12 as well as LF05 through LF10. LF19 run 38102835917 is still
in progress and LF20 run 38103238320 is pending. LF13/LF19/LF20 and these
new LF21 statements remain unchecked. Full-root validation remains LF01
through LF04. No local Lean executable is available. The new module is
included in targeted CI and root imports. No hand-written sorry, admit or
project axiom is introduced. Research refs remain unchanged. No aperture,
F4 or RH claim is made.
