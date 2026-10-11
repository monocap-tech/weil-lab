# RPB108 LF11: hosted diagnostic repair

The first hosted compilation of the cumulative analytic submissions exposed
errors in LF05, LF06 and LF07. This pass repairs those errors before adding
further analytic declarations. LF01 through LF04 remain the checked boundary.

## Observed diagnostics

- LF05 run 38096709611 failed its complete-root build solely in the new
  `NeutralLogMetricEndpointSource` module. Topology notation was not opened,
  and `add_neg_eq_sub` was not a recognized rewrite name.
- LF10 run 38097558393, job 114346881403, failed its targeted analytic build
  in the endpoint module, Laplace module and Poisson module. The missing
  topology scope affected both endpoint and Laplace limit statements.
- The Poisson integrand's intended cast of real absolute value was elaborated
  as complex absolute value, requiring the nonexistent lattice on complex
  numbers. The set-integral congruences also left the measure unspecified.
  The Fourier exponent simplification left a `starRingEnd` application.

## Repair submitted

Open the Topology scope explicitly in the endpoint and Laplace modules.
Use the established reverse `sub_eq_add_neg` rewrite for endpoint reflection.
Force the absolute value to be real before casting it into the complex
Poisson exponent. Specify volume for both set-integral congruences. Simplify
`starRingEnd_apply` before the real-star simplification in the Fourier pair.

There are no new mathematical hypotheses or theorem declarations. Compiler
warnings that erroneous declarations use an inserted sorry are consequences
of failed elaboration; they are not accepted proofs or hand-written sorry
tokens. These failed runs provide no kernel certification of LF05 onward.

## Validation and next cursor

The repair is submitted for a fresh cumulative targeted build and full-root
build. LF05 through LF10 remain unchecked until that build succeeds. Local
source checks cannot substitute for Lean compilation. Research branch refs
and the PR base remain unchanged.

After the repaired source foundations compile, resume exponential far-tail
domination and genuine endpoint-tail convergence. Endpoint L2 control,
Poisson mixture exchange, zero-extension splitting and identification with
the spectral source remain open. No aperture positivity, F4 or RH claim.
