# RPB108 LF27: affine transport elaboration repairs

LF26 run 38104201830, job 114366609602, compiled EndpointL2 successfully.
LF21's squared-log integrability and actual endpoint-tail MemLp 2 on finite
distance intervals are now module-level kernel checked. The checked boundary
also includes LF05 through LF10, LF12, LF13 repaired by LF20, and LF19.
Complete-root validation remains LF01 through LF04.

The cumulative build failed in CapL2 and ExteriorSplit. LF27 addresses
all observed diagnostics: construct the volume-preserving map c-y by
composing negation and left addition, replacing the unavailable subtraction
convenience name; give transported exterior convergence an explicit
IntegrableOn type before invoking congr_fun; simplify measurable-equivalence
applications in the embedding proof; and expose half-line memberships as
scalar inequalities before linarith proves the sign of x-y.

No theorem statement, interval, modulus, analytic assumption or numerical
constant changes. Exterior convergence is still derived from the checked
positive-distance tail convergence. Physical-cap L2 is still derived from
the checked distance-variable L2 theorem. These transport modules and the
downstream zero-extension representative require a fresh cumulative check.

The complete-root and unfinished-declaration checks were skipped after
the targeted failure. No local Lean executable is available. No hand-written
sorry, admit or project axiom is introduced. Research refs remain untouched.
After transport compilation, combine the convergent internal and exterior
pieces into the complete complex jump split, then establish mixture exchange,
weak source attachment and spectral source identity. No aperture, F4 or RH
claim is made.
