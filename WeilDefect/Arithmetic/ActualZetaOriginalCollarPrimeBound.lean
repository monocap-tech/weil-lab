import WeilDefect.Arithmetic.ActualZetaOriginalCollarFourierMass
import WeilDefect.Arithmetic.ActualZetaOriginalRealOddSchwartzFullSource
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointTwistedAmplitude
import Mathlib.MeasureTheory.Group.Integral

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate

/-! NF600: attach the genuine two-collar geometry to the actual
correlation and literal prime term. Use one cross-collar overlap
per sign, with the left/right squared energies paid exactly once. -/

theorem neutralNF600Correlation_eq (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) (t : ℝ) :
    neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) t =
      ∫ x : ℝ, s x * conj (s (x-t)) := by
  have h := neutralNF573OriginalCollar_window_ae s hs
  have ht := (measurePreserving_sub_right volume t).quasiMeasurePreserving.ae_eq_comp h
  unfold neutralWindowCorrelation
  apply integral_congr_ae
  filter_upwards [h,ht] with x hx hxt
  simpa only [Function.comp_apply,hx,hxt]

theorem neutralNF600Correlation_prime_vanish (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (n : ℕ) (hn : 2≤n) (h9 : n≠9) :
    neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (Real.log n)=0 ∧
    neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (-Real.log n)=0 := by
  have hp : 0 ≤ Real.log (n:ℝ) := Real.log_nonneg (by exact_mod_cast (show 1≤n by omega))
  constructor
  · rw [neutralNF600Correlation_eq s hs]
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    by_cases hx : x ∈ neutralNF543OriginalCollars
    · have hy : x-Real.log n ∉ neutralNF543OriginalCollars := by
        intro hy
        apply neutralNF600NoPrimeOverlap n hn h9 _ _ hy hx
        rw [show x-(x-Real.log n)=Real.log n by ring,abs_of_nonneg hp]
      simp [hs _ hy]
    · simp [hs _ hx]
  · rw [neutralNF600Correlation_eq s hs]
    apply integral_eq_zero_of_ae
    filter_upwards [] with x
    by_cases hx : x ∈ neutralNF543OriginalCollars
    · have hy : x-(-Real.log n) ∉ neutralNF543OriginalCollars := by
        intro hy
        apply neutralNF600NoPrimeOverlap n hn h9 _ _ hx hy
        rw [show x-(-Real.log n)-x=Real.log n by ring,abs_of_nonneg hp]
      simp [hs _ hy]
    · simp [hs _ hx]

/-- General translated product estimate with disjoint source masks.
The masks only select which two physical energy pieces are charged. -/
theorem neutralNF600CrossCorrelation_bound (s : 𝓢(ℝ,ℂ)) (t : ℝ)
    (A B : Set ℝ) (hA : MeasurableSet A) (hB : MeasurableSet B)
    (hd : Disjoint A B)
    (hcross : ∀ x, s x ≠ 0 → s (x-t) ≠ 0 → x ∈ A ∧ x-t ∈ B) :
    ‖∫ x : ℝ, s x * conj (s (x-t))‖ ≤ neutralNF600Mass s/2 := by
  let e := fun x : ℝ => ‖s x‖^2
  let a := A.indicator e
  let b := B.indicator e
  have he : Integrable e :=
    (memLp_two_iff_integrable_sq_norm s.continuous.aestronglyMeasurable).mp (s.memLp 2 volume)
  have ha : Integrable a := he.indicator hA
  have hb : Integrable b := he.indicator hB
  have hbt : Integrable (fun x : ℝ => b (x-t)) :=
    ((measurePreserving_sub_right volume t).integrable_comp hb.aestronglyMeasurable).mpr hb
  have hg : Integrable (fun x : ℝ => (a x + b (x-t))/2) :=
    (ha.add hbt).div_const 2
  have hpoint (x : ℝ) : ‖s x * conj (s (x-t))‖ ≤ (a x+b (x-t))/2 := by
    by_cases hx : s x=0
    · simp only [hx,zero_mul,norm_zero]
      apply div_nonneg _ (by norm_num)
      exact add_nonneg (by dsimp [a]; split_ifs <;> positivity)
        (by dsimp [b]; split_ifs <;> positivity)
    by_cases hy : s (x-t)=0
    · simp only [hy,map_zero,mul_zero,norm_zero]
      apply div_nonneg _ (by norm_num)
      exact add_nonneg (by dsimp [a]; split_ifs <;> positivity)
        (by dsimp [b]; split_ifs <;> positivity)
    obtain ⟨hxa,hxb⟩ := hcross x hx hy
    simp only [a,b,Set.indicator_of_mem hxa,Set.indicator_of_mem hxb,e,norm_mul,Complex.norm_conj]
    nlinarith only [sq_nonneg (‖s x‖-‖s (x-t)‖)]
  have hi : Integrable (fun x : ℝ => ‖s x * conj (s (x-t))‖) := by
    apply hg.mono' (by fun_prop)
    filter_upwards [] with x
    rw [Real.norm_eq_abs,abs_of_nonneg (norm_nonneg _)]
    exact hpoint x
  have hsum : (∫ x : ℝ, a x+b x) ≤ ∫ x : ℝ,e x := by
    apply integral_mono (ha.add hb) he
    intro x
    by_cases hxa : x∈A
    · have hxb : x∉B := fun h => Set.disjoint_left.mp hd hxa h
      simp [a,b,hxa,hxb]
    · by_cases hxb : x∈B
      · simp [a,b,hxa,hxb]
      · simp [a,b,hxa,hxb,e]
  have hcost : (∫ x : ℝ, (a x+b (x-t))/2) ≤ neutralNF600Mass s/2 := by
    rw [integral_div,integral_add ha hbt,integral_sub_right_eq_self,
      neutralNF600Mass_eq_integral]
    rw [integral_add ha hb] at hsum
    exact div_le_div_of_nonneg_right hsum (by norm_num)
  exact (norm_integral_le_integral_norm _).trans
    ((integral_mono hi hg hpoint).trans hcost)

theorem neutralNF600Correlation_log9_bound (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    ∀ t : ℝ, t=Real.log 9 ∨ t=-Real.log 9 →
      ‖neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) t‖ ≤
        neutralNF600Mass s/2 := by
  let L := Ioo (-(11/10:ℝ)) (-(11/10:ℝ)+1/500)
  let R := Ioo ((11/10:ℝ)-1/500) (11/10:ℝ)
  have hd : Disjoint L R := by
    rw [Set.disjoint_left]
    intro x hx hy
    linarith [hx.2,hy.1]
  intro t ht
  rw [neutralNF600Correlation_eq s hs]
  rcases ht with rfl|rfl
  · apply neutralNF600CrossCorrelation_bound s _ R L measurableSet_Ioo measurableSet_Ioo hd.symm
    intro x hx hy
    have hu : x∈neutralNF543OriginalCollars := by by_contra h; exact hx (hs _ h)
    have hv : x-Real.log 9∈neutralNF543OriginalCollars := by by_contra h; exact hy (hs _ h)
    have hh := neutralNF600Log9_cross _ _ hv hu (by ring)
    exact ⟨hh.2,hh.1⟩
  · apply neutralNF600CrossCorrelation_bound s _ L R measurableSet_Ioo measurableSet_Ioo hd
    intro x hx hy
    have hu : x∈neutralNF543OriginalCollars := by by_contra h; exact hx (hs _ h)
    have hv : x-(-Real.log 9)∈neutralNF543OriginalCollars := by by_contra h; exact hy (hs _ h)
    exact neutralNF600Log9_cross _ _ hu hv (by ring)

def neutralNF600Prime (s : 𝓢(ℝ,ℂ)) : ℂ :=
  ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
    (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (Real.log n) +
      neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (-Real.log n))

theorem neutralNF600Prime_single (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    neutralNF600Prime s =
      ((ArithmeticFunction.vonMangoldt 9 / Real.sqrt 9 : ℝ) : ℂ) *
        (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (Real.log 9) +
        neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (-Real.log 9)) := by
  unfold neutralNF600Prime
  apply tsum_eq_single 9
  intro n hn
  by_cases h : 2≤n
  · obtain ⟨h1,h2⟩ := neutralNF600Correlation_prime_vanish s hs n h hn
    simp [h1,h2]
  · have he : n=0 ∨ n=1 := by omega
    rcases he with rfl|rfl <;> simp

/-- The coefficient is a separate exact arithmetic lemma; the
complete prime sum has already been reduced to the true n=9 term. -/
theorem neutralNF600Prime_bound (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (hc : ArithmeticFunction.vonMangoldt 9 / Real.sqrt 9 ≤ (2/5:ℝ)) :
    |(neutralNF600Prime s).re| ≤ (2/5:ℝ)*neutralNF600Mass s := by
  have h1 := neutralNF600Correlation_log9_bound s hs (Real.log 9) (Or.inl rfl)
  have h2 := neutralNF600Correlation_log9_bound s hs (-Real.log 9) (Or.inr rfl)
  apply (Complex.abs_re_le_norm _).trans
  rw [neutralNF600Prime_single s hs,norm_mul,Complex.norm_real,Real.norm_eq_abs,
    abs_of_nonneg (div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _))]
  have hs0 := norm_add_le
    (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (Real.log 9))
    (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (-Real.log 9))
  have hh : ‖neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (Real.log 9) +
    neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (-Real.log 9)‖ ≤
    neutralNF600Mass s := by linarith
  exact mul_le_mul hc hh (norm_nonneg _) (by norm_num)

theorem neutralNF600Prime9_coefficient :
    ArithmeticFunction.vonMangoldt 9 / Real.sqrt 9 ≤ (2/5:ℝ) := by
  have h9 : ArithmeticFunction.vonMangoldt 9 = Real.log 3 := by
    rw [show (9:ℕ)=3^2 by norm_num,
      ArithmeticFunction.vonMangoldt_apply_pow (by decide),
      ArithmeticFunction.vonMangoldt_apply_prime (by decide)]
  have he : (3:ℝ) < Real.exp (6/5) := by
    have h := Real.sum_le_exp_of_nonneg (show (0:ℝ) ≤ 6/5 by norm_num) 5
    apply lt_of_lt_of_le _ h
    norm_num [Finset.sum_range_succ,Nat.factorial_succ]
  have hl := (Real.log_lt_iff_lt_exp (by norm_num : (0:ℝ)<3)).mpr he
  rw [h9,show Real.sqrt 9=3 by norm_num]
  linarith

theorem neutralNF600Prime_bound_actual (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    |(neutralNF600Prime s).re| ≤ (2/5:ℝ)*neutralNF600Mass s :=
  neutralNF600Prime_bound s hs neutralNF600Prime9_coefficient

end
end WeilDefect
