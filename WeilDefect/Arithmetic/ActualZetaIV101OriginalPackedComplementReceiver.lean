import WeilDefect.Arithmetic.ActualZetaIV100OriginalAffineCollarPacking
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate

/-- The literal complete signed mixed explicit formula, not an auxiliary PSD form. -/
def neutralIV101Mixed (a : ℝ) (u v : 𝓢(ℝ,ℂ)) : ℂ :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a (u.toLp 2 volume) (v.toLp 2 volume))

def neutralIV101Q (a : ℝ) (u : 𝓢(ℝ,ℂ)) : ℝ :=
  (neutralIV101Mixed a u u).re

/-- Physical mass orthogonality to the entire IV100 packed sector.
This does not assert orthogonality for the signed Weil pairing. -/
def neutralIV101MassComplement (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) : Prop :=
  ∀ c : Fin k → ℂ, inner ℂ ((neutralIV100Packed k hk c).toLp 2 volume)
    (v.toLp 2 volume) = 0

/-- Exact two-vector polarization from IV008/IV009. All mixed signed
arithmetic, pole and Gamma terms remain in the literal source. -/
theorem neutralIV101Q_add (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Q a (u+v) =
      neutralIV101Q a u + 2*(neutralIV101Mixed a u v).re +
        neutralIV101Q a v := by
  let s : Fin 2 → 𝓢(ℝ,ℂ) := ![u,v]
  have hs : ∀ i : Fin 2, ∀ x : ℝ, x ∉ Set.Icc (-a) a → s i x = 0 := by
    intro i x hx
    fin_cases i
    · simpa [s] using hu x hx
    · simpa [s] using hv x hx
  have hS : neutralIV009PhysicalSchwartzSum s (fun _ => 1) = u+v := by
    simp [neutralIV009PhysicalSchwartzSum, Fin.sum_univ_two, s]
  have hE : neutralIV007OriginalMixedEnergy a s (fun _ => 1) =
      neutralIV101Mixed a u u + neutralIV101Mixed a u v +
        (neutralIV101Mixed a v u + neutralIV101Mixed a v v) := by
    simp [neutralIV007OriginalMixedEnergy, Fin.sum_univ_two, s,
      neutralIV007OriginalMixedEntry, neutralIV101Mixed]
  have hH : conj (neutralIV101Mixed a u v) = neutralIV101Mixed a v u := by
    simpa [s, neutralIV007OriginalMixedEntry, neutralIV101Mixed] using
      neutralIV008OriginalMixedEntry_hermitian a s hs 0 1
  have hHR := congrArg Complex.re hH
  simp only [Complex.conj_re] at hHR
  have hP := neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
    a s (fun _ => 1) hs
  rw [hS, hE] at hP
  have hR := congrArg Complex.re hP
  simp only [Complex.add_re] at hR
  change (neutralIV101Mixed a u u).re + (neutralIV101Mixed a u v).re +
    ((neutralIV101Mixed a v u).re + (neutralIV101Mixed a v v).re) =
      neutralIV101Q a (u+v) at hR
  unfold neutralIV101Q
  change (neutralIV101Mixed a (u+v) (u+v)).re =
    (neutralIV101Mixed a u u).re + 2*(neutralIV101Mixed a u v).re +
      (neutralIV101Mixed a v v).re
  change _ = (neutralIV101Mixed a (u+v) (u+v)).re at hR
  linarith

/-- The packed sector lies in the actual frozen collars. -/
theorem neutralIV101Packed_collars (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    neutralNF735InOriginalCollars (neutralIV100Packed k hk c) := by
  unfold neutralIV100Packed
  exact neutralIV099Sector_collars Finset.univ (neutralIV100Carrier k hk) c
    (fun i _ => neutralIV100Carrier_collars k hk i)

/-- Full, untruncated original signed diagonal margin. The 2/5 margin is
inherited from NF600, not a new global coercivity assertion. -/
theorem neutralIV101Packed_full_margin (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    (2/5:ℝ)*‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 ≤
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c) := by
  change (2/5:ℝ)*‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 ≤
    neutralNF598SmoothWeil (neutralIV100Packed k hk c)
  exact neutralNF600SmoothCollarLower _ (neutralIV101Packed_collars k hk c)

/-- Quantitative scalar mixed-loss receiver on the original full form.
The mixed estimate is explicitly a premise, not an established bound.
The constant 5/2 is the inverse of the proved 2/5 diagonal margin. -/
theorem neutralIV101Packed_mixed_loss
    (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) (v : 𝓢(ℝ,ℂ)) (K : ℝ)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hmix : |(neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v).re| ≤
      K * ‖(neutralIV100Packed k hk c).toLp 2 volume‖ * ‖v.toLp 2 volume‖) :
    neutralIV101Q (11/10:ℝ) v - (5/2:ℝ)*K^2*‖v.toLp 2 volume‖^2 ≤
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c + v) := by
  have hwin := neutralIV009OriginalCollars_supported_window
    (neutralIV100Packed k hk c) (neutralIV101Packed_collars k hk c)
  rw [neutralIV101Q_add (11/10:ℝ) _ v hwin hv]
  have hu := neutralIV101Packed_full_margin k hk c
  have hcross := (abs_le.mp hmix).1
  nlinarith only [hu, hcross,
    sq_nonneg ((2/5:ℝ)*‖(neutralIV100Packed k hk c).toLp 2 volume‖ -
      K*‖v.toLp 2 volume‖)]

/-- Uniform complement receiver: still requires the actual mixed and
complement estimates. No claim of covering larger windows or all tests. -/
theorem neutralIV101Packed_complement_nonneg (k : ℕ) (hk : 0 < k) (K : ℝ)
    (hmix : ∀ (c : Fin k → ℂ) (v : 𝓢(ℝ,ℂ)),
      neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      |(neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v).re| ≤
        K * ‖(neutralIV100Packed k hk c).toLp 2 volume‖ * ‖v.toLp 2 volume‖)
    (hcomp : ∀ v : 𝓢(ℝ,ℂ), neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      (5/2:ℝ)*K^2*‖v.toLp 2 volume‖^2 ≤ neutralIV101Q (11/10:ℝ) v)
    (c : Fin k → ℂ) (v : 𝓢(ℝ,ℂ)) (horth : neutralIV101MassComplement k hk v)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    0 ≤ neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c + v) := by
  exact le_trans (sub_nonneg.mpr (hcomp v horth hv))
    (neutralIV101Packed_mixed_loss k hk c v K hv (hmix c v horth hv))

#print axioms neutralIV101Q_add
#print axioms neutralIV101Packed_collars
#print axioms neutralIV101Packed_full_margin
#print axioms neutralIV101Packed_mixed_loss
#print axioms neutralIV101Packed_complement_nonneg

end
end WeilDefect
