# RC218 — coupled residual interface and shared source-tail refinement

Parent: RC217 `fa20e123c4d0711e7dbb18c8bfdbca8b4c25d97e`.

RC218 assembles the full ten-trial/eight-response nominal residual Gram and transports the same action-error vector through both the variational and residual terms. It also replaces the broad entrywise source-tail uncertainty by a common-leading-tail Gram. The source family, operator, norm, and domain remain unchanged.

The best attained inverse enclosure uses the refined structural bounds, not the coupled trial bounds. Its relative width is **6.717377** with the new source Gram floor. On **RC217's identical comparison floor**, the width is **6.933992**, improving the old **12.263225** bound. This distinction is recorded explicitly; changing the Gram normalization is not silently presented as an enclosure improvement.

The inverse gate still fails its **0.5** threshold. Neither of the tested coupled trial maps improves on the refined structural enclosure. No expanded inverse acceptance, Stage I closure, or impossibility of acceptance is claimed.

## Reusable exact data

The materialized native-carrier artifact contains every historical native t10 finite center and generator radius through degree 16382 and every native delta = z_b6 − v10 center through degree 8190. Both historical hashes are reproduced. Their unchanged selected analytic moments and scales are included.

The prefix-interface artifact contains directed entry enclosures for all ten-trial source/source, source/nominal-action, and nominal-action/nominal-action pairings through degree **65534**. The nominal source/action matrix is not assumed symmetric. This interface can form new residual Grams for rational trial maps by matrix arithmetic, without rebuilding the native sources or repeating the prefix sums.

Signed source and action leading coefficients share the same infinite eta carrier. Nonleading absolute bounds and the common eta tail-energy bound are supplied. The full source-tail Gram retains the signed leading rank-one term before bounding the four nonleading source contributions. Finite lower source Grams remain valid because the omitted full source Gram is positive semidefinite. Native sources themselves are never replaced by truncations.

## Residual and coupled-error proof

For each trial map Y, define U = T Y and nominal residual Rhat = S − Mhat U. The finite residual Gram is formed from the joint prefix matrices, including all cancellation terms, before Loewner rounding. The full analytic residual tail keeps its signed common leading coefficient. All remaining tail generators are paid with a weighted triangle Gram; orthogonality is not assumed.

Two maps are evaluated: least residual on all ten trial vectors, and least residual on the eight response-source vectors. A complete action-error Gram bounds e = (M − Mhat)U. The inverse-response identity uses the same e in its variational and residual terms. Lower and upper Young parameters then bound U + Rhat and U + (2/a)Rhat, with the inherited spectral metric a = 32125/230953. Error payments are combined before Young inequalities rather than independently charged twice.

Numerical optimization proposes positive rational weights and parameters only. Enclosures, source and residual tails, gate decisions, and relative-width grid bounds are checked with exact rational PSD arithmetic. Floating eigenvalues may propose a narrow integer bracket; exact PSD tests establish both endpoints and the minimal 1e-6 grid bound. They do not certify acceptance.

Numerical diagnostics suggest that the current action-error envelope is a substantial part of the coupled trial uncertainty. Those diagnostics are not extra lower-bound certificates. Subsequent work must distinguish improving collective error payments from enriching the residual trial; an action-error pass alone does not establish inverse acceptance.

## Validation and retained results

Full reversed-order replay reproduces the certificate, materialized native carriers, and prefix interface exactly, using the stored rational proposals. All 81 immutable input/helper pins match the live parent tree. Incorrect input pins are rejected before reconstruction, and a synthetic coupled-envelope control passes. Publication is add-only.

The accepted RC210 six-source inverse width remains **0.436100**. The passed RC216 eight-source action-error factor remains **0.420465**. Source-range/augmentation obligations, odd coverage, Stage I, RH, F4, and Lean closure remain open.

Next cursor: RC219 — use the saved interface to audit and reduce the dominant coupled residual/error payments, including collective shared-tail cancellation or residual enrichment as justified by the data.
