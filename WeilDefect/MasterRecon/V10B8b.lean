import WeilDefect.MasterRecon.V10B8a
import WeilDefect.MasterRecon.V10B7e
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma

/-! V10B8b: literal literature explicit formula interface, not an
assertion of its truth. Definitions follow Zeta23/ExplicitFormula.lean
at mirror revision 77f832c86fbb3e5336b949dae0fdcae26baea87c.
The exact diagonal attachment leaves EF_lit as a named hypothesis. -/
namespace WeilDefect.MasterRecon.V10B8b

open MeasureTheory Set Complex
open scoped ComplexConjugate InnerProduct BigOperators
open V10B8a (paperFT weilTest)

noncomputable def gammaOf (ρ : ℂ) : ℂ := (ρ-1/2)/I

theorem I_mul_gamma (ρ : ℂ) : I*gammaOf ρ = ρ-1/2 := by
  unfold gammaOf
  rw [mul_comm,div_mul_cancel₀ _ I_ne_zero]

theorem I_mul_conj_gamma (ρ : ℂ) :
    I*conj (gammaOf ρ) = V10A.reflect ρ-1/2 := by
  unfold gammaOf V10A.reflect
  rw [map_div₀,map_sub,Complex.conj_I]
  have hhalf : conj (1/2:ℂ) = (1/2:ℂ) := by simp
  rw [hhalf]
  field_simp [I_ne_zero]
  ring

theorem paperFT_at_zero (f : ℝ → ℂ) (ρ : ℂ) :
    paperFT f (gammaOf ρ) = V07A.mellin f (ρ-1/2) := by
  rw [V10B8a.paperFT_mellin,I_mul_gamma]

theorem paperFT_at_reflection (f : ℝ → ℂ) (ρ : ℂ) :
    paperFT f (conj (gammaOf ρ)) = V07A.mellin f (V10A.reflect ρ-1/2) := by
  rw [V10B8a.paperFT_mellin,I_mul_conj_gamma]

noncomputable def gammaBracket (r : ℝ) : ℝ :=
  (Complex.digamma (1/4+I*r/2)).re - Real.log Real.pi

noncomputable def primeTerm (k : ℝ → ℂ) (n : ℕ) : ℂ :=
  ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
    (k (Real.log n)+k (-Real.log n))

noncomputable def literatureRHS (k : ℝ → ℂ) : ℂ :=
  paperFT k (I/2)+paperFT k (-I/2) -
    (∑' n : ℕ, primeTerm k n) +
    (1/(2*Real.pi):ℂ) * ∫ r : ℝ, paperFT k r * (gammaBracket r:ℂ)

noncomputable def zeroSummand (k : ℝ → ℂ) (ρ : V10B6f.StripIndex) : ℂ :=
  (V09D.mult ρ.val:ℂ)*paperFT k (gammaOf ρ.val)

def LiteralEF : Prop :=
  ∀ k : ℝ → ℂ, ContDiff ℝ 2 k → HasCompactSupport k →
    Summable (zeroSummand k) ∧ (∑' ρ, zeroSummand k ρ) = literatureRHS k

theorem weighted_cross (f : ℝ → ℂ) (m : ℕ) (z w : ℂ) :
    V07A.weightedMellin f m z * conj (V07A.weightedMellin f m w) =
      (m:ℂ)*V07A.mellin f z*conj (V07A.mellin f w) := by
  unfold V07A.weightedMellin
  rw [map_mul,Complex.conj_ofReal]
  have h : (Real.sqrt (m:ℝ):ℂ)*(Real.sqrt (m:ℝ):ℂ) = (m:ℂ) := by
    exact_mod_cast (show Real.sqrt (m:ℝ)*Real.sqrt (m:ℝ) = (m:ℝ) by
      rw [← pow_two,Real.sq_sqrt (by positivity)])
  calc
    _ = ((Real.sqrt (m:ℝ):ℂ)*(Real.sqrt (m:ℝ):ℂ))*
      V07A.mellin f z*conj (V07A.mellin f w) := by ring
    _ = _ := by rw [h]

theorem autocorr_zero_real (f : ℝ → ℂ) (hf : Continuous f)
    (hfc : HasCompactSupport f) (ρ : V10B6f.StripIndex) :
    (zeroSummand (weilTest f f) ρ).re = V10B6f.zeroTerm f ρ.val := by
  unfold zeroSummand V10B6f.zeroTerm
  rw [V10B8a.paperFT_weilTest hf hf hfc hfc,paperFT_at_zero,paperFT_at_reflection,
    weighted_cross]
  congr 1
  ring

theorem zeroTerm_congr_ae (f g : ℝ → ℂ) (h : f =ᵐ[volume] g) (ρ : ℂ) :
    V10B6f.zeroTerm f ρ = V10B6f.zeroTerm g ρ := by
  unfold V10B6f.zeroTerm V07A.weightedMellin
  rw [V10B8a.mellin_congr_ae f g h (ρ-1/2),
    V10B8a.mellin_congr_ae f g h (V10A.reflect ρ-1/2)]

theorem diagonal_of_literalEF (hEF : LiteralEF) (t : ℝ)
    (T : V08I.logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (hT : V10B6d.LiteralCoordinates t T)
    (g : V08I.logCarrier t) (f : ℝ → ℂ)
    (hf : ContDiff ℝ 2 f) (hfc : HasCompactSupport f)
    (hae : (V08I.physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f) :
    (inner ℂ (V10B6c.signedGram T g) g).re = (literatureRHS (weilTest f f)).re := by
  obtain ⟨_,hdiag⟩ := V10B6f.full_strip_diagonal t T hT
    V10B6h.strip_reflection_closed V10B6h.strip_reflection_mult g
  obtain ⟨hs,he⟩ := hEF (weilTest f f)
    (V10B8a.weilTest_contDiff hf hf.continuous hfc)
    (V10B8a.weilTest_hasCompactSupport hfc hfc)
  rw [hdiag,← he]
  have hr := (Complex.reCLM.hasSum hs.hasSum).tsum_eq
  change (∑' ρ, (zeroSummand (weilTest f f) ρ).re) =
    (∑' ρ, zeroSummand (weilTest f f) ρ).re at hr
  rw [← hr]
  apply tsum_congr
  intro ρ
  rw [zeroTerm_congr_ae _ f hae,autocorr_zero_real f hf.continuous hfc]

end WeilDefect.MasterRecon.V10B8b

#print axioms WeilDefect.MasterRecon.V10B8b.I_mul_gamma
#print axioms WeilDefect.MasterRecon.V10B8b.I_mul_conj_gamma
#print axioms WeilDefect.MasterRecon.V10B8b.paperFT_at_zero
#print axioms WeilDefect.MasterRecon.V10B8b.paperFT_at_reflection
#print axioms WeilDefect.MasterRecon.V10B8b.weighted_cross
#print axioms WeilDefect.MasterRecon.V10B8b.autocorr_zero_real
#print axioms WeilDefect.MasterRecon.V10B8b.zeroTerm_congr_ae
#print axioms WeilDefect.MasterRecon.V10B8b.diagonal_of_literalEF
