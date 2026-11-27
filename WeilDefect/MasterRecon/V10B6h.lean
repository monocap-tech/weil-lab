import WeilDefect.MasterRecon.V10B6e
import WeilDefect.MasterRecon.V10B6g

/-! V10B6h: discharge reflection closure and multiplicity invariance
using the two independent analytic transport modules. -/
namespace WeilDefect.MasterRecon.V10B6h

open scoped ComplexConjugate

theorem strip_reflection_closed (ρ : ℂ) (hρ : V09D.stripZero ρ) :
    V09D.stripZero (V10A.reflect ρ) :=
  V10B6e.reflection_zero_of_conj
    (fun z hz => V10B6g.zeta_conjugate_value z (V10B6e.strip_ne_one hz)) ρ hρ

theorem strip_reflection_mult (ρ : ℂ) (hρ : V09D.stripZero ρ) :
    V09D.mult (V10A.reflect ρ) = V09D.mult ρ :=
  V10B6e.reflection_mult_of_conj_order
    (fun z hz => V10B6g.zeta_conjugate_order z (V10B6e.strip_ne_one hz)) ρ hρ

theorem strip_reflection_iff (ρ : ℂ) :
    V09D.stripZero (V10A.reflect ρ) ↔ V09D.stripZero ρ := by
  constructor
  · intro h
    simpa only [V10A.reflect_involution] using strip_reflection_closed _ h
  · exact strip_reflection_closed ρ

theorem strip_reflection_positive_mult (ρ : ℂ) (hρ : V09D.stripZero ρ) :
    0 < V09D.mult ρ ∧ V09D.mult (V10A.reflect ρ) = V09D.mult ρ :=
  ⟨V10B6g.strip_mult_positive ρ hρ,strip_reflection_mult ρ hρ⟩

end WeilDefect.MasterRecon.V10B6h

#print axioms WeilDefect.MasterRecon.V10B6h.strip_reflection_closed
#print axioms WeilDefect.MasterRecon.V10B6h.strip_reflection_mult
#print axioms WeilDefect.MasterRecon.V10B6h.strip_reflection_iff
#print axioms WeilDefect.MasterRecon.V10B6h.strip_reflection_positive_mult
