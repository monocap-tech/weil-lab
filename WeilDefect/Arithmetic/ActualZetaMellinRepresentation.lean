import WeilDefect.Arithmetic.ActualZetaMellinGrowth
import Mathlib.Analysis.MellinTransform

namespace WeilDefect
noncomputable section
open Set MeasureTheory
open scoped Topology

/-- The actual large-t theta remainder, extended by zero below one. -/
def neutralActualZetaThetaTailKernel : ℝ → ℂ :=
  (Ioi 1).indicator (fun t => (neutralActualZetaThetaRemainder t : ℂ))

theorem neutralActualZetaThetaTailKernel_mellin (s : ℂ) :
    mellin neutralActualZetaThetaTailKernel s =
      ∫ t : ℝ in Ioi 1, neutralActualZetaThetaMellinTailIntegrand s t := by
  simp only [mellin, neutralActualZetaThetaTailKernel, ← indicator_smul,
    setIntegral_indicator measurableSet_Ioi,
    inter_eq_right.mpr (Ioi_subset_Ioi (show (0 : ℝ) ≤ 1 by norm_num)),
    smul_eq_mul, neutralActualZetaThetaMellinTailIntegrand]

theorem neutralActualZetaThetaTailKernel_convergent (s : ℂ) :
    MellinConvergent neutralActualZetaThetaTailKernel s := by
  obtain ⟨p, C, hp, hC, hb⟩ := neutralActualZetaThetaMellinTail_bound
  obtain ⟨n, hn⟩ := exists_nat_gt (s.re - 1)
  have hi := (hb n s hn.le).1
  change IntegrableOn (fun t : ℝ =>
    (t : ℂ) ^ (s - 1) • neutralActualZetaThetaTailKernel t) (Ioi 0)
  simpa only [neutralActualZetaThetaTailKernel, ← indicator_smul,
    smul_eq_mul, neutralActualZetaThetaMellinTailIntegrand] using
    (hi.integrable_indicator measurableSet_Ioi).integrableOn (s := Ioi 0)

/-- Identify the actual modified FE-pair kernel with its two tail pieces.
The equality includes t=1, where all pieces are zero. -/
theorem neutralActualZetaModifiedKernel_eq {t : ℝ} (ht0 : 0 < t) :
    (HurwitzZeta.hurwitzEvenFEPair 0).f_modif t =
      neutralActualZetaThetaTailKernel t +
        (t : ℂ) ^ (-(1 / 2 : ℂ)) * neutralActualZetaThetaTailKernel t⁻¹ := by
  have hpow : (t : ℂ) ^ (-(1 / 2 : ℂ)) =
      ((t ^ (-(1 / 2 : ℝ)) : ℝ) : ℂ) := by
    simpa only [Complex.ofReal_neg, Complex.ofReal_div, Complex.ofReal_one,
      Complex.ofReal_ofNat] using
      (Complex.ofReal_cpow ht0.le (-(1 / 2 : ℝ))).symm
  rcases lt_trichotomy t 1 with ht | rfl | ht
  · have hit : 1 < t⁻¹ := (one_lt_inv₀ ht0).2 ht
    have hf := HurwitzZeta.evenKernel_functional_equation (0 : UnitAddCircle) t
    rw [← HurwitzZeta.evenKernel_eq_cosKernel_of_zero] at hf
    have he : HurwitzZeta.evenKernel 0 t - t ^ (-(1 / 2 : ℝ)) =
        t ^ (-(1 / 2 : ℝ)) * neutralActualZetaThetaRemainder t⁻¹ := by
      rw [neutralActualZetaThetaRemainder, hf, Real.rpow_neg ht0.le, one_div]
      ring
    simp only [WeakFEPair.f_modif, HurwitzZeta.hurwitzEvenFEPair,
      Function.comp_apply, if_pos rfl, one_mul, smul_eq_mul, mul_one,
      Pi.add_apply, indicator_of_notMem (show t ∉ Ioi 1 by exact not_lt.mpr ht.le),
      indicator_of_mem (show t ∈ Ioo 0 1 from ⟨ht0, ht⟩), zero_add,
      neutralActualZetaThetaTailKernel,
      indicator_of_notMem (show t ∉ Ioi 1 by exact not_lt.mpr ht.le),
      indicator_of_mem (show t⁻¹ ∈ Ioi 1 from hit), zero_add, hpow]
    exact_mod_cast he
  · simp [WeakFEPair.f_modif, HurwitzZeta.hurwitzEvenFEPair,
      neutralActualZetaThetaTailKernel]
  · have hit : t⁻¹ < 1 := (inv_lt_one₀ ht0).2 ht
    simp [WeakFEPair.f_modif, HurwitzZeta.hurwitzEvenFEPair,
      neutralActualZetaThetaTailKernel, neutralActualZetaThetaRemainder,
      ht, not_lt.mpr ht.le, not_lt.mpr hit.le]

/-- The reflected small-t Mellin term is convergent without an
operator-domain or divisor-growth premise. -/
theorem neutralActualZetaThetaReflected_convergent (s : ℂ) :
    MellinConvergent (fun t : ℝ =>
      (t : ℂ) ^ (-(1 / 2 : ℂ)) • neutralActualZetaThetaTailKernel t⁻¹) s := by
  apply MellinConvergent.cpow_smul.mpr
  have h := (MellinConvergent.comp_rpow
    (f := neutralActualZetaThetaTailKernel)
    (s := s + -(1 / 2 : ℂ)) (a := -1) (by norm_num)).mpr
      (neutralActualZetaThetaTailKernel_convergent
        ((s + -(1 / 2 : ℂ)) / (-1 : ℝ)))
  simpa only [Real.rpow_neg_one] using h

/-- Actual completed zeta with its poles removed is the half-sum of
the two convergent theta tail integrals. Mellin inversion retains the
change-of-variables Jacobian. -/
theorem neutralActualZetaCompleted_mellin_tails (z : ℂ) :
    completedRiemannZeta₀ z =
      ((∫ t : ℝ in Ioi 1, neutralActualZetaThetaMellinTailIntegrand (z / 2) t) +
       (∫ t : ℝ in Ioi 1,
         neutralActualZetaThetaMellinTailIntegrand ((1 - z) / 2) t)) / 2 := by
  have he : mellin (HurwitzZeta.hurwitzEvenFEPair 0).f_modif (z / 2) =
      mellin (fun t : ℝ => neutralActualZetaThetaTailKernel t +
        (t : ℂ) ^ (-(1 / 2 : ℂ)) •
          neutralActualZetaThetaTailKernel t⁻¹) (z / 2) := by
    apply setIntegral_congr_fun measurableSet_Ioi
    intro t ht
    rw [neutralActualZetaModifiedKernel_eq ht]
    rfl
  have hs := (hasMellin_add
    (neutralActualZetaThetaTailKernel_convergent (z / 2))
    (neutralActualZetaThetaReflected_convergent (z / 2))).2
  change mellin (HurwitzZeta.hurwitzEvenFEPair 0).f_modif (z / 2) / 2 = _
  rw [he, hs, mellin_cpow_smul, mellin_comp_inv]
  have ha : -(z / 2 + -(1 / 2 : ℂ)) = (1 - z) / 2 := by ring
  rw [ha, neutralActualZetaThetaTailKernel_mellin,
    neutralActualZetaThetaTailKernel_mellin]

end
end WeilDefect
