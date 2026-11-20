import Mathlib.Tactic

namespace WeilDefect

/-! NF732: direct exact Fin 242 assembly from the eight independent original
coordinate ranges. Source-independent logical transfer: original physical
HD/A numerical gate facts must be supplied as eight verified proof inputs. -/

/-- Direct eight-range global certificate with no intermediate 31-block or
128-coordinate master dependency. The final range has 18 positions, not 32. -/
theorem neutralNF732AllFin242OfEightQuads
    (P : Fin 242 → Prop)
    (q000 : ∀ i : Fin 242, 0 ≤ i.val → i.val < 32 → P i)
    (q004 : ∀ i : Fin 242, 32 ≤ i.val → i.val < 64 → P i)
    (q008 : ∀ i : Fin 242, 64 ≤ i.val → i.val < 96 → P i)
    (q012 : ∀ i : Fin 242, 96 ≤ i.val → i.val < 128 → P i)
    (q016 : ∀ i : Fin 242, 128 ≤ i.val → i.val < 160 → P i)
    (q020 : ∀ i : Fin 242, 160 ≤ i.val → i.val < 192 → P i)
    (q024 : ∀ i : Fin 242, 192 ≤ i.val → i.val < 224 → P i)
    (q028 : ∀ i : Fin 242, 224 ≤ i.val → i.val < 242 → P i)
    : ∀ i : Fin 242, P i := by
  intro i
  by_cases h32 : i.val < 32
  · exact q000 i (by omega) h32
  by_cases h64 : i.val < 64
  · exact q004 i (by omega) h64
  by_cases h96 : i.val < 96
  · exact q008 i (by omega) h96
  by_cases h128 : i.val < 128
  · exact q012 i (by omega) h128
  by_cases h160 : i.val < 160
  · exact q016 i (by omega) h160
  by_cases h192 : i.val < 192
  · exact q020 i (by omega) h192
  by_cases h224 : i.val < 224
  · exact q024 i (by omega) h224
  exact q028 i (by omega) i.isLt

#print axioms neutralNF732AllFin242OfEightQuads

end WeilDefect
