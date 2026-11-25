import WeilDefect.Morphology.NeutralLogHilbertCarrier

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology

/-- A limit at the endpoint of the actual inward interval can always be
approached by strictly inward scales, without choosing the endpoint. -/
theorem f08_069_strictInward_exists_of_tendsto
    (F : Set.Icc (1 / 2 : ℝ) 1 → RealComplexL2) (k : RealComplexL2)
    (hF : Tendsto F
      (𝓝 (⟨1, by constructor <;> norm_num⟩ : Set.Icc (1 / 2 : ℝ) 1))
      (𝓝 k)) (ε : ℝ) (hε : 0 < ε) :
    ∃ lam : Set.Icc (1 / 2 : ℝ) 1, lam.1 < 1 ∧ ‖F lam - k‖ < ε := by
  obtain ⟨δ, hδ, h⟩ := (Metric.tendsto_nhds_nhds.mp hF) ε hε
  let t : ℝ := min (δ / 2) (1 / 4)
  have ht : 0 < t := lt_min (by linarith) (by norm_num)
  have htδ : t ≤ δ / 2 := min_le_left _ _
  have htq : t ≤ 1 / 4 := min_le_right _ _
  let lam : Set.Icc (1 / 2 : ℝ) 1 := ⟨1 - t, by
    constructor <;> linarith⟩
  refine ⟨lam, ?_, ?_⟩
  · change 1 - t < 1
    linarith
  · have hdist : dist lam
        (⟨1, by constructor <;> norm_num⟩ : Set.Icc (1 / 2 : ℝ) 1) < δ := by
      change dist (1 - t : ℝ) 1 < δ
      rw [Real.dist_eq]
      have he : 1 - t - 1 = -t := by ring
      rw [he, abs_neg, abs_of_pos ht]
      linarith
    simpa only [dist_eq_norm] using h hdist

/-- Simultaneously choose an approximation and a collar small enough to
fit a strictly positive physical support margin. -/
theorem f08_069_eventualCollar_choice
    (F : ℕ → RealComplexL2) (k : RealComplexL2)
    (r : ℕ → ℝ) (hF : Tendsto F atTop (𝓝 k))
    (hr : Tendsto r atTop (𝓝 (0 : ℝ)))
    (margin ε : ℝ) (hm : 0 < margin) (he : 0 < ε) :
    ∃ n : ℕ, r n < margin ∧ ‖F n - k‖ < ε := by
  have h1 := (Metric.tendsto_nhds.mp hr) margin hm
  have h2 := (Metric.tendsto_nhds.mp hF) ε he
  have hboth : ∀ᶠ n : ℕ in atTop, r n < margin ∧ ‖F n - k‖ < ε := by
    filter_upwards [h1, h2] with n hn hfn
    rw [Real.dist_eq, sub_zero] at hn
    rw [dist_eq_norm] at hfn
    exact ⟨lt_of_le_of_lt (le_abs_self _) hn, hfn⟩
  exact hboth.exists

/-- Widening the allowed support interval preserves the actual domain
and its existing finite logarithmic energy. -/
theorem f08_069_canonicalDomain_mono {b a : ℝ} (hba : b ≤ a) :
    neutralCanonicalLogFormDomain b ≤ neutralCanonicalLogFormDomain a := by
  intro f hf
  refine ⟨?_, hf.2⟩
  filter_upwards [hf.1] with x hx hout
  apply hx
  intro hin
  exact hout (Set.Icc_subset_Icc (neg_le_neg hba) hba hin)

def f08_069_canonicalWiden {b a : ℝ} (hba : b ≤ a)
    (f : neutralCanonicalLogFormDomain b) : neutralCanonicalLogFormDomain a :=
  ⟨f.val, f08_069_canonicalDomain_mono hba f.property⟩

/-- The same physical vector has exactly the same weighted coordinate
after changing its allowed support radius. -/
theorem f08_069_canonicalWiden_weighted_eq {b a : ℝ} (hba : b ≤ a)
    (f : neutralCanonicalLogFormDomain b) :
    neutralLogWeightedL2 (f08_069_canonicalWiden hba f) =
      neutralLogWeightedL2 f := by
  apply Lp.ext
  filter_upwards [neutralLogWeightedL2_coe (f08_069_canonicalWiden hba f),
    neutralLogWeightedL2_coe f] with xi h1 h2
  rw [h1, h2]
  rfl

/-- A collar strictly smaller than the original radius provides genuine
interior support, not just membership in the closed original window. -/
theorem f08_069_strictCollar_subset {b a : ℝ} (hba : b < a) :
    Set.Icc (-b) b ⊆ Set.Ioo (-a) a := by
  intro x hx
  exact ⟨lt_of_lt_of_le (neg_lt_neg hba) hx.1, lt_of_le_of_lt hx.2 hba⟩

#print axioms f08_069_strictInward_exists_of_tendsto
#print axioms f08_069_eventualCollar_choice
#print axioms f08_069_canonicalDomain_mono
#print axioms f08_069_canonicalWiden_weighted_eq
#print axioms f08_069_strictCollar_subset

end
end WeilDefect
