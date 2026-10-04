import WeilDefect.Arithmetic.ActualZetaNativeSymbolSign
import WeilDefect.FiniteExponentialIndependence

namespace WeilDefect
noncomputable section
set_option maxHeartbeats 800000

/-- Complex Bombieri ordinates distinguish actual zero points. Their real
parts alone need not do so. -/
theorem neutralActualZetaOrdinate_injective :
    Function.Injective neutralActualZetaOrdinate := by
  intro ρ σ h
  apply Subtype.ext
  rw [← neutralActualZetaOrdinate_source ρ, ← neutralActualZetaOrdinate_source σ, h]

theorem neutralActualZetaSourceFrequency_injective :
    Function.Injective (fun ρ : NeutralActualZetaZeroPoint =>
      problemOneFreq (neutralActualZetaOrdinate ρ)) := by
  intro ρ σ h
  apply neutralActualZetaOrdinate_injective
  have hi := congrArg (fun z : ℂ => Complex.I * z) h
  simpa [problemOneFreq, mul_assoc, Complex.I_sq] using hi

/-- Exact parameter redundancy: identical complex ordinates are precisely
copies of the same actual zero point. No zero simplicity is used. -/
theorem neutralActualZetaDivisorOrdinate_eq_iff_point
    (q r : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaDivisorOrdinate q = neutralActualZetaDivisorOrdinate r ↔
      q.1 = r.1 := by
  exact neutralActualZetaOrdinate_injective.eq_iff

/-- Value observations at divisor copies carry precisely the same vanishing
information as one value at each actual point; no jet is manufactured. -/
theorem neutralActualZetaValueObservations_zero_iff_points (F : ℂ → ℂ) :
    (∀ q : NeutralActualZetaDivisorCoordinate,
      F (neutralActualZetaDivisorOrdinate q) = 0) ↔
    (∀ ρ : NeutralActualZetaZeroPoint, F (neutralActualZetaOrdinate ρ) = 0) := by
  constructor
  · intro h ρ
    exact h ⟨ρ, ⟨0, neutralActualZetaMultiplicity_pos ρ⟩⟩
  · intro h q
    exact h q.1

/-- Actual finite source modes at distinct points are independent on every
nonempty support interval. This is finite rigidity, not completeness. -/
theorem neutralActualZetaFiniteSourceModes_independent
    {n : ℕ} (ρ : Fin n → NeutralActualZetaZeroPoint)
    (hρ : Function.Injective ρ) (c : Fin n → ℂ)
    (a : ℝ) (ha : 0 < a)
    (hzero : Set.EqOn
      (fun x : ℝ => ∑ i : Fin n, c i *
        realExpMode (problemOneFreq (neutralActualZetaOrdinate (ρ i))) x)
      0 (Set.Ioo (-a) a)) :
    c = 0 := by
  apply wd_t24_finite_distinct_frequency_exponential_independence
    (fun i => problemOneFreq (neutralActualZetaOrdinate (ρ i))) c
    (neutralActualZetaSourceFrequency_injective.comp hρ) (-a) a
    (by linarith) hzero

end
end WeilDefect
