# IV130 checkpoint — compiler-driven repair of IV125 and integrated IV129 gate

Native run 45751086812 at db661e36d7d976c698d530e272e2a10f127963e7 failed in IV125. IV124 built successfully (5 standard-axiom declarations verified from native log); IV125 cell cancellation itself has standard axioms. The later audit and compiled custody step was skipped, so no claim of compiled artifact custody for these results.

Four IV125 repairs: make pointwise Pi.sub explicit in the integrability proof; normalize the polynomial band integral and discharge the residual propositional goal; remove redundant dsimp on the logarithm nonnegativity goal; use the correct additive monotonicity orientation for exp(1)+T. Apply the same polynomial normalization fix to IV126's a.e. receiver. No theorem statements changed.

This commit preserves the IV128–129 descendants and reuses the IV127 workflow on the IV129 branch for a single dedicated integrated build of IV124–129, with all 34 named declarations and six compiled modules. Native acceptance is pending. Second Schur implementation is deferred until these dependencies compile; this checkpoint introduces no new mathematical claim. Other inherited workflows may still run due to broad triggers.
