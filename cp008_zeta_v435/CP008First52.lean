module

public import Zeta.Zeros.BuildCerts

/-!
CP008 genuine upstream Euler–Maclaurin interval arithmetic kernel PROOF
CANDIDATE, with source data isolated from the original immutable Zeta release.

The upstream tactic reads THIS Lake project's
python/out/euler_maclaurin/zeros/zeros_00001.txt,
not the original widened store. Only if this specific module actually passes
Lean + its standard-axiom audit may the 52 narrow source intervals be counted
as formally certified. No all-zero count nor full Weil EF matrix is asserted.
-/

@[expose] public section

namespace CP008First52

open Zeta.Certificates

/-- All 52 proposed five-decimal subintervals, in the ORIGINAL order.
The underlying Zeta `build_batch` checks REAL Hardy-Z endpoint signs and
error bounds using its original `Enclosure` algorithm; it MUST NOT be replaced
by mpmath point samples. The proof remains a candidate until real CI passes. -/
theorem refinedCandidateBatch :
    BatchSpec 52 1413472 100000 14742277 100000 := by
  build_batch 0 52

end CP008First52

#print axioms CP008First52.refinedCandidateBatch
