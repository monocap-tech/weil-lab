# NF583 — original full graph limit infrastructure accepted; literal odd sequence integration

Stacked on NF582 #613. All new proofs in this pass are compiler-pending.

## Verified new milestones

- NF574 run 44031883892 job 133865520017 completed SUCCESS, including genuine two-source graph dominated convergence and specialization to the actual zero-strip raw samples at original B. This certifies the conditional full graph limit from log-carrier convergence and uniform strip control, not the endpoint approximation itself.
- NF581 run 44032558751 job 133867703891 accepted the full complex raw/window evaluation dictionary and the pointwise-sample logarithmic carrier limit; NF575 run 44032560045 job 133867706404 independently accepted the weighted logarithmic norm limit. Thus both graph-domination components now compile.
- NF582 run 44033840579 job 133871858557 reported SUCCESS for normalized mollifier recovery and the independent scalar Fourier limits/twisted integrability; NF579 run 44033840571 job 133871858398 independently accepted the mollifier and smooth seed module, and the pointwise continuum limit.
- NF580 run 44031883844 reported a remaining analytic identity diagnostic: the dependent oscillator branch was split, but the fixed parity ite inside the function was not. NF583 explicitly splits oscillator order parity before fun_prop. The unconditional Gram is still not accepted.
- NF581 literal endpoint admission still failed on three local diagnostics (unexpanded delta, pointwise function-square norm, and redundant rfl). Repairs committed.
- NF579 run 44033840571 reported only two errors in the exact complex transform module: missing Measure namespace for Haar integral_comp_div and redundant Complex.real_smul rewrite. Repaired. NF582's independent scale sequence also failed but its focused run was still running and complete logs unavailable. No acceptance claimed for that sequence.

## Mathematical integration

For the identical original half h, let O(h)(x)=h(x)-h(-x). With h integrable and supported on the original positive collar, the real odd transform is H(z)-H(-z) by the measure-preserving reflection and linearity of the actual integral. NF583 implements this, integrability and support of the literal half-sequence, and the odd sequence's uniform full strip bound and real-axis pointwise limits. It selects the same real odd Schwartz functions constructed by NF581, not a different approximating family.

The new terminal theorem neutralNF583OriginalEndpoint_actualSeedGraph uses the actual endpoint formula h_U and its physical L2 realization. Given measurable U, the original sup bound 2e-7, integrability of h_U, and its one-collar strip envelope, it returns the literal real odd supported Schwartz approximation sequence and full actual two-source graph lifts converging to the endpoint. No independent seed norm convergence, log-energy convergence, or seed strip assumption is imposed. Compiler-pending. Half-source integrability is still an explicit premise, but is mathematically immediate from its compact support and L2 membership; formal connection remains. The source-specific original U attachment and endpoint Fourier integration-by-parts estimate are not certified here.

No fresh numerical replay or local Lean build, no main merge, no axioms/sorry/admit intentionally introduced. Full signed Weil coercivity, W_ODD_NEG and RH OPEN.
