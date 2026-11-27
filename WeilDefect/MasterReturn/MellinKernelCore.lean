import WeilDefect.MasterReturn.KernelCompleteness
import WeilDefect.MasterReturn.CarrierTranslation
import WeilDefect.MasterRecon.V10A2

/-! RETURN108-M: actual finite translation banks and full kernel receiver.
All sample and carrier maps are the original RECON objects.
The compact signed defect is an explicit premise; no positivity or
superlinear critical-line supply is used. Staged, not yet compiled. -/
namespace WeilDefect.MasterReturn.MellinKernelCore

open MeasureTheory Set Filter Metric
open scoped Topology ENNReal InnerProduct
open WeilDefect.MasterRecon
open V08I (logCarrier physicalInclusion)
open V10A (Index normalizedPair displacement multiplicity ordinate)
open CarrierTranslation KernelCompleteness

/-! The following evaluation linearity proofs are copied from the pinned
V10B6b carrierMellin interface, without importing the rectangle budget. -/
noncomputable def carrierMellin (t : ℝ) (g : V08I.logCarrier t) (z : ℂ) : ℂ :=
  V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ) z

theorem carrier_integrand_integrable (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t) (z : ℂ) :
    Integrable (fun x : ℝ => Complex.exp (z*(x : ℂ)) *
      V08I.physicalInclusion t g x) :=
  V09B.mellin_integrand_integrable t ht _
    (V08K.supported_integrable t _ (V08I.physicalInclusion_support t g))
    (V08I.physicalInclusion_support t g) z

theorem carrierMellin_add (t : ℝ) (ht : 0 ≤ t)
    (g h : V08I.logCarrier t) (z : ℂ) :
    carrierMellin t (g+h) z = carrierMellin t g z + carrierMellin t h z := by
  unfold carrierMellin V07A.mellin
  rw [← integral_add (carrier_integrand_integrable t ht g z)
    (carrier_integrand_integrable t ht h z)]
  apply integral_congr_ae
  rw [map_add]
  filter_upwards [Lp.coeFn_add (V08I.physicalInclusion t g)
    (V08I.physicalInclusion t h)] with x hx
  change (V08I.physicalInclusion t g + V08I.physicalInclusion t h) x =
    V08I.physicalInclusion t g x + V08I.physicalInclusion t h x at hx
  rw [hx, mul_add]

theorem carrierMellin_smul (t : ℝ) (a : ℂ)
    (g : V08I.logCarrier t) (z : ℂ) :
    carrierMellin t (a • g) z = a * carrierMellin t g z := by
  unfold carrierMellin V07A.mellin
  rw [← integral_const_mul]
  apply integral_congr_ae
  rw [map_smul]
  filter_upwards [Lp.coeFn_smul a (V08I.physicalInclusion t g)] with x hx
  change (a • V08I.physicalInclusion t g) x =
    a * V08I.physicalInclusion t g x at hx
  rw [hx]
  ring


/-- Literal coordinates, definitionally the same proposition as
V10B6d.LiteralCoordinates. The adapter is a separate source obligation. -/
def LiteralCoordinates (t : ℝ) (T : logCarrier t →L[ℂ] V07C.Coeff Index) : Prop :=
  ∀ (g : logCarrier t) (i : Index),
    T g i = normalizedPair (physicalInclusion t g : ℝ → ℂ) i

noncomputable def observation (t : ℝ) (ht : 0 ≤ t) (z : ℂ) :
    logCarrier t →ₗ[ℂ] ℂ where
  toFun g := carrierMellin t g z
  map_add' g h := carrierMellin_add t ht g h z
  map_smul' c g := carrierMellin_smul t c g z

theorem observation_eq (t : ℝ) (ht : 0 ≤ t) (z : ℂ) (g : logCarrier t) :
    observation t ht z g = V07A.mellin (physicalInclusion t g : ℝ → ℂ) z := rfl

theorem nonzero_mellin_neighborhood (a : ℝ) (ha : 0 ≤ a)
    (g : logCarrier a) (hg : g ≠ 0) :
    ∃ z : ℂ, ∃ r : ℝ, 0 < r ∧
      ∀ w ∈ ball z r, V07A.mellin (physicalInclusion a g : ℝ → ℂ) w ≠ 0 := by
  let F := V07A.mellin (physicalInclusion a g : ℝ → ℂ)
  have hF : F ≠ 0 := by
    intro h
    exact hg (V09B.carrier_zero_of_mellin_zero a g h)
  have hex : ∃ z, F z ≠ 0 := by
    by_contra hn
    apply hF
    funext z
    by_contra hz
    exact hn ⟨z, hz⟩
  obtain ⟨z, hz⟩ := hex
  have hc : Continuous F := continuous_iff_continuousAt.mpr fun w =>
    (V09B.mellin_entire a ha _ (V08K.supported_integrable a _
      (V08I.physicalInclusion_support a g))
      (V08I.physicalInclusion_support a g) w).continuousAt
  have ho : IsOpen (F ⁻¹' ({0} : Set ℂ)ᶜ) :=
    isClosed_singleton.isOpen_compl.preimage hc
  have hz' : z ∈ F ⁻¹' ({0} : Set ℂ)ᶜ := by simpa using hz
  obtain ⟨r, hr, hball⟩ := Metric.isOpen_iff.mp ho z hz'
  exact ⟨z, r, hr, fun w hw => by simpa using hball hw⟩

/-- Equally spaced positive translations fit in one enlarged aperture,
and the complex nodes can be varied along a real line in a nonvanishing
Mellin neighborhood. The two mesh sizes need not agree. -/
theorem finite_meshes (a b : ℝ) (hab : a < b) (z : ℂ)
    (r : ℝ) (hr : 0 < r) (n : ℕ) :
    ∃ d e : ℝ, 0 < d ∧ 0 < e ∧
      (∀ i : Fin n, a + |(i.val : ℝ)*d| ≤ b) ∧
      (∀ j : Fin n, z + ((j.val : ℝ)*e : ℝ) ∈ ball z r) ∧
      Function.Injective (fun j : Fin n =>
        Complex.exp ((z + ((j.val : ℝ)*e : ℝ))*(d:ℂ))) := by
  let d := (b-a)/((n:ℝ)+1)
  let e := r/((n:ℝ)+1)
  have hden : 0 < (n:ℝ)+1 := by positivity
  have hd : 0 < d := div_pos (sub_pos.mpr hab) hden
  have he : 0 < e := div_pos hr hden
  have hdm : ((n:ℝ)+1)*d = b-a := by
    dsimp [d]
    field_simp
  have hem : ((n:ℝ)+1)*e = r := by
    dsimp [e]
    field_simp
  refine ⟨d,e,hd,he,?_,?_,?_⟩
  · intro i
    have hi : (i.val:ℝ) ≤ (n:ℝ)+1 := by
      have h : (i.val:ℝ) < n := by exact_mod_cast i.isLt
      linarith
    rw [abs_of_nonneg (by positivity : 0 ≤ (i.val:ℝ)*d)]
    linarith [mul_le_mul_of_nonneg_right hi hd.le]
  · intro j
    have hj : (j.val:ℝ) < (n:ℝ)+1 := by
      have h : (j.val:ℝ) < n := by exact_mod_cast j.isLt
      linarith
    rw [mem_ball, dist_eq_norm, add_sub_cancel_left, Complex.norm_real,
      Real.norm_eq_abs, abs_of_nonneg (by positivity : 0 ≤ (j.val:ℝ)*e)]
    linarith [mul_lt_mul_of_pos_right hj he]
  · intro i j hij
    have h := congrArg norm hij
    simp only [Complex.norm_exp, Complex.mul_re, Complex.ofReal_re,
      Complex.ofReal_im, Complex.add_re, Complex.add_im, mul_zero, sub_zero] at h
    have h' := Real.exp_injective h
    apply Fin.ext
    have heq : (i.val:ℝ) = (j.val:ℝ) := by
      apply (mul_right_cancel₀ he.ne')
      apply (mul_right_cancel₀ hd.ne')
      nlinarith
    exact_mod_cast heq

theorem weighted_shift (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) (m : ℕ) (z : ℂ) :
    V07A.weightedMellin (physicalInclusion b (shiftCarrier a b s hab g) : ℝ → ℂ) m z =
      Complex.exp (z*(s:ℂ))*V07A.weightedMellin (physicalInclusion a g : ℝ → ℂ) m z := by
  unfold V07A.weightedMellin
  rw [shiftCarrier_mellin]
  ring

/-- A zero of the complete normalized pair remains zero after translation.
Critical singleton and nonfixed two-coordinate conventions are separated.
No cancellation in only one of the channels is used. -/
theorem normalizedPair_shift_zero (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) (i : Index)
    (hzero : normalizedPair (physicalInclusion a g : ℝ → ℂ) i = 0) :
    normalizedPair (physicalInclusion b (shiftCarrier a b s hab g) : ℝ → ℂ) i = 0 := by
  let f := (physicalInclusion a g : ℝ → ℂ)
  let h := (physicalInclusion b (shiftCarrier a b s hab g) : ℝ → ℂ)
  have hs (z : ℂ) : V07A.weightedMellin h (multiplicity i) z =
      Complex.exp (z*(s:ℂ))*V07A.weightedMellin f (multiplicity i) z :=
    weighted_shift a b s hab g _ z
  change normalizedPair f i = 0 at hzero
  change normalizedPair h i = 0
  by_cases hi : displacement i = 0
  · have hz := congrArg (fun p : V07C.Pair => (WithLp.ofLp p).1) hzero
    change (WithLp.ofLp (normalizedPair f i)).1 = 0 at hz
    rw [V10A.normalizedPair_fixed f i hi] at hz
    apply WithLp.ofLp_injective
    rw [V10A.normalizedPair_fixed h i hi]
    change (V07A.weightedMellin h (multiplicity i)
      ((ordinate i:ℂ)*Complex.I), (0:ℂ)) = (0,0)
    change V07A.weightedMellin f (multiplicity i) ((ordinate i:ℂ)*Complex.I) = 0 at hz
    rw [hs, hz, mul_zero]
  · rw [V10A.normalizedPair_nonfixed f i hi] at hzero
    rw [V10A.normalizedPair_nonfixed h i hi]
    let z := (displacement i:ℂ)+(ordinate i:ℂ)*Complex.I
    let w := -(displacement i:ℂ)+(ordinate i:ℂ)*Complex.I
    let u := V07A.weightedMellin f (multiplicity i) z
    let v := V07A.weightedMellin f (multiplicity i) w
    have hp := congrArg (fun p : V07C.Pair => (WithLp.ofLp p).1) hzero
    have hn := congrArg (fun p : V07C.Pair => (WithLp.ofLp p).2) hzero
    change V07A.pairPlus u v = 0 at hp
    change V07A.pairMinus u v = 0 at hn
    have he := V10A2.pair_energy_sum u v
    rw [hp, hn] at he
    have hu : u = 0 := norm_eq_zero.mp (by
      simp only [norm_zero, zero_pow (by norm_num : (2:ℕ) ≠ 0), zero_add] at he
      nlinarith [sq_nonneg ‖v‖, norm_nonneg u])
    have hv : v = 0 := norm_eq_zero.mp (by
      simp [hp, hn, hu] at he
      nlinarith [norm_nonneg v])
    apply WithLp.ofLp_injective
    change (V07A.pairPlus (V07A.weightedMellin h (multiplicity i) z)
      (V07A.weightedMellin h (multiplicity i) w),
      V07A.pairMinus (V07A.weightedMellin h (multiplicity i) z)
      (V07A.weightedMellin h (multiplicity i) w)) = (0,0)
    simp [hs, show V07A.weightedMellin f (multiplicity i) z = 0 from hu,
      show V07A.weightedMellin f (multiplicity i) w = 0 from hv,
      V07A.pairPlus, V07A.pairMinus]

theorem shift_mem_fullKernel (a b s : ℝ) (hab : a+|s| ≤ b)
    (A : logCarrier a →L[ℂ] V07C.Coeff Index)
    (T : logCarrier b →L[ℂ] V07C.Coeff Index)
    (hA : LiteralCoordinates a A) (hT : LiteralCoordinates b T)
    (g : logCarrier a) (hg : A g = 0) :
    shiftCarrier a b s hab g ∈ T.toLinearMap.ker := by
  change T (shiftCarrier a b s hab g) = 0
  apply lp.ext
  funext i
  change T (shiftCarrier a b s hab g) i = 0
  rw [hT _ i]
  apply normalizedPair_shift_zero
  rw [← hA g i, hg]
  rfl

theorem actual_kernel_banks (a b : ℝ) (ha : 0 ≤ a) (hab : a < b)
    (A : logCarrier a →L[ℂ] V07C.Coeff Index)
    (T : logCarrier b →L[ℂ] V07C.Coeff Index)
    (hA : LiteralCoordinates a A) (hT : LiteralCoordinates b T)
    (g : logCarrier a) (hg : A g = 0) (hnz : g ≠ 0) (n : ℕ) :
    ∃ v : Fin n → T.toLinearMap.ker, LinearIndependent ℂ v := by
  obtain ⟨z,r,hr,hF⟩ := nonzero_mellin_neighborhood a ha g hnz
  obtain ⟨d,e,hd,he,hs,hz,hinj⟩ := finite_meshes a b hab z r hr n
  let w : Fin n → ℂ := fun j => z + ((j.val:ℝ)*e:ℝ)
  let v : Fin n → T.toLinearMap.ker := fun i =>
    ⟨shiftCarrier a b ((i.val:ℝ)*d) (hs i) g,
      shift_mem_fullKernel a b _ (hs i) A T hA hT g hg⟩
  refine ⟨v, independent_of_vandermonde_observations v
    (fun j => (observation b (ha.trans hab.le) (w j)).comp T.toLinearMap.ker.subtype)
    (fun j => Complex.exp (w j*(d:ℂ)))
    (fun j => V07A.mellin (physicalInclusion a g : ℝ → ℂ) (w j))
    hinj (fun j => hF _ (hz j)) ?_⟩
  intro j i
  change V07A.mellin (physicalInclusion b
    (shiftCarrier a b ((i.val:ℝ)*d) (hs i) g) : ℝ → ℂ) (w j) = _
  rw [shiftCarrier_mellin]
  have h : w j * (((i.val:ℝ)*d:ℝ):ℂ) = (i.val:ℂ)*(w j*(d:ℂ)) := by
    push_cast
    ring
  rw [h, Complex.exp_nat_mul, mul_comm]

/-- Conditional full-kernel receiver independent of rectangle sampling budgets.
The factor R can be instantiated by the literal signed adjoint receiver
when that operator module has been verified. -/
theorem actual_fullKernel_zero_of_factor (a b : ℝ) (ha : 0 ≤ a) (hab : a < b)
    (A : logCarrier a →L[ℂ] V07C.Coeff Index)
    (T : logCarrier b →L[ℂ] V07C.Coeff Index)
    (hA : LiteralCoordinates a A) (hT : LiteralCoordinates b T)
    (R : V07C.Coeff Index →L[ℂ] logCarrier b)
    (K : logCarrier b →L[ℂ] logCarrier b) (hK : IsCompactOperator K)
    (hfactor : R.comp T = ContinuousLinearMap.id ℂ (logCarrier b)+K)
    (g : logCarrier a) (hg : A g = 0) : g = 0 :=
  fullSample_zero_of_enlarged_compact T R K hK hfactor g
    (fun hnz n => actual_kernel_banks a b ha hab A T hA hT g hg hnz n)

end WeilDefect.MasterReturn.MellinKernelCore

#print axioms WeilDefect.MasterReturn.MellinKernelCore.observation_eq
#print axioms WeilDefect.MasterReturn.MellinKernelCore.nonzero_mellin_neighborhood
#print axioms WeilDefect.MasterReturn.MellinKernelCore.finite_meshes
#print axioms WeilDefect.MasterReturn.MellinKernelCore.weighted_shift
#print axioms WeilDefect.MasterReturn.MellinKernelCore.normalizedPair_shift_zero
#print axioms WeilDefect.MasterReturn.MellinKernelCore.shift_mem_fullKernel
#print axioms WeilDefect.MasterReturn.MellinKernelCore.actual_kernel_banks
#print axioms WeilDefect.MasterReturn.MellinKernelCore.actual_fullKernel_zero_of_factor

#print axioms WeilDefect.MasterReturn.MellinKernelCore.carrier_integrand_integrable
#print axioms WeilDefect.MasterReturn.MellinKernelCore.carrierMellin_add
#print axioms WeilDefect.MasterReturn.MellinKernelCore.carrierMellin_smul
