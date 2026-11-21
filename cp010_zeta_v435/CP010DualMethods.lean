module

public import Zeta.Zeros.BuildCerts
public import Zeta.Zeros.BuildCertsRS

/-!
CP010 dual source-verified sign-change PROOF CANDIDATES at actual global
zeta positive-zero index 53 (RS store local row index 1).
Both import the original unchanged external Zeta v4.35 analytic infrastructure.
The original IV### Lean v4.34 and independent full Turing count are untouched.

Acceptance requires a real Lean kernel build + actual .olean/axiom audit, and
external source-row containment checks. Neither theorem claims they certify
the same root without the still-missing complete-count/bijection argument.
-/

@[expose] public section

namespace CP010DualMethods
open Zeta.Certificates

/-- Original Riemann-Siegel full/linear-free named-error kernel tactic,
a COARSE candidate around global zero #53. -/
theorem coarseRiemannSiegelCandidate :
    BatchSpec 1 15000 100 15010 100 := by
  build_batch_rs 0 1

/-- Independently original Euler-Maclaurin named-error kernel tactic,
a NARROW candidate around global zero #53. The selected cutoff parameters
were copied from the real upstream final (#52) Euler source row; their
continued applicability at t=150 requires THIS theorem to compile. -/
theorem narrowEulerMaclaurinCandidate :
    BatchSpec 1 15005352 100000 15005353 100000 := by
  build_batch 0 1

end CP010DualMethods

#print axioms CP010DualMethods.coarseRiemannSiegelCandidate
#print axioms CP010DualMethods.narrowEulerMaclaurinCandidate
