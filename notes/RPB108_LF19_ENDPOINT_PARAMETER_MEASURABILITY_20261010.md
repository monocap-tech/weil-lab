# RPB108 LF19: endpoint candidate parameter measurability

Submit four measurability statements for the actual physical formulas:
the moving endpoint tail, the sum of both exterior tails, the internal
finite-cap jump integral as a function of its observation point, and the
complete endpoint candidate for an arbitrary measurable complex trial.

The moving tail is expressed as a full-line integral of the measurable
indicator of d<r times ell(r). Parameter measurability of the Bochner
integral then applies; the indicator integral is exactly the original
restricted-measure integral. The internal jump proof uses a jointly
measurable complex integrand and the actual finite-cap restricted measure.
No uniform integrability or convergence hypothesis is silently introduced.

This is a prerequisite for L2 membership, not its proof. Positive-distance
convergence and endpoint bounds remain separate. Totalized values at or
beyond endpoints do not establish analytic convergence there.

At submission, LF18 run 38102732677 is in progress. LF17 compiled LF05
through LF10; full-root validation remains LF01 through LF04. LF18's
EndpointBounds repair, EndpointLog and these four new statements await
kernel checking. There is no local Lean executable. Targeted CI and root
imports include the new module. No hand-written sorry, admit or project
axiom is introduced; research refs remain unchanged.

Next: resolve compiler diagnostics, establish squared-log integrability
and endpoint L2 membership, then complete mixture exchange, zero-extension
splitting and physical/spectral source identification. No aperture, F4 or
RH claim is made.
