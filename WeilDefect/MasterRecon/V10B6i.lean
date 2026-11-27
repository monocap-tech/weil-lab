import WeilDefect.MasterRecon.V10B6f
import WeilDefect.MasterRecon.V10B6h

/-! V10B6i: arithmetic signed receiver without reflection or positive
multiplicity hypotheses. Local counting and critical-line supply remain
separate inputs. No explicit-formula or positivity claim is made. -/
namespace WeilDefect.MasterRecon.V10B6i

open scoped ENNReal NNReal InnerProduct
open V10A (Index)
open V10B6c (signedGram analysisChannel)

theorem full_strip_receiver (t : ℝ) (ht : 0 ≤ t) (A : ℝ) (hA : 0 ≤ A)
    (hcount : ∀ n : ℤ, (V09D.count (n : ℝ) ((n : ℝ)+1) : ℝ) ≤
      A * Real.log (|(n : ℝ)|+3)) :
    ∃ T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index,
      V10B6d.LiteralCoordinates t T ∧
      (signedGram T).adjoint = signedGram T ∧
      ∀ g : V08I.logCarrier t,
        Summable (fun z : V10B6f.StripIndex =>
          |V10B6f.zeroTerm (V08I.physicalInclusion t g : ℝ → ℂ) z.val|) ∧
        (inner ℂ (signedGram T g) g).re =
          ∑' z : V10B6f.StripIndex,
            V10B6f.zeroTerm (V08I.physicalInclusion t g : ℝ → ℂ) z.val := by
  obtain ⟨T,hT⟩ := V10B6b.bounded_arithmetic_analysis t ht A hA hcount
  exact ⟨T,hT,V10B6c.signedGram_symmetric T,fun g =>
    V10B6f.full_strip_diagonal t T hT V10B6h.strip_reflection_closed
      V10B6h.strip_reflection_mult g⟩

theorem positive_kernel (t : ℝ) (ht : 0 ≤ t)
    (T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index)
    (hT : V10B6d.LiteralCoordinates t T)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (g : V08I.logCarrier t) (hg : analysisChannel true T g = 0) : g = 0 :=
  V10B6d.arithmetic_positive_kernel t T ht hT
    V10B6g.strip_mult_positive hdens g hg

theorem positive_coercivity (t : ℝ) (ht : 0 ≤ t)
    (T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index)
    (hT : V10B6d.LiteralCoordinates t T)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ g : V08I.logCarrier t,
      ‖g‖^2 ≤ ‖analysisChannel true T g‖^2 +
        M * ‖V08I.physicalInclusion t g‖^2) :
    ∃ b : ℝ≥0, 0 < b ∧ ∀ g : V08I.logCarrier t,
      ‖g‖^2 * (b : ℝ) ≤ ‖analysisChannel true T g‖^2 :=
  V10B6d.arithmetic_positive_coercivity t T ht hT
    V10B6g.strip_mult_positive hdens M hM hdef

end WeilDefect.MasterRecon.V10B6i

#print axioms WeilDefect.MasterRecon.V10B6i.full_strip_receiver
#print axioms WeilDefect.MasterRecon.V10B6i.positive_kernel
#print axioms WeilDefect.MasterRecon.V10B6i.positive_coercivity
