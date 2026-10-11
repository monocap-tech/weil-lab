# RPB108 LF13: logarithmic endpoint majorant

Adds `NeutralLogMetricEndpointLog.lean` on the isolated formalization branch.

## Four public declarations submitted

The endpoint tail splits exactly into its interval integral from d to one
and its tail beyond one, for every d>0. This uses actual integrability of
both improper tails from LF12, rather than an unproved split of totalized
integrals.

For 0<d<=1 the interval term is at most `log(1/d)`, by LF09's reciprocal
majorant and the exact inverse integral. The far term is at most
`C=1/(2*pi^2*exp(1))`. Thus `tail(d) <= log(1/d)+C` near an endpoint.
For d>1, LF12 gives `tail(d) <= C/d <= C`. Together these establish the
global positive-distance bound `tail(d) <= C+abs(log(d))`.

The two-tail exterior source at |x|<B is therefore bounded by
`2*C + abs(log(B-x)) + abs(log(B+x))`. Both terms remain present. This
supplies the correct growth class for endpoint L2 control; the earlier
reciprocal-distance bound alone could not establish that control.

## Validation boundary

LF01 through LF04 remain checked by complete hosted builds. LF11's repair
run 38098224642 is still running its targeted build when LF13 is prepared.
LF05 onward remain unchecked until hosted compilation succeeds. LF13 is
added to the cumulative targeted build and complete root. There is no
local Lean executable; an unfinished-declaration scan is not a kernel check.

## Next cursor

Resolve any remaining hosted diagnostics. Establish square integrability
of the actual two-tail exterior source using this logarithmic majorant,
including parameter measurability and endpoint a.e. handling. Then combine
with the bounded internal term for measurable bounded Lipschitz trials.
Poisson mixture exchange, zero-extension splitting, physical L2 convergence
and equality with the spectral metric source remain open.

No research branch ref or PR base is changed. No aperture positivity,
Green-domain identification, F4 closure or RH claim is made.
