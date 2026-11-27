import WeilDefect.MasterRecon.V10B6c

/-! V10B6d: absolute convergence of the normalized signed orbit
diagonal and its literal arithmetic evaluation. Full-strip reindexing,
reflection multiplicity and the original explicit formula are not
asserted by this module. -/
namespace WeilDefect.MasterRecon.V10B6d

open scoped ENNReal NNReal InnerProduct ComplexConjugate
open V10A (Index displacement ordinate multiplicity normalizedPair)
open V10B6c (channel analysisChannel signedGram)

variable {ι : Type*}

theorem channel_sq_summable (b : Bool) (x : V07C.Coeff ι) :
    Summable (fun i => ‖channel b (x i)‖^2) := by
  have h := (lp.memℓp (V10B6c.projection b x)).summable
    (by norm_num : 0 < (2 : ℝ≥0∞).toReal)
  simpa only [ENNReal.toReal_ofNat, Real.rpow_natCast, V10B6c.projection_apply] using h

theorem signed_channel_abs_summable (x : V07C.Coeff ι) :
    Summable (fun i => |‖channel true (x i)‖^2 - ‖channel false (x i)‖^2|) := by
  apply Summable.of_norm_bounded ((channel_sq_summable true x).add (channel_sq_summable false x))
  intro i
  rw [Real.norm_eq_abs, abs_abs]
  exact abs_sub_le_add_of_nonneg (sq_nonneg _) (sq_nonneg _)

theorem signed_channel_tsum (x : V07C.Coeff ι) :
    (∑' i, (‖channel true (x i)‖^2 - ‖channel false (x i)‖^2)) =
      ‖V10B6c.projection true x‖^2 - ‖V10B6c.projection false x‖^2 := by
  rw [(channel_sq_summable true x).tsum_sub (channel_sq_summable false x),
    V10B6a.lp_two_norm_sq, V10B6a.lp_two_norm_sq]
  simp only [V10B6c.projection_apply]

noncomputable def orbitTerm (f : ℝ → ℂ) (i : Index) : ℝ :=
  if displacement i = 0 then
    (multiplicity i : ℝ)*‖V07A.mellin f ((i : ℂ)-1/2)‖^2
  else
    2 * (V07A.weightedMellin f (multiplicity i) ((i : ℂ)-1/2) *
      conj (V07A.weightedMellin f (multiplicity i)
        (V10A.reflect (i : ℂ)-1/2))).re

theorem orbitTerm_eq_channel (f : ℝ → ℂ) (i : Index) :
    orbitTerm f i = ‖channel true (normalizedPair f i)‖^2 -
      ‖channel false (normalizedPair f i)‖^2 := by
  unfold orbitTerm
  change _ = ‖(WithLp.ofLp (normalizedPair f i)).1‖^2 -
    ‖(WithLp.ofLp (normalizedPair f i)).2‖^2
  by_cases hi : displacement i = 0
  · rw [if_pos hi, V10B6a.fixed_exponent i hi]
    exact (V10A2.normalized_fixed_energy f i hi).symm
  · rw [if_neg hi]
    exact (V10A2.normalized_nonfixed_energy f i hi).symm

theorem orbitTerm_abs_le (f : ℝ → ℂ) (i : Index) :
    |orbitTerm f i| ≤ ‖normalizedPair f i‖^2 := by
  rw [orbitTerm_eq_channel, V10B6a.pair_norm_sq]
  change |‖(WithLp.ofLp (normalizedPair f i)).1‖^2 -
    ‖(WithLp.ofLp (normalizedPair f i)).2‖^2| ≤ _
  exact abs_sub_le_add_of_nonneg (sq_nonneg _) (sq_nonneg _)

variable (t : ℝ)
variable (T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index)

def LiteralCoordinates : Prop :=
  ∀ (g : V08I.logCarrier t) (i : Index),
    T g i = normalizedPair (V08I.physicalInclusion t g : ℝ → ℂ) i

theorem positive_coordinates (hT : LiteralCoordinates t T)
    (g : V08I.logCarrier t) (i : Index) :
    analysisChannel true T g i =
      (WithLp.ofLp (normalizedPair (V08I.physicalInclusion t g : ℝ → ℂ) i)).1 := by
  rw [V10B6c.analysisChannel_apply, hT g i]
  rfl

theorem negative_coordinates (hT : LiteralCoordinates t T)
    (g : V08I.logCarrier t) (i : Index) :
    analysisChannel false T g i =
      (WithLp.ofLp (normalizedPair (V08I.physicalInclusion t g : ℝ → ℂ) i)).2 := by
  rw [V10B6c.analysisChannel_apply, hT g i]
  rfl

theorem arithmetic_orbit_abs_summable (hT : LiteralCoordinates t T)
    (g : V08I.logCarrier t) :
    Summable (fun i : Index => |orbitTerm (V08I.physicalInclusion t g : ℝ → ℂ) i|) := by
  have h := signed_channel_abs_summable (T g)
  apply h.congr
  intro i
  rw [hT g i, orbitTerm_eq_channel]

theorem arithmetic_orbit_diagonal (hT : LiteralCoordinates t T)
    (g : V08I.logCarrier t) :
    (inner ℂ (signedGram T g) g).re =
      ∑' i : Index, orbitTerm (V08I.physicalInclusion t g : ℝ → ℂ) i := by
  rw [V10B6c.signedGram_diagonal]
  change ‖V10B6c.projection true (T g)‖^2 -
    ‖V10B6c.projection false (T g)‖^2 = _
  rw [← signed_channel_tsum]
  apply tsum_congr
  intro i
  rw [hT g i, orbitTerm_eq_channel]

theorem arithmetic_positive_kernel (ht : 0 ≤ t) (hT : LiteralCoordinates t T)
    (hm : ∀ ρ, V09D.stripZero ρ → 0 < V09D.mult ρ)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (g : V08I.logCarrier t) (hg : analysisChannel true T g = 0) : g = 0 :=
  V10A2.normalized_positive_kernel t ht (analysisChannel true T)
    hm hdens (positive_coordinates t T hT) g hg

theorem arithmetic_positive_coercivity (ht : 0 ≤ t) (hT : LiteralCoordinates t T)
    (hm : ∀ ρ, V09D.stripZero ρ → 0 < V09D.mult ρ)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ g : V08I.logCarrier t,
      ‖g‖^2 ≤ ‖analysisChannel true T g‖^2 +
        M * ‖V08I.physicalInclusion t g‖^2) :
    ∃ b : ℝ≥0, 0 < b ∧ ∀ g : V08I.logCarrier t,
      ‖g‖^2 * (b : ℝ) ≤ ‖analysisChannel true T g‖^2 :=
  V10A2.normalized_positive_coercivity t ht (analysisChannel true T)
    hm hdens (positive_coordinates t T hT) M hM hdef

theorem arithmetic_signed_receiver (ht : 0 ≤ t) (A : ℝ) (hA : 0 ≤ A)
    (hcount : ∀ n : ℤ, (V09D.count (n : ℝ) ((n : ℝ)+1) : ℝ) ≤
      A * Real.log (|(n : ℝ)|+3)) :
    ∃ T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index,
      LiteralCoordinates t T ∧
      (signedGram T).adjoint = signedGram T ∧
      ∀ g : V08I.logCarrier t,
        Summable (fun i : Index => |orbitTerm (V08I.physicalInclusion t g : ℝ → ℂ) i|) ∧
        (inner ℂ (signedGram T g) g).re =
          ∑' i : Index, orbitTerm (V08I.physicalInclusion t g : ℝ → ℂ) i := by
  obtain ⟨T,hT⟩ := V10B6b.bounded_arithmetic_analysis t ht A hA hcount
  exact ⟨T,hT,V10B6c.signedGram_symmetric T,fun g =>
    ⟨arithmetic_orbit_abs_summable t T hT g, arithmetic_orbit_diagonal t T hT g⟩⟩

end WeilDefect.MasterRecon.V10B6d

#print axioms WeilDefect.MasterRecon.V10B6d.channel_sq_summable
#print axioms WeilDefect.MasterRecon.V10B6d.signed_channel_abs_summable
#print axioms WeilDefect.MasterRecon.V10B6d.signed_channel_tsum
#print axioms WeilDefect.MasterRecon.V10B6d.orbitTerm_eq_channel
#print axioms WeilDefect.MasterRecon.V10B6d.orbitTerm_abs_le
#print axioms WeilDefect.MasterRecon.V10B6d.positive_coordinates
#print axioms WeilDefect.MasterRecon.V10B6d.negative_coordinates
#print axioms WeilDefect.MasterRecon.V10B6d.arithmetic_orbit_abs_summable
#print axioms WeilDefect.MasterRecon.V10B6d.arithmetic_orbit_diagonal
#print axioms WeilDefect.MasterRecon.V10B6d.arithmetic_positive_kernel
#print axioms WeilDefect.MasterRecon.V10B6d.arithmetic_positive_coercivity
#print axioms WeilDefect.MasterRecon.V10B6d.arithmetic_signed_receiver
