import WeilDefect.Arithmetic.ActualZetaIV106E19KProjectionReserve

namespace WeilDefect
noncomputable section
open InnerProductSpace ContinuousLinearMap
open scoped BigOperators InnerProduct

/-- Projection is the identity on the kernel, with the original
adjoint and subtype conventions. -/
theorem neutralIV106E19KProject_self (k : ℕ) (hk : 0 < k)
    (x : neutralIV106E12Kernel k hk) :
    neutralIV106E19KProject k hk x.val = x := by
  let P := neutralIV106E19KProject k hk
  let d := P x.val-x
  have h : inner ℂ d d = 0 := by
    change inner ℂ d (P x.val-x) = 0
    rw [inner_sub_right]
    change inner ℂ d ((ContinuousLinearMap.adjoint
      (neutralIV106E12Kernel k hk).subtypeL) x.val) - inner ℂ d x = 0
    rw [adjoint_inner_right]
    change inner ℂ d.val x.val - inner ℂ d.val x.val = 0
    exact sub_self _
  exact sub_eq_zero.mp (inner_self_eq_zero.mp h)

/-- A row-span correction achieving the exact projection exists,
even for a redundant constraint bank. This is an existence result,
not a numerical evaluation of its coefficients. -/
theorem neutralIV106E19KAttainment (k : ℕ) (hk : 0 < k)
    (v : neutralIV106E13H) :
    ∃ d : neutralIV106E16Index k → ℂ,
      (neutralIV106E19KProject k hk v).val =
        v-(∑ j, d j • neutralIV106E14LiftedRow k hk j).val := by
  obtain ⟨x,y,hv⟩ := neutralIV106E13Split k hk v
  obtain ⟨d,hd⟩ := neutralIV106E14Synthesis k hk y
  refine ⟨d,?_⟩
  rw [hv,hd,map_add,neutralIV106E19KProject_self,
    neutralIV106E19KProject_finite,add_zero,add_sub_cancel_right]

/-- Exact full action Gram after an exact row correction. The pairings
are in the original logarithmic carrier, not physical L2. -/
theorem neutralIV106E19KAction_gram {J : Type*} [Fintype J]
    (k : ℕ) (hk : 0 < k) (z : J → neutralIV106E12Kernel k hk) :
    ∃ d : J → neutralIV106E16Index k → ℂ,
      ∀ a b,
      inner ℂ (neutralIV106E12Compressed k hk (z a))
        (neutralIV106E12Compressed k hk (z b)) =
      inner ℂ
        (neutralActualZetaLogWeilFormOperator (11/10) (z a).val -
          (∑ j, d a j • neutralIV106E14LiftedRow k hk j).val)
        (neutralActualZetaLogWeilFormOperator (11/10) (z b).val -
          (∑ j, d b j • neutralIV106E14LiftedRow k hk j).val) := by
  classical
  choose d hd using fun a : J => neutralIV106E19KAttainment k hk
    (neutralActualZetaLogWeilFormOperator (11/10) (z a).val)
  refine ⟨d,?_⟩
  intro a b
  change inner ℂ
    (neutralIV106E19KProject k hk
      (neutralActualZetaLogWeilFormOperator (11/10) (z a).val)).val
    (neutralIV106E19KProject k hk
      (neutralActualZetaLogWeilFormOperator (11/10) (z b).val)).val = _
  rw [hd a,hd b]

#print axioms neutralIV106E19KProject_self
#print axioms neutralIV106E19KAttainment
#print axioms neutralIV106E19KAction_gram
end
end WeilDefect
