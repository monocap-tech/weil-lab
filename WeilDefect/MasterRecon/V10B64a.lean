import WeilDefect.MasterRecon.V10B17Defs
import WeilDefect.MasterRecon.V10B61a

/-! Exact original retained-space attachment. The original adjoint bank
is unchanged; neither the tail estimate nor physical A/R is assumed. -/
namespace WeilDefect.MasterRecon.V10B64a
open MeasureTheory
open scoped InnerProduct
open V08I (logCarrier physicalInclusion)
open V08K (supportMeasure)
open V10B17a (poleDifference)
open V10B13a (moment)
open V10B33a (legendre)
open V10B47c (load)

noncomputable def constraints : Fin 15 ⊕ Unit → logCarrier (1/4) →L[ℂ] ℂ :=
  Sum.elim (fun j => moment (1/4) (by norm_num) j.val)
    (fun _ => poleDifference (1/4) (by norm_num))

theorem bank_identity (i : Fin 15 ⊕ Unit) :
    V10B17b.bank i = (constraints i).adjoint 1 := by
  cases i <;> rfl

theorem retained_original_iff (g : logCarrier (1/4)) :
    g ∈ V10B17b.retainedᗮ ↔
      (∀ j<15, moment (1/4) (by norm_num) j g=0) ∧
      poleDifference (1/4) (by norm_num) g=0 := by
  have hb : V10B17b.bank = fun i => (constraints i).adjoint 1 :=
    funext bank_identity
  unfold V10B17b.retained
  rw [hb, V10B50a.adjoint_span_iff constraints g]
  constructor
  · intro h
    exact ⟨fun j hj => h (Sum.inl ⟨j,hj⟩), h (Sum.inr ())⟩
  · rintro ⟨hm,hp⟩ i
    cases i with
    | inl j => exact hm j.val j.isLt
    | inr u => exact hp

theorem retained_literal_iff (g : logCarrier (1/4)) :
    g ∈ V10B17b.retainedᗮ ↔
      (∀ j<15, (∫ x, (legendre j (2*x+1/2):ℂ)*
        physicalInclusion (1/4) g x ∂supportMeasure (1/4))=0) ∧
      (∫ x, (Complex.ofReal (load (2*x+1/2)))*
        physicalInclusion (1/4) g x ∂supportMeasure (1/4))=0 := by
  rw [retained_original_iff]
  constructor
  · rintro ⟨hm,hp⟩
    exact ⟨(V10B52b.original_moment_kernel g).mp hm,
      (V10B61a.literal_pole_zero_iff g hm).mp hp⟩
  · rintro ⟨hl,hq⟩
    have hm := (V10B52b.original_moment_kernel g).mpr hl
    exact ⟨hm,(V10B61a.literal_pole_zero_iff g hm).mpr hq⟩

end WeilDefect.MasterRecon.V10B64a

#print axioms WeilDefect.MasterRecon.V10B64a.bank_identity
#print axioms WeilDefect.MasterRecon.V10B64a.retained_original_iff
#print axioms WeilDefect.MasterRecon.V10B64a.retained_literal_iff
