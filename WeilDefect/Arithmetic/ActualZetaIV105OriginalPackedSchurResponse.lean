import WeilDefect.Arithmetic.ActualZetaIV104OriginalPackedMassProjection
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-! Exact signed-energy response receiver on the original packed sector.
Response existence and residual Schur positivity are separate obligations.
The physical mass projection does not assert signed orthogonality. -/

theorem neutralIV105Packed_add (k : ℕ) (hk : 0 < k) (c d : Fin k → ℂ) :
    neutralIV100Packed k hk c + neutralIV100Packed k hk d =
      neutralIV100Packed k hk (fun i => c i + d i) := by
  ext x
  change neutralIV100Packed k hk c x + neutralIV100Packed k hk d x =
    neutralIV100Packed k hk (fun i => c i + d i) x
  simp only [neutralIV100Packed, neutralIV099Sector_apply, add_mul,
    Finset.sum_add_distrib]

theorem neutralIV105Packed_zero (k : ℕ) (hk : 0 < k) :
    neutralIV100Packed k hk (fun _ => (0 : ℂ)) = 0 := by
  ext x
  simp [neutralIV100Packed, neutralIV099Sector_apply]

/-- Exact completion using a response in the SAME original sector.
Only the real part is needed for the signed diagonal identity. -/
theorem neutralIV105Schur_identity (k : ℕ) (hk : 0 < k)
    (c d : Fin k → ℂ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hresponse : (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v).re =
      (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c)
        (neutralIV100Packed k hk d)).re) :
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c + v) =
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (fun i => c i + d i)) +
      (neutralIV101Q (11/10:ℝ) v -
        neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk d)) := by
  have hc := neutralIV009OriginalCollars_supported_window _
    (neutralIV101Packed_collars k hk c)
  have hd := neutralIV009OriginalCollars_supported_window _
    (neutralIV101Packed_collars k hk d)
  rw [← neutralIV105Packed_add k hk c d,
    neutralIV101Q_add _ _ v hc hv,
    neutralIV101Q_add _ _ _ hc hd, hresponse]
  ring

/-- A direction-dependent loss rather than the uniform scalar K² loss. -/
theorem neutralIV105Schur_lower (k : ℕ) (hk : 0 < k)
    (c d : Fin k → ℂ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hresponse : (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v).re =
      (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c)
        (neutralIV100Packed k hk d)).re) :
    (2/5:ℝ) * ‖(neutralIV100Packed k hk (fun i => c i + d i)).toLp 2 volume‖^2 +
      (neutralIV101Q (11/10:ℝ) v -
        neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk d)) ≤
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c + v) := by
  rw [neutralIV105Schur_identity k hk c d v hv hresponse]
  exact add_le_add_right (neutralIV101Packed_full_margin k hk (fun i => c i + d i)) _

/-- Fixed-window receiver. Every residual needs an actual signed response
and a nonnegative Schur remainder. Neither is asserted by this theorem. -/
theorem neutralIV105Window_nonneg_of_response (k : ℕ) (hk : 0 < k)
    (hresponse : ∀ v : 𝓢(ℝ,ℂ), neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      ∃ d : Fin k → ℂ,
        (∀ c : Fin k → ℂ,
          (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v).re =
            (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c)
              (neutralIV100Packed k hk d)).re) ∧
        neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk d) ≤
          neutralIV101Q (11/10:ℝ) v)
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) :
    0 ≤ neutralIV101Q (11/10:ℝ) s := by
  let v := neutralIV104Residual k hk s
  let c := neutralIV104Coefficient k hk s
  have hv := neutralIV104Residual_supported k hk s hs
  obtain ⟨d, hd, hschur⟩ := hresponse v
    (neutralIV104Residual_orthogonal k hk s) hv
  have h := neutralIV105Schur_lower k hk c d v hv (hd c)
  have hdecomp : neutralIV100Packed k hk c + v = s :=
    neutralIV104Decomposition k hk s
  rw [hdecomp] at h
  have hpos : 0 ≤ (2/5:ℝ) *
      ‖(neutralIV100Packed k hk (fun i => c i + d i)).toLp 2 volume‖^2 := by
    positivity
  linarith

#print axioms neutralIV105Packed_add
#print axioms neutralIV105Packed_zero
#print axioms neutralIV105Schur_identity
#print axioms neutralIV105Schur_lower
#print axioms neutralIV105Window_nonneg_of_response

end
end WeilDefect
