# RC206 terminology

A directional action-error Gram is a matrix upper bound for all mixtures of the fixed eight trial actions. Its shape, rather than only its largest factor relative to the source Gram, determines the cost of the variational and residual inverse bounds.

For positive raw trial weights w_i and certified error norms epsilon_i, C=sum_i epsilon_i/w_i. The diagonal raw bound H_ii=C epsilon_i w_i dominates epsilon epsilon^T. Triangle/Cauchy bounds give the action-error Gram E_triangle=Y^T H Y. The fixed-trial signed bound E_signed=(473/200000)G_lower is independently valid. Any convex combination lambda E_triangle+(1-lambda)E_signed, 0<=lambda<=1, is therefore valid for the same error map.

RC206 jointly optimizes weights, the convex mix, and positive Young parameters. Numerical calculations propose rational parameters; exact rational PSD checks verify their consequences. Reversed-order replay does not rerun optimization. A directional inverse improvement does not imply that the uniform scalar action-error factor improved, or that the new error Gram is smaller in every direction.

The actual source/trial carriers, nominal residual matrices and complete signed infinite tails are unchanged. RC203's physical reconstruction is inherited as a certified premise. Stage I, native source/odd-parity coverage, RH, F4 and Lean closure remain open.
