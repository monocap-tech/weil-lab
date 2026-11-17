# NF580 — genuine original global independence accepted; fixed-frequency limits

Stacked on NF579 PR #610. All newly written Lean proof scripts remain compiler pending.

## Verified compiler progress

- NF569 run 44029577788, job 133857981794 independently passed the generic square kernel transport and the actual original real finite-combination derivative and complex splitting modules.
- NF569 job 133857982085 passed the original analytic left and right kernel and global independence build step; NF570 run 44029578035 job 133857982708 independently passed the complete original oscillator-to-global-complex-independence job. Thus original global complex independence is now Lean accepted, not merely a proof candidate.
- NF570 job 133857982971 passed the original physical weighted-square and separation recheck, but the local-to-global analytic identity module failed; terminal canonical Gram build was skipped. The NF569 job also confirmed the actual real physical corrected test module compiled. Unconditional Gram positivity is NOT yet accepted.
- NF578 job 133857986789 reported success for the independent exact scalar and actual convolution geometry step (job still running when inspected).
- NF574 run 44029577671 job 133857981272 passed the actual multiplicity divisor logarithmic-square summable envelope step. The subsequent full graph dominated-convergence module failed on elaboration/simplification. Thus the infinite dyadic divisor majorant is now accepted, but the complete graph limit is not.
- NF579 job 133861153155 reported failures in the mollifier and transform build steps. Full job still running and its log was not downloadable when inspected.

## Compiler recovery

Repaired the four local-to-global analytic identity diagnostics: no-progress dsimp, faithful real-to-complex embedding, Pi complex scalar application, and conjugation notation. No mathematical premise is added. Also repaired the actual divisor graph limit's ambiguous constant Tendsto, real squared norm absolute-value simplification and residual id applications in the positive/negative inner-product limits.

## Independent scalar limits

New ActualZetaOriginalEndpointScalarLimits.lean implements three candidate ingredients without importing the pending mollifier or full graph modules.

1. For any family of actual normalized bumps of shrinking outer radius, at fixed real t the literal integral of rho(y)*exp(i*t*y) tends to 1. Use Mathlib's ContDiffBump.convolution_tendsto_right_of_continuous only for g(x)=exp(-i*t*x), evaluated at 0. This avoids approximate identity on the singular physical source altogether.
2. If h is integrable and u_n tends to t, the literal real-frequency Fourier integral H(u_n) tends to H(t), by DCT with majorant |h| and unit-modulus real exponential.
3. Compactly supported integrable real h has integrable complex exponential twist at every fixed z, with pointwise norm majorant exp(|Im z| A)*|h| on support |x|<=A. This pays the integrability inputs of NF579's twisted-convolution identity.

These scalar lemmas will feed NF579's direct sample route. Integration with the actual historical endpoint, the fixed contraction sequence, raw/window dictionary, full strip estimate and the source-binding obligation are still outstanding.

## Actual archive replay

The frozen NF494-native.zip was available locally. Direct Python Fraction replay in this pass read the raw 996666-byte member, verified SHA256 39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181 and both original source/seam hashes, all 400 ordered intervals, exact stored tail0, derivative-tail formula, M0<2e-7, M1<7e-4, U(B)<-1e-11. PASS. Numeric displays: M0=1.9659655557684862e-7, M1=0.0006957098822919963, endpoint upper=-1.16798644909683e-11, tail0=4.076412541946651e-121, tail1=8.153897824035919e-116. This is a replay under the inherited holomorphic majorant, not a Lean source identity.

## Standing

No local Lean executable. New proof candidates and focused CI committed; no main merge; no new axiom/sorry/admit intentionally introduced. Terminal unconditional Gram, full source-graph limit and original U binding still open in Lean. Full signed Weil coercivity, W_ODD_NEG and RH OPEN.
