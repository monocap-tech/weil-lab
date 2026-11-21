module

public import Zeta.Main

/-!
CP006 isolated upstream Zeta v4.35 proof attachment, NOT a Weil-Lab v4.34 import.
The canonical original IV### build is not modified or upgraded.

All statements below derive from the actual Zeta generated Turing+interval
certificate; none exports rational ordinates or proves Weil EF normalization.
-/

@[expose] public section

namespace CP006ZeroBridge

open Zeta.Certificates

/-- Original kernel theorem for the certified *complete multiplicity count*
through its certified Gram point, not a guessed zero roster. -/
theorem certified_count_at_gram :
    riemannZeta.N (gramPoint certifiedZeroCount.minIdx) =
      certifiedZeroCount.intervals.length :=
  riemannZeta.N_gramPoint_eq certifiedZeroCount

/-- Source-locked enumeration length; proofs are the actual source batch length
and Turing-completeness combination, not a new numerical witness. -/
theorem certified_total_zero_count_at_gram :
    riemannZeta.N (gramPoint certifiedZeroCount.minIdx) = 1748002 := by
  calc
    _ = certifiedZeroCount.intervals.length :=
      certified_count_at_gram
    _ = certifiedZeroIntervals.intervals.length := rfl
    _ = 1748002 := certifiedZeroIntervals_length

/-- Genuine external finite-height RH statement, only below 1000449. -/
theorem certified_finite_height_line :
    RiemannHypothesisUpTo 1000449 :=
  Zeta.riemannHypothesisUpTo_1000449

/-- Genuine external certified simple zeros, only below 1000449. -/
theorem certified_finite_height_simple :
    SimpleZerosUpTo 1000449 :=
  Zeta.simpleZerosUpTo_1000449

end CP006ZeroBridge

#print axioms CP006ZeroBridge.certified_count_at_gram
#print axioms CP006ZeroBridge.certified_total_zero_count_at_gram
#print axioms CP006ZeroBridge.certified_finite_height_line
#print axioms CP006ZeroBridge.certified_finite_height_simple
