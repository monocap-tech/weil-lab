import WeilDefect.Arithmetic.ActualZetaIV099OriginalFiniteCollarSectorGate
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap BigOperators ContDiff

/-- Scalar affine pullback of the same certified IV097 plateau. -/
def neutralIV100AffineFun (a b : ℝ) (x : ℝ) : ℂ :=
  (neutralIV097Plateau (a*x+b) : ℂ)

theorem neutralIV100Affine_compact (a b : ℝ) (ha : 0 < a) :
    HasCompactSupport (neutralIV100AffineFun a b) := by
  apply HasCompactSupport.intro
    (K := Icc ((1099/1000-3/4000-b)/a) ((1099/1000+3/4000-b)/a))
    isCompact_Icc
  intro x hx
  have hz : (3/4000:ℝ) ≤ |a*x+b-1099/1000| := by
    by_contra h
    have h' := abs_lt.mp (lt_of_not_ge h)
    apply hx
    constructor
    · apply (div_le_iff₀ ha).mpr
      nlinarith [h'.1]
    · apply (le_div_iff₀ ha).mpr
      linarith [h'.2]
  simp [neutralIV100AffineFun, neutralIV097Plateau_zero _ hz]

def neutralIV100Affine (a b : ℝ) (ha : 0 < a) : 𝓢(ℝ,ℂ) :=
  (neutralIV100Affine_compact a b ha).toSchwartzMap
    ((Complex.ofRealCLM.contDiff.comp neutralIV097Plateau_smooth).comp
      (show ContDiff ℝ ∞ (fun x : ℝ => a*x+b) by fun_prop))

theorem neutralIV100Affine_hasDerivAt (a b x : ℝ) :
    HasDerivAt (fun y : ℝ => neutralIV097Plateau (a*y+b))
      (neutralIV097PlateauDerivative (a*x+b) * a) x := by
  have hlin : HasDerivAt (fun y : ℝ => a*y+b) a x := by
    simpa using ((hasDerivAt_id x).const_mul a).add_const b
  have h := (neutralIV097Plateau_hasDerivAt (a*x+b)).comp x hlin
  change HasDerivAt (fun y : ℝ => neutralIV097Plateau (a*y+b))
    (neutralIV097PlateauDerivative (a*x+b) * a) x at h
  exact h

theorem neutralIV100Affine_derivative (a b : ℝ) (ha : 0 < a) (x : ℝ) :
    deriv (neutralIV100Affine a b ha : ℝ → ℂ) x =
      (neutralIV097PlateauDerivative (a*x+b) : ℂ) * (a : ℂ) := by
  change deriv (fun y : ℝ => (neutralIV097Plateau (a*y+b) : ℂ)) x = _
  simpa only [Complex.ofReal_mul] using
    (neutralIV100Affine_hasDerivAt a b x).ofReal_comp.deriv

/-- Exact Lebesgue Jacobian; no numerical quadrature. -/
theorem neutralIV100Affine_integral (g : ℝ → ℝ) (a b : ℝ) (ha : 0 < a) :
    (∫ x : ℝ, g (a*x+b)) = a⁻¹ * ∫ x : ℝ, g x := by
  have he : (fun x : ℝ => g (a*x+b)) = fun x => g (a*(x+b/a)) := by
    funext x
    congr 1
    field_simp [ha.ne'] <;> ring
  rw [he]
  calc
    (∫ x : ℝ, g (a*(x+b/a))) = ∫ x : ℝ, g (a*x) :=
      integral_add_right_eq_self (fun x : ℝ => g (a*x)) (b/a)
    _ = _ := by
      rw [Measure.integral_comp_mul_left, abs_of_pos (inv_pos.mpr ha), smul_eq_mul]

theorem neutralIV100Affine_mass (a b : ℝ) (ha : 0 < a) :
    ‖(neutralIV100Affine a b ha).toLp 2 volume‖^2 =
      a⁻¹ * ‖neutralIV097Schwartz.toLp 2 volume‖^2 := by
  rw [← neutralIV098Mass_integral (neutralIV100Affine a b ha),
    ← neutralIV098Mass_integral neutralIV097Schwartz]
  change (∫ x : ℝ, ‖neutralIV097Schwartz (a*x+b)‖^2) =
    a⁻¹ * ∫ x : ℝ, ‖neutralIV097Schwartz x‖^2
  exact neutralIV100Affine_integral (fun x : ℝ => ‖neutralIV097Schwartz x‖^2) a b ha

theorem neutralIV100Affine_energy (a b : ℝ) (ha : 0 < a) :
    neutralIV096DerivativeEnergy (neutralIV100Affine a b ha) =
      a * neutralIV096DerivativeEnergy neutralIV097Schwartz := by
  unfold neutralIV096DerivativeEnergy
  simp_rw [neutralIV100Affine_derivative, neutralIV097Schwartz_derivative]
  simp only [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_pos ha, mul_pow]
  calc
    _ = ∫ x : ℝ, a^2 * |neutralIV097PlateauDerivative (a*x+b)|^2 := by
      apply integral_congr_ae
      exact Filter.Eventually.of_forall fun x => mul_comm _ _
    _ = a^2 * (a⁻¹ * ∫ x : ℝ, |neutralIV097PlateauDerivative x|^2) := by
      rw [integral_const_mul, neutralIV100Affine_integral
        (fun x : ℝ => |neutralIV097PlateauDerivative x|^2) a b ha]
    _ = _ := by field_simp [ha.ne'] <;> ring

theorem neutralIV100Affine_energy_ratio (a b : ℝ) (ha : 0 < a) :
    neutralIV096DerivativeEnergy (neutralIV100Affine a b ha) ≤
      (16000000*a^2) * ‖(neutralIV100Affine a b ha).toLp 2 volume‖^2 := by
  rw [neutralIV100Affine_energy, neutralIV100Affine_mass]
  have h : neutralIV096DerivativeEnergy neutralIV097Schwartz ≤
      16000000 * ‖neutralIV097Schwartz.toLp 2 volume‖^2 := by
    linarith [neutralIV098Schwartz_energy_upper, neutralIV097Schwartz_mass_lower]
  calc
    _ ≤ a * (16000000 * ‖neutralIV097Schwartz.toLp 2 volume‖^2) :=
      mul_le_mul_of_nonneg_left h ha.le
    _ = _ := by field_simp [ha.ne'] <;> ring

theorem neutralIV100Affine_mass_pos (a b : ℝ) (ha : 0 < a) :
    0 < ‖(neutralIV100Affine a b ha).toLp 2 volume‖^2 := by
  rw [neutralIV100Affine_mass]
  exact mul_pos (inv_pos.mpr ha)
    (lt_of_lt_of_le (by norm_num) neutralIV097Schwartz_mass_lower)

/-- Use k equal cells of the already certified right plateau interval.
At each cell boundary both adjacent plateaus and their derivatives vanish. -/
def neutralIV100PackShift (k i : ℕ) : ℝ :=
  1099/1000 - (k:ℝ)*(1099/1000-3/4000) - (2*(i:ℝ)+1)*(3/4000)

theorem neutralIV100Pack_window (k i : ℕ) (x : ℝ)
    (h : |(k:ℝ)*x+neutralIV100PackShift k i-1099/1000| < (3/4000:ℝ)) :
    (2*(i:ℝ))*(3/4000) < (k:ℝ)*(x-(1099/1000-3/4000)) ∧
      (k:ℝ)*(x-(1099/1000-3/4000)) < (2*(i:ℝ)+2)*(3/4000) := by
  unfold neutralIV100PackShift at h
  obtain ⟨hl,hu⟩ := abs_lt.mp h
  constructor <;> linarith

theorem neutralIV100Pack_nonoverlap (k i j : ℕ) (x : ℝ) (hij : i ≠ j) :
    (3/4000:ℝ) ≤ |(k:ℝ)*x+neutralIV100PackShift k i-1099/1000| ∨
    (3/4000:ℝ) ≤ |(k:ℝ)*x+neutralIV100PackShift k j-1099/1000| := by
  by_contra h
  push_neg at h
  obtain ⟨hiL,hiU⟩ := neutralIV100Pack_window k i x h.1
  obtain ⟨hjL,hjU⟩ := neutralIV100Pack_window k j x h.2
  rcases lt_or_gt_of_ne hij with hij' | hji'
  · have hh : (i:ℝ)+1 ≤ (j:ℝ) := by exact_mod_cast (Nat.succ_le_of_lt hij')
    linarith
  · have hh : (j:ℝ)+1 ≤ (i:ℝ) := by exact_mod_cast (Nat.succ_le_of_lt hji')
    linarith

theorem neutralIV100Pack_containment (k i : ℕ) (hk : 0 < k) (hi : i < k)
    (x : ℝ)
    (h : |(k:ℝ)*x+neutralIV100PackShift k i-1099/1000| < (3/4000:ℝ)) :
    1099/1000-3/4000 < x ∧ x < 1099/1000+3/4000 := by
  have hkp : (0:ℝ) < (k:ℝ) := by exact_mod_cast hk
  have hip : (i:ℝ)+1 ≤ (k:ℝ) := by exact_mod_cast (Nat.succ_le_of_lt hi)
  have hin : (0:ℝ) ≤ (i:ℝ) := by positivity
  obtain ⟨hl,hu⟩ := neutralIV100Pack_window k i x h
  constructor
  · by_contra hnot
    have hbad : (k:ℝ)*(x-(1099/1000-3/4000)) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos hkp.le (sub_nonpos.mpr (le_of_not_gt hnot))
    linarith
  · by_contra hnot
    have hbad := mul_le_mul_of_nonneg_left
      (show (6/4000:ℝ) ≤ x-(1099/1000-3/4000) by linarith [le_of_not_gt hnot]) hkp.le
    linarith


/-- Each cell is a concrete affine pullback of the original plateau. -/
def neutralIV100Carrier (k : ℕ) (hk : 0 < k) (i : Fin k) : 𝓢(ℝ,ℂ) :=
  neutralIV100Affine (k:ℝ) (neutralIV100PackShift k i.val) (by exact_mod_cast hk)

theorem neutralIV100Carrier_collars (k : ℕ) (hk : 0 < k) (i : Fin k) :
    neutralNF735InOriginalCollars (neutralIV100Carrier k hk i) := by
  intro x hx
  have hz : (3/4000:ℝ) ≤ |(k:ℝ)*x+neutralIV100PackShift k i.val-1099/1000| := by
    by_contra h
    obtain ⟨hl,hu⟩ := neutralIV100Pack_containment k i.val hk i.isLt x (lt_of_not_ge h)
    apply hx
    unfold neutralNF543OriginalCollars
    right
    constructor <;> linarith
  change (neutralIV097Plateau ((k:ℝ)*x+neutralIV100PackShift k i.val) : ℂ) = 0
  simp [neutralIV097Plateau_zero _ hz]

theorem neutralIV100Carrier_disjoint (k : ℕ) (hk : 0 < k) :
    neutralIV099Disjoint (Finset.univ : Finset (Fin k))
      (fun i => (neutralIV100Carrier k hk i : ℝ → ℂ)) := by
  intro i hi j hj hij x
  have hne : i.val ≠ j.val := fun h => hij (Fin.ext h)
  rcases neutralIV100Pack_nonoverlap k i.val j.val x hne with h | h
  · left
    change (neutralIV097Plateau ((k:ℝ)*x+neutralIV100PackShift k i.val) : ℂ) = 0
    simp [neutralIV097Plateau_zero _ h]
  · right
    change (neutralIV097Plateau ((k:ℝ)*x+neutralIV100PackShift k j.val) : ℂ) = 0
    simp [neutralIV097Plateau_zero _ h]

theorem neutralIV100Carrier_derivative_disjoint (k : ℕ) (hk : 0 < k) :
    neutralIV099Disjoint (Finset.univ : Finset (Fin k))
      (fun i => deriv (neutralIV100Carrier k hk i : ℝ → ℂ)) := by
  intro i hi j hj hij x
  have hne : i.val ≠ j.val := fun h => hij (Fin.ext h)
  rcases neutralIV100Pack_nonoverlap k i.val j.val x hne with h | h
  · left
    change deriv (neutralIV100Carrier k hk i : ℝ → ℂ) x = 0
    unfold neutralIV100Carrier
    rw [neutralIV100Affine_derivative]
    simp [neutralIV097PlateauDerivative_zero _ h]
  · right
    change deriv (neutralIV100Carrier k hk j : ℝ → ℂ) x = 0
    unfold neutralIV100Carrier
    rw [neutralIV100Affine_derivative]
    simp [neutralIV097PlateauDerivative_zero _ h]

theorem neutralIV100Carrier_energy_ratio (k : ℕ) (hk : 0 < k) (i : Fin k) :
    neutralIV096DerivativeEnergy (neutralIV100Carrier k hk i) ≤
      (16000000*(k:ℝ)^2) * ‖(neutralIV100Carrier k hk i).toLp 2 volume‖^2 :=
  neutralIV100Affine_energy_ratio (k:ℝ) (neutralIV100PackShift k i.val) (by exact_mod_cast hk)

theorem neutralIV100Carrier_mass_pos (k : ℕ) (hk : 0 < k) (i : Fin k) :
    0 < ‖(neutralIV100Carrier k hk i).toLp 2 volume‖^2 :=
  neutralIV100Affine_mass_pos (k:ℝ) (neutralIV100PackShift k i.val) (by exact_mod_cast hk)

def neutralIV100Packed (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) : 𝓢(ℝ,ℂ) :=
  neutralIV099Sector Finset.univ (neutralIV100Carrier k hk) c

theorem neutralIV100Packed_mass_zero_iff (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    ‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 = 0 ↔ ∀ i, c i = 0 := by
  unfold neutralIV100Packed
  rw [neutralIV099Sector_mass_zero_iff Finset.univ (neutralIV100Carrier k hk) c
    (neutralIV100Carrier_disjoint k hk)
    (fun i hi => neutralIV100Carrier_mass_pos k hk i)]
  simp

theorem neutralIV100Packed_margin (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) (N : ℕ) :
    ((2/5:ℝ) - (16000000*(k:ℝ)^2) / ((N:ℝ)+1)^2) *
      ‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal 10 N (neutralIV100Packed k hk c) := by
  exact neutralIV099Sector_margin Finset.univ (neutralIV100Carrier k hk) c
    (16000000*(k:ℝ)^2) 10 N
    (fun i hi => neutralIV100Carrier_collars k hk i)
    (neutralIV100Carrier_disjoint k hk) (neutralIV100Carrier_derivative_disjoint k hk)
    (fun i hi => neutralIV100Carrier_energy_ratio k hk i)
    (by exact_mod_cast neutralIV098ArithmeticCutoff)

theorem neutralIV100Cutoff_budget (k N : ℕ) (hN : 8945*k ≤ N) :
    (16000000:ℝ)*(k:ℝ)^2 ≤ ((N:ℝ)+1)^2 / 5 := by
  have hkn : (8945:ℝ)*(k:ℝ) ≤ (N:ℝ) := by exact_mod_cast hN
  have hkp : (0:ℝ) ≤ (k:ℝ) := by positivity
  have hsq : ((8945:ℝ)*(k:ℝ))^2 ≤ ((N:ℝ)+1)^2 :=
    pow_le_pow_left₀ (by positivity) (by linarith) 2
  have hc : (16000000:ℝ)*(k:ℝ)^2 ≤ ((8945:ℝ)*(k:ℝ))^2/5 := by
    nlinarith only [sq_nonneg (k:ℝ)]
  linarith

theorem neutralIV100Packed_cutoff (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ)
    (N : ℕ) (hN : 8945*k ≤ N) :
    (1/5:ℝ) * ‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal 10 N (neutralIV100Packed k hk c) := by
  exact neutralIV099Sector_cutoff Finset.univ (neutralIV100Carrier k hk) c
    (16000000*(k:ℝ)^2) 10 N
    (fun i hi => neutralIV100Carrier_collars k hk i)
    (neutralIV100Carrier_disjoint k hk) (neutralIV100Carrier_derivative_disjoint k hk)
    (fun i hi => neutralIV100Carrier_energy_ratio k hk i)
    (by exact_mod_cast neutralIV098ArithmeticCutoff)
    (neutralIV100Cutoff_budget k N hN)

#print axioms neutralIV100Affine_compact
#print axioms neutralIV100Affine_hasDerivAt
#print axioms neutralIV100Affine_derivative
#print axioms neutralIV100Affine_integral
#print axioms neutralIV100Affine_mass
#print axioms neutralIV100Affine_energy
#print axioms neutralIV100Affine_energy_ratio
#print axioms neutralIV100Affine_mass_pos
#print axioms neutralIV100Pack_window
#print axioms neutralIV100Pack_nonoverlap
#print axioms neutralIV100Pack_containment
#print axioms neutralIV100Carrier_collars
#print axioms neutralIV100Carrier_disjoint
#print axioms neutralIV100Carrier_derivative_disjoint
#print axioms neutralIV100Carrier_energy_ratio
#print axioms neutralIV100Carrier_mass_pos
#print axioms neutralIV100Packed_mass_zero_iff
#print axioms neutralIV100Packed_margin
#print axioms neutralIV100Cutoff_budget
#print axioms neutralIV100Packed_cutoff

end
end WeilDefect
