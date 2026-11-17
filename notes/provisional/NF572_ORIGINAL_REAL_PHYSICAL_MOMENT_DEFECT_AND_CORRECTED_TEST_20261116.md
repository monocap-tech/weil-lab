# NF572 — original physical real moment defect and simultaneous real-odd corrected-test interface

Stacked on NF571 PR #603. All new theorem implementations pending pinned Lean acceptance.

## Compiler checkpoint

NF567 physical job 133780805041 completed FAILURE at the old pre-NF570 odd-parity finite-sum rewrite (line 132). This is the previously diagnosed obstruction; the repair already exists at NF570. NF567 source block and old missing iteratedDeriv failures are addressed at NF571/NF570 respectively. No newer diagnostics from NF568 run 44007069874, NF569 run 44008111871, NF570 run 44009355552 or NF571 run 44010225539: jobs remained queued at last check. No new theorem is promoted to LEAN PASS. NF550 and NF561–NF563 plus earlier polynomial/sinh/physical successes remain valid.

## Independent physical target moment identity and reality

New ActualZetaOriginalJ242RealPhysicalMoments.lean imports accepted NF549 physical moment machinery only (plus Mathlib). For arbitrary physical L² vector ell, the literal original moment is the continuum integral

    J_i(ell) = ∫ conj(J_i^window(x)) ell(x) dx.

The proof uses L² inner product and the a.e. source representative lemma. Reality is a.e., so there is no assumption that an L² class has a canonical pointwise real value. If conj(ell)=ell a.e., its original J242 moments are real. For a pointwise real Schwartz g, its physical L² representative is a.e. real, hence its moments are real as well. Therefore d=J(ell)-J(g) is real before any inversion or positivity.

## Actual corrected test

New ActualZetaOriginalJ242RealPhysicalCorrectedTest.lean consumes the independent real-moment result and NF571 canonical inverse conjugation, NF551 oddness and accepted NF543/NF548 geometry, moment recovery and log-carrier admission. With positivity explicitly assumed, for a.e.-real ell and a real odd Schwartz g vanishing off E, the literal NF543 correction f=g+R(J(ell)-J(g)) is pointwise real, odd, vanishes off E, exactly matches all 242 target moments, and is the physical L² realization of some actual original logarithmic Hilbert carrier element. The target ell need not already be a smooth test or an H¹ vector. This does not prove existence of a sequence g with any graph convergence.

The existing endpoint module ActualZetaOriginalJ242CanonicalGramPositivity.lean now instantiates the conditional statement with the NF569 strict Gram candidate. The integrated theorem has no explicit positivity premise, but depends on pending original source independence, NF551, NF571, and new NF572. NOT compiler certified.

## Boundary

We have not established that a particular historical target ell is a.e. real in this module, or that a particular seed g satisfies the real/odd/support hypotheses; these are explicit inputs. No topological support inclusion stronger than pointwise vanishing outside E is asserted. No coercivity, graph convergence, uniform bound on R, convergence of corrected sequences, signed Weil positivity or RH follows from this finite exact correction interface.

One new focused CI job checks independent real physical moments first, then conditional corrected test, then full endpoint even if an earlier independent step fails. Earlier CI queue remains the principal blocker. NF573 priority: consume actual source/physical diagnostics and certify; avoid extra multi-job workflows while queued. NF528 graph, NF527 full 1/10 coercivity, NF539 signed Weil identity, W_ODD_NEG and RH remain open.
