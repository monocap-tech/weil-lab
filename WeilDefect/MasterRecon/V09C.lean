import WeilDefect.MasterRecon.V09B
import Mathlib.NumberTheory.LSeries.ZetaZeros

/-! V09C: literal critical-line sampling receiver. The arithmetic density
hypothesis is explicit. No axiom or proof of the zeta zero-density theorem
is introduced here. -/
namespace WeilDefect.MasterRecon.V09C

open MeasureTheory Set Metric
open scoped Topology

def CriticalSample (z : ℂ) : Prop :=
  z.re = 0 ∧ 0 < z.im ∧ riemannZeta ((1 / 2 : ℂ) + z) = 0

def SuperlinearSupply (P : ℂ → Prop) : Prop :=
  ∀ L : ℝ, ∃ (T : ℝ) (S : Finset ℂ), 1 ≤ T ∧
    (∀ z ∈ S, P z ∧ ‖z‖ ≤ T) ∧ L * T < (S.card : ℝ)

/-- Move a supply centered at zero into the arbitrary-centered disks
required by the certified Jensen receiver. -/
theorem supply_arbitrary_center (P : ℂ → Prop) (hP : SuperlinearSupply P)
    (c : ℂ) (a b : ℝ) :
    ∃ (r : ℝ) (S : Finset ℂ), 0 < r ∧
      (∀ z ∈ S, z ∈ closedBall c r ∧ P z) ∧
      a + b * r < (S.card : ℝ) := by
  let L := |a| + |b| * (1 + ‖c‖) + 1
  obtain ⟨T, S, hT, hS, hlarge⟩ := hP L
  let r := T + ‖c‖
  have hr : 0 < r := by dsimp [r]; linarith [norm_nonneg c]
  refine ⟨r, S, hr, ?_, ?_⟩
  · intro z hz
    refine ⟨?_, (hS z hz).1⟩
    rw [mem_closedBall, dist_eq_norm]
    calc
      ‖z - c‖ ≤ ‖z‖ + ‖c‖ := norm_sub_le z c
      _ ≤ T + ‖c‖ := by linarith [(hS z hz).2]
      _ = r := rfl
  · have ha : a ≤ |a| * T := calc
      a ≤ |a| := le_abs_self _
      _ = |a| * 1 := by ring
      _ ≤ |a| * T := mul_le_mul_of_nonneg_left hT (abs_nonneg _)
    have hb : b * r ≤ |b| * r :=
      mul_le_mul_of_nonneg_right (le_abs_self _) hr.le
    have hc : ‖c‖ ≤ ‖c‖ * T := by
      simpa using mul_le_mul_of_nonneg_left hT (norm_nonneg c)
    have hrad : r ≤ (1 + ‖c‖) * T := by
      dsimp [r]
      nlinarith only [hc]
    have hbc := mul_le_mul_of_nonneg_left hrad (abs_nonneg b)
    have hle : a + b * r ≤ L * T := by
      dsimp [L]
      calc
        a + b * r ≤ |a| * T + |b| * ((1 + ‖c‖) * T) :=
          add_le_add ha (hb.trans hbc)
        _ ≤ (|a| + |b| * (1 + ‖c‖) + 1) * T := by
          nlinarith only [hT]
    exact hle.trans_lt hlarge

theorem critical_samples_unique (F : ℂ → ℂ) (hF : ∀ z, AnalyticAt ℂ F z)
    (A B : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B)
    (hg : ∀ z, ‖F z‖ ≤ Real.exp (A + B * ‖z‖))
    (hd : SuperlinearSupply CriticalSample)
    (hz : ∀ z, CriticalSample z → F z = 0) : F = 0 := by
  apply V09A.exponential_type_unique_of_superlinear_zeros F hF A B hA hB hg
  intro c a b
  obtain ⟨r, S, hr, hs, hlarge⟩ := supply_arbitrary_center CriticalSample hd c a b
  exact ⟨r, S, hr, fun z hzS => ⟨(hs z hzS).1, hz z (hs z hzS).2⟩, hlarge⟩

theorem critical_mellin_injective (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t)
    (hd : SuperlinearSupply CriticalSample)
    (hz : ∀ z, CriticalSample z →
      V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ) z = 0) : g = 0 := by
  let f := (V08I.physicalInclusion t g : ℝ → ℂ)
  have hs := V08I.physicalInclusion_support t g
  have hf : Integrable f := V08K.supported_integrable t _ hs
  have hzero : V07A.mellin f = 0 :=
    critical_samples_unique (V07A.mellin f)
      (V09B.mellin_entire t ht f hf hs)
      (∫ x, ‖f x‖) t (integral_nonneg fun _ => norm_nonneg _) ht
      (V09B.mellin_exponential_type t ht f hf hs) hd hz
  exact V09B.carrier_zero_of_mellin_zero t g hzero

end WeilDefect.MasterRecon.V09C

#print axioms WeilDefect.MasterRecon.V09C.supply_arbitrary_center
#print axioms WeilDefect.MasterRecon.V09C.critical_samples_unique
#print axioms WeilDefect.MasterRecon.V09C.critical_mellin_injective
