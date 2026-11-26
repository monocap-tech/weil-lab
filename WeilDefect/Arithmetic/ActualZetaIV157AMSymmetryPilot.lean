import WeilDefect.Arithmetic.ActualZetaIV146AMCellData

namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- Small bounded pilot: direct literal symmetry, using the existing
weight lookup, not a separate replacement table. -/
def neutralIV157SymBlock (k : ℕ) : Bool :=
  (List.range 64).all (fun j =>
    neutralIV146Value ((64*k+j:ℕ):ℤ) ==
      neutralIV146Value (16383-((64*k+j:ℕ):ℤ)))

theorem neutralIV157SymPilot : neutralIV157SymBlock 0 = true := by decide

#print axioms neutralIV157SymPilot
end WeilDefect
