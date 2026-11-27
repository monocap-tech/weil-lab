import WeilDefect.MasterRecon.V10B7d
import WeilDefect.MasterRecon.V10B6i

/-! V10B7e: unconditional bounded arithmetic coefficient and signed
zero-sum receiver, with no external arithmetic inputs. This is not
the original explicit formula, coercivity or RH. -/
namespace WeilDefect.MasterRecon.V10B7e

open scoped InnerProduct
open V10A (Index normalizedPair)

theorem arithmetic_analysis (t : ℝ) (ht : 0 ≤ t) :
    ∃ T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index,
      V10B6d.LiteralCoordinates t T := by
  obtain ⟨A,hA,hcount⟩ := V10B7d.integer_local_count
  exact V10B6b.bounded_arithmetic_analysis t ht A hA hcount

theorem signed_receiver (t : ℝ) (ht : 0 ≤ t) :
    ∃ T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index,
      V10B6d.LiteralCoordinates t T ∧
      (V10B6c.signedGram T).adjoint = V10B6c.signedGram T ∧
      ∀ g : V08I.logCarrier t,
        Summable (fun z : V10B6f.StripIndex =>
          |V10B6f.zeroTerm (V08I.physicalInclusion t g : ℝ → ℂ) z.val|) ∧
        (inner ℂ (V10B6c.signedGram T g) g).re =
          ∑' z : V10B6f.StripIndex,
            V10B6f.zeroTerm (V08I.physicalInclusion t g : ℝ → ℂ) z.val := by
  obtain ⟨A,hA,hcount⟩ := V10B7d.integer_local_count
  exact V10B6i.full_strip_receiver t ht A hA hcount

theorem analysis_unique (t : ℝ) (T U : V08I.logCarrier t →L[ℂ] V07C.Coeff Index)
    (hT : V10B6d.LiteralCoordinates t T)
    (hU : V10B6d.LiteralCoordinates t U) : T = U := by
  ext g : 1
  apply lp.ext
  funext i
  exact (hT g i).trans (hU g i).symm

end WeilDefect.MasterRecon.V10B7e

#print axioms WeilDefect.MasterRecon.V10B7e.arithmetic_analysis
#print axioms WeilDefect.MasterRecon.V10B7e.signed_receiver
#print axioms WeilDefect.MasterRecon.V10B7e.analysis_unique
