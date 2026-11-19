import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerCenters

namespace WeilDefect

/-! NF681: exact local dot receipts attach to the genuine global
cache once their row/column and result projections are proven.
Neither local products nor hashes alone imply global validity. -/

theorem neutralNF681HDGate_of_projection
    (s : NF626ScaledInputs) (c : NF626CenterCache) (i j : Fin 242)
    (hrow dcol : Fin 242 → ℤ) (z : ℤ)
    (hh : hrow = s.H i) (hd : dcol = fun k => s.D k j)
    (hz : z = c.HD i j) (hp : z = neutralNF626Dot hrow dcol) :
    c.HDGate s i j = true := by
  unfold NF626CenterCache.HDGate
  apply decide_eq_true
  rw [← hz, ← hh, ← hd]
  exact hp

theorem neutralNF681AGate_of_projection
    (s : NF626ScaledInputs) (c : NF626CenterCache) (i j : Fin 242)
    (dcol hdcol : Fin 242 → ℤ) (z : ℤ)
    (hd : dcol = fun k => s.D k i) (hh : hdcol = fun k => c.HD k j)
    (hz : z = c.A i j) (hp : z = neutralNF626Dot dcol hdcol) :
    c.AGate s i j = true := by
  unfold NF626CenterCache.AGate
  apply decide_eq_true
  rw [← hz, ← hd, ← hh]
  exact hp

/-- The exact already-verified global product identities can be
assembled into the incumbent Boolean without recomputing them. -/
theorem neutralNF681CacheCheck_of_valid
    (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hv : c.Valid s) : c.check s = true := by
  unfold NF626CenterCache.check NF626ScaledInputs.wCheck
  simp only [Bool.and_eq_true]
  refine ⟨?_, ?_, ?_, ?_⟩
  · apply List.all_eq_true.mpr
    intro j _
    exact decide_eq_true (hv.1 j)
  · apply List.all_eq_true.mpr
    intro i _
    apply List.all_eq_true.mpr
    intro j _
    exact decide_eq_true (hv.2.1 i j)
  · apply List.all_eq_true.mpr
    intro i _
    apply List.all_eq_true.mpr
    intro j _
    exact decide_eq_true (hv.2.2.1 i j)
  · apply List.all_eq_true.mpr
    intro i _
    exact decide_eq_true (hv.2.2.2 i)

#print axioms neutralNF681HDGate_of_projection
#print axioms neutralNF681AGate_of_projection
#print axioms neutralNF681CacheCheck_of_valid

end WeilDefect
