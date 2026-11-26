import WeilDefect.Arithmetic.ActualZetaIV130OriginalCorrectedMixed
import WeilDefect.Arithmetic.ActualZetaIV129OriginalFiniteHead
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap

/-- Exact variational loss, on the actual original smooth tail. No
existence of a smooth minimizing response is assumed. -/
def neutralIV131Loss (k : ℕ) (hk : 0 < k) (h z : 𝓢(ℝ,ℂ)) : ℝ :=
  -2*(neutralIV130Mixed k hk h z).re - neutralIV107SchurEnergy k hk z

def neutralIV131LossSet (k : ℕ) (hk : 0 < k) (Z : Submodule ℂ (𝓢(ℝ,ℂ)))
    (h : 𝓢(ℝ,ℂ)) : Set ℝ :=
  Set.range (fun z : Z => neutralIV131Loss k hk h z.val)

def neutralIV131Penalty (k : ℕ) (hk : 0 < k) (Z : Submodule ℂ (𝓢(ℝ,ℂ)))
    (h : 𝓢(ℝ,ℂ)) : ℝ :=
  sSup (neutralIV131LossSet k hk Z h)

/-- Scalar square completion bounds the variational payment. -/
theorem neutralIV131Scalar_payment (eta C m b q : ℝ) (he : 0 < eta)
    (hb : -b ≤ C*m) (hq : eta*m^2 ≤ q) :
    -2*b-q ≤ C^2/eta := by
  have hs : (2*C*m-eta*m^2)*eta ≤ C^2 := by
    nlinarith only [sq_nonneg (eta*m-C)]
  have hpay := (le_div_iff₀ he).2 hs
  linarith only [hb,hq,hpay]

theorem neutralIV131Loss_le (k : ℕ) (hk : 0 < k) (h z : 𝓢(ℝ,ℂ))
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hz : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : eta*‖z.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z) :
    neutralIV131Loss k hk h z ≤
      (neutralIV109RowConstant (11/10:ℝ) (h-neutralIV130ResponseVector k hk h))^2/eta := by
  have hr := neutralIV130Mixed_physical_bound k hk h z hh hz
  have hb := (neg_le_abs (neutralIV130Mixed k hk h z).re).trans
    ((Complex.abs_re_le_norm _).trans hr)
  exact neutralIV131Scalar_payment eta _ _ _ _ he hb hc

theorem neutralIV131Loss_bdd (k : ℕ) (hk : 0 < k) (Z : Submodule ℂ (𝓢(ℝ,ℂ)))
    (h : 𝓢(ℝ,ℂ))
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hz : ∀ z : Z, ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z.val x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : Z, eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val) :
    BddAbove (neutralIV131LossSet k hk Z h) := by
  refine ⟨(neutralIV109RowConstant (11/10:ℝ)
    (h-neutralIV130ResponseVector k hk h))^2/eta, ?_⟩
  rintro r ⟨z,rfl⟩
  exact neutralIV131Loss_le k hk h z.val hh (hz z) eta he (hc z)

theorem neutralIV131Penalty_le (k : ℕ) (hk : 0 < k) (Z : Submodule ℂ (𝓢(ℝ,ℂ)))
    (h : 𝓢(ℝ,ℂ))
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hz : ∀ z : Z, ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z.val x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : Z, eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val) :
    neutralIV131Penalty k hk Z h ≤
      (neutralIV109RowConstant (11/10:ℝ) (h-neutralIV130ResponseVector k hk h))^2/eta := by
  unfold neutralIV131Penalty
  apply csSup_le
  · exact ⟨neutralIV131Loss k hk h (0 : Z).val, ⟨0,rfl⟩⟩
  · rintro r ⟨z,rfl⟩
    exact neutralIV131Loss_le k hk h z.val hh (hz z) eta he (hc z)

/-- Exact second Schur sign equivalence on a single head fibre.
The penalty is a supremum over the original tail, not a trial solve. -/
theorem neutralIV131Fibre_iff (k : ℕ) (hk : 0 < k) (Z : Submodule ℂ (𝓢(ℝ,ℂ)))
    (h : 𝓢(ℝ,ℂ))
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hz : ∀ z : Z, ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z.val x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : Z, eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val) :
    (∀ z : Z, 0 ≤ neutralIV107SchurEnergy k hk (h+z.val)) ↔
      neutralIV131Penalty k hk Z h ≤ neutralIV107SchurEnergy k hk h := by
  constructor
  · intro hp
    unfold neutralIV131Penalty
    apply csSup_le
    · exact ⟨neutralIV131Loss k hk h (0 : Z).val, ⟨0,rfl⟩⟩
    · rintro r ⟨z,rfl⟩
      have hs := hp z
      rw [neutralIV130Schur_add k hk h z.val hh (hz z)] at hs
      unfold neutralIV131Loss
      linarith only [hs]
  · intro hp z
    have hb := neutralIV131Loss_bdd k hk Z h hh hz eta he hc
    have hl : neutralIV131Loss k hk h z.val ≤ neutralIV131Penalty k hk Z h := by
      exact le_csSup hb ⟨z,rfl⟩
    have hq := hl.trans hp
    unfold neutralIV131Loss at hq
    rw [neutralIV130Schur_add k hk h z.val hh (hz z)]
    linarith only [hq]

/-- The literal tail submodule, in the original Schwartz space. -/
def neutralIV131Tail (k : ℕ) (hk : 0 < k) (N : ℕ) : Submodule ℂ (𝓢(ℝ,ℂ)) :=
  neutralIV129Complement k hk ⊓ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N)

theorem neutralIV131Tail_coercive_exists (k : ℕ) (hk : 0 < k) (eta : ℝ) :
    ∃ N : ℕ, 0 < N ∧ ∀ z : neutralIV131Tail k hk N,
      eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val := by
  obtain ⟨N,hN,hc⟩ := neutralIV128Schur_coercive_tail_exists k hk eta
  refine ⟨N,hN,?_⟩
  intro z
  have hz := z.property
  change z.val ∈ neutralIV129Complement k hk ∧
    z.val ∈ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N) at hz
  have hn : neutralIV127CellNull (11/10:ℝ) N z.val :=
    (neutralIV129CellMap_zero_iff _ N z.val).1 (LinearMap.mem_ker.mp hz.2)
  exact hc z.val hz.1.1 hn

#print axioms neutralIV131Scalar_payment
#print axioms neutralIV131Loss_le
#print axioms neutralIV131Loss_bdd
#print axioms neutralIV131Penalty_le
#print axioms neutralIV131Fibre_iff
#print axioms neutralIV131Tail_coercive_exists

end
end WeilDefect
