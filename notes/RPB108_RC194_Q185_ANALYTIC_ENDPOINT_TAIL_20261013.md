# RC194: retain the complete signed endpoint tail of q185

Starting checkpoint: RC193, fccad016257120934190076a8761c1b3a51ba07a. Aperture11/10, supported canonical operator M=D^-1 L, exact finite q185, and D-energy norm are unchanged.

RC185 discarded the endpoint output beyond4094 and paid its entire norm. RC194 represents that tail using25 exact signed moments and pays only the geometric remainder.

| Same-source absolute D-norm bound | RC185 | RC194 |
|---|---:|---:|
| Complete canonical q185 action error | 0.00000896200771676814 | <0.000000001053302 |
| Unrepresented endpoint output contribution | 0.000008960954415172735 | <6.110e-66 |

The complete action bound improves by more than8508 times. Its leading remaining payment is the unchanged regular-action upper1.0533015952920647e-9. Decimal summaries are outward summaries of exact rational certificate bounds.

## Uniform tail identity and bound

Let lambda_m=m(m+1), lambda=256*257, and eta_n=(2n+1)/(lambda_n D_n). Outside the finite input, all n>m, so the endpoint kernel gives

Cq185_n = eta_n sum_m q185_m/(1-lambda_m/lambda_n).

Expand each denominator through order24. The retained signed moments are mu_k=sum_m q185_m(lambda_m/lambda)^k. The coefficient remainder factor is exactly

sum_m q185_m (lambda_m/lambda_n)^25/(1-lambda_m/lambda_n).

Put A=sum_m |q185_m|, rho=lambda/(4096*4097), and T=B/[(s_lower+H_4094)*4093*4094]. The inherited eta-tail estimate gives sum_{even n>=4096} ||eta_n Pn||_D^2 <= T. Therefore the full unrepresented endpoint tail has D-norm at most sqrt(T) A rho^25/(1-rho). The certificate evaluates this upper below6.110e-66. Exact signed moments introduce no moment-rounding error.

This is a bound for every omitted degree, not a numerical extrapolation. Exact rational controls at4096,8192,65536 separately verify the geometric identity and its pointwise bound; they are controls rather than the proof of the infinite-tail estimate.

## Prefix and complete action

The finite endpoint polynomial is referenced by the SHA-256-bound RC185 certificate. Its coefficient radii are summed in the D-energy norm using the upper diagonal endpoint s_upper+H_n. The negative-r polynomial's coefficient radii are paid similarly. RC185's regular polynomial and its full regular error remain unchanged. The refined action is q185 + finite endpoint prefix + analytic endpoint tail + negative-r polynomial + regular polynomial.

The complete bound combines the endpoint prefix/remainder error, negative-r coefficient error and regular error. The q185 canonical pairing is independently re-enclosed from its unchanged finite coefficients, with the new complete action payment, and still lies strictly between the structural aD and2D bounds. The old actual-residual-to-q185 approximation error remains unchanged and is retained separately; action accuracy on q185 does not imply that it exactly equals the actual residual.

## Verification and remaining work

Four certificates are SHA-256 bound: RC193, RC185, RC129, RC121. Direct historical source/metric attachments are checked. Forward generation and reversed-order replay reproduce the entire certificate exactly, including all moments and control values.

```
python scripts/validate_rpb108_rc194_q185_analytic_endpoint_tail.py --output certificates/rpb108_rc194_q185_analytic_endpoint_tail.json
python scripts/validate_rpb108_rc194_q185_analytic_endpoint_tail.py --replay --output certificates/rpb108_rc194_q185_analytic_endpoint_tail.json
```

No inverse response is evaluated in this pass. The latest five-source inverse width remains1.254303 with ratio2.508606 and failed acceptance. The accepted smaller-family results remain intact. Stage I, full native coverage, original Weil positivity, RH, F4 and Lean closure remain open/unclaimed.

Next: rebuild complete mixed rows and all residual/tail matrices using RC192, RC193 and RC194, then reevaluate the unchanged five-source inverse. The new analytic tail must be included in mixed pairings, trial energies and residuals; old matrices cannot be reused with a smaller substituted error number.
