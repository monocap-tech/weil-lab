import WeilDefect.MasterRecon.V10B11b
import WeilDefect.MasterRecon.V10B10c

/-! The exceptional sector of the literal arithmetic receiver.
Finite-dimensional existence is not an effective dimension bound;
the finite Schur form remains the unresolved positivity obligation. -/
namespace WeilDefect.MasterRecon.V10B11c

open scoped InnerProduct NNReal
open V08I (logCarrier)
open V10B6c (signedGram analysisChannel)
open V10B11b (energy response)

theorem signed_symmetric (t : ℝ)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index) :
    ∀ x y : logCarrier t, inner ℂ (signedGram T x) y =
      inner ℂ x (signedGram T y) := by
  intro x y
  calc
    _ = inner ℂ ((signedGram T).adjoint x) y := by rw [V10B6c.signedGram_symmetric]
    _ = _ := ContinuousLinearMap.adjoint_inner_left _ y x

theorem finite_schur_receiver (t : ℝ)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (K : logCarrier t →L[ℂ] logCarrier t) (hK : IsCompactOperator K)
    (hG : signedGram T = 1+K) :
    ∃ S : Submodule ℂ (logCarrier t), ∃ hS : FiniteDimensional ℂ S,
      ∃ htail : ∀ x ∈ Sᗮ, (1/2:ℝ)*‖x‖^2 ≤ energy (signedGram T) x,
        ∃ R : S →L[ℂ] Sᗮ,
          (∀ x, V10B11b.tailBlock S (signedGram T) (R x) =
            V10B11b.crossBlock S (signedGram T) x) ∧
          ((∀ g : logCarrier t, 0 ≤ energy (signedGram T) g) ↔
            ∀ x : S, 0 ≤ energy (signedGram T) (x:logCarrier t) -
              energy (signedGram T) (R x:logCarrier t)) := by
  obtain ⟨S,hS,htail⟩ := V10B11a.finite_exceptional_sector (signedGram T) K hK hG
  letI : FiniteDimensional ℂ S := hS
  letI : CompleteSpace S := FiniteDimensional.completeSpace ℂ S
  let R := ((V10B11b.tailInverse S (signedGram T) (1/2) (by norm_num) htail).symm
    .toContinuousLinearMap).comp (V10B11b.crossBlock S (signedGram T))
  refine ⟨S,hS,htail,R,?_ ,?_⟩
  · intro x
    exact V10B11b.response_eq S (signedGram T) (1/2) (by norm_num) htail x
  · exact V10B11b.positivity_iff_schur S (signedGram T) (signed_symmetric t T)
      (1/2) (by norm_num) htail

theorem arithmetic_finite_schur (t : ℝ) (ht : 0 < t)
    (hOld : V10B9b.OldApproximation)
    (hStirling : V10B8f.VerticalStirling)
    (hEF : V10B8b.LiteralEF)
    (hSupply : V09C.SuperlinearSupply V09C.CriticalSample) :
    ∃ T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index,
      V10B6d.LiteralCoordinates t T ∧
      ∃ S : Submodule ℂ (logCarrier t), FiniteDimensional ℂ S ∧
        (∀ x ∈ Sᗮ, (1/2:ℝ)*‖x‖^2 ≤ energy (signedGram T) x) ∧
        ∃ R : S →L[ℂ] Sᗮ,
          (∀ g : logCarrier t, 0 ≤ energy (signedGram T) g) ↔
          ∀ x : S, 0 ≤ energy (signedGram T) (x:logCarrier t) -
            energy (signedGram T) (R x:logCarrier t) := by
  obtain ⟨T,hT,⟨K,hK,hG⟩,_⟩ :=
    V10B9c.arithmetic_coercivity t ht hOld hStirling hEF hSupply
  obtain ⟨S,hS,htail,R,_,he⟩ := finite_schur_receiver t T K hK hG
  exact ⟨T,hT,S,hS,htail,R,he⟩

end WeilDefect.MasterRecon.V10B11c

#print axioms WeilDefect.MasterRecon.V10B11c.signed_symmetric
#print axioms WeilDefect.MasterRecon.V10B11c.finite_schur_receiver
#print axioms WeilDefect.MasterRecon.V10B11c.arithmetic_finite_schur
