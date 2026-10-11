# RPB108 LF25: squared-log exponent cast normalization

LF22 run 38103549861, job 114364244474, compiled EndpointLog successfully.
The checked module boundary now includes LF13's logarithmic near-tail,
global absolute-log and two-endpoint budgets, repaired by LF20, together
with LF05 through LF10, LF12 and LF19. Complete-root validation remains
LF01 through LF04.

The cumulative build stopped in EndpointL2 at the helper identifying the
square of a real power. Rewriting the natural square through rpow_natCast
and rpow_mul left the equality d^(a*(2:Nat cast to Real))=d^(a*2).
LF25 adds norm_num to normalize that cast. This changes no analytic bound,
theorem statement or trial hypothesis. The remaining EndpointL2 proof
produced no additional diagnostics in that run, but the module is not
considered checked until it compiles as a whole.

LF24 run 38103969680 is in progress at submission. EndpointL2, physical
cap L2, zero-extension representative and exterior half-line identities
still await cumulative checking. The complete root and unfinished-
declaration checks were skipped after the targeted failure. There is no
local Lean executable. No hand-written sorry, admit or project axiom is
introduced. Research refs remain untouched.

After the L2 chain compiles, combine internal cancellation and both
exterior integrals into the complete complex jump split, then prove
mixture exchange and weak physical attachment. Spectral source identity
remains open. No aperture, F4 or RH claim is made.
