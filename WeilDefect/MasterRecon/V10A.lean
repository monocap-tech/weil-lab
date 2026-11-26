import WeilDefect.MasterRecon.V09D
import WeilDefect.MasterRecon.V09E

/-! V10A: actual right-half strip-zero indexing and fixed-point
normalization. Arithmetic reflection closure and positivity of the
analytic multiplicity remain explicit inputs. Critical-line zeros are
singletons, not duplicated reflected pairs. -/
namespace WeilDefect.MasterRecon.V10A

open scoped ENNReal ComplexConjugate

abbrev Index := {ρ : ℂ // V09D.stripZero ρ ∧ (1 : ℝ) / 2 ≤ ρ.re}

def reflect (ρ : ℂ) : ℂ := 1 - conj ρ

noncomputable def displacement (i : Index) : ℝ := (i : ℂ).re - 1 / 2

def ordinate (i : Index) : ℝ := (i : ℂ).im

noncomputable def multiplicity (i : Index) : ℕ := V09D.mult (i : ℂ)

theorem reflect_re (ρ : ℂ) : (reflect ρ).re = 1 - ρ.re := by
  simp [reflect, Complex.sub_re]

theorem reflect_im (ρ : ℂ) : (reflect ρ).im = ρ.im := by
  simp [reflect, Complex.sub_im]

theorem reflect_involution (ρ : ℂ) : reflect (reflect ρ) = ρ := by
  apply Complex.ext
  · rw [reflect_re, reflect_re]; ring
  · rw [reflect_im, reflect_im]

theorem reflect_fixed_iff (ρ : ℂ) : reflect ρ = ρ ↔ ρ.re = 1 / 2 := by
  constructor
  · intro h
    have he := congrArg Complex.re h
    rw [reflect_re] at he
    linarith
  · intro h
    apply Complex.ext
    · rw [reflect_re, h]; norm_num
    · exact reflect_im ρ

theorem displacement_nonnegative (i : Index) : 0 ≤ displacement i := by
  exact sub_nonneg.mpr i.property.2

theorem displacement_bound (i : Index) : |displacement i| ≤ 1 / 2 := by
  rw [abs_of_nonneg (displacement_nonnegative i)]
  have h := i.property.1.2.2
  unfold displacement
  linarith

theorem right_exponent (i : Index) :
    ((displacement i : ℝ) : ℂ) + (ordinate i : ℂ) * Complex.I =
      (i : ℂ) - 1 / 2 := by
  apply Complex.ext <;>
    simp [displacement, ordinate, Complex.sub_re, Complex.sub_im,
      Complex.add_re, Complex.add_im, Complex.mul_re, Complex.mul_im,
      Complex.div_re, Complex.div_im] <;> norm_num

theorem left_exponent (i : Index) :
    -((displacement i : ℝ) : ℂ) + (ordinate i : ℂ) * Complex.I =
      reflect (i : ℂ) - 1 / 2 := by
  apply Complex.ext <;>
    simp [displacement, ordinate, reflect_re, reflect_im,
      Complex.sub_re, Complex.sub_im, Complex.add_re, Complex.add_im,
      Complex.mul_re, Complex.mul_im, Complex.div_re, Complex.div_im] <;>
    ring

/-- Every strip zero belongs to exactly one reflection orbit
represented by a right-half zero; this statement proves existence.
Uniqueness is separated below. -/
theorem orbit_coverage
    (hr : ∀ ρ, V09D.stripZero ρ → V09D.stripZero (reflect ρ))
    (ρ : ℂ) (hρ : V09D.stripZero ρ) :
    ∃ i : Index, ρ = (i : ℂ) ∨ ρ = reflect (i : ℂ) := by
  by_cases h : (1 : ℝ) / 2 ≤ ρ.re
  · exact ⟨⟨ρ, hρ, h⟩, Or.inl rfl⟩
  · have hh : (1 : ℝ) / 2 ≤ (reflect ρ).re := by
      rw [reflect_re]
      linarith [lt_of_not_ge h]
    exact ⟨⟨reflect ρ, hr ρ hρ, hh⟩, Or.inr (reflect_involution ρ).symm⟩

theorem orbit_representative_unique (i j : Index)
    (h : (i : ℂ) = (j : ℂ) ∨ (i : ℂ) = reflect (j : ℂ)) : i = j := by
  apply Subtype.ext
  rcases h with h | h
  · exact h
  · have hi := i.property.2
    have hj := j.property.2
    have he := congrArg Complex.re h
    rw [reflect_re] at he
    have hfix : (j : ℂ).re = 1 / 2 := by linarith
    exact h.trans ((reflect_fixed_iff (j : ℂ)).mpr hfix)

theorem critical_coverage
    (hm : ∀ ρ, V09D.stripZero ρ → 0 < V09D.mult ρ)
    (z : ℂ) (hz : V09C.CriticalSample z) :
    ∃ i : Index, displacement i = 0 ∧ 0 < multiplicity i ∧
      (ordinate i : ℂ) * Complex.I = z := by
  rcases hz with ⟨hre, him, hzero⟩
  let ρ : ℂ := (1 / 2 : ℂ) + z
  have hr : ρ.re = 1 / 2 := by
    simp [ρ, Complex.add_re, Complex.div_re, hre] <;> norm_num
  have hs : V09D.stripZero ρ := ⟨hzero, by rw [hr]; norm_num, by rw [hr]; norm_num⟩
  let i : Index := ⟨ρ, hs, hr.ge⟩
  refine ⟨i, ?_, hm ρ hs, ?_⟩
  · change ρ.re - 1 / 2 = 0
    rw [hr, sub_self]
  · apply Complex.ext
    · simp [Complex.mul_re, hre]
    · simp [ordinate, i, ρ, Complex.mul_im, Complex.add_im, Complex.div_im]

/-- Nonfixed reflection orbits use the ordinary two-point unitary
pair transform. Fixed points use one copy of the weighted sample
and a zero negative coordinate. This avoids a factor-of-two error
in the actual Weil sum. -/
noncomputable def normalizedPair (f : ℝ → ℂ) (i : Index) : V07C.Pair :=
  if displacement i = 0 then
    WithLp.toLp 2
      (V07A.weightedMellin f (multiplicity i) ((ordinate i : ℂ) * Complex.I), 0)
  else V07E.samplePair f (multiplicity i) (displacement i) (ordinate i)

theorem normalizedPair_fixed (f : ℝ → ℂ) (i : Index) (h : displacement i = 0) :
    WithLp.ofLp (normalizedPair f i) =
      (V07A.weightedMellin f (multiplicity i) ((ordinate i : ℂ) * Complex.I), 0) := by
  simp [normalizedPair, h]

theorem normalizedPair_nonfixed (f : ℝ → ℂ) (i : Index) (h : displacement i ≠ 0) :
    normalizedPair f i =
      V07E.samplePair f (multiplicity i) (displacement i) (ordinate i) := by
  simp [normalizedPair, h]

theorem normalized_fixed_zero (f : ℝ → ℂ) (i : Index)
    (hd : displacement i = 0) (hm : 0 < multiplicity i)
    (hz : (WithLp.ofLp (normalizedPair f i)).1 = 0) :
    V07A.mellin f ((ordinate i : ℂ) * Complex.I) = 0 := by
  rw [normalizedPair_fixed f i hd] at hz
  change (Real.sqrt (multiplicity i : ℝ) : ℂ) *
    V07A.mellin f ((ordinate i : ℂ) * Complex.I) = 0 at hz
  have hq : (Real.sqrt (multiplicity i : ℝ) : ℂ) ≠ 0 := by
    have hp : 0 < Real.sqrt (multiplicity i : ℝ) :=
      Real.sqrt_pos.2 (by exact_mod_cast hm)
    exact_mod_cast hp.ne'
  exact (mul_eq_zero.mp hz).resolve_left hq

end WeilDefect.MasterRecon.V10A

#print axioms WeilDefect.MasterRecon.V10A.reflect_re
#print axioms WeilDefect.MasterRecon.V10A.reflect_im
#print axioms WeilDefect.MasterRecon.V10A.reflect_involution
#print axioms WeilDefect.MasterRecon.V10A.reflect_fixed_iff
#print axioms WeilDefect.MasterRecon.V10A.displacement_nonnegative
#print axioms WeilDefect.MasterRecon.V10A.displacement_bound
#print axioms WeilDefect.MasterRecon.V10A.right_exponent
#print axioms WeilDefect.MasterRecon.V10A.left_exponent
#print axioms WeilDefect.MasterRecon.V10A.orbit_coverage
#print axioms WeilDefect.MasterRecon.V10A.orbit_representative_unique
#print axioms WeilDefect.MasterRecon.V10A.critical_coverage
#print axioms WeilDefect.MasterRecon.V10A.normalizedPair_fixed
#print axioms WeilDefect.MasterRecon.V10A.normalizedPair_nonfixed
#print axioms WeilDefect.MasterRecon.V10A.normalized_fixed_zero
