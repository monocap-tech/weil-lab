import WeilDefect.MasterRecon.V07F

/-! V08A: composite conditional rigidity in the ordinary selected raw
coefficient model. The original translated-test neutral pairing is the
input, not the analytic equation. Arithmetic sample boundedness,
coercivity, carrier membership and the physical translation orbit
remain explicit hypotheses. -/
namespace WeilDefect.MasterRecon.V08A

open MeasureTheory Set
open scoped ENNReal NNReal InnerProduct Topology
open V07C

theorem mellin_congr_ae {f h : ℝ → ℂ}
    (he : f =ᵐ[volume] h) (w : ℂ) :
    V07A.mellin f w = V07A.mellin h w := by
  unfold V07A.mellin
  apply integral_congr_ae
  filter_upwards [he] with x hx
  rw [hx]

theorem samplePair_congr_ae {f h : ℝ → ℂ}
    (he : f =ᵐ[volume] h) (m : ℕ) (d g : ℝ) :
    V07E.samplePair f m d g = V07E.samplePair h m d g := by
  unfold V07E.samplePair V07A.weightedMellin
  simp only [mellin_congr_ae he]

variable {ι H : Type*} [DecidableEq ι]
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- A raw neutral mode that persists against all small translated tests
has zero physical L² representative. The finite load v and positive
coercivity are inputs; the analytic translation equation is a conclusion
of the exact sampling and pairing identities. -/
theorem conditional_neutral_rigidity
    (C : H →L[ℂ] V06D.PhysicalL2) (A : H →L[ℂ] Coeff ι)
    (m : ι → ℕ) (d g : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2)
    (E : ι → Pair →L[ℂ] Pair) (c : ℝ) (hc : 0 ≤ c)
    (hE : ∀ i, ‖E i‖ ≤ c)
    (s : Finset ι) (v : Coeff ι) (hv : ∀ i, i ∉ s → v i = 0)
    (b : ℝ≥0) (hb : 0 < b)
    (hco : ∀ x : H, ‖x‖ ^ 2 * (b : ℝ) ≤
      (inner ℂ ((A.adjoint ∘L V07B.blockLift E c hc hE ∘L A) x) x).re)
    (k : H) (tail : ℝ) (htail : V06D.TailZero (C k) tail)
    (eps : ℝ) (heps : 0 < eps) (T : ℝ → H)
    (Y : ℝ → H → Coeff ι)
    (hA : ∀ x i, A x i = V07E.samplePair (C x) (m i) (d i) (g i))
    (hY : ∀ a : ℝ, |a| < eps → ∀ x i,
      Y a x i = V07E.samplePair (V07A.translate (-a) (C x)) (m i) (d i) (g i))
    (hphys : ∀ a : ℝ, |a| < eps →
      (C (T a) : V06D.PhysicalL2) =ᵐ[volume] fun x => C k (x - a))
    (hneutral : ∀ a : ℝ, |a| < eps → ∀ x : H,
      inner ℂ (V07B.blockLift E c hc hE (A k)) (Y a x) =
        inner ℂ v (Y a x)) :
    C k = 0 := by
  let D := displacement d hd
  let Q := V07B.blockLift E c hc hE
  let G := V07F.selectedGenerator s g
  have hcov : ∀ a : ℝ, |a| < eps → ∀ x : H,
      Y a x = phase g (-a) (NormedSpace.exp ((-(a : ℂ)) • D) (A x)) := by
    intro a ha x
    have h := V07E.sampled_translation (C x) m d g hd (-a) (A x) (Y a x)
      (hA x) (hY a ha x)
    simpa only [Complex.ofReal_neg] using h
  have hback : ∀ a : ℝ, |a| < eps → Y a (T a) = A k := by
    intro a ha
    have he : V07A.translate (-a) (C (T a)) =ᵐ[volume] (C k : V06D.PhysicalL2) := by
      have hh := V06D.ae_translate (hphys a ha) a
      filter_upwards [hh] with x hx
      change C (T a) (x - (-a)) = C k x
      simpa only [sub_neg_eq_add, add_sub_cancel_right] using hx
    apply lp.ext
    funext i
    change Y a (T a) i = A k i
    rw [hY a ha, hA]
    exact samplePair_congr_ae he _ _ _
  have heq : ∀ a : ℝ, |a| < eps →
      V06A.translatedForm A D Q (a : ℂ) (T a) =
        V06B.selectedForcing A D G v (a : ℂ) := by
    intro a ha
    apply ext_inner_right ℂ
    intro x
    calc
      inner ℂ (V06A.translatedForm A D Q (a : ℂ) (T a)) x =
          inner ℂ (Q (phase g (-a)
            (NormedSpace.exp ((-(a : ℂ)) • D) (A (T a)))))
            (phase g (-a) (NormedSpace.exp ((-(a : ℂ)) • D) (A x))) :=
        (V07E.translated_form_pairing A d g hd E c hc hE a (T a) x).symm
      _ = inner ℂ (Q (Y a (T a))) (Y a x) := by
        rw [← hcov a ha (T a), ← hcov a ha x]
      _ = inner ℂ v (Y a x) := by
        rw [hback a ha]
        exact hneutral a ha x
      _ = inner ℂ (V06B.selectedForcing A D G v (a : ℂ)) x := by
        rw [hcov a ha x]
        exact (V07F.selected_forcing_pairing A s d g hd v hv a x).symm
  obtain ⟨r, hr, U, hU, _, huniq⟩ :=
    V06B.coercive_selected_orbit A D Q G v b hb hco
  let R := min r eps
  have hR : 0 < R := lt_min hr heps
  have hUR : AnalyticOnNhd ℂ U (Metric.ball 0 R) := by
    intro z hz
    apply hU z
    rw [Metric.mem_ball] at hz ⊢
    exact hz.trans_le (min_le_left r eps)
  apply V06D.analytic_translation_right_tail_rigidity C U (C k) R hR hUR _ tail htail
  intro a ha
  have hae : |a| < eps := ha.trans_le (min_le_right r eps)
  have har : (a : ℂ) ∈ Metric.ball (0 : ℂ) r := by
    rw [Metric.mem_ball, dist_zero_right, Complex.norm_real, Real.norm_eq_abs]
    exact ha.trans_le (min_le_left r eps)
  have h := huniq (a : ℂ) har (T a) (heq a hae)
  rw [h]
  exact hphys a hae

end WeilDefect.MasterRecon.V08A

#print axioms WeilDefect.MasterRecon.V08A.mellin_congr_ae
#print axioms WeilDefect.MasterRecon.V08A.samplePair_congr_ae
#print axioms WeilDefect.MasterRecon.V08A.conditional_neutral_rigidity
