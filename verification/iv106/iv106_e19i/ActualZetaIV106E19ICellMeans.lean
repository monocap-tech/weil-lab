import WeilDefect.Arithmetic.ActualZetaIV106C3ActualConstraints
import WeilDefect.Arithmetic.ActualZetaIV106E18VLiteralMatch
import WeilDefect.Arithmetic.ActualZetaIV106E18OLiteralMatrix

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap

theorem neutralIV106E19IWidth_pos : 0 < neutralIV106E18LWidth := by
  norm_num [neutralIV106E18LWidth]

/-- The literal C3 cells coincide with the E18 trial cells. -/
theorem neutralIV106E19ICell_eq (i : Fin 665) :
    neutralIV106C3Cell (11/10:ℝ) 665 i =
      Icc (neutralIV106E18LLeft i.val)
        (neutralIV106E18LLeft i.val+neutralIV106E18LWidth) := by
  unfold neutralIV106C3Cell neutralIV106E18LLeft neutralIV106E18LWidth
  congr 1 <;> ring

/-- The clipped polynomial vanishes also at both cell endpoints. -/
theorem neutralIV106E19IOutside_open (l h : ℝ) (hh : 0 < h)
    (x : ℝ) (hx : x ∉ Ioo l (l+h)) :
    neutralIV106E18ITrial l h x = 0 := by
  by_cases hm : x ∈ Icc l (l+h)
  · rw [neutralIV106E18ITrial_inside l h hh x hm]
    have he : x = l ∨ x = l+h := by
      by_contra hn
      push_neg at hn
      exact hx ⟨lt_of_le_of_ne hm.1 (Ne.symm hn.1),lt_of_le_of_ne hm.2 hn.2⟩
    rcases he with rfl | he
    · simp [(neutralIV106E18IPoly_endpoints h).1]
    · rw [he,show (l+h-l)/h=1 by field_simp [hh.ne'] <;> ring]
      simp [(neutralIV106E18IPoly_endpoints h).2]
  · exact neutralIV106E18ITrial_outside l h hh x hm

theorem neutralIV106E19IDisjoint (i j : ℕ) (hij : i ≠ j)
    (x : ℝ) (hx : x ∈ Icc (neutralIV106E18LLeft i)
      (neutralIV106E18LLeft i+neutralIV106E18LWidth)) :
    neutralIV106E18ITrial (neutralIV106E18LLeft j) neutralIV106E18LWidth x = 0 := by
  apply neutralIV106E19IOutside_open _ _ neutralIV106E19IWidth_pos
  intro hj
  unfold neutralIV106E18LLeft neutralIV106E18LWidth at hx hj
  rcases lt_or_gt_of_ne hij with h | h
  · have hh : (i:ℝ)+1 ≤ (j:ℝ) := by exact_mod_cast (show i+1 ≤ j by omega)
    linarith [hx.2,hj.1]
  · have hh : (j:ℝ)+1 ≤ (i:ℝ) := by exact_mod_cast (show j+1 ≤ i by omega)
    linarith [hx.1,hj.2]

/-- All 665 individual means vanish, not only the global mean. Adjacent
closed cells cause no issue because the endpoint values are zero. -/
theorem neutralIV106E19IMean (i : Fin 665) (j : ℕ) :
    (∫ x in neutralIV106C3Cell (11/10:ℝ) 665 i,
      neutralIV106E18OTrial j x) = 0 := by
  rw [neutralIV106E19ICell_eq]
  let l := neutralIV106E18LLeft j
  let h := neutralIV106E18LWidth
  have hh : 0 < h := neutralIV106E19IWidth_pos
  have he : (∫ x in Icc (neutralIV106E18LLeft i.val)
      (neutralIV106E18LLeft i.val+h), neutralIV106E18OTrial j x) =
      ∫ x in Icc (neutralIV106E18LLeft i.val)
        (neutralIV106E18LLeft i.val+h), neutralIV106E18ITrial l h x := by
    apply integral_congr_ae
    filter_upwards [ae_restrict_of_ae
      (neutralIV106E18JTrial_memLp l h hh).coeFn_toLp] with x hx
    exact hx
  rw [he]
  by_cases hij : i.val=j
  · rw [hij,integral_Icc_eq_integral_Ioc,← intervalIntegral.integral_of_le
      (by change l ≤ l+h; linarith)]
    have hz := neutralIV106E18K2Affine l h 0 hh
    have hzero := neutralIV106E18K1Zero h 0 (Or.inl rfl)
    simpa [hzero] using hz
  · apply integral_eq_zero_of_ae
    filter_upwards [ae_restrict_mem (measurableSet_Icc :
      MeasurableSet (Icc (neutralIV106E18LLeft i.val) (neutralIV106E18LLeft i.val+h)))] with x hx
    exact neutralIV106E19IDisjoint i.val j hij x hx

theorem neutralIV106E19IWindow (j : ℕ) (hj : neutralIV106E18LEligible j) :
    Icc (neutralIV106E18LLeft j) (neutralIV106E18LLeft j+neutralIV106E18LWidth) ⊆
      Icc (-(11/10:ℝ)) (11/10) := by
  intro x hx
  apply neutralIV106E18LWindow j hj
  rw [mem_closedBall,Real.dist_eq,abs_le]
  have hb : 0 < neutralIV106E18LBuffer := by norm_num [neutralIV106E18LBuffer]
  constructor <;> linarith [hx.1,hx.2]

theorem neutralIV106E19IAdmission (j : ℕ) (hj : neutralIV106E18LEligible j) :
    ∃ p : NeutralLogHilbertCarrier (11/10:ℝ),
      neutralLogPhysical p.val = neutralIV106E18OTrial j :=
  neutralIV106E18VLiteral_admission _ _ _ neutralIV106E18LBuffer
    neutralIV106E19IWidth_pos (by norm_num [neutralIV106E18LBuffer])
    (neutralIV106E19IWindow j hj)

#print axioms neutralIV106E19IWidth_pos
#print axioms neutralIV106E19ICell_eq
#print axioms neutralIV106E19IOutside_open
#print axioms neutralIV106E19IDisjoint
#print axioms neutralIV106E19IMean
#print axioms neutralIV106E19IWindow
#print axioms neutralIV106E19IAdmission
end
end WeilDefect
