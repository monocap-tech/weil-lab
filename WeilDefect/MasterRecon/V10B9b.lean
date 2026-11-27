import WeilDefect.MasterRecon.V10B9a

/-! Exact physical-domain interface to the F08-075 density theorem.
The old approximation theorem is deliberately an explicit premise
until its generated-source custody closure is available on this branch. -/
namespace WeilDefect.MasterRecon.V10B9b

open MeasureTheory Set
open scoped FourierTransform
open V08I (FullL2 logCarrier physicalInclusion)
open V10B9a (oldDensity newDensity forwardConstant)

def OldApproximation : Prop :=
  ∀ (t : ℝ), 0 < t → ∀ f : FullL2,
    (∀ᵐ x ∂volume, x ∉ Icc (-t) t → f x = 0) →
    Integrable (oldDensity f) →
    ∀ δ : ℝ, 0 < δ →
      ∃ q : FullL2, ∃ h : ℝ → ℂ,
        ContDiff ℝ 2 h ∧ tsupport h ⊆ Ioo (-t) t ∧
        (q : ℝ → ℂ) =ᵐ[volume] h ∧
        Integrable (oldDensity q) ∧ Integrable (oldDensity (q-f)) ∧
        (∫ u, oldDensity (q-f) u) < δ

def SmoothCore (t : ℝ) : Set (logCarrier t) :=
  {g | ∃ f : ℝ → ℂ, ContDiff ℝ 2 f ∧ tsupport f ⊆ Icc (-t) t ∧
    (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f}

theorem smooth_rep_supported (t : ℝ) (q : FullL2) (h : ℝ → ℂ)
    (hs : tsupport h ⊆ Ioo (-t) t) (hae : (q : ℝ → ℂ) =ᵐ[volume] h) :
    ∀ᵐ x ∂volume, x ∉ Icc (-t) t → q x = 0 := by
  filter_upwards [hae] with x hx
  intro hout
  rw [hx]
  by_contra hn
  have hm : x ∈ tsupport h := subset_tsupport _ (show x ∈ Function.support h from hn)
  exact hout (Ioo_subset_Icc_self (hs hm))

theorem fixed_support_approx (hOld : OldApproximation) (t : ℝ) (ht : 0 < t)
    (g : logCarrier t) (ε : ℝ) (hε : 0 < ε) :
    ∃ k : logCarrier t, k ∈ SmoothCore t ∧ ‖k-g‖ < ε := by
  let p := physicalInclusion t g
  have hnew : Integrable (newDensity p) := V08I.logCarrier_energy_integrable t g
  have hold := (V10B9a.integrable_old_iff_new p).mpr hnew
  have hC := V10B9a.forwardConstant_pos
  let δ := ε^2/forwardConstant
  have hδ : 0 < δ := by dsimp [δ]; positivity
  obtain ⟨q,h,hh,hs,hae,hq,herr,he⟩ := hOld t ht p
    (V08I.physicalInclusion_support t g) hold δ hδ
  have hqs := smooth_rep_supported t q h hs hae
  have hqn := (V10B9a.integrable_old_iff_new q).mp hq
  let k := V08J.liftPhysical t q hqs hqn
  have hk : physicalInclusion t k = q := V08J.physicalInclusion_lift t q hqs hqn
  refine ⟨k,⟨h,hh,hs.trans Ioo_subset_Icc_self,?_⟩,?_⟩
  · rw [hk]
    exact hae
  · have hn := V08I.logCarrier_energy t (k-g)
    rw [map_sub,hk] at hn
    change ‖k-g‖^2 = ∫ u, newDensity (q-p) u at hn
    have hb := V10B9a.energy_forward (q-p) herr
    have hlt := mul_lt_mul_of_pos_left he hC
    have hδeq : forwardConstant*δ = ε^2 := by dsimp [δ]; field_simp [hC.ne']
    rw [hδeq] at hlt
    have hsq : ‖k-g‖^2 < ε^2 := hn.trans_le hb |>.trans_lt hlt
    nlinarith [norm_nonneg (k-g)]

theorem core_dense_of_old (hOld : OldApproximation) (t : ℝ) (ht : 0 < t) :
    Dense (SmoothCore t) := by
  intro g
  rw [Metric.mem_closure_iff]
  intro ε hε
  obtain ⟨k,hk,he⟩ := fixed_support_approx hOld t ht g ε hε
  exact ⟨k,hk,by rw [dist_comm,dist_eq_norm]; exact he⟩

end WeilDefect.MasterRecon.V10B9b

#print axioms WeilDefect.MasterRecon.V10B9b.smooth_rep_supported
#print axioms WeilDefect.MasterRecon.V10B9b.fixed_support_approx
#print axioms WeilDefect.MasterRecon.V10B9b.core_dense_of_old
