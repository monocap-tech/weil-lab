# NF575 — physical L² convergence plus original strip bound suffices for full-source convergence

Stacked on NF574 PR #606. New proofs are committed Lean candidates; their compilation is pending.

## Verified compiler progress

- NF568 job 133784875295 successfully built ActualZetaOriginalJ242Generic67PlusPoleRootCount before failing at obsolete List.get_map in the original block coverage module (repair inherited from NF571).
- NF569 job 133788248951 successfully built ActualZetaOriginalJ242FrequencyNonzero, so the exact nonzero p_a ⇒ nonzero F_a implication is Lean accepted.
- NF570 job 133792336052 built ActualZetaOriginalJ242HermiteSignedOscillatorSum and ActualZetaOriginalJ242ActualOscillatorHermiteBridge successfully, then stopped at the old NF567 List.get_map failure. Thus the full literal 241-source oscillator-to-Hermite correspondence and full 242-column kernel root obligations including the sinh pole are now Lean accepted on that head. The complete 67-block and degree contradiction instantiation remain pending.
- NF569 independent job 133788248582 fails at (RingHom.id ℝ)c in square transport linearity; NF575 adds RingHom.id_apply. NF569 full job 133788248951 independently identifies two no-progress simp calls for smoothness of actual original generators as functions. NF575 uses the accepted NF562 exact function equality and smooth trig factor, plus the explicit last sinh generator function equality. Both repairs await Lean acceptance.
- NF568 immutable source audit 133784875215 passed again. Earlier NF550 physical weighted square and conditional separation remain accepted. NF570 physical/parity and NF571–NF574 jobs were queued at last inspection.

## Main analytical reduction

NF574 required log-Hilbert carrier convergence in addition to a common strip envelope. NF575 removes the need to prove a separate H^(1/4) approximation theorem to meet that gate.

Write E(t)=(1+log(2+|t|))/(1+|t|), r=1+|ξ|. In the true Mathlib Fourier coordinate t=-2πξ, log(e+|ξ|) <= L r^(1/4), E(-2πξ) <= D r^(-3/4), with L=4(e+1)^(1/4), D=1+4(2+2π)^(1/4). These follow from log x <=4x^(1/4), pi>3, and elementary inequalities. Hence log weight times the squared transform of any target with |F(z)|<=M E(Re z) is dominated by L(MD)^2 r^(-5/4), integrable on ℝ. This is the actual one-log form energy and not a quadratic Fourier moment (which would exclude the endpoint).

New ActualZetaOriginalStripLogCarrier.lean isolates the continuum argument from NF574's pending graph modules. It adapts the existing a.e. L¹/L² Fourier agreement and window evaluation dictionary to arbitrary supported physical L² vectors, builds their exact weighted log carrier, and retains physical realization.

New ActualZetaOriginalStripLogConvergence.lean uses fixed window sample continuity from its true L² exponential column. If g_n→f in ordinary physical L² with a common strip bound on all g_n and f, then weighted Fourier differences tend pointwise to zero and are bounded by the same integrable envelope with 2M. Lebesgue dominated convergence and the exact carrier norm identity give log-Hilbert convergence, not merely physical convergence.

New ActualZetaOriginalPhysicalStripFullGraph.lean composes this with NF574's actual multiplicity-preserving two-source convergence candidate. Given ordinary L² convergence, support and common strip envelope, it constructs full graph lifts of the same physical f and g_n and proves convergence in the genuine complete source graph. No Gram assumption.

## Original target and geometry

ActualZetaOriginalEndpointLogGeometry.lean defines the actual historical formula as h_U(x)-h_U(-x), where h_U(x)=1_{(B-δ,B)}(x)(U(x)/2)log(B/(B-x)), B=11/10, δ=1/500. It proves candidate real and odd symmetry, collar support, and membership in physical L² from a measurable U with bounded amplitude in the collar. The singularity is paid by d^(-1/2) on (0,δ): log(B/d)≤4(B/d)^(1/4), so squared integrability follows. The original compression margin (1-s)δ/4 is positive, and s E(st)≤E(t) for 0<s≤1. No actual affine convolution transform identity or approximation L² theorem is yet formalized here.

The integrated endpoint graph theorem uses the historical bound |U(x)|≤2·10^-7, and constructs the physical L² target from the literal endpoint formula. U remains a real function argument; identification with the frozen NF494 analytic U400 source SHA256 39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181 is an explicit remaining source-custody obligation. The historical coefficient interval archive has NOT been replayed or turned into an exact Lean function in NF575. Likewise its analytic derivative/strip estimates and actual smooth seed construction are not proved by the generic theorems. The current interface takes the uniform strip estimates and physical L² convergence as hypotheses. A source-independent formula is not a proof about a particular U400 merely by using its name.

## Next gates

Use genuine historical U source attachment and one-collar endpoint-log Fourier split/integration by parts; then formalize the same collar compression and mollification identity and ordinary L² convergence. With these inputs, NF575 and NF574 remove the independent fractional/logarithmic convergence hurdle, and NF573 transports exact moment correction. All new Lean code and inherited source graph dependency chain await acceptance. One focused verification workflow avoids duplicate broad audit; no new axiom/sorry/admit intentionally introduced. Physical/cofinite NF527 1/10 coercivity, NF539 full signed Weil bridge, W_ODD_NEG and RH remain open.
